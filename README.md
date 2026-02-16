# AI Agents Setup

Battle-tested configuration for AI coding agents.

## Documentation Structure

| Path | Purpose | Start Here |
|------|---------|------------|
| `AGENTS.md` | **Constitution** — behavior rules and protocols | ✅ Always read first |
| `/.agents/docs/GUIDELINES.md` | **Teaching Guide** — how to think and write docs | ✅ Read when writing docs |
| `/.agents/docs/PRD.md` | Product requirements (template) | Fill per project |
| `/.agents/docs/TECH_STACK.md` | Technology choices (template) | Fill per project |
| `/.agents/docs/PROGRESS.md` | Session state (template) | Update each session |
| `/.agents/docs/LESSONS.md` | Learned patterns (template) | Log corrections here |
| `/.agents/docs/MEMORY.md` | Architectural decisions (template) | Fill per project |
| `/.agents/skills/self-cognitive/SKILL.md` | Self-cognitive meta skill | Use for verification/retrospectives |

**Domain-Specific** (fill based on GUIDELINES.md Part 3):
- `/.agents/docs/BACKEND.md` — Backend patterns
- `/.agents/docs/FRONTEND.md` — Frontend standards

## Quick Start

1. Copy `AGENTS.md` to project root — this is your AI's constitution
2. Copy `/.agents/docs/` to your project
3. **Read** `GUIDELINES.md` to learn how to fill templates properly
4. Fill templates with project-specific info (use GUIDELINES.md Part 3 for Backend/Frontend)
5. Set `AGENTS.md` as your AI tool's instruction file

### Learning Path for AI Agents

```
First Session:
AGENTS.md ──► Understand behavior rules
     │
     ▼
GUIDELINES.md ──► Learn how to think & write
     │
     ▼
Fill PRD.md, TECH_STACK.md ──► Establish project context

Ongoing:
PROGRESS.md ◄──► Update each session
LESSONS.md ◄──► Log when corrected
```

## Agent Processing Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      SESSION START                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  READ: AGENTS.md → PROGRESS.md → Risk-based tiered docs     │
│  ├─ Low:   Target files only                                │
│  ├─ Normal: + PRD.md, TECH_STACK.md                         │
│  └─ High:   + SECURITY.md, all relevant docs                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
            ┌────────────────────┐
            │   TASK CLASSIFY    │
            │  ┌──────────────┐  │
            │  │ ≤20 LOC,     │  │
            │  │ 1 file,      │──┼──► TRIVIAL? ──Yes──► EXECUTE
            │  │ no new       │  │                      │
            │  │ behavior     │  │                      No
            │  └──────────────┘  │                       │
            └────────────────────┘                       ▼
                                               ┌─────────────────┐
                                               │   CREATE PLAN   │
                                               │  - Goal/Scope   │
                                               │  - Tasks        │
                                               │  - Risks        │
                                               └────────┬────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │  AWAIT APPROVAL │
                                               │ (unless AUTO-   │
                                               │  PILOT mode)    │
                                               └────────┬────────┘
                                                        │
                                                        ▼
┌───────────────────────────────────────────────────────┴──────┐
│                         EXECUTE                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────┐  │
│  │  Implement  │───►│   Verify    │───►│   Document      │  │
│  │  (atomic)   │    │  LSP/tests  │    │  PROGRESS.md    │  │
│  └─────────────┘    └─────────────┘    └─────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │  Success │ │  Error   │ │ Security │
    │   Done   │ │   ───►   │ │   Vuln   │
    └──────────┘ │ Diagnose │ │   ───►   │
                 │ Reproduce│ │   Stop   │
                 │  Retry   │ │   Warn   │
                 │          │ │Escalate  │
                 └──────────┘ └──────────┘
```

## Reading Flow

```
AGENTS.md → PROGRESS.md → [Tier-based docs]
```

- **Low risk**: Targets only
- **Normal risk**: + PRD.md, TECH_STACK.md
- **High risk**: + All relevant docs

## Key Concepts

- **Lazy Reading**: Read only what you need (tier-based)
- **Explicit Approval**: Plans need approval (unless AUTO-PILOT)
- **Template→Production**: Fill templates before relying on them
- **AGENTS.md First**: Always check constitution before other docs
- **GUIDELINES.md Teaches**: It's a tutorial, not just reference — explains HOW to think and write

### For AI Agents: How to Use This System

1. **Thinking**: See GUIDELINES.md Part 1 (The AI Mindset)
2. **Writing**: See GUIDELINES.md Part 2 (The Writing Process)
3. **Backend/Frontend**: See GUIDELINES.md Part 3 (Domain Guides)  
4. **Templates**: See GUIDELINES.md Part 4 (Document Templates)

See `AGENTS.md` for complete behavior rules.
