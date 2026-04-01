# Progress

Read after `current-focus.md` to recover the latest state and hand-off details. Keep each section concise.

## Current State

- Design-skill layout cutover is complete in the working tree: `generating-design-tokens` is a shipped leaf, `using-design` is optional.
- Root reference docs and live docs are aligned with the new boundary; verification passed.

## Latest Completed Work

- Updated the template skill docs so the shipped suite routes token work directly to `generating-design-tokens`, and the optional `using-design` family no longer owns that child.
- Updated `docs/reference/{architecture,codemap,memory}.md` to record the shipped/optional boundary truth.
- Refreshed `docs/live/{current-focus,progress,todo}.md` to match the cutover and handoff state.
- Verified there are no stale shipped-tier `using-design` path references left in the repo.

## Blockers

- None.

## Touched Files

- `docs/live/{current-focus,progress,todo}.md`
- `docs/reference/{architecture,codemap,memory}.md`
- `templates/base/.agents/skills/{generating-design-tokens,using-labs21-suite}/...`
- `templates/base/.agents/skills-optional/using-design/{SKILL.md,references/children.json,generative-ui/{SKILL.md,references/dependency-graph.md}}`
- `templates/base/.agents/skills-optional/using-documents/...`
- `templates/base/.agents/skills-optional/website-building/shared/...`

## Verification

- `git diff --check` passed.
- Grepped the repo for stale `.agents/skills/using-design/design-foundations/SKILL.md` and `using-design/generating-design-tokens` references; none remain.
- Any remaining `using-design` mentions in the shipped suite docs are intentional boundary text, not evidence of a shipped child.
- Confirmed the live and reference docs now describe the moved skill layout.

## Next Recommended Action

- Handoff.