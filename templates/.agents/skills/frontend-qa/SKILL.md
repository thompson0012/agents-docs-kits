---
name: frontend-qa
description: Use when validating frontend behavior in a real browser, including functional flows, visual quality, accessibility, responsive behavior, perceived performance, or adversarial edge cases.
---

# Frontend QA

## Overview

Frontend QA validates what users actually experience in the browser.
Signoff lens: **Utility × Usability × Craft** — does it solve the right job,
stay understandable under real interaction, and feel intentional rather than merely unbroken.

Shared QA methodology is defined in [qa-core.md](../references/qa-core.md). Read it first.
This file defines only frontend-specific extensions.

## Domain-Specific Passes

In addition to the 7 core passes defined in qa-core.md:

- **Visual pass** — initial viewport, post-interaction states, dense states, smallest supported viewport
- **Accessibility pass** — semantics, keyboard flow, focus visibility, contrast, announcements, touch targets
- **Perceived-performance pass** — load behavior, navigation smoothness, layout stability, back/forward behavior
- **Responsive pass** — breakpoint behavior, resize/zoom stress

## Signoff Criteria

- Missing **Utility**: the feature works but doesn't help the user → FAIL
- Missing **Usability**: users hesitate, misclick, or need instructions; accessibility gaps block completion → FAIL
- Missing **Craft**: visual noise, weak hierarchy, or broken edge states degrade trust → FAIL

## References

- [qa-core.md](../references/qa-core.md) — Shared QA methodology
- [Framework](references/framework.md) — Utility × Usability × Craft in detail
- [Playbook](references/playbook.md) — Pass execution playbook
- [Reporting](references/reporting.md) — Findings format and severity classification
