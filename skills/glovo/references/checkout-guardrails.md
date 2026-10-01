# Checkout Guardrails - Glovo

Treat these actions as increasingly sensitive.

## Browse safe

- switching between category and store pages
- reading ETA, fees, minimums, and promo labels
- comparing stores without changing the cart

## Draft cart only if requested

- adding items to an empty cart
- editing quantities on a fresh draft
- testing substitutions or notes for a candidate order

If the cart already contains items, ask whether to preserve, replace, or merge before editing.

## Explicit confirmation required

Require explicit current-thread confirmation before:

- changing the delivery address
- clearing a non-empty cart
- applying a final promo that changes the total
- confirming payment and placing the order

## Final summary format

Before live checkout, confirm all of the following are visible on screen:

- store name
- items and quantities
- substitutions or special notes
- active delivery address
- ETA
- delivery fee, service fee, tip, and total
- payment method shown by Glovo

Proceed with a live order only after every line is confirmed and the user explicitly approves in the current conversation.
