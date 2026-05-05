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



def check_cross_language(repo_root: str | Path = ".") -> dict[str, Any]:
    """Check for incompatible primitives across languages in the project."""
    root = Path(repo_root).expanduser().resolve()

    # Scan all source files
    go_crypto: set[str] = set()
    py_crypto: set[str] = set()
    ts_crypto: set[str] = set()

    go_crypto_patterns = {
        "aes": r"crypto/aes|aes\.NewCipher",
        "sha256": r"crypto/sha256|sha256\.New",
        "sha1": r"crypto/sha1|sha1\.New",
        "md5": r"crypto/md5|md5\.New",
        "des": r"crypto/des|des\.NewCipher",
        "bcrypt": r"golang\.org/x/crypto/bcrypt",
    }
    py_crypto_patterns = {
        "xor": r"\bxor\b|operator\.xor",
        "md5": r"hashlib\.md5|md5\(",
        "sha1": r"hashlib\.sha1|sha1\(",
        "des": r"pyDes|des\.DES",
        "aes": r"Crypto\.Cipher\.AES|AES\.new|from Cryptodome",
    }

    for p in root.rglob("*"):
        if not p.is_file():
            continue
        parts = p.parts
        if any(skip in parts for skip in (".git", "node_modules", "vendor", "__pycache__", ".agents", ".harness")):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        suffix = p.suffix
        if suffix == ".go":
            for name, pat in go_crypto_patterns.items():
                if re.search(pat, text):
                    go_crypto.add(name)
        elif suffix == ".py":
            for name, pat in py_crypto_patterns.items():
                if re.search(pat, text):
                    py_crypto.add(name)

    findings: list[dict[str, Any]] = []

    # Known incompatible pairs
    incompatible_pairs = [
        (("go", "aes"), ("py", "xor"), "P0",
         "Go uses AES but Python uses XOR — encryption primitives are incompatible across languages"),
        (("go", "sha256"), ("py", "md5"), "P1",
         "Go uses SHA-256 but Python uses MD5 — hash strength mismatch across languages"),
        (("go", "aes"), ("py", "des"), "P1",
         "Go uses AES but Python uses DES — encryption strength mismatch across languages"),
    ]

    for (lang_a, algo_a), (lang_b, algo_b), severity, desc in incompatible_pairs:
        crypto_a = go_crypto if lang_a == "go" else py_crypto
        crypto_b = go_crypto if lang_b == "go" else py_crypto
        if algo_a in crypto_a and algo_b in crypto_b:
            findings.append({
                "rule_id": "XLANG-001",
                "severity": severity,
                "axis": "delivery_completeness",
                "name": "cross_language_crypto_mismatch",
                "description": desc,
                "file": "<project>",
                "line": 0,
                "match": f"{lang_a}/{algo_a} vs {lang_b}/{algo_b}",
                "fix_hint": f"Standardize on one algorithm across all languages. Prefer AES-256-GCM.",
            })

    blocking = [f for f in findings if f["severity"] in ("P0", "P1", "P2")]
    return {
        "verdict": "deny" if blocking else "allow",
        "reasons": ["cross_language_crypto_mismatch"] if blocking else [],
        "summary": {
            "go_algorithms": sorted(go_crypto),
            "py_algorithms": sorted(py_crypto),
            "mismatches": len(findings),
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
    parser.add_argument(
        "--cross-language",
        action="store_true",
        help="Also check for cross-language algorithm mismatches (AES vs XOR etc.).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = check_contract(args.contract_path, args.repo_root)

    if args.cross_language:
        xlang = check_cross_language(args.repo_root)
        result["findings"].extend(xlang["findings"])
        if xlang["findings"]:
            result["reasons"].extend(xlang["reasons"])
        result["summary"]["cross_language"] = xlang["summary"]
        if xlang["verdict"] == "deny":
            result["verdict"] = "deny"

    if args.format == "json":
        print(json.dumps(result))
    else:
        s = result["summary"]
        print(f"Tasks checked: {s['tasks_checked']}")
        print(f"Symbols declared: {s['symbols_declared']}")
        print(f"Symbols matched: {s['symbols_matched']}")
        print(f"Symbols missing: {s['symbols_missing']}")
        if "cross_language" in s:
            xl = s["cross_language"]
            print(f"\nCross-language algorithms:")
            print(f"  Go: {', '.join(xl['go_algorithms']) if xl['go_algorithms'] else 'none detected'}")
            print(f"  Python: {', '.join(xl['py_algorithms']) if xl['py_algorithms'] else 'none detected'}")
            print(f"  Mismatches: {xl['mismatches']}")
        print(f"Verdict: {result['verdict']}")
        if result["findings"]:
            print("\nIssues:")
            for f in result["findings"]:
                src = f.get('file', '<project>')
                line = f.get('line', 0)
                match = f.get('match', '')
                desc = f.get('description', '')
                print(f"  {src}:{line} [{f.get('rule_id', '?')}] {match or desc}")

    return 0 if result["verdict"] == "allow" else 1


if __name__ == "__main__":
    raise SystemExit(main())
