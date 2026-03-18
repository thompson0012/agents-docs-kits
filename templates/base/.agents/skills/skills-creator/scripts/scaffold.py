#!/usr/bin/env python3
"""
Scaffold a new SKILL.md package using the skills-creator templates.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

FORBIDDEN_WORDS = {"anthropic", "claude", "helper", "utils", "tools"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def validate_name(raw: str) -> str:
    name = raw.strip()
    if not name:
        _fail("Skill name is required.")
    if len(name) > 64:
        _fail("Skill name must be 64 characters or fewer.")
    if not NAME_PATTERN.match(name):
        _fail("Use lowercase letters, numbers, and single hyphens only (no leading/trailing/double hyphens).")
    lowered = name.lower()
    for word in FORBIDDEN_WORDS:
        if word in lowered:
            _fail(f"Skill name cannot include '{word}'.")
    if not lowered.endswith("ing"):
        print("NOTE: Gerund form is preferred (e.g., processing-pdfs).", file=sys.stderr)
    return lowered


def load_template(template_path: Path, skill_name: str) -> str:
    content = template_path.read_text(encoding="utf-8")
    return content.replace("replace-with-gerund-form", skill_name)


def scaffold(skill_name: str, output_dir: Path) -> Path:
    target_dir = output_dir / skill_name
    if target_dir.exists():
        _fail(f"Destination already exists: {target_dir}")

    template_root = Path(__file__).resolve().parent.parent / "assets"
    skill_template = template_root / "skill_template.md"
    eval_template = template_root / "eval_template.md"

    target_dir.mkdir(parents=True, exist_ok=False)
    evals_dir = target_dir / "evals"
    evals_dir.mkdir(parents=True, exist_ok=True)

    rendered_skill = load_template(skill_template, skill_name)
    (target_dir / "SKILL.md").write_text(rendered_skill, encoding="utf-8")
    shutil.copy(eval_template, evals_dir / "eval_template.md")

    print(f"Created skill at {target_dir}")
    print("- Edit SKILL.md to finalize description, steps, and references.")
    print("- Add scripts/ and references/ if the workflow needs them.")
    print("- Draft at least 3 evaluation scenarios using eval_template.md.")
    print(f"- Validate with: python3 scripts/validate.py {skill_name}")
    return target_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a SKILL.md package scaffold.")
    parser.add_argument("skill_name", help="Gerund-form skill folder name (lowercase, hyphenated).")
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Destination directory for the new skill (default: current directory).",
    )
    args = parser.parse_args()

    skill_name = validate_name(args.skill_name)
    out_dir = Path(args.output_dir).expanduser().resolve()

    try:
        scaffold(skill_name, out_dir)
    except FileNotFoundError as exc:
        _fail(f"Missing template file: {exc}")
    except PermissionError:
        _fail("Permission denied while writing files. Choose a writable destination.")


if __name__ == "__main__":
    main()
