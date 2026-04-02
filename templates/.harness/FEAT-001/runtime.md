# Runtime Notes: FEAT-001

## Environment

- App root: project root
- Start command: `npm run dev`
- Test command: browser verification against the contract script
- Local URL: `http://localhost:3000`

## Commands Run

- `npm run dev` -> started the app for browser verification.
- Opened `http://localhost:3000` and toggled `@theme-toggle`.

## Evidence

- Clicking the toggle adds the `dark` class to `<html>`.
- The page background transitions to `#0f172a` in dark mode.
- The rendered UI still failed review because dark-mode text contrast was too low and the toggle looked like a generic checkbox.

## Blockers / Gaps

- None. The failure is intentionally preserved so the next generator pass can reuse the same evidence.
