# Runtime

Read when work uses explicit delivery control across sessions or roles. Keep this current before each baton pass.

## Current Mode

- Mode: `single-session` | `compacted-continuation` | `planner-generator-evaluator`
- Why this mode:
- Active boundary:

## Current Baton Owner

- Owner:
- Owns now:
- Must update before pass:

## Next-Role Entry Criteria

- Next role:
- Enter when:
- Required reads:
- Required truth before entry:

## Reset vs Compaction Rule

- Stay in-session when:
- Use `context-compaction` when the same role should continue after a reset or context pressure.
- Do not compact when:
- Reset result:

## Artifact Pointers

- `docs/live/current-focus.md`:
- `docs/live/runtime.md`:
- `docs/live/progress.md`:
- `docs/live/qa.md`:
- Other artifact:

## Stop / Escalation Conditions

- Stop and return `blocked` when:
- Return to planner when:
- Return to generator when:
