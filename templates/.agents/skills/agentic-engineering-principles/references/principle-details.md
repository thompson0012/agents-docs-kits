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

**Why guessing fails:** Every abstraction is a map that selects some details and omits others. Without a concrete consumer, you don't know which details matter. The abstraction becomes a map of a territory you've never visited — it's as likely to mislead as to help. "Make it generic" without two concrete examples is building a bridge to nowhere.

### 3. Add at the lowest level, not the highest

Fix the gap where you find it. Order of preference:

```
one parameter > one method > one class > one module > one new layer
```

**Abstraction threshold test:** Before adding a formal abstraction (interface, new class, new module), run this triage:

| Question | If yes | If no |
|---|---|---|
| Do multiple implementations exist or are concretely planned? | Add abstraction | Keep concrete |
| Does this code need polymorphism (behavior varies by type)? | Add abstraction | Keep concrete |
| Is a test seam genuinely required? | Add abstraction | Keep concrete |

If all three are "no," the abstraction is speculative — delete it or don't create it.

### 4. Invest proportionally to change frequency

Architectural complexity is a hedge against future change. The question isn't "is this abstract enough?" but "how often does this change?"

| Change profile | How to treat it |
|---|---|
| **High volatility + high criticality** | Full isolation: interface, bounded context, high test coverage |
| **Low volatility + low criticality** | Keep simple: no ceremony, concrete types, minimal tests |
| **Unknown volatility** | Keep simple until proven otherwise. Let the code tell you it changes often before you invest in protecting it. |

Apply this *before* deciding which layers or abstractions a component needs. The same codebase should have high-ceremony hotspots and low-ceremony stable zones — uniformity is a smell.

### 5. System provides primitives; doesn't compose for the user

Give the fewest possible fundamental building blocks. Let the user compose them. Don't predict how the user will compose.

### 6. One line of working code > a page of design doc

Evidence is not "Book X says we need Y." Evidence is "This code doesn't work because Y is missing."

---

## Architecture Principles

### 7. Core is minimal and never bloats

The core does exactly one thing. All advanced capabilities hang off the core. Core growing = direction is wrong.

**Litmus test:** Can a developer replace any non-core component without modifying the kernel? If the answer is "no" for any component, the boundary between core and protocol is wrong.

**Deciding what goes in core:** Core ≠ Domain. Core = what changes least often. Volatile business logic needs isolation but doesn't belong in the "core" — it needs its own bounded context with high test coverage. Stable infrastructure (data types that have settled, utility functions, established protocols) belongs in or near the core. Ask: "Would changing this break everything, or would changing everything break this?" The answer tells you whether it's core or satellite.

### 8. Plugins mount at timing points, not as subsystems

- Define fixed execution timing points (hooks)
- Plugins declare which point they care about; they don't control when they execute
- No plugin management framework
- No plugin registry

### 9. One structure, many purposes

Don't build different subsystems for different problems. Find a unified data structure that solves multiple needs simultaneously.

One less structure = one less category of synchronization bugs.

**Split boundary:** When a new use case requires twisting the core structure's semantics to work, that's when to split. Preserving structural semantics > minimizing structural count.

### 10. Code = configuration

Internal tools don't need a configuration system. Declarative API beats YAML / JSON / env-var assembly.

---

## Decision Discipline

### 11. Evidence threshold

Every removed feature has explicit "bring it back" conditions: how many use cases, how many users, what pain point. Not "never add it." Means "add it when there's evidence."

**Testing corollary:** Tests that exercise deprecated paths are safety nets, not evidence. When validating a new architecture, every test must exercise the new API surface. Backward-compat tests prove nothing was broken; kernel-native tests prove the new design actually works.

### 12. Review must include a "cut" step

Reviews default to addition. Finding "what's missing" is easier than finding "what's extra."

**After every review, ask:**
- What was added?
- What can be removed?

### 13. AI adds; humans subtract

AI tends toward over-design, pattern-mapping, and not cleaning up. The human's core value isn't generating more design — it's judging which designs shouldn't exist.

**AI behavior rules:**
- After writing code, actively check for removable code, files, abstraction layers
- Don't keep unused code for "completeness"
- Don't introduce indirection layers "that might be useful later"

### 14. Docs growing = direction is wrong

Good design makes documentation shorter. If docs grow after every iteration, stop and ask why.

### 15. Deprecation must allow gradual migration

Breaking changes must let old and new coexist for at least one version cycle. User code shouldn't break all at once.

Every deprecated symbol must carry a scheduled removal version: `@deprecated(since="0.2", remove_in="0.4")`. Without a removal target, deprecated code becomes permanent dead weight. Backward compatibility is a safety net, not a storage room.

---

## Debuggability

### 16. System must make failure causes obvious

A failing composition must produce an error message that points to the specific primitive.

```
❌ "Something went wrong"
✅ "createUser() failed: email already exists (user_service.go:42)"
```

In a minimal system, user code is composed. If the system doesn't tell you which primitive failed and why, debugging cost turns "give primitives, let users compose" into punishment.

---

## Performance Boundary

### 17. Naive compositions shouldn't cause orders-of-magnitude performance penalties

If a common composition pattern is more than 3x slower than a hand-rolled solution, the system should provide a more efficient composition path rather than forcing users to bypass the system.
