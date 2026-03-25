# Code Map

Read when you need to find where to work. Prefer only high-value paths.

## Key Paths

- Path: `templates/base/docs/live/`
- Purpose: live handoff surface for current objective, runtime control, continuity, QA evidence, and task selection.
- Update when: a live-doc path, handoff contract, or evaluation artifact changes.

- Path: `templates/base/docs/reference/`
- Purpose: stable reference docs for architecture, codemap, implementation, design, memory, and lessons.
- Update when: boundaries, high-value paths, or stable repo guidance changes.

- Path: `templates/base/.agents/skills/software-delivery/`
- Purpose: router family for feature discovery, harness control, plan reviews, and independent frontend evaluation.
- Update when: a software-delivery leaf is added, removed, renamed, or materially repurposed.

- Path: `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- Purpose: top-level discoverability for first-party skill families, including the software-delivery leaves.
- Update when: category routing or skill inventory changes.

## Entrypoints

- Entrypoint: `templates/base/AGENTS.md`
- Consumer: any agent starting or resuming work in the template
- Notes: root read order; points into the live docs and reference docs.

- Entrypoint: `templates/base/.agents/skills/software-delivery/SKILL.md`
- Consumer: agents choosing the right software-delivery lane
- Notes: routes to `feature-discovery`, `harness-design`, `plan-product-review`, `plan-engineering-review`, `plan-design-review`, or `frontend-evaluator`.

- Entrypoint: `templates/base/docs/live/runtime.md`
- Consumer: planner, generator, or evaluator working under explicit delivery control
- Notes: records the active mode and baton rules; skip for trivial work that stays in one obvious session.

- Entrypoint: `templates/base/docs/live/qa.md`
- Consumer: independent evaluator or any role auditing acceptance evidence
- Notes: canonical markdown artifact for evaluator evidence, verdict, and retry contract when independent acceptance exists.

## High-Value Files

- File: `templates/base/docs/live/current-focus.md`
- Why it matters: defines the active boundary and next-owner instruction.
- Read after: `templates/base/AGENTS.md`

- File: `templates/base/docs/live/todo.md`
- Why it matters: records the queued work so the active baton owner and next owner can see what remains and what is already done.
- Read after: `templates/base/docs/live/current-focus.md`

- File: `templates/base/docs/live/runtime.md`
- Why it matters: tells whether the work is `single-session`, `compacted-continuation`, or `planner-generator-evaluator`, and who owns the baton now.
- Read after: `templates/base/docs/live/current-focus.md`

- File: `templates/base/docs/live/progress.md`
- Why it matters: preserves continuity, touched files, blockers, and verification truth.
- Read after: `templates/base/docs/live/current-focus.md`

- File: `templates/base/docs/live/qa.md`
- Why it matters: carries audit-friendly QA evidence plus `pass`, `fail`, or `blocked` when independent evaluation exists.
- Read after: `templates/base/docs/live/runtime.md`

- File: `templates/base/.agents/skills/software-delivery/feature-discovery/SKILL.md`
- Why it matters: starts the delivery family when the feature or change request is still fuzzy.
- Read after: `templates/base/.agents/skills/software-delivery/SKILL.md`

- File: `templates/base/.agents/skills/software-delivery/harness-design/SKILL.md`
- Why it matters: defines mode selection, baton rules, and the live-doc artifact contract.
- Read after: `templates/base/.agents/skills/software-delivery/SKILL.md`

- File: `templates/base/.agents/skills/software-delivery/plan-product-review/SKILL.md`
- Why it matters: reviews value, scope, sequencing, and MVP cuts before build.
- Read after: `templates/base/.agents/skills/software-delivery/SKILL.md`

- File: `templates/base/.agents/skills/software-delivery/plan-engineering-review/SKILL.md`
- Why it matters: reviews architecture, failure modes, tests, and rollout risk before build.
- Read after: `templates/base/.agents/skills/software-delivery/SKILL.md`

- File: `templates/base/.agents/skills/software-delivery/plan-design-review/SKILL.md`
- Why it matters: reviews UX flows, states, accessibility, and interface clarity before build.
- Read after: `templates/base/.agents/skills/software-delivery/SKILL.md`

- File: `templates/base/.agents/skills/software-delivery/frontend-evaluator/SKILL.md`
- Why it matters: defines evidence, verdict, defect, and retry expectations for browser-facing signoff.
- Read after: `templates/base/.agents/skills/software-delivery/SKILL.md`
