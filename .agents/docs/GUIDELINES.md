# GUIDELINES.md

> **Status**: TEMPLATE  
> **Purpose**: Documentation writing standards

How to create and maintain project documentation.

---

## 1. Document Header (Required)

Every doc must start with:

```markdown
> **Status**: TEMPLATE | PRODUCTION | EXAMPLES-ONLY
> **Last Updated**: YYYY-MM-DD

Brief description of document purpose.
```

**Status meanings**:
- `TEMPLATE`: Generic, not project-specific (default)
- `PRODUCTION`: Validated, authoritative
- `EXAMPLES-ONLY`: Fictional examples to remove

---

## 2. Writing Standards

- **Concise**: Clear over complete
- **Scannable**: Use tables, lists, and headings
- **Evidence-based**: Derive from code or user input
- **Assumptions labeled**: Mark inferences clearly

---

## 3. Plan Template

Use when proposing non-trivial work:

```markdown
## Plan: [Title]

**Goal**: [What and why]

**Scope**:
- In: [What's included]
- Out: [What's excluded]

**Tasks**:
1. [ ] [Task] — Verification: [how to confirm]
2. [ ] [Task] — Verification: [how to confirm]

**Risks**: [What could go wrong]

**Rollback**: [How to recover]
```

---

## 4. Update Protocol

When docs need changing:

1. **Propose**:
   ```markdown
   PROPOSED UPDATE to [filename]:
   
   OLD:
   [exact text]
   
   NEW:
   [proposed text]
   
   REASON: [why]
   ```

2. **Wait**: For explicit approval
3. **Apply**: Make the change
4. **Log**: Record in LESSONS.md

---

## 5. Template Reference

| File | Contains | Fill With |
|------|----------|-----------|
| **PRD.md** | Product requirements | Goals, features, user journeys |
| **TECH_STACK.md** | Technology choices | Tools, versions, constraints |
| **PROGRESS.md** | Session state | Completed tasks, blockers |
| **LESSONS.md** | Learned patterns | Mistakes and prevention rules |
| **FRONTEND_GUIDELINES.md** | Frontend patterns | UI conventions, accessibility |
| **BACKEND_STRUCTURE.md** | Backend patterns | API conventions, data flow |
| **MEMORY.md** | Decisions | ADRs, glossary, history |

---

## 6. Quick Reference

**Before work**:
```markdown
ASSUMPTIONS:
- [Assumption to verify]
```

**After work**:
```markdown
CHANGES:
- [file]: [what changed and why]
```
