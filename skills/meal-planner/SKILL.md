---
name: meal-planner
description: >
  Plan household meals with weekly menus, shopping lists, batch-cooking notes,
  budget targets, dietary restrictions, pantry checks, and leftover reuse. Use
  when the user asks to plan dinners for the week, build a shopping list from a
  menu, reduce food waste, track a food budget, coordinate household diets, or
  turn preferences plus inventory into a cookable plan. Prefer `cooking` for
  stove-side rescue, `recipe` for saving/scaling individual recipes, `grocery`
  for pantry/list logistics without menus, `calories`/`nutrition`/`dietitian`
  for macros/micros/clinical diets, and `daily-planner` for calendar timeboxing.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍽️","requires":{"config":["<state_root>/meal-planner/"]}}'
  related-skills: '{"cooking":"Stove-side technique and dish rescue once a meal is chosen.","recipe":"Capture, scale, and file individual recipes rather than the household week.","grocery":"Shopping-list and pantry logistics when no weekly menu is needed.","nutrition":"Micronutrient gaps and supplement/food-drug interactions.","calories":"Calorie and macro tracking after menus exist.","dietitian":"Clinical or therapeutic nutrition plans.","daily-planner":"Calendar and timeboxing for cook/shop blocks.","food":"Casual food logging and classification outside multi-day planning."}'
---

# Meal Planner

Turn household preferences, dietary restrictions, inventory, and budget into a
cookable weekly plan with linked shopping lists and batch-prep notes.

This skill is stateful. Runtime meal-planning data lives under a resolved
`<state_root>/meal-planner/` tree outside this package. Never write runtime
state into the skill tree.

## State location

Meal-planner preferences, weekly plans, recipes, shopping lists, inventory, and
memory are persistent user state. Resolve one `<state_root>` before any read or
write:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/meal-planner/`, `<workspace>/memory/meal-planner/`,
   `~/meal-planner/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable meal-planning state, create
   `<workspace>/meal-planner/` when `<workspace>` is available; otherwise ask
   for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the rest of the invocation.

Use the selected `<state_root>` for every meal-planner state path under
`<state_root>/meal-planner/` (`memory.md`, `weeks/`, `recipes/`, `shopping/`,
`inventory/`, `templates/`, `archive/`). Legacy `~/Clawic/data/meal-planner/`
and `~/clawic/meal-planner/` copies are migration sources only — move them into
the resolved `<state_root>/meal-planner/` when the user asks, and say in one
line that you moved them and from where. Skill resources stay under
`references/` and `assets/`; never treat the literal string `<state_root>` as a
filesystem directory name.

After resolving `<state_root>`, if this is first use or state is empty, read
`references/setup.md`. File formats live in `assets/data-templates.md`.

## Progressive disclosure

Load reference files only when the matching situation needs depth:

- first-run onboarding → `references/setup.md`
- shopping-list construction → `references/shopping-guide.md`
- batch cooking / component prep → `references/meal-prep.md`
- food-budget heuristics → `references/budget-tips.md`
- citation URLs and claim status → `references/sources.md`
- markdown templates → `assets/data-templates.md`

## When to use

- User wants a weekly or multi-day meal plan with breakfast/lunch/dinner slots
- User needs a shopping list generated from a plan and current inventory
- User wants batch-prep suggestions, leftover reuse, or waste reduction
- User is coordinating household diets, allergies, kid preferences, or guests
- User asks for a food-budget target while planning meals

Prefer other skills when:

| Ask | Prefer |
|-----|--------|
| Dish is bland/burnt/broken at the stove | `cooking` |
| Save/scale/convert one recipe | `recipe` |
| Grocery list/pantry only, no menu | `grocery` / `shopping` / `inventory` |
| Calories/macros | `calories` |
| Micronutrients / labs / supplements | `nutrition` |
| Clinical therapeutic diet | `dietitian` |
| Timebox cook/shop on a calendar | `daily-planner` |
| Casual “what did I eat” logging | `food` |

## Architecture

```text
<state_root>/meal-planner/
├── memory.md
├── weeks/
│   └── YYYY-WXX.md
├── recipes/
│   └── {recipe-name}.md
├── shopping/
│   └── YYYY-MM-DD.md
├── inventory/
│   ├── pantry.md
│   └── fridge.md
├── templates/
│   └── {template-name}.md
└── archive/
```

## Quick reference

| Situation | Play |
|-----------|------|
| First use / empty state | Resolve `<state_root>`, then `references/setup.md` |
| Plan next week | Read `memory.md` + inventory, write `weeks/YYYY-WXX.md` |
| Shopping trip | Diff plan vs inventory → `shopping/YYYY-MM-DD.md` via `references/shopping-guide.md` |
| Busy week | Component prep list via `references/meal-prep.md` |
| Budget pressure | Qualifying heuristics in `references/budget-tips.md`; never invent official USDA figures without a live source |
| Allergy / restriction change | Update `memory.md` before suggesting food |
| Leftovers / waste | Reuse planned leftovers; see EPA wasted-food guidance in `references/sources.md` |

## Core rules

1. **Check memory first.** Before planning, read
   `<state_root>/meal-planner/memory.md` for allergies, intolerances,
   preferences, household members, time budget, and spend targets.
2. **Restrictions are sacred.** Allergy and intolerance entries block a recipe
   before suggestion. Prefer substitutions only after confirming severity.
3. **Inventory before shopping.** Read
   `<state_root>/meal-planner/inventory/pantry.md` and `fridge.md` when
   present; do not duplicate stocked staples.
4. **Link every shopping item to meals.** Orphan list items are a waste risk.
5. **Plan for real life.** Leave 1–2 flex slots; include leftover reuse; keep
   weeknight prep time honest.
6. **Budget claims need sources.** Treat thrifty/moderate dollar bands as local
   heuristics unless a live official series is cited in `references/sources.md`.
7. **Stay in scope.** This skill plans and lists; it does not place grocery
   orders, store payment data, or give medical nutrition therapy.
8. **Consent for state writes.** Create or migrate state only after the user
   wants durable planning files; say what you wrote and where.

## Weekly plan format

```markdown
# Week YYYY-WXX

## Overview
- Budget target: $XXX (heuristic or user-stated)
- Dietary focus: ...
- Special events: ...

## Monday
**Breakfast:** ... | Prep: X min
**Lunch:** ... | Prep: X min
**Dinner:** ... | Prep: X min | Recipe: `recipes/meal.md`

## Batch Prep
- [ ] ...

## Shopping Needed
[Generated from meals above after inventory check]
```

## Recipe and shopping notes

Recipe cards and shopping-list section order live in
`assets/data-templates.md` and `references/shopping-guide.md`. Keep dietary
tags and substitutions next to ingredients when restrictions exist.

## Security and privacy

**Local-only data:** plans, recipes, shopping lists, inventory, and household
dietary notes under `<state_root>/meal-planner/`.

**This skill does not:**

- send meal data to external services
- access health apps or fitness trackers
- store payment information
- read files outside the resolved `<state_root>/meal-planner/` tree

**User control:** plain markdown files; the user may edit or delete
`<state_root>/meal-planner/` at any time.

## Scope

This skill only:

- resolves `<state_root>` and manages meal-planning markdown under
  `<state_root>/meal-planner/`
- builds weekly plans, shopping lists, batch-prep notes, and preference memory
- routes stove, recipe-collection, calorie, micronutrient, and clinical asks to
  peer skills

Outside scope: grocery checkout, medical nutrition advice, calorie coaching,
and calendar ownership.
