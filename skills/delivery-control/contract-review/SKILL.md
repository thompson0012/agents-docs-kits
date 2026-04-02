---
name: contract-review
description: Use when the main need is approving or rejecting the current implementation slice before execution, using `docs/live/contract.md` as the canonical contract and returning a clear go/no-go verdict.
---

# Contract Review

Use this skill to decide whether the current implementation slice is ready to execute.

This skill is the authoritative approval lane for the current slice. It reviews the proposed boundary, acceptance conditions, and exposed risks in `docs/live/contract.md`, then returns a go/no-go judgment. It does not choose the control mode, implement the work, or run post-build QA.

## Boundary

Use this skill when:
- a current implementation slice already exists and the next real decision is whether execution may start
- the team wants an explicit approval or rejection of the slice contract before the generator touches files
- the contract must be checked for scope honesty, observable acceptance, and actionable boundaries rather than polished prose
- a harness-design workflow names pre-execution contract approval as a required gate

Do not use this skill when:
- the main need is deciding execution mode, baton rules, or handoff structure — use `delivery-control/harness-design`
- the main need is product planning, architecture design, or PRD review rather than approval of the current slice
- the work has already been implemented and now needs browser-facing acceptance — use `delivery-control/frontend-evaluator`
- the work is complete and the team wants durable lessons extracted — use `delivery-control/compound`

## Core Contract

- `docs/live/contract.md` is the canonical artifact for the current implementation slice. Review that file, not a stale proposal in chat.
- Judge only the current slice. Do not widen the scope into a backlog review, code review family, or architecture board.
- Approve only when the slice states a bounded change surface, a truthful goal, observable acceptance, and enough constraints that the generator will not need to guess.
- Reject when the contract is missing, stale, too broad, contradictory, hides known uncertainty, or leaves acceptance vague enough that plausible failure could still look successful.
- A rejection must name the concrete defects that block execution and the owner who must revise the contract before review runs again.
- Do not convert rejection into vague "proceed carefully" advice. The output is a real gate: execution is either approved or rejected.
- Do not write or repair the implementation from inside this skill. Fixing the slice belongs to the planner or contract author; executing the slice belongs to the generator.

## Review Questions

Answer these in order:

1. **Canonical artifact** — Does `docs/live/contract.md` exist and clearly describe the current slice rather than a historical or hypothetical one?
2. **Goal truthfulness** — Does the slice say what will actually be changed, and only that?
3. **Boundary control** — Are the allowed files, systems, or surfaces narrow enough that the generator cannot silently sprawl?
4. **Acceptance observability** — Would a skeptical reviewer know exactly what evidence proves the slice succeeded or failed?
5. **Risk honesty** — Are open questions, dependencies, and non-goals surfaced clearly enough that execution will not invent answers mid-flight?
6. **Return path** — If this slice fails in execution, is it clear whether the defect returns to the generator or the planner?

If any answer is no, reject the slice until the defect is fixed.

## Output Shape

Return a compact verdict with these sections:
1. **Verdict** — exactly `Approved` or `Rejected`
2. **Slice summary** — one short statement of what the current slice is allowed to do
3. **Reasons** — the approval basis or the rejection defects
4. **Required revisions** — only for `Rejected`; name the exact contract defects that must change before retry
5. **Next route** — where work goes next (`harness-engineering`, `delivery-control/harness-design`, or generator execution under the approved contract)

## Failure Modes to Avoid

- Turning this into generic design review or post-implementation code review.
- Approving because the contract sounds reasonable while acceptance still depends on generator guesswork.
- Rewriting the slice instead of judging it.
- Letting article-style artifact names drift away from canonical `docs/live/contract.md`.
- Treating partial approval, soft approval, or "approved with TODOs" as acceptable. If the TODO matters, reject.
