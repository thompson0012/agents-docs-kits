# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

Task 38 is now complete. The prompt-skill surface now cleanly splits prompt architecture from prompt enrichment: `meta-prompting` focuses on designing and stress-testing prompt artifacts, while the new `prompt-augmentation` leaf handles sparse text, image, and video prompt expansion plus useful variants. The next likely step is to resume Task 35's methodology-overlay refinements unless prompt-skill eval coverage becomes the higher priority.

## Latest Completed Work

Rewrote `templates/base/.agents/skills/meta-prompting/SKILL.md` to keep it portable and architecture-focused, added `templates/base/.agents/skills/prompt-augmentation/SKILL.md` as a new leaf skill, and updated `templates/base/.agents/skills/using-agent-practices/{SKILL.md,references/category-map.md}` so prompt artifact routing distinguishes system-prompt architecture work from sparse prompt enrichment.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Resume Task 35: refine the capability-based methodology overlays in the finance, research, and webapp docs. The prompt-skill split is in place; add dedicated prompt-skill eval coverage later only if discovery quality starts drifting.

## Touched Files

- `templates/base/.agents/skills/meta-prompting/SKILL.md`
- `templates/base/.agents/skills/prompt-augmentation/SKILL.md`
- `templates/base/.agents/skills/using-agent-practices/{SKILL.md,references/category-map.md}`
- `docs/live/progress.md`
- `docs/live/todo.md`
- deleted stray `.DS_Store` artifacts at the repo root and under `templates/` / `templates/base/.agents/skills/`

## Verification Status

Observed success for:

- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/meta-prompting --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/prompt-augmentation --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
- `python3 scripts/audit_base_template_skills.py`
- `git diff --check` returned no output
- readback review confirmed that `meta-prompting` now owns prompt architecture, `prompt-augmentation` owns sparse generation-prompt enrichment, and the `using-agent-practices` router surfaces distinguish the two without overlapping triggers

## Hand-off Note

Prompt-related work now has two honest leaf skills with non-overlapping boundaries. Use `meta-prompting` for prompt/system-prompt design and evaluation; use `prompt-augmentation` when the job is enriching or varying a sparse generation prompt. Unless more prompt-suite evaluation is requested, the repo's default next move is still Task 35.