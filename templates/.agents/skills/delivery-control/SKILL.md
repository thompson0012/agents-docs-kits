---
name: delivery-control
description: Use when a repository already uses `using-agents-stack` and the work needs an overlay control policy: deciding whether the workflow should stay single-session, use `context-compaction`, require slice approval, require independent browser QA, or close with compound extraction. This family adds SOP on top of agents-stack; it does not replace the orchestrator.
---

# Delivery Control

This router layers delivery policy on top of the agents-stack workflow. `using-agents-stack` still chooses and dispatches the next phase child; `delivery-control` decides which control gate, handoff rule, or postflight obligation must apply around that work.

Do not perform the phase work here. Choose the narrowest control-policy child, then hand off.

## Core Contract

- Keep `using-agents-stack` as the phase orchestrator. `delivery-control` only adds governance, gates, and postflight policy.
- Defer greenfield product definition (Strategy, MVP, PRDs, System Architecture) to `greenfield-product`.
- Choose exactly one primary control route or decide that no delivery-control route fits.
- Use `references/children.json` as the source of truth for child boundaries, prerequisites, and install hints.

## Decision Order

Apply these checks in order.

### 0. Is this a net-new product or greenfield initiative?
Route to `greenfield-product` if the user is starting from a raw idea, needs a strategic blueprint, a comprehensive PRD, or a baseline system architecture.

### 1. Does the repository already use agents-stack and need the control model layered on top of it?
Route to `delivery-control/harness-design` when the work needs explicit control over single-session vs compacted-continuation vs planner/generator/evaluator loops, plus the baton rules, live artifacts, pass/fail boundaries, and postflight extract-or-skip decision that keep multi-session execution honest.

Use this lane for orchestration policy, not ordinary stage selection.

### 2. Is the main need approving or rejecting the current implementation slice before execution?
Route to `delivery-control/contract-review` when the work already has a proposed implementation slice and the real decision is whether that slice is narrow enough, honest enough, and observable enough to let execution start.

Use this lane for slice approval. Do not broaden it into generic design review, code review, or implementation.

### 3. Is the main need independent browser-facing acceptance?
Route to `delivery-control/frontend-evaluator` when browser-facing work already exists and the user wants a skeptical pass/fail QA gate with evidence, defects, and retry guidance.

This lane verifies; it does not implement or fix.

### 4. Is the main need structured knowledge extraction from completed work?
Route to `delivery-control/compound` when a feature, phase, or delivery cycle has completed and the team wants to extract reusable lessons and durable truths into `docs/reference/lessons.md` and `docs/reference/memory.md`.

This lane extracts; it does not implement, orchestrate, evaluate, or approve the current slice.

### 5. No delivery-control route
If none of the above fits cleanly, do not force this family. Answer directly or let the agent fall back to generic repo implementation skills.

## Router Output

Return one of these forms and then invoke the selected skill if needed:

- `Route to greenfield-product`.
- `Route to delivery-control/harness-design.`
- `Route to delivery-control/contract-review.`
- `Route to delivery-control/frontend-evaluator.`
- `Route to delivery-control/compound.`
- `No delivery-control route fits; answer directly.`

Add one sentence explaining why the selected route is the narrowest correct fit.

## References

- `references/children.json`

## Failure Modes to Avoid

- routing to `delivery-control` for greenfield product definition, v1.0 PRDs, or baseline system architecture instead of `greenfield-product`
- using `delivery-control/harness-design` as a second orchestrator instead of the control overlay on top of `using-agents-stack`
- routing `delivery-control/contract-review` for generic architecture review or code review after implementation
- treating `delivery-control/contract-review` as a generic review family instead of a pre-execution slice-approval gate
- routing `delivery-control/compound` during active implementation instead of after work completes
- routing `delivery-control/compound` for generic note-taking or progress journaling instead of structured knowledge extraction