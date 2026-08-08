---
name: sell
description: Help users sell personal items by researching prices, writing listings, selecting appropriate platforms, and handling offers safely. Use when the user wants to price, list, or sell an item, choose a selling platform, respond to a buyer, or assess a selling scam.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💵"}'
  related-skills: '{"ebay":"Platform-specific listing optimization and fee calculation for eBay sales.","etsy":"Handmade and vintage listing SEO and pricing on Etsy.","facebook-marketplace":"Local selling on Facebook Marketplace with scam detection.","negotiate":"Structured negotiation tactics for high-stakes buyer interactions.","shipping":"Carrier selection, customs, and delivery for shipped sales.","vinted":"Clothing resale on Vinted with bundle pricing and shipping."}'
---

Start with the item condition, sale timeline (speed versus net return), location, and willingness to ship. If the user is deciding how to respond to an offer, payment, address change, or meeting request, load `references/safety.md` before recommending a response.

When exact current comps, platform availability, fee terms, or payment eligibility are unavailable, identify the information the seller must verify and give a decision process. Do not invent a current price, fee, platform feature, percentage buffer, or seller-protection outcome.

For a price-or-platform answer without the seller's live account data, explicitly preserve the unknowns: state that the seller must verify completed comps, the platform's available delivery/payment flow, and the resulting net payout. Do not rank platforms by speed or state that a local flow is fee-free without evidence from that account and region.

## Core Flow

1. **Identify** — What is it? Condition? Complete?
2. **Price** — Research comparable completed sales and set a net-return floor (see `references/pricing.md`)
3. **Platform** — Match the item and delivery method to an available platform; verify its current terms before quoting fees (see `references/platforms.md`)
4. **List** — Title, photos, description
5. **Manage** — Handle offers, detect scams, reprice if needed

## Reference Loading Guide

Load references on demand based on the task:

| File | Load when |
|------|-----------|
| `references/pricing.md` | User needs pricing strategy for a specific item type (used electronics, handmade, collectibles, bulk lots, commissions) |
| `references/platforms.md` | User asks where to sell, needs fee comparisons, or wants multi-platform strategy |
| `references/safety.md` | Before advising on a buyer, payment, pickup, shipping address, or dispute |

## Pricing Quick Start

**For used items with market comps:**
1. Search eBay **SOLD** listings (not active)
2. Check FB Marketplace in your area
3. Set floor (minimum you'll accept)
4. Choose a listing price with a negotiation buffer that the current comps support

**For handmade/unique items:**
Materials + labor + overhead + desired profit

For detailed strategies by item type, see `references/pricing.md`.

## Listing Formula

**Title:** `[Brand] [Model] [Key Spec] [Condition]`
> Sony WH-1000XM4 Wireless Headphones - Excellent

**Photos (minimum 5):**
1. Hero shot — clean background
2. All angles
3. Close-up of features/branding
4. Every flaw (builds trust)
5. What's included

**Description:**
- What it is (brand, model, specs)
- Honest condition
- What's included
- Shipping/pickup options

## Handling Offers

| Offer | Response |
|-------|----------|
| Below your documented floor | State your floor once or decline courteously |
| At or above your floor but below target | Counter with a price supported by recent comps |
| At or above your target | Accept when the transaction also meets your safety and delivery terms |

**Soft declines:**
> "I have interest at asking price"
> "I'll keep your offer in mind if it doesn't sell by [date]"

## Safety

Before any transaction, read `references/safety.md` to check for:
- Escalation signals (overpayment, off-platform payment requests, QR codes, verification-code requests)
- Safe meeting practices for local sales
- Payment and seller-protection eligibility conditions
- Evidence to preserve for shipping and disputes

## Repricing Strategy

Set a review date before publishing. At each review, compare views, messages, completed comps, and net return; then keep the price, revise the presentation, adjust to current evidence, or accept the documented floor.

## Failure Modes and Recovery

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| No SOLD comps found on eBay | Niche or new item, no resale market | Search "for parts" listings for floor; price at cost-plus instead; consider bundling with related items |
| Item gets views but no offers | Price, photos, or title may not match current buyer expectations | Recheck completed comps; re-shoot the hero photo with a cleaner background; revise the title to lead with brand and model; adjust only when the evidence supports it |
| Lowball offers only | Listed above market or reaching the wrong audience | Compare the documented floor with fresh comps; state the floor or counter from evidence; try a platform with a more suitable buyer audience when available |
| Buyer claims item broken after pickup | Evidence or terms are incomplete | Preserve messages, photos, and pre-handoff test evidence; follow the platform process when used and check applicable local rules before resolving a material dispute |
| Payment seems "too easy" | Possible overpayment, spoofed confirmation, or third-party pickup scam | Treat the payment and pickup terms—not an offer percentage alone—as the signal; end the transaction path, preserve the message, verify the transaction in the official app or website, then report or block through the platform when appropriate |
| Item is still unsold at the review date | Price, presentation, audience, or listing visibility may be weak | Recheck completed comps, refresh photos and title, adjust the price to current evidence, and use platform-supported renew or relist options |

## Decision Rules

- **Price from SOLD comps.** Used items are worth what buyers actually paid today. Filter eBay to "Sold Items" and use those prices as your baseline.
- **Show every flaw in photos.** Photographing each defect upfront builds trust and prevents post-sale disputes, negative feedback, and refund demands.
- **Use a payment flow whose current seller-protection terms fit the sale.** Review eligibility, proof-of-delivery, and dispute requirements before relying on protection.
- **Set your floor price before listing.** Write down your minimum acceptable price before the listing goes live. This anchors you against emotional pressure during negotiations.
- **Verify payment in the official transaction view before shipping.** Confirm the funds, shipping address, and protection eligibility there rather than relying on a message or email.
- **Calculate net return from current platform terms.** Fees, shipping availability, payment processing, and protection terms vary by platform, category, account, and region; use `references/platforms.md` immediately before quoting a net price.

## Gotchas

- **eBay SOLD listings, not active.** Active listings show asking price, not what buyers actually paid. Always filter to "Sold Items."
- **Mark sold on every platform.** Cross-listing without marking sold leads to double-selling. Update all listings the moment an item sells.
- **Email "payment confirmed" is not payment confirmed.** Scammers send spoofed PayPal/eBay/Poshmark emails. Always log into the platform directly to verify funds cleared.
- **Use the transaction's verified delivery details.** A post-payment address change can remove seller-protection eligibility; confirm the current terms and retain tracking evidence.
