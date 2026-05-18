# Reporting

## Severity Levels

### Blocker
Release-stopping failure in a core journey or safety-critical expectation.

Examples:
- Critical flow cannot complete (e.g., checkout, login, form submission)
- User data is lost or corrupted from normal interaction
- The UI becomes unusable on a required device or accessibility path
- Security vulnerability exposed through the UI (XSS, data leak)
- Entire page crashes (white screen, uncaught error)

### Major
High-impact failure with a real user cost, but not total release stop by itself.

Examples:
- Confusing or misleading state in a primary workflow
- Responsive breakage that hides important controls on mobile
- Severe accessibility regression with no workaround (missing labels, broken keyboard nav)
- Significant visual regression — brand colors wrong, layout broken
- Animation jank or layout shift that disrupts reading

### Minor
Real defect with limited blast radius or low urgency.

Examples:
- Non-critical visual inconsistency (1px spacing deviation where functional)
- Secondary-state polish issue (hover state slightly off in rarely-used component)
- Copy or spacing problem that does not block comprehension
- Missing advisory best practice (e.g., 80/20 rule not followed)

## Finding Format

For every finding, use this template:

```markdown
### [FINDING-ID] | Severity: Blocker | Major | Minor
**Title:** [Short statement of what failed]
**Layer:** [Visual | Interaction | Design System | Accessibility | Responsive | Content | Performance]
**Area:** [Route, screen, or component]
**Environment:** [Browser, viewport, device, OS theme, relevant settings]
**Steps to Reproduce:**
1. ...
2. ...
3. ...
**Observed:** [What actually happened — quote text, describe visuals precisely]
**Expected:** [What should have happened per design spec or contract]
**Evidence:** [Screenshot, recording, quoted UI text, metric value, DevTools measurement]
**Notes:** [Scope, likely owner, conditions, workarounds]
```

## Concise Bug Report Template

Use this shape for quick reporting:

```md
Severity: Blocker | Major | Minor
Layer: Visual | Interaction | Design System | Accessibility | Responsive | Content | Performance
Title: <short statement of failure>
Area: <route, screen, or feature>
Environment: <browser, viewport, device, theme, relevant settings>
Steps:
1. ...
2. ...
3. ...
Observed: <what actually happened>
Expected: <what should have happened>
Evidence: <screenshot, recording, quoted UI text, metric>
Notes: <scope, likely owner, or conditions>
```

## What NOT to Count as a Pass

Do not call the feature passed because:
- The code looks correct — code is not behavior
- One happy-path run succeeded once — most failures live in non-happy-path states
- The DOM contains the expected element even though the experience is confusing or broken
- A screenshot looks fine without reproducing the interactive state
- The issue only happens on small screens, slow conditions, keyboard use, or malformed content — these are first-class states, not edge cases
- You did not verify a claim but assumed it from nearby behavior
- The design system library "should handle it" — verify the actual rendered output

## Reporting Discipline

- Report what was tested, what failed, and what remains unverified.
- Keep evidence attached to the state where the claim matters.
- Separate confirmed defects from open questions.
- Do not soften severity because a workaround exists unless the workaround is realistic for the typical user.
- Flag findings that are product gaps vs. design problems vs. frontend bugs vs. backend dependencies — different owners, different fix paths.

## Signoff Statement Template

```md
## Signoff: [Feature/Page Name]

### QA Coverage
- Layers executed: [list layers 1-7]
- Viewports tested: [list]
- Browsers tested: [list]
- Devices tested: [list]
- Total criteria checked: [N]
- Total findings: [N] (Blocker: X, Major: Y, Minor: Z)

### Utility Assessment
- [ ] Core job can be completed
- [ ] Core action is obvious
- [ ] All states support the real workflow
- Assessment: PASS | FAIL — [reason]

### Usability Assessment
- [ ] Controls are self-explanatory
- [ ] Keyboard, focus, touch interaction is coherent
- [ ] Interface is stable under loading, navigation, error, backtracking
- [ ] Accessibility gaps: [none | list]
- Assessment: PASS | FAIL — [reason]

### Craft Assessment
- [ ] Visual hierarchy is clear at first glance
- [ ] Spacing, motion, copy feel deliberate
- [ ] Edge states look designed
- [ ] Brand temperament matches expectations
- [ ] One intentional design "break" present (or documented as not needed)
- Assessment: PASS | FAIL — [reason]

### Overall Signoff
- [ ] APPROVED — ready for release
- [ ] CONDITIONAL — approved with documented known issues (list)
- [ ] REJECTED — blocking findings must be resolved (list)

### Unverified Gaps
- [list any area or state not tested and why]
```

## Finding ID Convention

Use sequential IDs prefixed by layer:
- `VIS-001` — Visual layer finding
- `INT-001` — Interaction layer finding
- `DSY-001` — Design System layer finding
- `A11-001` — Accessibility layer finding
- `RES-001` — Responsive layer finding
- `CON-001` — Content layer finding
- `PER-001` — Performance layer finding
