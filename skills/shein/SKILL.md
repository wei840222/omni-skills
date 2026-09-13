---
name: shein
description: Assist Shein shopping with size conversion, quality checks, price tracking,
  shipping expectations, and return caveats. Use when the user asks for Shein product
  research, fit guidance, deal timing, or cart strategy. Not for general multi-store
  shopping (`shopping`), outfit styling (`fashion`), or full ecommerce ops (`ecommerce`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛍️"}'
  related-skills: '{"shopping":"General multi-store purchase research and deal timing outside Shein.","fashion":"Outfit styling and wardrobe strategy beyond Shein product picks.","ecommerce":"Broader store operations and funnel work outside one marketplace."}'
---

## When to Use

Load this skill when the user explicitly wants help shopping on Shein: finding products, converting sizes, judging quality signals, tracking prices, building a cart, or setting shipping/return expectations.

Route elsewhere when:
- the question is multi-store purchase research without a Shein lock-in → `shopping`
- the user wants outfit/styling systems rather than a Shein buy → `fashion`
- the work is full ecommerce ops beyond one marketplace → `ecommerce`

This skill is stateless and does not store local configuration.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Size conversion | `references/sizing.md` | Fit, letter-size vs measurements, Curve/plus, shoes |
| Quality signals | `references/quality.md` | Fabric, construction, photo evidence, sub-brands |
| Official sources | `references/sources.md` | Verify shipping, returns, and policy claims |

## Core Rules

### 1. Always Check Reviews First
Before recommending any product:
- Prefer items with substantial review volume; treat sparse reviews as higher risk
- Check photo reviews for real color, drape, and construction
- Read 1-star reviews for recurring defects (sheer fabric, broken hardware, odor)
- Look for sizing feedback from reviewers with similar measurements

### 2. Size Conversion Priority
| Region | Action |
|--------|--------|
| US/EU user | Convert with `references/sizing.md`, then confirm the item chart |
| Asia user | Often closer to chart letter sizes; still verify measurements |
| Any user | Prefer exact bust/waist/hip/length over letter size alone |

Shein letter sizes commonly run smaller than US/EU RTW. Never treat letter size as authoritative without the product size chart.

### 3. Price Intelligence
- Track candidate prices over several days before large carts when time allows
- Flash-sale “original” prices are often inflated; judge value against recent street price
- Stack only codes the user is actually eligible for (app, email, creator); do not invent stackability
- Optimize toward free-shipping thresholds only when the extra item is still wanted

### 4. Quality Assessment Protocol
Use signals from `references/quality.md`:
- Fabric composition and season suitability (breathability vs pure polyester)
- Seller photo count and detail shots
- Review mentions of pilling, seam failure, odor, or see-through fabric
- Compare similar items across sellers before locking a pick

### 5. Shipping Reality
Treat shipping windows as estimates that vary by warehouse, destination, and peak season. Prefer current checkout estimates and `references/sources.md` over memorized ranges.

| Destination | Typical standard | Typical express |
|-------------|------------------|-----------------|
| US/EU | often ~1–3 weeks | faster paid options when offered |
| Other | often longer | depends on lane and customs |

Set expectations: express is mainly for time-sensitive carts; standard is usually enough for non-urgent wardrobe fills.

### 6. Return Policy Awareness
- Confirm the live return window and exclusions on Shein Help for the user’s region before promising refunds
- Common non-returnable categories include intimate apparel and final-sale / hygiene-sensitive items when marked
- Return shipping cost and method vary by region and reason
- Photograph condition on arrival for damaged or wrong-item claims

### 7. Smart Cart Building
1. Add candidates, then pause before checkout when time allows (promotions often appear later)
2. Check Similar Items for better-reviewed alternatives at similar price
3. Combine wanted items toward free shipping instead of padding with junk
4. Re-read carts over ~$50 after a cooling-off pause when the purchase is discretionary

## Common Traps

- Trusting studio photos without review photos → real item often differs in color and fabric hand
- Ordering by letter size only → Shein sizes frequently run small
- Skipping fabric content → uncomfortable or sheer materials
- Assuming every coupon stacks → eligibility and exclusions matter
- Rushing checkout → missing better comps, size notes, or a later promo

## Failure Modes

- User gives only letter size → ask for key measurements or the product chart before firm size advice
- Policy claim is region-sensitive (returns/shipping) → open `references/sources.md` and prefer live Help Center text
- User wants styling system, not a Shein buy → hand off to `fashion` / `shopping`
