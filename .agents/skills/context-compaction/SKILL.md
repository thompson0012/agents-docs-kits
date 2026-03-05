---
name: context-compaction
description: Use when the conversation context is getting long, approaching token limits, switching sessions, or when asked to summarize/compact the current session state for handoff or continuation.
---

# Context Compaction

## Overview
Transform a long conversation history into a **single canonical state snapshot** that allows seamless continuation — without loss of critical instructions, decisions, or progress. The goal is maximum fidelity at minimum token cost.

## When to Use
- Context window is approaching limits
- Starting a new session to continue existing work
- Handing off to another agent or session
- User asks to "compact", "summarize session", "save state", or "create a handoff"

## Core Principles

1. **Lossless Signal Preservation** — Verbatim accuracy for critical data: file paths, IDs, variable values, constraints, agreed definitions. Never approximate.
2. **Single Canonical Representation** — If a decision evolved, record only the final state. Strip the history of changes, keep only the result.
3. **Lazy Load via Document References** — Do NOT inline full file contents. Reference paths instead: `"re-read when needed: .agents/docs/PRD.md"`. This prevents bloating the compacted context.
4. **Agents.md Instructions are Sacred** — Always extract and preserve active behavioral rules from `AGENTS.md` and session-level overrides.
5. **Objective Drift Awareness** — Record both the original objective AND the current focus objective separately if they have diverged.
6. **Style Normalization** — Strip all emotional tone, hesitation, conversational filler. Output reads like a system log.

## Required Output Format

```markdown
# 📦 Compacted Session State
**Compacted:** [ISO timestamp] | **Est. Tokens:** [count]

<preserve>
## 🏗️ Structural State
| Dimension | Value |
| :--- | :--- |
| **Original Objective** | [What the session was originally opened to do] |
| **Current Focus** | [What is actively being worked on right now] |
| **Phase** | Planning / Development / Debugging / Review / Deployment |
| **CWD** | [Absolute working directory path] |
| **Auto-Pilot** | ON / OFF |
</preserve>

<preserve>
## 📜 Active Agents.md Rules (Session-Level)
- [Any AGENTS.md protocols currently active, e.g. "AUTO-PILOT mode ON", "EMERGENCY override active"]
- [Any user-overridden behaviors explicitly set this session]
- No active overrides: [state this explicitly if none]

→ Full rules: re-read when needed: `AGENTS.md`
</preserve>

## 🧬 Knowledge Graph (Merged & De-duplicated)
- `[entity/variable]`: **[value]**
  - *Definition:* [Synthesized from across the session]
  - *Constraints:* [Hard limits]

## 🧠 Decisions (Compressed)
- **[Topic]** → **[Final Decision]**
  - *Why:* [Core reason — 1 sentence]

## 🚧 Progress & Milestones
- [x] **[Milestone]**: [Result / output data]
- [ ] **[Milestone]**: [Blocker / requirements]

## 📁 File State
| File | Status | Notes |
| :--- | :--- | :--- |
| `[path]` | Modified / Created / Pending | [Brief note] |

→ For full context on any file, re-read the file directly when needed.

## 📋 Open Tasks
- [ ] [Task 1]
- [ ] [Task 2]

## ⚠️ Critical Persistent Info
<!-- Things that MUST NOT be lost between sessions -->
- [e.g., "Invariant: all inputs sanitized before DB write"]
- [e.g., "API key in .env — never commit"]
- [e.g., "Schema: users(id, name, email, created_at)"]

## 🔁 Continue From Here
**Last action:** [Exact last thing the agent did or was doing]
**Next action:** [What must happen first upon resuming]
**Missing info:** [What is still needed from the user, if anything]
```

## Pruning Rules

| Keep | Prune |
| :--- | :--- |
| Final decisions and rationale | History of how decisions evolved |
| Current file paths and status | Old tool output logs |
| Active constraints and invariants | Repeated explanations |
| Agents.md rule overrides | Verbose earlier turns |
| Open tasks | Resolved/cancelled tasks |
| Critical config/values | Intermediate variable states |

**Focus window:** Summarize first 70% at high level. Preserve detail for the most recent 20-30% of the session.

## Lazy Load Pattern

Instead of inlining document content, reference it:

```markdown
→ Re-read when needed: `.agents/docs/PRD.md`
→ Re-read when needed: `.agents/docs/TECH_STACK.md`
→ Re-read when needed: `.agents/docs/PROGRESS.md`
```

Only inline content that:
- Has been modified this session and not yet saved
- Is a short critical value (API key hint, invariant, schema snippet < 5 lines)
- Would be expensive to rediscover (e.g., a resolved ambiguity)

## Agents.md Preservation Rule

Extract from `AGENTS.md` and the conversation any active session-level overrides:
- AUTO-PILOT ON/OFF status
- EMERGENCY override (log reason)
- Any user-stated behavioral changes ("for this session, skip approval for X")

If none: explicitly state `"No active AGENTS.md session overrides."` — never leave this blank.

## Common Mistakes

| Mistake | Fix |
| :--- | :--- |
| Inlining entire files | Use lazy-load references instead |
| Recording decision history | Keep only the final state |
| Vague milestone entries | Include concrete output/result data |
| Omitting original objective | Always record both original + current focus |
| Leaving Agents.md section blank | Explicitly state "no active overrides" |
| Approximating numbers/paths | Copy verbatim or omit entirely |

## Rationalization Table

| Excuse | Reality |
| :--- | :--- |
| "The history is short, no need to compact" | If context is long enough to cause concern, compact it |
| "I'll just summarize loosely" | Loose summaries lose critical constraints — use the format |
| "Agents.md rules are obvious, skip" | Rules must be explicit; next session can't infer session overrides |
| "File contents are important, include them" | Reference paths; inline only if modified and unsaved |

## Red Flags — STOP and Fix

- Compacted output is longer than 30% of original — prune harder
- File contents inlined instead of referenced
- Original objective missing (only current focus recorded)
- Agents.md section absent or blank
- Decision history included instead of final decision only
