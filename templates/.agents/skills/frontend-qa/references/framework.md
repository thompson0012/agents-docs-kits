# Framework

Frontend QA uses one signoff lens: Utility × Usability × Craft. A screen is not truly ready if any one factor is missing.

## Utility
Utility asks whether the surface solves the user's actual job.

Questions to ask:
- Is the core action obvious?
- Can the user reach the outcome without extra ceremony?
- Do the visible states support the real workflow, including empty, loading, and recovery?

Failure when missing:
- The feature works but does not help.
- The important action is buried behind noise, dead ends, or unnecessary steps.
- The team ships a technically valid screen that still misses the user problem.

## Usability
Usability asks whether a normal user can understand and complete the job without friction.

Questions to ask:
- Are controls, labels, and next steps self-explanatory?
- Does keyboard, focus, and touch interaction stay coherent?
- Does the interface remain stable under slow loading, navigation, error, and backtracking?

Failure when missing:
- Users hesitate, misclick, or need instructions for obvious tasks.
- The UI technically responds but feels slow, unstable, or confusing.
- Accessibility gaps block or degrade completion.

## Craft
Craft asks whether the surface feels intentional, trustworthy, and cared for.

Questions to ask:
- Is hierarchy clear at first glance?
- Do spacing, motion, copy, and states feel deliberate rather than default?
- Do edge states look designed, not forgotten?

Failure when missing:
- The product feels generic, brittle, or unfinished.
- Visual noise, weak hierarchy, clipping, or awkward motion reduce trust.
- Error, empty, loading, and disabled states expose the seams of the implementation.

## How the Lens Changes Signoff
The lens changes QA from “did anything break?” to “is this honestly ready for users?”

Signoff guidance:
- Missing Utility is a signoff failure even if the UI is visually polished.
- Missing Usability is a signoff failure even if the feature technically exists.
- Missing Craft may still block signoff when trust, clarity, readability, or perceived quality materially degrade the experience.
- A pass means the surface is useful, understandable, and intentional in the browser states that matter.

## Practical Rule
Do not average the three dimensions together. One strong dimension does not cancel out a weak one.