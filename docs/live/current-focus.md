# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Keep the first-party skill suite under `templates/base/.agents/skills/` organized around an owned routing model: a suite router (`using-agent-practices`), a reasoning-family router (`using-reasoning`), the existing leaf skills, and a shared category map that explains how the pieces fit together.

## Scope

- Keep the new router skills under `templates/base/.agents/skills/using-agent-practices/` and `templates/base/.agents/skills/using-reasoning/`.
- Keep the suite taxonomy reference under `templates/base/.agents/skills/using-agent-practices/references/category-map.md`.
- Keep the starter skill-creator eval fixtures under each new router's `evals/evals.json`.
- Keep the existing 11 live leaf skills in place without renaming them.

## Constraints

- Use owned suite terminology; do not depend on third-party `superpowers` naming inside the first-party router skills.
- Keep the skill directory flat for now; express categories through routers and references rather than nested discovery assumptions.
- Preserve the existing leaf skill names and descriptions unless a future task explicitly asks to retune them.
- Do not commit from this task.

## Success Criteria

- `using-agent-practices/SKILL.md` routes across the current owned suite categories and points reasoning requests to `using-reasoning`.
- `using-reasoning/SKILL.md` routes cleanly among `thinking-ground`, `problem-definition`, `dynamic-problem-solving`, `domain-expert-consultation`, and `strategic-foresight`.
- Both router skills include starter `evals/evals.json` fixtures for future `skill-creator` iteration.
- `using-agent-practices/references/category-map.md` records the suite categories and routing rule of thumb.