# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The packaged strategic scenario-planning skill now lives at `templates/base/.agents/skills/strategic-foresight/` with clearer trigger guidance that keys on a concrete signal plus implications under uncertainty.

## Latest Completed Work

Renamed the packaged skill directory from `future-catcher` to `strategic-foresight`, changed the frontmatter name, rewrote the description for more precise activation, and added body sections for positioning, trigger rules, strong signals, and non-triggers.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

None for this objective.

## Touched Files

- `templates/base/.agents/skills/strategic-foresight/SKILL.md`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`

## Verification Status

Re-read `templates/base/.agents/skills/strategic-foresight/SKILL.md` after editing and confirmed the frontmatter name is `strategic-foresight`, the description encodes explicit positive and negative trigger conditions, and the body distinguishes it from generic advisory or summary work. Searched `templates/base/.agents/skills` for `future-catcher` / `Future Catcher` and found no remaining packaged-skill references. Confirmed the old `templates/base/.agents/skills/future-catcher/` directory was removed. `docs/live/*` intentionally retains the old name as historical context for this rename.

## Hand-off Note

If this template is consumed by any external system-level skill registry, update that registry to call the renamed skill `strategic-foresight`; within this repository, the rename is complete.