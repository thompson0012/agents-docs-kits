#!/usr/bin/env python3
"""Validate the root AGENTS router contract for this repository."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT_GUIDE = REPO_ROOT / "AGENTS.md"
MANIFEST_PATH = REPO_ROOT / ".agents" / "router-manifest.json"
ROOT_LOCAL_GUIDES = {
    ".agents/AGENTS.md": (
        "## Local Scope",
        "## Owns",
        "## Does Not Own",
        "## Required Reads",
        "## Local Update Rules",
        "## Failure Modes to Avoid",
    ),
    ".agents/skills/AGENTS.md": (
        "## Local Scope",
        "## Owns",
        "## Does Not Own",
        "## Required Reads",
        "## Local Update Rules",
        "## Failure Modes to Avoid",
    ),
    "docs/AGENTS.md": (
        "## Local Scope",
        "## Owns",
        "## Does Not Own",
        "## Required Reads",
        "## Local Update Rules",
        "## Failure Modes to Avoid",
    ),
    "docs/live/AGENTS.md": (
        "## Local Scope",
        "## Owns",
        "## Does Not Own",
        "## Required Reads",
        "## Local Update Rules",
        "## Failure Modes to Avoid",
    ),
    "docs/reference/AGENTS.md": (
        "## Local Scope",
        "## Owns",
        "## Does Not Own",
        "## Required Reads",
        "## Local Update Rules",
        "## Failure Modes to Avoid",
    ),
}
TEMPLATE_LOCAL_GUIDES = {
    "templates/base/.agents/AGENTS.md": ROOT_LOCAL_GUIDES[".agents/AGENTS.md"],
    "templates/base/.agents/skills/AGENTS.md": ROOT_LOCAL_GUIDES[".agents/skills/AGENTS.md"],
    "templates/base/.agents/skills-optional/AGENTS.md": ROOT_LOCAL_GUIDES[".agents/skills/AGENTS.md"],
    "templates/base/docs/AGENTS.md": ROOT_LOCAL_GUIDES["docs/AGENTS.md"],
    "templates/base/docs/live/AGENTS.md": ROOT_LOCAL_GUIDES["docs/live/AGENTS.md"],
    "templates/base/docs/reference/AGENTS.md": ROOT_LOCAL_GUIDES["docs/reference/AGENTS.md"],
}
ROOT_REQUIRED_SNIPPETS = (
    "## Startup Minimum",
    "### repo work",
    "### template work",
    "## Scope Fences",
    "## Decision Order",
    "## Escalation Rules",
    "## Failure Modes to Avoid",
    "## Verification for Router Changes",
    "python3 scripts/validate_agents_router.py",
    "## Discovery Index",
    ".agents/router-manifest.json",
    "templates/base/AGENTS.md",
)
MANIFEST_TOP_LEVEL = {"router_name", "purpose", "startup_paths", "decision_order", "children"}
MANIFEST_CHILD_FIELDS = {
    "name",
    "path",
    "kind",
    "scope",
    "summary",
    "route_when",
    "avoid_when",
    "requires",
    "fallbacks_to",
}
ALLOWED_CHILD_KINDS = {"skill", "local-agents"}
ALLOWED_CHILD_SCOPES = {"repo", "template"}


@dataclass
class Issue:
    level: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the root AGENTS router contract.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def validate_headings(path: Path, headings: tuple[str, ...]) -> list[Issue]:
    issues: list[Issue] = []
    if not path.exists():
        return [Issue("error", f"missing file: {path.relative_to(REPO_ROOT)}")]
    content = read_text(path)
    for heading in headings:
        if heading not in content:
            issues.append(Issue("error", f"{path.relative_to(REPO_ROOT)} missing heading: {heading}"))
    return issues


def validate_root_guide() -> list[Issue]:
    issues: list[Issue] = []
    content = read_text(ROOT_GUIDE)
    for snippet in ROOT_REQUIRED_SNIPPETS:
        if snippet not in content:
            issues.append(Issue("error", f"AGENTS.md missing required snippet: {snippet}"))

    for indexed_path in (
        ".agents/AGENTS.md",
        ".agents/skills/AGENTS.md",
        ".agents/router-manifest.json",
        "docs/AGENTS.md",
        "docs/live/AGENTS.md",
        "docs/reference/AGENTS.md",
        "templates/base/AGENTS.md",
    ):
        if indexed_path not in content:
            issues.append(Issue("error", f"AGENTS.md discovery index missing path: {indexed_path}"))
    return issues


def validate_manifest() -> list[Issue]:
    issues: list[Issue] = []
    if not MANIFEST_PATH.exists():
        return [Issue("error", "missing file: .agents/router-manifest.json")]

    data = read_json(MANIFEST_PATH)
    if not isinstance(data, dict):
        return [Issue("error", ".agents/router-manifest.json must contain a JSON object")]

    missing = MANIFEST_TOP_LEVEL - set(data)
    for key in sorted(missing):
        issues.append(Issue("error", f"router manifest missing top-level field: {key}"))

    extra = set(data) - MANIFEST_TOP_LEVEL
    for key in sorted(extra):
        issues.append(Issue("warning", f"router manifest uses non-standard top-level field: {key}"))

    router_name = data.get("router_name")
    if not isinstance(router_name, str) or not router_name.strip():
        issues.append(Issue("error", "router_name must be a non-empty string"))

    purpose = data.get("purpose")
    if not isinstance(purpose, str) or not purpose.strip():
        issues.append(Issue("error", "purpose must be a non-empty string"))

    startup_paths = data.get("startup_paths")
    if not isinstance(startup_paths, dict):
        issues.append(Issue("error", "startup_paths must be an object"))
    else:
        for name in ("repo_work", "template_work"):
            value = startup_paths.get(name)
            if not isinstance(value, list) or not value or any(not isinstance(item, str) or not item.strip() for item in value):
                issues.append(Issue("error", f"startup_paths.{name} must be a non-empty array of strings"))
                continue
            for relative in value:
                if not (REPO_ROOT / relative).exists():
                    issues.append(Issue("error", f"startup path does not exist: {relative}"))

    decision_order = data.get("decision_order")
    if not isinstance(decision_order, list) or not decision_order or any(not isinstance(item, str) or not item.strip() for item in decision_order):
        issues.append(Issue("error", "decision_order must be a non-empty array of strings"))

    children = data.get("children")
    if not isinstance(children, list) or not children:
        issues.append(Issue("error", "children must be a non-empty array"))
        return issues

    child_names: set[str] = set()
    pending_fallbacks: list[tuple[str, str]] = []
    for index, child in enumerate(children, start=1):
        label = f"child #{index}"
        if not isinstance(child, dict):
            issues.append(Issue("error", f"{label} must be an object"))
            continue

        extra_child = set(child) - MANIFEST_CHILD_FIELDS
        for key in sorted(extra_child):
            issues.append(Issue("warning", f"{label} uses non-standard field: {key}"))

        missing_child = MANIFEST_CHILD_FIELDS - set(child)
        for key in sorted(missing_child):
            issues.append(Issue("error", f"{label} missing field: {key}"))

        name = child.get("name")
        if not isinstance(name, str) or not name.strip():
            issues.append(Issue("error", f"{label} name must be a non-empty string"))
            child_name = None
        else:
            child_name = name.strip()
            if child_name in child_names:
                issues.append(Issue("error", f"duplicate child name: {child_name}"))
            child_names.add(child_name)

        path_value = child.get("path")
        if not isinstance(path_value, str) or not path_value.strip():
            issues.append(Issue("error", f"{label} path must be a non-empty string"))
        elif not (REPO_ROOT / path_value).exists():
            issues.append(Issue("error", f"{label} path does not exist: {path_value}"))

        kind = child.get("kind")
        if not isinstance(kind, str) or kind not in ALLOWED_CHILD_KINDS:
            issues.append(Issue("error", f"{label} kind must be one of: {', '.join(sorted(ALLOWED_CHILD_KINDS))}"))

        scope = child.get("scope")
        if not isinstance(scope, str) or scope not in ALLOWED_CHILD_SCOPES:
            issues.append(Issue("error", f"{label} scope must be one of: {', '.join(sorted(ALLOWED_CHILD_SCOPES))}"))

        summary = child.get("summary")
        if not isinstance(summary, str) or not summary.strip():
            issues.append(Issue("error", f"{label} summary must be a non-empty string"))

        for field in ("route_when", "avoid_when", "requires", "fallbacks_to"):
            value = child.get(field)
            if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
                issues.append(Issue("error", f"{label} {field} must be an array of non-empty strings"))

        for required_path in child.get("requires", []) if isinstance(child.get("requires"), list) else []:
            if not (REPO_ROOT / required_path).exists():
                issues.append(Issue("error", f"{label} requires missing path: {required_path}"))

        for fallback in child.get("fallbacks_to", []) if isinstance(child.get("fallbacks_to"), list) else []:
            if child_name:
                pending_fallbacks.append((child_name, fallback))

    for child_name, fallback in pending_fallbacks:
        if fallback not in child_names:
            issues.append(Issue("error", f"child {child_name} falls back to unknown child: {fallback}"))

    return issues


def validate_root_skill_inventory() -> list[Issue]:
    issues: list[Issue] = []
    skills_dir = REPO_ROOT / ".agents" / "skills"
    actual = sorted(path.name for path in skills_dir.iterdir() if path.is_dir())
    content = read_text(skills_dir / "AGENTS.md")
    for entry in actual:
        bullet = f"- `{entry}/`"
        if bullet not in content:
            issues.append(Issue("error", f".agents/skills/AGENTS.md missing inventory bullet: {bullet}"))
    return issues


def main() -> int:
    args = parse_args()
    issues: list[Issue] = []
    issues.extend(validate_root_guide())
    issues.extend(validate_manifest())
    issues.extend(validate_root_skill_inventory())

    for relative, headings in ROOT_LOCAL_GUIDES.items():
        issues.extend(validate_headings(REPO_ROOT / relative, headings))
    for relative, headings in TEMPLATE_LOCAL_GUIDES.items():
        issues.extend(validate_headings(REPO_ROOT / relative, headings))

    errors = [issue for issue in issues if issue.level == "error"]
    warnings = [issue for issue in issues if issue.level == "warning"]

    for issue in errors + warnings:
        print(f"{issue.level}: {issue.message}")

    if errors:
        return 1
    if warnings and args.strict:
        return 1
    print("router validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
