# QA Evidence: FEAT-001

## Environment Used

- Start command: `npm run dev`
- URL / entrypoint: `http://localhost:3000`
- Test command: browser verification against the contract script

## Acceptance Checks

1. Clicking `@theme-toggle` toggles dark mode.
   - Action: Opened the app and clicked the toggle once.
   - Observed result: `<html>` gained the `dark` class.
   - Status: PASS
   - Evidence: Browser session state and `review.md` summary.

2. Dark mode background transitions to `#0f172a`.
   - Action: Observed the shell after toggling dark mode.
   - Observed result: The page background transitioned to `#0f172a`.
   - Status: PASS
   - Evidence: Visual/browser check during the review pass.

3. Dark-mode text contrast is acceptable.
   - Action: Reviewed body and surface text after dark mode activated.
   - Observed result: Contrast remained too low against the dark surface.
   - Status: FAIL
   - Evidence: This is the design-quality failure recorded in `review.md`.

4. The toggle control is purpose-built and animated rather than a generic checkbox.
   - Action: Inspected the rendered control after toggling.
   - Observed result: The control still read as a generic checkbox-style UI.
   - Status: FAIL
   - Evidence: This is the originality failure recorded in `review.md`.

## Additional Findings

- The functionality is sound, but the sprint stays open because the quality rubric failed.

## Reproducibility Gaps

- None; the failure is preserved in the review artifacts.
