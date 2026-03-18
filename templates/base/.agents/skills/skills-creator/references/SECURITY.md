# Security Audit Checklist

Run this before distributing a skill. Treat the skill like shipped software.

- No unexpected network calls in scripts; document every outbound request.
- Do not access files outside the skill directory unless explicitly required and declared.
- No external URL fetches embedded in SKILL.md (fetched content can be injected).
- Scope bash commands narrowly and make side effects explicit.
- Note any optional dependencies and their trust boundaries.
- Ensure scripts handle invalid inputs, missing files, and permission errors safely.
- Keep platform-specific steps isolated; avoid assuming install rights on any surface.
