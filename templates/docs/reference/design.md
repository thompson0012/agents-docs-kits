# Design Reference

This starter is for generative UI work that should feel authored, not scaffolded. Functional output is necessary but not sufficient.

## Design language

- Build around clear hierarchy: every screen should make the primary action, current state, and supporting context obvious at a glance.
- Prefer composed surfaces over generic component dumps. Cards, panels, and controls should look intentionally related.
- Use contrast to signal importance, not decoration. Text, controls, and status cues must remain legible in every supported theme.
- Motion should explain state change, not distract from it. Keep transitions purposeful, brief, and tied to interaction or data updates.
- Empty, loading, error, and success states are part of the design, not cleanup work.
- Default library styling is a starting point only. Reviewers should reject results that still look like untouched scaffold output.

## Generative UI expectations

Generators should produce interfaces that are:

- system-aware: layout responds to real content length and viewport changes,
- stateful: loading, error, disabled, and success cases are explicit,
- inspectable: interactive elements expose stable hooks for QA when needed,
- expressive: visual treatment has intent, not just utility,
- maintainable: tokens, spacing, and interaction patterns are reused consistently.

## Review bar

Adversarial review should check four axes:

1. Functionality: the intended interaction works under realistic conditions.
2. Craft: spacing, typography, alignment, and responsiveness hold up without obvious rough edges.
3. Design quality: color, hierarchy, motion, and states feel coherent and product-ready.
4. Originality: the result avoids generic checkbox-and-card boilerplate when the feature calls for a designed experience.

## Common fail conditions

Reject work when any of the following are true:

- contrast drops below an obviously safe readability bar,
- the feature works only in the happy path,
- interactions depend on brittle text selectors or invisible state,
- the output is technically correct but visually generic,
- responsive or keyboard states were ignored,
- motion is noisy, ornamental, or missing where state change needs explanation.

## Generator done bar

Before declaring UI work ready for review, confirm:

- the primary flow is testable end to end,
- empty/error/loading states are designed,
- focus and hover states are visible,
- theme-specific colors still preserve hierarchy,
- the feature adds deliberate visual character appropriate to the product.
