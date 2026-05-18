# Playbook — Seven-Layer QA Execution Guide

## Pre-Flight: QA Inventory

Before testing any layer, list:
- Core user journeys and workflows
- Visible UI claims from design specifications
- All interaction states and transitions for every component
- Risky failure modes
- Target viewports and device classes
- Edge cases likely to expose brittle behavior
- Signoff claims to verify

Every signoff claim should map to at least one explicit test.

---

## Layer 1: Visual QA Playbook

**Goal:** Confirm pixel-level fidelity to the design source.

**Procedure:**
1. Open the page in the target browser (Chrome, Safari, Firefox).
2. Use DevTools eyedropper to sample colors from rendered elements.
3. Compare sampled values against design tokens or Figma reference.
4. Measure spacing with DevTools (select element → Computed → margin/padding).

**Checklist:**
- [ ] All colors match design tokens (±0 tolerance for hex values)
- [ ] Font sizes match (±0px), line-heights match (±0.05), letter-spacing matches
- [ ] Spacing (padding, margin, gap) matches design within ±1px
- [ ] Shadows (x, y, blur, spread, color) match design specification
- [ ] Border radius values are from the token inventory, not ad-hoc
- [ ] Gradients: angle and color stops match design
- [ ] Opacity values match (e.g., disabled state at 0.4, not 0.38)
- [ ] Dark mode toggle: no white flash, all elements remap correctly via tokens

**Evidence:** Screenshot overlay (PerfectPixel) or side-by-side comparison with annotated deviations.

---

## Layer 2: Interaction QA Playbook

**Goal:** Confirm every interactive element is complete and correct across all states.

**Procedure:**
1. Identify all interactive elements on the page (buttons, inputs, links, cards, toggles, modals).
2. For each element, test all five states.
3. Test loading states by throttling network (DevTools → Network → Slow 3G).
4. Test error states by triggering failures (invalid form submission, network disconnect).
5. Test navigation: go forward, go back, verify state preservation.

**Checklist:**
- [ ] Default state renders correctly
- [ ] Hover state activates within 100-150ms with correct visual change
- [ ] Active/Pressed state triggers on click/tap with correct visual feedback
- [ ] Focus state appears on Tab navigation with visible focus ring
- [ ] Disabled state is visually distinct but still readable
- [ ] Loading state prevents double-submit and shows appropriate indicator
- [ ] Empty state is graceful — shows meaningful message, not a broken page
- [ ] Error state shows clear message with recovery path
- [ ] Toggles/modals: open AND close correctly (reversible)
- [ ] Back/forward navigation preserves or correctly resets state

**Evidence:** Record before/action/after for each state. Screenshot key transitions.

---

## Layer 3: Design System QA Playbook

**Goal:** Confirm the implementation faithfully uses the design system.

**Procedure:**
1. Search the full source code for hardcoded color values.
2. Inspect elements to verify CSS custom property usage.
3. Check component versions against the design system library.
4. Verify breakpoint consistency across pages.
5. Audit z-index values.

**Checklist:**
- [ ] No hardcoded `#XXXXXX` hex values (search: `#[0-9a-fA-F]{3,8}`)
- [ ] No hardcoded `rgb()` or `hsl()` values (search: `rgb\(`, `hsl\(`)
- [ ] All colors use CSS custom properties (`var(--...)`) or `oklch()` derivations
- [ ] Token naming convention is consistent across all files
- [ ] Design system component library is on the correct version
- [ ] All icons are from the same icon library with consistent stroke width
- [ ] Breakpoints are consistent (check `@media` queries — same values across pages)
- [ ] No magic z-index numbers (`9999`, `99999`) — use design system z-index scale
- [ ] CSS custom property declarations are in the correct scope (`:root` vs component-level)

**Evidence:** Grep search results, component version audit, breakpoint comparison table.

---

## Layer 4: Accessibility QA Playbook

**Goal:** Confirm the feature is usable by everyone.

**Procedure:**
1. Run axe DevTools or WAVE automated scan (catches ~30% of issues).
2. Navigate the entire flow using only keyboard (Tab, Shift+Tab, Enter, Space, Escape).
3. Test with macOS VoiceOver or Windows NVDA screen reader.
4. Check contrast ratios with Stark or Colour Contrast Analyser.
5. Test with OS "Reduce motion" setting enabled.
6. Test with browser font size set to "Very Large".
7. View the page in grayscale (browser DevTools → Rendering → Emulate vision deficiencies).

**Checklist:**
- [ ] Heading hierarchy is logical (h1 → h2 → h3, no skipped levels)
- [ ] All form inputs have associated `<label>` elements
- [ ] All images have `alt` text (descriptive for content, empty `alt=""` for decoration)
- [ ] All interactive elements are keyboard-reachable and operable
- [ ] Focus order matches visual order (no focus traps)
- [ ] Visible focus ring on all focusable elements (no `outline: none` without replacement)
- [ ] Body text contrast ≥ 4.5:1 against background (AA)
- [ ] Large text (≥18px bold or ≥24px) contrast ≥ 3:1 (AA)
- [ ] Primary text contrast ladder: primary ≥ 7:1, secondary ≥ 4.5:1, placeholder ≥ 3:1, disabled ≥ 2:1
- [ ] UI is usable in grayscale — status is not communicated by color alone
- [ ] Touch targets ≥ 44×44px (or 48×48dp for Material Design)
- [ ] `prefers-reduced-motion: reduce` disables all animations and autoplay
- [ ] `prefers-color-scheme: dark` renders correctly without white flash
- [ ] ARIA roles, states, and live regions are correct (no redundant ARIA)
- [ ] Screen reader announces dynamic content changes (form errors, loading completion)

**Evidence:** axe/WAVE report, keyboard navigation trace, contrast measurement values, screen reader recording.

---

## Layer 5: Responsive QA Playbook

**Goal:** Confirm the feature works correctly across all target viewports and devices.

**Procedure:**
1. Start at 1440px (desktop baseline) and resize down to 320px.
2. Test specific breakpoints: 320, 375, 414, 768, 1024, 1280, 1440, 1920, 2560.
3. Test on at least one real mobile device (not just DevTools emulation).
4. Rotate device between portrait and landscape.
5. Set browser font size to "Very Large" and re-test.
6. Zoom to 200% and verify no horizontal scroll.

**Checklist:**
- [ ] No horizontal overflow at any viewport 320px–2560px
- [ ] Essential controls are visible in the initial mobile viewport (no "mystery meat" navigation)
- [ ] Text wraps correctly under long labels and real data at all widths
- [ ] Images scale correctly without distortion
- [ ] Touch targets remain ≥ 44×44px at all breakpoints
- [ ] Sticky headers do not occupy excessive screen space on mobile
- [ ] Modals and dialogs fit within the viewport on small screens
- [ ] Landscape mode: content is not clipped by notches or gesture bars
- [ ] Safe areas respected: no content hidden behind iPhone notch or home indicator
- [ ] Font scaling to 200% does not break layout or truncate text

**Evidence:** Screenshots at each major breakpoint, device test notes.

---

## Layer 6: Content QA Playbook

**Goal:** Confirm the feature handles real-world, messy content.

**Procedure:**
1. Replace all placeholder data with extreme test content.
2. Test each content type separately to isolate issues.
3. Use browser DevTools to edit text content live and observe results.

**Test Cases:**
- **Long text:** "Mohammed bin Salman Al Saud" as username; 500-word paragraph as bio; URL with 200+ characters
- **Emoji:** "🚀 Crypto enthusiast | 💎 Diamond hands | 🌙 To the moon!!!" in a single field
- **RTL:** "مرحبا بالعالم" (Arabic) and "שלום עולם" (Hebrew) if i18n in scope
- **Special characters:** `<script>alert(1)</script>`, `&amp;`, `<>` in user input
- **Missing images:** `<img src="broken-url.jpg">` — verify graceful fallback
- **Extreme numbers:** "¥9,999,999.99" in price field; "1,000,000,000" in counter
- **Mixed content:** "用户123abc用户" (Chinese + numbers + English without spaces)
- **Date formats:** "2024年12月31日", "31/12/2024", "December 31, 2024"

**Checklist:**
- [ ] Long text does not overflow containers or break layout
- [ ] Emoji does not disrupt line-height or cause layout shifts
- [ ] RTL text renders with correct direction (if applicable)
- [ ] Special characters are escaped, not executed (XSS prevention)
- [ ] Broken images show a labeled placeholder, not the browser broken-image icon
- [ ] Extreme numbers fit within their containers without overflow
- [ ] Mixed-language content wraps correctly without orphan characters
- [ ] Empty/null/partial data states render gracefully (no "undefined" or "NaN" visible)

**Evidence:** Screenshots of each stress test case, console error log.

---

## Layer 7: Performance QA Playbook

**Goal:** Confirm the feature feels fast and smooth based on measured metrics.

**Procedure:**
1. Run Lighthouse audit (Desktop and Mobile).
2. Open DevTools Performance panel and record a typical user flow.
3. Test with network throttling (Slow 3G).
4. Test with CPU throttling (4x slowdown).
5. Test back/forward navigation speed.

**Metrics:**
| Metric | Target |
|---|---|
| First Contentful Paint (FCP) | < 1.8s |
| Largest Contentful Paint (LCP) | < 2.5s |
| Cumulative Layout Shift (CLS) | < 0.1 |
| Time to Interactive (TTI) | < 3.8s |
| Total Blocking Time (TBT) | < 200ms |
| Speed Index | < 3.4s |

**Checklist:**
- [ ] FCP < 1.8s on throttled mobile
- [ ] LCP < 2.5s on throttled mobile
- [ ] CLS < 0.1 (no layout jumps during load)
- [ ] Fonts use `font-display: swap` — text is visible during font load, not invisible
- [ ] Images use modern formats (WebP/AVIF) with fallbacks
- [ ] Images have explicit `width`/`height` to prevent layout shift
- [ ] Images use `loading="lazy"` for below-the-fold content
- [ ] Animations run at 60fps (check DevTools → Performance → FPS meter)
- [ ] No animated `width`/`height`/`top`/`left` — only `transform` and `opacity`
- [ ] Back/forward cache works — page restores instantly from bfcache
- [ ] Third-party scripts do not block rendering (use `async`/`defer`)
- [ ] No massive JavaScript bundles blocking interactivity

**Evidence:** Lighthouse report PDF, Performance panel recording, WebPageTest waterfall.

---

## Adversarial Edge-Case Pass (applies across all layers)

Deliberately try to break the surface:

- Rapid repeated clicks (double-submit, triple-toggle)
- Network: offline → online transition
- Browser: resize while animation is playing
- Browser: switch tabs during form submission
- Device: rotate during page load
- Input: paste 10,000 characters into a text field
- Scroll: rapid scroll up/down repeatedly
- Keyboard: hold down Tab key to rapid-fire through focusable elements

If the UI survives only clean data and patient clicks, it is not ready.

## Evidence Collection Rules

- Record the exact state where the issue appears.
- Capture reproduction steps, not just outcomes.
- Quote visible text exactly when reporting copy, labels, or error states.
- Use screenshots or recordings when they clarify a visual or motion claim.
- Keep notes on what remains unverified so the report does not overclaim.
