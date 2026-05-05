---
name: dynamic-problem-solving
description: Use when the user has already stated a specific decision, diagnosis, or question and needs rigorous multi-lens analysis of a clearly defined complicated problem.
---

# Dynamic Problem Solving

Use this skill to analyze a **defined** problem with 2-4 deliberately chosen lenses, force those lenses to collide, and end in a specific action or decision.

This is a nested child under `using-reasoning`; its path is `using-reasoning/dynamic-problem-solving/`, and the router selects it before standalone use.

For lens details, read:

- `references/lens-library.md`
- `references/bias-inventory.md`

For a compact reminder, use:

- `assets/quick-invoke-template.md`

## Core Contract

- Start only after the problem is stated clearly and solution-neutrally.
- Analyze with **2-4 lenses**, never more.
- Pair at least one **human lens** with one **structural lens**.
- Treat disagreement between lenses as signal, not noise.
- End with a concrete recommendation, tradeoff statement, and disconfirming test.
- Do not manufacture certainty when the domain does not support it.

## Entry Gate

### Gate 1 — Problem quality

Proceed only if the problem can be restated in one or two sentences.

If not, stop and say:

> Before analysis can begin, define the problem in one sentence: what specifically needs to be decided, diagnosed, or understood?

Then route to `using-reasoning/problem-definition`.

### Gate 2 — Problem domain

Classify before analyzing.

```text
SIMPLE       -> known best practice exists; apply it directly
COMPLICATED  -> expert analysis adds value; proceed with this skill
COMPLEX      -> cause and effect are emergent; run small experiments instead
CHAOTIC      -> stabilize first; analyze later
```

Only **COMPLICATED** problems proceed.

## Workflow

### Phase 0 — Frame the Problem Before Choosing Lenses

Capture the minimum framing needed to avoid shallow analysis.

#### 0a. Intuition record

Record the first instinct before structured reasoning overwrites it.

```text
First instinct:
Emotion present:
What that emotion may be signaling:
```

#### 0b. Core classification

Classify the problem on these dimensions:

- **Type**: decision, diagnosis, prediction, design, negotiation
- **Stakes**: reversible or irreversible
- **Time tier**:
  - T1: under 1 hour
  - T2: under 1 day
  - T3: over 1 day
- **Uncertainty**: known, unknown, unknowable
- **Core tension**:
  - human vs human
  - human vs system
  - resource vs goal
  - short-term vs long-term

#### 0c. Stakeholder map

Name:

- who is affected
- who holds decision power
- who has information you lack
- whose incentives are misaligned
- who will actively resist the outcome

#### 0d. Attachment check

Watch for:

- a preferred answer already chosen
- money, reputation, identity, or relationships tied to one outcome
- strong emotion concentrated on one option

If attachment is high:

- restate the problem in third person
- treat the preferred answer as a hypothesis
- if the tone is defensive or anxious, run `using-reasoning/thinking-ground` before continuing

#### Required framing output

Produce one sentence in this pattern:

```text
This is a [TYPE] problem with [REVERSIBILITY] stakes, [TIME TIER] timing,
[UNCERTAINTY] uncertainty, centered on [TENSION], with likely resistance from [STAKEHOLDERS].
```

### Phase 1 — Select the Minimum Lens Set

Choose 2-4 lenses using the routing logic below.

```text
Bottlenecks or operational design    -> Engineering
Compliance, liability, regulation     -> Legal / Regulatory
Competition or adaptation            -> Biology / Ecology
Feedback loops or long-term effects  -> Systems Dynamics
Human behavior involved              -> Psychology
Incentives or allocation matter      -> Economics
Multiple strategic actors            -> Game Theory
No precedent / assumptions suspect   -> First Principles
Precedent, pattern recognition       -> History / Analogical Reasoning
Relationship-heavy / high-context    -> Relationship Dynamics
Risk, probability, forecasting       -> Probability & Statistics
Signal degradation, communication breakdown -> Information Theory
UX, adoption, unmet needs            -> Design Thinking
Values or legitimacy conflict        -> Philosophy
```

Selection rules:

1. Hard cap at four lenses.
2. Include one human lens and one structural lens whenever humans are involved.
3. If every selected lens points to the same answer too quickly, add one adversarial lens.
4. T1 decisions use at most two lenses.
5. First Principles can override the initial set when every other lens depends on questionable assumptions.
6. Match depth tier to time tier: T1 uses Basic prompts, T2 uses Intermediate, T3 uses Advanced.
7. Check contraindication before confirming each lens. If any contraindication matches the problem, either drop the lens or pair it with one that covers its blind area.

### Phase 2 — Apply Each Lens Independently

Do not blend lenses yet.

For each chosen lens, answer:

1. What mechanism does this lens highlight?
2. What evidence supports that mechanism here?
3. What does this lens imply should happen next?
4. What would disconfirm this reading?
5. What is this lens likely to miss?

Use the lens library for the relevant prompts and failure modes.

### Phase 2.5 — Extract and Test Transfer

> Run this phase only when the user is explicitly asking for reuse, analogy, transfer, or cross-domain innovation, or when First Principles reveals a mechanism that is likely to transfer beyond the original context.

Keep it short and structural:

1. Separate the **surface phenomenon** from the **causal mechanism** actually doing the work here.
2. Restate that mechanism as a portable **meta-principle** in object-agnostic terms, consistent with First Principles thinking.
3. Generate **3 candidate transfers** that are structurally similar but superficially different.
4. Test each candidate for **physics, constraints, incentives, and resource mismatch**.
5. Name the **disconfirming case** for each candidate and discard weak fits before moving on.

If no transfer survives contact with reality, say so explicitly and continue with the normal collision step.

### Phase 3 — Force Collision

After independent passes, compare the lenses directly.

#### 3a. Agreements and Contradictions

- Where do the lenses agree?
- Where do they contradict each other?

#### 3b. Conflict Resolution Ladder

Apply these layers in order. Stop when any layer resolves the contradiction.

##### Layer 1 — Evidence Weighting

For each lens's conclusion, answer:
- Is this based on observed behavior/data or inferred mechanism?
  → If based on data, weight +1
- Does this conclusion have base-rate support from similar cases?
  → If supported, weight +1
- Has this conclusion ruled out the most obvious alternative explanation?
  → If yes, weight +1

Output the scores. The lens with the highest evidence weight takes priority.
Record each defeated lens's warning signals as risk items to preserve downstream.

##### Layer 2 — Assumption Strip

Run only if Layer 1 left unresolved contradictions (scores tied or all scores low).

For each conflicting lens:
- What must be true for this lens's conclusion to hold?
- Which of those conditions are verified? Which are assumed?

The lens depending on fewer unverified assumptions wins.

If any lens's conclusion rests entirely on unverified assumptions, downgrade its status from "finding" to "inference."

##### Layer 3 — Testability Check

Run only if Layers 1-2 left contradictions unresolved.

For each conflicting lens:
- Does its conclusion produce an observable, testable prediction?
- How quickly and cheaply can that prediction be verified?

When unable to determine which lens is correct, adopt the lens whose conclusion is fastest to falsify. This is not because it is more likely true, but because being wrong costs least.

##### Layer 4 — Decision Path

Run only if all three previous layers failed to resolve the contradiction.

Output three paths instead of one answer:
- **Safe path (conservative):** adopt the lowest-common-denominator recommendation across all lenses
- **Aggressive path (optimistic):** adopt the lens with strongest evidence weighting despite unresolved contradictions
- **Hedge path (option-preserving):** keep two lenses' predictions alive and prepare for both

For each path, state:
- Under what conditions this path would be optimal
- The trigger signal that would make you switch to another path

#### 3c. Boundary Scan

Look for what the current lenses may still ignore:

- outside-view base rates
- unknown stakeholders
- cultural or relationship dynamics
- hidden constraints
- second-order effects
- unknown unknowns revealed by an outsider or novice question

#### 3d. Mirror-Imaging Check

If your explanation of another actor depends on motives they have not shown, label it as inference, not fact.

### Phase 4 — Synthesize Into a Decision

Turn the collision into an action-oriented synthesis.

Include:

- the best current recommendation or decision
- the tradeoff being accepted
- the single most dangerous assumption
- what would most likely make the recommendation wrong
- the first test, experiment, or action
- what not to do next

Decision rules:

- **Reversible** -> bias toward action, then update quickly.
- **Irreversible** -> test the most dangerous assumption before commitment.
- **Unknown uncertainty** -> preserve optionality.
- **Unknowable uncertainty** -> use scenarios, not point forecasts.

### Phase 5 — Calibrate

Before finishing, compare the synthesis against the initial intuition.

Ask:

- Did the analysis confirm or overturn the first instinct?
- If it confirmed it, what evidence prevented rationalization?
- If it overturned it, what was missed at first glance?
- Does the answer feel hollow because the reasoning is weak, or because this problem should not be solved analytically at all?

If the work feels hollow, performative, or defended, route through `using-reasoning/thinking-ground` before giving final confidence.

## Output Format

Return these sections:

### Problem Restatement
- one or two sentences

### Framing Summary
- type, stakes, time tier, uncertainty, tension, stakeholders

### Selected Lenses
- 2-4 bullets with one-line justification each

### Lens Findings
- one subsection per lens
- mechanism, evidence, implication, disconfirming signal

### Transfer Candidates
- optional; include only for reuse, analogy, or cross-domain requests
- surface phenomenon vs causal mechanism
- portable meta-principle
- 3 candidate transfers, each with fit, boundary, and disconfirming case


### Collision
- agreements
- contradictions
- conflict resolution: which layers triggered and what they resolved
- dominant tension
- boundary-scan findings

### Recommendation
- concrete decision or next action
- tradeoff accepted
- most dangerous assumption
- first test
- what not to do next
- confidence level with reason

### If We Are Wrong
- 2-4 bullets describing the most plausible failure paths

## Failure Modes to Avoid

- starting before the problem is truly defined
- using too many lenses and calling it rigor
- confusing elegant language with strong reasoning
- forcing a complicated-style answer onto a complex or chaotic situation
- skipping disconfirming evidence
- treating stakeholder motives as facts without evidence
- ending with analysis instead of action
