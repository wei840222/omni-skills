# Memory Setup — Grocery

## Initial Setup

Create the resolved `<state_root>` directory, then create the files used below:

```bash
mkdir -p <state_root>
touch <state_root>/memory.md
touch <state_root>/pantry.md
```

## memory.md Template

Copy to `<state_root>/memory.md`:

```markdown
# Grocery Memory

## Household
<!-- Size, members, special notes -->
- Size:
- Members:

## Restrictions
<!-- Allergies, diets, strong dislikes -->

## Preferences
<!-- Brands, stores, typical quantities -->
- Primary store:
- Backup store:
- Quantities:

## Current List
<!-- Active shopping list -->

## Picky Eaters
<!-- Per-person restrictions within household -->

---
*Last: YYYY-MM-DD*
```

## pantry.md Template

Copy to `<state_root>/pantry.md`:

```markdown
# Pantry Inventory

## Fridge
| Item | Qty | Expires |
|------|-----|---------|

## Freezer
| Item | Qty | Expires |
|------|-----|---------|

## Pantry
| Item | Qty | Expires |
|------|-----|---------|

## Running Low
<!-- Items to restock soon -->

---
*Updated: YYYY-MM-DD*
```

## Optional Files

Use `<state_root>/stores.md` for store order and notes, and `<state_root>/history.md` for past purchases and patterns.
