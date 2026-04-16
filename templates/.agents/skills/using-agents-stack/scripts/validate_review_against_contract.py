#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from validation_common import (
    append_unique,
    parse_acceptance_criteria,
    parse_bool,
    parse_contract_check_results,
    parse_scalar,
    read_text,
    split_sections,
)



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that review evidence accounts for every contract acceptance criterion before PASS publication."
        )
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
    sprint_dir = repo_root / ".harness" / workstream_id

    contract_path = sprint_dir / "contract.md"
    qa_path = sprint_dir / "qa.md"
    review_path = sprint_dir / "review.md"

    reasons: list[str] = []

    contract_text, contract_errors = read_text(contract_path, "missing_contract_md")
    qa_text, qa_errors = read_text(qa_path, "missing_qa_md")
    review_text, review_errors = read_text(review_path, "missing_review_md")
    append_unique(reasons, contract_errors)
    append_unique(reasons, qa_errors)
    append_unique(reasons, review_errors)

    contract_ids: list[str] = []
    qa_ids: set[str] = set()
    review_ids: list[str] = []
    missing_ids: list[str] = []
    unexpected_ids: list[str] = []

    if contract_text is not None:
        contract_sections = split_sections(contract_text)
        acceptance_section = contract_sections.get("acceptance criteria")
        if acceptance_section is None:
            append_unique(reasons, ["missing_acceptance_criteria_section"])
        else:
            criteria, acceptance_errors = parse_acceptance_criteria(acceptance_section)
            append_unique(reasons, acceptance_errors)
            contract_ids = [criterion["id"] for criterion in criteria]

    if qa_text is not None:
        qa_sections = split_sections(qa_text)
        acceptance_checks = qa_sections.get("acceptance checks")
        if acceptance_checks is None:
            append_unique(reasons, ["missing_qa_acceptance_checks_section"])
        else:
            for line in acceptance_checks:
                stripped = line.strip()
                if stripped.startswith("### AC-"):
                    qa_ids.add(stripped.removeprefix("### ").split(":", 1)[0].strip())
                elif stripped.startswith("- `AC-"):
                    qa_ids.add(stripped.split("`", 2)[1])
            if not qa_ids:
                append_unique(reasons, ["missing_qa_acceptance_ids"])

    declared_total: int | None = None
    declared_checked: int | None = None
    declared_all_accounted: bool | None = None
    review_status: str | None = None

    if review_text is not None:
        review_sections = split_sections(review_text)

        status_section = review_sections.get("status")
        if not status_section:
            append_unique(reasons, ["missing_review_status_section"])
        else:
            for line in status_section:
                stripped = line.strip()
                if stripped in {"PASS", "FAIL", "BLOCKED"}:
                    review_status = stripped
                    break
            if review_status is None:
                append_unique(reasons, ["invalid_review_status"])

        coverage_section = review_sections.get("coverage metadata")
        if coverage_section is None:
            append_unique(reasons, ["missing_review_coverage_metadata"])
        else:
            total_value = parse_scalar(coverage_section, "criteria_total")
            checked_value = parse_scalar(coverage_section, "criteria_checked")
            all_accounted_value = parse_scalar(
                coverage_section, "all_acceptance_criteria_accounted_for"
            )

            if total_value is None:
                append_unique(reasons, ["missing_criteria_total"])
            else:
                try:
                    declared_total = int(total_value)
                except ValueError:
                    append_unique(reasons, ["invalid_criteria_total"])
                else:
                    if declared_total < 0:
                        append_unique(reasons, ["invalid_criteria_total"])

            if checked_value is None:
                append_unique(reasons, ["missing_criteria_checked"])
            else:
                try:
                    declared_checked = int(checked_value)
                except ValueError:
                    append_unique(reasons, ["invalid_criteria_checked"])
                else:
                    if declared_checked < 0:
                        append_unique(reasons, ["invalid_criteria_checked"])

            declared_all_accounted = parse_bool(all_accounted_value)
            if declared_all_accounted is None:
                append_unique(reasons, ["missing_all_acceptance_criteria_accounted_for"])

        contract_results_section = review_sections.get("contract check results")
        if contract_results_section is None:
            append_unique(reasons, ["missing_contract_check_results_section"])
            checks = []
        else:
            checks, check_errors = parse_contract_check_results(contract_results_section)
            append_unique(reasons, check_errors)
            review_ids = [check["id"] for check in checks]

            if review_status == "PASS":
                for check in checks:
                    if check["status"] != "PASS":
                        append_unique(reasons, ["pass_review_has_non_pass_contract_check"])
                        break

    if contract_ids:
        missing_ids = [criterion_id for criterion_id in contract_ids if criterion_id not in review_ids]
        unexpected_ids = [criterion_id for criterion_id in review_ids if criterion_id not in contract_ids]
        if missing_ids:
            append_unique(reasons, ["missing_review_coverage_for_contract_ids"])
        if unexpected_ids:
            append_unique(reasons, ["unexpected_review_contract_ids"])

        missing_qa_ids = [criterion_id for criterion_id in contract_ids if criterion_id not in qa_ids]
        if missing_qa_ids:
            append_unique(reasons, ["missing_qa_evidence_for_contract_ids"])

        if declared_total is not None and declared_total != len(contract_ids):
            append_unique(reasons, ["criteria_total_mismatch"])
        if declared_checked is not None and declared_checked != len(review_ids):
            append_unique(reasons, ["criteria_checked_mismatch"])
        if declared_all_accounted is True and len(review_ids) != len(contract_ids):
            append_unique(reasons, ["all_acceptance_criteria_accounted_for_mismatch"])
        if declared_all_accounted is False and len(review_ids) == len(contract_ids):
            append_unique(reasons, ["all_acceptance_criteria_accounted_for_mismatch"])

    verdict = "allow" if not reasons else "deny"
    summary = {
        "workstream_id": workstream_id,
        "contract_acceptance_ids": contract_ids,
        "qa_acceptance_ids": sorted(qa_ids),
        "review_acceptance_ids": review_ids,
        "missing_acceptance_ids": missing_ids,
        "unexpected_acceptance_ids": unexpected_ids,
        "review_status": review_status,
    }
    print(json.dumps({"verdict": verdict, "reasons": reasons, "summary": summary}))
    return 0 if verdict == "allow" else 1


if __name__ == "__main__":
    raise SystemExit(main())
