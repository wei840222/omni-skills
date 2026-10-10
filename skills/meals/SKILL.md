---
name: meals
description: >
  Build and maintain a personal meal-planning system: weekly dinner/lunch plans,
  shopping lists from planned meals, pantry-aware aggregation, leftovers reuse,
  and a growing meal database of meals you actually cook. Use when the user wants
  a weekly meal plan, shopping list from meals, leftover strategy, batch-cook
  prep, or to save/rate past dinners. Prefer `calories` for food/calorie logging,
  `water` for hydration-only tracking, `shopping` for generic errands outside meal
  ingredients, and `cooking` for technique-focused recipe execution.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍽️"}'
  related-skills: '{"shopping":"Generic shopping lists and store runs beyond meal-ingredient aggregation.","cooking":"Technique and recipe execution once a meal is chosen.","calories":"Food and calorie logging rather than weekly meal planning.","water":"Hydration tracking separate from meal composition.","habits":"Recurring meal-prep or cook-night routines.","daily-planner":"Places cook nights into the day schedule.","health":"Broader health context when meal balance intersects care plans.","journal":"Free-form food notes outside structured meal records."}'
---

# Meals

Own **personal meal planning**: weekly plans, shopping lists from planned meals, pantry staples, leftovers, ratings, and a database of meals you actually cook—not aspirational recipe browsing.

## State location

Meal state may exist in `<workspace>/meals/`, `<workspace>/memory/meals/`, or `~/meals/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/meals/`, `<workspace>/memory/meals/`, `~/meals/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and state must be created, default to `<workspace>/meals/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/meals/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Do not treat the literal string `<state_root>` as a filesystem path. Do not write payment cards, delivery passwords, or unrelated secrets into meal files. Do not write learned preferences into `SKILL.md`.

Default layout (create files on first authorized write):

```text
<state_root>/
├── plans/           # weekly plans, e.g. 2026-W41.md
├── meals/           # one file per saved meal
├── shopping/        # generated lists keyed to a plan
├── preferences.md   # restrictions, dislikes, favorites, pantry staples
└── memory.md        # ratings, patterns, household size
```

If older meal files exist outside the candidate roots, offer a one-time migrate into the resolved `<state_root>/` and say in one line what moved; do not keep marketplace homepage links.

## Core behavior

- User plans their week → organize dinners/lunches under constraints (busy nights, guests, leftovers).
- Generate shopping lists → aggregate ingredients from the active plan; combine quantities; group by store section; subtract pantry staples.
- Track what works → save meals actually cooked with prep/cook time, servings, tags, and ratings.
- Balance variety → avoid the same main protein or cuisine several nights in a row unless the user intends repeats.
- Prefer repeats of rated favorites over inventing a new recipe every night.

## When the user plans meals

1. Ask how many dinners/lunches to plan and household size or guests.
2. Ask which nights are busy (need ≤30 min / one-pot / no-cook) vs flexible.
3. Load `<state_root>/preferences.md` and recent plans when present.
4. Draft a simple weekday list; mark takeout/leftover nights explicitly.
5. Offer shopping-list generation after the plan is accepted.
6. For deeper formats, batch cooking, ratings, and seasonal rules, read `references/domain.md`.
7. For verified plate-balance and food-safety boundaries, read `references/sources.md` before stating nutrition guidelines as fact.

## Failure and safety

- Missing preferences or empty meal DB: start with 3–4 simple dinners and ask one clarifying question at a time; do not invent allergies.
- Conflicting multi-root state: use highest-precedence root only; never merge silently.
- Nutrition claims: stick to plate-balance patterns from `references/sources.md`; do not prescribe medical diets or calorie targets here (`calories` owns logging).
- Food safety: leftovers and batch-cook guidance stays high-level; when unsure, prefer cooler storage and shorter keep windows and point to official FSIS/CDC pages in sources.
- Busy-night pressure: never push ambitious multi-component recipes; offer under-30 / one-pot / repeat-favorite first.

## Progressive disclosure

Depth on demand—load only the reference required for the current step.

| Need | Load |
| --- | --- |
| Meal DB fields, weekly format, shopping aggregation, pantry, leftovers, ratings, batch cook, seasonal cues | `references/domain.md` |
| Official plate-balance, leftovers safety, Agent Skills format URLs used this refactor | `references/sources.md` |
