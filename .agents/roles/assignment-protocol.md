# Swarm Assignment Protocol

Shared protocol for assigning tasks across agent roles.

## 1. Intake

Capture:
- `Objective`
- `Scope In/Out`
- `Success Criteria`
- `Risk Level`
- `Constraints`

Coordinator owns intake quality.

## 2. Decomposition

Split objective into atomic tasks.
Each task must include one clear owner role and one verification method.

## 3. Role Routing Matrix

- `researcher`: unknowns, architecture mapping, evidence gathering
- `implementer`: approved code or doc changes
- `reviewer`: risk-first quality gate
- `verifier`: final acceptance validation
- `swarm-coordinator`: orchestration, drift control, escalation

## 4. Standard Handoff Format

Use this exact payload:

- `Task`: one-sentence objective
- `Role`: assignee role
- `Context`: relevant files, assumptions, constraints
- `Deliverable`: expected artifact
- `Done When`: acceptance criteria
- `Verification`: command/checklist
- `Escalate If`: explicit failure conditions

## 5. Quality Gates

- No task starts without `Done When` and `Verification`.
- Security/high-risk items require explicit approval before implementation.
- Reviewer/verifier gates cannot be skipped for medium+ risk tasks.

## 6. Drift Control

Coordinator checks scope alignment at each milestone.
If drift is accepted, update objective and rationale before continuing.

## 7. Completion

Task is complete only when:
- Acceptance criteria are satisfied
- Verification passes
- Outstanding risks are documented
