---
name: plants
description: Track houseplant care, watering, growth, and issues. Use when the user wants to add a houseplant, log care, plan seasonal routines, or diagnose common plant symptoms; do not use for outdoor garden planning.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌱"}'
---

## State location

Plant state may exist in `<workspace>/plants/`, `<workspace>/memory/plants/`, or `~/plants/`. Before reading or writing plant state, resolve `<state_root>` once: use an explicitly configured path when present; otherwise select the first existing candidate in that order. If none exists and the user asks to save plant data, default to `<workspace>/plants/`. Keep the selected root for the entire invocation; when more than one candidate exists, use only the highest-precedence root and tell the user instead of merging copies.

## Core workflow

1. Identify whether the user wants to add, log, plan, or diagnose a houseplant.
2. Resolve `<state_root>` before accessing records. Ask before creating or changing persistent records.
3. Load [Plant Care Records](references/care-records.md) for file layouts, logging, reminders, propagation, or archival. Load [Plant Health and Seasonal Care](references/plant-health.md) for species guidance or symptoms.
4. Use observations and care logs before proposing a diagnosis. Present watering intervals as conditions to check, not fixed calendar rules.
5. Record only confirmed user-provided facts. For uncertain health issues, explain likely causes, safe checks, and when professional help is appropriate.

## Operating boundaries

- Keep one Markdown record per plant at `<state_root>/plants/<plant-name>.md`; create optional folders and records only for requested features.
- For watering, inspect soil moisture, light, drainage, season, and the plant's condition before recommending action. Water when the relevant soil depth is dry rather than following an unverified interval.
- Preserve removed or deceased plant records by moving them to `<state_root>/archive/` with the known cause and lessons learned; do not silently delete history.
- For pest, fungal, or severe root-rot concerns, isolate the plant when practical and load the health reference for low-risk triage. Avoid representing a remote diagnosis as certain.

## Quick routing

| User intent | Load | Outcome |
|---|---|---|
| Add a plant, log watering, repot, propagate, or review history | [Plant Care Records](references/care-records.md) | A consistent record and care log under `<state_root>`. |
| Drooping, yellowing, pests, light, fertilizer, or seasonal care | [Plant Health and Seasonal Care](references/plant-health.md) | Condition-based checks and species-appropriate guidance. |
| Outdoor beds, zones, crop rotations, or harvest planning | `garden` skill | Keep this skill focused on houseplants. |
