# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Apply the repo-doc control-plane cutover so each documentation surface owns exactly one job:

| Surface | Single responsibility |
| --- | --- |
| `README.md` | Human onboarding — what the repo is, how to get started |
| `AGENTS.md` | Agent operating contract — rules, procedures, verification |
| `docs/live/` | Live state — focus, progress, todo, roadmap |
| `docs/reference/` | Durable truth — architecture, memory, codemap |
| `templates/base/.agents/skills/` | Routing truth — single-sourced in metadata, not prose |

Why now: README and AGENTS currently overlap on onboarding content, active surfaces still reference removed family names, live docs drift from each other, reference docs contain placeholder scaffold, and router skills duplicate policy in both SKILL.md prose and metadata files.

## Scope

In scope:
- Split README (human) from AGENTS (agent) with no overlapping authority.
- Remove obsolete family references from active onboarding and router surfaces.
- Add `roadmap.md` as the canonical phased-work lineage artifact.
- Align `progress.md` and `todo.md` so they do not contradict each other or `current-focus.md`.
- Replace `docs/reference/memory.md` placeholder with real durable truths and freshness metadata.
- Deduplicate router SKILL.md prose that restates metadata already in `router-metadata.md` or `children.json`.

Out of scope:
- Reopening capability-overlay work unless this change exposes a regression.
- Modifying product code, template generation logic, or validator scripts.
- Adding new router families or product-specific implementation work.

## Constraints

- One concept, one representation — no compatibility shims, no duplicate authorities.
- Live docs must be self-contained: an agent resumes from these files, not chat memory.
- Template live docs remain neutral scaffolds with no seeded prose.

## Success Criteria

- Each of the five surfaces listed above owns one job with no overlap.
- No obsolete family references remain in active onboarding or router surfaces.
- `todo.md` and `progress.md` are coherent with this focus and with each other.
- `roadmap.md` preserves goal lineage across phase execution and resume.
- `docs/reference/memory.md` contains real content, not placeholder scaffold.
