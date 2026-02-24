#!/usr/bin/env python3
"""
validate_ledgers.py

Lightweight validation for agent stack artifacts:
- CODEMAP.md freshness check
- CHANGELOG.md entry count check
- Active ledger required fields check

Usage:
    python3 .agents/scripts/validate_ledgers.py
"""

import os
import sys
import re
from datetime import datetime, timedelta

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
DOCS_DIR = os.path.join(REPO_ROOT, ".agents", "docs")
LEDGERS_DIR = os.path.join(DOCS_DIR, "ledgers")

REQUIRED_FILES = [
    "AGENTS.md",
    ".agents/docs/PROGRESS.md",
    ".agents/docs/CODEMAP.md",
    ".agents/docs/CHANGELOG.md",
    ".agents/docs/SESSION_BOOTSTRAP.md",
    ".agents/docs/OBJECTIVE_LEDGER.md",
]

STALE_DAYS = 30
CHANGELOG_MIN_ENTRIES = 1

errors = []
warnings = []


def check_required_files():
    for rel_path in REQUIRED_FILES:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if not os.path.exists(full_path):
            errors.append(f"MISSING: {rel_path}")
        else:
            print(f"  OK: {rel_path}")


def check_codemap_freshness():
    codemap_path = os.path.join(DOCS_DIR, "CODEMAP.md")
    if not os.path.exists(codemap_path):
        return

    with open(codemap_path) as f:
        content = f.read()

    match = re.search(r"\*\*Last Updated\*\*:\s*(\d{4}-\d{2}-\d{2})", content)
    if not match:
        warnings.append("CODEMAP.md: Missing 'Last Updated' field")
        return

    last_updated = datetime.strptime(match.group(1), "%Y-%m-%d")
    age = (datetime.now() - last_updated).days

    if age > STALE_DAYS:
        errors.append(f"CODEMAP.md: Stale — last updated {age} days ago (threshold: {STALE_DAYS})")
    else:
        print(f"  OK: CODEMAP.md is {age} days old")


def check_changelog_entries():
    changelog_path = os.path.join(DOCS_DIR, "CHANGELOG.md")
    if not os.path.exists(changelog_path):
        return

    with open(changelog_path) as f:
        content = f.read()

    entries = re.findall(r"^### Entry \d+", content, re.MULTILINE)
    count = len(entries)

    if count < CHANGELOG_MIN_ENTRIES:
        warnings.append(f"CHANGELOG.md: Only {count} entries (minimum: {CHANGELOG_MIN_ENTRIES})")
    else:
        print(f"  OK: CHANGELOG.md has {count} entries")


def check_active_ledgers():
    if not os.path.exists(LEDGERS_DIR):
        warnings.append("ledgers/: Directory missing — create for active task tracking")
        return

    ledger_files = [f for f in os.listdir(LEDGERS_DIR) if f.endswith(".md") and f != "README.md"]

    for fname in ledger_files:
        fpath = os.path.join(LEDGERS_DIR, fname)
        with open(fpath) as f:
            content = f.read()

        required_fields = ["## Objective", "## Scope", "**Status**"]
        for field in required_fields:
            if field not in content:
                errors.append(f"ledgers/{fname}: Missing required field '{field}'")

        active = "status**: active" in content.lower()
        if active:
            print(f"  ACTIVE: ledgers/{fname}")
        else:
            print(f"  OK: ledgers/{fname}")


def main():
    print("\n=== Agent Stack Validation ===\n")

    print("Checking required files...")
    check_required_files()

    print("\nChecking CODEMAP.md freshness...")
    check_codemap_freshness()

    print("\nChecking CHANGELOG.md entries...")
    check_changelog_entries()

    print("\nChecking active ledgers...")
    check_active_ledgers()

    print("\n--- Results ---")
    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ {w}")
    if not errors and not warnings:
        print("\n  All checks passed.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
