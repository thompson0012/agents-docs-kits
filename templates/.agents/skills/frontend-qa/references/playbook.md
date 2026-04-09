# Playbook

## QA Inventory
Before testing, list:
- core user journeys
- visible UI claims
- risky states and transitions
- supported viewports or device classes
- edge cases likely to expose brittle behavior

Every signoff claim should map to at least one explicit check.

## Browser Posture
- Use a real browser and real user interactions.
- Prefer observing the live UI over reasoning from code.
- Keep one continuous session long enough to test realistic flows and back-navigation.
- Re-check state after every meaningful interaction instead of assuming the UI kept up.

## Functional Browser Pass
Test the critical path first, then cover obvious secondary controls.

Include:
- initial state to completed outcome
- reversible interactions where applicable
- loading, empty, success, retry, and error behavior
- navigation away and return when the flow is stateful

A functional pass is incomplete if it only proves the happy path once.

## Visual Regression Pass
Inspect the states where appearance matters, not just the default screen.

Cover:
- initial viewport
- post-interaction states
- dense or worst-case content
- smallest supported viewport
- any theme or mode that changes layout or contrast

Look for clipping, weak hierarchy, broken layering, unreadable text, unstable motion, and obviously placeholder-looking UI.

## Accessibility Pass
Check both obvious semantics and real interaction.

Cover:
- page structure, headings, and landmarks
- labels, roles, names, and status announcements
- keyboard reachability and visible focus
- contrast and reduced-motion behavior
- touch target size and mobile ergonomics

Accessibility is not a separate courtesy pass. It is part of whether the feature is usable.

## Perceived Performance and Smoothness Pass
Measure the experience users feel, not only raw timing numbers.

Cover:
- initial load readiness
- navigation and interaction responsiveness
- loading indicator quality and skeleton accuracy
- layout stability during data arrival
- animation and transition smoothness
- back and forward behavior after state changes

A fast but jumpy or disorienting UI still fails this pass.

## Responsive and Cross-Device Pass
Check the layout the user actually starts in, then push smaller and touch-oriented conditions.

Cover:
- essential controls visible in the initial mobile viewport
- no horizontal overflow or obscured actions
- text wrapping under long labels and real data
- touch interaction, scrolling, and keyboard overlap where relevant
- at least one small-screen pass and one comfortable desktop pass

If the product is mobile-critical, add a device-faithful pass instead of relying on desktop resize alone.

## Adversarial Edge-Case Pass
Deliberately try to break the surface.

Stress with:
- empty, null, partial, and maximum data
- long strings, unusual Unicode, RTL, and mixed-direction text
- rapid repeated actions and double submit
- slow, partial, or failed network behavior
- resize, zoom, font scaling, and reduced-motion settings
- overlapping UI states such as modals, toasts, dropdowns, or validation messages

If the UI survives only clean data and patient clicks, it is not ready.

## Evidence Collection Rules
- Record the exact state where the issue appears.
- Capture reproduction steps, not just outcomes.
- Quote visible text exactly when reporting copy, labels, or error states.
- Use screenshots or recordings when they clarify a visual or motion claim.
- Keep notes on what remains unverified so the report does not overclaim.

## Minimum State Coverage
Before signoff, try to touch as many of these as the feature meaningfully supports:
- default
- loading
- empty
- populated
- success
- error
- partial data
- dense or maximum data
- disabled or read-only
- unauthorized or redirected state
