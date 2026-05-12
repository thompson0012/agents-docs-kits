# Principle Details

> This file contains the full body of each principle. SKILL.md keeps the quick-reference version; this is the authoritative reference for when deeper justification is needed.

---

## Design Thinking

### 1. Start from usage, not from capability

```
❌ Ask: What features should the system support?
✅ Ask: What code does the user want to write?
```

**Execution rule:** Write caller-side code first. Only change the system when that code doesn't work. Don't design outward from system capabilities.

### 2. Add only with a concrete instance; don't guess

Every addition must correspond to a **specific, concrete use case that cannot be achieved with the existing API**.

```
Don't add:
- "Might need this in the future"
- "Framework X has this pattern so we should too"
- "It feels more complete this way"
```

Guessed requirements are not requirements.

### 3. Add at the lowest level, not the highest

Fix the gap where you find it. Order of preference:

```
one parameter > one method > one class > one module > one new layer
```

### 4. System provides primitives; doesn't compose for the user

Give the fewest possible fundamental building blocks. Let the user compose them. Don't predict how the user will compose.

### 5. One line of working code > a page of design doc

Evidence is not "Book X says we need Y." Evidence is "This code doesn't work because Y is missing."

---

## Architecture Principles

### 6. Core is minimal and never bloats

The core does exactly one thing. All advanced capabilities hang off the core. Core growing = direction is wrong.

### 7. Plugins mount at timing points, not as subsystems

- Define fixed execution timing points (hooks)
- Plugins declare which point they care about; they don't control when they execute
- No plugin management framework
- No plugin registry

### 8. One structure, many purposes

Don't build different subsystems for different problems. Find a unified data structure that solves multiple needs simultaneously.

One less structure = one less category of synchronization bugs.

**Split boundary:** When a new use case requires twisting the core structure's semantics to work, that's when to split. Preserving structural semantics > minimizing structural count.

### 9. Code = configuration

Internal tools don't need a configuration system. Declarative API beats YAML / JSON / env-var assembly.

---

## Decision Discipline

### 10. Evidence threshold

Every removed feature has explicit "bring it back" conditions: how many use cases, how many users, what pain point. Not "never add it." Means "add it when there's evidence."

### 11. Review must include a "cut" step

Reviews default to addition. Finding "what's missing" is easier than finding "what's extra."

**After every review, ask:**
- What was added?
- What can be removed?

### 12. AI adds; humans subtract

AI tends toward over-design, pattern-mapping, and not cleaning up. The human's core value isn't generating more design — it's judging which designs shouldn't exist.

**AI behavior rules:**
- After writing code, actively check for removable code, files, abstraction layers
- Don't keep unused code for "completeness"
- Don't introduce indirection layers "that might be useful later"

### 13. Docs growing = direction is wrong

Good design makes documentation shorter. If docs grow after every iteration, stop and ask why.

### 14. Deprecation must allow gradual migration

Breaking changes must let old and new coexist for at least one version cycle. User code shouldn't break all at once.

---

## Debuggability

### 15. System must make failure causes obvious

A failing composition must produce an error message that points to the specific primitive.

```
❌ "Something went wrong"
✅ "createUser() failed: email already exists (user_service.go:42)"
```

In a minimal system, user code is composed. If the system doesn't tell you which primitive failed and why, debugging cost turns "give primitives, let users compose" into punishment.

---

## Performance Boundary

### 16. Naive compositions shouldn't cause orders-of-magnitude performance penalties

If a common composition pattern is more than 3x slower than a hand-rolled solution, the system should provide a more efficient composition path rather than forcing users to bypass the system.
