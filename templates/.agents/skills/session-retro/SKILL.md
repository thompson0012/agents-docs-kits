---
name: session-retro
description: Use when a session is ending — audits the session against agentic-engineering principles, extracts patterns and insights with causal power over future decisions, writes them to the persistent insights log. Trigger via /retro or auto-propose on closure signals.
version: 0.1.0
---

# Session Retro

Closing ritual. Run near session end. Delegates audit work to @oracle.

## Goals

Two-tier design:

| Tier | Level | Trigger | Purpose |
|------|-------|---------|---------|
| 1 | Per-session | `/retro` or end-of-session signals | Extract what from this session would change future behavior |
| 2 | Cross-session | Every 5 entries in session-log (or manual request) | Find patterns across sessions — recurring pitfalls, stable decisions, emergent principles |

Tier 1 answers: **what did this session teach us?**
Tier 2 answers: **what have the last N sessions been teaching us repeatedly that we still haven't absorbed?**

## Trigger Rules

### Manual

User types `/retro` at any time. Run immediately.

### Auto-propose

Orchestrator proposes a retro when **two or more** of these signals are present:

- Last 2+ turns were verification / validation / "done" style exchanges
- User said "好了" / "就這樣" / "沒了" / "ok" / "done" or equivalent closure phrase
- Multiple files were changed and no new work is queued
- A `verification-before-completion` pass just completed

When auto-proposing: ask "Run session retro?" — one line, no preamble. If user says yes, execute. If no, drop it.

## Output Format

Write to `.agents/insights/session-log.md`. Cumulative file — append a dated entry, do not create new files.

Each entry:

```markdown
## YYYY-MM-DD · session summary (≤8 words)

### Decisions (why, not what)
- Reason we chose A over B. Tradeoffs considered.

### Unresolved
- Known gaps, parked work, Phase 2 items. Why parked.

### Pitfalls
- Non-obvious edge cases, dependency surprises, time-wasters. Root cause.

### Patterns
- Reusable method or heuristic. How to recognize when it applies again.

### Charter violations
- Principle(s) violated, anti-pattern matched. Concrete location/decision.

### API surface
- Semantic changes to public API. What was added, deprecated, removed.
```

Omit any section with nothing to record. Never pad.

## Execution Flow

### Tier 1 — Per-session retro

1. **Orchestrator** loads this skill.
2. **Orchestrator** prepares a compact context packet for @oracle:
   - Key decisions made this session (what was debated, what was chosen)
   - Files changed (paths only, not content)
   - Notable discussion themes
   - Any known regrets or second-guesses
3. **Orchestrator** delegates to @oracle with:
    - The context packet above
    - Instruction: audit against the 16 principles in `.agents/skills/agentic-engineering-principles/references/principle-details.md` and the anti-patterns in `.agents/skills/agentic-engineering-principles/references/anti-patterns.md`
    - Instruction: apply the filtering rule — only record what would change future behavior
   - Instruction: return the six-section output, omitting empty sections
4. **@oracle** audits, returns the structured verdict.
5. **Orchestrator** appends the verdict to `.agents/insights/session-log.md`.
6. **Orchestrator** reports one-line summary to user: "Retro done. N items recorded."
7. **Orchestrator** checks entry count: if count % 5 == 0, ask user: "5 sessions recorded. Run cross-session retro to find patterns?"

### Tier 2 — Cross-session synthesis

Triggered manually (`/retro --cross`) or automatically every 5 entries.

1. **Orchestrator** reads all entries from `.agents/insights/session-log.md`.
2. **Orchestrator** delegates to @oracle with:
   - All session entries (minus any empty sections)
   - Instruction: find patterns across sessions — what decisions keep being made the same way? what pitfalls keep appearing? what principles are chronically violated?
   - Instruction: return a cross-session synthesis with:
     - **Emerging patterns** — heuristics that surfaced repeatedly across sessions
     - **Chronic violations** — principles that keep being broken and why
     - **Stable decisions** — decisions made consistently across sessions (these can now become convention)
     - **Recommended updates** — what should change in the constitution, skills, or orchestrator prompt based on accumulated evidence
3. **@oracle** returns the synthesis.
4. **Orchestrator** appends the synthesis to `.agents/insights/session-log.md` as a special `## Cross-session` entry.
5. **Orchestrator** reports to user: "Cross-session retro done. X patterns found, Y chronic violations."
6. If the synthesis identifies skill or constitution gaps, **orchestrator** suggests concrete follow-up work.

## Filtering Rule

Before writing any item, ask: **"Would a future session make a different decision if it knew this?"**

| Record | Don't record |
|--------|-------------|
| Why we chose A over B (future may face same tradeoff) | What we did (git log has it) |
| A surprising pitfall with root cause | File manifests (git diff has them) |
| A reusable method discovered | Conversation summary (context-compaction handles that) |
| A principle we violated and why | Handoff context (@agent-handoff does that) |
| Open questions with clear re-open conditions | Vague "think about this later" notes |

## Constitution Reference

This skill audits against:

- **16 principles**: `.agents/skills/agentic-engineering-principles/references/principle-details.md`
- **Anti-patterns**: `.agents/skills/agentic-engineering-principles/references/anti-patterns.md`

Refer to those files directly; do not duplicate them here.

## Failure Modes

- **Recording everything.** If every session gets an entry, the log becomes noise. Skip sessions where nothing meets the filter.
- **Vague patterns.** "Test more" is useless. "When mock returns dict not model, mypy won't catch it — validate with isinstance at boundary" is useful.
- **Oracle without context.** If the context packet is too thin, oracle invents violations. Give it the minimum it needs to audit honestly.
- **Forgetting to propose.** Orchestrator must check trigger signals before its final "done" message. The last chance is the verification phase.
- **Cross-session too early.** Running Tier 2 with only 1-2 entries has nothing to synthesize. The 5-entry threshold is a minimum; if entries are sparse, the orchestrator should skip the auto-proposal.
- **Cross-session too late.** Beyond 10 entries without a synthesis, earlier lessons are forgotten and trends ossify. The orchestrator should become more assertive about proposing after 8+ entries.
