# AI Agents Setup

Battle-tested configuration for AI coding agents.

## Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | **Constitution** — behavior rules and protocols |
| `/.agents/docs/GUIDELINES.md` | How to write documentation |
| `/.agents/docs/PRD.md` | Product requirements (template) |
| `/.agents/docs/TECH_STACK.md` | Technology choices (template) |
| `/.agents/docs/PROGRESS.md` | Session state (template) |
| `/.agents/docs/LESSONS.md` | Learned patterns (template) |
| `/.agents/docs/FRONTEND_GUIDELINES.md` | Frontend standards (template) |
| `/.agents/docs/BACKEND_STRUCTURE.md` | Backend patterns (template) |
| `/.agents/docs/MEMORY.md` | Decisions (template) |

## Quick Start

1. Copy `AGENTS.md` to project root
2. Copy `/.agents/docs/` to your project
3. Fill templates with project-specific info
4. Set `AGENTS.md` as your AI tool's instruction file

## Reading Flow

```
AGENTS.md → PROGRESS.md → [Tier-based docs]
```

- **Low risk**: Targets only
- **Normal risk**: + PRD.md, TECH_STACK.md
- **High risk**: + All relevant docs

## Key Concepts

- **Lazy Reading**: Read only what you need
- **Explicit Approval**: Plans need approval (unless AUTO-PILOT)
- **Template→Production**: Fill templates before relying on them
- **AGENTS.md First**: Always check constitution before other docs

See `AGENTS.md` for complete behavior rules.
