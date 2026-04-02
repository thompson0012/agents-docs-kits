---
name: generator-proposal
description: Use when a harness mode needs a bounded implementation slice with explicit targets, exclusions, a launch command, a QA script, success criteria, and evidence expectations.
---

# Proposal Reference

## Purpose

Turn the accepted control plan into one honest slice of work.

## Core contract

- Stay within the current control model.
- Keep the slice narrow enough that the next owner can verify it in one honest pass.
- Treat `docs/reference/requirements.md` as the upstream requirement source when it exists.
- Do not write application code.
- Do not widen the scope silently.
- Chunk only when the control model says the task needs it.

## Required sections

- target files
- forbidden changes
- launch command
- QA script
- baseline / success criteria
- evidence expectations
- known risks or open questions

## QA script rules

- Use live interactions, not source inspection.
- Name the exact UI actions or observable checks.
- If browser-facing behavior is involved, make the checks precise enough for `delivery-control/frontend-evaluator` to replay.

## Handoff behavior

- If the proposal is rejected, the generator revises it.
- If it is accepted, `delivery-control/contract-review` turns it into the canonical slice contract at `docs/live/contract.md`.
