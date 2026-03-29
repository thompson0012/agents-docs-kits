# Architecture Reference

Read when system shape, boundaries, or invariants matter. Keep this focused on stable structure.

## System Boundaries

- Inside scope: portable skill routing, including the `project-founding` and `software-delivery` families, shared web QA guidance, and template live/reference docs that carry delivery state across sessions.
- Outside scope: product-specific implementations, runtime-specific harness code, and mandatory evaluator overhead for trivial one-shot tasks.
- Boundary note: `project-founding` owns staged blueprinting before a PRD exists, `feature-spec` owns scoped requirements artifacts after the blueprint is stable, and `startup-pressure-test` owns harsh commercial teardown once the blueprint can be challenged honestly.
- Boundary note: `software-delivery` owns delivery-control routing and independent frontend acceptance selection; `website-building` owns web implementation and builder-side browser QA, then may recommend evaluator follow-on.

## Invariants

- Invariant: `software-delivery/harness-design` is only for cross-session control, compaction rules, baton passing, and planner/generator/evaluator structure.
- Why it must hold: routing ordinary single-session execution into harness design would duplicate the base router and blur ownership.
- Failure signal: routine build or plan-review work is described as harness design without any explicit session-control problem.

- Invariant: independent browser signoff belongs to `software-delivery/frontend-evaluator`, while `website-building` remains the builder-facing implementation and QA family.
- Why it must hold: the repo now distinguishes builder verification from a fresh evaluator's pass/fail gate.
- Failure signal: `website-building` is treated as the final independent acceptance gate, or evaluator work starts fixing implementation.

- Invariant: `templates/base/docs/live/runtime.md` and `templates/base/docs/live/qa.md` are the canonical live docs when explicit delivery control or evaluator evidence exists.
- Why it must hold: baton state and acceptance evidence must survive session resets and role changes in one predictable place.
- Failure signal: runtime mode, baton owner, evidence, or verdict only live in chat transcripts or ad hoc files.

- Invariant: `project-founding` owns founding blueprints, while `feature-spec` and `startup-pressure-test` remain distinct follow-on surfaces instead of partial substitutes.
- Why it must hold: collapsing blueprinting, PRD writing, and viability teardown into one family would hide whether the user needs product definition, a detailed spec, or commercial skepticism.
- Failure signal: staged project-definition requests route straight to `feature-spec`, or harsh viability teardowns route into `project-founding` as if they were the same job.

## Major Components

- Component: `templates/base/.agents/skills/software-delivery/`
- Responsibility: routes non-trivial software work across discovery, harness control, plan review, implementation handoff, independent frontend evaluation, and readiness reflection.
- Key dependency: `references/children.json` plus the nested `harness-design/` and `frontend-evaluator/` leaves.

- Component: `templates/base/.agents/skills/using-labs21-suite/`
- Responsibility: top-level discoverability router for the shipped Labs21 template suite; it routes only across the owned top-level skills and refuses to claim moved external families as part of the suite.
- Key dependency: `references/children.json` plus `references/category-map.md` for the current top-level suite inventory.

- Component: `templates/base/.agents/skills/project-founding/`
- Responsibility: routes new project and product ideas into either general staged blueprinting or AI/agentic founding with explicit governance, cost, and control design.
- Key dependency: `references/children.json` plus the nested `project-foundation/` and `ai-agent-foundation/` leaves.

- Component: `templates/base/docs/live/{current-focus.md,progress.md,todo.md,runtime.md,qa.md}`
- Responsibility: carries recovery state across normal continuation, explicit baton passes, and evaluator evidence collection.
- Key dependency: truthful updates from the active role before handoff.