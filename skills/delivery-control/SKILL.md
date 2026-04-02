---
name: delivery-control
description: Use when a software feature request needs delivery-control orchestration, current-slice contract approval, independent frontend QA, or structured knowledge extraction from completed work. For greenfield product definition (strategy, PRDs, v1 architecture), use labs21-product-suite instead.
---

# Delivery Control

Use this router to enforce delivery governance, execution honesty, and durable knowledge capture on feature work that is already defined.

For net-new product creation, raw ideas, comprehensive PRDs, or system architecture from scratch, use `labs21-product-suite` instead.

Do not perform the stage work here. Choose the narrowest next skill, then hand off.

## Core Contract

- Defer greenfield product definition (Strategy, MVP, PRDs, System Architecture) to `labs21-product-suite`. `delivery-control` governs how to deliver; `labs21-product-suite` defines what to build.
- Choose exactly one primary route or decide that no delivery-control route fits.
- Use `references/children.json` as the source of truth for child boundaries.

## Decision Order

Apply these checks in order.

### 0. Is this a net-new product or greenfield initiative?
Route to `labs21-product-suite` if the user is starting from a raw idea, needs a strategic blueprint, a comprehensive PRD, or a baseline system architecture.

### 1. Is the main need cross-session delivery control or harness design?
Route to `delivery-control/harness-design` when the work needs explicit control over single-session vs compacted continuation vs planner/generator/evaluator loops, plus the baton rules, live artifacts, pass/fail boundaries, and postflight extract-or-skip decision that keep multi-session execution honest.

Use this lane for orchestration and control. Do not use it for ordinary single-session work, current-slice approval, or the extraction itself.

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

- `Route to labs21-product-suite.`
- `Route to delivery-control/harness-design.`
- `Route to delivery-control/contract-review.`
- `Route to delivery-control/frontend-evaluator.`
- `Route to delivery-control/compound.`
- `No delivery-control route fits; answer directly.`

Add one sentence explaining why the selected route is the narrowest correct fit.

## References

- `references/children.json`

## Failure Modes to Avoid

- routing to `delivery-control` for greenfield product definition, v1.0 PRDs, or baseline system architecture instead of `labs21-product-suite`
- routing `delivery-control/harness-design` for ordinary single-session stage selection instead of true cross-session delivery control
- routing `delivery-control/harness-design` for current-slice approval instead of `delivery-control/contract-review`
- treating `delivery-control/contract-review` as a generic review family instead of a pre-execution slice-approval gate
- routing `delivery-control/compound` during active implementation instead of after work completes
- routing `delivery-control/compound` for generic note-taking or progress journaling instead of structured knowledge extraction