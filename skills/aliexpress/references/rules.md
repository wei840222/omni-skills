# AliExpress sourcing rules

Use these rules before recommending a purchase or a supplier. Thresholds below are working heuristics for comparing listings, not AliExpress platform law. Refund timing follows the order's Buyer Protection window.

## 1. Vendor evaluation beyond stars

Star rating alone is incomplete. Collect these five signals before calling a seller trustworthy:

| Signal | Warning sign | Positive indicator |
|--------|--------------|--------------------|
| Store age | <1 year | >3 years |
| Followers | <1000 | >10,000 |
| Response rate | <80% | >95% |
| Positive feedback | <95% | >98% |
| Photo reviews | Stock photos only | Real customer photos |

When the user asks "is this seller trustworthy?", require all five signals. If any signal is missing, say which one is missing and withhold the trust verdict.

## 2. Real cost calculation

The item price is not the landed cost. Compute:

```text
Landed Cost = Item Price + Shipping + Import Tax (if the destination threshold applies) + Payment Fee (2-3%)
```

- Shipping time on listings commonly spans a few days to several weeks; read the method on that listing.
- A "free shipping" badge often selects the slowest method. Confirm the stated delivery window before treating it as acceptable.
- AliExpress Standard Shipping and ePacket-style tracked methods are the usual middle tier. Use the listing's own estimate, not a memorized day count, as the promise to the user.

Import tax is destination-specific. The old "$150" cutoff is not a universal rule. Ask for the destination country when tax status is not already known.

## 3. Same product, different vendors

Before recommending a purchase, search the same product across vendors:

- Price can vary widely for visually identical items.
- Similar photos across stores often mean the same factory. Prefer the higher-rated store when photos match.
- A lower price plus thin review history is a test-batch risk, not an automatic bargain.

## 4. Dispute and refund timing

AliExpress Buyer Protection refunds an item that does not arrive, arrives damaged, or is not as described, inside the protection period shown for that order.

- Not received or lost in transit: use the guaranteed delivery window on the order detail page. File after that window, not merely because today's estimate passed.
- Item not as described, damaged, or short: the public Buyer Protection page says this is eligible within 15 days of receiving the item.
- Open the return/refund from My orders → order detail → Return/refund, and keep screenshots of the listing, tracking, and received goods.
- A partial refund can be the better recovery when a full dispute would miss the window or the evidence is thin.
- EU/EEA/UK statutory rights (including 14-day withdrawal and a minimum 2-year conformity right) sit beside, and are not replaced by, Buyer Protection.

Source: https://www.aliexpress.com/p/buyerprotection/index.html

## 5. Dropshipping bar

Load `references/dropshipping.md` for margin math. The sourcing bar for a resale supplier is stricter than a one-off personal buy: positive feedback at or above 98%, and store age of at least 2 years.

## 6. Scam patterns

Warn, with the evidence that triggered the warning:

- Price more than 50% below comparable listings: treat as bait-and-switch until a second vendor confirms the same goods.
- "Ships from a local warehouse" with no warehouse proof on the listing: treat the claim as unverified.
- A brand name at about 90% below typical retail: treat as counterfeit risk and prefer an unbranded equivalent.
- Empty-box risk: ask for tracking that includes delivery photos before closing the issue as received.

## Common traps and the check that replaces them

- Star rating only → collect store age, photo reviews, and response rate.
- Ignoring the shipping method → read the listing's delivery window; slow "free shipping" can be many weeks.
- Margin from item price alone → add shipping, payment fees, platform fees, and a return reserve.
- Filing a not-received refund on the estimate date → wait until the order's guaranteed delivery window has passed, and still file inside buyer protection.
- Treating a "Top Brand" badge as proof → verify store age, reviews, and price against other vendors.
