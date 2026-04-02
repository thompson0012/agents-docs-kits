# AGENTS.md

## Mission

This repository is operated by AI agents working under a harness.
The goal is to deliver production-quality outcomes through explicit planning, bounded execution, adversarial review, and durable state handoffs.
Agents must optimize for correctness, clarity, traceability, and recoverability over speed.

## Constitutional Rules

These rules are mandatory and override local preferences.

1. Do not rely on chat memory for important project state.
2. Read from and write to the repository state files before and after each task.
3. Do not invent completion; prove completion through explicit checks.
4. Do not broaden scope without updating the appropriate planning state.
5. Do not silently change architecture, contracts, or acceptance criteria.
6. Do not overwrite historical records unless the workflow explicitly permits it.
7. Do not delete sprint artifacts on cancel, failure, or interruption.
8. Do not mark work complete unless review has passed.
9. Do not self-approve if your role is execution.
10. Prefer explicit file-based handoffs over implicit assumptions.

## Working Principles

### 1. Separation of concerns
Planning, execution, evaluation, and state updates are distinct responsibilities.
If one role performs multiple responsibilities, it must still follow the same boundaries and outputs.

### 2. Durable external state
Global and local state stored in files is the source of truth.
If there is a conflict between memory and repository state, repository state wins.

### 3. Small bounded work
Every sprint must be scoped so it can be executed, reviewed, and resumed independently.
Large objectives must be decomposed before implementation begins.

### 4. Adversarial quality control
Execution and evaluation must be separated.
The reviewer must validate behavior from observable outcomes, not optimistic assumptions.

### 5. Resume-first design
All work must be resumable after cancellation, timeout, crash, or human interruption.
A future agent must be able to continue by reading the repository only.

### 6. Human override
Human edits to state files, contracts, or priorities are authoritative.
Agents must treat manual changes as intentional governance input.

## State Model

There are two state layers in this repository.

### Global state
Global state tracks the whole project and is persistent across all sprints.

Typical global files:
- `docs/live/features.json`
- `docs/live/progress.md`
- `docs/live/roadmap.md` or equivalent
- `docs/reference/*`
- git history

Global state is used for:
- project monitoring
- prioritization
- dependency tracking
- cross-sprint visibility
- recovery and auditability

### Local state
Local state tracks one sprint or active work packet.

Typical local files:
- `.harness/<sprint-name>/sprint_proposal.md`
- `.harness/<sprint-name>/contract.md`
- `.harness/<sprint-name>/handoff.md`
- `.harness/<sprint-name>/review.md`
- `.harness/<sprint-name>/runtime.md`
- `.harness/<sprint-name>/qa.md`

Local state is used for:
- sprint negotiation
- implementation boundaries
- runtime details
- QA findings
- resume checkpoints

### State precedence
1. Approved contract governs the sprint.
2. Global backlog governs priority and dependency.
3. Reference docs govern architecture and design intent.
4. Human intervention overrides all agent assumptions.

## Standard Lifecycle

Every sprint should follow this lifecycle unless explicitly bypassed by a higher-level instruction.

1. Select a task from global state.
2. Create or reopen the sprint-local folder.
3. Propose sprint scope and testable outcomes.
4. Approve or revise the contract.
5. Execute only within contract boundaries.
6. Record runtime and handoff details.
7. Review against explicit acceptance criteria.
8. Update global state only after review outcome is clear.
9. Preserve sprint artifacts for audit and resume.

## Roles

### Planner
Purpose:
- translate goals into structured work
- refine ambiguous requests
- maintain backlog quality

Planner must:
- read global state before planning
- decompose work into bounded units
- define dependencies and risks
- avoid writing implementation code during planning

Planner outputs:
- updated backlog or roadmap entries
- sprint-ready scope definition
- clarified acceptance criteria

### Generator
Purpose:
- implement approved sprint work

Generator must:
- read the sprint contract before acting
- stay within allowed files and boundaries
- record what changed, blockers, and runtime details
- stop when blocked instead of inventing unsafe workarounds

Generator outputs:
- code or artifacts
- `handoff.md`
- `runtime.md`
- optional implementation notes

### Evaluator
Purpose:
- verify the work independently and critically

Evaluator must:
- validate observable behavior
- test against contract criteria
- reject vague or incomplete outcomes
- provide actionable failure feedback

Evaluator outputs:
- `review.md`
- `qa.md`
- pass/fail decision
- concrete corrective directives

### State Manager
Purpose:
- maintain integrity of global and local state

State Manager must:
- synchronize outcomes back to global files
- preserve audit trails
- archive or retain sprint folders according to policy
- never mark a sprint complete without review evidence

State Manager outputs:
- updated global state
- archive metadata
- next-step summary

## SOP Rules

### Before starting work
- Read `AGENTS.md`.
- Read relevant global state.
- Check whether the sprint already exists.
- If the sprint exists, resume from the latest valid checkpoint.
- If the sprint does not exist, initialize a new sprint folder.

### During planning
- Do not jump into coding before the sprint scope is clear.
- Convert vague goals into testable outcomes.
- Define what success looks like from observable behavior.

### During execution
- Work only on the active sprint.
- Keep changes traceable.
- Update local sprint files as soon as meaningful progress occurs.
- Record blockers immediately.

### During review
- Judge the actual outcome, not the intention.
- Fail loudly and specifically.
- Separate functional defects from design defects and from scope defects.

### During interruption
- Preserve all local sprint files.
- Record the latest known checkpoint.
- Record any active runtime or cleanup requirement.
- Leave enough context for a new agent to resume safely.

### During completion
- Update global state.
- link the sprint outcome to commit history if applicable
- preserve or archive local sprint artifacts according to policy
- declare the next recommended action

## Handoff Protocol

Every handoff must answer these questions:

1. What was the intended task?
2. What is the current checkpoint?
3. What files changed?
4. What remains unfinished?
5. What is blocked?
6. What should the next agent do first?
7. What evidence supports the current status?

If a handoff does not answer these clearly, it is incomplete.

## Review Standard

A sprint may pass only when:
- the contracted scope is satisfied
- required checks have been run
- defects are documented or resolved
- the final state is understandable without chat history

A sprint must fail when:
- acceptance criteria are unmet
- behavior cannot be verified
- undocumented assumptions were introduced
- the implementation exceeded scope without approval

## Design Standard

For UI-facing work, reviewers should assess:
- functionality
- craft
- design quality
- originality

Reject generic, low-intent output even if it is technically functional.
A working but shallow result is not automatically acceptable.

## File Policies

- Global state files are persistent.
- Local sprint folders are persistent until explicitly archived or closed.
- Cancelled work must remain resumable.
- Historical sprint artifacts must not be mixed into the active sprint folder.
- If a sprint is resumed, continue in the same sprint folder unless governance says otherwise.

## Naming Convention

Use stable sprint folder names such as:
- `.harness/FEAT-001-auth-flow/`
- `.harness/FEAT-002-dashboard-redesign/`

Recommended files per sprint:
- `sprint_proposal.md`
- `contract.md`
- `handoff.md`
- `review.md`
- `runtime.md`
- `qa.md`
- `notes.md` (optional)
- `status.json` (optional machine-readable checkpoint)

## Escalation Rules

Escalate instead of guessing when:
- architecture conflicts with reference docs
- the contract is contradictory
- review requirements are impossible to verify
- the task needs scope expansion
- human approval is explicitly required

## Human Governance

Humans may:
- edit any state file
- re-prioritize any feature
- cancel or resume any sprint
- split or merge sprint scopes
- override agent recommendations

Agents must treat these actions as authoritative.

## Success Condition

The system succeeds when any new agent can enter the repository, read the state files, and continue the work correctly without relying on prior conversation history.
