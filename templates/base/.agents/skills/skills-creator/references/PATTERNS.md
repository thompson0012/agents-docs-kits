# Progressive Disclosure Patterns

## Levels
- **Level 1 — Metadata**: YAML frontmatter only. Always loaded; keep minimal.
- **Level 2 — Instructions**: SKILL.md body. Stay under 5,000 tokens/500 lines. Put only what is needed to execute.
- **Level 3 — Resources**: `references/`, `scripts/`, `assets/`. Load on demand only. Never chain beyond one hop (`SKILL.md → ref.md` only).

## Fragility → Instruction Style
- **Low fragility**: heuristics and short bullets.
- **Medium fragility**: parameterized pseudocode and explicit flags.
- **High fragility**: exact commands to run; forbid edits.

## Routing Content
- Inline edge cases that fit in ≤3 lines; move the rest to `references/`.
- Keep a single term per concept across the SKILL and references.
- Avoid time-sensitive content in SKILL.md; move legacy notes under a `Legacy Patterns` section in references if needed.

## Evaluation Pattern (Claude A / Claude B)
1. Author the skill (Claude A).
2. Fresh session loads the skill and runs real tasks (Claude B).
3. Record failures, patch the SKILL/scripts, and re-run until scenarios pass.
