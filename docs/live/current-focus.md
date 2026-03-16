# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Create the packaged `startup-pressure-test` skill in English from the supplied startup pressure-test prompt, turning it into a reusable agentic workflow with fact-checking, pessimistic benchmarks, interactive decision points, and a 180-day business simulation.

## Scope

- Add `templates/base/.agents/skills/startup-pressure-test/SKILL.md`.
- Encode trigger conditions in the frontmatter description for harsh business viability pressure tests around concrete startup ideas.
- Translate the workflow into English with stages for fact check, market scrutiny, launch simulation, user behavior, financial reckoning, and postmortem.
- Remove the generated placeholder resource files that are not needed for this skill.

## Constraints

- Keep the skill focused on commercial validation, not technical implementation guidance.
- Require fact-checking before the simulation proceeds.
- Preserve interactive decision points and allow open-text user strategies instead of forcing A/B/C choices.
- Do not commit from this task.

## Success Criteria

- `startup-pressure-test` exists under the packaged skill path.
- The skill frontmatter and body are in English and clearly encode when to use the skill.
- The body preserves the day-based pressure-test workflow and financial realism of the source prompt.
- The live docs record the completed work and verification state.