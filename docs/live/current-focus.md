# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

The design-skill layout cutover is complete in the working tree. `generating-design-tokens` is a top-level shipped leaf, `using-design` lives under `templates/base/.agents/skills-optional/`, and the repo docs now reflect that boundary.

## Scope

In scope:
- Keep `docs/reference/{architecture,codemap,memory}.md` and `docs/live/{current-focus,progress,todo}.md` aligned with the cutover truth.
- Preserve the distinction between the shipped suite and the optional broader design router.

Out of scope:
- Modifying product code, template generation logic, or validator scripts.
- Editing template skill files or `docs/reference/lessons.md`.
- Editing `docs/live/roadmap.md` unless absolutely necessary.

## Constraints

- One concept, one representation — docs must not describe two conflicting layouts.
- Live docs must be self-contained: an agent resumes from these files, not chat memory.

## Success Criteria

- Root reference docs and live docs describe the cutover truthfully.
- No stale shipped `using-design` references remain in the active surfaces.
