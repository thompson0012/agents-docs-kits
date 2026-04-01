---
name: compound
description: Use when the main need is structured extraction of reusable lessons, durable truths, or historical context from completed work — rehydrating from live docs, session history, and reference archives, then writing distilled knowledge back to docs/reference/lessons.md and docs/reference/memory.md.
---

# Compound — Structured Knowledge Extraction

Use this skill after meaningful work completes to extract durable knowledge from what happened and write it into the project's long-term reference archives.

This skill does not implement features, run browser QA, or design orchestration. It reads what happened, distills what matters, and updates the two durable archives so future sessions start smarter.

## Boundary

Use this skill when:
- a feature, phase, or delivery cycle has completed and the team wants to capture lessons before context is lost
- a harness-design postflight hands off to compound extraction
- a session produced surprising outcomes, failed approaches, hard-won fixes, or policy decisions that should survive compaction
- the user explicitly asks to update durable memory or extract lessons from recent work

Do not use this skill when:
- the work is still in progress and the need is orchestration or implementation — use `harness-design` or the relevant implementation skill
- the need is browser-facing acceptance — use `frontend-evaluator`
- the request is generic note-taking, status reporting, or progress journaling — that belongs in `docs/live/progress.md`, not here
- the user wants a PRD, architecture doc, or design spec — those are product artifacts, not extracted knowledge

## Core Contract

- **Read before writing.** Rehydrate from these sources in order before extracting anything:
  1. `docs/live/current-focus.md` — what was the objective?
  2. `docs/live/progress.md` — what actually happened, what was verified, what failed?
  3. `docs/live/qa.md` — evaluator verdicts and defect evidence, when present
  4. `docs/live/runtime.md` — execution mode and baton history, when present
  5. `docs/reference/lessons.md` — existing lessons to avoid duplication
  6. `docs/reference/memory.md` — existing durable truths to avoid duplication
  7. Session history or conversation context — raw material for extraction
- **Two archives, two purposes.** Write to exactly the right file:
  - `docs/reference/lessons.md` — reusable mistake patterns, anti-patterns, failed approaches, migration regrets, hard-won fixes, and debugging insights. Each entry answers: *what went wrong, why, and what to do instead.*
  - `docs/reference/memory.md` — durable decisions, policies, defaults, truths, and conventions that should persist beyond the current session. Each entry answers: *what was decided, why, and when it applies.*
- **Extract, do not transcribe.** A lesson is not a session log entry. Distill the transferable insight — the pattern another session can act on without reading the history that produced it.
- **Deduplicate against existing entries.** If an existing lesson or memory entry already covers the insight, strengthen or update it rather than adding a near-duplicate.
- **Preserve attribution.** When a lesson comes from a specific failure or decision, note enough context (feature, phase, date) that a reader can trace the origin without re-reading the full history.
- **Stay append-friendly.** Add entries to the existing structure in each file. Do not reorganize, re-sort, or rewrite unrelated entries.
- **No implementation side-effects.** This skill reads code and docs for evidence but does not change product code, test files, configuration, or live-doc state. Its only write targets are `docs/reference/lessons.md` and `docs/reference/memory.md`.

## Input Sources

The skill expects at least one of these to contain meaningful recent work:
- Live docs (`docs/live/*`) with current-session state
- Session conversation history with observable outcomes
- A harness-design postflight handoff naming what to extract

If none of these contain extractable material, say so and exit. Do not invent lessons from speculation.

## Extraction Categories

When scanning completed work, look for entries in these categories:

### For `docs/reference/lessons.md`
- **Failed approaches** — things tried that did not work, with the reason
- **Debugging insights** — non-obvious root causes, misleading symptoms, or diagnostic techniques
- **Migration regrets** — patterns that seemed right but created downstream cost
- **Anti-patterns** — recurring mistakes observed across sessions or features
- **Hard-won fixes** — solutions that required significant investigation to discover

### For `docs/reference/memory.md`
- **Policy decisions** — explicit choices about how the project operates (naming, packaging, routing, defaults)
- **Architectural truths** — invariants, boundaries, or component relationships discovered or confirmed
- **Convention locks** — patterns the team committed to that future work must follow
- **Tool/dependency decisions** — choices about libraries, services, or infrastructure with rationale

## Output Shape

Return a summary of what was extracted:
1. **Sources consulted** — which docs and history were read
2. **Lessons extracted** — count and brief titles of entries added to `docs/reference/lessons.md`
3. **Memory entries extracted** — count and brief titles of entries added to `docs/reference/memory.md`
4. **Skipped** — insights considered but not written, with reason (already covered, too speculative, not transferable)
5. **No extraction needed** — if the completed work produced no durable knowledge worth archiving, state that explicitly

## Failure Modes to Avoid

- Turning this into a session log or progress dump — extraction means distillation, not transcription.
- Writing vague lessons like "be more careful" or "test earlier" — every entry must be specific enough that a reader can act on it without context.
- Duplicating existing entries instead of strengthening them.
- Extracting from speculation or intent rather than observable outcomes.
- Modifying product code, tests, live docs, or any file outside the two reference archives.
- Running as a background process during implementation — compound extraction happens after work completes, not during.
