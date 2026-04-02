---
name: harness-design
description: Use when the real problem is cross-session delivery control: deciding whether work should stay in one session, resume through `context-compaction`, or run through a planner/generator/evaluator loop with explicit handoffs, return paths, canonical live artifacts, and a postflight compound-extraction gate.
---

# Harness Design

Use this skill to define the control model for work that will span resets, handoffs, or independent verification.

This skill owns orchestration and control. It does not implement the product work, approve the current implementation slice, run browser QA, or extract durable knowledge — those belong to the generator, `contract-review`, `frontend-evaluator`, and `compound` respectively. When orchestrated work finishes, this skill defines the postflight handoff to `compound` for knowledge extraction.

## Boundary

Use this skill when:
- the team must choose between one uninterrupted session, a resumed continuation, or a planner/generator/evaluator loop
- work will cross session boundaries and needs explicit baton passing instead of implicit memory
- independent evaluation must be separated from generation so pass/fail decisions stay credible
- the main uncertainty is orchestration, handoff truthfulness, or retry ownership rather than product scope or implementation details
- completed work needs a structured postflight that routes to `compound` for lesson extraction before the session ends

Do not use this skill when:
- the router can already choose the next ordinary stage without more control design
- the main need is approving or rejecting the current implementation slice — use `delivery-control/contract-review`
- the main need is a PRD, plan review, implementation, or browser QA rather than the control model around that work
- the request only says "be more organized" or "track status better" without a concrete cross-session or role-separation problem
- the main need is extracting lessons or updating durable memory after work is done — use `delivery-control/compound` directly

## Core Contract

- Choose exactly one execution mode: `single-session`, `compacted-continuation`, or `planner-generator-evaluator`.
- Make the choice from observable conditions such as session-boundary risk, context volume, independent-verification needs, and defect-routing needs.
- Name `context-compaction` as the canonical mechanism for `compacted-continuation`. Do not describe compaction as an ad hoc summary.
- Keep planner, generator, and evaluator as separate owners. Planner and evaluator must not collapse into the same role.
- Define the handoff artifacts, pass/fail gates, and return paths before any implementation begins.
- When the workflow uses a current implementation-slice contract, `docs/live/contract.md` is the canonical live artifact for that slice.
- `delivery-control/contract-review` is the authoritative approval lane for the current implementation slice. This skill decides whether that lane is required and who must revise a rejected contract; it does not self-approve.
- When live docs are part of the workflow, require honest updates before each baton pass so the next role reads current truth rather than stale intent.
- Preserve goal lineage: the source goal, plan goal, and current phase goal must remain linked until the user explicitly retires or replaces the work.
- Rehydrate from stored truth before phase 1 and after every compaction; do not continue from chat memory alone.
- Stay portable. Do not assume a vendor-specific runtime, daemon, background supervisor, or always-on agent framework.
- **Postflight rule:** every non-trivial control model must name whether a compound-extraction handoff is required at completion. If the work produced lessons, decisions, or durable truths, the postflight routes to `delivery-control/compound`. If not, state that no extraction is needed and why.

## Mode Selection

Choose the mode by the dominant control risk.

### `single-session`
Use this mode when all of the following are true:
- one agent can complete the next meaningful slice without crossing a session reset
- the work fits in a single bounded attempt without context pressure
- no independent evaluator is needed before the next decision
- failures can be handled directly by the same agent without ambiguous ownership

Choose `single-session` because the work is small and bounded, not because no one has thought about alternatives.

### `compacted-continuation`
Use this mode when:
- the same role should continue the work, but the session will likely reset or exceed comfortable context size
- continuity depends on preserving current state, decisions, touched files, and next action across sessions
- the main problem is state transfer, not role separation or independent acceptance

For this mode, `context-compaction` is the canonical mechanism. Use it to produce the continuation snapshot and keep the same role responsible after the reset.

Do not choose `compacted-continuation` when the real need is skeptical verification, explicit retry routing between roles, or multi-role control.

### `planner-generator-evaluator`
Use this mode when any of these are true:
- the work is large enough that planning, building, and judging should not happen inside one role
- browser-facing, risky, or high-cost changes require independent pass/fail evaluation
- repeated retries are plausible and must route to the correct owner instead of looping vaguely
- the team needs explicit contracts for what the planner decides, what the generator may change, what the contract reviewer may reject before execution, and what the evaluator may reject after execution

Choose this mode only when role separation buys real control. Do not use it as ceremony for routine work.

## Role Ownership

### Planner
Owns:
- choosing the execution mode
- drafting scope, contracts, acceptance gates, and handoff artifacts
- deciding what the generator is allowed to change
- deciding when `delivery-control/contract-review` must approve the current slice before execution
- deciding whether a reported defect is actually a scope, contract, or orchestration problem

Does not own:
- implementing the code or content changes
- approving its own current-slice contract when the contract-review lane exists
- grading its own plan as the final evaluator

### Generator
Owns:
- executing the plan inside the permitted boundary
- updating the agreed handoff artifacts with what actually changed, what was verified, and what remains true or blocked
- returning implementation defects with concrete evidence when the plan was followed but the output failed

Does not own:
- expanding scope silently
- redefining acceptance criteria during implementation
- self-certifying contract approval or independent acceptance when those lanes exist

### Evaluator
Owns:
- checking the delivered work against the planner's contract and the observable acceptance gate
- reporting pass, fail, and defect evidence clearly enough that the next owner knows what must change
- preserving independence from generation so the evaluation is not a self-justification loop

Does not own:
- writing the implementation fix
- rewriting the plan unless the failure proves the plan itself is wrong

## Handoff Artifacts

For any non-trivial control model, define these artifacts explicitly:
- `docs/live/current-focus.md` — current objective and active boundary
- `docs/live/contract.md` — canonical current implementation-slice contract and allowed change boundary
- `docs/live/roadmap.md` — source goal, plan goal, phase ledger, goal changes, and resume rules for phased work
- `docs/live/runtime.md` — current execution mode, baton owner, and transition rules
- `docs/live/progress.md` — progress record with touched files and verification evidence
- `docs/live/qa.md` — evaluation record when an evaluator exists
- next-owner instruction stating who acts next and why (written into `docs/live/current-focus.md`)

### Postflight Compound Handoff

At the end of orchestrated work, the control model must produce a handoff decision:
- **Extract:** route to `delivery-control/compound` with a note naming what to extract (failed approaches, policy decisions, debugging insights, convention locks).
- **Skip:** state that no compound extraction is needed because the work produced no durable knowledge worth archiving.

The postflight decision is part of the control artifact, not an afterthought. Write it before the final baton pass so the receiving role — or the user — can act on it immediately.

When live docs are in use, update them before handoff with the current truth. At minimum, the receiving role must be able to recover:
- what mode is active
- what was changed
- what was verified
- what failed
- who owns the next action
- what the original source goal is
- what phase goal is active now
- whether the user changed direction and retired the old goal

## Return Paths

Every failure must route to one owner.

- **Implementation defect** -> return to the generator. The plan was still valid, but the produced work did not satisfy it.
- **Slice-contract defect** -> return to the planner or contract author. The current implementation slice was not safe to execute as written and must be revised before generation starts.
- **Scope, contract, or orchestration defect discovered after execution** -> return to the planner. The control model, boundary, or acceptance logic was wrong or incomplete.
- **Environment or setup blocker** -> mark the work as `blocked`. Do not pretend planning or implementation can proceed until the external blocker is removed.
- **Goal-lineage drift** -> return to the planner. If the current phase can no longer be reconciled with the source goal or roadmap, the control artifact is stale and must be rewritten before more implementation continues.

If a failure could fit more than one bucket, choose the earliest broken contract. Do not send generator work back to the planner just because the failure was discovered late.

## Output Shape

Return a compact control artifact with these sections:
1. **Chosen mode** — exactly one of `single-session`, `compacted-continuation`, `planner-generator-evaluator`
2. **Why this mode** — the observable conditions that made the other modes wrong
3. **Role ownership** — planner, generator, evaluator, and contract-review boundaries when used
4. **Handoff artifacts** — what must exist before baton passing
5. **Return paths** — implementation defect, slice-contract defect, scope/contract/orchestration defect, environment blocker
6. **Postflight** — whether compound extraction is required and what to extract, or why extraction is skipped
7. **Next route** — the next skill or work lane that should execute under this control model

## Related framework

The broader Superpowers-replacing workflow pack lives in [harness-engineering](../../harness-engineering/SKILL.md). This skill stays focused on cross-session control, while the framework leaf owns the full coding workflow.

## Failure Modes to Avoid

- Treating ordinary stage selection as harness design.
- Calling a vague summary "compaction" instead of using `context-compaction`.
- Letting planner and evaluator collapse into one role and then calling the result independent.
- Using planner/generator/evaluator loops as a prestige pattern for routine work.
- Using harness-design to approve or reject the current slice instead of routing that judgment to `delivery-control/contract-review`.
- Writing handoffs that say what was intended instead of what is currently true.
- Hiding environment blockers inside implementation retries.
- Describing a runtime-specific agent service, daemon, or orchestrator as if it were required by this skill.
- Skipping the postflight compound decision — every control artifact must state extract or skip.
- Routing to `compound` during active implementation instead of at completion.