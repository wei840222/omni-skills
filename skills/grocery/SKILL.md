---
name: grocery
description: Build and manage grocery lists, pantry inventory, household quantities, and dietary-restriction checks. Use when the user wants to add, remove, organize, or review shopping items, pantry stock, or household buying preferences.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🛒"}'
  related-skills: '{"meals":"Use meals for weekly meal planning, recipes, and dietary balance; use grocery for ingredient purchasing, pantry inventory, and shopping-list logistics."}'
---

## When to Use

Use this skill for grocery-shopping logistics: creating or maintaining lists, tracking user-reported pantry inventory, remembering household quantities, and checking items against known dietary restrictions. For deciding what to eat or building a weekly meal plan, route to `meals`.

## State Location

Store persistent grocery data outside this skill package in `<state_root>/`. Resolve `<state_root>` in this order:

1. `${WORKSPACE_DIR}/.grocery` when `WORKSPACE_DIR` is set, otherwise `${CLAWIC_WORKSPACE}/.grocery` when `CLAWIC_WORKSPACE` is set.
2. `~/.local/share/grocery` on Linux or `~/Library/Application Support/grocery` on macOS.

Create the selected directory before writing. Keep all household data within this resolved directory.

```
<state_root>/
├── memory.md          # Preferences, restrictions, and current lists
├── pantry.md          # User-reported stock, quantities, and dates
├── history.md         # Past purchases and patterns
└── stores.md          # Preferred stores and aisle layouts
```

## Quick Reference

| Topic | Load when | File |
| --- | --- | --- |
| Memory and pantry setup | Creating or repairing household state files | `assets/memory-template.md` |
| List operations | Adding, removing, grouping, exporting, or reconciling list items | `references/lists.md` |
| Food-safety and allergen checks | Interpreting dates, storage, or ingredient labels for a stated restriction | `references/domain-knowledge.md` |

## Core Workflow

1. Read `<state_root>/memory.md` and `pantry.md` when they exist; otherwise create them from `assets/memory-template.md`.
2. Capture newly stated household size, dietary restrictions, stores, and typical quantities in `memory.md`.
3. Apply the requested list change using `references/lists.md`; deduplicate items and reconcile user-reported pantry stock.
4. Check requested items against recorded restrictions. For packaged food or uncertain ingredients, ask for the ingredient label rather than infer safety.
5. Return the organized list and explicitly identify substitutions, conflicts, or missing information.

## Scope

This skill maintains lists from user input, tracks user-reported pantry inventory, remembers household preferences and restrictions, and suggests household-appropriate quantities. It operates only on `<state_root>/` data and user-provided information; it does not query store inventory or prices, place orders, scan receipts, or access files outside the state directory.

## Common Traps

- Check household size before scaling recipe ingredients.
- Use the user’s preferred stores before suggesting unfamiliar or exotic ingredients.
- Load stored restrictions and pantry data before changing the list.
- When a recipe conflicts with a restriction, present a safe substitution or ask whether to omit the item.
- Treat a package’s ingredient label and allergy advisory as the source of truth for a product-specific allergen decision.
