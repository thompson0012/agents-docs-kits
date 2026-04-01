# Progress

Read after `current-focus.md` to recover the latest state and hand-off details. Keep each section concise.

## Current State

All implementation phases are complete. The live-doc, onboarding, reference, and router surfaces now share one authority per concern.

See `roadmap.md` for the full phase ledger and goal lineage.

## Latest Completed Work

- Rewrote `current-focus.md` to reflect the docs control-plane cutover objective.
- Created `roadmap.md` as the canonical phased-work lineage artifact.
- Rewrote `progress.md` (this file) as a concise session ledger.
- Rewrote `todo.md` as a short current-actions queue aligned with this focus.
- Rewrote `README.md` and `AGENTS.md` to split human onboarding from the agent contract.
- Rewrote `docs/reference/{codemap,architecture,memory}.md` to make the reference surfaces task-first and honest.
- Simplified router metadata in `templates/base/.agents/skills/{using-labs21-suite,labs21-product-suite}/...` so prose no longer duplicates policy.
- Prior to this session:
  - Rebuilt `labs21-product-suite` into canonical router-package shape with bundled assets.
  - Refreshed `using-labs21-suite` to include `using-design`, `using-reasoning`; removed deleted family references.
  - Drafted harness goal-lineage hardening plan at `docs/superpowers/plans/2026-03-27-harness-goal-lineage-hardening.md`.

## Blockers

None.

## Touched Files

- `docs/live/{current-focus,progress,todo,roadmap}.md`
- `README.md`
- `AGENTS.md`
- `docs/reference/{codemap,architecture,memory}.md`
- `templates/base/.agents/skills/{using-labs21-suite,labs21-product-suite}/...`

## Verification

- `git diff --check` passed.
- Confirmed `todo.md` no longer conflicts with `current-focus.md`.
- Confirmed `roadmap.md` preserves source goal and resume rules.
- Confirmed README/AGENTS no longer duplicate the same onboarding contract.

## Next Recommended Action

- None; reopen only if new drift or a regression appears.
