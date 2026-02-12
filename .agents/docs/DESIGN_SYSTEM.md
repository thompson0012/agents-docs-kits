# DESIGN_SYSTEM.md — Visual & Interaction Standards

> **STATUS**: TEMPLATE
> **OWNER**: Human (final authority) / AI (maintenance)
> **LAST REVIEWED**: 2026-02-12

**Purpose**: This document defines the visual and interaction standards for the project, ensuring consistency and high-quality UI/UX across all components.

## Tokens

**Purpose**: Define the foundational design values used to build the interface.

| Token | Description | Value Example |
|-------|-------------|---------------|
| `color-primary` | Primary brand color. | `#3b82f6` *(Example — fictional, delete before use)* |
| `color-surface` | Background color for cards and modals. | `#ffffff` *(Example — fictional, delete before use)* |
| `spacing-base` | Base unit for all spacing. | `4px` *(Example — fictional, delete before use)* |
| `font-size-body` | Standard text size. | `16px` *(Example — fictional, delete before use)* |

## Components

**Purpose**: Guidelines for creating and using reusable UI components.

- **Buttons**: Use primary variants for main actions and ghost/outline for secondary actions. Ensure a minimum touch target size of 44x44px.
- **Inputs**: Always include a clear `<label>` and provide immediate validation feedback.
- **Modals**: Use for focused tasks that require user attention. Ensure the modal can be closed via the `Esc` key.

## Motion & Accessibility

**Purpose**: Standards for animations and inclusive design.

- **Motion**: Keep animations short (< 300ms) and purposeful. Support `prefers-reduced-motion` media queries to disable non-essential animations.
- **Accessibility**:
  - **Semantic HTML**: Use proper tags (`<nav>`, `<main>`, `<footer>`) to provide structure for screen readers.
  - **ARIA**: Use ARIA attributes only when standard HTML elements are insufficient.
  - **Keyboard Navigation**: All interactive elements should be reachable and operable using only the keyboard.
  - **Contrast**: Maintain a minimum contrast ratio of 4.5:1 for standard text (WCAG 2.1 AA).

## Icons & Assets

**Purpose**: Guidance on selecting and managing visual assets.

- **Icon Library**: Prefer SVG-based icon libraries (e.g., Lucide, Heroicons) for scalability and performance.
- **Alt Text**: All meaningful images should have descriptive `alt` text. Use `alt=""` for purely decorative images.
- **Performance**: Optimize all raster images (PNG, JPEG) using modern formats like WebP or Avif where supported.
