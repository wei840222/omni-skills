---
name: aliexpress
description: Evaluate AliExpress vendors, compare landed costs and dropshipping margins, and time buyer-protection refunds. Use when the user asks whether a seller is trustworthy, whether a price includes real shipping, or when to open a return or refund.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🛒"}'
  related-skills: '{"temu":"Compare a similar marketplace listing when the user is choosing between AliExpress and Temu.","inventory":"Record purchased goods, warranties, and claim evidence after an order is placed.","seo":"Shape a resale listing after sourcing is decided.","contracts":"Track a supplier agreement once terms move beyond a marketplace order.","alipay":"Handle Alipay payment integration; it does not evaluate AliExpress sellers."}'
---

## When to load

Load when the user is buying, sourcing, or dropshipping on AliExpress and needs a vendor check, a landed-cost figure, or a refund timing decision.

- **Vendor check**: Load `references/vendors.md` before calling a seller trustworthy, especially for orders over $20.
- **Rules and scams**: Load `references/rules.md` for the five-signal check, landed-cost formula, and scam patterns.
- **Dropshipping**: Load `references/dropshipping.md` when the user is reselling, not making a one-off personal purchase.

This skill gives sourcing judgment. It does not place orders, store credentials, or persist buyer notes.

## Quick reference

| Need | Load |
|------|------|
| Five-signal vendor check, landed cost, dispute timing | `references/rules.md` |
| Store metrics, review quality, image-search check | `references/vendors.md` |
| Supplier minimums, margin math, tracked shipping | `references/dropshipping.md` |

## Decision path

1. Name the job: one-off buy, vendor trust check, or dropshipping margin.
2. Load only the matching reference. Do not treat star rating as sufficient evidence.
3. For a purchase recommendation, compute landed cost and compare at least two vendors selling the same item.
4. For a missing parcel, use the order's own guaranteed delivery window before opening a not-received refund. A late estimate alone is not the filing trigger.
5. State the missing signal when evidence is incomplete, then stop the recommendation until that signal is supplied.

## Recovery

- If a cited shipping time or fee is not on the listing, ask for the listing's shipping method and price instead of inventing one.
- If buyer-protection eligibility is unclear, point the user to the order page and the Buyer Protection page rather than promising a refund.
- If the user wants a payment integration, switch to `alipay` or the relevant payment skill. This package does not sign API requests.
