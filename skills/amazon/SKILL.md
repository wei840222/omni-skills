---
name: amazon
description: Navigate Amazon as a buyer, seller, or affiliate by tracking prices,
  optimizing listings, and making smart purchasing decisions.
metadata:
  openclaw: '{"emoji": "📦"}'
  related-skills: null
---

## Quick Reference

| File | Purpose |
|------|---------|
| `references/buying.md` | Smart purchasing, comparisons, reorders |
| `references/pricing.md` | Price tracking, deal detection, timing |
| `references/selling.md` | FBA/FBM operations, listing optimization |
| `references/affiliates.md` | Amazon Associates, commission optimization |
| `references/security.md` | Credentials, payments, account safety |
| `references/legal.md` | ToS compliance, automation limits |

## When to load

| User Request | Agent Action |
|--------------|--------------|
| "Find best X under $Y" | Search, compare reviews/ratings/price history, recommend |
| "Track price of [product]" | Monitor, alert on drops, suggest buy timing |
| "Reorder my [consumable]" | Find previous order, check price vs last time, reorder |
| "Is this deal real?" | Check price history, detect inflated-then-discounted |
| "Compare [A] vs [B]" | Side-by-side specs, reviews sentiment, value analysis |
| "Help me sell [product]" | Listing optimization, keyword research, pricing strategy |
| "Generate affiliate link" | Create tagged link, track performance |

## Buyer Mode — Core Capabilities

**Product research:**
- Search with filters (price, rating, Prime, seller type)
- Aggregate reviews — summarize pros/cons, detect fake patterns
- Compare alternatives with feature matrix
- Check seller reputation (third-party risk assessment)

**Price intelligence:**
- Track historical prices (detect fake discounts)
- Alert on price drops to target
- Identify best time to buy (Prime Day, Black Friday patterns)
- Compare across Amazon regions when applicable

**Purchasing:**
- Add to cart, apply coupons/Subscribe & Save
- Reorder recurring items with price verification
- Gift purchases with delivery coordination
- Returns/refunds initiation

See `references/buying.md` for detailed workflows.

## Seller Mode — Core Capabilities

**Listing management:**
- Create/optimize product listings
- Keyword research for search visibility
- A+ Content recommendations
- Image requirements compliance

**Operations:**
- Inventory monitoring and restock alerts
- FBA shipment planning
- Pricing vs competition tracking
- Review monitoring and response drafts

**Analytics:**
- Sales velocity, conversion rates
- Advertising performance (PPC)
- Profit margin calculation (fees, shipping, returns)

See `references/selling.md` for seller workflows.

## Affiliate Mode — Core Capabilities

**Link management:**
- Generate affiliate links with proper tags
- Shorten/customize for platforms
- Track click-through and conversions

**Content optimization:**
- High-commission product categories
- Seasonal trending products
- Comparison content ideas

See `references/affiliates.md` for affiliate strategies.

## Critical Security Rules

**Credentials — Required protections:**
- Keep Amazon passwords out of agent memory and plain-text storage
- Keep session cookies scoped to the active trusted device/session
- Require human completion of 2FA prompts; never bypass them

**Payments — ALWAYS:**
- Confirm total before purchase
- Verify shipping address
- Alert on unusual amounts

**Automation — LIMITS:**
- Implement rate limiting on all requests to protect account standing
- Require explicit human confirmation before executing any automated purchasing
- Respect session timeouts

See `references/security.md` for complete security protocols.

## Legal Constraints

**Automation boundaries:**
- Amazon ToS prohibits certain bots — know the limits
- Affiliate disclosure required on all monetized content
- Seller account actions need manual confirmation

**What's allowed:**
- Price tracking via public pages
- Affiliate link generation
- Listing optimization assistance

**What requires caution:**
- Automated purchasing (needs explicit user auth flow)
- Review analysis at scale (rate limits)
- Scraping product data (use official APIs when available)

See `references/legal.md` for ToS details and safe practices.
