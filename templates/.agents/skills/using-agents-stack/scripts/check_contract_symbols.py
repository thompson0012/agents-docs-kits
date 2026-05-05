#!/usr/bin/env python3
"""Verify that contract-declared symbols exist in actual code.

Takes a structured contract (from generator-proposal's `## Task Decomposition`)
and checks each declared function/method/type/interface symbol against the
actual codebase. Language-agnostic and domain-agnostic -- purely structural.

Contract format (YAML or JSON):

    tasks:
      - id: auth-module
        symbols:
          - name: ValidateToken
            kind: function  # function | method | type | interface
            signature: "func ValidateToken(token string) (*Claims, error)"
            file_hint: internal/auth/
        depends_on: []

Usage:
    python check_contract_symbols.py <contract.json> --repo-root <root>
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Symbol extractors per language
# ---------------------------------------------------------------------------

GO_FUNC_PATTERN = re.compile(
    r"^func\s+(?:\(\w+\s+\*?\w+\)\s+)?(?P<name>\w+)\([^)]*\)",
    re.MULTILINE,
)
GO_TYPE_PATTERN = re.compile(
    r"^type\s+(?P<name>\w+)\s+(struct|interface)\s*\{",
    re.MULTILINE,
)

PY_FUNC_PATTERN = re.compile(
    r"^def\s+(?P<name>\w+)\(",
    re.MULTILINE,
)
PY_CLASS_PATTERN = re.compile(
    r"^class\s+(?P<name>\w+)[(:]",
    re.MULTILINE,
)

TS_FUNC_PATTERN = re.compile(
    r"(?:export\s+)?(?:async\s+)?function\s+(?P<name>\w+)\(",
    re.MULTILINE,
)


def _extract_go_symbols(text: str) -> set[str]:
    names: set[str] = set()
    for m in GO_FUNC_PATTERN.finditer(text):
        names.add(m.group("name"))
    for m in GO_TYPE_PATTERN.finditer(text):
        names.add(m.group("name"))
    return names


def _extract_py_symbols(text: str) -> set[str]:
    names: set[str] = set()
    for m in PY_FUNC_PATTERN.finditer(text):
        names.add(m.group("name"))
    for m in PY_CLASS_PATTERN.finditer(text):
        names.add(m.group("name"))
    return names


TS_ARROW_PATTERN = re.compile(
    r"(?:export\s+)?(?:const|let|var)\s+(?P<name>\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>",
    re.MULTILINE,
)
TS_INTERFACE_PATTERN = re.compile(
    r"(?:export\s+)?interface\s+(?P<name>\w+)\b",
    re.MULTILINE,
)
TS_TYPE_PATTERN = re.compile(
    r"(?:export\s+)?type\s+(?P<name>\w+)\s*=",
    re.MULTILINE,
)
TS_CLASS_PATTERN = re.compile(
    r"(?:export\s+)?class\s+(?P<name>\w+)\b",
    re.MULTILINE,
)


def _extract_ts_symbols(text: str) -> set[str]:
    names: set[str] = set()
    for m in TS_FUNC_PATTERN.finditer(text):
        names.add(m.group("name"))
    for m in TS_ARROW_PATTERN.finditer(text):
        names.add(m.group("name"))
    for m in TS_INTERFACE_PATTERN.finditer(text):
        names.add(m.group("name"))
    for m in TS_TYPE_PATTERN.finditer(text):
        names.add(m.group("name"))
    for m in TS_CLASS_PATTERN.finditer(text):
        names.add(m.group("name"))
    return names


EXTRACTORS = {
    ".go": _extract_go_symbols,
    ".py": _extract_py_symbols,
    ".ts": _extract_ts_symbols,
    ".tsx": _extract_ts_symbols,
}


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def _collect_code_symbols(search_dir: Path, file_exts: set[str]) -> dict[str, set[str]]:
    """Walk search_dir, extract all defined symbols by file extension."""
    symbols: dict[str, set[str]] = defaultdict(set)

    for p in search_dir.rglob("*"):
        if not p.is_file():
            continue
        ext = p.suffix
        if ext not in EXTRACTORS:
            continue
        if ext not in file_exts:
            continue
        # skip vendor, node_modules, .git
        parts = p.parts
        if any(skip in parts for skip in (".git", "node_modules", "vendor", "__pycache__", ".agents", ".harness")):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        extractor = EXTRACTORS[ext]
        symbols[ext] |= extractor(text)

    return symbols


def _find_symbol_in_dir(
    name: str, search_dir: Path, code_symbols: dict[str, set[str]] | None = None
) -> tuple[bool, str | None]:
    """Check if a symbol exists in the codebase. Returns (found, location)."""
    # Try cached symbols first
    if code_symbols is not None:
        for ext, names in code_symbols.items():
            if name in names:
                return True, f"found in {ext} files under {search_dir}"
        return False, None

    # Fallback: scan files
    for p in search_dir.rglob("*"):
        if not p.is_file() or p.suffix not in EXTRACTORS:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        extractor = EXTRACTORS[p.suffix]
        if name in extractor(text):
            return True, str(p)
    return False, None


def check_contract(
    contract_path: str | Path, repo_root: str | Path = "."
) -> dict[str, Any]:
    """Main entry point. Returns check results dict."""
    contract_path = Path(contract_path).expanduser().resolve()
    root = Path(repo_root).expanduser().resolve()

    # Load contract
    try:
        raw = contract_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {
            "verdict": "blocked",
            "reasons": ["contract_file_not_found"],
            "summary": {"tasks_checked": 0, "symbols_declared": 0, "symbols_matched": 0, "symbols_missing": 0},
            "findings": [],
        }

    # Try JSON first, then attempt to extract structured tasks from markdown
    contract_data: dict[str, Any] | None = None
    tasks: list[dict[str, Any]] = []

    try:
        contract_data = json.loads(raw)
        tasks = contract_data.get("tasks", [])
    except json.JSONDecodeError:
        # Extract from markdown: look for fenced JSON/YAML blocks under ## Task Decomposition
        sections = raw.split("\n## ")
        for section in sections:
            if section.lower().startswith("task decomposition"):
                # Find fenced code block
                fence_match = re.search(r"```(?:json|yaml)?\s*\n(.*?)```", section, re.DOTALL | re.IGNORECASE)
                if fence_match:
                    block = fence_match.group(1)
                    try:
                        contract_data = json.loads(block)
                        tasks = contract_data.get("tasks", [])
                    except json.JSONDecodeError:
                        # Try YAML
                        try:
                            import yaml
                            contract_data = yaml.safe_load(block)
                            tasks = contract_data.get("tasks", []) if contract_data else []
                        except Exception:
                            pass
                break

    if not tasks:
        return {
            "verdict": "deny",
            "reasons": ["no_tasks_in_contract"],
            "summary": {"tasks_checked": 0, "symbols_declared": 0, "symbols_matched": 0, "symbols_missing": 0},
            "findings": [],
        }

    # Collect code symbols once for efficiency
    all_exts: set[str] = set()
    search_roots: list[Path] = []
    for task in tasks:
        file_hint = task.get("file_hint", "")
        if file_hint:
            d = root / file_hint
            if d.exists():
                search_roots.append(d)
        # Collect expected extensions from declared signatures
        for sym in task.get("symbols", []):
            sig = sym.get("signature", "")
            if "func " in sig:
                all_exts.add(".go")
            elif "def " in sig:
                all_exts.add(".py")
            elif "function " in sig or "=>" in sig:
                all_exts.add(".ts")

    if not search_roots:
        search_roots = [root]

    code_symbols: dict[str, set[str]] = {}
    for sr in search_roots:
        cs = _collect_code_symbols(sr, all_exts)
        for ext, names in cs.items():
            if ext not in code_symbols:
                code_symbols[ext] = set()
            code_symbols[ext] |= names

    # Check each task's symbols
    findings: list[dict[str, Any]] = []
    total_declared = 0
    total_matched = 0
    total_missing = 0

    for task in tasks:
        task_id = task.get("id", "unknown")
        symbols = task.get("symbols", [])
        total_declared += len(symbols)

        for sym in symbols:
            name = sym.get("name", "")
            kind = sym.get("kind", "")
            sig = sym.get("signature", "")

            found, location = _find_symbol_in_dir(name, root, code_symbols)

            if found:
                total_matched += 1
            else:
                total_missing += 1
                findings.append(
                    {
                        "task_id": task_id,
                        "symbol": name,
                        "kind": kind,
                        "declared_signature": sig,
                        "status": "missing",
                        "fix_hint": f"Implement '{name}' in {task.get('file_hint', 'the codebase')} or remove it from the contract.",
                    }
                )

    reasons: list[str] = []
    if total_missing > 0:
        reasons.append("symbols_missing_from_code")

    return {
        "verdict": "allow" if total_missing == 0 else "deny",
        "reasons": reasons,
        "summary": {
            "tasks_checked": len(tasks),
            "symbols_declared": total_declared,
            "symbols_matched": total_matched,
            "symbols_missing": total_missing,
        },
        "findings": findings,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

from collections import defaultdict


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify contract-declared symbols exist in code."
    )
    parser.add_argument(
        "contract_path",
        help="Path to the contract file (JSON or markdown with embedded ## Task Decomposition).",
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
    result = check_contract(args.contract_path, args.repo_root)

    if args.format == "json":
        print(json.dumps(result))
    else:
        s = result["summary"]
        print(f"Tasks checked: {s['tasks_checked']}")
        print(f"Symbols declared: {s['symbols_declared']}")
        print(f"Symbols matched: {s['symbols_matched']}")
        print(f"Symbols missing: {s['symbols_missing']}")
        print(f"Verdict: {result['verdict']}")
        if result["findings"]:
            print("\nMissing symbols:")
            for f in result["findings"]:
                print(f"  [{f['task_id']}] {f['symbol']} ({f['kind']}) — not found in code")

    return 0 if result["verdict"] == "allow" else 1


if __name__ == "__main__":
    raise SystemExit(main())
