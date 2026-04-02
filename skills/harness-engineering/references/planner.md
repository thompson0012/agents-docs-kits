---
name: planner
description: Use when you need to frame a coding request, decide whether it stays direct or needs delivery-control, and prepare the handoff without duplicating harness-design's mode-selection rules.
---

# Planner Reference

## Purpose

Frame the work before building.
This reference decides whether the request should stay on the direct harness-engineering path or be handed to `delivery-control/harness-design` for an authoritative control decision.

## Core contract

- Rehydrate from `docs/live/current-focus.md` and `docs/live/progress.md` before planning.
- If the request is actually greenfield product/spec creation, route it to `labs21-product-suite` instead of forcing it into harness engineering.
- Decide whether the request is:
  - product definition -> `labs21-product-suite`
  - a bounded direct build slice -> stay in `harness-engineering`
  - non-trivial delivery control -> `delivery-control/harness-design`
- When handing off to `delivery-control/harness-design`, pass the facts that matter: objective, context-pressure risk, need for independent evaluation, likely handoff artifacts, and any reason the smaller path would be dishonest.
- Do not restate the detailed mode matrix here. `delivery-control/harness-design` owns the authoritative rules for `single-session`, `compacted-continuation`, and `planner-generator-evaluator`.
- Surface whether the next phase will need a canonical approved contract in `docs/live/contract.md` and which requirement source in `docs/reference/requirements.md` or live docs should anchor it.

## Workflow

1. Read the current live truth.
2. Classify the request: product definition, direct delivery slice, or control-plane problem.
3. If direct delivery is still honest, keep the work on the harness-engineering path.
4. If control design is needed, hand the case to `delivery-control/harness-design` with the specific risks and expectations rather than your own replacement rules.
5. State what must be true before a proposal can become a contract.

## Output shape

- route decision
- why this is the narrowest honest route
- required inputs for the next owner
- contract preconditions
- whether a postflight extract-or-skip decision is expected at the end

## Failure modes

- Treating every ordinary build slice as a harness-design problem.
- Rewriting the mode-selection matrix instead of deferring to `delivery-control/harness-design`.
- Planning execution details before the control owner has chosen the path.
- Forgetting to identify the requirement source that the future contract must anchor to.
