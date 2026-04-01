# Architecture Reference

## Current Shipped Surfaces

<!--
List active surfaces here: skill routers, direct leaves, doc surfaces.
Keep this section honest — if a surface is removed, delete it in the same change.
-->

-

## Historical / Removed Names

<!--
Record names that no longer exist so future sessions do not reference stale surfaces.

| Removed name | What replaced it |
|-------------|-----------------|
| … | … |
-->

-

## Invariants

<!--
Architectural truths the codebase enforces. Add entries as they emerge.

Key invariants to capture:
- Suite boundary honesty: routers may claim only currently shipped children.
- Delivery-control is a three-lane control plane: `harness-design` (orchestration),
  `frontend-evaluator` (independent evaluation), `compound` (historical extraction).
  Orchestration designs session boundaries and pass/fail gates. Evaluation verifies
  without implementing. Compound distills postflight signals into the two durable
  archives — it does not orchestrate or evaluate.
- Compound lane owns postflight knowledge: only `compound` writes to the durable
  archives (`docs/reference/memory.md` for truths, `docs/reference/lessons.md` for
  reusable failure-mode / fix patterns). Orchestration and evaluation surfaces raw
  signals that compound distills.
- Memory ≠ lessons: `memory.md` records durable truths that survive sessions;
  `lessons.md` records reusable failure-mode / fix patterns. A truth is not a lesson;
  a lesson is not a truth.
- Template inertness: generated scaffolds contain no prefilled content.
- Router metadata as source of truth: `references/children.json` is the authority for
  child inventory.
-->

-

## Major Components

<!--
Map high-level components, their responsibility, and key dependencies.

| Component | Responsibility | Key dependency |
|-----------|----------------|----------------|
| … | … | … |

Include at minimum:
- Top-level suite router
- Delivery-control family (orchestration, evaluation, extraction lanes)
- Product suite router
- Design and reasoning family routers
- Doc surfaces (live state, durable reference, template scaffold)
-->

-
