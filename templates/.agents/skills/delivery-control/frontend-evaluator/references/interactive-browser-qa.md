---
name: interactive-browser-qa
description: Canonical browser-facing QA workflow for delivery-control/frontend-evaluator, tied to the live slice contract and QA record.
---

# Interactive Browser QA

## Purpose

Run a skeptical browser-facing acceptance pass against the current delivery slice and produce an audit-friendly record in `docs/live/qa.md`.

## Core contract

- Use `docs/live/contract.md` as the primary acceptance source when it exists. If it does not exist, reconstruct the acceptance scope from the user request, planner or generator handoff, and observed browser-facing behavior.
- Treat `docs/live/qa.md` as the canonical evidence artifact. Record evidence as you go; do not backfill from memory.
- Use real browser interaction and observed state as the primary evidence source. Screenshots, traces, and DOM snapshots support claims; they do not replace direct verification.
- Keep the evaluation browser-facing. Check rendered behavior, responsive fit, and accessibility basics; do not turn this into a static code review.
- Distinguish environmental blockers from product defects. A broken product is `fail`; an unusable evaluation environment is `blocked`.

## Workflow

1. Rehydrate scope from `docs/live/contract.md` when present, then fill gaps from the user request, planner handoff, `docs/live/current-focus.md`, and the delivered UI.
2. Start the expected preview or app entrypoint. If startup fails or required credentials, services, or network access are missing, capture blocker evidence immediately.
3. Convert each contract clause, user-visible claim, and critical flow into explicit checks for the evidence matrix.
4. Exercise the main user journey with live interactions. Verify the observed state after each meaningful step.
5. Probe adjacent states that could invalidate the contract: loading, empty, validation, error, permission, and recovery paths when they exist in scope.
6. Check viewport fit at representative sizes for the slice. Record clipping, overflow, off-screen controls, broken layering, and focus traps as defects rather than as “polish”.
7. Check main-flow accessibility basics in the rendered experience: keyboard reachability, visible focus, meaningful names or labels, and obvious contrast or semantic failures.
8. Write `docs/live/qa.md` as you work, then issue exactly one verdict: `pass`, `fail`, or `blocked`.

## Minimum evidence

- requirement-to-evidence mapping for every verdict claim
- reproduction path and evidence pointer for each defect
- explicit note on environments and viewports checked
- accessibility basics checked and their result
- retry conditions for the next credible evaluator run

## Failure modes

- starting from a generic checklist instead of the slice contract
- treating screenshots as proof without confirming behavior
- calling a product defect `blocked`
- recording conclusions after the run from memory
- skipping exploratory browser coverage around the touched surface
