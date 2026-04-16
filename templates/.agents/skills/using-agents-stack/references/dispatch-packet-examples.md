# Dispatch Packet Examples

These examples are copyable patterns for maintaining blind review, honest no-publish compound skips, and dispatch-frame mismatch handling.
They are guidance, not a second routing contract. If they conflict with `AGENTS.md`, the phase skill, or stronger durable evidence, those sources win.

## Blind review packet

```md
Reviewer packet:
- Artifact paths:
  - .harness/WORKSTREAM-014/contract.md
  - .harness/WORKSTREAM-014/runtime.md
  - .harness/WORKSTREAM-014/handoff.md
- Question: Does the implementation satisfy every contract acceptance id without out-of-scope changes?
- Criteria: reproduce the runtime, check each `AC-###`, record findings with severity and `duplicate_of`, fail closed on missing evidence.
```

## No-publish compound skip

```md
Compound outcome:
- Feature id: FEATURE-014
- Evidence path reviewed: .harness/WORKSTREAM-014/
- Verdict: skip_publish
- Reason: no decisive reusable lesson survives beyond this sprint; artifacts record only sprint-local corrections.
- Queue action: clear FEATURE-014 from compound_pending_feature_ids without inventing memory.md residue.
```

## Dispatch-frame mismatch handling

```md
Worker entry mismatch:
- Dispatch frame claimed: WORKSTREAM-014 awaiting_review
- Stronger durable evidence found: .harness/WORKSTREAM-014/review.md already exists and status.json phase is review_recorded
- Action: stop before writing, preserve truthful files, return control to orchestrator for state-update routing.
```
