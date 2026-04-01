# Roadmap

Canonical carrier for phased-work goal lineage. Read after `current-focus.md` to understand where the current objective came from, what phases deliver it, and how to resume after compaction.

## Source Goal

- Source goal: Harden the agents-docs-kits documentation surfaces so each surface owns exactly one job, with no overlapping authority, no obsolete references, and no placeholder content.
- Origin: recurring drift between README/AGENTS onboarding, stale family names in active surfaces, live-doc conflicts (progress vs. todo), and scaffold-only reference docs.

## Plan Goal

- Plan goal: Execute a single-batch cutover that splits human onboarding (README) from agent contract (AGENTS), aligns live docs, replaces reference placeholders, and deduplicates router prose — then verify coherence across all five surfaces.

## Phase Ledger

| Phase | Description | Status |
| --- | --- | --- |
| 1 | Live-doc alignment: rewrite current-focus, progress, todo; create roadmap | Completed |
| 2 | Onboarding split: rewrite README (human-first) and AGENTS (agent-first), remove obsolete families | Completed |
| 3 | Reference docs: replace `docs/reference/memory.md` placeholder with real durable truths | Completed |
| 4 | Router deduplication: trim SKILL.md prose in `using-labs21-suite` and `labs21-product-suite` to not restate metadata | Completed |
| 5 | Cross-surface verification: confirm no overlap, no stale references, no contradictions | Completed |

## Goal Changes

| Date | Change | Reason |
| --- | --- | --- |
| 2026-04-01 | Initial roadmap created from docs control-plane cutover objective | Live docs lacked a lineage artifact; progress and todo were drifting |

## Resume Rules

1. Read `current-focus.md` first for the active objective and constraints.
2. Read this file to locate the current phase and confirm the source goal has not changed.
3. Read `progress.md` for session-level state: what was just done, what to do next.
4. Read `todo.md` for the actionable queue.
5. Do not rely on chat memory. All resumable state lives in these four files.
6. When a phase completes, mark it `Completed` in the ledger above and update `progress.md` and `todo.md` accordingly.
7. When the source goal changes, record the change in the Goal Changes table with a date and reason.
