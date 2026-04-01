# Code Map

## If you want to…

<!--
Quick-lookup table mapping goals to starting points.

| Goal | Start here |
|------|-----------|
| Find the right skill for a request | top-level suite router |
| Route software delivery work | `delivery-control` router |
| Design cross-session orchestration | `delivery-control/harness-design` |
| Run independent browser acceptance | `delivery-control/frontend-evaluator` |
| Extract durable lessons or memory after delivery | `delivery-control/compound` → writes to `docs/reference/memory.md` and `docs/reference/lessons.md` |
| Understand the live-doc contract | `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md` |
| … | … |
-->

| Goal | Start here |
|------|-----------|
| | |

## Key Paths

<!--
List skill routers, direct leaves, and doc surfaces.

Skill routers route to children:
- Top-level suite router — owns the shipped boundary.
- Delivery-control router — three-lane control plane:
  `harness-design` (orchestration), `frontend-evaluator` (evaluation),
  `compound` (durable knowledge extraction into memory and lessons archives).
- Product suite, design-family, and reasoning-family routers.

Direct leaves have no children.

Doc paths:
- `docs/live/` — mutable repo-level execution state.
- `docs/reference/` — durable project context (architecture, codemap, memory, lessons, implementation, design).
  Memory and lessons are the compound lane's write targets for postflight knowledge.
-->

-

## Entrypoints

-

## Router metadata

<!--
Each router package stores its child inventory in `references/children.json`.
That file is the source of truth for which children the router owns and when to route to each child.
-->

-
