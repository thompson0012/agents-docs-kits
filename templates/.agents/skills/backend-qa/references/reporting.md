# Reporting

## Severity Levels
### Blocker
Release-stopping failure in a core backend workflow, trust boundary, or integrity guarantee.

Examples:
- primary API or job flow cannot reach the promised outcome
- data is lost, corrupted, duplicated, or leaked under realistic use
- auth or tenancy boundary is broken in a way that risks material harm
- failures cannot be diagnosed because the backend hides the truth of what happened

### Major
High-impact failure with real consumer or operator cost, but not total release stop by itself.

Examples:
- contract semantics are ambiguous enough that callers may mis-handle outcomes
- retry, queue, or webhook behavior is unreliable under common failure conditions
- observability is incomplete enough to slow triage or hide blast radius
- performance degrades sharply under realistic pressure with a plausible workaround

### Minor
Real defect with limited blast radius or low urgency.

Examples:
- secondary contract inconsistency with low current consumer impact
- noisy or incomplete logging that does not block diagnosis
- non-critical performance or operability issue outside the primary path

## Finding Classification
Classify each finding as one primary type:
- Code defect: implementation behavior is wrong for the intended contract.
- Contract gap: the system may behave consistently, but the public or operational contract is ambiguous, incomplete, or misleading.
- Environment issue: the validation was blocked or degraded by infrastructure, dependency, credential, or runtime conditions outside the code change.
- Product tradeoff: the behavior is intentional but carries an explicit user, operator, or risk cost that decision-makers should accept knowingly.

## Evidence to Capture
For every finding, capture:
- severity
- classification
- short title stating what failed
- exact request, event, or job input
- exact response, completion state, or observed side effect
- affected endpoint, consumer flow, worker, queue, or webhook path
- auth or tenant context when relevant
- before and after data state when integrity is in question
- supporting evidence: logs, traces, metrics, queue state, or quoted machine fields
- expected behavior versus observed behavior
- whether the issue is deterministic, intermittent, or condition-dependent

## Concise Backend QA Report Template
Use this shape:

```md
Severity: Blocker | Major | Minor
Classification: Code defect | Contract gap | Environment issue | Product tradeoff
Title: <short statement of failure>
Area: <endpoint, job, queue, webhook, or auth boundary>
Context: <auth state, tenant, payload shape, dependency conditions, load profile>
Steps:
1. ...
2. ...
3. ...
Observed: <what actually happened>
Expected: <what should have happened>
Evidence: <request/response pair, job id, log or trace id, metric, before/after state>
Blast Radius: <who or what is affected>
Notes: <scope, likely owner, workaround realism, or explicit unverified gap>
```

## What Not to Count as a Pass
Do not call the backend passed because:
- the code path looks correct
- one happy-path request succeeded once
- a retry eventually worked, but the caller could not tell what happened
- logs exist, but they cannot be tied back to the request or job under test
- the database looks fine after cleanup even though the live flow corrupted or duplicated state first
- the issue appears only under replay, duplicate delivery, slow dependencies, concurrency, or large input
- you did not verify a contract or invariant but assumed it from nearby behavior

## Reporting Discipline
- Report what was tested, what failed, and what remains unverified.
- Keep evidence attached to the exact request, job, or state transition where the claim matters.
- Separate confirmed defects from open questions and blocked checks.
- Do not soften severity because an operator workaround exists unless the workaround is realistic, timely, and safe.
