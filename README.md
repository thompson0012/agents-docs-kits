# Project AI Coding Agents Setup

This repository contains a **battle-tested configuration** for using AI coding agents (especially Claude Code / Claude 3.5 / Claude 4 / Cursor / Windsurf / Aider / etc.) to build and maintain production-grade software with high reliability, consistency, and safety.

The heart of this setup is two central files:

- **`AGENTS.md`** — the **operating system / constitution** of the AI coding agent  
- **`GUIDELINES.md`** — the **documentation style guide** that teaches the agent how to write and maintain all other project documents

Together, they turn a general-purpose LLM into a disciplined, self-correcting, context-aware senior engineer that follows strict rules, preserves existing code style, avoids regressions, and continuously improves.

## Core Files

### AGENTS.md

**Purpose**  
This is the **single source of truth** for how the AI agent should behave during every coding session.

It defines:

- Role & mindset (executor, not architect)
- Mandatory session startup ritual (reading key documents)
- Strict approval gates before writing any code
- Protection rules (no regressions, no hallucinations, no unsolicited refactors)
- Security & prompt-injection defenses
- Coding standards (match existing codebase first!)
- Testing & bug-fixing rituals (test-first bug reproduction)
- Self-improvement loop (every correction → new permanent rule)
- Communication format & completion checklist

**Key philosophy**  
> You are the hands. The user is the architect.  
> Documentation is law.  
> Safety & correctness over speed.  
> Every mistake becomes a permanent rule.

### GUIDELINES.md

**Purpose**  
This file teaches the agent **exactly how to write, structure, and update every other documentation file** in the project.

It covers precise formats and rules for:

- PRD.md / PRODUCT.md
- IMPLEMENTATION_PLAN.md
- LESSONS.md (learned lessons & anti-patterns)
- progress.txt
- TECH_STACK.md
- DESIGN_SYSTEM.md
- APP_FLOW.md
- FRONTEND_GUIDELINES.md / BACKEND_STRUCTURE.md
- MEMORY.md (long-term architectural decisions)
- tasks/todo.md

**Key philosophy**  
> Documentation must be concise, scannable, consistent, and version-controlled.  
> The agent is not allowed to invent structure — it must follow these exact templates.

## How They Work Together

1. At the start of **every session**, the agent is instructed (in `AGENTS.md`) to read:
   - `AGENTS.md` (behavior rules)
   - `GUIDELINES.md` (how to write docs)
   - All other tracked documents (`progress.txt`, `LESSONS.md`, `IMPLEMENTATION_PLAN.md`, etc.)

2. When the agent needs to **create or update any document**, it must follow the **exact structure and rules** defined in `GUIDELINES.md`.

3. When the user **corrects** the agent (wrong pattern, hallucination, bad decision, etc.), the agent:
   - Proposes a new precise rule
   - Suggests where to add it (usually in `AGENTS.md`)
   - Waits for approval before updating

This creates a **self-hardening system** that gets better and more aligned with your project over time.

## Sources & Experts This Setup Draws From

This configuration is **not** invented from scratch. It is a **heavily synthesized and battle-hardened** version based on real-world patterns shared by top practitioners and teams in 2024–2026.

**Primary influences & experts:**

- **Boris Cherny** (@bcherny) — Claude Code engineer at Anthropic  
  → Ruthless iteration after every mistake, session startup reading order, self-improvement loop

- **Omar Sar0** (@omarsar0) — AI engineering patterns, structured prompting, agent memory systems

- **Kloss** (@kloss_xyz) — Multi-file context management, protection rules, approval gates

- **Anthropic Claude Code community** (especially shared `CLAUDE.md` templates on GitHub & X)

- **Simon Willison** & **Cursor / Aider** power users  
  → Emphasis on test-first bug fixing, progress.txt style state tracking

- **Various high-signal GitHub repos** (especially Claude + Cursor + Windsurf setups with 100+ stars)

- **Public X threads** (2025–2026) on agent reliability, security hardening, prompt injection defense, and parallel sub-agents

Special thanks to the many developers who openly shared their `CLAUDE.md` / `AGENTS.md` files and correction rituals — this is a collective distillation of what actually works in production.

## How to Use This Setup

1. Place `AGENTS.md` and `GUIDELINES.md` in your project root (or `/docs/`)
2. In your AI coding tool (Claude Code, Cursor, Aider, etc.):
   - Set `AGENTS.md` as the **project instruction file** / **custom system prompt** / **memory file**
   - Or use `@AGENTS.md` in prompts
3. Let the agent read both files at the start of every session
4. **Correct ruthlessly** — every mistake is a chance to make the agent permanently better
5. Commit changes to `AGENTS.md`, `GUIDELINES.md`, `LESSONS.md`, etc. — treat them like code

## Philosophy in One Sentence

> Turn the AI from a helpful assistant into a disciplined, self-correcting senior engineer that follows your rules forever.

Happy coding — and happy hardening!

<!-- 
Last updated: February 2026
-->
