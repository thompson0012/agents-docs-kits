# Migration Contract Recipe

This reference helps agents-stack proposal and review workers make schema or data transition work observable without inventing a second contract.
It is guidance, not a harness contract. If it conflicts with `AGENTS.md`, `.harness/<id>/contract.md`, or the state-machine rules, those sources win.

## When to consult

Use this reference when the selected work changes schema, durable storage layout, backfills, or compatibility assumptions across time.

## What the contract or review should make observable

For migration work, the contract or proposal should usually name:
- the exact schema or data shape before the change
- the action that performs the migration, backfill, or cleanup
- the expected after-state and how it is inspected
- rollback or recovery expectations when the migration is reversible
- any temporary incompatibility window or re-authorization boundary
- the stable `AC-###` ids that tie before/action/after evidence to the contract

## Guardrails

- Do not treat a successful migration command alone as proof; require inspection of the resulting schema or rows.
- If the migration is irreversible, say so explicitly and require stronger preflight checks before approval.
- If the change relies on backfill ordering, batching, or cleanup phases, keep those boundaries explicit instead of burying them in one vague criterion.
- If a reviewer cannot tell whether the after-state came from the migration versus pre-seeded data, the sprint is not review-ready.
- Keep deferred follow-up work honest. A migration contract must not hide required operational cleanup or compatibility removal inside a "later" footnote.
