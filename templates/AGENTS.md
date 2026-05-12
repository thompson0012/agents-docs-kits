# AGENTS.md

This repository uses the agents-stack harness — a stateful, resumable, adversarial framework that manages understanding depth as rigorously as task execution.

## Canonical Topology

```text
.
├── AGENTS.md
├── .agents/
│   └── skills/
│       └── using-agents-stack/
│           ├── SKILL.md                     # root router (orchestrator)
│           ├── thesis/                      # form falsifiable claim
│           ├── challenge/                   # adversarial test via oracle/council
│           ├── response/                    # tactical design per gap
│           ├── synthesis/                   # unify into coherent framework
│           ├── contract/                    # define buildable scope
│           ├── build/                       # implement contract
│           ├── audit/                       # independent verification
│           └── references/
│               ├── state-machine.md
│               ├── children.json
│               └── templates/.harness/
├── .harness/<WORKSTREAM-ID>/
│   ├── thesis.md
│   ├── challenge.md
│   ├── response.md
│   ├── synthesis.md
│   ├── contract.md
│   ├── handoff.md
│   ├── audit.md
│   └── status.json
└── docs/
    ├── live/
    │   ├── tracked-work.json
    │   └── plan.md
    ├── reference/
    │   ├── architecture.md
    │   └── design.md
    └── archive/<ID>_<timestamp>/
```

## Three Layers

| Layer | Question | Phases | Output |
|-------|----------|--------|--------|
| **Direction** | What are we understanding? | thesis → challenge | thesis.md, challenge.md |
| **Method** | How do we respond to gaps? | response → synthesis | response.md, synthesis.md |
| **Action** | What do we build to verify? | contract → build → audit | contract.md, handoff.md, audit.md |

Layers proceed sequentially. Action layer produces insight that may trigger a spiral turn back to Direction layer at greater depth.

## Core Invariants

1. **Files beat chat memory.** If files and conversation disagree, files win.
2. **One active workstream.** At most one workstream is non-parked at any time.
3. **Generator ≠ Auditor.** Build and audit must be independent workers.
4. **Artifact precedence.** `audit.md > handoff.md > contract.md > (thesis/challenge/response/synthesis) > status.json > tracked-work.json > plan.md`
5. **Depth and attempt are independent.** `depth` tracks understanding layers. `attempt` tracks execution retries. They never interfere.
6. **Response before Synthesis.** `response.md` must complete before `synthesis.md`. Order is enforced by the orchestrator.
7. **Spiral turn is not retry.** Spiral turn increments `depth` and returns to thesis. Retry increments `attempt` and keeps the same contract.
8. **Cold start must work.** A new agent entering cold must recover full state from files alone, without chat history.

## State

### `docs/live/plan.md`
Single resume anchor. Three sections: **Why** (source goal), **What** (current workstream/layer/phase/depth), **Next** (immediate action + blockers). Also holds cross-workstream **Lessons**.

### `docs/live/tracked-work.json`
Single registry of all workstreams. Tracks: `active_workstream_id`, `parked_workstream_ids`, and per-workstream metadata (title, depth, layer, phase, evidence_path).

### `.harness/<ID>/status.json`
Per-workstream checkpoint (7 fields):
```json
{"workstream_id":"", "depth":0, "layer":"", "phase":"", "attempt":0, "max_attempts":3, "max_depth":6, "blocked_reason":null}
```

## Orchestrator-Worker Model

- The root router (`using-agents-stack`) is the only orchestrator. It reads state, routes, dispatches workers, merges results, and is the human-facing boundary.
- Workers run one phase each in a fresh context. Workers must not spawn nested workers.
- Tool walls are hard: audit workers get read-only access except for `audit.md`. Build workers get write access limited to contract-defined files.
- Dispatch: provide worker prompt (SKILL.md path) + workstream ID + artifact paths. No elaborate formalism.

## Routing

Routes are layer-internal, layer-to-layer, or spiral-turn:

**Within a layer:** check artifact existence in order (thesis → challenge, response → synthesis, contract → build → audit).

**Between layers:** challenge complete + no translation needed → response. Synthesis complete → contract.

**Comprehension gate:** If challenge verdict is abstract and needs translation for downstream, the orchestrator routes a translation pass (appends to challenge.md) before proceeding.

**After audit:**
- PASS + no deeper insight → archive (update tracked-work.json + plan.md)
- PASS + deeper insight → spiral turn: `depth++`, reset to thesis
- FAIL → retry if `attempt < max_attempts` and `clean_restore_ref` exists
- BLOCKED → `awaiting_human`
- `attempt >= max_attempts` or `depth >= max_depth` → `escalated_to_human`

## Resume Procedure

1. Read `AGENTS.md`
2. Read `docs/live/plan.md` and `docs/live/tracked-work.json`
3. Identify active workstream, read `.harness/<ID>/status.json`
4. Read strongest artifact in precedence order
5. Verify checkpoint matches reality on disk
6. Resume from strongest valid checkpoint

## Archive Policy

Archive only after audit PASS + no deeper insight:
- Move sprint evidence to `docs/archive/<ID>_<timestamp>/`
- Update `tracked-work.json` (clear active, point evidence_path to archive)
- Update `plan.md` (clear active workstream, append lessons)

## Success Condition

The harness is healthy when a cold-start agent can read the files above and continue safely without any chat history.
