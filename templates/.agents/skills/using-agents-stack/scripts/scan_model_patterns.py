#!/usr/bin/env python3
"""Scan code for known open-source model failure patterns.

Patterns are model-agnostic: they detect structural defects that weaker LLMs
systematically produce regardless of domain. Hardcoded, not prompt-guided --
the same model that wrote `_ =` will approve it in self-review.

Usage:
    python scan_model_patterns.py <target-dir> [--repo-root <root>] [--format json|text]
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Pattern definitions
# ---------------------------------------------------------------------------
# Each rule = (id, severity, description, regex, file_globs)
# file_globs: which files to scan (e.g. ["*.go", "*.py"]); empty = all text files

RULES: list[dict[str, Any]] = [
    {
        "id": "PAT-001",
        "severity": "P1",
        "axis": "implementation_discipline",
        "name": "silent_error_discard",
        "description": "Error return value silently discarded with `_ =`",
        "pattern": re.compile(r"^\s*_\s*=\s*\w+\([^)]*\)", re.MULTILINE),
        "file_globs": ["*.go"],
        "fix_hint": "Propagate the error with `if err != nil { return ... }` or write an audit entry.",
    },
    {
        "id": "PAT-002",
        "severity": "P2",
        "axis": "implementation_discipline",
        "name": "annotated_defect",
        "description": "Known defect documented in comment instead of fixed",
        "pattern": re.compile(
            r"(?:^\s*(?://|#|/\*)\s*)(TODO|FIXME|HACK|For production|not yet implemented|Simplified|workaround)",
            re.IGNORECASE,
        ),
        "file_globs": ["*.go", "*.py", "*.ts", "*.tsx", "*.js", "*.rs"],
        "fix_hint": "Fix the defect or, if deferred, record it in the contract's deferred-work section, not in a code comment.",
    },
    {
        "id": "PAT-003",
        "severity": "P2",
        "axis": "implementation_discipline",
        "name": "hand_parsed_format",
        "description": "Manual string-splitting parser for a format that has a library available",
        "pattern": re.compile(
            r'strings\.SplitN?\([^,]+,\s*"[:\|=]"',
        ),
        "file_globs": ["*.go"],
        "fix_hint": "Check go.mod for an existing parser library (yaml, json, toml). Prefer `encoding/json`, `gopkg.in/yaml.v3`, etc.",
    },
    {
        "id": "PAT-004",
        "severity": "P1",
        "axis": "implementation_discipline",
        "name": "missing_defer_close",
        "description": "Resource acquired without corresponding defer close/rollback",
        "pattern": re.compile(
            r"(os\.Open|sql\.Open|http\.Get|db\.Begin|tx\.Prepare)\(",
        ),
        "file_globs": ["*.go"],
        "requires_context": True,  # needs nearby defer check
        "context_lines": 10,
        "fix_hint": "Add `defer x.Close()` or `defer tx.Rollback()` immediately after acquisition.",
    },
    {
        "id": "PAT-005",
        "severity": "P2",
        "axis": "design_completeness",
        "name": "unstructured_error",
        "description": "Error returned as plain map[string]string instead of structured type",
        "pattern": re.compile(
            r'map\[string\]string\{"error":',
        ),
        "file_globs": ["*.go"],
        "fix_hint": "Define a structured error type with typed fields (code, recovery_hint, timestamp) so callers can handle it programmatically.",
    },
    {
        "id": "PAT-006",
        "severity": "P1",
        "axis": "design_completeness",
        "name": "single_layer_ip_extraction",
        "description": "Client IP extracted from RemoteAddr only, no proxy header fallback",
        "pattern": re.compile(
            r"r\.RemoteAddr",
        ),
        "file_globs": ["*.go"],
        "requires_context": True,
        "context_lines": 5,
        "fix_hint": "Check X-Forwarded-For, X-Real-IP, then SplitHostPort, then RemoteAddr. Never trust a single source.",
    },
    {
        "id": "PAT-007",
        "severity": "P1",
        "axis": "design_completeness",
        "name": "missing_audit_in_handler",
        "description": "API handler function with no audit/trace call",
        "pattern": re.compile(
            r"func\s+\(.*\)\s+handle\w+\(.*http\.ResponseWriter",
        ),
        "file_globs": ["*.go"],
        "requires_context": True,
        "context_lines": 30,
        "fix_hint": "Every handler must write an audit entry on both success and failure paths.",
    },
    {
        "id": "PAT-008",
        "severity": "P2",
        "axis": "design_completeness",
        "name": "return_501_stub",
        "description": "Endpoint returns HTTP 501 Not Implemented stub",
        "pattern": re.compile(
            r"StatusNotImplemented|501|not yet implemented|NotImplemented",
            re.IGNORECASE,
        ),
        "file_globs": ["*.go", "*.py", "*.ts", "*.tsx", "*.js"],
        "fix_hint": "Either implement the endpoint fully or remove the route definition. A stub endpoint is a runtime surprise.",
    },
    {

        "id": "PAT-009",
        "severity": "P3",
        "axis": "implementation_discipline",
        "name": "python_bare_except",
        "description": "Bare except or except Exception that silently swallows errors",
        "pattern": re.compile(
            r"except\s*(Exception)?\s*:",
            re.IGNORECASE,
        ),
        "file_globs": ["*.py"],
        "requires_context": True,
        "context_lines": 3,
        "fix_hint": "Catch specific exception types and either log, re-raise, or handle explicitly.",
    },
    {
        "id": "PAT-010",
        "severity": "P2",
        "axis": "design_completeness",
        "name": "missing_input_validation",
        "description": "Handler extracts request body/param without validation",
        "pattern": re.compile(
            r"(json\.NewDecoder|json\.Unmarshal|r\.URL\.Query\(\).Get)\(",
        ),
        "file_globs": ["*.go"],
        "requires_context": True,
        "context_lines": 10,
        "fix_hint": "Validate length, format, enum values, and bounds on every external input before use.",
    },
    {
        "id": "PAT-011",
        "severity": "P0",
        "axis": "delivery_completeness",
        "name": "cross_language_crypto_mismatch",
        "description": "Different encryption primitives used across languages in the same project",
        "project_level": True,
        "fix_hint": "Use the same encryption algorithm (e.g., AES-256-GCM) in all languages. Never mix AES with XOR.",
    },
    {
        "id": "PAT-012",
        "severity": "P1",
        "axis": "delivery_completeness",
        "name": "hardcoded_config",
        "description": "Hardcoded port, address, or path that should be configurable",
        "pattern": re.compile(
            r''':\d{4,5}\b|"localhost:\d+"|"/api/v\d+/'''
        ),
        "file_globs": ["*.go", "*.py", "*.ts", "*.tsx", "*.js"],
        "fix_hint": "Use environment variables or a config file instead of hardcoding ports, hosts, and paths.",
    },
    {
        "id": "PAT-013",
        "severity": "P1",
        "axis": "delivery_completeness",
        "name": "missing_health_check",
        "description": "HTTP server defined without a health check or readiness endpoint",
        "project_level": True,
        "fix_hint": "Add /health and /ready endpoints. In Go, use `net/http` with a dedicated health handler.",
    },
    {
        "id": "PAT-014",
        "severity": "P2",
        "axis": "delivery_completeness",
        "name": "no_graceful_shutdown",
        "description": "Server entrypoint without graceful shutdown (no signal handling, no drain)",
        "project_level": True,
        "fix_hint": "Listen for SIGINT/SIGTERM, drain connections, then exit. In Go: `signal.Notify` + `srv.Shutdown`.",
    },
    {
        "id": "PAT-015",
        "severity": "P2",
        "axis": "delivery_completeness",
        "name": "schema_change_without_migration",
        "description": "Database schema change detected without a migration file or directory",
        "project_level": True,
        "fix_hint": "Every schema change must have an up and down migration. Create a `migrations/` directory with versioned SQL files.",
    },
]


# ---------------------------------------------------------------------------
# Scanner
# ---------------------------------------------------------------------------

def _match_globs(file_path: Path, globs: list[str]) -> bool:
    if not globs:
        return True
    from fnmatch import fnmatch

    name = file_path.name
    return any(fnmatch(name, g) for g in globs)


def _find_files(target: Path, globs: list[str]) -> list[Path]:
    """Walk target directory, yield files matching globs."""
    if target.is_file():
        return [target] if _match_globs(target, globs) else []
    files: list[Path] = []
    for p in target.rglob("*"):
        if p.is_file() and _match_globs(p, globs):
            # skip vendor, node_modules, .git
            parts = p.parts
            if any(skip in parts for skip in (".git", "node_modules", "vendor", "__pycache__", ".agents")):
                continue
            files.append(p)
    return files


def _scan_file(file_path: Path, rule: dict[str, Any]) -> list[dict[str, Any]]:
    """Scan a single file against one rule. Returns list of finding dicts."""
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    findings: list[dict[str, Any]] = []
    pat = rule["pattern"]
    lines = text.splitlines()

    if rule.get("requires_context"):
        # For context-sensitive rules, find the anchor match, then check surrounding lines
        for m in pat.finditer(text):
            lineno = text[: m.start()].count("\n") + 1
            ctx_start = max(0, lineno - 1 - rule.get("context_lines", 10))
            ctx_end = min(len(lines), lineno - 1 + rule.get("context_lines", 10) + 1)
            context = lines[ctx_start:ctx_end]

            # Rule-specific context checks
            skip = False
            if rule["id"] == "PAT-004":  # missing defer close
                ctx_text = "\n".join(context)
                if "defer" in ctx_text:
                    skip = True
            elif rule["id"] == "PAT-006":  # single layer IP
                ctx_text = "\n".join(context)
                if any(
                    kw in ctx_text
                    for kw in ("X-Forwarded-For", "X-Real-IP", "SplitHostPort")
                ):
                    skip = True
            elif rule["id"] == "PAT-007":  # missing audit
                ctx_text = "\n".join(context)
                if any(kw in ctx_text for kw in ("audit", "Audit", "trace", "Trace")):
                    skip = True
            elif rule["id"] == "PAT-010":  # missing validation
                ctx_text = "\n".join(context)
                if any(kw in ctx_text for kw in ("valid", "Valid", "check", "Check", "len(", "== \"\"", "== 0")):
                    skip = True
            elif rule["id"] == "PAT-009":  # bare except with pass
                ctx_text = "\n".join(context)
                if "pass" not in ctx_text:
                    skip = True  # except exists but has real handling, not just pass

            if skip:
                continue

            findings.append(
                {
                    "rule_id": rule["id"],
                    "severity": rule["severity"],
                    "axis": rule.get("axis", ""),
                    "name": rule["name"],
                    "description": rule["description"],
                    "file": str(file_path),
                    "line": lineno,
                    "match": m.group(0).strip()[:120],
                    "fix_hint": rule["fix_hint"],
                }
            )
    else:
        # Simple line-based matching
        for i, line in enumerate(lines, start=1):
            if pat.search(line):
                findings.append(
                    {
                        "rule_id": rule["id"],
                        "severity": rule["severity"],
                        "axis": rule.get("axis", ""),
                        "name": rule["name"],
                        "description": rule["description"],
                        "file": str(file_path),
                        "line": i,
                        "match": line.strip()[:120],
                        "fix_hint": rule["fix_hint"],
                    }
                )

    return findings


def scan(target: str | Path, repo_root: str | Path = ".") -> dict[str, Any]:
    """Main entry point. Returns scan results dict with axis breakdown."""
    target_path = Path(target).expanduser().resolve()
    root = Path(repo_root).expanduser().resolve()

    all_findings: list[dict[str, Any]] = []
    rule_hits: dict[str, int] = defaultdict(int)
    files_scanned: set[str] = set()
    all_scanned_texts: dict[str, str] = {}  # path -> text for project-level checks

    # Per-file scanning (skip project_level rules)
    for rule in RULES:
        if rule.get("project_level"):
            continue
        files = _find_files(target_path, rule.get("file_globs", []))
        for fpath in files:
            files_scanned.add(str(fpath))
            findings = _scan_file(fpath, rule)
            if findings:
                rule_hits[rule["id"]] += len(findings)
            all_findings.extend(findings)
            # Cache text for project-level checks
            if str(fpath) not in all_scanned_texts:
                try:
                    all_scanned_texts[str(fpath)] = fpath.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    pass

    # ------------------------------------------------------------------
    # Project-level checks
    # ------------------------------------------------------------------
    project_findings: list[dict[str, Any]] = []

    # PAT-011: cross-language crypto mismatch
    go_has_aes = any(
        ("crypto/aes" in t or "aes.NewCipher" in t)
        for p, t in all_scanned_texts.items() if p.endswith(".go")
    )
    py_has_xor = any(
        ("operator.xor" in t or "operator import xor" in t.lower() or
         re.search(r"\bxor\b", t, re.IGNORECASE))
        for p, t in all_scanned_texts.items() if p.endswith(".py")
    )
    if go_has_aes and py_has_xor:
        rule = next(r for r in RULES if r["id"] == "PAT-011")
        project_findings.append({
            "rule_id": "PAT-011", "severity": "P0", "axis": "delivery_completeness",
            "name": rule["name"], "description": rule["description"],
            "file": "<project>", "line": 0,
            "match": "Go uses AES, Python uses XOR — incompatible encryption across languages",
            "fix_hint": rule["fix_hint"],
        })
        rule_hits["PAT-011"] = 1

    # PAT-013: HTTP server exists but no /health endpoint
    has_http_server = any(
        ("ListenAndServe" in t or "http.Server" in t or "app.run(" in t)
        for t in all_scanned_texts.values()
    )
    has_health_endpoint = any(
        ("/health" in t or "/ready" in t or "healthz" in t)
        for t in all_scanned_texts.values()
    )
    if has_http_server and not has_health_endpoint:
        rule = next(r for r in RULES if r["id"] == "PAT-013")
        project_findings.append({
            "rule_id": "PAT-013", "severity": "P1", "axis": "delivery_completeness",
            "name": rule["name"], "description": rule["description"],
            "file": "<project>", "line": 0,
            "match": "HTTP server found but no /health or /ready endpoint detected",
            "fix_hint": rule["fix_hint"],
        })
        rule_hits["PAT-013"] = 1

    # PAT-014: entrypoint without signal.Notify / graceful shutdown
    has_main = any(
        ("func main()" in t or 'if __name__ == "__main__"' in t)
        for t in all_scanned_texts.values()
    )
    has_signal_handling = any(
        ("signal.Notify" in t or "signal.signal(" in t or "SIGTERM" in t or "SIGINT" in t)
        for t in all_scanned_texts.values()
    )
    if has_main and not has_signal_handling:
        rule = next(r for r in RULES if r["id"] == "PAT-014")
        project_findings.append({
            "rule_id": "PAT-014", "severity": "P2", "axis": "delivery_completeness",
            "name": rule["name"], "description": rule["description"],
            "file": "<project>", "line": 0,
            "match": "Entrypoint found but no signal handling (SIGTERM/SIGINT) for graceful shutdown",
            "fix_hint": rule["fix_hint"],
        })
        rule_hits["PAT-014"] = 1

    # PAT-015: schema changes without migration directory
    has_schema_change = any(
        ("CREATE TABLE" in t or "ALTER TABLE" in t or "CREATE INDEX" in t)
        for t in all_scanned_texts.values()
    )
    has_migration_dir = any(
        ("migrations/" in p.lower() or "migrate" in p.lower())
        for p in all_scanned_texts
    ) or target_path.joinpath("migrations").is_dir()

    if has_schema_change and not has_migration_dir:
        rule = next(r for r in RULES if r["id"] == "PAT-015")
        project_findings.append({
            "rule_id": "PAT-015", "severity": "P2", "axis": "delivery_completeness",
            "name": rule["name"], "description": rule["description"],
            "file": "<project>", "line": 0,
            "match": "SQL schema changes detected but no migrations/ directory found",
            "fix_hint": rule["fix_hint"],
        })
        rule_hits["PAT-015"] = 1

    all_findings.extend(project_findings)

    # ------------------------------------------------------------------
    # Axis breakdown
    # ------------------------------------------------------------------
    AXES = ["design_completeness", "implementation_discipline", "delivery_completeness"]
    axis_counts: dict[str, dict[str, int]] = {}
    for axis in AXES:
        axis_findings = [f for f in all_findings if f.get("axis") == axis]
        blocking = [f for f in axis_findings if f.get("severity") in ("P0", "P1", "P2")]
        axis_counts[axis] = {
            "total": len(axis_findings),
            "blocking": len(blocking),
        }

    # Overall verdict: deny if ANY axis has blocking findings
    any_blocking = any(c["blocking"] > 0 for c in axis_counts.values())

    blocking = [f for f in all_findings if f.get("severity") in ("P0", "P1", "P2")]
    advisory = [f for f in all_findings if f.get("severity") not in ("P0", "P1", "P2")]

    return {
        "verdict": "deny" if any_blocking else "allow",
        "summary": {
            "total_findings": len(all_findings),
            "blocking_findings": len(blocking),
            "advisory_findings": len(advisory),
            "files_scanned": len(files_scanned),
            "rules_triggered": dict(rule_hits),
            "rules_not_triggered": [r["id"] for r in RULES if r["id"] not in rule_hits],
            "axis_breakdown": axis_counts,
        },
        "findings": all_findings,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan code for known LLM failure patterns."
    )
    parser.add_argument(
        "target",
        help="File or directory to scan.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root (default: current directory).",
    )
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="Output format (default: json).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = scan(args.target, args.repo_root)

    if args.format == "json":
        print(json.dumps(result))
    else:
        s = result["summary"]
        print(f"Files scanned: {s['files_scanned']}")
        print(f"Findings: {s['total_findings']} ({s['blocking_findings']} blocking, {s['advisory_findings']} advisory)")
        print(f"Verdict: {result['verdict']}")
        if s["rules_triggered"]:
            print("\nRules triggered:")
            for rid, count in s["rules_triggered"].items():
                rule = next(r for r in RULES if r["id"] == rid)
                print(f"  {rid} ({rule['severity']}): {count} hits — {rule['name']}")
        if "axis_breakdown" in s:
            print("\nAxis breakdown:")
            for axis, counts in s["axis_breakdown"].items():
                status = "CLEAN" if counts["blocking"] == 0 else "BLOCKED"
                print(f"  {axis}: {counts['total']} findings ({counts['blocking']} blocking) — {status}")
        if result["findings"]:
            print("\nDetail:")
            for f in result["findings"]:
                print(f"  {f['file']}:{f['line']} [{f['rule_id']}] {f['match']}")

    return 0 if result["verdict"] == "allow" else 1


if __name__ == "__main__":
    raise SystemExit(main())
