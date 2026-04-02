# Sprint Proposal: FEAT-001

## Summary
Polish the existing dark mode toggle implementation after adversarial review. The DOM behavior already works; this sprint closes the quality gap before the feature can be marked complete.

## Workflow State
- Current phase: `review_failed`
- Current owner: `generator`
- Resume source: `review.md`
- Next checkpoint: apply the review directives in `src/theme/ThemeProvider.tsx` and `src/App.tsx`, preserve the failed review evidence, then refresh `handoff.md` for a new adversarial review pass.

## Problem Statement
The first pass correctly adds and removes the `dark` class on `<html>`, but the review failed on two quality bars:
1. dark-mode text contrast is too low
2. the toggle control is a generic checkbox instead of a deliberate UI element

## Scope
- Update theme variables and component styling so dark mode meets the contrast expectation from the review.
- Replace the generic toggle input with a styled, animated SVG-based control.
- Keep the work inside the contracted files.

## Boundaries
- Allowed files: `src/theme/ThemeProvider.tsx`, `src/App.tsx`
- Do not modify routing, package manifests, or unrelated global styling.

## Evidence Required
- Local verification that toggling still applies the `dark` class to `<html>`
- Visual confirmation that dark-mode text remains readable against `#0f172a`
- Updated `handoff.md` that tells the evaluator exactly what to test next
