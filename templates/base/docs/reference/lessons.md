# Lessons

Read after mistakes, rework, or surprises. Capture only reusable lessons.

## Mistakes

- What happened:
- Why it happened:

## Anti-Patterns

- Pattern to avoid:
- Better default:

## Fixes

- Fix:
- When to apply:
- Evidence:

- Fix: write router and skill edits under `templates/base/`, not the user-home copy, and remove any accidental repo-root `.agents/` duplicate before verifying.
- When to apply: whenever scaffolding or copying skill packages in this repository.
- Evidence: this task initially wrote to the wrong location and left a duplicate tree until the repo-root copy was deleted.
