---
name: generator-execution
description: Use when an approved contract must be implemented from the canonical contract source while keeping live docs truthful and leaving a clean handoff for evaluation or closeout.
---

# Generator Execution Reference

## Purpose

Build the approved slice and leave enough truth for the next role.
Execution follows the canonical contract, not a remembered proposal.

## Core contract

- Read `docs/live/contract.md` before changing code when that contract exists.
- Read `docs/reference/requirements.md` when it exists so implementation stays anchored to the canonical requirement source rather than a paraphrase.
- Implement only the approved contract.
- Keep the live docs honest while work is underway.
- Record what changed, what was verified, what is still risky, and who owns the next decision.
- Start the dev server if the contract requires a live UI.
- Do not self-approve the contract and do not self-evaluate the delivered browser experience.
- Leave a closeout recommendation: route to `delivery-control/compound` for extraction, or say explicitly why extraction should be skipped.

## Required outputs

- updated codebase
- truthful `docs/live/progress.md`
- `docs/live/current-focus.md` if the objective changes
- `docs/live/runtime.md` when explicit delivery control is in use
- a handoff note containing the local URL or other access path, changed files, verification state, and postflight extract-or-skip recommendation

In article vocabulary, this handoff note is the transient stand-in for `handoff.md`; `project_sync.md` is represented by the repo's live docs, not a separate file. The approved contract is canonical in `docs/live/contract.md`, not a package-local artifact.

## Handoff truth should include

- what changed
- what contract clauses were satisfied
- what was verified
- what remains uncertain
- what the evaluator or closeout owner should look at next
- whether closeout should extract through `delivery-control/compound` or skip extraction, with reason

## Failure modes

- Coding from a stale proposal instead of the approved canonical contract.
- Marking work in review without evidence.
- Hiding a setup gap behind a success claim.
- Leaving behind a handoff that only names a URL and nothing else.
- Inventing a parallel state file instead of using the repo's canonical live docs.
- Trying to perform compound extraction during implementation instead of leaving an extract-or-skip handoff.
