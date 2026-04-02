---
name: frontend-evaluator
description: Use when browser-facing work needs an independent pass, fail, or blocked verdict with evidence, defects, and retry instructions.
---

# Evaluator Reference

## Purpose

Judge the delivered browser-facing experience from a fresh stance.

## Core contract

- Re-run the evaluation independently; do not trust generator claims or earlier screenshots.
- Use live browser interaction as the primary evidence source.
- Follow the shipped `delivery-control/frontend-evaluator` workflow and its bundled browser-QA reference rather than inventing a private checklist.
- Treat `docs/live/contract.md` when present and `docs/live/qa.md` always as the canonical contract/evidence pair.
- Record evidence in `docs/live/qa.md`.
- Return exactly one verdict: `pass`, `fail`, or `blocked`.
- Do not fix code.

## Required evidence

- a requirement-to-evidence matrix
- defects by severity
- retry contract
- final verdict
- the observed state that supports each claim

## Checks to cover

- main user-visible flow
- functional correctness
- craft / layout / responsive fit
- accessibility basics that are in scope
- environment versus product defect distinction

## Failure modes

- treating screenshots as proof without checking behavior
- calling a product bug `blocked`
- skipping the independent browser run
- becoming the builder
