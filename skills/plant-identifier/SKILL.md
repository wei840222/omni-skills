---
name: plant-identifier
description: Identify plants from photos using trait-based analysis. Use for plant IDs, lookalike triage, evidence-led follow-up captures, and approved reusable observation logs.
metadata:
  openclaw: '{"emoji":"🌿"}'
  related-skills: '{"image":"Inspects and improves plant photos before identification.","photography":"Improves close-up capture, lighting, and color reliability for plant evidence.","photos":"Organizes repeated observation photo sets.","plants":"Provides broader plant-care context after identification."}'
---

## State location

Plant Identifier state may exist in `<workspace>/plant-identifier/`, `<workspace>/memory/plant-identifier/`, or `~/plant-identifier/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured state root when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/plant-identifier/`, `<workspace>/memory/plant-identifier/`, `~/plant-identifier/`.
3. If multiple candidate directories exist, use only the highest-precedence directory and tell the user that multiple copies were found.
4. If none exists and the user approves saving state, create `<workspace>/plant-identifier/` and use it for the invocation. If the host cannot provide `<workspace>`, ask for a state root before creation.

Use the selected `<state_root>` for every state operation in this invocation; do not merge or synchronize other candidate directories.

## When to Use

Use for a photo-based plant ID, similar-species triage, a recurring houseplant or wild observation, or guidance on the next diagnostic image. Route general care after identification to the related `plants` skill.

## Quick Reference

- **Setup and consent**: On first activation or when state is incomplete, read `references/setup.md`.
- **Memory structure**: Before formatting an approved observation log, read `references/memory-template.md`.
- **Evidence checklist**: Before locking an identification result, read `references/evidence-guide.md`.

## Scope

This skill:
- identifies plants from visible traits in user-supplied images;
- returns one to three ranked candidates with explicit uncertainty;
- asks for the single most useful next photo when evidence is incomplete; and
- stores local observation notes only with user approval.

## Safety and Privacy

- Treat plant identifications as provisional until diagnostic traits are visible.
- For eating, touching, burning, or medicinal use, preserve an unresolved-safety status and direct the user to qualified local expertise for a decision.
- Keep image processing local and ask before writing any local observation data.

## Core Workflow

1. **Assess image quality and coverage.** Check for whole-plant view, leaves, flowers, fruit, stem, or bark. If the subject is distant, cropped, wilted, or mixed with other plants, request the highest-value missing view.
2. **Read `references/evidence-guide.md` and assess evidence in its stated order.** Work from growth habit through habitat context rather than using leaf color alone.
3. **Return a ranked, bounded result.** Give one to three candidates with High (85–95), Medium (60–84), or Low (35–59) confidence. Name supporting traits, missing traits, and the level of identification supported (species, genus, or family).
4. **Resolve conflict with a decisive next observation.** When candidates differ in genus or family, state the conflict and request the plant part that distinguishes them. For a possible toxic lookalike, treat the highest-risk candidate as the safety baseline until diagnostic evidence arrives.
5. **Handle high-stakes uncertainty.** If confidence remains low or use could cause harm, recommend qualified local verification; Pl@ntNet can supply an additional image-based hypothesis but does not replace such verification.
6. **Save only approved durable state.** After resolving `<state_root>`, read `references/memory-template.md` before creating an observation or preference record.

## Common Traps

- Leaf color alone is shared by many unrelated plants; combine diagnostic traits before ranking candidates.
- Houseplant stress damage can reflect environment rather than species identity.
- Missing leaf undersides, stem nodes, bark, flowers, or fruit can limit confidence.
- A tentative ID does not establish edibility, toxicity thresholds, or medicinal safety.
