# AGENTS.md

This repository uses the agents-stack harness. The harness is stateful, resumable, and adversarial by design: files are the source of truth, one runnable sprint is active at a time, and the top-level router acts as an orchestrator that dispatches fresh worker agents for each phase instead of swapping personas inline.

## Canonical Topology

```text
.
├── AGENTS.md
├── .agents/
│   └── skills/
│       └── using-agents-stack/
│           ├── SKILL.md                     # root router
│           ├── project-initializer/
│           ├── generator-proposal/
│           ├── evaluator-contract-review/
│           ├── generator-execution/
│           ├── adversarial-live-review/
│           └── state-update/
├── .harness/
│   ├── <FEAT-ID>/                           # the one runnable sprint workspace, or a parked human-gated sprint
│   │   ├── sprint_proposal.md
│   │   ├── contract.md
│   │   ├── runtime.md                       # optional but expected once execution starts
│   │   ├── handoff.md
│   │   ├── qa.md                            # optional until review writes it
│   │   ├── review.md
│   │   └── status.json
│   └── ... parked awaiting_human / escalated_to_human sprint folders when needed
└── docs/
    ├── live/
    │   ├── features.json
    │   ├── progress.md
    │   └── memory.md
    ├── archive/
    │   └── FEAT-000_timestamp/
    │       ├── sprint_proposal.md
    │       ├── contract.md
    │       ├── handoff.md
    │       ├── review.md
    │       └── status.json
    ├── reference/
    │   ├── architecture.md
    │   └── design.md
    └── scripts/
        ├── init.sh
        └── orchestrator.py
```

## What Each Area Means

### `AGENTS.md`
The repository constitution. Read this first. It defines topology, lifecycle, state precedence, role ownership, and recovery rules.

### `docs/live/*`
Global durable state for the whole repo.

- `features.json`: the backlog, dependency graph, runnable active sprint pointer, and any parked sprint metadata the project needs to understand what can run next.
- `progress.md`: append-only ledger of reviewed outcomes, failures, pauses, escalations, and next actions.
- `memory.md`: durable lessons, operational caveats, and facts future agents should not rediscover every session.

### `docs/reference/*`
Stable reference context.

- `architecture.md`: current runtime, entrypoints, major subsystems, integration boundaries, and orchestration rules.
- `design.md`: current UI/product intent, interaction model, and notable UX constraints.

Reference docs guide decisions, but they do not override an approved sprint contract.

### Canonical active contract
For an active sprint, the only canonical execution contract is `.harness/<FEAT-ID>/contract.md`. `docs/live/features.json` may point to the active feature, local sprint folder, phase, and resume checkpoint, but it must not become a second contract.

Generators and reviewers build from the approved local contract on disk, not from remembered proposal text or paraphrased scope in chat. If the live state points at a sprint whose local contract is missing, execution must stop until the checkpoint is re-established.

### `docs/archive/*`
Historical evidence for completed sprints.

Each archived folder is read-only history for one sprint after state-update processes a PASS result. Archive artifacts exist for audit and learning; they are never the active source of truth for an in-flight sprint.

### `.harness/<FEAT-ID>/*`
Local workspace for one runnable sprint at a time plus any explicitly parked human-gated sprints.

This folder is where proposal, contract, execution evidence, review evidence, and resume state live while the sprint is active or parked. It survives interruption and failure. On PASS it is archived; on FAIL, `build_failed`, `awaiting_human`, or `escalated_to_human` it stays in `.harness/` until corrected, resumed, canceled, or explicitly closed.

### `docs/scripts/*`
Repository-local harness utilities.

- `init.sh`: safe bootstrap that creates missing baseline directories and files without overwriting user work.
- `orchestrator.py`: optional helper that inspects durable state and prepares or records worker dispatch and resume decisions. It is not the source of truth and it must not turn the orchestrator into an inline executor.

### `.agents/skills/using-agents-stack/*`
Router-style skill package for the harness.

The root skill is the orchestrator. It dispatches exactly one fresh child worker/sub-agent/Task agent based on durable state and the host runtime's delegation primitive. The canonical children are worker prompts with phase-scoped tool access:
- `project-initializer`
- `generator-proposal`
- `evaluator-contract-review`
- `generator-execution`
- `adversarial-live-review`
- `state-update`

## Core Invariants

1. **Files beat chat memory.** If the repo and the conversation disagree, the repo wins.
2. **One runnable active sprint only.** At most one feature may be runnable in `docs/live/features.json`, and at most one `.harness/<FEAT-ID>/` folder may represent runnable non-terminal work.
3. **Parked sprints must say so explicitly.** Additional non-terminal `.harness/<FEAT-ID>/` folders are allowed only when their durable phase is `awaiting_human` or `escalated_to_human`. Parked sprints never count as the runnable active sprint.
4. **Execution does not self-approve.** Code or artifact generation cannot mark itself complete.
5. **Build/startup triage happens before live review.** If the implementation cannot build, boot, or reach its declared runtime checkpoint, record `build_failed` and return to execution. Do not spend an adversarial review worker on a sprint that never became reviewable.
6. **Retry requires a clean restore boundary.** Any retry after `review_failed` or `build_failed` must name a durable `clean_restore_ref` first. That reference may be a disposable worktree, VCS snapshot, or equivalent restore boundary. Unsafe unconditional destructive reset is not the default harness behavior.
7. **Attempt budgets are finite.** Automatic retries require durable `attempt_count` and `max_attempts`. Once the budget is exhausted or recovery is unsafe, the sprint must move to `escalated_to_human` instead of looping.
8. **Archive only after PASS.** Failed, parked, escalated, or interrupted work stays in `.harness/` with its evidence intact.
9. **State must stay resumable.** A cold-start agent must be able to continue from files alone.
10. **The orchestrator dispatches fresh workers.** Child phase work runs in a fresh worker/sub-agent/Task agent with a clean context window, not as an inline persona swap inside the orchestrator.
11. **Only the orchestrator may delegate.** Workers must not spawn nested workers.
12. **Tool walls are hard boundaries.** Evaluators and reviewers must not get broad repo write tools; if the runtime exposes a narrow artifact-return primitive, scope it only to the evaluator-owned artifact. Every other worker gets only the minimum tool scope for its phase.

## State Roles and Precedence

Use this precedence when files disagree:

1. explicit human edits or instructions
2. active sprint artifact with the strongest phase evidence:
   - `review.md`
   - `handoff.md`
   - `runtime.md`
   - `contract.md`
   - `sprint_proposal.md`
3. `.harness/<FEAT-ID>/status.json`
4. `docs/live/features.json`
5. `docs/live/progress.md` and `docs/live/memory.md`
6. `docs/reference/*`
7. `docs/archive/*` as historical evidence only

Interpretation rules:
- For an active or parked sprint, the strongest local artifact defines the real phase even if `status.json` is stale.
- `docs/live/features.json` is the project-wide selector for whether any sprint should be runnable and for which pending work is dependency-ready next.
- Archive files never override active live or local state.

## What To Do When State Disagrees

### Local sprint is ahead of global state
Example: `handoff.md` exists but `features.json` still says `pending`.

Treat the sprint as interrupted, not complete. Resume from the strongest local artifact, then use `state-update` to reconcile global state. Do not start a new runnable sprint.

### Global state says active, but local sprint state is missing or incomplete
Example: `features.json` marks `FEAT-001` active but `.harness/FEAT-001/` is missing `contract.md`.

Stop and re-establish the missing local checkpoint before doing code work. Usually that means routing back to proposal or contract review rather than guessing what the contract should have said.

### Local and global state name different runnable features
This is illegal. Do not pick one casually. Preserve both evidence trails, then reconcile before any implementation continues.

### Parked sprint is missing its human gate metadata
Example: local phase is `awaiting_human` but `status.json` does not say what the human must do or how to resume.

Stop and repair the parked checkpoint. A parked sprint without a durable gate is not safely resumable and must not be treated as a silent blocker.

### Review exists but status is stale
Trust `review.md` over `status.json`. The next owner is `state-update`.

## Deterministic startup routing rules
At session start, route using these rules in order:
- live state missing or untrustworthy -> run `project-initializer`
- multiple runnable backlog items or multiple runnable `.harness/<FEAT-ID>/` folders -> stop and escalate instead of inventing a winner
- exactly one runnable active feature and a matching `.harness/<FEAT-ID>/` folder -> route from the strongest local artifact
- `review.md` exists and the failure has already been reconciled into `review_failed` in local and live state -> resume `generator-execution` on that same sprint only after confirming the named `clean_restore_ref` and remaining attempt budget
- `runtime.md` or `status.json` records `build_failed` -> resume `generator-execution` on that same sprint only after confirming the named `clean_restore_ref` and remaining attempt budget
- retryable failure exists but `clean_restore_ref` is missing, recovery is unsafe, or `attempt_count >= max_attempts` -> route to `state-update` so the sprint becomes `awaiting_human` or `escalated_to_human`
- `review.md` exists but local and live state do not yet agree on the outcome -> route to `state-update`
- no runnable active sprint and no parked sprint folders -> select the highest-priority pending backlog item whose dependencies are satisfied and enter proposal work
- no runnable active sprint and parked `awaiting_human` / `escalated_to_human` sprint folders exist -> dependency-walk `docs/live/features.json`; if a pending feature is ready, open proposal work for that feature, otherwise surface the parked blockers clearly and wait
- local non-terminal sprint exists but live state does not name it correctly -> treat the sprint as interrupted and reconcile it before opening new runnable work

## Single-Active-Sprint Rule

The harness executes one runnable sprint at a time.

A valid live state looks like this:
- exactly one backlog item is marked runnable (`in_progress`, `contracted`, `in_review`, `review_failed`, `build_failed`, or equivalent active retry state), or none when the system is between sprints
- exactly one `.harness/<FEAT-ID>/` folder contains runnable local artifacts
- any additional `.harness/<FEAT-ID>/` folders are explicitly parked in `awaiting_human` or `escalated_to_human`
- every other feature is pending, blocked by dependency, parked for human input, archived, cancelled, or completed, but not simultaneously runnable

Do not open a second runnable sprint while another runnable sprint is still live. Finish, fail, pause, escalate, cancel, or archive the current runnable sprint first.

## Orchestrator-worker execution model

The `using-agents-stack` root skill is the only orchestrator in this starter. It reads durable state, decides the next phase, and dispatches a fresh worker for that phase.

Execution rules:
- Use the host runtime's delegation primitive when available (`sub-agent`, `Task agent`, parallel worker, or equivalent). Do not require a literal `spawn_subagent` API.
- The orchestrator never performs child phase work inline. It hands a fresh worker the feature id, subject, allowed files, tool-scope profile, and required artifact outputs, then waits for durable artifacts.
- Workers return through files first: `contract.md`, `runtime.md`, `handoff.md`, `review.md`, `status.json`, and other sprint artifacts remain the canonical trace.
- Workers do not reinterpret their tool wall. Evaluation and review workers stay read-only except for any narrowly scoped artifact-return path; execution and state-update workers get only the write access their phase requires.
- Workers must not spawn nested workers. Delegation depth stops at the orchestrator.
- Parallel workers are allowed only for independent, non-overlapping work that the orchestrator can reconcile without hidden chat state or conflicting writes.

## Phase Model

The lifecycle is explicit. Typical state flow:

1. **Uninitialized**  
   Missing or untrustworthy `docs/live/*`. Owner: `project-initializer`.
2. **Pending backlog item**  
   Feature exists in `features.json` but no runnable sprint workspace exists yet. Owner: `generator-proposal`.
3. **Proposed**  
   `.harness/<FEAT-ID>/sprint_proposal.md` exists. Owner: `evaluator-contract-review`.
4. **Contracted**  
   `.harness/<FEAT-ID>/contract.md` exists and defines the only approved execution scope. Owner: `generator-execution`.
5. **In execution / build triage**  
   `runtime.md` records what was attempted, plus any build/startup checkpoint needed before review. Owner: `generator-execution`.
6. **Build failed**  
   The sprint did not pass build/startup triage and must return directly to execution with a clean restore boundary and remaining attempt budget. Owner: `generator-execution` then orchestrator.
7. **In review**  
   `handoff.md` is ready and a reviewer can reproduce the result from sprint-local evidence. Owner: `adversarial-live-review`.
8. **Review failed**  
   `review.md` records a FAIL. State-update preserves the sprint and routes a clean retry or escalation. Owner: `state-update` then orchestrator.
9. **Awaiting human**  
   Automation is intentionally paused at a durable artifact boundary so a human can inspect, edit, approve, or supply missing information. Owner: human, then orchestrator.
10. **Escalated to human**  
   Automatic retry must stop because the attempt budget is exhausted or safe recovery cannot be established. Owner: human.
11. **Archived PASS**  
   State-update updates `docs/live/*`, moves the sprint record to `docs/archive/<FEAT-ID>_<timestamp>/`, and clears the runnable active sprint.

### Phase transition table
| Phase | Responsible role | Required artifact(s) | Exact condition to advance | Next phase |
| --- | --- | --- | --- | --- |
| `pending` | `generator-proposal` | backlog entry in `docs/live/features.json` | one dependency-ready feature is selected as the only runnable sprint candidate | `proposed` |
| `proposed` | `evaluator-contract-review` | `.harness/<FEAT-ID>/sprint_proposal.md`, `status.json` | proposal scope, file bounds, observable checks, and recovery assumptions survive adversarial review | `contracted` |
| `contracted` | `generator-execution` | `.harness/<FEAT-ID>/contract.md` | execution starts inside the approved contract and `status.json` reflects active work with attempt budgeting | `in_progress` |
| `in_progress` | `generator-execution` | code changes, `runtime.md`, `status.json` | the contracted work builds or starts at the declared checkpoint; if it does not, record `build_failed` instead of paying for live review | `in_review` or `build_failed` |
| `build_failed` | `generator-execution` then orchestrator | `runtime.md`, `status.json` with `attempt_count`, `max_attempts`, and `clean_restore_ref` | a clean restore boundary is named, attempts remain, and the next execution worker can restart from a truthful checkpoint | `in_progress` or `escalated_to_human` |
| `in_review` | `adversarial-live-review` | `contract.md`, `runtime.md`, `handoff.md`, `review.md` | the reviewer records exactly one verdict with evidence: PASS, FAIL, or BLOCKED, and the evidence checks before/action/after state transitions rather than only a final static state | `passed`, `review_failed`, or `awaiting_human` |
| `review_failed` | `state-update` then orchestrator | `review.md`, preserved `.harness/<FEAT-ID>/`, updated live state, retry metadata | FAIL is reconciled into durable state without deleting evidence, a clean restore boundary is named, and attempts remain for another execution pass | `in_progress` or `escalated_to_human` |
| `awaiting_human` | human then orchestrator | `status.json`, relevant local artifact, and explicit human instructions or edits | the human action is durably recorded, the resume checkpoint is updated, and the next owner can continue without hidden chat state | `proposed`, `contracted`, `in_progress`, or `in_review` |
| `escalated_to_human` | human | `status.json`, `progress.md`, and preserved local evidence | a human explicitly changes the plan, resets the budget, replaces the restore boundary, or closes the sprint | `pending`, `contracted`, `in_progress`, or `cancelled` |
| `passed` | `state-update` | `review.md`, updated `docs/live/*`, archive copy | PASS is synchronized into live state and the sprint artifact set is preserved under `docs/archive/<FEAT-ID>_<timestamp>/` | `archived` |

`BLOCKED` is a review verdict, not a license to keep looping. State-update must translate a blocked review into either `awaiting_human` when a human can unblock and resume from files, or `escalated_to_human` when automation must stop.

## Resume Procedure

When a sprint is interrupted by timeout, crash, human pause, failed build triage, or failed review retry:

1. Read `AGENTS.md`.
2. Read `docs/live/features.json`, `docs/live/progress.md`, and `docs/live/memory.md`.
3. Identify the one runnable active feature, if any, and list any parked `awaiting_human` or `escalated_to_human` sprint folders separately.
4. Read `.harness/<FEAT-ID>/status.json` and capture the claimed `phase`, `owner_role`, `resume_from`, `last_verified_step`, `local_url`, `active_pids`, `blocked_on`, `worker_id`, `worker_subject`, `tool_scope_profile`, `spawn_depth`, `parent_worker_id`, `attempt_count`, `max_attempts`, and `clean_restore_ref` fields.
5. When the phase is `awaiting_human` or `escalated_to_human`, also capture the pause or escalation metadata that explains what changed, what the human must do, and which phase resumes next.
6. Read local artifacts in evidence order: `review.md`, `handoff.md`, `runtime.md`, `contract.md`, `sprint_proposal.md`.
7. Verify that the claimed checkpoint matches reality on disk and in any running process before trusting it.
8. If processes were recorded in `status.json` or `runtime.md`, verify whether they still exist before reusing them.
9. Before retrying from `review_failed` or `build_failed`, verify the clean restore boundary named by `clean_restore_ref`. Use a disposable worktree, VCS snapshot, or equivalent restore reference that tells the truth about what will be retried. Do not assume an unconditional destructive reset.
10. Resume from the strongest valid checkpoint, not from guesswork or a stale phase field.
11. If the state is contradictory, reconcile it before starting new implementation.

Every active sprint `status.json` must include at minimum:
- `sprint_id`
- `phase`
- `owner_role`
- `resume_from`
- `last_verified_step`
- `last_updated_at`

Every sprint that can re-enter execution must also include:
- `attempt_count`
- `max_attempts`

Add these fields when they apply:
- `clean_restore_ref` when a retry requires returning to a known-good workspace boundary
- `local_url` when a running artifact exists
- `active_pids` when processes are live
- `blocked_on` when a sprint cannot safely continue
- `worker_id` when the next worker has an explicit dispatch identity
- `worker_subject` when the next worker needs a terse, durable task label
- `tool_scope_profile` when the orchestrator intentionally narrows tool access for that worker
- `spawn_depth` for dispatch traceability; the orchestrator is depth `0` and workers must remain at depth `1`
- `parent_worker_id` when the handoff needs to name the orchestrator dispatch that created the worker
- `pause_reason` and `human_action_required` when the sprint is `awaiting_human`
- `escalation_reason` when the sprint is `escalated_to_human`

## Archive Policy

Archive only after all of the following are true:
- `review.md` exists and says PASS
- the reviewed work matches the approved contract
- `docs/live/features.json` and `docs/live/progress.md` have been updated to reflect the reviewed outcome
- the runnable active sprint has a clear next action for the backlog

On archive:
- move or copy the complete sprint evidence into `docs/archive/<FEAT-ID>_<timestamp>/`
- preserve at minimum `sprint_proposal.md`, `contract.md`, `handoff.md`, `review.md`, and `status.json`
- keep the archive immutable except for corrections required to preserve historical truth

Do not archive:
- failed reviews
- build/startup triage failures
- parked work awaiting human input
- escalated work that still needs a resume trail
- partial work with no decisive review outcome

## Scripts and Automation Boundary
`docs/scripts/*` exists for bootstrap and orchestration helpers only. Scripts may inspect state, help reconcile it, and record narrowly scoped timeout metadata, but they must never become the hidden source of truth for the harness.

Any script-driven mutation must be reflected back into the documented file contracts in `docs/live/*`, `.harness/<FEAT-ID>/*`, or `docs/archive/*`. If a script and the state files disagree, the state files win until the discrepancy is reconciled explicitly.

Scripts must surface missing or inconsistent backlog data instead of inventing a next feature choice. File contracts stay canonical even when helper output is convenient.

## Role Responsibilities

### Router: `using-agents-stack`
Reads durable state, chooses the next phase, and dispatches exactly one fresh worker/sub-agent/Task agent with explicit worker metadata and phase-appropriate tool scope. It routes; it does not implement, review, or rewrite history inline.

All leaf roles below are worker prompts run in fresh workers. None of them may spawn additional workers.

### `project-initializer`
Worker prompt. Creates or repairs `docs/live/*` and `docs/reference/*` so the repo has truthful durable state. It does not open an execution sprint unless a human explicitly chose one.

### `generator-proposal`
Worker prompt. Turns one dependency-ready backlog item into a bounded sprint proposal with explicit scope, allowed files, forbidden areas, acceptance checks, and risks. It does not write implementation code.

### `evaluator-contract-review`
Worker prompt. Attacks the proposal. It either returns or materializes `contract.md` as the approved execution boundary, or rejects the proposal with specific revision demands. It must not receive broad repo write access outside that artifact path.

### `generator-execution`
Worker prompt. Implements only the approved contract, records reproducible runtime details, performs build/startup triage before review, and writes `handoff.md` only when the sprint is actually reviewable. It does not self-approve, does not widen scope silently, and does not spawn helpers.

### `adversarial-live-review`
Worker prompt. Reproduces the result against the contract and issues exactly one of `PASS`, `FAIL`, or `BLOCKED` with evidence. It does not update global state, must not receive broad write access, and must reject hardcoded or static pass conditions that do not prove a real state transition.

### `state-update`
Worker prompt. Makes the repo tell the truth after review or blocked retry. It updates `docs/live/*`, preserves failed sprint evidence, archives PASS results, and translates blocked or exhausted work into `awaiting_human` or `escalated_to_human` when automation must stop.

## Review Verdict Contract
Every independent review must end with exactly one verdict: `PASS`, `FAIL`, or `BLOCKED`.
- `PASS`: the approved contract was met, the evidence is reproducible, and state-update may close and archive the sprint
- `FAIL`: the sprint stays active, defects are listed explicitly, a clean restore boundary is named for the next retry, and the next retry instructions point back to the same sprint
- `BLOCKED`: the reviewer could not reach a truthful PASS/FAIL because an environment, dependency, missing-evidence, or human-decision problem prevented judgment; the blocker and next recovery step must be explicit

Every review artifact must include:
- evidence checked
- contract criteria passed or failed
- before/action/after state-transition evidence, not just a final static state
- defect list or blocker list
- next owner
- retry, pause, or recovery instructions

Hardcoded end states, static snapshots without the triggering action, and acceptance criteria that can pass without exercising the feature are invalid review evidence.

Generator-authored review artifacts are invalid. `review.md` and `qa.md` only count when they were produced by the independent review phase.

## Before Editing Anything

1. Read this file.
2. Read the relevant `docs/live/*` files.
3. If a sprint is active or parked, read the local `.harness/<FEAT-ID>/` artifacts before touching code.
4. Stay within the current phase boundary. If the correct fix requires a different phase, hand off instead of smuggling it in.

## Success Condition

The harness is healthy when a new agent can enter cold, inspect the files above, identify the single correct runnable owner and phase, see any parked human gates or escalations clearly, and continue safely without relying on prior chat context.
