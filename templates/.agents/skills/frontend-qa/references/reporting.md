# Reporting

## Severity Levels
### Blocker
Release-stopping failure in a core journey or safety-critical expectation.

Examples:
- critical flow cannot complete
- user data is lost or corrupted from normal interaction
- the UI becomes unusable on a required device or accessibility path

### Major
High-impact failure with a real user cost, but not total release stop by itself.

Examples:
- confusing or misleading state in a primary workflow
- responsive breakage that hides important controls
- severe accessibility, visual, or performance regression with a workaround

### Minor
Real defect with limited blast radius or low urgency.

Examples:
- non-critical visual inconsistency
- secondary-state polish issue
- copy or spacing problem that does not block comprehension

## Evidence to Capture
For every finding, capture:
- severity
- short title stating what failed
- exact reproduction steps
- affected route, screen, or component area
- viewport or device context
- visible evidence: quoted text, screenshot, recording, or measured signal
- expected behavior versus observed behavior
- whether the issue is a product gap, design problem, frontend bug, backend dependency, or unknown

## Concise Bug Report Template
Use this shape:

```md
Severity: Blocker | Major | Minor
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

## What Not to Count as a Pass
Do not call the feature passed because:
- the code looks correct
- one happy-path run succeeded once
- the DOM contains the expected element even though the experience is confusing or broken
- a screenshot looks fine without reproducing the interactive state
- the issue only happens on small screens, slow conditions, keyboard use, or malformed content
- you did not verify a claim but assumed it from nearby behavior

## Reporting Discipline
- Report what was tested, what failed, and what remains unverified.
- Keep evidence attached to the state where the claim matters.
- Separate confirmed defects from open questions.
- Do not soften severity because a workaround exists unless the workaround is realistic for the user.
