# Framework

Backend QA uses one signoff lens: Utility × Reliability × Contract. A service is not honestly ready if any one factor is missing.

## Utility
Utility asks whether the backend produces the outcome its consumer actually needs.

Questions to ask:
- Does the endpoint, job, or event flow complete the consumer's real job?
- Does the system return enough information for the next consumer to act without guesswork?
- Do success, empty, delayed, replayed, and recovery states still move the workflow forward?

Failure when missing:
- The service returns technically valid output that does not solve the consumer's job.
- The happy path works, but important real states such as eventual completion, replay, or partial fulfillment leave callers stranded.
- Operators can see activity, but the product outcome is missing or incomplete.

## Reliability
Reliability asks whether the backend stays truthful under failure, retries, concurrency, and load.

Questions to ask:
- What happens on timeout, dependency failure, partial outage, restart, or duplicate delivery?
- Can concurrent or repeated requests corrupt state, double-apply work, or hide failure behind a plausible success?
- Do retries, queues, workers, and compensating paths converge on the correct final state?

Failure when missing:
- The service lies about success, loses work, or applies it twice.
- State becomes inconsistent across storage, caches, queues, or downstream systems.
- Recovery depends on luck, manual cleanup, or hidden operator knowledge.

## Contract
Contract asks whether the backend's public and operational promises are explicit, stable, and honest.

Questions to ask:
- Are status codes, schemas, permissions, idempotency rules, ordering guarantees, and error semantics correct?
- Can callers distinguish validation failure, auth failure, conflict, dependency failure, timeout, and accepted-but-not-finished work?
- Do logs, traces, metrics, and job states preserve the truth of what happened?

Failure when missing:
- Callers receive ambiguous responses and must infer what happened.
- Auth or tenancy boundaries are inconsistently enforced.
- Observability hides the failure mode or makes the blast radius unknowable.

## How the Lens Changes Signoff
The lens changes QA from “did one request succeed?” to “is this backend honest and dependable for the consumers who rely on it?”

Signoff guidance:
- Missing Utility is a signoff failure even if the transport and schema look correct.
- Missing Reliability is a signoff failure even if most requests succeed under light load.
- Missing Contract is a signoff failure even if the internal behavior eventually converges.
- A pass means the backend produces the needed outcome, survives realistic stress without lying, and preserves a stable contract for callers and operators.

## Practical Rule
Do not average the three dimensions together. A strong schema does not cancel out corrupt state. Good throughput does not cancel out dishonest error semantics.
