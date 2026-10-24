---
name: food-delivery
description: "Manage food delivery ordering workflows. Use when selecting delivery platforms, applying dietary and budget filters, comparing fee structures, or managing reorders."
metadata:
  openclaw: '{"emoji": "🍕", "requires": {"bins": []}, "os": ["linux", "darwin", "win32"],
    "displayName": "Food Delivery"}'
---

## When to load

Load this skill when the user explicitly requests food delivery, asks for restaurant recommendations, or needs to manage household dietary preferences and delivery orders. bypass loading this skill for generic recipe generation or grocery shopping.

## State location

Food Delivery state may exist in `<workspace>/food-delivery/`, `<workspace>/memory/food-delivery/`, or `~/food-delivery/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/food-delivery/`, `<workspace>/memory/food-delivery/`, `~/food-delivery/`.
3. If none exists and state must be created, default to `<workspace>/food-delivery/`.

Use the selected `<state_root>` for every state operation in this skill.

Memory lives in `<state_root>/food-delivery/`.

```
<state_root>/food-delivery/
├── memory.md          # Core preferences, restrictions, defaults
├── restaurants.md     # Restaurant ratings, dishes, notes
├── orders.md          # Recent orders for variety tracking
└── people.md          # Household/group member preferences
```

See `assets/memory-template.md` for initialization.

## Quick Reference

| Topic | File |
|-------|------|
| Memory setup | `assets/memory-template.md` |
| Decision framework | `references/decisions.md` |
| Ordering workflow | `references/ordering.md` |
| Common traps | `references/traps.md` |

## Core Execution

1. Read `<state_root>/food-delivery/memory.md` to identify preferences and critical dietary restrictions.
2. Determine user context (time, occasion, group size).
3. Filter out options that violate restrictions or repeat recent orders (`<state_root>/food-delivery/orders.md`).
4. Consult `references/decisions.md` to finalize selection logic.
5. Execute the order using the workflow in `references/ordering.md`.
6. Avoid common pitfalls outlined in `references/traps.md`.

## Boundary constraints

- Maintain credit card numbers outside of state, exact addresses, or account passwords in state.
- Strictly enforce critical dietary restrictions.
