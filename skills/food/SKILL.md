---
name: food
description: >
  Classify and organize food inputs (meal photos, nutrition labels, recipes,
  menus, and text logs) into preferences, products, patterns, places, and
  recipes. Use when logging food, scanning labels, saving recipes, tracking
  restaurants or inventory, reviewing weekly eating patterns, or flagging
  dietary restrictions. Not for detailed calorie/macro coaching (`calories`),
  clinical diet plans (`dietitian`), multi-day meal planning (`meal-planner`),
  or pure pantry stock lists without food classification (`inventory`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍽️"}'
  related-skills: '{"calories":"Detailed macro, TDEE, and label math after food is classified.","dietitian":"Clinical or therapeutic nutrition plans beyond casual logging.","habits":"Turns recurring meal or prep routines into trackable habits.","inventory":"Pantry or fridge stock lists when classification is already done.","journal":"Free-form food notes outside structured food memory.","meal-planner":"Multi-day meal plans once preferences and inventory are known."}'
---

## State location

Food state may exist in `<workspace>/food/`, `<workspace>/memory/food/`, or `~/food/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/food/`, `<workspace>/memory/food/`, `~/food/`.
3. If none exists and the user wants persistent tracking, create `<workspace>/food/`. If `<workspace>` is unavailable, ask for a state root instead of guessing from the current directory.
4. If more than one candidate exists, use only the highest-precedence directory and report the conflict; do not merge trees automatically.

Use the selected `<state_root>` for every state operation in this skill. Prefer portable `<state_root>` paths; never hard-code host-specific absolute roots. Skill resources stay under `references/` and `assets/`; never treat the literal string `<state_root>` as a filesystem path.

```text
<state_root>/
└── memory.md   # Preferences, products, patterns, places, recipes
```

Create or update state only after the user opts in. Store high-signal food memory only—no medical diagnoses, no full health records.

## When to use

Load for **food classification and personal food memory**:

- Log a meal from photo or text
- Scan a nutrition label or barcode photo into reusable products
- Save a recipe from photo or text
- Capture restaurant or menu context
- Record allergies / exclusions permanently and flag conflicts
- Weekly variety, timing, and eating-out pattern insights

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| Detailed macros, TDEE, cut/bulk targets | `calories` |
| Clinical / therapeutic diet planning | `dietitian` |
| Multi-day meal planning | `meal-planner` |
| Pure pantry stock without classification | `inventory` |
| Free-form notes outside food memory | `journal` |
| Habit streaks for prep or meal routines | `habits` |

## Core rules

1. Auto-detect input type: meal photo, nutrition label, recipe, menu, inventory photo, or text.
2. Extract items, portions when visible, context, and nutrition only when readable—state uncertainty ranges instead of fake precision.
3. Tag every entry: `#meal`, `#recipe`, `#product`, `#restaurant`, `#inventory`, `#preference` as appropriate.
4. Offer nutrition estimates conditionally ("Want a nutrition estimate?")—never force calorie theater on every log.
5. Remember restrictions permanently under Preferences and flag likely conflicts before the user eats.
6. Build a personal database of scanned products, frequent meals, places, and saved recipes in `<state_root>/memory.md`.
7. Provide insights only from stored entries: variety, meal timing, frequent foods, eating-out ratio; label estimates as non-medical.
8. For detailed macro coaching after classification, hand off to `calories`.

## Quick reference

Load only what improves the current answer.

| Need | File |
|------|------|
| Input-type routing and pipelines | `references/processing.md` |
| Memory sections and write rules | `references/memory.md` |
| Allergen / label safety defaults | `references/domain.md` |
| Continuity memory template | `assets/memory-template.md` |

## Security and privacy

- Opt-in local state only under the resolved `<state_root>/`.
- Prefer on-device classification of user photos; do not upload private meal photos to undeclared third parties without explicit consent.
- Store preferences and high-signal summaries only—no full medical charts.
- Nutrition estimates are informational, not medical advice or diagnosis.
