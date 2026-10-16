# Basket Workflows — Walmart

Use the smallest workflow that matches the request. Always attach a needed-by
window before optimizing for savings.

## Weekly stock-up

- Start from household size, meal plan, and staple thresholds.
- Split the basket into `must-have`, `replaceable`, and `nice-to-have`.
- Mark items that can tolerate substitutions before checking value.
- Review unit value only after basket coverage is solid.

## Urgent top-off

- Optimize for speed and reliability, not perfect savings.
- Keep the basket short and protect items needed in the next 24 hours.
- Warn the user about mixed shipping items unless the user accepts split
  fulfillment.

## Repeat reorder

- Pull from prior successful baskets and confirmed staple rules under
  `<state_root>/`.
- Ask what changed since the last order: budget, schedule, guests, diet, or
  inventory.
- Revalidate any item with a history of bad substitutions or stock issues.
- Prefer Purchase History / My Items entry points before rebuilding manually.

## Mixed basket

- Flag grocery, general merchandise, and regulated items separately.
- Tell the user when the basket may split into pickup, shipping, or delayed
  components.
- Keep cold-chain and pharmacy-adjacent items on the tightest timing path.

## Output shape

For every serious basket recommendation, return:

- basket mode and needed-by window
- must-have items
- replaceable items with fallback logic
- optional items that can drop if stock or budget breaks
- final warning list: split shipping, sensitive substitutions, timing risks
