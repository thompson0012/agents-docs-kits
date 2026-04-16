#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

BLOCKING_SEVERITIES = {"P0", "P1", "P2", "P3"}
NONE_MARKERS = {"", "none", "null", "n/a", "na", "-"}
YES_MARKERS = {"yes", "true"}
NO_MARKERS = {"no", "false"}

ACCEPTANCE_PATTERN = re.compile(
    r"^\s*-\s*`(?P<id>AC-\d{3})`\s*\|\s*stateful=(?P<stateful>yes|no|true|false)\s*\|\s*reversible=(?P<reversible>yes|no|true|false)\s*$",
    re.IGNORECASE,
)
ACCEPTANCE_SUBFIELD_PATTERN = re.compile(
    r"^\s*-\s*(?P<key>Requirement|Evidence|Before state|Action|After state|Reverse check):\s*(?P<value>.+?)\s*$",
    re.IGNORECASE,
)
CONTRACT_CHECK_PATTERN = re.compile(
    r"^\s*-\s*`(?P<id>AC-\d{3})`\s*\|\s*status=(?P<status>PASS|FAIL|BLOCKED|NOT_RUN)\s*\|\s*evidence=(?P<evidence>.+?)\s*$",
    re.IGNORECASE,
)
FINDING_PATTERN = re.compile(
    r"^\s*-\s*`?(?P<id>[^`|]+?)`?\s*\|\s*severity=(?P<severity>[A-Za-z0-9_-]+)\s*\|\s*status=(?P<status>[A-Za-z0-9_-]+)\s*\|\s*duplicate_of=(?P<duplicate_of>[^|]*)\s*$"
)


def append_unique(reasons: list[str], additions: list[str]) -> None:
    for reason in additions:
        if reason not in reasons:
            reasons.append(reason)


class ValidationError(Exception):
    pass


def read_json(path: Path, missing_reason: str, invalid_reason: str) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, [missing_reason]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None, [invalid_reason]

    if not isinstance(data, dict):
        return None, [invalid_reason]
    return data, []



def read_text(path: Path, missing_reason: str) -> tuple[str | None, list[str]]:
    try:
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    except FileNotFoundError:
        return None, [missing_reason]

    if not text.strip():
        return None, [missing_reason]
    return text, []



def split_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip("\n")
        if line.startswith("## "):
            current = line[3:].strip().lower()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return sections



def parse_scalar(section_lines: list[str], key: str) -> str | None:
    needle = f"- {key}:"
    for line in section_lines:
        stripped = line.strip()
        if stripped.startswith(needle):
            return stripped[len(needle) :].strip()
    return None



def parse_list(section_lines: list[str], key: str) -> list[str] | None:
    needle = f"- {key}:"
    for index, line in enumerate(section_lines):
        stripped = line.strip()
        if not stripped.startswith(needle):
            continue

        inline = stripped[len(needle) :].strip()
        if inline == "[]":
            return []
        if inline:
            return [inline]

        values: list[str] = []
        cursor = index + 1
        while cursor < len(section_lines):
            candidate = section_lines[cursor]
            candidate_stripped = candidate.strip()
            if not candidate_stripped:
                cursor += 1
                continue
            if candidate.startswith("  - ") or candidate.startswith("\t- "):
                values.append(candidate_stripped[2:].strip())
                cursor += 1
                continue
            if candidate_stripped.startswith("- "):
                break
            cursor += 1
        return values
    return None



def parse_bool(value: str | None) -> bool | None:
    if value is None:
        return None
    lowered = value.strip().lower()
    if lowered in YES_MARKERS:
        return True
    if lowered in NO_MARKERS:
        return False
    return None



def normalize_duplicate(value: str) -> str | None:
    lowered = value.strip().lower()
    if lowered in NONE_MARKERS:
        return None
    return value.strip()



def collect_top_level_bullets(section_lines: list[str]) -> list[str]:
    values: list[str] = []
    for line in section_lines:
        stripped = line.strip()
        if stripped.startswith("- ") and not line.startswith("  - ") and not line.startswith("\t- "):
            values.append(stripped[2:].strip())
    return values



def section_has_content(section_lines: list[str]) -> bool:
    return any(line.strip() for line in section_lines)



def parse_acceptance_criteria(section_lines: list[str]) -> tuple[list[dict[str, Any]], list[str]]:
    criteria: list[dict[str, Any]] = []
    reasons: list[str] = []
    seen_ids: set[str] = set()
    cursor = 0

    while cursor < len(section_lines):
        line = section_lines[cursor]
        stripped = line.strip()
        if not stripped:
            cursor += 1
            continue

        header = ACCEPTANCE_PATTERN.match(stripped)
        if header is None:
            append_unique(reasons, ["invalid_acceptance_criteria_format"])
            cursor += 1
            continue

        criterion_id = header.group("id").strip()
        if criterion_id in seen_ids:
            append_unique(reasons, ["duplicate_acceptance_id"])
        seen_ids.add(criterion_id)

        stateful = parse_bool(header.group("stateful"))
        reversible = parse_bool(header.group("reversible"))
        if stateful is None or reversible is None:
            append_unique(reasons, ["invalid_acceptance_flags"])
            cursor += 1
            continue

        cursor += 1
        fields: dict[str, str] = {}
        while cursor < len(section_lines):
            candidate = section_lines[cursor]
            candidate_stripped = candidate.strip()
            if not candidate_stripped:
                cursor += 1
                continue
            if ACCEPTANCE_PATTERN.match(candidate_stripped):
                break
            if not (candidate.startswith("  - ") or candidate.startswith("\t- ")):
                append_unique(reasons, ["invalid_acceptance_subfield_format"])
                cursor += 1
                continue
            subfield = ACCEPTANCE_SUBFIELD_PATTERN.match(candidate_stripped)
            if subfield is None:
                append_unique(reasons, ["invalid_acceptance_subfield_format"])
                cursor += 1
                continue
            key = subfield.group("key").strip().lower().replace(" ", "_")
            fields[key] = subfield.group("value").strip()
            cursor += 1

        if reversible and not stateful:
            append_unique(reasons, ["reversible_acceptance_requires_stateful"])
        if not fields.get("requirement"):
            append_unique(reasons, ["missing_acceptance_requirement"])
        if not fields.get("evidence"):
            append_unique(reasons, ["missing_acceptance_evidence"])
        if stateful:
            for key in ("before_state", "action", "after_state"):
                if not fields.get(key):
                    append_unique(reasons, [f"missing_{key}"])
        if reversible and not fields.get("reverse_check"):
            append_unique(reasons, ["missing_reverse_check"])

        criteria.append(
            {
                "id": criterion_id,
                "stateful": stateful,
                "reversible": reversible,
                "fields": fields,
            }
        )

    if not criteria:
        append_unique(reasons, ["missing_acceptance_criteria"])
    return criteria, reasons



def parse_contract_check_results(section_lines: list[str]) -> tuple[list[dict[str, str]], list[str]]:
    checks: list[dict[str, str]] = []
    reasons: list[str] = []
    seen_ids: set[str] = set()

    for line in section_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if not stripped.startswith("-"):
            continue
        match = CONTRACT_CHECK_PATTERN.match(stripped)
        if match is None:
            append_unique(reasons, ["invalid_contract_check_format"])
            continue
        criterion_id = match.group("id").strip()
        if criterion_id in seen_ids:
            append_unique(reasons, ["duplicate_contract_check_id"])
            continue
        seen_ids.add(criterion_id)
        evidence = match.group("evidence").strip()
        if not evidence:
            append_unique(reasons, ["missing_contract_check_evidence"])
        checks.append(
            {
                "id": criterion_id,
                "status": match.group("status").strip().upper(),
                "evidence": evidence,
            }
        )

    if not checks:
        append_unique(reasons, ["missing_contract_check_results"])
    return checks, reasons



def parse_findings(section_lines: list[str]) -> tuple[list[dict[str, str | None]], list[str]]:
    findings: list[dict[str, str | None]] = []
    reasons: list[str] = []

    for line in section_lines:
        stripped = line.strip()
        if not stripped.startswith("-"):
            continue
        match = FINDING_PATTERN.match(stripped)
        if match is None:
            if stripped.startswith("- `") or "severity=" in stripped or "duplicate_of=" in stripped:
                append_unique(reasons, ["invalid_finding_format"])
            continue
        findings.append(
            {
                "id": match.group("id").strip(),
                "severity": match.group("severity").strip().upper(),
                "status": match.group("status").strip().upper(),
                "duplicate_of": normalize_duplicate(match.group("duplicate_of")),
            }
        )

    if not findings:
        append_unique(reasons, ["missing_findings_list"])
    return findings, reasons
