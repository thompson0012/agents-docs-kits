#!/usr/bin/env python3
"""Audit the base template skill suite for portability and legacy-surface drift."""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "templates" / "base" / ".agents" / "skills"
LEAF_VALIDATOR = SKILLS_ROOT / "create-skill" / "scripts" / "validate.py"
ROUTER_VALIDATOR = SKILLS_ROOT / "create-router-skill" / "scripts" / "validate_router.py"

STALE_SKILL_PATH = re.compile(r"(?<!\.agents/)skills/")
UNSUPPORTED_TOOL_PATTERNS: dict[str, re.Pattern[str]] = {
    "browser_task": re.compile(r"\bbrowser_task\b"),
    "call_external_tool": re.compile(r"\bcall_external_tool\b"),
    "deploy_website": re.compile(r"\bdeploy_website\b"),
    "describe_external_tools": re.compile(r"\bdescribe_external_tools\b"),
    "finance_watchlist_fetch": re.compile(r"\bfinance_watchlist_fetch\b"),
    "js_repl": re.compile(r"\bjs_repl\b"),
    "list_external_tools": re.compile(r"\blist_external_tools\b"),
    "memory_search": re.compile(r"\bmemory_search\b"),
    "memory_update": re.compile(r"\bmemory_update\b"),
    "run_subagent": re.compile(r"\brun_subagent\b"),
    "screenshot_page": re.compile(r"\bscreenshot_page\b"),
    "start_server": re.compile(r"\bstart_server\b"),
}
VENDOR_PATTERNS: dict[str, re.Pattern[str]] = {
    "Perplexity branding": re.compile(r"\bPerplexity(?: Computer| Finance)?\b"),
    "perplexity finance URL": re.compile(r"perplexity\.ai/finance"),
    "Perplexity-built phrasing": re.compile(r"built by Perplexity"),
    "Perplexity-aligned phrasing": re.compile(r"Perplexity-aligned"),
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    kind: str
    detail: str


def list_skill_dirs() -> list[Path]:
    return sorted(path for path in SKILLS_ROOT.rglob("SKILL.md") if path.is_file())


def run_validator(command: list[str]) -> tuple[int, str]:
    proc = subprocess.run(command, capture_output=True, text=True)
    output = (proc.stdout + proc.stderr).strip()
    return proc.returncode, output


def validate_skill_files() -> list[str]:
    failures: list[str] = []
    for skill_file in list_skill_dirs():
        skill_dir = skill_file.parent
        rc, output = run_validator([sys.executable, str(LEAF_VALIDATOR), str(skill_dir), "--strict"])
        if rc != 0:
            failures.append(f"leaf validator failed for {skill_dir.relative_to(REPO_ROOT)}\n{indent(output)}")

        if (skill_dir / "references" / "children.json").exists():
            rc, output = run_validator([sys.executable, str(ROUTER_VALIDATOR), str(skill_dir), "--strict"])
            if rc != 0:
                failures.append(f"router validator failed for {skill_dir.relative_to(REPO_ROOT)}\n{indent(output)}")
    return failures


def indent(text: str) -> str:
    return "\n".join(f"  {line}" for line in text.splitlines()) if text else "  <no output>"


def scan_markdown() -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(SKILLS_ROOT.rglob("*.md")):
        rel = path.relative_to(REPO_ROOT)
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if STALE_SKILL_PATH.search(line):
                findings.append(Finding(rel, line_number, "stale-skill-path", line.strip()))
            for label, pattern in UNSUPPORTED_TOOL_PATTERNS.items():
                if pattern.search(line):
                    findings.append(Finding(rel, line_number, f"unsupported-tool:{label}", line.strip()))
            for label, pattern in VENDOR_PATTERNS.items():
                if pattern.search(line):
                    findings.append(Finding(rel, line_number, f"vendor-string:{label}", line.strip()))
    return findings


def scan_artifacts() -> list[Path]:
    return sorted(path.relative_to(REPO_ROOT) for path in REPO_ROOT.rglob(".DS_Store"))


def main() -> int:
    failures = validate_skill_files()
    findings = scan_markdown()
    artifacts = scan_artifacts()

    if not failures and not findings and not artifacts:
        print("Base template skill audit passed.")
        return 0

    print("Base template skill audit failed.")

    if failures:
        print("\nValidator failures:")
        for entry in failures:
            print(f"- {entry}")

    if findings:
        print("\nContent findings:")
        for finding in findings:
            print(f"- {finding.path}:{finding.line} [{finding.kind}] {finding.detail}")

    if artifacts:
        print("\nRepository artifacts:")
        for path in artifacts:
            print(f"- {path}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
