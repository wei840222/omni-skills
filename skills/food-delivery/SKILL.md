---
name: food-delivery
description: Manage end-to-end food delivery orders by learning preferences, filtering options based on state constraints, and optimizing across delivery platforms.
metadata:
  openclaw: '{"emoji": "🍕", "requires": {"bins": []}, "os": ["linux", "darwin", "win32"],
    "displayName": "Food Delivery"}'
---

## When to load

Load this skill when the user explicitly requests food delivery, asks for restaurant recommendations, or needs to manage household dietary preferences and delivery orders. bypass loading this skill for generic recipe generation or grocery shopping.

## State location

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
