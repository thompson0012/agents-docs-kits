---
name: postflight
description: Use when a delivery cycle reaches closeout and you need to compare the outcome against the canonical contract, then route either to `delivery-control/compound` or to an explicit skip decision.
---

# Postflight Reference

## Purpose

Close the loop honestly.
Postflight decides whether the completed run produced durable knowledge worth extracting after checking what actually happened against the canonical contract and requirement source.

## Core contract

- Re-read `docs/live/contract.md` when it exists.
- Re-read `docs/reference/requirements.md` when it exists.
- Check `docs/live/progress.md`, `docs/live/qa.md` when present, and `docs/live/runtime.md` when present before deciding closeout.
- Decide extract or skip explicitly.
- If extraction is warranted, route to `delivery-control/compound` with a note naming what to preserve.
- If extraction is not warranted, say why the work produced no durable lesson, policy, or truth worth archiving.
- Do not delete evidence before the extraction decision is made.
- Do not treat status cleanup as knowledge capture.

## Inputs

- `docs/live/contract.md`, when present
- `docs/reference/requirements.md`, when present
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/qa.md`, when present
- `docs/live/runtime.md`, when present
- any observed failure, surprise, or durable decision from the run

## Outputs

- extract-or-skip decision
- what to preserve through `delivery-control/compound`, or why nothing will be extracted
- who owns the next action
- any candidate lesson or memory entries to distill

## Failure modes

- judging closeout against memory instead of the canonical contract
- bypassing `delivery-control/compound` after deciding extraction is needed
- wiping the trail before compound can read it
- writing a status summary instead of identifying a durable truth
- skipping extraction without saying why
