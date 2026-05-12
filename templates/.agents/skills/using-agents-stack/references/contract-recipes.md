# Contract Recipes

This reference helps agents-stack proposal and review workers make different domains of work observable without inventing a second contract. It is guidance, not a harness contract. If it conflicts with `AGENTS.md`, `.harness/<id>/contract.md`, or the state-machine rules, those sources win.

Use the recipe that matches the selected work. If the sprint spans multiple surfaces, combine recipes.

---

## Frontend UI

### When to consult
Use when the selected work is frontend UI or browser-visible interaction and the prompt or proposal would otherwise be too generic. Especially useful when the surface needs layout, interaction flow, and data-shape clarity before code exists.

### Prompt-side structure
When a UI contract recipe is useful, prefer the lightest structure that still answers the risk:
- `Mermaid_Logic` for state, branching, and failure flow
- `ASCII_Layout` for spatial hierarchy and composition
- `Data_Schema` only when typed renderer payloads or data binding are part of the risk
- `contract_check` as a private preflight rubric, not a canonical wire format

### What the contract or review should make observable
- the stable `AC-###` id for each meaningful interaction outcome
- the route, page, or component
- the starting state the reviewer must see before acting
- the action the reviewer performs
- the expected after-state
- the reverse or repeated action when the behavior should be reversible or toggleable
- the viewport or device class when layout matters
- the selector, label, or visible text that proves the state changed because of the action, not just because a final state was already rendered
- loading, empty, error, and retry states when those are in scope

### Guardrails
- Do not make these blocks mandatory for all frontend work.
- Do not replace `.harness/<id>/contract.md` as the canonical sprint contract.
- Do not use this reference to bypass real-browser validation.
- Proposal and review workers should tighten the slice or fail it when the signoff could be reward-hacked by a hardcoded final DOM, static screenshot, canned response, or other fake green path that never proves the transition.
- For toggles, undo flows, and other reversible interactions, require proof of the forward transition and the reversal instead of accepting a one-way final state.
- If the browser-visible proof cannot distinguish a real interaction from a seeded end state, the sprint is not review-ready yet.
- Keep diagrams disposable; regenerate them when the code or contract changes.
- For browser signoff, use `frontend-qa`.
- If the selected work is not frontend, skip this recipe.

---

## Backend API

### When to consult
Use when the selected work is primarily API-visible, service-visible, or auth-boundary-visible and the prompt or proposal would otherwise be too generic. Especially useful when reviewers must distinguish a real endpoint behavior change from a plausible implementation narrative.

### What the contract or review should make observable
- the route, method, or entrypoint
- the caller identity or auth boundary when one matters
- the request shape or fixture input needed to exercise the path
- the expected status code, response shape, or durable side effect
- the failure path that proves validation, auth, or dependency handling is real
- the exact command, HTTP call, or reproducible script the reviewer will run
- the stable `AC-###` ids that tie request/response checks back to the contract

### Guardrails
- Do not replace `.harness/<id>/contract.md` as the canonical sprint contract.
- Do not treat unit-test success alone as proof when the contract is about endpoint behavior or data integrity.
- Require a criterion per meaningful outcome: success path, auth/permission denial, validation failure, idempotency/retry behavior when relevant.
- If the signoff could be reward-hacked by a canned response, static fixture, or bypassed auth boundary, tighten the slice or fail it.
- For stateful work, require before/action/after evidence tied to durable storage, emitted records, or observable logs — not only returned JSON.
- If the work reaches across services or third-party boundaries, name which boundary is in scope and which is explicitly deferred.

---

## Integration (Third-Party / Cross-System)

### When to consult
Use when the selected work depends on an external API, webhook, storage provider, credentialed service, or another system boundary whose behavior must be proved honestly.

### What the contract or review should make observable
- the external boundary or system involved
- the trigger that causes the integration call or callback
- the request or event shape that crosses the boundary
- the observable success result in local state, logs, records, or returned data
- the expected failure behavior when the external system rejects, times out, or returns malformed data
- the fallback or no-fallback rule when recovery matters
- the stable `AC-###` ids that tie each integration outcome to its proof path

### Guardrails
- Do not hide missing credentials, sandbox requirements, or unavailable fixtures inside vague "environment issue" prose.
- If a reviewer cannot tell whether the external path really ran versus a canned local stub, the sprint is not review-ready.
- If the contract depends on a recorded callback or webhook, require proof of both the outbound trigger and the inbound observable effect.
- Make idempotency, retry, and duplicate-delivery expectations explicit whenever the integration is asynchronous or callback-driven.
- If honest review requires a fake or sandbox boundary, say so explicitly and name exactly what remains unproved in production terms.

---

## Async Worker (Background Jobs / Queues)

### When to consult
Use when the selected work is not primarily request/response driven and the contract must prove job dispatch, queue state, retries, or asynchronous side effects.

### What the contract or review should make observable
- the trigger that enqueues or starts the worker
- the queue, scheduler, or worker entrypoint involved
- the starting state before the job runs
- the action that causes the job to run or retry
- the expected after-state in queue depth, job record, durable storage, emitted event, or observable log
- the retry, dedupe, or idempotency rule when failures matter
- the stable `AC-###` ids that tie each async outcome to its proof path

### Guardrails
- Do not accept a final database state alone when the contract is about the transition from enqueue to execution to completion.
- If the worker is retryable, require proof of the retry trigger and the post-retry state rather than a one-shot happy path.
- If the worker should not duplicate work, require explicit proof of dedupe or idempotency under repeated triggers.
- If a reviewer cannot tell whether the job actually ran versus a record being pre-seeded, the sprint is not review-ready.
- Make the environment assumptions explicit: queue backend, scheduler cadence, fixture data, and any manual kick command the reviewer must use.

---

## Migration (Schema / Data Transitions)

### When to consult
Use when the selected work changes schema, durable storage layout, backfills, or compatibility assumptions across time.

### What the contract or review should make observable
- the exact schema or data shape before the change
- the action that performs the migration, backfill, or cleanup
- the expected after-state and how it is inspected
- rollback or recovery expectations when the migration is reversible
- any temporary incompatibility window or re-authorization boundary
- the stable `AC-###` ids that tie before/action/after evidence to the contract

### Guardrails
- Do not treat a successful migration command alone as proof; require inspection of the resulting schema or rows.
- If the migration is irreversible, say so explicitly and require stronger preflight checks before approval.
- If the change relies on backfill ordering, batching, or cleanup phases, keep those boundaries explicit instead of burying them in one vague criterion.
- If a reviewer cannot tell whether the after-state came from the migration versus pre-seeded data, the sprint is not review-ready.
- Keep deferred follow-up work honest. A migration contract must not hide required operational cleanup or compatibility removal inside a "later" footnote.
