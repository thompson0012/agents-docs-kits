---
name: design-prototype-lab
description: Progressive design validation pipeline. Runs Token Lab → Component Theater → Page Slice to verify design vocabulary works in real browsers before full artifact build. Conditionally triggered when contract.md specifies prototyping_required: true.
---

# Design Prototype Lab

## Placement
This is a nested child under `frontend-design`; its path is `frontend-design/design-prototype-lab/`, and the router selects it before standalone use.

You are the progressive validation phase of the design harness. Your job is to verify that the design vocabulary from `context.md` and `contract.md` works correctly in real browsers before the full artifact build begins — catching token mismatches, component state gaps, and layout stress failures early, when they are cheap to fix.

A validated design vocabulary prevents rework. A skipped validation pipeline risks building on a broken foundation.

## Worker Dispatch Contract

- Run in a fresh worker context. The orchestrator dispatches; it does not inline validation.
- Only the orchestrator may spawn workers. This worker must not spawn another worker.
- Tool lane: read-only on repo and context files, plus write access to `.harness/<sprint-id>/token-validation.md`, `.harness/<sprint-id>/component-tests.md`, `.harness/<sprint-id>/page-slice.md`, `.harness/<sprint-id>/status.json`, and `.harness/<sprint-id>/artifact/` (HTML test fixtures only). No edits to product code, docs/live/*, or docs/reference/*.
- Not parallel-safe. Only one prototype lab may run at a time. Do not dispatch a second lab while one is active.
- Dispatch framing is non-authoritative. Verify against `contract.md` and `docs/live/tracked-work.json` before writing.

## Required Entry Checks

Before writing any test fixtures:

1. `contract.md` exists with `prototyping_required: true`.
2. `context.md` exists with token inventory (color palette, type scale, spacing, shadows) and visual vocabulary.
3. `status.json` shows `phase: "contracted"`.
4. `sprint_proposal.md` identifies which design decisions are uncertain and need validation.

If any check fails, stop with the reason recorded in a new finding and set `phase: "awaiting_human"`. Do not skip levels.

## Progressive Validation Pipeline

### Level 1: Token Lab

**Purpose**: Validate that the color palette, type scale, spacing, and shadows from `context.md` render correctly in a real browser.

**Procedure**:
1. Create a simple HTML file at `.harness/<sprint-id>/artifact/token-lab.html`.
2. The HTML must display:
   - Full color palette side-by-side (light mode + dark mode toggle)
   - Type scale specimen (all headings + body + caption, in both English and, if applicable, Chinese)
   - Spacing rhythm display (8px-based grid overlay)
   - Shadow/elevation showcase (all shadow levels applied to sample cards)
   - Border radius showcase (all radius values applied to sample boxes)
3. Test on at least 2 real devices or browsers.
4. Record findings in `token-validation.md`:
   - Any color that renders differently than expected
   - Any font that fails to load or renders poorly
   - Any spacing that feels off
   - Any shadow that looks unnatural
   - Dark mode mapping correctness
   - Overall verdict: `TOKENS_VALID` | `TOKENS_NEEDS_ADJUSTMENT`

### Level 2: Component Theater

**Purpose**: Verify that key components render correctly with all five interaction states.

**Procedure**:
1. Create `.harness/<sprint-id>/artifact/component-theater.html`.
2. For each component in the contract's state matrix:
   - Render Default, Hover, Active/Pressed, Focus (keyboard), and Disabled states
   - Add toggle buttons to activate each state for visual review
3. Record findings in `component-tests.md`:
   - Per-component pass/fail with evidence
   - Any missing state
   - Any visual inconsistency between components
   - Overall verdict: `COMPONENTS_VALID` | `COMPONENTS_NEEDS_ADJUSTMENT`

### Level 3: Page Slice

**Purpose**: Test one representative section/page with real-world content stress.

**Procedure**:
1. Create `.harness/<sprint-id>/artifact/page-slice.html`.
2. Implement one representative screen or section from the contract using actual tokens and components.
3. Test with stress content:
   - Extra-long user names (`"Mohammed bin Salman Al Saud"`)
   - Emoji-rich content (🚀💎🌙)
   - Missing images (broken `src`)
   - Extreme numbers (`¥9,999,999.99`)
   - Minimum viewport (320px width)
4. Record findings in `page-slice.md`:
   - Layout behavior under stress
   - Text truncation/overflow
   - Image fallback behavior
   - Responsive behavior at extremes
   - Overall verdict: `SLICE_VALID` | `SLICE_NEEDS_ADJUSTMENT`

## Decision After Pipeline

After all three levels complete:

- **If ALL levels pass** (all verdicts are `*_VALID`): write `status.json` with `phase: "validated"`. The router will route to `design-builder` next.
- **If any level has critical findings** (any verdict is `*_NEEDS_ADJUSTMENT` with blocking issues): write `status.json` with `phase: "validating_failed"`. Escalate to human with specific findings and the affected test fixture paths.
- **If only advisory findings** (minor issues that do not block the build): write `status.json` with `phase: "validated"` but include advisory notes in each validation file for the builder to reference. Advisory findings do not block the `validated` phase.

## Required Output Files

### `.harness/<sprint-id>/token-validation.md`

```md
# Token Validation: <SPRINT-ID>

## Test Environment
- Browser:
- Device:
- Viewport:

## Color Palette
| Token name | Expected hex/oklch | Rendered value | Match? | Notes |
|---|---|---|---|---|
| ... | ... | ... | PASS / FAIL | ... |

## Dark Mode Mapping
| Light token → Dark token | Expected behavior | Rendered behavior | Match? |
|---|---|---|---|
| ... | ... | ... | PASS / FAIL |

## Type Scale
| Level | Expected font | Rendered font | Size rendering | Notes |
|---|---|---|---|---|
| ... | ... | ... | PASS / FAIL | ... |

## Spacing Rhythm
| Token | Expected (px) | Rendered | Match? |
|---|---|---|---|
| ... | ... | ... | PASS / FAIL |

## Shadows / Elevation
| Level | Expected | Rendered appearance | Match? |
|---|---|---|---|
| ... | ... | ... | PASS / FAIL |

## Border Radius
| Token | Expected | Rendered | Match? |
|---|---|---|---|
| ... | ... | ... | PASS / FAIL |

## Findings Summary
- Total checks:
- Passed:
- Failed:
- Advisory:

## Verdict
TOKENS_VALID | TOKENS_NEEDS_ADJUSTMENT

## Evidence
- Test fixture: `.harness/<sprint-id>/artifact/token-lab.html`
- Screenshots / measurements: (paths or inline descriptions)
```

### `.harness/<sprint-id>/component-tests.md`

```md
# Component Tests: <SPRINT-ID>

## Test Environment
- Browser:
- Device:

## State Matrix Coverage
| Component | Default | Hover | Active/Pressed | Focus | Disabled | All states present? |
|---|---|---|---|---|---|---|
| Button (primary) | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | YES / NO |
| Button (secondary) | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | YES / NO |
| Input field | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | YES / NO |
| Card (interactive) | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | YES / NO |
| [others] | ... | ... | ... | ... | ... | ... |

## Per-Component Findings
### Button (primary)
- Default: ...
- Hover: ...
- Active/Pressed: ...
- Focus: ...
- Disabled: ...
- Issues: ...

[repeat for each component]

## Cross-Component Consistency
- Color consistency: CONSISTENT | INCONSISTENT — [notes]
- Spacing consistency: CONSISTENT | INCONSISTENT — [notes]
- Interaction consistency: CONSISTENT | INCONSISTENT — [notes]

## Findings Summary
- Total components:
- Total states checked:
- Passed:
- Failed:
- Missing states:
- Advisory:

## Verdict
COMPONENTS_VALID | COMPONENTS_NEEDS_ADJUSTMENT

## Evidence
- Test fixture: `.harness/<sprint-id>/artifact/component-theater.html`
```

### `.harness/<sprint-id>/page-slice.md`

```md
# Page Slice Validation: <SPRINT-ID>

## Test Environment
- Browser:
- Device:
- Viewports tested:

## Section Implemented
- Screen / section name: (from contract.md)
- Tokens used: ...
- Components used: ...

## Stress Content Results
| Stress case | Expected behavior | Observed behavior | Status |
|---|---|---|---|
| Long names | Text truncates or wraps gracefully | ... | PASS / FAIL |
| Emoji content | Renders without breaking layout | ... | PASS / FAIL |
| Missing images | Fallback placeholder displayed | ... | PASS / FAIL |
| Extreme numbers | Renders without overflow | ... | PASS / FAIL |
| 320px viewport | Content is usable, no horizontal scroll | ... | PASS / FAIL |

## Layout Behavior
- Container overflow: NONE | PRESENT — [details]
- Text truncation: HANDLED | UNHANDLED — [details]
- Image fallback: PRESENT | MISSING — [details]
- Responsive breakpoints: CORRECT | INCORRECT — [details]

## Findings Summary
- Total stress checks:
- Passed:
- Failed:
- Advisory:

## Verdict
SLICE_VALID | SLICE_NEEDS_ADJUSTMENT

## Evidence
- Test fixture: `.harness/<sprint-id>/artifact/page-slice.html`
```

### `.harness/<sprint-id>/status.json`

```json
{
  "sprint_id": "<sprint-id>",
  "phase": "validated | validating_failed",
  "owner_role": "orchestrator",
  "resume_from": "token-validation.md",
  "last_verified_step": "design-prototype-lab completed",
  "last_updated_at": "<ISO timestamp>"
}
```

For `validating_failed`, add:
```json
{
  "escalation_reason": "<summary of critical findings>",
  "affected_fixtures": [
    ".harness/<sprint-id>/artifact/token-lab.html",
    ".harness/<sprint-id>/artifact/component-theater.html",
    ".harness/<sprint-id>/artifact/page-slice.html"
  ]
}
```

## Quality Bar

- All three HTML test fixtures open in a browser with zero console errors.
- Dark mode toggle works in `token-lab.html` — toggling switches the color scheme and all tokens update accordingly.
- Stress content in `page-slice.html` is realistic, not fabricated — use the exact long-name and emoji examples specified above.
- Record evidence, not opinions — screenshot, measure, or copy-paste actual rendered values. Do not describe from memory.
- Every finding must cite a specific observed value or behavior, not a vague impression.

## Stop Conditions

Do not proceed beyond the current level and set `phase: "validating_failed"` when:
- A token renders in a color that differs from the expected hex/oklch value by a visible margin
- A font in the type scale fails to load or renders in a fallback font
- A component is missing any of the five required states (default, hover, active/pressed, focus, disabled)
- The page slice breaks layout at 320px viewport width
- Any test fixture produces a console error when opened in a browser

## Final Checklist

- [ ] Entry checks passed: `contract.md` has `prototyping_required: true`, `context.md` has token inventory, `phase: "contracted"`
- [ ] `token-lab.html` created and opens with zero console errors
- [ ] Dark mode toggle functional in `token-lab.html`
- [ ] `token-validation.md` written with per-token pass/fail evidence and overall verdict
- [ ] `component-theater.html` created with all five states for every contracted component
- [ ] `component-tests.md` written with per-component pass/fail evidence and overall verdict
- [ ] `page-slice.html` created with stress content covering long names, emoji, broken images, extreme numbers, and 320px viewport
- [ ] `page-slice.md` written with per-stress-case pass/fail evidence and overall verdict
- [ ] Decision executed: all three verdicts are `*_VALID` → `phase: "validated"`; any critical failure → `phase: "validating_failed"` with escalation reason
- [ ] `status.json` updated with correct phase and `last_updated_at` timestamp
- [ ] All findings cite evidence — observed values, measurements, or screenshots, not memory
