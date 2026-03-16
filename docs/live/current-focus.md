# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

The packaging repair is complete for `strategic-foresight`, `startup-pressure-test`, and `liquid-glass-design`; preserve the repaired workflow, packaged artifacts, and evaluation records until a new task supersedes them.

## Scope

- Keep the repaired packaging helper under `templates/base/.agents/skills/skill-creator/scripts/package_skill.py`.
- Keep the repaired skill sources under `templates/base/.agents/skills/`, including the frontmatter now present in `liquid-glass-design/SKILL.md`.
- Keep the updated evaluation artifacts under `templates/base/.agents/skills/evaluation-2026-03-16/`.
- Keep the packaged `.skill` artifacts present in `dist/`.

## Constraints

- Use the repository `skill-creator` workflow for future re-evaluation, not ad hoc checks.
- Continue using `PYTHONPATH=.tmp-pyyaml-real` for local packaging; `PyYAML==6.0.3` is now installed there and required by `quick_validate.py`.
- The packager now intentionally skips `.DS_Store` and `__pycache__` so packaged skills contain only real resources.
- Do not commit from this task.

## Success Criteria

- `dist/` contains `strategic-foresight.skill`, `startup-pressure-test.skill`, and `liquid-glass-design.skill`.
- Zip inspection confirms each packaged skill contains only `SKILL.md` under its skill directory.
- The evaluation records in `templates/base/.agents/skills/evaluation-2026-03-16/` reflect the successful rerun and the applied repairs.