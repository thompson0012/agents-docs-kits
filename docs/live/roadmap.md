# Roadmap

Canonical carrier for phased-work goal lineage. Read after `current-focus.md` to understand where the current objective came from, what phases deliver it, and how to resume after compaction.

## Source Goal

- Source goal: The delivery-control family in `templates/base/` should carry the strongest portable lifecycle patterns from gstack (browser QA, evidence-gated acceptance), Superpowers (session orchestration, plan execution, verification-before-completion), and Compound Engineering (durable archives, goal lineage, session compaction) so every generated repo ships a delivery-control surface that enforces honest multi-session execution.
- Origin: The template-cutover batch aligned scaffolds and naming, but the delivery-control family itself still needed the deeper portable patterns those source systems proved.

## Plan Goal

- Plan goal: Absorb the strongest portable patterns from gstack, Superpowers, and Compound Engineering into the `templates/base/` delivery-control family — upgrading its router, children, live/reference scaffolds, suite-index guidance, and website-building follow-on guidance — without adding product-specific content, compatibility shims, or duplicate authorities.

## Phase Ledger

| Phase | Description | Status |
| --- | --- | --- |
| 0 | Recast root live docs to describe the delivery-control upgrade objective | Completed |
| 1 | Audit gstack, Superpowers, and Compound Engineering for portable delivery-control patterns | Completed |
| 2 | Integrate selected patterns into `delivery-control` router and children | Completed |
| 3 | Update live-doc and reference scaffolds if delivery-control changes require it | Completed |
| 4 | Update suite router / category map and website-building follow-on guidance so delivery-control's new lanes are discoverable | Completed |
| 5 | Cross-surface verification: no overlap, stale references, or contradictions | Completed |

## Goal Changes

| Date | Change | Reason |
| --- | --- | --- |
| 2026-04-01 | New batch: delivery-control upgrade replaces completed template-cutover as active objective | Template cutover is done; delivery-control family needs deeper portable patterns from gstack, Superpowers, and Compound Engineering. |
| 2026-04-01 | Prior: template-cutover batch replaced root cutover as the active objective | Root cutover was done; templates still carried the old shape. |

## Resume Rules

1. Read `current-focus.md` first for the active objective and constraints.
2. Read this file to locate the current phase and confirm the source goal has not changed.
3. Read `progress.md` for session-level state: what was just done, what to do next.
4. Read `todo.md` for the actionable queue.
5. Do not rely on chat memory. All resumable state lives in these four files.
6. When a phase completes, mark it `Completed` in the ledger above and update `progress.md` and `todo.md` accordingly.
7. When the source goal changes, record the change in the Goal Changes table with a date and reason.
