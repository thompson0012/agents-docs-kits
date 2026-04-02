---
name: harness-engineering
description: Use when you want the front-door harness workflow for coding work: frame the request, route control decisions to delivery-control, keep handoffs truthful, and close with independent evaluation plus extract-or-skip compounding.
---

# Harness Engineering

## Overview

This is the narrative front door for the repo's harness-style delivery workflow.
It explains the sequence an agent should follow, but it does not become a second control plane.

The loop is simple:
frame the work, get the right control decision, approve a real contract, execute honestly, evaluate independently when needed, then close with an explicit extract-or-skip decision.

## Authoritative owners

- `delivery-control/harness-design` owns execution-mode and control-plane decisions.
- `delivery-control/contract-review` owns contract approval or rejection before implementation starts.
- `delivery-control/frontend-evaluator` owns independent browser-facing acceptance.
- `delivery-control/compound` owns durable knowledge extraction after work completes.
- `labs21-product-suite` owns idea -> PRD / baseline architecture work.
- `context-compaction` is the continuation helper when the same role must resume after a reset.

This skill stays the front door by narrating the workflow and pointing each decision to its canonical owner.

## Core contract

- Start here when the request is already coding work and the agent needs one coherent delivery workflow.
- If the request is still product definition, route to `labs21-product-suite` before using this pack.
- Do not make up private control rules here. When execution mode or baton design matters, defer to `delivery-control/harness-design`.
- Do not approve contracts here. Use `delivery-control/contract-review` as the gate.
- Keep article artifact names like `contract.md`, `proposal_feedback.md`, `handoff.md`, and `project_sync.md` as vocabulary only unless they map to canonical repo docs.
- Treat `docs/live/contract.md` as the canonical approved contract and `docs/reference/requirements.md` as the canonical requirements reference when those docs exist.

## Workflow

1. Frame the request.
   - If the work is still idea -> PRD / baseline architecture, hand it to `labs21-product-suite`.
   - Otherwise use the planner reference to decide whether the work can stay direct or needs an explicit control-plane decision.
2. Choose the control path.
   - If control design, cross-session execution, or explicit role separation matters, hand the decision to `delivery-control/harness-design`.
   - If the work is already a bounded direct slice, continue without pretending this skill is a router family.
3. Propose the implementation slice.
   - Use the proposal reference to define target files, forbidden changes, launch command, QA script, success criteria, and evidence expectations.
4. Gate the contract.
   - Use the contract-review reference as the bridge into `delivery-control/contract-review`, which approves or rejects the slice.
5. Execute the approved slice.
   - Use the execution reference to build against the approved contract, keep live docs truthful, and leave an honest handoff.
6. Evaluate independently when needed.
   - Use the frontend-evaluator reference when browser-facing work needs a separate pass / fail / blocked judgment.
7. Close the loop.
   - Use the postflight reference to decide whether the completed run should route to `delivery-control/compound` or explicitly skip extraction.

## What this replaces

This skill is the repo-native front door for a Superpowers-style workflow pack.

- Anthropic harness practice appears as explicit control decisions, truthful handoffs, and independent evaluation.
- Compound Engineering practice appears as an explicit extract-or-skip closeout through `delivery-control/compound`.
- The macro-boundary stays intact: one coherent workflow pack, not a new top-level router family.

## References

- [planner reference](references/planner.md)
- [generator contract proposal](references/generator-proposal.md)
- [contract review reference](references/contract-review.md)
- [generator execution reference](references/generator-execution.md)
- [frontend evaluator reference](references/frontend-evaluator.md)
- [postflight reference](references/postflight.md)

## Final checklist

- [ ] The front door is clear, but control-plane ownership stays explicit.
- [ ] Execution-mode choice lives in `delivery-control/harness-design`, not here.
- [ ] Contract approval lives in `delivery-control/contract-review`, not here.
- [ ] Evaluation and compounding stay in their own delivery-control lanes.
- [ ] The workflow reads as one coherent pack without inventing extra routers.
