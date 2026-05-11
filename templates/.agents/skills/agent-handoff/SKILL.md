---
name: agent-handoff
description: Use when an AI agent must hand off in-progress work to a successor agent and needs a structured, high-signal payload that prevents hallucination, re-litigation of settled decisions, and duplicate work.
---

# Agent Handoff

## Overview

Agent handoff produces a structured state payload that lets a successor agent continue work without rediscovering settled context. The handoff is NOT a conversation dump. It is a compact, schema-driven payload that lists artifacts, decisions, constraints, open questions, a concrete next step, and surgical file anchors.

## Core Contract

- Produce a JSON payload following the handoff schema; every section is required.
- List concrete artifacts, not narrative descriptions of process.
- Include decision rationale to prevent the successor from re-litigating settled choices.
- Constraints must be prohibitions ("Do not X"), not advice.
- Provide a single, immediately executable next step — not a plan or list.
- Context anchors must point to specific files and line ranges, not entire directories.
- Be stingy with tokens: if a section is empty, write `[]`. Do not duplicate information already encoded in anchors.

## When to Use

Use this skill when an agent is about to transfer in-progress work to another agent, either within a team, across a handoff boundary in a multi-agent system, or when saving checkpoints for later resumption.

## When Not to Use

Do not use this skill for:
- Simple task completion summaries where the work is done (no successor needed)
- Conversation logs or chat exports that are meant for human review
- Project documentation or architecture decisions records (use project docs instead)

## Workflow

### Phase 1 — Prepare the Handoff

Before writing the payload, identify:
- What was actually completed (concrete artifacts)
- What decisions were made and why
- What must NOT be touched (constraints and non-goals)
- What single action the successor should take first

### Phase 2 — Produce the Payload

Generate a JSON payload matching the [handoff schema](references/handoff-schema.md). Every section is required. Include all fields even if empty.

### Phase 3 — Apply System-Level Filters

If the runtime supports input filters:
- Strip noisy intermediate messages (failed tool calls, retries, debugging chatter)
- Keep only the user's original prompts and the final successful assistant responses
- Pass the cleaned history alongside the structured payload

### Phase 4 — Validate

Before declaring the handoff complete, check:
- Every artifact entry names a concrete deliverable
- Every decision includes its reason
- The next step is a single, executable instruction
- Context anchors reference real files with line ranges
- Constraints are prohibitions, not vague warnings
- No narrative or meta-commentary has leaked into the payload

## References

- [Handoff Schema](references/handoff-schema.md) — Full JSON schema with field descriptions and examples

## Failure Modes

- Producing narrative ("I tried several approaches") instead of artifacts ("Created src/auth.py")
- Omitting decision reasons, forcing the successor to guess why a choice was made
- Writing vague constraints like "Be careful" instead of "Do not modify migrations/"
- Providing a multi-step plan as the next step instead of one concrete action
- Including entire file contents or full directory paths as context anchors instead of surgical line ranges
- Passing unfiltered conversation history full of failed attempts and intermediate noise

## Final Checklist

- [ ] Goal stated in 1-3 sentences
- [ ] Current state lists concrete artifacts, not process narrative
- [ ] Every decision includes rationale
- [ ] Constraints are prohibitions
- [ ] Next step is a single, immediately executable action
- [ ] Context anchors use file path + line ranges
- [ ] Empty sections use `[]`, not placeholder text
- [ ] No meta-commentary or apology in payload
- [ ] Conversation history filters applied (when runtime supports it)
