#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from validation_common import (
    append_unique,
    collect_top_level_bullets,
    parse_acceptance_criteria,
    read_text,
    section_has_content,
    split_sections,
)

REQUIRED_SECTIONS = {
    "objective": "missing_objective_section",
    "allowed files": "missing_allowed_files_section",
    "forbidden changes": "missing_forbidden_changes_section",
    "acceptance criteria": "missing_acceptance_criteria_section",
    "verification plan": "missing_verification_plan_section",
    "assumptions & reward-hack surfaces": "missing_assumptions_section",
    "non-goals / deferred work": "missing_non_goals_section",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a sprint contract before execution begins."
    )
    parser.add_argument("workstream_id", help="Sprint/workstream identifier to validate.")
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root containing docs/live and .harness (default: current directory).",
    )
    return parser.parse_args()



def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).expanduser().resolve()
    workstream_id = args.workstream_id
    contract_path = repo_root / ".harness" / workstream_id / "contract.md"

    reasons: list[str] = []
    contract_text, contract_errors = read_text(contract_path, "missing_contract_md")
    append_unique(reasons, contract_errors)

    criterion_ids: list[str] = []
    if contract_text is not None:
        lines = [line.rstrip("\n") for line in contract_text.splitlines()]
        if not lines or workstream_id not in lines[0]:
            append_unique(reasons, ["contract_header_missing_workstream_id"])

        sections = split_sections(contract_text)
        for section_name, reason in REQUIRED_SECTIONS.items():
            if section_name not in sections:
                append_unique(reasons, [reason])

        objective_section = sections.get("objective", [])
        if objective_section and not section_has_content(objective_section):
            append_unique(reasons, ["empty_objective_section"])

        allowed_files = collect_top_level_bullets(sections.get("allowed files", []))
        if sections.get("allowed files") is not None and not allowed_files:
            append_unique(reasons, ["empty_allowed_files"])

        forbidden_changes = collect_top_level_bullets(sections.get("forbidden changes", []))
        if sections.get("forbidden changes") is not None and not forbidden_changes:
            append_unique(reasons, ["empty_forbidden_changes"])

        verification_plan = collect_top_level_bullets(sections.get("verification plan", []))
        if sections.get("verification plan") is not None and not verification_plan:
            append_unique(reasons, ["empty_verification_plan"])

        assumptions = collect_top_level_bullets(
            sections.get("assumptions & reward-hack surfaces", [])
        )
        if sections.get("assumptions & reward-hack surfaces") is not None and not assumptions:
            append_unique(reasons, ["empty_assumptions_section"])

        non_goals = collect_top_level_bullets(sections.get("non-goals / deferred work", []))
        if sections.get("non-goals / deferred work") is not None and not non_goals:
            append_unique(reasons, ["empty_non_goals_section"])

        acceptance_section = sections.get("acceptance criteria")
        if acceptance_section is not None:
            criteria, acceptance_errors = parse_acceptance_criteria(acceptance_section)
            append_unique(reasons, acceptance_errors)
            criterion_ids = [criterion["id"] for criterion in criteria]

    verdict = "allow" if not reasons else "deny"
    summary = {
        "workstream_id": workstream_id,
        "acceptance_ids": criterion_ids,
        "acceptance_count": len(criterion_ids),
    }
    print(json.dumps({"verdict": verdict, "reasons": reasons, "summary": summary}))
    return 0 if verdict == "allow" else 1


if __name__ == "__main__":
    raise SystemExit(main())
