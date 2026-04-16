# Contract validation fixtures

Use this fixture lane for contract-review guard behavior that must prove a sprint contract is execution-ready before code starts. Router evals answer "which child should run next?" Retry guard fixtures answer "may a failed sprint retry cleanly?" Contract-validation fixtures answer "is this contract specific enough that execution and review can be judged without debate?"

Keep this separate from router and retry fixtures:
- `evals.json` models prompt-to-route expectations for the router
- `guard-eval-fixtures.md` models retry eligibility and temporal clean-resume truth
- contract-validation fixtures model contract shape, acceptance-id discipline, and fail-closed approval readiness

## Portable schema

```yaml
fixtures:
  - id: unique-fixture-id
    phase_or_artifact_gate: contract approval gate
    before_state:
      required_artifacts:
        - .harness/WORKSTREAM-003/contract.md
      required_fields:
        contract.md.acceptance_criteria[0].id: AC-001
      invariants:
        - every acceptance criterion uses a stable `AC-###` id
        - every criterion includes `Requirement` and `Evidence`
    guard_action: Decide whether the contract is execution-ready
    expected_after_state:
      outcome: allow_contract
      next_owner: generator-execution
      evidence:
        - execution can proceed without inventing hidden acceptance logic
    fail_closed_expectation:
      when:
        - required sections are missing
        - acceptance ids are duplicated or malformed
        - stateful criteria omit before/action/after fields
        - reversible criteria omit reverse-check proof
      outcome: deny_contract
      evidence:
        - keep the sprint in contract-review or proposal revision state
```

## Positive example: bounded contract with complete acceptance fields

```yaml
- id: contract-allows-structured-acceptance-criteria
  phase_or_artifact_gate: contract approval gate
  before_state:
    required_artifacts:
      - .harness/WORKSTREAM-003/contract.md
    required_fields:
      contract.md.sections: [Objective, Allowed Files, Forbidden Changes, Acceptance Criteria, Verification Plan, Assumptions & Reward-Hack Surfaces, Non-Goals / Deferred Work]
    invariants:
      - AC-001 is non-stateful and includes Requirement and Evidence
      - AC-002 is stateful and reversible and includes Before state, Action, After state, and Reverse check
      - allowed files and forbidden changes are both explicit
  guard_action: Decide whether the contract is execution-ready
  expected_after_state:
    outcome: allow_contract
    next_owner: generator-execution
    evidence:
      - execution can start without inventing acceptance shape or file boundaries
  fail_closed_expectation:
    when:
      - any required section disappears
      - any acceptance id is duplicated or malformed
    outcome: deny_contract
```

## Negative example: stateful criterion missing transition proof

```yaml
- id: contract-denies-stateful-criterion-without-before-after
  phase_or_artifact_gate: contract approval gate
  before_state:
    required_artifacts:
      - .harness/WORKSTREAM-004/contract.md
    invariants:
      - AC-002 is flagged stateful=yes
      - AC-002 omits Before state or After state
  guard_action: Decide whether the contract is execution-ready
  expected_after_state:
    outcome: deny_contract
    evidence:
      - contract review must fail closed because the reviewer would be forced to invent the missing transition proof
  fail_closed_expectation:
    when:
      - a stateful criterion is defined only as a final static state
    outcome: deny_contract
```

## Negative example: reversible criterion missing reverse check

```yaml
- id: contract-denies-reversible-criterion-without-reverse-check
  phase_or_artifact_gate: contract approval gate
  before_state:
    required_artifacts:
      - .harness/WORKSTREAM-005/contract.md
    invariants:
      - AC-003 is flagged reversible=yes
      - AC-003 omits Reverse check
  guard_action: Decide whether the contract is execution-ready
  expected_after_state:
    outcome: deny_contract
    evidence:
      - contract review must fail closed because a one-way final state could fake success
  fail_closed_expectation:
    when:
      - reversible behavior can be "approved" without proving reversal
    outcome: deny_contract
```
