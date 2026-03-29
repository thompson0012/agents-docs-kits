---
name: project-foundation
description: Use when turning a new product, service, workflow, or internal system idea into a staged blueprint with explicit scope boundaries, covered versus uncovered situations, business-value prioritization, and roadmap versions.
---

# Project Foundation

Use this skill to turn a vague or ambitious idea into a staged, commercially grounded, technically extensible project blueprint.

The goal is not hype and not a harsh startup teardown. The goal is a truthful plan for what to build first, what to defer, what the design already handles, and how it can grow without collapsing.

## Core Contract

- Preserve the full founding arc: clarify the problem, choose the wedge, define product 1.0, expose covered and uncovered situations, rank features by business value, and lay out roadmap versions.
- Separate long-term vision, current scope, and implementation details. Do not blur them together.
- Prioritize features by pain, willingness to pay or trust impact, urgency, implementation burden, and strategic leverage.
- State what is covered, partially covered, uncovered, and intentionally deferred. A polished omission is still a defect.
- Keep extensibility concrete: name the stable core, the variable layer, and the interfaces that preserve optionality.
- Do not replace `startup-pressure-test`. This skill designs the blueprint; it does not pretend to prove the business survives harsh market math.

## When This Skill Fits

Use it for:

- new products that need a clear first wedge
- internal tools or workflow systems that need staged scope and roadmap discipline
- ambitious ideas that risk overbuilding unless the plan is decomposed honestly
- product concepts that need a blueprint before PRDs, specs, sprint plans, or prototypes

Route away when:

- the real job is startup viability teardown, CAC/churn/runway stress, or investor-style skepticism
- AI or agent control surfaces are central enough that model behavior, override, latency, and budget design will shape the whole blueprint

## Workflow

### Phase 1 — Clarify the project and the wedge

Define:

- what the project is
- who it serves
- the job it helps them do
- why now matters
- why this first wedge is commercially acceptable now

Force one-sentence clarity. If the value cannot be explained plainly, the concept is still immature.

### Phase 2 — Map the pain and current environment

Capture the near-term world around the product:

- technology or workflow shifts that make the timing plausible
- adoption constraints and trust barriers
- economic, workflow, trust/compliance, technical, and adoption pain

Focus on current pain strong enough to earn adoption, not on fantasy future demand.

### Phase 3 — Define product 1.0 and the system spine

Specify:

- target user and primary use case
- must-have features and explicit non-goals
- the minimum stable core
- the variable layer expected to evolve
- the interfaces or contracts that preserve future expansion

Design for current adoption while preserving believable extension points.

### Phase 4 — Surface blind spots and robustness

Explicitly separate:

- covered situations
- partially covered situations
- uncovered situations
- intentionally deferred work

Then answer the robustness questions:

1. If usage grows 10x, what breaks first?
2. If a core assumption improves more slowly than hoped, does the project still matter?
3. If compliance, trust, or operational burden rises, can the design adapt?
4. If a competitor copies visible features, what remains defensible?

### Phase 5 — Re-rank by business value

For each capability or gap, decide whether to:

- build now
- reserve in architecture
- run as an experiment
- avoid entirely

Use business value, trust effect, strategic leverage, and implementation burden. Do not treat every uncovered case as a build ticket.

### Phase 6 — Build the staged roadmap

Produce at least these versions:

- v1.0 trusted wedge
- v2.0 operational strength
- v3.0 scale or governance
- long-term leverage

Each version should name the objective, user value, technical milestone, commercial milestone, and the signal that justifies moving to the next stage.

## Operating Lenses

Use these lenses only to sharpen judgment, not to duplicate the whole output.

- **Founder lens** — wedge, timing, business model, defensibility
- **Architect lens** — core layer, interfaces, extension points, failure boundaries
- **Operator or buyer lens** — trust, adoption friction, implementation burden, migration path

## Anti-Patterns

- platform before wedge
- architecture theatre without a real user or buyer
- feature inflation from every uncovered case
- vision collapse where short-term pragmatism erases long-term direction
- vague extensibility claims with no interface boundary

## Output Template

Use this template literally.

```md
# Project Name

## Executive Framing
- What it is:
- Who it serves:
- Core problem solved:
- Why now:

## World Context
- Technology or workflow shifts:
- Adoption constraints:
- Trust or compliance constraints:
- Why this timing is plausible:

## Market Pain Map
### Economic pain
- ...

### Workflow pain
- ...

### Trust or compliance pain
- ...

### Technical pain
- ...

### Adoption pain
- ...

## Product Thesis
- We believe:
- Therefore this product should exist because:
- Its first valuable form is:

## Product 1.0 Definition
- Target user:
- Primary use case:
- Must-have features:
- Explicit non-goals:
- Why someone would adopt it now:

## System Blueprint
- Core layer:
- Variable layer:
- Interface layer:
- Data or control flow:
- Future extension points:

## Covered vs Uncovered Situations
### Covered now
- ...

### Partially covered
- ...

### Not yet covered
- ...

### Intentionally deferred
- ...

## Feature Prioritization by Business Value
| Capability | Pain / value reason | Effort or complexity | Decision |
| --- | --- | --- | --- |
| ... | ... | ... | Build now / Reserve / Experiment / Avoid |

## Roadmap
### v1.0 — Trusted wedge
- Objective:
- User value:
- Technical milestone:
- Commercial milestone:
- Exit criteria:

### v2.0 — Operational strength
- Objective:
- User value:
- Technical milestone:
- Commercial milestone:
- Exit criteria:

### v3.0 — Scale or governance
- Objective:
- User value:
- Technical milestone:
- Commercial milestone:
- Exit criteria:

### Long-term leverage
- Strategic destination:
- What becomes possible later:

## Robustness Questions
- 10x usage failure point:
- Slow-improvement assumption:
- Compliance or trust tightening:
- Copycat defensibility:

## Risks and Assumptions
- Adoption risks:
- Technical risks:
- Operational risks:
- Strategic risks:
- Assumptions to validate next:

## Next Recommendation
- Most logical next artifact or action:
```

## What Good Looks Like

A strong result makes the reader say:

- I understand what to build first.
- I understand what not to build yet.
- I can see which situations are already handled and which are still exposed.
- I can explain why the roadmap sequence makes business sense.
- I can extend the system later without rewriting the story of version 1.
