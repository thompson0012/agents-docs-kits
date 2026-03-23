---
name: prompt-augmentation
description: Use when a sparse or under-specified prompt for text, image, or video generation needs enrichment, clearer direction, or useful variants while preserving the user's core subject.
---

# Prompt Augmentation

Use this skill when the prompt is too thin to drive good generation, but the underlying subject is already present. Enrich the prompt; do not redesign the whole prompt architecture.

## Boundary

This skill expands generation prompts. It does not design system prompts, multi-turn agent instructions, or broader prompt architecture. Route that work to `meta-prompting`.

## Workflow

### 1. Classify the mode

Identify the target mode from the request:

- text-to-image
- text-to-video
- text-to-text generation

If the mode is unclear and would change the output materially, ask or state the assumption before finalizing.

### 2. Preserve the core subject

Lock the user's non-negotiables before expanding:

- main subject, actor, or scene
- intended action or outcome
- explicit constraints already present
- any named style, medium, or audience the user already chose

Do not swap the subject for a different idea. Add specificity without changing what the prompt is about.

### 3. Expand the right dimensions

Add only details that improve controllability.

For image or video prompts, consider:

- subject attributes and composition
- setting, time, weather, or environment
- lighting, color, and mood
- camera, lens, framing, or perspective
- style, material, or rendering cues
- motion, pacing, or transitions for video
- quality or format cues when they help rather than clutter

For text generation prompts, consider:

- role or voice
- audience and context
- objective and success criteria
- constraints, tone, and output shape

### 4. Build useful variants

When variants help, produce a small set with meaningful distance, for example:

- grounded or literal
- cinematic or expressive
- stylized or highly directed

Keep the same core subject across variants. Change direction, emphasis, or intensity, not the user's underlying idea.

When the target workflow uses positive and negative prompts, write both as plain strings. Negative prompts should remove likely failure modes, not ban desired elements.

### 5. Run a contradiction audit

Before delivering, silently check for:

- style conflicts or mutually exclusive cues
- negatives that exclude desired content
- missing spatial, temporal, or audience context
- overwritten core-subject details
- redundant filler that adds length without control

Patch contradictions before output.

## Delivery

Default to portable output:

- a single enriched prompt when one answer is enough
- labeled variants when comparison helps
- optional negative prompts when the target workflow supports them

Use plain strings by default. Use tables, bullets, or JSON only when the user or runtime actually benefits from structure.

## Quality Bar

A good augmented prompt:

- preserves the user's subject
- adds concrete control, not random decoration
- offers variants only when they are meaningfully different
- avoids contradictions and dead weight
- stays ready to paste into the target generation workflow
