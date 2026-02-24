# Codemap

> **Version**: 1.0.0  
> **Status**: PRODUCTION  
> **Last Updated**: 2026-02-24

Living architecture documentation. Provides high-level system overview so agents don't need to re-read the entire codebase.

---

## Schema

```yaml
codemap:
  version: string           # Semver
  status: TEMPLATE|PRODUCTION|STALE
  last_updated: ISO8601
  
  system:
    name: string
    type: web-app|cli|library|service
    purpose: string         # One-line description
    architecture_pattern: string  # layered|microservices|event-driven|monolith
    
  entry_points:
    - name: string
      path: string
      description: string
      
  modules:
    - name: string
      path: string
      responsibility: string
      design_patterns:
        - string
      dependencies:
        - path: string
          purpose: string
      consumers:
        - path: string
          usage: string
          
  data_flows:
    - name: string
      description: string
      steps:
        - component: string
          action: string
          
  external_dependencies:
    - name: string
      purpose: string
      version: string
```

---

## Architecture

```
+-------------------------------------------------------+
|                    CODEMAP                            |
|              (Single Source of Truth)                  |
+-------------------------------------------------------+
                          |
          +---------------+---------------+
          |                               |
          v                               v
+------------------+            +------------------+
|  System Overview |            |  Module Details  |
|  - Entry points  |            |  - Responsibilities|
|  - Purpose       |            |  - Patterns      |
|  - Architecture  |            |  - Dependencies  |
+------------------+            +------------------+
          |                               |
          v                               v
+------------------+            +------------------+
|  Data Flow       |            |  Integration     |
|  - Key flows     |            |  - External deps |
|  - Step-by-step  |            |  - APIs          |
+------------------+            +------------------+
```

---

## Maintenance Rules

**When to Update:**
1. New module/directory added
2. Module responsibility changes
3. New architectural pattern introduced
4. Entry points change
5. Significant dependency added/removed

**Who Updates:**
- Agent making the architectural change
- Must update BEFORE completing task

**Update Process:**
1. Identify affected sections
2. Update with new information
3. Update `last_updated` timestamp
4. Add entry to CHANGELOG.md
5. Verify ASCII diagrams still accurate

---

## Integration with Session Bootstrap

```
[Session Start]
    |
    v
+------------------+      +------------------------+
| Load Codemap     |----->| Extract System Context |
|                  |      | - entry points         |
|                  |      | - module structure     |
+------------------+      +-----------+------------+
                                      |
                                      v
+------------------+      +------------------------+
| Load Change Log  |----->| Extract Recent Changes |
| (last N entries) |      | - recent deltas        |
+------------------+      | - impact areas         |
                          +-----------+------------+
                                      |
                                      v
+------------------+      +------------------------+
| Bootstrap        |<-----+ Inject Context         |
| Complete         |      | - codemap summary      |
+------------------+      | - recent changes       |
                          +------------------------+
```

---

## Template

```markdown
# [System Name] Codemap

> **Version**: 1.0.0  
> **Last Updated**: [ISO8601]  
> **Status**: PRODUCTION

## System Overview

**Name**: [System name]

**Type**: [web-app|cli-tool|library|service]

**Purpose**: [One-line description of what this system does]

**Architecture Pattern**: [layered|microservices|event-driven|monolith]

## Entry Points

| Name | Path | Description |
|------|------|-------------|
| [name] | [path] | [description] |

## Module Structure

```
[src/]
    |
    +-- [module1]/          [responsibility]
    |   +-- [submodule]/    [responsibility]
    |
    +-- [module2]/          [responsibility]
```

### [Module Name]

**Path**: `[path]`

**Responsibility**: [What this module does]

**Design Patterns**:
- [Pattern 1]: [How it's used]
- [Pattern 2]: [How it's used]

**Dependencies**:
- `[module/path]`: [Why it's needed]

**Consumers**:
- `[module/path]`: [How it uses this module]

## Data Flows

### [Flow Name]

```
[Component A] --[action]--> [Component B] --[action]--> [Component C]
```

1. **[Component A]**: [Action description]
2. **[Component B]**: [Action description]
3. **[Component C]**: [Action description]

## External Dependencies

| Name | Purpose | Version |
|------|---------|---------|
| [name] | [purpose] | [version] |
```

---

## Validation

**Completeness Check:**
- [ ] All modules documented
- [ ] All entry points listed
- [ ] ASCII diagrams present and accurate
- [ ] Dependencies up to date
- [ ] `last_updated` within last 30 days

**Quality Check:**
- [ ] Responsibilities are specific, not vague
- [ ] Design patterns are named correctly
- [ ] Data flows traceable
- [ ] No orphaned references

---

## Quick Reference

```bash
# Check freshness
date -r .agents/docs/CODEMAP.md +%Y-%m-%d

# View system type
grep "^**Type**:" .agents/docs/CODEMAP.md

# List entry points
sed -n '/## Entry/,/## Module/p' .agents/docs/CODEMAP.md | grep "|"
```

---

**Rule**: Agent has enough context to proceed without `ls -R` or `find .`.