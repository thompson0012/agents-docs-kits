# FRONTEND_GUIDELINES.md — Frontend Development Standards

> **STATUS**: TEMPLATE
> **OWNER**: Human (final authority) / AI (maintenance)
> **LAST REVIEWED**: 2026-02-12

**Purpose**: This document provides deeper, example-heavy rules for frontend development. It focuses on maintainable patterns, accessibility, and performance.

## Preferred Patterns

**Purpose**: Document the coding styles and patterns used throughout the frontend.

- **Composition over Inheritance**: Prefer building complex components by combining simpler ones rather than using class inheritance.
- **Hooks for Logic**: Encapsulate reusable logic in custom hooks to keep components focused on the UI.
- **Controlled Components**: Prefer controlled components for forms to ensure a single source of truth for the data.

**Example (fictional, delete before use): Custom Hook for Data Fetching**
```typescript
function useFetchData(url: string) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(result => {
        setData(result);
        setLoading(false);
      });
  }, [url]);

  return { data, loading };
}
```

## Do / Don’t Table

**Purpose**: Quick reference for common development practices.

| Do | Don't |
|----|-------|
| Use semantic HTML elements (e.g., `<button>` for actions). | Use `<div>` or `<span>` with click handlers for buttons. |
| Memoize expensive calculations using `useMemo`. | Recalculate large data sets on every render. |
| Provide explicit `alt` text for images. | Leave `alt` attributes empty or use redundant text like "image". |

## Folder & Naming Conventions

**Purpose**: Maintain a consistent project structure.

- **Component Folders**: Group components with their styles and tests (e.g., `src/components/Button/`).
- **PascalCase**: Use PascalCase for component filenames and function names (e.g., `Header.tsx`).
- **camelCase**: Use camelCase for utility functions and variables (e.g., `formatDate.ts`).

## Common Gotchas & Anti-patterns

**Purpose**: Highlight pitfalls to avoid.

- **Prop Drilling**: Avoid passing data through many layers of components. Use context or state management instead.
- **Inline Styles**: Avoid using the `style` prop for complex styling. Prefer CSS modules or utility-first CSS.
- **Index as Key**: Avoid using the array index as a key in lists unless the list is static and never changes.

## Performance & Accessibility

- **TTI (Time to Interactive)**: Minimize main-thread work and defer non-critical JavaScript to improve TTI.
- **Bundle Size**: Use dynamic imports (`React.lazy`) and tree-shaking to keep the initial bundle size small.
- **Accessibility**: Ensure all interactive elements have sufficient color contrast and are operable via keyboard.
