# Project Progress Ledger

Append reviewed outcomes here: archived PASS results and any active FAIL states that materially change the next action. Routine execution chatter still belongs in `.harness/<feature-id>/` and the current backlog entry in `features.json`.

## Entry format

Each reviewed entry should record:

- the date and feature id,
- final status,
- what materially shipped or closed,
- where the archived sprint artifacts live,
- the next recommended action for the project.

## [2026-04-02] FEAT-000: Bootstrap Harness Starter

- **Status**: Archived after successful closeout
- **Outcome**: Established the initial harness skeleton, durable state files, and the first resumable sprint folder.
- **Artifacts**: `docs/archive/FEAT-000_timestamp/`
- **Evidence**: Final contract, handoff, review, and status snapshot were preserved with the archive.
- **Next Action**: Start proposal work for `FEAT-001`, then continue that sprint until it reaches a reviewed outcome.

## [2026-04-02] FEAT-001: Dark Mode Toggle Polish

- **Status**: Review failed; sprint remains active
- **Outcome**: The toggle behavior is functional, but the adversarial review failed on dark-mode contrast and on the generic checkbox-style control.
- **Artifacts**: `.harness/FEAT-001/`
- **Evidence**: `review.md`, `qa.md`, `runtime.md`, `handoff.md`, and `status.json` keep the failed review evidence intact.
- **Next Action**: Resume `generator-execution` for FEAT-001 from `.harness/FEAT-001/review.md`, rework the same implementation, and then rerun adversarial-live-review.

## Current focus convention

Do not add an entry for every execution checkpoint. While `FEAT-001` is active, its detailed source of truth is:

- `docs/live/features.json` for project-level priority and next action,
- `.harness/FEAT-001/status.json` for phase and resume pointer,
- `.harness/FEAT-001/review.md` for corrective directives after adversarial review.
