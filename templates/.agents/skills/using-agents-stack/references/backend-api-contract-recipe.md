# Backend API Contract Recipe

This reference helps agents-stack proposal and review workers make backend/API work observable without inventing a second contract.
It is guidance, not a harness contract. If it conflicts with `AGENTS.md`, `.harness/<id>/contract.md`, or the state-machine rules, those sources win.

## When to consult

Use this reference when the selected work is primarily API-visible, service-visible, or auth-boundary-visible and the prompt or proposal would otherwise be too generic.
It is especially useful when reviewers must distinguish a real endpoint behavior change from a plausible implementation narrative.

## What the contract or review should make observable

For backend/API work, the contract or proposal should usually name:
- the route, method, or entrypoint
- the caller identity or auth boundary when one matters
- the request shape or fixture input needed to exercise the path
- the expected status code, response shape, or durable side effect
- the failure path that proves validation, auth, or dependency handling is real
- the exact command, HTTP call, or reproducible script the reviewer will run
- the stable `AC-###` ids that tie request/response checks back to the contract

## Guardrails

- Do not replace `.harness/<id>/contract.md` as the canonical sprint contract.
- Do not treat unit-test success alone as proof when the contract is about endpoint behavior or data integrity.
- Require a criterion per meaningful outcome: success path, auth/permission denial, validation failure, idempotency/retry behavior when relevant.
- If the signoff could be reward-hacked by a canned response, static fixture, or bypassed auth boundary, tighten the slice or fail it.
- For stateful work, require before/action/after evidence tied to durable storage, emitted records, or observable logs — not only returned JSON.
- If the work reaches across services or third-party boundaries, name which boundary is in scope and which is explicitly deferred.
