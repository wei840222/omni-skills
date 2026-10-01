# Issue Recovery - Glovo

Use this order when something goes wrong.

## 1. Identify the exact state

Read the current Glovo page first:

- cart page
- checkout page
- live order tracking page
- support or order-history page

Verify the current state on screen before giving support advice.

## 2. Classify the problem

- missing or wrong item
- unavailable item or forced substitution
- courier delay
- address or contact problem
- payment failure
- cancellation or refund request

## 3. Respond by class

- **Missing or wrong item:** inspect the order record, item list, and support options before proposing refund language.
- **Unavailable item:** verify whether Glovo or the store substituted it and whether the total changed.
- **Courier delay:** check ETA drift before escalating.
- **Address problem:** verify whether the order can still be edited safely.
- **Payment failure:** verify whether a charge actually went through before retrying.

## 4. Save the durable lesson

After resolution, store only the reusable part under `<state_root>/`:

- store that frequently misses items
- promo that fails repeatedly
- address zone with slow delivery
- payment method that often gets rejected

Store only generalized incident summaries. Exclude receipts, transcripts, and payment details.
