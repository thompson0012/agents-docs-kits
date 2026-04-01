# Runtime

Control-plane state for the current delivery cycle. Update before every baton pass so the receiving role reads current truth, not stale intent.

## Current Mode

<!-- Exactly one of: single-session | compacted-continuation | planner-generator-evaluator -->

- Mode:
- Why this mode:
- Active boundary:
- Goal lineage: <!-- source goal → plan goal → current phase goal -->

## Current Baton Owner

- Owner: <!-- planner | generator | evaluator | blocked -->
- Owns now:
- Must update before pass:
- Last pass reason:

## Next-Role Entry Criteria

- Next role:
- Enter when:
- Required reads before entry:
- Required truth before entry: <!-- what must be current in live docs -->
- Must not enter while: <!-- guardrail conditions -->

## Reset vs Compaction Rule

- Stay in-session when:
- Use `context-compaction` when:
- Do not compact when:
- Rehydration sources after reset: <!-- ordered list of docs to read back -->
- Reset result: <!-- what the compacted snapshot must contain -->

## Artifact Pointers

### Live surfaces

- `docs/live/current-focus.md`:
- `docs/live/runtime.md`:
- `docs/live/progress.md`:
- `docs/live/qa.md`:
- `docs/live/roadmap.md`:

### Durable archives (postflight)

<!-- Updated by compound extraction after a delivery cycle completes. -->

- `docs/reference/lessons.md`:
- `docs/reference/memory.md`:

## Return Paths

<!-- Every failure routes to exactly one owner. -->

- Implementation defect → return to:
- Scope / contract / orchestration defect → return to:
- Environment or setup blocker → mark as:
- Goal-lineage drift → return to:

## Stop / Escalation Conditions

- Stop and return `blocked` when:
- Return to planner when:
- Return to generator when:
- Escalate to user when:

## Postflight Handoff

<!-- After the delivery cycle closes (pass or retire), before the control plane resets. -->

- Compound extraction needed: <!-- yes | no | deferred -->
- Extraction scope: <!-- what the compound skill should read -->
- Lessons candidates:
- Memory candidates:
