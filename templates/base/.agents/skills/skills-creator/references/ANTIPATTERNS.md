# Common Authoring Antipatterns

- Description in first person or without clear trigger conditions.
- Frontmatter bloated with unused fields; `name` does not match folder.
- Names with uppercase letters, underscores, or forbidden words; double/leading/trailing hyphens.
- Chained references (`SKILL.md → ref A → ref B`) that hide critical guidance.
- Time-sensitive or platform-bound instructions embedded in SKILL.md.
- Scripts without declared intent in the SKILL, or without error handling for missing files/permissions.
- Skipping evaluation scenarios or shipping without re-running validation after edits.
- Deep file paths inside `references/` that exceed one-level depth.
