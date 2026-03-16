# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The first-party skill suite now has an owned routing layer. `using-agent-practices` routes across the whole suite, `using-reasoning` routes the overlapping reasoning skills, and `using-agent-practices/references/category-map.md` records the current category abstraction for the 11 live leaf skills.

## Latest Completed Work

Created `templates/base/.agents/skills/using-agent-practices/SKILL.md`, `templates/base/.agents/skills/using-reasoning/SKILL.md`, a shared category map reference under `using-agent-practices/references/`, and starter `evals/evals.json` fixtures for both routers. The suite is now abstracted into Orchestration and Continuity, Reasoning and Strategy, Prompt Artifact Creation, Commercial Reality Testing, and Design Systems and Visual Prototyping, with only the reasoning cluster routed through a family router.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

If these routers will become stable entry points, run a true `skill-creator` eval loop against the new router skills next so the category ordering and descriptions can be pressure-tested on ambiguous prompts instead of only structurally validated.

## Touched Files

- `templates/base/.agents/skills/using-agent-practices/SKILL.md`
- `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- `templates/base/.agents/skills/using-agent-practices/evals/evals.json`
- `templates/base/.agents/skills/using-reasoning/SKILL.md`
- `templates/base/.agents/skills/using-reasoning/evals/evals.json`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`

## Verification Status

Read back both new SKILL files plus the new category map and eval fixtures. Ran and observed success for:
- `python3` frontmatter/JSON validation covering `templates/base/.agents/skills/using-agent-practices/SKILL.md`, `templates/base/.agents/skills/using-reasoning/SKILL.md`, both router `evals/evals.json` files, and the required sections in `using-agent-practices/references/category-map.md`.

## Hand-off Note

The suite abstraction is now documented without renaming the existing leaf skills. The next leverage point is evaluation quality, not more taxonomy: the owned routers exist, but their category order and trigger wording still need real ambiguous-prompt testing if you want them to become default entry points.