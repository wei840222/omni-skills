# Data Templates — Walmart

Copy these structures into the resolved `<state_root>/` only after the user
opts into durable memory. Never create a literal directory named `<state_root>`.

## memory.md

```markdown
# Walmart Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Household Scope
| Topic | Notes |
|------|-------|
| People served | [adults, kids, guests, pets] |
| Preferred store | [location or delivery area] |
| Default order mode | [pickup, delivery, shipping, mixed] |
| Weekly rhythm | [main stock-up day and top-off pattern] |
| Automation mode | [planning only, browser-assisted, marketplace api] |
| Preferred entry path | [Purchase History, My Items, fresh cart, seller workflow] |

## Basket Priorities
| Priority | Typical items | Notes |
|----------|---------------|------|
| Must-have | [milk, eggs, diapers] | Missing means the trip failed |
| Replaceable | [produce, snacks] | OK with bounded substitutions |
| Nice-to-have | [seasonal extras] | Drop first if budget or stock is tight |

## Substitution Rules
### Strict Match Only
| Category or item | Reason |
|------------------|--------|
| [baby formula] | brand/safety |
| [allergy-sensitive item] | medical risk |

### Flexible Substitutions
| Category or item | Allowed swap | Boundary |
|------------------|--------------|----------|
| [bananas] | same size / ripeness band | no overripe for baking-only unless asked |
| [paper towels] | equivalent sheet count | reject tiny multipacks sold as deals |

## Budget Guardrails
- Soft weekly ceiling:
- Hard never-exceed:
- Brands / packs to prefer for unit value:

## Pharmacy / Regulated Notes (operational only)
- Preferred pharmacy location:
- Pickup timing preference:
- Categories that must stay separate from grocery planning:
```

## weekly-cart.md

```markdown
# Weekly Cart — YYYY-MM-DD

mode: weekly-stock-up | urgent-top-off | reorder | mixed
needed_by: YYYY-MM-DD HH:MM / window
fulfillment: pickup | delivery | shipping | mixed
store_or_area:

## Must-have
| Item | Qty / size | Brand rule | Substitution |
|------|------------|------------|--------------|
| | | | none / bounded / flexible |

## Replaceable
| Item | Qty / size | Acceptable swap | Drop if |
|------|------------|-----------------|---------|
| | | | |

## Nice-to-have
| Item | Qty / size | Notes |
|------|------------|-------|
| | | |

## Risk flags
- Split shipping:
- Cold-chain:
- ID / age-restricted:
- Pharmacy-adjacent:
```

## order-log.md

```markdown
# Order Log

## YYYY-MM-DD — <order id or local label>
- Mode / window:
- Outcome: complete | partial | missing | substituted | damaged | split
- Missing / bad items:
- Substitution notes:
- Next-rule change:
```

## exceptions.md

```markdown
# Exceptions

## Never substitute
| Item / category | Reason | Owner confirmation date |
|-----------------|--------|-------------------------|
| | | |

## Always confirm before apply
- Address changes
- Checkout / place order
- Refill start
- Cancel / remove must-have items
```
