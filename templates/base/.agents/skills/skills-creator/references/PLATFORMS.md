# Platform Runtime Constraints

## Claude API
- No network access from skills
- No runtime package installation — pre-installed packages only
- Check code execution tool docs for available packages
- Skills shared workspace-wide via `/v1/skills` endpoints
- Required beta headers: `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14`

## Claude Code
- Full network access (same as local machine)
- Do NOT install packages globally — local installs only
- Skills live in `~/.claude/skills/` (personal) or `.claude/skills/` (project)
- Filesystem-based, no API upload needed

## Claude.ai
- Network access varies by user/admin settings
- Package behavior varies
- Custom skills: individual user only, uploaded as `.zip` via Settings > Features
- Available on Pro, Max, Team, Enterprise with code execution enabled

## Key Rule
Skills do NOT sync across surfaces. Manage separately per platform.
