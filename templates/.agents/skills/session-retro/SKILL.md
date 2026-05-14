---
name: session-retro
description: Use when a session is ending — audits the session against agentic-engineering principles, extracts patterns and insights with causal power over future decisions, writes them to the persistent insights log. Trigger via /retro or auto-propose on closure signals.
version: 0.1.0
---

# Session Retro

Closing ritual. Run near session end. Delegates audit work to @oracle.

## Goal

Answer one question across this session: **what did we learn that should change how we work tomorrow?**

If the answer is nothing, record nothing. The retro is not a summary — it's a filter. Only keep what has causal power over future decisions.

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

1. **Orchestrator** loads this skill.
2. **Orchestrator** prepares a compact context packet for @oracle:
   - Key decisions made this session (what was debated, what was chosen)
   - Files changed (paths only, not content)
   - Notable discussion themes
   - Any known regrets or second-guesses
3. **Orchestrator** delegates to @oracle with:
   - The context packet above
   - Instruction: audit against the 16 principles in `agentic-engineering-principles/references/principle-details.md` and the anti-patterns in `references/anti-patterns.md`
   - Instruction: apply the filtering rule — only record what would change future behavior
   - Instruction: return the six-section output above, omitting empty sections
4. **@oracle** audits, returns the structured verdict.
5. **Orchestrator** appends the verdict to `.agents/insights/session-log.md`.
6. **Orchestrator** reports one-line summary to user: "Retro done. N items recorded."

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

- **16 principles**: `agentic-engineering-principles/references/principle-details.md`
- **Anti-patterns**: `agentic-engineering-principles/references/anti-patterns.md`

Refer to those files directly; do not duplicate them here.

## Failure Modes

- **Recording everything.** If every session gets an entry, the log becomes noise. Skip sessions where nothing meets the filter.
- **Vague patterns.** "Test more" is useless. "When mock returns dict not model, mypy won't catch it — validate with isinstance at boundary" is useful.
- **Oracle without context.** If the context packet is too thin, oracle invents violations. Give it the minimum it needs to audit honestly.
- **Forgetting to propose.** Orchestrator must check trigger signals before its final "done" message. The last chance is the verification phase.
