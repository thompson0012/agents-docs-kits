# Durable Records

Use this folder for durable feature or decision pages created by an explicit agents-stack phase for a tracked feature when the material should survive chat loss but is not the active contract, not immutable archive evidence, and not stable project-wide reference truth. Do not use it as a raw chat dump or ad hoc inline persistence step.

## What belongs here
- feature-local decision notes, investigation summaries, tradeoff writeups, or handoff context that remain useful after the sprint
- sprint or discussion output that needs durable traceability but is too situational for `docs/reference/*` and too interpreted for `docs/archive/*`
- pages tied to a tracked workstream id and registered from that feature entry through `record_paths`

## What does not belong here
- active sprint contracts, proposals, runtime logs, reviews, or status files
- copied archive evidence from `.harness/<WORKSTREAM-ID>/` or `docs/archive/<WORKSTREAM-ID>_<timestamp>/`
- current project-wide truth that belongs in `docs/reference/*`
- untracked ideas; keep those in `docs/live/ideas.md` until a workstream id exists

## Page metadata and backlinks
At the top of each record, include:
- `workstream_id`: owning tracked workstream, when one exists
- `scope`: what question, slice, or discussion window this page covers
- `status`: current validity such as `informative`, `promoted`, `superseded`, or `expired`
- `superseded_by`: replacement record or reference path, if any
- `idea_ref`: originating idea section or durable discussion pointer, if any
- `evidence_path`: one canonical evidence path for the current supporting sprint evidence
- `reference_paths`: stable reference pages that absorbed durable truth from this record
- `sprint_contributions`: sprint folders or workstream ids that materially informed the page
- `archive_contributions`: archive folders that preserve cited PASS evidence

Backlink rules:
- register the page path under the owning feature entry `record_paths`
- link back to the current `evidence_path` for the supporting sprint
- when content becomes stable current truth, promote that truth into `docs/reference/*`, update `reference_paths`, and leave this record as provenance
- when content is replaced or no longer valid, update `status` and `superseded_by` instead of deleting history
