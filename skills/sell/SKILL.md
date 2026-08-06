---
name: sell
description: Help users sell items by pricing accurately, creating compelling listings, choosing platforms, and handling offers. Use when the user wants to sell something, price an item, list items for sale, handle buyer offers, detect selling scams, or choose where to sell — even if they don't explicitly mention "sell" or "listing".
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💵"}'
  related-skills: '{"ebay":"Platform-specific listing optimization and fee calculation for eBay sales.","etsy":"Handmade and vintage listing SEO and pricing on Etsy.","facebook-marketplace":"Local selling on Facebook Marketplace with scam detection.","negotiate":"Structured negotiation tactics for high-stakes buyer interactions.","shipping":"Carrier selection, customs, and delivery for shipped sales.","vinted":"Clothing resale on Vinted with bundle pricing and shipping."}'
---

Before acting, clarify: item condition, timeline (need gone fast vs maximize price), and willingness to ship.

## Core Flow

1. **Identify** — What is it? Condition? Complete?
2. **Price** — Research comps by type (see `references/pricing.md`)
3. **Platform** — Match item to audience (see `references/platforms.md`)
4. **List** — Title, photos, description
5. **Manage** — Handle offers, detect scams, reprice if needed

## Reference Loading Guide

Load references on demand based on the task:

| File | Load when |
|------|-----------|
| `references/pricing.md` | User needs pricing strategy for a specific item type (used electronics, handmade, collectibles, bulk lots, commissions) |
| `references/platforms.md` | User asks where to sell, needs fee comparisons, or wants multi-platform strategy |
| `references/safety.md` | Before any transaction — scam detection, safe meeting locations, payment method guidance |

## Pricing Quick Start

**For used items with market comps:**
1. Search eBay **SOLD** listings (not active)
2. Check FB Marketplace in your area
3. Set floor (minimum you'll accept)
4. List at floor + 15-20%

**For handmade/unique items:**
Materials + (hourly rate × hours) + 30% margin

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
| <50% asking | Ignore or "Price firm at X" |
| 50-70% | Counter at 90% |
| 70%+ | Counter 85-90% or accept if at floor |

**Soft declines:**
> "I have interest at asking price"
> "I'll keep your offer in mind if it doesn't sell by [date]"

## Safety

Before any transaction, read `references/safety.md` to check for:
- Red flags that mean "do not engage" (overpayment, off-platform payment requests, QR codes)
- Safe meeting practices for local sales
- Payment method guidance (cash for local, platform payment for shipped)
- 2025 scam patterns (fake payment emails, shipping label fraud, verification code scams)

## Repricing Strategy

- **Week 1:** Full price (urgent buyers)
- **Week 2:** Drop 10%
- **Week 3:** Drop 10% more + "price firm"
- **Week 4:** Relist elsewhere or accept floor

## Failure Modes and Recovery

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| No SOLD comps found on eBay | Niche or new item, no resale market | Search "for parts" listings for floor; price at cost-plus instead; consider bundling with related items |
| Item gets views but no offers | Price too high or photos unappealing | Drop 10% immediately; re-shoot hero photo with cleaner background; rewrite title to lead with brand |
| Lowball offers only | Listed above market or wrong platform | Check comps again; try a platform with different buyer expectations; add "OBO" to attract negotiators |
| Buyer claims item broken after pickup | No pre-sale documentation | Prevention: video record item working before handoff; have buyer test and confirm via text. Resolution: local sales are as-is, no refund obligation |
| Payment seems "too easy" | Likely scam — overpayment, fake confirmation, driver pickup | Stop. Read `references/safety.md` red flags. Verify payment by logging into platform directly, never click email links |
| Item not selling after 3 weeks | Stale listing, algorithm deprioritized | Relist as new (delete and recreate); cross-post to additional platforms; drop price 10-20% |

## Decision Rules

- **Price from SOLD comps.** Used items are worth what buyers actually paid today. Filter eBay to "Sold Items" and use those prices as your baseline.
- **Show every flaw in photos.** Photographing each defect upfront builds trust and prevents post-sale disputes, negative feedback, and refund demands.
- **Use platform payment or PayPal Goods & Services.** These provide seller protection. "Friends & Family", wire transfers, and gift cards offer zero recourse if something goes wrong.
- **Set your floor price before listing.** Write down your minimum acceptable price before the listing goes live. This anchors you against emotional pressure during negotiations.
- **Wait for payment confirmation before shipping.** Log into the payment platform directly and verify funds are cleared and eligible for seller protection. Email confirmations can be spoofed.
- **Factor platform fees into pricing.** eBay FVF ranges 2.5%–15.3% by category plus a per-order fee; FB Marketplace shipped is 10%; Vinted is 0% seller; Poshmark is 20%. Check `references/platforms.md` for current rates before quoting a net price.
- **Vinted pricing is fee-free for sellers.** Vinted charges buyers a Buyer Protection Fee at checkout. Price your items at full value — there is no seller-side deduction to compensate for.
- **FB Marketplace shipped orders carry a 10% fee.** Local pickup remains free. Price accordingly when listing with shipping.

## Gotchas

- **eBay SOLD listings, not active.** Active listings show asking price, not what buyers actually paid. Always filter to "Sold Items."
- **Mark sold on every platform.** Cross-listing without marking sold leads to double-selling. Update all listings the moment an item sells.
- **Email "payment confirmed" is not payment confirmed.** Scammers send spoofed PayPal/eBay/Poshmark emails. Always log into the platform directly to verify funds cleared.
- **Shipping address must match payment address.** A buyer requesting a different shipping address after payment is a common fraud pattern. Ship only to the verified address.
