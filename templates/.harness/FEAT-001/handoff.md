# Handoff: FEAT-001

## Intended task

Repair the dark-mode contrast and toggle design issues that failed review, without starting FEAT-002 or reopening contract review.

## Current checkpoint

Paused after a processed FAIL. Resume from `review.md` and re-enter generator-execution on the same sprint; the review evidence stays intact.

## Files changed in this slice

- `src/theme/ThemeProvider.tsx`
- `src/App.tsx`

## What remains unfinished

1. Raise dark-mode text contrast against `#0f172a`.
2. Replace the checkbox-style control with a purpose-built animated SVG toggle.
3. Refresh `runtime.md` and regenerate handoff evidence before the next review pass.

## Blockers

- No technical blocker was found.
- `review.md` is authoritative and must remain intact for the retry.

## First step for the next agent

Open `review.md`, apply the two corrective directives within the original contract boundary, then refresh `runtime.md` and this handoff before returning to review.

## Evidence supporting this status

- `contract.md` defines the allowed files and QA script.
- `runtime.md` captures the reproduction setup used for the failed pass.
- `qa.md` records the checked criteria and the failure evidence.
- `review.md` records the FAIL and the exact generator directives.
- `status.json` marks the sprint as `review_failed`, keeps `generator` as the owner, and points the next agent at `review.md`.
