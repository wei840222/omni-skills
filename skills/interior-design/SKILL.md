---
name: interior-design
description: Coordinate interior-design projects with space verification, supplier localization, material estimates, staging, and staged decision-making. Use when a user requests help planning, furnishing, or presenting an interior space.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏠"}'
---

## State location

Interior-design state may exist in `<workspace>/interior-design/`, `<workspace>/memory/interior-design/`, or `~/interior-design/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/interior-design/`, `<workspace>/memory/interior-design/`, `~/interior-design/`.
3. If none exists and the user explicitly wants persistent project tracking, create `<workspace>/interior-design/` only when a host-provided workspace is available; otherwise request an explicit state path.

If multiple candidate directories exist, use only the highest-precedence directory, tell the user that duplicate state was found, and do not merge, cross-read, or cross-write the others. Use the selected `<state_root>` for every state operation in this skill.

## When to use

Use for renovation planning, furniture selection, material estimates, rental or sale staging, interior photography preparation, and room-specific layout questions. Do not create state for one-off advice; create it only after the user asks to track a project.

## Core workflow

1. Classify the request: layout, materials, style, staging, photography, or room-specific planning.
2. For a layout or product recommendation, gather room dimensions, ceiling height, doors, windows, fixed elements, access route, budget tier, region, and items that must remain.
3. Load the matching reference from the table below. Treat its measurements and cost guidance as preliminary planning inputs; verify local code, manufacturer requirements, accessibility needs, availability, and installer constraints before a purchase or physical work.
4. Compare options against the stated constraints and explain assumptions, trade-offs, and the next verification step.
5. For structural, electrical, plumbing, gas, fire-safety, accessibility, permit, or hazardous-material work, identify the local authority or qualified professional needed before recommending execution.
6. Persist confirmed preferences only after the user opts into tracking; then use `<state_root>` and `references/memory-template.md`.

## Project state

```text
<state_root>/
├── memory.md          # Active project and confirmed preferences; create after tracking is enabled
├── spaces/            # Per-room dimensions and constraints; create when a room is tracked
├── suppliers.md       # Verified local suppliers and price tiers; create when supplier research is saved
└── archive/           # Completed projects; create when a project is archived
```

## Reference guide

| Topic | File | Load when |
|---|---|---|
| Project memory | `references/memory-template.md` | Creating or updating opted-in project state |
| Measurements and quantities | `references/calculations.md` | Estimating materials, fit, circulation, or budget assumptions |
| Style direction | `references/styles.md` | Identifying or combining styles |
| Sale and rental staging | `references/staging.md` | Preparing a property for listing, viewing, or guest use |
| Photography | `references/photography.md` | Planning a shot list, lighting, or photography briefing |
| Room-specific planning | `references/spaces.md` | Working on a living room, kitchen, bedroom, bathroom, or office |
| Constraints and decision traps | `references/rules.md` | Before a layout, product, or staging recommendation |

## Scope and safeguards

- Provide advisory planning, calculations from supplied measurements, and comparisons within stated constraints.
- Confirm explicit style preferences rather than inferring them from silence.
- Confirm the user's region and real availability before naming a purchasable product or supplier.
- Keep purchasing, supplier contact, contracts, permits, and physical execution with the user or an authorized professional.
- Keep `SKILL.md` read-only. Store opted-in project information only under `<state_root>/`.
