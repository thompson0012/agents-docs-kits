---
name: contract-review
description: Use when a generator proposal is ready and harness-engineering needs to hand it to `delivery-control/contract-review` for the authoritative approval or rejection decision.
---

# Contract Review Reference

## Purpose

Bridge from proposal to the real contract gate.
This reference does not approve or reject scope itself; it packages the proposal so `delivery-control/contract-review` can make the authoritative decision.

## Core contract

- Do not review the contract in parallel here. Route the proposal to `delivery-control/contract-review`.
- Hand off the exact materials the gate needs: proposal, target files, forbidden changes, launch command, QA script, success criteria, evidence expectations, and known risks.
- Treat `docs/reference/requirements.md` as the upstream requirements source when it exists.
- Treat `docs/live/contract.md` as the canonical approved contract when the gate approves the slice.
- Keep browser QA separate. The contract gate checks whether the slice is buildable and judgeable later; `delivery-control/frontend-evaluator` checks the delivered browser experience.
- If the gate rejects the proposal, return the required revisions to the proposal owner without pretending the slice is approved.

## Handoff bundle

Include:

- the current proposal
- requirement source
- launch command
- QA script grounded in live behavior
- explicit pass conditions
- forbidden changes
- open risks or assumptions
- who revises the proposal if it is rejected

## Outputs

- `Route to delivery-control/contract-review.`
- the proposal bundle needed for that gate
- next owner after approval or rejection

`contract.md` and `proposal_feedback.md` remain workflow vocabulary here. Canonical repo truth belongs in `docs/live/contract.md` and the live docs, not package-local state files.

## Failure modes

- Acting like this reference is the approval authority.
- Writing a private contract file instead of using the canonical live contract path.
- Mixing evaluator concerns into the contract gate.
- Letting a rejected proposal drift into implementation anyway.
