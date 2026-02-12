# Project AI Coding Agents Setup

This repository contains a **battle-tested configuration** for using AI coding agents (especially Claude Code / Claude 3.5 / Claude 4 / Cursor / Windsurf / Aider / etc.) to build and maintain production-grade software with high reliability, consistency, and safety.

> **Template Kit Notice**: This repository is a **generic template system**. Any examples in `/.agents/docs/` are **fictional** and must be replaced or removed before real use.

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
- Risk-tiered session startup (lazy reading: Low/Normal/High)
- Strict approval gates before writing any code
- Protection rules (no regressions, no hallucinations, no unsolicited refactors)
- Security & prompt-injection defenses
- Coding standards (match existing codebase first!)
- Testing & bug-fixing rituals (test-first bug reproduction)
- Self-improvement protocol (corrections become permanent rules via §6)
- Documentation evolution protocol (structured update process via §5)
- Completion checklist & escalation criteria

**Key philosophy**  
> You are the hands. The user is the architect.  
> Documentation is law.  
> Safety & correctness over speed.  
> Every mistake becomes a permanent rule.

### GUIDELINES.md

**Purpose**  
This file teaches the agent **exactly how to write, structure, and update every other documentation file** in the project.

It covers precise formats and rules for:

- PRD.md
- IMPLEMENTATION_PLAN.md
- LESSONS.md (learned lessons & anti-patterns)
- PROGRESS.md
- TECH_STACK.md
- DESIGN_SYSTEM.md
- APP_FLOW.md
- FRONTEND_GUIDELINES.md / BACKEND_STRUCTURE.md
- MEMORY.md (long-term architectural decisions)
- TASKS.md

**Key philosophy**  
> Documentation must be concise, scannable, consistent, and version-controlled.  
> The agent is not allowed to invent structure — it must follow these exact templates.

## How They Work Together

- `AGENTS.md` is the constitution (highest priority rules).
- `/.agents/docs/*` are supporting guides and project docs used as needed.
- `/.agents/docs/PROGRESS.md` carries session state forward.
- Each doc starts with a **STATUS** header (TEMPLATE / PRODUCTION / EXAMPLES-ONLY).
- Template-to-Production: after user feedback + clarified goals, the agent updates AGENTS.md + docs via the Documentation Evolution Protocol.
- If you want durable, linkable plan/task records across sessions, see `/.agents/docs/PLANS.md`.

## AI Agent Behavior Summary (when coding in this repo)
- Always read `AGENTS.md` + `/.agents/docs/PROGRESS.md` first.
- Respect STATUS headers; only trust `STATUS: PRODUCTION` docs as authoritative.
- TEMPLATE/EXAMPLES-ONLY docs are context-only; do not make binding decisions from them.
- If core docs are TEMPLATE, stop and run Template-to-Production before coding (doc updates only).
- Use risk tiers to decide which docs to read (PRD/TECH_STACK/IMPLEMENTATION_PLAN, then SECURITY/docs map for high-risk).
- For non-trivial tasks (> 20 lines or > 1 file): write a plan and wait for explicit approval.
- Session mode can be set in `/.agents/docs/PROGRESS.md` via `SESSION_MODE: STANDARD | AUTO-PILOT`.
- If the user says “AUTO-PILOT”, the agent can auto plan/research/execute within the project folder for the session.
- If AUTO-PILOT is off, dangerous actions require explicit approval.
- Execute in atomic steps and verify (tests/build/manual as applicable).
- Update docs only via the Documentation Evolution Protocol (propose → approval → update → log).
- Record session state in PROGRESS and new rules in LESSONS when corrected.

## AI Agent Activation Flow (ASCII)

This section visualizes what happens when an AI agent is activated in this repo, how it decides what to read, how it plans work, where approvals happen, and how `AGENTS.md` and `/.agents/docs/*` interact.

```text
================================================================================
AI AGENT ACTIVATION FLOW (this repo)
Reflects: AGENTS.md constitution + /.agents/docs supporting docs + approval gates + docs
================================================================================

LEGEND
------
[Doc]        = a file the agent reads/writes
(§X)         = section in AGENTS.md
<Decision?>  = branching decision
{Action}     = action the agent performs
-->          = next step
==>          = “consult /.agents/docs/* as needed” expansion

SESSION MODE
------------
AUTO-PILOT = auto plan/research/execute within the project folder (session-scoped)
SESSION_MODE = STANDARD | AUTO-PILOT (set per session in PROGRESS.md)


┌──────────────────────────────────────────────────────────────────────────────┐
│ 0) AGENT ACTIVATED IN PROJECT FOLDER                                          │
└──────────────────────────────────────────────────────────────────────────────┘
        |
        v
┌──────────────────────────────────────────────────────────────────────────────┐
│ 1) LOAD CONSTITUTION + SESSION STATE                                          │
└──────────────────────────────────────────────────────────────────────────────┘
{Read} [AGENTS.md]
  - authority model + conflict ladder (§1, §3)
  - risk-tier reading rules (§2)
  - workflow + approval gate (§4)
  - doc evolution protocol (§5)
  - self-improvement protocol (§6)
  - security/protection (§7)
  - engineering/testing defaults (§8)
  - doc map (§9)
  - completion checklist (§10)

{Read} [/.agents/docs/PROGRESS.md]  (always; session carry-over)
{Read} SESSION_APPROVAL_MODE (STANDARD | PLAN+DOC | ALL)
{Check} STATUS headers (TEMPLATE / PRODUCTION / EXAMPLES-ONLY)
{Rule} TEMPLATE/EXAMPLES-ONLY docs = context-only (non-authoritative)
<Decision?> Any core doc still TEMPLATE?
  +-- Yes --> {STOP} run Template-to-Production (doc updates only; approval required)
  +-- No  --> continue
        |
        v
<Decision?> Any referenced doc missing?  (Missing-Doc Protocol §2)
        |
        +-- No  --> continue
        |
        +-- Yes --> {STOP}
                    {Notify user: missing doc(s)}
                    {Ask: scaffold missing doc OR proceed with safe defaults}
                    (Never hallucinate)

        |
        v
┌──────────────────────────────────────────────────────────────────────────────┐
│ 2) CLASSIFY WORK RISK TIER (what else to read before planning)                │
└──────────────────────────────────────────────────────────────────────────────┘
<Decision?> Risk tier?  (§2)
        |
        +-- Low  (mechanical/small change, <5 files, no auth/data deletion)
        |     |
        |     v
        |   {Read only target files + PROGRESS}
        |
        +-- Normal (default features / UI changes)
        |     |
        |     v
|   {Also read} [/.agents/docs/PRD.md] [/.agents/docs/TECH_STACK.md] [/.agents/docs/IMPLEMENTATION_PLAN.md]
        |
        +-- High  (auth/payments/data deletion/infra/>5 files)
              |
              v
{Also read} [/.agents/docs/SECURITY.md] + relevant docs in Doc Map (§9)


        |
        v
┌──────────────────────────────────────────────────────────────────────────────┐
│ 3) FOR EACH USER TASK: PLAN OR DO TRIVIAL                                     │
└──────────────────────────────────────────────────────────────────────────────┘
<Decision?> Is task trivial?  (§4)
(trivial = ≤ 20 LOC, 1 file, no new behavior, no security/data changes, no API/DB changes)
        |
        +-- Yes (Trivial Path)
        |     |
        |     v
        |   {Implement minimal change}
  |   {Verify} (tests/build/manual as required)
|   {Update} [/.agents/docs/PROGRESS.md] (what changed, what’s next)
        |   --> Done
        |
        +-- No (Plan Path)
              |
              v
┌──────────────────────────────────────────────────────────────────────────────┐
│ 4) WRITE THE PLAN (how the agent breaks down work)                             │
└──────────────────────────────────────────────────────────────────────────────┘
{Write plan} using [/.agents/docs/GUIDELINES.md] "Plan Template (RECOMMENDED)"
PLAN MUST include:
  - Goal / Scope / Non-goals
  - Constraints (tools, time, compatibility, risk tier)
  - Assumptions (explicit; tie to PRD/TECH_STACK where relevant)
  - Risks / unknowns
  - TASK BREAKDOWN (atomic + verifiable)
     * each task has: files/areas, success criteria, verification, deps/blockers
  - Rollback / Stop conditions

==> While planning, consult docs as needed (Doc Map §9):
  - [/.agents/docs/PRD.md]                 (what to build / requirements)
  - [/.agents/docs/TECH_STACK.md]          (what tools/versions are allowed)
  - [/.agents/docs/IMPLEMENTATION_PLAN.md] (milestones, dependencies, verification)
  - [/.agents/docs/TEST_STRATEGY.md]       (testing patterns; bug reproduction)
  - [/.agents/docs/APP_FLOW.md]            (user journeys + edge cases)
  - [/.agents/docs/DESIGN_SYSTEM.md]       (UI tokens + accessibility expectations)
  - [/.agents/docs/FRONTEND_GUIDELINES.md] (frontend patterns/perf/accessibility)
  - [/.agents/docs/BACKEND_STRUCTURE.md]   (backend layering/security/data flow)
  - [/.agents/docs/MEMORY.md]              (stable architectural decisions/glossary)
  - [/.agents/docs/TASKS.md]               (atomic task tracking conventions)

        |
        v
<Decision?> Does plan include doc changes OR STATUS needs promotion?
        |
        +-- No  --> proceed
        |
        +-- Yes --> {Prepare doc update proposals}
                    (Batch with plan approval allowed; §5 “Batching”)

        |
        v
┌──────────────────────────────────────────────────────────────────────────────┐
│ 5) APPROVAL GATE (no implementation without explicit approval)                │
└──────────────────────────────────────────────────────────────────────────────┘
<Decision?> AUTO-PILOT enabled OR user explicitly approves the plan?  (§4 step 3)
        |
        +-- No  --> {STOP} (do not implement)
        |
        +-- Yes --> continue


        |
        v
┌──────────────────────────────────────────────────────────────────────────────┐
│ 6) EXECUTE IN ATOMIC STEPS + VERIFY                                           │
└──────────────────────────────────────────────────────────────────────────────┘
Loop per atomic task:
  {Implement 1 atomic task}  (§4 step 4)
  {Verify}                   (§4 step 5, §8 “Test Default”, §10 checklist)
    - Run relevant tests (or add tests for bug fixes; §4 Error Protocol)
    - Run build/typecheck if applicable
    - Manual checks if relevant

  <Decision?> Verification failed?
    |
    +-- No  --> mark task done, proceed to next atomic task
    |
    +-- Yes --> {Error Protocol} (§4)
               - Diagnosis first
               - For bugs: minimal reproduction test first
               - Fix root cause; re-verify; do NOT paper over failures

  <Decision?> Security issue discovered?  (§7)
    |
    +-- No  --> continue
    |
    +-- Yes --> {STOP immediately}
               {Write WARNING}
               {Wait for explicit direction}
               (Optionally: safe reproduction test if appropriate)

  <Decision?> User corrected the agent?  (§6)
    |
    +-- No  --> continue
    |
    +-- Yes --> {Self-Improvement Protocol}
               - Acknowledge mistake
               - Propose new preventive rule + location
  - Use Doc Evolution Protocol before editing docs (§5)


        |
        v
┌──────────────────────────────────────────────────────────────────────────────┐
│ 7) DOCUMENTATION UPDATES (NOT AUTO; proposal + approval required)             │
└──────────────────────────────────────────────────────────────────────────────┘
<Decision?> Do any docs need updating due to work done OR Template-to-Production trigger?
        |
        +-- No  --> continue
        |
                   +-- Yes --> {Doc Evolution Protocol} (§5)
                   1) STOP and DECLARE: "I notice [doc] needs update: [reason]"
                   2) PROPOSE:
                      PROPOSED DOC UPDATE to [filename]:
                      OLD: [exact quoted section]
                      NEW: [proposed change]
                      REASON: [why]
                   3) WAIT for approval
                   4) APPLY doc edits only after approval
                   5) LOG decision in [/.agents/docs/LESSONS.md]
                   6) UPDATE [/.agents/docs/PROGRESS.md]


        |
        v
┌──────────────────────────────────────────────────────────────────────────────┐
│ 8) SESSION CLOSEOUT                                                           │
└──────────────────────────────────────────────────────────────────────────────┘
{Update} [/.agents/docs/PROGRESS.md]
  - Completed / In Progress / Blockers / Notes

{Update} [/.agents/docs/LESSONS.md] when the user corrects the agent
  - new patterns / mistakes / prevention rules

{Ensure consistency}
  - doc map references still correct
  - STATUS headers reflect reality (TEMPLATE vs PRODUCTION)
  - no supporting doc overrides AGENTS.md (Conflict Ladder §3)


================================================================================
QUICK “WHICH DOC DO I USE?” MAP
================================================================================
- Need to decide WHAT to build?            -> [/.agents/docs/PRD.md]
- Need to confirm allowed tools/versions?  -> [/.agents/docs/TECH_STACK.md]
- Need the execution roadmap?              -> [/.agents/docs/IMPLEMENTATION_PLAN.md]
- Need user journey + error handling UX?   -> [/.agents/docs/APP_FLOW.md]
- Need UI tokens/accessibility rules?      -> [/.agents/docs/DESIGN_SYSTEM.md]
- Need frontend patterns/perf?             -> [/.agents/docs/FRONTEND_GUIDELINES.md]
- Need backend layering/security patterns? -> [/.agents/docs/BACKEND_STRUCTURE.md]
- Need test expectations?                 -> [/.agents/docs/TEST_STRATEGY.md]
- Need long-lived decisions/glossary?      -> [/.agents/docs/MEMORY.md]
- Need atomic task checklist conventions?  -> [/.agents/docs/TASKS.md]
- Need session carry-over state?           -> [/.agents/docs/PROGRESS.md]
- Need “what we learned / avoid next time”?-> [/.agents/docs/LESSONS.md]
```

1. At the start of **every session**, the agent follows the **risk-tiered reading strategy** defined in `AGENTS.md` §2:
   - **Always**: `AGENTS.md` (behavior rules) + `/.agents/docs/PROGRESS.md` (session state)
   - **Normal+**: Adds `PRD.md`, `IMPLEMENTATION_PLAN.md`, `TECH_STACK.md`
   - **High-risk**: Full reading of all files listed in the Documentation Map (§9)

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
  → Emphasis on test-first bug fixing, PROGRESS.md style state tracking

- **Various high-signal GitHub repos** (especially Claude + Cursor + Windsurf setups with 100+ stars)

- **Public X threads** (2025–2026) on agent reliability, security hardening, prompt injection defense, and parallel sub-agents

Special thanks to the many developers who openly shared their `CLAUDE.md` / `AGENTS.md` files and correction rituals — this is a collective distillation of what actually works in production.

## Quick Start (Template Mode)
1. Copy `AGENTS.md` to your project root.
2. Copy `/.agents/docs/` into your project and keep filenames unchanged.
3. Replace all **Example (fictional)** blocks in `PRD.md`, `TECH_STACK.md`, `IMPLEMENTATION_PLAN.md`, `PROGRESS.md`, `TASKS.md`, and `MEMORY.md`.
4. Point your AI tool to `AGENTS.md` as the project instruction file.
5. Start the first session and let the agent follow the risk-tiered reading rules.

## How to Use This Setup

1. Place `AGENTS.md` in your project root and supporting docs (including `GUIDELINES.md`) under `/.agents/docs/`
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
