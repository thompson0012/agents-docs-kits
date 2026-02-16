---
name: self-cognitive
description: Use when the user asks for a confidence check, sanity check, retrospective, postmortem, lessons learned, or to make a workflow repeatable or persistent.
---

# Self-Cognitive Meta Skill

## Overview
Provide a structured self-cognitive response that verifies reasoning, captures lessons, and produces persistable updates.

## Modes
Choose the smallest set of modes that match the request:
- **Preflight Verification**: before execution or decisions.
- **Postflight Retro**: after work is done or after errors.
- **Skill Extraction**: when the user wants persistence or repeatability.

## Core Rules
- Separate facts from assumptions.
- State risks and how to validate quickly.
- Calibrate confidence (low/medium/high) with evidence.
- Never include secrets or sensitive data in any output.
- Keep outputs concise; prefer bullets.
- Always include the JSON artifact.
- If the template grows, move detailed guidance to `references/` and keep this file lean.

## Iteration Loop (Revolve)
Use an iterative loop to strengthen outputs over time:
1. Draft with the required template.
2. Compare against the required sections and JSON artifact.
3. Capture rationalizations or omissions.
4. Update the skill update proposal accordingly.
5. Re-run pressure scenarios until compliant.

## Required Output Template

## Goal
One sentence describing what is being verified or improved.

## Current context
- Bullet facts from the conversation.

## Verification
### Assumptions
- ...

### Risks and failure modes
- ...

### Checks
- ...

### Confidence
- Level: low | medium | high
- Why: ...
- To raise confidence:
  - ...

## Lessons learned
### Technical
- ...

### Process
- ...

### Prompting and coordination
- ...

## Persistable updates
### Memory summary
- User preferences:
  - ...
- Project facts:
  - ...
- Open questions:
  - ...

### Skill update proposal
If a target skill exists, propose minimal patch text.
If no target skill exists, propose a new skill outline and frontmatter suggestions.

### Artifacts JSON
```json
{
  "self_cognitive_meta": {
    "goal": "",
    "context_facts": [],
    "verification": {
      "assumptions": [],
      "risks": [],
      "checks": [],
      "confidence": {
        "level": "low",
        "why": "",
        "to_raise": []
      }
    },
    "lessons_learned": {
      "technical": [],
      "process": [],
      "prompting_and_coordination": []
    },
    "memory_summary": {
      "user_preferences": [],
      "project_facts": [],
      "open_questions": []
    },
    "skill_updates": {
      "target_skill_name": null,
      "proposed_patch": null,
      "new_skill_drafts": []
    }
  }
}
```

## Common Mistakes
- Skipping the verification section to save time.
- Omitting the JSON artifact.
- Mixing assumptions with facts.
- Declaring confidence without evidence.
- Treating the first draft as final instead of iterating.

## Rationalization Table
| Excuse | Reality |
|---|---|
| "We’re in a rush, skip verification." | Speed is not a reason to omit required sections. |
| "We already wrote most of it." | Sunk cost doesn’t replace RED/GREEN/REFACTOR. |
| "High-level is enough." | The template is mandatory regardless of brevity. |
| "One pass is enough." | Iteration is required to close gaps and strengthen compliance. |

## Red Flags — STOP and Restart
- “Skip verification to move faster.”
- “I’ll add lessons learned later.”
- “This is too simple to structure.”
- “No JSON needed.”

Violating the letter of the rules is violating the spirit of the rules.

## Example (concise)

## Goal
Validate whether the deployment plan is safe to execute today.

## Current context
- Deployment touches auth config and rate limits.

## Verification
### Assumptions
- Rate limit change is backward compatible.

### Risks and failure modes
- Auth flow could reject valid tokens.

### Checks
- Dry-run staging deploy and login.

### Confidence
- Level: medium
- Why: staging verified, no prod traffic tested
- To raise confidence:
  - Run canary on 5% traffic

## Lessons learned
### Technical
- Staging coverage missed token edge case.

### Process
- Add token-matrix checklist to deploys.

### Prompting and coordination
- Ask for rollout window upfront.

## Persistable updates
### Memory summary
- User preferences:
  - Wants explicit confidence levels.
- Project facts:
  - Auth uses token rotation.
- Open questions:
  - Canary tooling availability

### Skill update proposal
- Draft a rollout-checklist skill if repeated.

### Artifacts JSON
```json
{
  "self_cognitive_meta": {
    "goal": "Validate whether the deployment plan is safe to execute today.",
    "context_facts": ["Deployment touches auth config and rate limits."],
    "verification": {
      "assumptions": ["Rate limit change is backward compatible."],
      "risks": ["Auth flow could reject valid tokens."],
      "checks": ["Dry-run staging deploy and login."],
      "confidence": {
        "level": "medium",
        "why": "staging verified, no prod traffic tested",
        "to_raise": ["Run canary on 5% traffic"]
      }
    },
    "lessons_learned": {
      "technical": ["Staging coverage missed token edge case."],
      "process": ["Add token-matrix checklist to deploys."],
      "prompting_and_coordination": ["Ask for rollout window upfront."]
    },
    "memory_summary": {
      "user_preferences": ["Wants explicit confidence levels."],
      "project_facts": ["Auth uses token rotation."],
      "open_questions": ["Canary tooling availability"]
    },
    "skill_updates": {
      "target_skill_name": null,
      "proposed_patch": null,
      "new_skill_drafts": ["rollout-checklist"]
    }
  }
}
```
