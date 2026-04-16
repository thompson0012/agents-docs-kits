# Integration Contract Recipe

This reference helps agents-stack proposal and review workers make third-party or cross-system integrations observable without inventing a second contract.
It is guidance, not a harness contract. If it conflicts with `AGENTS.md`, `.harness/<id>/contract.md`, or the state-machine rules, those sources win.

## When to consult

Use this reference when the selected work depends on an external API, webhook, storage provider, credentialed service, or another system boundary whose behavior must be proved honestly.

## What the contract or review should make observable

For integration work, the contract or proposal should usually name:
- the external boundary or system involved
- the trigger that causes the integration call or callback
- the request or event shape that crosses the boundary
- the observable success result in local state, logs, records, or returned data
- the expected failure behavior when the external system rejects, times out, or returns malformed data
- the fallback or no-fallback rule when recovery matters
- the stable `AC-###` ids that tie each integration outcome to its proof path

## Guardrails

- Do not hide missing credentials, sandbox requirements, or unavailable fixtures inside vague "environment issue" prose.
- If a reviewer cannot tell whether the external path really ran versus a canned local stub, the sprint is not review-ready.
- If the contract depends on a recorded callback or webhook, require proof of both the outbound trigger and the inbound observable effect.
- Make idempotency, retry, and duplicate-delivery expectations explicit whenever the integration is asynchronous or callback-driven.
- If honest review requires a fake or sandbox boundary, say so explicitly and name exactly what remains unproved in production terms.
