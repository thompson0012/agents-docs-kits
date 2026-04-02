# Project Progress Ledger

Append reviewed outcomes here: archived PASS results and any active FAIL, BUILD_FAILED, or parked-human states that materially change the next action. Routine execution chatter still belongs in `.harness/<feature-id>/` and the current backlog entry in `features.json`.

## Entry format

Each reviewed or reconciled entry should record:

- the date and feature id,
- final or parked status,
- what materially shipped, failed, or blocked progress,
- where the archived or active sprint artifacts live,
- retry budget and clean restore requirements when another execution pass is possible,
- the next recommended action for the project.

## [2026-04-02] FEAT-000: Bootstrap Harness Starter

- **Status**: Archived after successful closeout
- **Outcome**: Established the initial harness skeleton, durable state files, and the first resumable sprint folder.
- **Artifacts**: `docs/archive/FEAT-000_timestamp/`
- **Evidence**: Final contract, handoff, review, and status snapshot were preserved with the archive.
- **Next Action**: Start proposal work for `FEAT-001`, then continue that sprint until it reaches a reviewed outcome.

## [2026-04-02] FEAT-001: Dark Mode Toggle Polish

- **Status**: Review failed; sprint remains the single runnable active sprint
- **Outcome**: The toggle behavior is functional, but the adversarial review failed on dark-mode contrast and on the generic checkbox-style control.
- **Artifacts**: `.harness/FEAT-001/`
- **Evidence**: `review.md`, `qa.md`, `runtime.md`, `handoff.md`, and `status.json` keep the failed review evidence intact.
- **Retry Budget**: Attempt `1` of `3` is consumed.
- **Clean Restore**: The next execution pass must start from `disposable-worktree:feat-001-attempt-02-baseline`, or an equivalent durable restore boundary. Do not default to destructive reset unless the workspace is explicitly disposable.
- **Next Action**: Restore FEAT-001 from the clean boundary, resume `generator-execution` from `.harness/FEAT-001/review.md`, rerun build/startup triage after the fix, and only then return to `adversarial-live-review`.

## Current focus convention

Do not add an entry for every execution checkpoint. While `FEAT-001` is active, its detailed source of truth is:

- `docs/live/features.json` for project-level priority, parked-vs-runnable state, retry budget, and next action,
- `.harness/FEAT-001/status.json` for phase, resume pointer, attempt counts, and clean-restore metadata,
- `.harness/FEAT-001/review.md` for corrective directives after adversarial review.

If a sprint moves to `awaiting_human` or `escalated_to_human`, record that parked state here and in `features.json`, then choose new work only from dependency-ready pending features.
