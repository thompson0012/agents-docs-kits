# Environment

## Local Development

From the project root:

```bash
npm install
npm run dev
```

This starts the template's Express backend and Vite frontend together. The default port is 5000 unless the project is configured otherwise.

Leave the dev server running while you iterate. After code changes, reload the page in the browser tool and keep going. Restart the server only if it actually crashes or you intentionally switch to a different runtime command.

## Production Sanity Check

When the task needs a local production check:

```bash
npm run build
NODE_ENV=production node dist/index.cjs
```

The client build output goes to `dist/public`, and the bundled server entrypoint is `dist/index.cjs`.

## Browser QA

Use `../../shared/12-playwright-interactive.md` for the browser QA workflow.

In this harness, browser automation goes through the current browser tool:
- open a session,
- navigate to the local URL,
- prefer `observe` to understand state,
- interact with the page using clicks, typing, fills, and keyboard input,
- use screenshots only when they provide evidence that observation alone cannot.

## Template Runtime Notes

- The template is already wired for hash routing in `client/src/App.tsx`. Preserve that setup unless you are intentionally redesigning routing across the whole app.
- `vite.config.ts` uses `base: "./"`; keep asset paths relative unless you are intentionally changing the hosting model.
- Use the shared query client helpers for backend requests so the app stays consistent across local development and built output.
- Prefer backend-backed or in-memory app state as the source of truth. If you add browser storage, do it deliberately and test the actual behavior.

## Packages

After copying `../template/` into the working project, run `npm install`. The template already includes the major packages most webapp tasks need.

### UI Components

- `@radix-ui/react-*` packages for shadcn/ui primitives
- `class-variance-authority`, `clsx`, and `tailwind-merge`
- `cmdk`, `embla-carousel-react`, `input-otp`, `react-resizable-panels`, `vaul`

### Data & Forms

- `@tanstack/react-query`
- `react-hook-form` and `@hookform/resolvers`
- `drizzle-orm`, `drizzle-zod`, `drizzle-kit`
- `zod`, `zod-validation-error`

### Styling

- `tailwindcss`, `autoprefixer`, `postcss`
- `tailwindcss-animate`, `tw-animate-css`
- `@tailwindcss/typography`

### Icons & Visualization

- `lucide-react`
- `react-icons`
- `recharts`

### Animation & Interaction

- `framer-motion`
- `next-themes`

### Backend

- `express`
- `pg`
- `connect-pg-simple`, `express-session`, `memorystore`
- `passport`, `passport-local`
- `ws`

### Utilities & Build Tools

- `date-fns`, `react-day-picker`, `wouter`
- `vite`, `@vitejs/plugin-react`
- `typescript`, `tsx`, `esbuild`
