# Order Recovery — Walmart

Use this when the basket already failed in the real world. Update
`<state_root>/order-log.md` only with user consent.

## Missing item

- Check whether the item was canceled, substituted, delayed, or never packed.
- Reclassify the item: must-have now, can wait, or replace locally elsewhere.
- Update the order log if the same item fails repeatedly.

## Bad substitution

- Record exactly what went wrong: size, flavor, ingredient, or brand mismatch.
- Move that item into `strict match only` if the failure would predictably
  repeat.
- Offer the next safer rule, not just a refund path.

## Damaged or spoiled delivery

- Separate refund action from planning action.
- Replace perishables on the fastest path and move non-urgent items to the next
  basket.
- Add timing notes if late delivery likely caused the damage.

## Split shipment surprise

- Tell the user which items are still pending and which part of the order is
  complete.
- Rebuild the next basket around the real gap, not the original plan.
- Set expectations for one-window fulfillment for categories that repeatedly
  split.

## Slot or timing failure

- Recheck urgency and simplify the basket if the delivery window tightened.
- Protect must-have and cold-chain items first.
- Drop optional items rather than risking a full order miss.

## Recovery handoff order

1. Open the order detail / Chat with Shopper path the user can confirm.
2. Capture what failed without storing payment or prescription identifiers.
3. Rebuild the next basket around must-haves still missing.
4. Tighten substitution rules before the next apply.
