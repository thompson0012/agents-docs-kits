---
name: skills-creator
description: >
  Scaffolds, authors, validates, and iterates on SKILL.md packages following
  Anthropic's Agent Skills spec and authoring guidelines. Use when asked to
  create, refine, review, or evaluate a skill package.
license: MIT
compatibility: >
  Claude Code (full support); Claude API (no network, no runtime installs);
  Claude.ai (varying network). Python 3.9+ required for scripts.
allowed-tools: Bash(python3:*) Read Write
meta:
  author: your-org
  version: "2.0"
  spec: anthropic-agent-skills-2025-10-02
---

# Skills Creator

Guides the complete lifecycle of a SKILL.md package: discover → scaffold →
author → write scripts → evaluate → ship. Never skip Phase 5 (Evaluate).

## Preconditions
- Confirm the user's intent, target outcome, and where the skill will run. Keep instructions universal across surfaces.
- Identify tools, data, and external services up front; avoid hidden dependencies.
- Decide the output format (SKILL-only vs. SKILL + references/scripts).

## Phase 1 — Discover
Answer all five questions before writing anything:
1. **Single responsibility** — What is the one thing this skill does?
2. **Failure case** — What specific task fails without this skill?
3. **Dependencies** — Which tools or services are required?
4. **I/O contract** — What does the user provide? What is produced?
5. **Fragility** — How sensitive is execution to variation (drives instruction style)?

If any answer is unclear, stop and ask for clarification. Vague skills produce vague behavior.

## Phase 2 — Scaffold
- Generate the folder and boilerplate: `python3 scripts/scaffold.py <skill-name>`
- Naming rules (enforced by the scaffold/validator):
  - Gerund form preferred: `processing-pdfs`, `analyzing-logs`
  - Lowercase letters, numbers, hyphens only; max 64 chars; no leading/trailing/double hyphens
  - Forbidden words: `anthropic`, `claude`, `helper`, `utils`, `tools`
- Minimum valid output: `<skill-name>/SKILL.md` (add `scripts/` when execution steps exist)
- Use `assets/skill_template.md` for the SKILL and `assets/eval_template.md` for starter evals.

## Phase 3 — Author SKILL.md
### Frontmatter
Only add optional fields when they provide real value.
```yaml
---
name: <gerund-skill-name>
description: >
  [Third-person verb phrase. What it does. When to use it.]
license: MIT                         # if distributing
compatibility: Requires pdfplumber   # if environment-specific
allowed-tools: Bash(python3:*) Read  # if pre-approving tools
meta:
  author: your-org
  version: "1.0"
---
```

### Description formula
> "[Verb phrase]. Use when [trigger condition(s)]."
- Third-person only; include clear triggers; max 1,024 characters; no XML tags.

### Body structure
Calibrate instruction style to fragility:
- **Low**: natural-language heuristics
- **Medium**: parameterized pseudocode
- **High**: exact verbatim commands

Standard order:
1. Preconditions — what must be true before starting
2. Steps — numbered, imperative, one action per step
3. Tools — which tools to call and when (use fully-qualified MCP names)
4. Output — artifact type, format, destination
5. Edge Cases — inline if short; otherwise link to `references/`

### Progressive disclosure rules
- Level 1: frontmatter (always loaded)
- Level 2: SKILL body (<5k tokens, ≤500 lines)
- Level 3: `references/`, `scripts/`, `assets/` (loaded only when opened)
- References may go one level deep only. Move heavy content to `references/`.
- No time-sensitive content inline; put legacy items under `references/`.

### Progress checklist (example)
```
Task Progress:
- [ ] Step 1: Draft SKILL.md from template
- [ ] Step 2: Add references/scripts only if needed
- [ ] Step 3: Validate output
- [ ] Step 4: Fix errors and re-validate
- [ ] Step 5: Only proceed when validation passes
```

## Phase 4 — Write Scripts
- Keep scripts self-contained; handle `FileNotFoundError`, `PermissionError`, and invalid input explicitly.
- Use forward slashes only; add intent in SKILL: "Run scripts/<file>.py..." or "See scripts/<file>.py..."
- If packages are required, note them inline (e.g., `# pip install pdfplumber`) and confirm platform support first.

## Phase 5 — Evaluate (Never Skip)
- Write at least 3 scenarios using `assets/eval_template.md`.
- Claude A/Claude B loop (recommended):
  1. Author the skill (Claude A).
  2. Fresh session loads the skill and runs real tasks (Claude B).
  3. Record failures and close gaps in SKILL or scripts.
  4. Repeat until all scenarios pass.
- Run validation: `python3 scripts/validate.py <skill-name>`

## Phase 6 — Platform Check
Confirm the target surface before shipping; keep guidance universal. See `references/PLATFORMS.md` for constraints across Claude Code, Claude API, and Claude.ai.

## Phase 7 — Security Audit
Treat distributing a skill like releasing software. Review `references/SECURITY.md` before sharing externally.

## Pre-Ship Gate
Run the full checklist: `python3 scripts/validate.py <skill-name> --full`

Manual confirmations:
- [ ] `name` is gerund-form, ≤64 chars, no forbidden words, matches folder
- [ ] `description` is third-person, has trigger condition, ≤1,024 chars, no XML tags
- [ ] Body ≤500 lines, <5,000 tokens; heavy content lives in `references/`
- [ ] All file references are max one level deep
- [ ] Scripts declare intent, handle errors, and use forward slashes
- [ ] Platform constraints checked; no platform-bound instructions
- [ ] Minimum 3 evaluation scenarios written and passing
- [ ] Security audit completed if distributing

## References and Assets
- Patterns and disclosure guidance: `references/PATTERNS.md`
- Platform constraints: `references/PLATFORMS.md`
- Security audit checklist: `references/SECURITY.md`
- Common authoring mistakes: `references/ANTIPATTERNS.md`
- Templates: `assets/skill_template.md`, `assets/eval_template.md`
