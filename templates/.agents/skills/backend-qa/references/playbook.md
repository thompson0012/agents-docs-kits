# Playbook

## QA Inventory
Before testing, list:
- core consumer jobs and expected outcomes
- public and internal contracts: endpoints, events, jobs, webhooks, queue messages, auth boundaries
- state transitions, invariants, and data stores touched
- risky dependencies, retry paths, and partial-failure points
- observability sources available: logs, traces, metrics, queue state, before or after data state
- edge cases likely to expose dishonesty, duplication, corruption, or hidden coupling

Every signoff claim should map to at least one explicit check.

## Execution Posture
- Prefer real requests, real workers, real queues, and real dependencies when the live path is available.
- Keep one continuous test thread long enough to observe asynchronous completion, retries, and recovery.
- Capture correlation identifiers early so requests, jobs, logs, traces, and data state can be tied together.
- Re-check persisted state after every meaningful mutation instead of assuming the write or retry path behaved.
- Use mocks only when the real path is unavailable, and report that limitation explicitly.

## Functional Pass
Test the core backend outcomes first, then obvious secondary paths.

Include:
- initial request or event to completed business outcome
- accepted-now, completed-later flows for async jobs or queues
- retryable paths where the first attempt fails but the workflow should still converge
- reversible or compensating actions where the domain supports them
- webhook or queue consumer behavior from delivery to durable state change

A functional pass is incomplete if it proves only one clean success path once.

## Contract Pass
Inspect the service promise, not just whether a handler returns something.

Cover:
- status codes, response body shape, headers, and machine-readable error payloads
- authn and authz behavior for allowed, denied, expired, and missing credentials
- idempotency keys, duplicate delivery rules, conflict handling, and ordering guarantees
- pagination, filtering, sorting, or cursor behavior where consumers depend on it
- explicit distinction between validation failure, conflict, accepted-but-pending, dependency failure, timeout, and unknown error

If callers cannot reliably tell what happened from the contract, this pass fails.

## State and Data Integrity Pass
Verify what changed, not just what the endpoint said.

Cover:
- before and after state in each authoritative store touched by the workflow
- duplicate prevention and at-most-once or at-least-once behavior as designed
- transactional boundaries, partial writes, rollback paths, and compensating updates
- eventual consistency windows and whether they are explicit to callers
- referential integrity, tenant isolation, and invariants after retries or replays

A backend that returns success while the durable state is wrong fails this pass.

## Resilience Pass
Deliberately exercise the failure paths the system claims to handle.

Cover:
- slow or failing dependencies
- timeout and cancellation behavior
- partial outage where one dependency fails while others succeed
- worker restart, process crash, or redelivery during in-flight work
- poison messages, dead-letter handling, replay safety, and retry exhaustion
- degraded mode or fail-closed behavior when a dependency is unavailable

A resilience pass is incomplete if it proves only that failures are logged.

## Observability and Performance Pass
Check whether the system is diagnosable and whether performance stays honest under realistic pressure.

Cover:
- logs, traces, metrics, and job state for the full request or event lifecycle
- correlation between inbound request, downstream calls, retries, and final outcome
- queue depth, lag, saturation, throughput, latency, and timeout signals where relevant
- whether retries, drops, dead letters, throttling, or degraded mode are externally visible
- performance at normal load and at at least one stressful but realistic level

Fast but opaque is not a pass. Observable but collapsing under mild load is not a pass.

## Security and Abuse Pass
Validate trust boundaries, not just successful authorization.

Cover:
- unauthorized, under-authorized, over-authorized, and cross-tenant requests
- secret, token, or PII leakage in payloads, logs, traces, or error responses
- abuse controls such as throttling, replay protection, input size limits, and unsafe defaults
- dangerous state transitions attempted by the wrong actor or in the wrong order
- webhook authenticity or message provenance checks where external producers are involved

Security defects are backend QA findings even when the feature works for a valid user.

## Adversarial Pass
Try to break the backend with inputs and timing that honest traffic will eventually produce.

Stress with:
- malformed, partial, null, duplicate, or schema-adjacent payloads
- rapid repeated requests, duplicate webhook deliveries, and concurrent writes
- large payloads, deep nesting, long strings, unusual Unicode, and boundary numeric values
- delayed dependencies, reordered events, stale retries, and replay after recovery
- mismatched auth context, expired tokens, revoked permissions, and mixed-tenant references

If the system survives only well-formed, serialized, patient traffic, it is not ready.

## Evidence Collection Rules
- Record the exact request, event, or job input that triggered the behavior.
- Capture the response, status, headers, or completion state exactly.
- Preserve identifiers needed to join logs, traces, queue state, and data mutations.
- Record before and after data state when the claim involves persistence or integrity.
- Quote exact error text or machine fields when contract semantics matter.
- Keep notes on what remains unverified so the report does not overclaim.

## Minimum State Coverage
Before signoff, try to touch as many of these as the service meaningfully supports:
- success
- validation failure
- unauthorized or forbidden
- not found
- conflict or duplicate
- accepted and pending async work
- retry and replay
- partial dependency failure
- timeout or cancellation
- concurrent mutation
- maximum or unusual input
- recovery after restart or redelivery
