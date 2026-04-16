# Async Worker Contract Recipe

This reference helps agents-stack proposal and review workers make background jobs, queues, schedulers, and retrying workers observable without inventing a second contract.
It is guidance, not a harness contract. If it conflicts with `AGENTS.md`, `.harness/<id>/contract.md`, or the state-machine rules, those sources win.

## When to consult

Use this reference when the selected work is not primarily request/response driven and the contract must prove job dispatch, queue state, retries, or asynchronous side effects.

## What the contract or review should make observable

For async/worker work, the contract or proposal should usually name:
- the trigger that enqueues or starts the worker
- the queue, scheduler, or worker entrypoint involved
- the starting state before the job runs
- the action that causes the job to run or retry
- the expected after-state in queue depth, job record, durable storage, emitted event, or observable log
- the retry, dedupe, or idempotency rule when failures matter
- the stable `AC-###` ids that tie each async outcome to its proof path

## Guardrails

- Do not accept a final database state alone when the contract is about the transition from enqueue to execution to completion.
- If the worker is retryable, require proof of the retry trigger and the post-retry state rather than a one-shot happy path.
- If the worker should not duplicate work, require explicit proof of dedupe or idempotency under repeated triggers.
- If a reviewer cannot tell whether the job actually ran versus a record being pre-seeded, the sprint is not review-ready.
- Make the environment assumptions explicit: queue backend, scheduler cadence, fixture data, and any manual kick command the reviewer must use.
