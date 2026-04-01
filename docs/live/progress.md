# Progress

Read after `current-focus.md` to recover the latest state and hand-off details. Keep each section concise.

## Current State

- Delivery-control upgrade is complete in the working tree; verification passed.
- See `roadmap.md` for the phase lineage and goal history.

## Latest Completed Work

- Upgraded `templates/base/.agents/skills/delivery-control/` with a compound leaf and clarified orchestration, QA, and postflight extraction responsibilities.
- Updated the root and template reference archives/scaffolds to separate durable truths from reusable lessons and to reflect the compound lane.
- Retargeted the root live docs from the earlier template-cutover batch to the delivery-control upgrade objective.
- Fixed the suite router index/category map and website-building follow-on guidance so delivery lifecycle work and browser QA both route through the new delivery-control lanes.

## Blockers

- None.

## Touched Files

- `docs/live/{current-focus,progress,todo,roadmap}.md`
- `docs/reference/{architecture,codemap,memory,lessons}.md`
- `templates/base/.agents/skills/delivery-control/{SKILL.md,references/children.json,harness-design/SKILL.md,compound/SKILL.md}`
- `templates/base/.agents/skills/using-labs21-suite/{SKILL.md,references/category-map.md}`
- `templates/base/.agents/skills-optional/website-building/{SKILL.md,references/children.json,shared/12-playwright-interactive.md}`
- `templates/base/docs/live/{runtime,qa}.md`
- `templates/base/docs/reference/{architecture,codemap,memory,lessons}.md`

## Verification

- `git diff --check` passed.
- Focused stale-reference scans on active delivery-control and website-building surfaces found no `software-delivery` matches.
- Structural read-back confirmed the compound lane and archive split are present.
- Remaining `software-delivery` references are confined to historical/archive context, not active surfaces.

## Next Recommended Action

- Ready for handoff.
