# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Add a portable `software-delivery` router family that captures the strongest reusable lifecycle ideas from gstack without cloning its runtime-specific shape, while keeping the existing flat atomic skills discoverable and truthful.

## Scope

In Scope:
- Create a new top-level `templates/base/.agents/skills/software-delivery/` router with only the family-specific nested leaves it genuinely owns.
- Reuse existing flat atomic skills such as `using-reasoning`, `feature-spec`, `coding-and-data`, `website-building`, and `self-cognitive` through honest router metadata rather than wrapper skills.
- Update discovery surfaces and continuity docs so the new router is discoverable without introducing a generic `router-skills/` folder or moving existing top-level routers.
- Keep `scripts/audit_base_template_skills.py` green after the new family lands.

Explicitly Out of Scope:
- No new atomic skills (reuse existing ones only)
- No changes to existing top-level routers or skill names
- No gstack-specific imports (telemetry, slash-commands, browser-daemon)
- No generic `router-skills/` folder

Scope Expansion Test: If this work requires creating files not listed above, pause and confirm.

## Constraints

- Keep shipped skill names and current top-level router layout stable; add the new family without relocating existing routers or atomic skills.
- Do not import gstack telemetry, slash-command naming, browser-daemon assumptions, or vendor-specific preambles.
- Do not reintroduce stale `skills/` paths, vendor branding, unsupported tool names, template placeholders, or a generic `router-skills/` grouping.
- Prefer capability-based overlays to product- or vendor-specific instructions.

## Success Criteria

- The new `software-delivery` router and its family-specific leaf skills are structurally valid, portable, and clearly bounded.
- Discovery surfaces (`README.md`, `templates/base/AGENTS.md`, and the category map) describe the new router honestly without forcing it onto trivial work.
- The portability audit and all relevant validators pass after the new family lands.