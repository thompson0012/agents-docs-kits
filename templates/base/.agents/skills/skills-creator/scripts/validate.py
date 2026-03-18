#!/usr/bin/env python3
"""
Validate a SKILL.md package for naming, frontmatter, and structure.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    yaml = None

FORBIDDEN_WORDS = {"anthropic", "claude", "helper", "utils", "tools"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DESCRIPTION_MAX = 1024
BODY_LINE_MAX = 500
DEEP_REFERENCE = re.compile(r"references/[^\s/]+/[^\s/]+")
XML_TAG = re.compile(r"<[^>]+>")


def _fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def parse_frontmatter(skill_path: Path) -> Tuple[Dict[str, str], List[str]]:
    content = skill_path.read_text(encoding="utf-8").splitlines()
    if not content or content[0].strip() not in ("---", "***"):
        _fail("SKILL.md must start with YAML frontmatter delimiter '---'.")

    end_index = None
    for idx, line in enumerate(content[1:], start=1):
        if line.strip() in ("---", "***"):
            end_index = idx
            break
    if end_index is None:
        _fail("Frontmatter is not closed with a delimiter line ('---').")

    frontmatter_lines = "\n".join(content[1:end_index])
    body_lines = content[end_index + 1 :]

    if yaml:
        try:
            data = yaml.safe_load(frontmatter_lines) or {}
        except Exception as exc:  # pragma: no cover
            _fail(f"Invalid YAML frontmatter: {exc}")
    else:
        data = parse_frontmatter_fallback(frontmatter_lines)
    return data, body_lines


def parse_frontmatter_fallback(frontmatter: str) -> Dict[str, str]:
    data: Dict[str, str] = {}
    current_key: str | None = None
    buffer: List[str] = []

    def flush_buffer() -> None:
        nonlocal buffer, current_key
        if current_key and buffer:
            data[current_key] = "\n".join(buffer).strip()
        buffer = []

    for raw_line in frontmatter.splitlines():
        line = raw_line.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if current_key:
                buffer.append(line.strip())
            continue
        flush_buffer()
        key, sep, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if not sep:
            continue
        if value in {"", ">", "|"}:
            current_key = key
            buffer = []
        else:
            data[key] = value
            current_key = None
    flush_buffer()
    return data


def check_name(name: str, folder_name: str, errors: List[str], warnings: List[str]) -> None:
    if len(name) > 64 or not name:
        errors.append("Frontmatter 'name' must be 1-64 characters.")
    if name != folder_name:
        errors.append(f"Frontmatter 'name' must match folder '{folder_name}'.")
    if not NAME_PATTERN.match(name):
        errors.append("Name must use lowercase letters, numbers, and single hyphens (no leading/trailing/double hyphens).")
    for word in FORBIDDEN_WORDS:
        if word in name.lower():
            errors.append(f"Name cannot include '{word}'.")
    if not name.endswith("ing"):
        warnings.append("Gerund form is preferred (e.g., processing-pdfs).")


def check_description(description: str, errors: List[str], warnings: List[str]) -> None:
    if not description:
        errors.append("Frontmatter 'description' is required.")
        return
    if len(description) > DESCRIPTION_MAX:
        errors.append(f"Description exceeds {DESCRIPTION_MAX} characters.")
    if "use when" not in description.lower():
        warnings.append("Description should include an explicit trigger (e.g., 'Use when ...').")
    if XML_TAG.search(description):
        errors.append("Description must not contain XML/HTML tags.")


def check_body(body_lines: List[str], errors: List[str], warnings: List[str]) -> None:
    if len(body_lines) > BODY_LINE_MAX:
        errors.append(f"SKILL.md body exceeds {BODY_LINE_MAX} lines.")
    body_text = "\n".join(body_lines)
    if DEEP_REFERENCE.search(body_text):
        warnings.append("File references should be only one level deep under references/.")


def check_evals(skill_dir: Path, full: bool, errors: List[str], warnings: List[str]) -> None:
    eval_dir = skill_dir / "evals"
    if not full or not eval_dir.exists():
        return
    scenario_files = [p for p in eval_dir.iterdir() if p.is_file() and p.suffix.lower() in {".md", ".json", ".yaml", ".yml"}]
    if len(scenario_files) < 3:
        errors.append("At least 3 evaluation scenarios are required for --full validation.")


def validate(skill_dir: Path, full: bool) -> Tuple[List[str], List[str]]:
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.exists():
        _fail(f"SKILL.md not found in {skill_dir}")

    frontmatter, body = parse_frontmatter(skill_path)
    errors: List[str] = []
    warnings: List[str] = []

    name = str(frontmatter.get("name", "")).strip()
    check_name(name, skill_dir.name, errors, warnings)

    description = str(frontmatter.get("description", "")).strip()
    check_description(description, errors, warnings)

    check_body(body, errors, warnings)
    check_evals(skill_dir, full, errors, warnings)

    return errors, warnings


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a SKILL.md package.")
    parser.add_argument("skill_path", help="Path to the skill directory or SKILL.md file.")
    parser.add_argument("--full", action="store_true", help="Run the stricter pre-ship gate checks.")
    args = parser.parse_args()

    target = Path(args.skill_path).expanduser().resolve()
    skill_dir = target.parent if target.is_file() else target

    errors, warnings = validate(skill_dir, args.full)

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("Validation passed.")


if __name__ == "__main__":
    main()
