---
name: webapp
description: Use when building an app-like website such as SaaS, dashboards, admin panels, e-commerce flows, or interactive brand experiences that need application state or backend logic.
---

# Fullstack Web App

Build fullstack web applications with the pre-wired template in `template/`: Express, Vite, React, Tailwind CSS, shadcn/ui, and Drizzle ORM.

## Getting Started

Copy `template/` from this skill into your working project directory, then install dependencies from the new project root:

```bash
cd <project-name>
npm install
```

Run the local development server:

```bash
npm run dev
```

This starts the Express backend and the Vite-powered frontend together on the same local port.

## Build Order

Follow this order:

1. **Schema** — define the data model in `shared/schema.ts` first.
2. **Frontend** — build the React components and pages.
3. **Backend** — implement Express routes in `server/routes.ts`.
4. **Integration** — wire frontend and backend through the shared query client and mutations.
5. **Verification** — run browser QA locally, then run `npm run build` before signoff.

## Architecture

- Keep as much of the app in the frontend as makes sense; the backend should own persistence and external integrations.
- Minimize unnecessary file sprawl. Extract when it clarifies ownership, not by reflex.
- For complex apps, it is acceptable to stub backend behavior briefly while the frontend takes shape, but finish the real backend contract before signoff.
- Prefer backend-backed or in-memory canonical state. If you add browser storage, do it deliberately and test it; do not let core correctness depend on a convenience cache.

---

## Webapp Template — Design Notes

The shared design files listed in **References** are authoritative for colors, fonts, type scale, spacing, and quality bar. This section covers template-specific workflow.

### Replacing Placeholder Tokens in `index.css`

The template ships with starter color values in `client/src/index.css`. Replace them with a palette inferred from the product's subject matter before polishing the UI.

- A fitness tracker should feel energetic.
- A recipe app should feel warm.
- A finance dashboard should feel precise.

When deriving a custom palette, use HSL values in `H S% L%` format with matching light and dark variants.

If the subject gives no clear signal and the user gives no style direction after being asked, fall back to the shared defaults in `../shared/01-design-tokens.md`.

### Webapp-Specific Type and Font Rules

- **`text-xl` is the normal heading ceiling.** Most app surfaces should stay compact.
- **Marketing or brand-experience hero sections are the exception.** Use larger display treatment only when the product genuinely contains that kind of surface.
- **Font mapping:** the template's Tailwind setup maps display and body use through the same primary sans stack. Create hierarchy with weight, spacing, and composition unless the app truly needs a second family.

---

## Art Direction by Product Type

| Product Type | Concept-Driven Direction | Token Starting Points |
|---|---|---|
| **SaaS / productivity** | Match the product's personality: calm and typographic, structured and efficient, or visual and spacious. | Neutral surfaces, one accent, typography that fits the product's tone |
| **Dashboard / analytics** | Finance feels sober and precise. Marketing can be warmer and more visual. The data domain sets the tone. | Sans-serif plus optional monospace for data, high contrast, load `dashboards.md` |
| **E-commerce** | Derive the look from the merchandise and audience. | Product-category-driven palette, strong CTA contrast |
| **Brand experience** | Derive everything from the brand promise. | Controlled accents, stronger motion, larger display only where earned |
| **Admin panel** | Utilitarian, clear, efficient. Domain still matters. | Dense layout, restrained color, strong information hierarchy |

---

## Best Practices by App Type

### SaaS Products & Dashboards

- Sidebar navigation with clear grouping when the app needs multiple areas
- Dark mode as a first-class surface when it suits the users
- Real-time updates only when the product benefits from them
- Export paths for charts and tables when the workflow calls for them
- Role-based views when permissions are real, not speculative
- Onboarding or setup guidance when a blank state would otherwise confuse users

### E-Commerce & Online Stores

- Product pages that put imagery, price, and action above the fold
- Fast checkout with as few steps as the product allows
- Faceted search when the catalog size earns it
- Clear trust signals: shipping, returns, reviews, payment confidence
- Mobile-first purchase flow

### Brand Experiences & Marketing Apps

- Scroll-driven narrative only when it supports the story
- Immersive sections only when performance stays under control
- Micro-interactions that reward exploration without becoming noise
- Responsive storytelling that still works on small screens

---

## Types

- Design the data model in `shared/schema.ts` before writing the rest of the app.
- Keep models as simple as the product allows.
- For each model, also define:
  - an insert schema with `createInsertSchema`,
  - an insert type from `z.infer<typeof insertSchema>`,
  - a select type from `typeof table.$inferSelect`.
- Common pitfall: array columns should use the column method form, such as `text().array()`.

## Storage

- Update `IStorage` in `server/storage.ts` for every CRUD operation the app needs.
- Keep the storage interface typed from `@shared/schema`.

## Backend

- Define API routes inside `registerRoutes(httpServer, app)` in `server/routes.ts`.
- Keep routes thin. Validate inputs, delegate persistence to storage, and return truthful responses.
- Validate request bodies with Zod schemas derived from the shared schema.
- Do not create a second server entrypoint unless you are intentionally redesigning the template.

## Frontend

- The template is already wired for hash routing. Preserve `useHashLocation` in `client/src/App.tsx` unless you are deliberately changing the app's routing model across the whole project.
- Add new pages under `client/src/pages` and register them in `client/src/App.tsx`.
- Use `Link` or `useLocation` from `wouter` instead of mutating `window.location` directly.
- For in-page scrolling inside a routed app, use DOM scrolling helpers rather than hash-anchor navigation.
- Use the shadcn form wrapper and `react-hook-form` for forms.
- Use `@tanstack/react-query` for data fetching and mutations.
- Use the shared query client helpers for backend requests instead of scattering raw `fetch()` calls.
- Invalidate the appropriate query keys after mutations.
- Show loading, empty, and error states.
- Use `import.meta.env` for client-side environment variables.
- Add stable `data-testid` attributes to meaningful interactive controls and dynamic content.

## Styling and Theming

- The template uses Tailwind CSS v3.
- Keep the `@tailwind base`, `@tailwind components`, and `@tailwind utilities` directives in CSS.
- Custom properties intended for Tailwind-driven color usage should stay in `H S% L%` format.
- Replace every starter token in `client/src/index.css`; partial palette updates create incoherent themes.
- Use the `@` aliases already configured in the template.
- Prefer `lucide-react` for interface icons and `react-icons/si` for brand logos when needed.

## Dark Mode

1. Keep dark mode class-based.
2. Define matching tokens in `:root` and `.dark`.
3. When not relying on tokenized utility classes, specify explicit light and dark treatments for visual properties.

## Running the Project

Use the stack's normal shell commands from the project root:

```bash
npm run dev
```

For a production sanity check:

```bash
npm run build
NODE_ENV=production node dist/index.cjs
```

## Installing Packages

Install additional dependencies with the package manager in the project root:

```bash
npm install <package-name>
```

## Testing

Read `../shared/12-playwright-interactive.md` for browser QA. Use the current browser automation tool against the local dev server to exercise core flows, inspect responsive states, and capture screenshots only when they support a claim.

## Config File Guidance

- Avoid modifying `server/vite.ts` or `vite.config.ts` unless the task actually requires it.
- Avoid modifying `drizzle.config.ts` unless the data or migration setup truly changes.
- The template already wires path aliases, frontend serving, and the build output locations.

## Environment

Read `references/environment.md` for package inventory, local run commands, and template runtime notes.

## References

**Before writing code**, read the shared design files below, then add any webapp-specific references that match the task.

**Shared design guidance:**
- `../shared/01-design-tokens.md` — always read
- `../shared/02-typography.md` — always read
- `../shared/03-motion.md` — read when the app has motion or animation
- `../shared/05-taste.md` — read for any user-facing app
- `../shared/08-standards.md` — always read

**Webapp-specific references:**
- `references/shadcn_component_rules.md` — when building or modifying shadcn UI
- `references/layout_and_spacing.md` — when structuring page layouts and spacing rhythm
- `references/sidebar_rules.md` — when building or modifying a sidebar
- `references/visual_style_and_contrast.md` — when tuning contrast, borders, shadows, or hero media
- `dashboards.md` — when the app is a dashboard or similarly data-dense surface

## SEO

- Ensure each page has a unique, descriptive title
- Add concise meta descriptions
- Implement Open Graph tags when the product benefits from link previews
