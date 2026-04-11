#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
TERMINAL_PHASES = {"archived", "completed", "cancelled"}
PARKED_PHASES = {"awaiting_human", "escalated_to_human"}
FAILED_PHASES = {"build_failed", "review_failed"}
RUNNABLE_BACKLOG_STATUSES = {
    "in_progress",
    "proposed",
    "contracted",
    "executing",
    "awaiting_review",
    "in_review",
    "build_failed",
    "review_failed",
    "paused_by_timeout",
}
DEPENDENCY_SATISFIED_STATUSES = {"archived", "completed", "done", "passed"}
ARTIFACT_PRECEDENCE = (
    "review.md",
    "handoff.md",
    "runtime.md",
    "contract.md",
    "sprint_proposal.md",
)
CHILD_TARGETS = {
    "project-initializer": "using-agents-stack/project-initializer",
    "generator-brainstorm": "using-agents-stack/generator-brainstorm",
    "generator-proposal": "using-agents-stack/generator-proposal",
    "evaluator-contract-review": "using-agents-stack/evaluator-contract-review",
    "generator-execution": "using-agents-stack/generator-execution",
    "adversarial-live-review": "using-agents-stack/adversarial-live-review",
    "state-update": "using-agents-stack/state-update",
    "compound-capture": "using-agents-stack/compound-capture",
}
RETRY_GUARD_TIMEOUT_SECONDS = 10


Decision = dict[str, Any]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read agents-stack durable state and emit one deterministic routing decision "
            "without mutating repository files."
        )
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root containing docs/live and .harness (default: current directory).",
    )
    return parser.parse_args()


def read_json_object(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, "missing"

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None, "invalid_json"

    if not isinstance(data, dict):
        return None, "invalid_shape"
    return data, None


def nonempty_file(path: Path) -> bool:
    try:
        return bool(path.read_text(encoding="utf-8").strip())
    except FileNotFoundError:
        return False


def relative_path(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def normalize_phase(status: dict[str, Any]) -> str:
    phase = status.get("phase")
    if not isinstance(phase, str):
        return ""
    return phase.strip()


def runnable_active_pointer(tracked_work: dict[str, Any]) -> str | None:
    pointer = tracked_work.get("runnable_active_sprint_id")
    if pointer in (None, ""):
        pointer = tracked_work.get("active_sprint_id")
    if not isinstance(pointer, str):
        return None
    pointer = pointer.strip()
    return pointer or None


def load_backlog(tracked_work: dict[str, Any]) -> tuple[list[dict[str, Any]] | None, list[str], bool]:
    backlog = tracked_work.get("backlog")
    if not isinstance(backlog, list):
        return None, ["missing_backlog"], True

    entries: list[dict[str, Any]] = []
    errors: list[str] = []
    for index, item in enumerate(backlog):
        if not isinstance(item, dict):
            errors.append(f"invalid_backlog_entry_{index}")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id.strip():
            errors.append(f"missing_backlog_id_{index}")
        entries.append(item)

    return entries, errors, bool(errors)


def load_compound_queue(tracked_work: dict[str, Any]) -> tuple[list[str] | None, list[str], bool]:
    raw_queue = tracked_work.get("compound_pending_feature_ids")
    if raw_queue is None:
        raw_queue = []
    if not isinstance(raw_queue, list):
        return None, ["invalid_compound_queue_shape"], True

    queue: list[str] = []
    errors: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(raw_queue):
        item_id = str(item).strip()
        if not item_id:
            errors.append(f"empty_compound_queue_entry_{index}")
            continue
        if item_id in seen:
            errors.append(f"duplicate_compound_queue_id_{item_id}")
            continue
        seen.add(item_id)
        queue.append(item_id)

    return queue, errors, False


def backlog_index(backlog: list[dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], list[str]]:
    index: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    for position, item in enumerate(backlog):
        raw_id = item.get("id")
        if not isinstance(raw_id, str):
            errors.append(f"missing_backlog_id_{position}")
            continue
        item_id = raw_id.strip()
        if not item_id:
            errors.append(f"missing_backlog_id_{position}")
            continue
        if item_id in index:
            errors.append(f"duplicate_backlog_id_{item_id}")
            continue
        index[item_id] = item
    return index, errors


def dependency_status_satisfied(status: Any) -> bool:
    return str(status).strip().lower() in DEPENDENCY_SATISFIED_STATUSES


def backlog_priority(item: dict[str, Any], ordinal: int) -> tuple[int, int]:
    priority = item.get("priority")
    if isinstance(priority, bool):
        priority = None
    if isinstance(priority, int):
        return priority, ordinal
    return 10**9, ordinal


def select_next_feature(
    backlog: list[dict[str, Any]],
    candidate_statuses: set[str],
) -> tuple[dict[str, Any] | None, list[str]]:
    by_id, index_errors = backlog_index(backlog)
    if index_errors:
        return None, index_errors

    ready: list[tuple[tuple[int, int], dict[str, Any]]] = []
    errors: list[str] = []

    for ordinal, item in enumerate(backlog):
        item_id = str(item.get("id", "")).strip()
        if not item_id:
            continue

        status = str(item.get("status", "")).strip().lower()
        if status not in candidate_statuses:
            continue

        dependencies = item.get("dependencies", [])
        if dependencies is None:
            dependencies = []
        if not isinstance(dependencies, list):
            errors.append(f"non_list_dependencies_{item_id}")
            continue

        blocked = False
        for dependency in dependencies:
            dependency_id = str(dependency).strip()
            if not dependency_id:
                errors.append(f"empty_dependency_id_{item_id}")
                blocked = True
                continue
            dependency_item = by_id.get(dependency_id)
            if dependency_item is None:
                errors.append(f"missing_dependency_{item_id}_{dependency_id}")
                blocked = True
                continue
            if not dependency_status_satisfied(dependency_item.get("status")):
                blocked = True
                break

        if blocked:
            continue

        ready.append((backlog_priority(item, ordinal), item))

    if errors:
        return None, errors
    if not ready:
        return None, []

    ready.sort(key=lambda pair: pair[0])
    return ready[0][1], []


def is_runnable_phase(phase: str) -> bool:
    return bool(phase) and phase not in TERMINAL_PHASES and phase not in PARKED_PHASES


def strongest_artifact(sprint_dir: Path) -> str | None:
    for artifact in ARTIFACT_PRECEDENCE:
        if nonempty_file(sprint_dir / artifact):
            return artifact
    return None


def load_local_entries(repo_root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    harness_root = repo_root / ".harness"
    if not harness_root.exists():
        return [], []

    entries: list[dict[str, Any]] = []
    errors: list[str] = []

    for sprint_dir in sorted(path for path in harness_root.iterdir() if path.is_dir()):
        status_path = sprint_dir / "status.json"
        status, status_error = read_json_object(status_path)
        artifact = strongest_artifact(sprint_dir)

        if status_error == "missing":
            if artifact is not None:
                errors.append(f"missing_status_json_{sprint_dir.name}")
            continue
        if status_error == "invalid_json":
            errors.append(f"invalid_status_json_{sprint_dir.name}")
            continue
        if status_error == "invalid_shape" or status is None:
            errors.append(f"invalid_status_shape_{sprint_dir.name}")
            continue

        phase = normalize_phase(status)
        if not phase:
            errors.append(f"missing_status_phase_{sprint_dir.name}")
            continue

        sprint_id = status.get("sprint_id")
        if sprint_id is None or sprint_id == "":
            sprint_id = sprint_dir.name
        if not isinstance(sprint_id, str) or not sprint_id.strip():
            errors.append(f"invalid_sprint_id_{sprint_dir.name}")
            continue
        sprint_id = sprint_id.strip()
        if sprint_id != sprint_dir.name:
            errors.append(f"sprint_dir_mismatch_{sprint_dir.name}_{sprint_id}")
            continue

        if phase in PARKED_PHASES:
            resume_from = status.get("resume_from")
            if not isinstance(resume_from, str) or not resume_from.strip():
                errors.append(f"missing_parked_resume_from_{sprint_id}")
            human_action_required = status.get("human_action_required")
            if phase == "awaiting_human" and (
                not isinstance(human_action_required, str) or not human_action_required.strip()
            ):
                errors.append(f"missing_human_action_required_{sprint_id}")

        entries.append(
            {
                "sprint_dir": sprint_dir,
                "status_path": status_path,
                "status": status,
                "phase": phase,
                "sprint_id": sprint_id,
                "artifact": artifact,
            }
        )

    return entries, errors


def find_feature_for_sprint(
    backlog: list[dict[str, Any]], sprint_id: str
) -> tuple[dict[str, Any] | None, list[str]]:
    matches: list[dict[str, Any]] = []
    for item in backlog:
        item_sprint_id = item.get("sprint_id")
        item_id = item.get("id")
        if isinstance(item_sprint_id, str) and item_sprint_id.strip() == sprint_id:
            matches.append(item)
            continue
        if isinstance(item_id, str) and item_id.strip() == sprint_id:
            matches.append(item)

    if len(matches) > 1:
        return None, [f"ambiguous_live_feature_for_{sprint_id}"]
    if not matches:
        return None, [f"missing_live_feature_for_{sprint_id}"]
    return matches[0], []


def runnable_backlog_ids(backlog: list[dict[str, Any]]) -> tuple[list[str], list[str]]:
    ids: list[str] = []
    errors: list[str] = []
    for ordinal, item in enumerate(backlog):
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id.strip():
            errors.append(f"missing_backlog_id_{ordinal}")
            continue
        status = item.get("status")
        if isinstance(status, str) and status.strip() in RUNNABLE_BACKLOG_STATUSES:
            ids.append(item_id.strip())
    return ids, errors


def run_retry_guard(repo_root: Path, workstream_id: str) -> tuple[str, list[str]]:
    script_path = Path(__file__).with_name("verify_retry_guard.py")
    if not script_path.exists():
        return "deny", ["missing_retry_guard_script"]

    try:
        completed = subprocess.run(
            [
                sys.executable,
                str(script_path),
                workstream_id,
                "--repo-root",
                str(repo_root),
            ],
            capture_output=True,
            text=True,
            timeout=RETRY_GUARD_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "deny", ["retry_guard_timeout"]
    except OSError:
        return "deny", ["retry_guard_exec_failed"]

    stdout = completed.stdout.strip()
    if not stdout:
        return "deny", ["retry_guard_empty_output"]

    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        return "deny", ["retry_guard_invalid_output"]

    verdict = payload.get("verdict")
    reasons = payload.get("reasons")
    if verdict not in {"allow", "deny"}:
        return "deny", ["retry_guard_invalid_verdict"]
    if not isinstance(reasons, list) or any(not isinstance(reason, str) for reason in reasons):
        return "deny", ["retry_guard_invalid_reasons"]
    return verdict, list(dict.fromkeys(reasons))


def route(
    child: str,
    *,
    reason_codes: list[str],
    feature_id: str | None = None,
    workstream_id: str | None = None,
    resume_from: str | None = None,
    evidence_path: str | None = None,
) -> Decision:
    return {
        "schema_version": SCHEMA_VERSION,
        "decision": "route",
        "child": child,
        "target": CHILD_TARGETS[child],
        "reason_codes": list(dict.fromkeys(reason_codes)),
        "feature_id": feature_id,
        "workstream_id": workstream_id,
        "resume_from": resume_from,
        "evidence_path": evidence_path,
    }


def no_family_child(
    *,
    reason_codes: list[str],
    feature_id: str | None = None,
    workstream_id: str | None = None,
    resume_from: str | None = None,
    evidence_path: str | None = None,
) -> Decision:
    return {
        "schema_version": SCHEMA_VERSION,
        "decision": "no_family_child",
        "child": None,
        "target": None,
        "reason_codes": list(dict.fromkeys(reason_codes)),
        "feature_id": feature_id,
        "workstream_id": workstream_id,
        "resume_from": resume_from,
        "evidence_path": evidence_path,
    }


def validate_output_shape(payload: Decision) -> None:
    required_keys = {
        "schema_version",
        "decision",
        "child",
        "target",
        "reason_codes",
        "feature_id",
        "workstream_id",
        "resume_from",
        "evidence_path",
    }
    if set(payload) != required_keys:
        raise ValueError("dispatcher output keys do not match schema")
    if payload["schema_version"] != SCHEMA_VERSION:
        raise ValueError("invalid schema version")
    if payload["decision"] not in {"route", "no_family_child"}:
        raise ValueError("invalid decision")
    if not isinstance(payload["reason_codes"], list) or not payload["reason_codes"]:
        raise ValueError("reason_codes must be a non-empty array")
    if any(not isinstance(reason, str) or not reason for reason in payload["reason_codes"]):
        raise ValueError("reason_codes entries must be non-empty strings")
    for key in ("feature_id", "workstream_id", "resume_from", "evidence_path"):
        value = payload[key]
        if value is not None and (not isinstance(value, str) or not value):
            raise ValueError(f"{key} must be null or a non-empty string")

    if payload["decision"] == "route":
        child = payload["child"]
        target = payload["target"]
        if child not in CHILD_TARGETS:
            raise ValueError("invalid child")
        if target != CHILD_TARGETS[child]:
            raise ValueError("target does not match child")
        return

    if payload["child"] is not None or payload["target"] is not None:
        raise ValueError("no_family_child must not include child target")


def dispatch_active_sprint(
    repo_root: Path,
    *,
    entry: dict[str, Any],
    feature: dict[str, Any],
    live_status: str,
) -> Decision:
    sprint_id = entry["sprint_id"]
    sprint_dir: Path = entry["sprint_dir"]
    phase: str = entry["phase"]
    artifact: str | None = entry["artifact"]
    feature_id = str(feature.get("id", "")).strip() or None

    evidence_artifact = artifact
    if evidence_artifact is None:
        resume_from = entry["status"].get("resume_from")
        if isinstance(resume_from, str) and resume_from.strip() and nonempty_file(sprint_dir / resume_from.strip()):
            evidence_artifact = resume_from.strip()

    evidence_path = (
        relative_path(sprint_dir / evidence_artifact, repo_root) if evidence_artifact is not None else relative_path(entry["status_path"], repo_root)
    )

    if artifact == "review.md":
        if phase == "review_failed" and live_status == "review_failed":
            verdict, guard_reasons = run_retry_guard(repo_root, sprint_id)
            if verdict == "allow":
                return route(
                    "generator-execution",
                    reason_codes=["reconciled_review_failed", "retry_guard_allowed"],
                    feature_id=feature_id,
                    workstream_id=sprint_id,
                    resume_from="review.md",
                    evidence_path=evidence_path,
                )
            return route(
                "state-update",
                reason_codes=["retry_guard_denied", *guard_reasons],
                feature_id=feature_id,
                workstream_id=sprint_id,
                resume_from="review.md",
                evidence_path=evidence_path,
            )

        return route(
            "state-update",
            reason_codes=["review_recorded_needs_reconciliation"],
            feature_id=feature_id,
            workstream_id=sprint_id,
            resume_from="review.md",
            evidence_path=evidence_path,
        )

    if phase == "review_failed":
        return route(
            "state-update",
            reason_codes=["review_failed_missing_review_evidence"],
            feature_id=feature_id,
            workstream_id=sprint_id,
            resume_from=evidence_artifact,
            evidence_path=evidence_path,
        )

    if phase == "build_failed":
        if live_status == "build_failed":
            verdict, guard_reasons = run_retry_guard(repo_root, sprint_id)
            if verdict == "allow":
                return route(
                    "generator-execution",
                    reason_codes=["reconciled_build_failed", "retry_guard_allowed"],
                    feature_id=feature_id,
                    workstream_id=sprint_id,
                    resume_from="runtime.md",
                    evidence_path=evidence_path,
                )
            return route(
                "state-update",
                reason_codes=["retry_guard_denied", *guard_reasons],
                feature_id=feature_id,
                workstream_id=sprint_id,
                resume_from="runtime.md",
                evidence_path=evidence_path,
            )

        return route(
            "state-update",
            reason_codes=["build_failed_needs_reconciliation"],
            feature_id=feature_id,
            workstream_id=sprint_id,
            resume_from="runtime.md" if artifact == "runtime.md" else evidence_artifact,
            evidence_path=evidence_path,
        )

    if artifact == "handoff.md":
        return route(
            "adversarial-live-review",
            reason_codes=["strongest_artifact_handoff"],
            feature_id=feature_id,
            workstream_id=sprint_id,
            resume_from="handoff.md",
            evidence_path=evidence_path,
        )

    if artifact in {"runtime.md", "contract.md"}:
        return route(
            "generator-execution",
            reason_codes=["strongest_artifact_execution"],
            feature_id=feature_id,
            workstream_id=sprint_id,
            resume_from=artifact,
            evidence_path=evidence_path,
        )

    if artifact == "sprint_proposal.md":
        return route(
            "evaluator-contract-review",
            reason_codes=["strongest_artifact_proposal"],
            feature_id=feature_id,
            workstream_id=sprint_id,
            resume_from="sprint_proposal.md",
            evidence_path=evidence_path,
        )

    return route(
        "state-update",
        reason_codes=["missing_active_checkpoint"],
        feature_id=feature_id,
        workstream_id=sprint_id,
        evidence_path=evidence_path,
    )


def compute_decision(repo_root: Path) -> Decision:
    tracked_work_path = repo_root / "docs" / "live" / "tracked-work.json"
    tracked_work, tracked_error = read_json_object(tracked_work_path)
    if tracked_error == "missing":
        return route(
            "project-initializer",
            reason_codes=["missing_tracked_work"],
            evidence_path=relative_path(tracked_work_path, repo_root),
        )
    if tracked_error == "invalid_json":
        return route(
            "project-initializer",
            reason_codes=["invalid_tracked_work_json"],
            evidence_path=relative_path(tracked_work_path, repo_root),
        )
    if tracked_error == "invalid_shape" or tracked_work is None:
        return route(
            "project-initializer",
            reason_codes=["invalid_tracked_work_shape"],
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    backlog, backlog_errors, backlog_untrustworthy = load_backlog(tracked_work)
    if backlog_untrustworthy:
        return route(
            "project-initializer",
            reason_codes=backlog_errors,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )
    assert backlog is not None

    queue, queue_errors, queue_untrustworthy = load_compound_queue(tracked_work)
    if queue_untrustworthy:
        return route(
            "project-initializer",
            reason_codes=queue_errors,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )
    assert queue is not None

    local_entries, local_errors = load_local_entries(repo_root)
    if local_errors:
        return route(
            "state-update",
            reason_codes=local_errors,
            evidence_path=relative_path(repo_root / ".harness", repo_root),
        )

    backlog_by_id, backlog_index_errors = backlog_index(backlog)
    if backlog_index_errors:
        return route(
            "state-update",
            reason_codes=backlog_index_errors,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    if queue_errors:
        return route(
            "state-update",
            reason_codes=queue_errors,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    missing_queued_features = [feature_id for feature_id in queue if feature_id not in backlog_by_id]
    if missing_queued_features:
        return route(
            "state-update",
            reason_codes=[f"missing_compound_queue_feature_{feature_id}" for feature_id in missing_queued_features],
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    local_by_id = {entry["sprint_id"]: entry for entry in local_entries}
    runnable_entries = [entry for entry in local_entries if is_runnable_phase(entry["phase"])]
    parked_entries = [entry for entry in local_entries if entry["phase"] in PARKED_PHASES]

    if len(runnable_entries) > 1:
        return route(
            "state-update",
            reason_codes=["multiple_runnable_local_sprints"],
            evidence_path=relative_path(repo_root / ".harness", repo_root),
        )

    runnable_ids, runnable_id_errors = runnable_backlog_ids(backlog)
    if runnable_id_errors:
        return route(
            "state-update",
            reason_codes=runnable_id_errors,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )
    if len(runnable_ids) > 1:
        return route(
            "state-update",
            reason_codes=["multiple_runnable_backlog_items"],
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    active_pointer = runnable_active_pointer(tracked_work)
    if runnable_entries:
        active_entry = runnable_entries[0]
        active_sprint_id = active_entry["sprint_id"]
        if active_pointer is None:
            return route(
                "state-update",
                reason_codes=["live_missing_runnable_active_sprint_id"],
                workstream_id=active_sprint_id,
                evidence_path=relative_path(active_entry["status_path"], repo_root),
            )
        if active_pointer != active_sprint_id:
            return route(
                "state-update",
                reason_codes=["live_local_active_sprint_mismatch"],
                workstream_id=active_sprint_id,
                evidence_path=relative_path(active_entry["status_path"], repo_root),
            )

        feature, feature_errors = find_feature_for_sprint(backlog, active_sprint_id)
        if feature_errors or feature is None:
            return route(
                "state-update",
                reason_codes=feature_errors or ["missing_live_feature_for_active_sprint"],
                workstream_id=active_sprint_id,
                evidence_path=relative_path(tracked_work_path, repo_root),
            )

        live_status = str(feature.get("status", "")).strip()
        if not live_status:
            return route(
                "state-update",
                reason_codes=["missing_live_status_for_active_sprint"],
                feature_id=str(feature.get("id", "")).strip() or None,
                workstream_id=active_sprint_id,
                evidence_path=relative_path(tracked_work_path, repo_root),
            )
        if live_status in PARKED_PHASES:
            return route(
                "state-update",
                reason_codes=["parked_sprint_marked_runnable_globally"],
                feature_id=str(feature.get("id", "")).strip() or None,
                workstream_id=active_sprint_id,
                evidence_path=relative_path(tracked_work_path, repo_root),
            )

        if queue:
            queued_feature = queue[0]
            return route(
                "compound-capture",
                reason_codes=["compound_queue_not_empty"],
                feature_id=queued_feature,
                workstream_id=active_sprint_id,
                evidence_path=relative_path(tracked_work_path, repo_root),
            )

        return dispatch_active_sprint(
            repo_root,
            entry=active_entry,
            feature=feature,
            live_status=live_status,
        )

    if active_pointer is not None:
        parked_entry = local_by_id.get(active_pointer)
        if parked_entry is not None and parked_entry["phase"] in PARKED_PHASES:
            return route(
                "state-update",
                reason_codes=["parked_sprint_marked_runnable_globally"],
                workstream_id=active_pointer,
                evidence_path=relative_path(parked_entry["status_path"], repo_root),
            )
        return route(
            "state-update",
            reason_codes=["missing_local_runnable_sprint"],
            workstream_id=active_pointer,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    if queue:
        queued_feature_id = queue[0]
        queued_feature = next((item for item in backlog if item.get("id") == queued_feature_id), None)
        workstream_id = None
        if isinstance(queued_feature, dict):
            raw_sprint_id = queued_feature.get("sprint_id")
            if isinstance(raw_sprint_id, str) and raw_sprint_id.strip():
                workstream_id = raw_sprint_id.strip()
        return route(
            "compound-capture",
            reason_codes=["compound_queue_not_empty"],
            feature_id=queued_feature_id,
            workstream_id=workstream_id,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    brainstorm_item, brainstorm_errors = select_next_feature(backlog, {"needs_brainstorm"})
    if brainstorm_errors:
        return route(
            "state-update",
            reason_codes=brainstorm_errors,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )
    if brainstorm_item is not None:
        feature_id = str(brainstorm_item.get("id", "")).strip() or None
        workstream_id = None
        raw_sprint_id = brainstorm_item.get("sprint_id")
        if isinstance(raw_sprint_id, str) and raw_sprint_id.strip():
            workstream_id = raw_sprint_id.strip()
        return route(
            "generator-brainstorm",
            reason_codes=["ready_needs_brainstorm_backlog_item"],
            feature_id=feature_id,
            workstream_id=workstream_id,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    pending_item, pending_errors = select_next_feature(backlog, {"pending"})
    if pending_errors:
        return route(
            "state-update",
            reason_codes=pending_errors,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )
    if pending_item is not None:
        feature_id = str(pending_item.get("id", "")).strip() or None
        workstream_id = None
        raw_sprint_id = pending_item.get("sprint_id")
        if isinstance(raw_sprint_id, str) and raw_sprint_id.strip():
            workstream_id = raw_sprint_id.strip()
        return route(
            "generator-proposal",
            reason_codes=["ready_pending_backlog_item"],
            feature_id=feature_id,
            workstream_id=workstream_id,
            evidence_path=relative_path(tracked_work_path, repo_root),
        )

    if parked_entries:
        parked_entry = parked_entries[0]
        feature, _ = find_feature_for_sprint(backlog, parked_entry["sprint_id"])
        feature_id = None
        if isinstance(feature, dict):
            raw_feature_id = feature.get("id")
            if isinstance(raw_feature_id, str) and raw_feature_id.strip():
                feature_id = raw_feature_id.strip()
        return no_family_child(
            reason_codes=["waiting_on_parked_human_gate", "no_dependency_ready_backlog_item"],
            feature_id=feature_id,
            workstream_id=parked_entry["sprint_id"],
            resume_from=str(parked_entry["status"].get("resume_from", "")).strip() or None,
            evidence_path=relative_path(parked_entry["status_path"], repo_root),
        )

    return no_family_child(
        reason_codes=["no_dependency_ready_backlog_item"],
        evidence_path=relative_path(tracked_work_path, repo_root),
    )


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).expanduser().resolve()
    decision = compute_decision(repo_root)
    validate_output_shape(decision)
    print(json.dumps(decision, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
