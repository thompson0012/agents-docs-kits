# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Resume Task 35: refine the capability-based methodology overlays in the finance, research, and webapp docs now that Task 39's harness-control and frontend-evaluator rollout is complete.

## Scope

In Scope:
- Tighten the finance, research, and webapp docs so capability overlays stay honest, portable, and easy to route.
- Preserve the Task 39 delivery-control boundaries already landed in `software-delivery`, `website-building`, and the template live-doc surface.
- Use the Task 39 reference docs as baseline continuity, not as a signal to reopen that work.

Explicitly Out of Scope:
- Reworking the shipped `software-delivery` router or its new `harness-design` / `frontend-evaluator` leaves unless a concrete blocker appears.
- Adding unrelated router families or new follow-on work outside the existing queue.
- Reopening validation-only work without an observed blocker.

## Constraints

- Treat Task 39 as complete; only revisit it if a concrete regression or unresolved validator failure appears.
- Keep `website-building` as the builder-side browser QA lane, with `software-delivery/frontend-evaluator` as the independent follow-on gate for non-trivial browser-facing signoff.
- Keep `templates/base/docs/live/runtime.md` and `templates/base/docs/live/qa.md` as optional live docs used only when explicit delivery control or independent evaluation is in play.

## Success Criteria

- Task 35 docs clearly explain capability-based overlays for finance, research, and webapp work.
- Task 39 boundaries remain coherent in the continuity and reference docs.
- If no blocker surfaces, the next handoff still points to Task 35.