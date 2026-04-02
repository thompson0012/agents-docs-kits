# Sprint Contract: FEAT-001

## Objective
Build a React Context provider that toggles a `dark` class on the HTML root.

## Boundaries
- **Allowed Files**: `src/theme/ThemeProvider.tsx`, `src/App.tsx`
- **Forbidden Changes**: Do not modify routing logic or `package.json`.

## Acceptance Criteria (QA Script)
1. Agent-browser navigates to `localhost:3000`.
2. Click the element `@theme-toggle`.
3. Verify the `<html>` tag contains the `dark` class.
4. Verify the background color transitions to `#0f172a`.
