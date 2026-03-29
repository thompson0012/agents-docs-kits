# Code Map

Read when you need to find where to work. Prefer only high-value paths.

## Key Paths

- Path: `templates/base/.agents/skills/software-delivery/`
- Purpose: router family for non-trivial software delivery, including `harness-design` and `frontend-evaluator`.
- Update when: the family boundary, child list, or eval coverage changes.

- Path: `templates/base/.agents/skills/website-building/`
- Purpose: builder-side web implementation and QA family that now points signoff-sensitive work to `software-delivery/frontend-evaluator`.
- Update when: builder QA guidance or evaluator follow-on rules change.

- Path: `templates/base/docs/live/`
- Purpose: continuity surface for repo work; `runtime.md` tracks baton state and `qa.md` stores evaluator evidence and verdicts.
- Update when: the live-doc contract or required handoff artifacts change.

- Path: `templates/base/.agents/skills/using-agent-practices/`
- Purpose: top-level router and category-map surface that makes first-hop family routing discoverable, including `project-founding` and `software-delivery`.
- Update when: first-hop routing or category descriptions change.

- Path: `templates/base/.agents/skills/project-founding/`
- Purpose: router family for staged project and product blueprinting, with separate general and AI/agentic founding leaves.
- Update when: the family boundary, child list, or founding-vs-spec/teardown routing rules change.

## Entrypoints

- Entrypoint: `templates/base/.agents/skills/software-delivery/SKILL.md`
- Consumer: agents deciding whether work needs discovery, harness control, review, evaluator signoff, implementation, or readiness reflection.
- Notes: enter here before direct leaf selection when non-trivial software delivery is ambiguous.

- Entrypoint: `templates/base/.agents/skills/software-delivery/references/children.json`
- Consumer: router authors and reviewers checking durable family boundaries.
- Notes: source of truth for `harness-design`, `frontend-evaluator`, external targets, and the `website-building` follow-on relationship.

- Entrypoint: `templates/base/.agents/skills/website-building/references/children.json`
- Consumer: web-routing maintainers confirming which child paths recommend independent evaluator follow-on.
- Notes: `webapp` and `game` currently recommend `software-delivery/frontend-evaluator`; informational work stays lighter-weight unless that changes.

- Entrypoint: `templates/base/.agents/skills/project-founding/SKILL.md`
- Consumer: agents deciding whether a new idea needs general founding or AI/agentic founding before a PRD or teardown exists.
- Notes: enter here when the job is staged blueprinting rather than feature-spec writing or startup pressure testing.

- Entrypoint: `templates/base/.agents/skills/project-founding/references/children.json`
- Consumer: router authors and reviewers checking durable founding-family boundaries.
- Notes: source of truth for the split between `project-foundation` and `ai-agent-foundation`.

- Entrypoint: `templates/base/docs/live/runtime.md`
- Consumer: planner, generator, evaluator, or same-role continuation across resets.
- Notes: only required when explicit delivery control is in play.

- Entrypoint: `templates/base/docs/live/qa.md`
- Consumer: independent evaluator or anyone auditing acceptance evidence.
- Notes: records the evidence matrix, defect list, verdict, and retry contract.

## High-Value Files

- File: `templates/base/.agents/skills/software-delivery/harness-design/SKILL.md`
- Why it matters: defines when to stay single-session, compact, or use planner/generator/evaluator control.
- Read after: `templates/base/.agents/skills/software-delivery/SKILL.md`

- File: `templates/base/.agents/skills/software-delivery/frontend-evaluator/SKILL.md`
- Why it matters: defines independent browser QA output, evidence standards, and pass/fail/blocked semantics.
- Read after: `templates/base/.agents/skills/software-delivery/SKILL.md`

- File: `templates/base/.agents/skills/website-building/shared/12-playwright-interactive.md`
- Why it matters: shared builder QA workflow and evaluator dependency reference for browser-facing work.
- Read after: `templates/base/.agents/skills/website-building/SKILL.md`

- File: `templates/base/docs/live/runtime.md`
- Why it matters: quickest place to recover baton ownership and execution mode during multi-session work.
- Read after: `docs/live/current-focus.md`

- File: `templates/base/docs/live/qa.md`
- Why it matters: quickest place to audit evaluator evidence and the final verdict when independent signoff exists.
- Read after: `templates/base/docs/live/runtime.md`