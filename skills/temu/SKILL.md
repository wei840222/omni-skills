---
name: temu
description: >
  Analyze Temu products, sellers, pricing, and scam risk before purchase.
  Use when the user wants Temu deal checks, review authenticity, seller scoring,
  size/material verification, shipping/return expectations, or coupon strategy.
  Not for multi-store shopping (`shopping`), fashion styling (`fashion`),
  Shein-only workflows (`shein`), or full ecommerce ops (`ecommerce`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛍️"}'
  related-skills: '{"shopping":"General multi-store purchase research outside Temu.","fashion":"Outfit styling and wardrobe strategy beyond Temu product picks.","shein":"Shein-specific sizing, quality, and marketplace workflows.","ecommerce":"Broader store operations and funnel work outside one marketplace."}'
---

## When to Use

Load this skill when the user wants help buying on Temu: product risk analysis, seller reliability, fake-discount checks, review authenticity, size/material verification, shipping/return expectations, or coupon stacking.

Route elsewhere when:
- the question is multi-store purchase research without a Temu lock-in → `shopping`
- the user wants outfit/styling systems rather than a Temu buy → `fashion`
- the ask is Shein-specific sizing/quality → `shein`
- the work is full ecommerce ops beyond one marketplace → `ecommerce`

This skill is stateless and does not store local configuration.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Review authenticity | `references/reviews.md` | Fake-review signals, photo evidence, minimum thresholds |
| Pricing / coupons | `references/pricing.md` | Discount illusion, coupon stack, total-cost math |
| Scam patterns | `references/scams.md` | Counterfeit, bait-and-switch, dropship, high-risk categories |
| Official anchors | `references/sources.md` | Re-verify shipping, returns, and policy claims |

When executing this skill, load the relevant reference before advising.

## Core Rules

### 1. Price Reality Check
"90% off" is usually fake. Before recommending any deal:
- Compare to AliExpress, Amazon, eBay for the same product
- Treat listed "original price" as marketing, not market value
- Calculate total: base + shipping + potential customs duties
- Historical lows and cross-platform prices matter more than current "discounts"

### 2. Review Analysis
Most Temu reviews are weak signal. Filter by:

| Signal | Weight |
|--------|--------|
| Photo reviews with product in hand | HIGH |
| Reviews mentioning specific measurements | HIGH |
| 1-star reviews citing defects | HIGH |
| Generic 5-star "great product!" | IGNORE |
| Reviews within 24h of listing | RED FLAG |

Prefer substantial order volume **and** real buyer photos. Load `references/reviews.md` for thresholds by risk level.

### 3. Seller Scoring
Check before buying:
- **Store age** — new stores (<6 months) = higher risk
- **Total sales** — more sales = more data points
- **Response rate** — <90% = restrict to low-value, non-critical items only
- **Photo consistency** — stock photos only = dropshipper risk

### 4. Duplicate Detection
Same product often appears from many sellers. Compare:
- Unit price (not just total)
- Shipping time from the actual warehouse location
- Review quality, not quantity
- Return policy differences

### 5. Scam Red Flags
Auto-flag as likely scam:

| Pattern | Action |
|---------|--------|
| Brand item 50%+ below retail | Counterfeit — flag as high risk and skip |
| Main photo differs from product photos | Bait-and-switch |
| No buyer photos in reviews | Unverified quality |
| Seller only has this one product | Dropship test account |
| Ships from country different than stated | Customs / fulfillment risk |

Load `references/scams.md` for category risk tables and dispute timing.

### 6. Size & Material Verification
Always verify listed specifications independently:
- Cross-reference with actual review measurements
- Search reviews for "actual size", "real material"
- "Leather" under $20 = PU/pleather
- Electronics without CE/FCC marks = higher customs/safety risk

### 7. Shipping Reality
Temu ETAs are optimistic. Treat published windows as lower bounds and re-check live checkout for the user's region:

| Temu Says | Practical planning default |
|-----------|----------------------------|
| 7-12 days | often 15-25 days |
| "Express" | often 10-15 days |
| "Standard" | often 20-45 days |

Plan 2-3 weeks minimum unless warehouse/checkout shows a local fulfillment path. Prefer `references/sources.md` over hard-coded global SLAs.

### 8. Coupon Optimization
Temu coupons stack in confusing ways:
- Stack welcome + category + free-shipping threshold when valid
- Track expiry windows
- Free shipping threshold often makes small single-item orders unprofitable
- "Lightning deals" rotate; re-check before checkout

### 9. Return Reality
Before buying, know:
- Return shipping often costs more than item value
- "Free returns" has exclusions (electronics, hygiene, and region rules)
- Dispute/protection windows are time-bounded — open disputes before protection expires
- Photo/video everything on arrival

Re-verify live return policy links in `references/sources.md` before quoting hard numbers.

### 10. Cross-Platform Decision

| Buy on Temu When | Prefer Alternative When |
|------------------|-------------------------|
| Disposable/trendy items | Need item in <1 week |
| Price difference >50% vs Amazon after total cost | Safety-critical (electronics, car parts) |
| Low-risk categories (decor, accessories) | Brand authenticity matters |
| Willing to wait 2-4 weeks | Need reliable customer service |

## Common Traps

- **Trusting "original price"** → fictional; compare to actual market prices
- **Ignoring shipping time** → plan 2-3 weeks unless local warehouse is confirmed
- **Buying brands** → treat deep brand discounts as counterfeit risk
- **Skipping photo reviews** → text-only praise is weak evidence
- **Missing dispute deadline** → document issues immediately and act before protection ends
- **Small orders without free shipping** → shipping can exceed item cost; batch when sensible
