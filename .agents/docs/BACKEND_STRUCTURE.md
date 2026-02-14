# BACKEND_STRUCTURE.md

> **Status**: TEMPLATE  
> **Last Updated**: YYYY-MM-DD

Backend architecture and API patterns.

> **Guide**: See [GUIDELINES.md Part 3: Backend Documentation](/.agents/docs/GUIDELINES.md#backend-documentation) for the teaching guide on how to write this.

---

## Quick Start

**To fill this template:**
1. Read GUIDELINES.md "How to write it" section for Backend
2. Examine 3-5 files in each layer of your actual codebase
3. Extract patterns and document with examples

---

## Architecture Overview

[One sentence what this backend does]

### Layer Structure
```
[Your actual structure here]
```

---

## Patterns

### 1. [Pattern Name]
**What**: [Description]
**Why**: [Rationale]
**Example**:
```typescript
[Code example]
```

---

## Do / Don't

| Do ✅ | Don't ❌ |
|-------|----------|
| [Good practice] | [Bad practice] |

---

## API Standards

- **Routes**: [Pattern]
- **Request/Response**: [Format]
- **Error Handling**: [Approach]

---

## Security Checklist

Every endpoint:
- [ ] Authentication required?
- [ ] Authorization checked?
- [ ] Input validated?
- [ ] Rate limited?
- [ ] SQL injection safe?
