# Harness Design Spec: Multi-Session Delivery Control and Strict Frontend Evaluation

Date: 2026-03-25
Status: Draft approved for spec review

## Summary

Add a first-class harness layer to the portable skill suite so the repository can describe and route work that needs stronger control than a single long-running agent session. The new layer should define when delivery stays in one session, when it compacts and resumes, and when it escalates into a planner/generator/evaluator loop with explicit handoff artifacts and independent verification.

At the same time, add a strict frontend evaluator path that treats browser-facing acceptance as an independent gate rather than only the builder's own QA loop.

## Problem

The current suite covers adjacent pieces but not the full harness shape:

- `software-delivery` already routes discovery, spec work, plan review, implementation, and readiness checks.
- `website-building` already requires a serious browser QA loop with an inventory, functional pass, visual pass, viewport checks, and exploratory testing.
- `context-compaction` already preserves continuation state across sessions.

What is missing is the orchestration layer that tells the truth about how non-trivial work should be controlled across multiple sessions and roles.

### Current gaps

1. No first-class guidance for when to use a single session versus compaction versus planner/generator/evaluator orchestration.
2. No portable file-based handoff contract for multi-session baton passing.
3. No independent skeptical evaluator role for browser-facing deliverables.
4. No closed-loop rule that decides whether failures return to the generator or escalate back to the planner.

## Goals

1. Add a portable harness-design surface for multi-session software delivery.
2. Add a strict frontend evaluator skill that can independently pass or fail browser-facing work.
3. Reuse existing top-level skills honestly instead of cloning them under a new family.
4. Preserve portability by avoiding vendor-specific runtimes, telemetry, slash-command assumptions, or daemon expectations.
5. Make handoff state explicit enough that a fresh session can continue work without inheriting hidden assumptions.

## Non-Goals

- Do not ship a runtime-specific implementation of a long-running agent harness in this change.
- Do not replace `website-building` or move its existing QA guidance.
- Do not turn the evaluator into a builder, fixer, or plan author.
- Do not add a generic review skill with fuzzy ownership.
- Do not require new atomic skills outside the harness-specific additions.

## Proposed Package Shape

Add two nested children under `templates/base/.agents/skills/software-delivery/`:

1. `harness-design/`
   - Purpose: define delivery-control patterns for work that has already been recognized as needing explicit cross-session coordination or role separation.
   - Scope: planner/generator/evaluator role boundaries, session-shape selection beyond a normal single-session router handoff, handoff artifacts, reset-versus-compaction rules, and closed-loop escalation.
   - Boundary: this child does not duplicate the base `software-delivery` router's normal stage selection. The router still chooses discovery, spec, review, implementation, or readiness for ordinary work. `harness-design` activates only when the main problem is cross-session orchestration, explicit baton passing, or independent evaluation design.

2. `frontend-evaluator/`
   - Purpose: provide an independent pass/fail gate for browser-facing deliverables.
   - Scope: requirement-to-evidence verification, skeptical browser validation, defect severity, retry contracts, and evaluator verdicts.
   - Boundary: this child does not build features or fix defects.

These two children are family-specific additions. Shared top-level skills remain shared:

- `website-building` for building and builder-side browser QA
- `coding-and-data` for repo-backed implementation
- `feature-spec` for scoped artifacts
- `self-cognitive` for readiness reflection, retrospectives, and confidence calibration
- `context-compaction` for session-state compression and handoff continuity

## Delivery Role Model

The harness defines three roles.

### Planner

Owns:
- cross-session execution-shape selection once `harness-design` has been chosen
- scope and success criteria
- work partitioning
- evaluator gates
- escalation decisions when repeated failures suggest the plan is wrong rather than merely exposing an implementation defect

Does not own:
- implementation details inside the build slice
- signoff based only on generator claims

### Generator

Owns:
- implementing one bounded slice
- updating touched files and claimed verification
- running builder-side QA before requesting evaluation
- stating assumptions, known gaps, and evidence honestly

Does not own:
- final acceptance of its own browser-facing work
- rewriting the evaluation rubric ad hoc

### Evaluator

Owns:
- independently verifying deliverables from the artifacts and stated requirements
- running skeptical browser-facing checks for frontend work
- returning only `pass`, `fail`, or `blocked`
- specifying exact retry conditions when the work fails

Does not own:
- silently fixing the work under review
- accepting plausible but unverified claims

## Session-Control Modes

The harness should define three explicit execution shapes.

### 1. `single-session`
Use when:
- the change is small
- risk is low
- the same session can honestly hold planning, implementation, and verification without loss of control

### 2. `compacted-continuation`
Use when:
- the main problem is context length, not correctness separation
- the same role should continue after context is compressed
- no independent evaluator boundary is needed yet

### 3. `planner-generator-evaluator`
Use when:
- the work is non-trivial, multi-step, or high-risk
- frontend/browser-facing quality is important enough to require independent acceptance
- the team needs fresh-session skepticism between build and signoff

### Selection rule

Choose the smallest mode that satisfies the observable risk:

- Use `single-session` when the work fits one bounded delivery slice, the same session can both build and verify honestly, and no fresh-session skepticism or baton handoff is required.
- Use `compacted-continuation` when the same role should keep working, the primary pressure is context length or continuity, and the handoff artifacts do not need an independent verdict before work continues.
- Use `planner-generator-evaluator` when the output is browser-facing or otherwise high-risk, when one session would otherwise both generate and accept its own work, or when the work is large enough that explicit baton passing and retry loops are part of the control model.
- Escalate from generator failure back to planner only when the evaluator exposes a scope, contract, or orchestration defect rather than a fixable implementation defect.

## File-Based Handoff Contract

Reuse the live docs as the backbone and add only the minimal new control files.

### Existing canonical files

- `docs/live/current-focus.md`
  - objective, scope, constraints, success criteria
- `docs/live/progress.md`
  - current state, touched files, claimed verification, next action
- `docs/live/todo.md`
  - queued and sequenced work

### New proposed files

#### `docs/live/runtime.md`
Purpose: describe the current execution shape and baton state.

Suggested sections:
- current mode (`single-session`, `compacted-continuation`, or `planner-generator-evaluator`)
- current baton owner (`planner`, `generator`, `evaluator`)
- entry criteria for the next role
- reset-versus-compaction rule for the next transition
- artifact pointers the next role must read first
- stop conditions and escalation paths

#### `docs/live/qa.md`
Purpose: preserve evaluator-grade evidence and verdicts across attempts.

Suggested sections:
- requirement-to-evidence matrix
- browser QA evidence summary
- defects grouped by `blocker`, `major`, and `minor`
- evaluator verdict (`pass`, `fail`, or `blocked`)
- retry contract for the next generator attempt

## Closed-Loop Behavior

For browser-facing work, the truthful loop becomes:

`Plan -> Build -> Builder QA -> Independent Frontend Evaluation -> Fix -> Re-evaluate`

Not:

`Plan -> Build -> Self-report success`

### Return-path rule

- If the evaluator finds an implementation defect, return to the generator.
- If the evaluator finds that the work implemented the wrong slice or violated plan assumptions, escalate to the planner.
- If the evaluator is blocked by environment or missing setup, return `blocked` with the unblock condition recorded explicitly.

## Frontend Evaluator Contract

`software-delivery/frontend-evaluator` should treat browser-facing signoff as an independent gate.

### Required output

- **Verdict**: `pass`, `fail`, or `blocked`
- **Evidence matrix**: each user-visible claim mapped to a concrete check and observed evidence
- **Defect list**: each defect with severity, reproduction steps, and why it matters
- **Retry instructions**: exact changes or checks required before re-review

### Minimum pass criteria

A browser-facing deliverable passes only if all of the following are true:

1. Every user-visible claim is mapped to evidence.
2. The evaluator completed an independent browser run from a fresh evaluator stance rather than relying on the generator's narrative.
3. The evaluator executed the shared interactive browser QA methodology currently documented at `website-building/shared/12-playwright-interactive.md`, including the functional pass, visual pass, viewport-fit checks, and exploratory pass, and recorded the resulting evidence in the evaluator artifact. Implementation should declare this as an explicit cross-family dependency in the relevant routing metadata rather than leaving the path as an implicit assumption.
4. Main-flow accessibility basics were checked and any failures were recorded truthfully.
5. No unresolved blocker or major defect remains.

### Automatic fail conditions

Fail the deliverable if any of the following are true:

- the evaluation relies on generator assertions without independent verification
- the shared browser QA workflow was only partially executed or not recorded against the evaluator artifact
- screenshots or observations do not support the claimed behavior
- only happy-path behavior was checked
- visible clipping, weak contrast, broken layering, or missing key states are dismissed as minor polish
- the evaluator cannot reproduce the environment and no honest `blocked` record is produced

## Relationship to Existing Skills

### `website-building`
Remains the builder-facing path for web implementation and builder-side browser QA.

Update its guidance and metadata so that non-trivial browser-facing work explicitly recommends `software-delivery/frontend-evaluator` as a follow-on gate after builder-side QA. This recommendation should be discoverable from the `website-building` flow, not only from `software-delivery`.

### `context-compaction`
Remains the mechanism for compressing session state.

`harness-design` should reference it as the correct tool when the role stays the same but the session needs a fresh context budget.

### `self-cognitive`
Remains the path for readiness reflection, risk calibration, and lessons learned.

It should not be treated as the default frontend acceptance gate. Acceptance belongs to the evaluator; reflective readiness remains a separate decision.

## Routing Changes

### `using-agent-practices`
Extend routing guidance so requests about:
- multi-session runtime control
- planner/generator/evaluator orchestration
- explicit delivery harnesses
- strict frontend acceptance gates

route to `software-delivery` rather than forcing direct implementation or generic reasoning.

### `software-delivery`
Add two new routing outcomes:
- `Route to software-delivery/harness-design.`
- `Route to software-delivery/frontend-evaluator.`

Decision-order additions:
1. Insert `harness-design` before the plan-review lanes and use it when the main problem is delivery control across multiple sessions, explicit baton passing, or planner/generator/evaluator separation. Do not route there for ordinary single-session stage selection that the base router already handles.
2. Insert `frontend-evaluator` immediately before the existing website-building step and use it when browser-facing work needs independent acceptance rather than more implementation guidance.
3. Narrow the existing website-building step so it continues to own building and builder-side QA for user-facing web work, but not independent evaluator signoff.

### `website-building` follow-on discovery
Add a recommendation path from `website-building` into `software-delivery/frontend-evaluator` so that a builder finishing browser QA can discover the independent evaluator without leaving the web flow blind. This should be encoded in the website-building metadata and referenced in the relevant child guidance.

## Verification and Acceptance for This Design Work

The design is complete when:

1. The new `software-delivery` child boundaries are explicit and non-overlapping.
2. The handoff contract names the minimal file surfaces needed for multi-session continuation.
3. The evaluator contract defines explicit pass/fail/blocked outcomes and hard fail conditions.
4. Routing guidance makes it clear when to choose harness design, frontend evaluation, website building, implementation, or self-cognitive review.
5. The package remains portable and vendor-agnostic.

## Open Implementation Questions

These do not block the design, but the implementation plan should settle them:

1. Whether `docs/live/runtime.md` and `docs/live/qa.md` should be added to the base template immediately or introduced as optional docs that the harness skill creates when needed.
2. Whether the evaluator should require a fixed evidence template in markdown, JSON, or both.

## Recommended Next Step

Proceed to implementation planning for:
- the two new `software-delivery` children
- the routing metadata updates
- the minimal live-doc additions for runtime and QA handoff
- the documentation updates that connect builder QA to independent frontend evaluation
