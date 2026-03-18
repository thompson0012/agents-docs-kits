# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The legacy `create-skill` guidance has been replaced by a universal `skills-creator` package with SKILL.md, scripts, references, and templates for scaffolding, validating, and evaluating new skills.

## Latest Completed Work

- Added `templates/base/.agents/skills/skills-creator/SKILL.md` with the seven-phase lifecycle, progressive disclosure rules, and links to supporting resources.
- Added assets (`skill_template.md`, `eval_template.md`) and references (`PATTERNS.md`, `PLATFORMS.md`, `SECURITY.md`, `ANTIPATTERNS.md`).
- Implemented `scripts/scaffold.py` (name checks + scaffold + eval template copy) and `scripts/validate.py` (frontmatter/name/description/line-count/reference-depth checks, optional eval count gate).
- Retired the old `create-skill` folder and refreshed live docs (current-focus, todo, progress).

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Author real evaluation scenarios for `skills-creator` (or downstream skills) and run the validator with `--full` once scenarios exist; optionally tune the gerund warning if keeping the `skills-creator` name as-is.

## Touched Files

- `templates/base/.agents/skills/skills-creator/SKILL.md`
- `templates/base/.agents/skills/skills-creator/assets/skill_template.md`
- `templates/base/.agents/skills/skills-creator/assets/eval_template.md`
- `templates/base/.agents/skills/skills-creator/references/PATTERNS.md`
- `templates/base/.agents/skills/skills-creator/references/PLATFORMS.md`
- `templates/base/.agents/skills/skills-creator/references/SECURITY.md`
- `templates/base/.agents/skills/skills-creator/references/ANTIPATTERNS.md`
- `templates/base/.agents/skills/skills-creator/scripts/scaffold.py`
- `templates/base/.agents/skills/skills-creator/scripts/validate.py`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`

## Verification Status

- `python3 -m compileall templates/base/.agents/skills/skills-creator/scripts`
- `python3 templates/base/.agents/skills/skills-creator/scripts/validate.py templates/base/.agents/skills/skills-creator` (passes with a gerund-name warning because the spec keeps `skills-creator`)

## Hand-off Note

`skills-creator` now packages the full lifecycle guidance plus scaffold/validate helpers and supporting references/templates. Add evaluation scenarios and re-run validation with `--full` when ready; adjust or silence the gerund warning if you prefer to keep the non-gerund name.
