---
description: Optimize listings, compare pricing, and detect scams across online marketplaces.
  Load this when a user wants to buy, sell, or research items on platforms like eBay,
  Amazon, Etsy, or Mercari.
metadata:
  openclaw: '{"emoji": "🛒"}'
  version: 1.0.1
name: marketplace
---



## Architecture

Role-based guidance for marketplace participation. Load relevant file based on user's role.

```
marketplace/
├── references/buyer.md      # Price comparison, scam detection, negotiation
├── references/seller.md     # Listing creation, pricing, platform rules
├── references/builder.md    # Marketplace creation, economics, liquidity
├── references/arbitrage.md  # Price gaps, ROI calculations, ToS risks
└── references/compliance.md # Tax obligations, legal pitfalls, bans
```

## Quick Reference

| Role | File | When to Load |
|------|------|--------------|
| Buying items | `references/buyer.md` | Comparing prices, spotting scams, negotiating |
| Selling items | `references/seller.md` | Creating listings, pricing, handling buyers |
| Building marketplace | `references/builder.md` | Designing platform, economics, payments |
| Arbitrage/Reselling | `references/arbitrage.md` | Finding price gaps, calculating true ROI |
| Legal/Tax questions | `references/compliance.md` | Tax nexus, ToS violations, suspensions |

## Core Rules

### 1. Platform-Specific, Must Be Specific
- Each platform has unique fees, rules, and dynamics
- eBay auction ≠ Amazon Buy Box ≠ FB Marketplace negotiation
- ALWAYS specify which platform advice applies to

### 2. Total Cost, Not Sticker Price
- Include: platform fees, shipping, taxes, return costs
- Amazon referral fee varies 8-45% by category
- eBay 13.25%+ Poshmark 20%+ Mercari 0% selling fee

### 3. Scam Pattern Recognition
- Stock photos on local marketplaces = red flag
- "Ship to my address, I'll pay extra" = triangulation fraud
- Payment outside platform = no protection
- New account + high-value item + urgency = likely scam

### 4. Pricing Research = SOLD, Not Listed
- Listed prices mean nothing—items sell at realized historical prices
- Always research completed/sold listings
- Factor in condition: "Good" vs "Very Good" = 30% price difference

### 5. Suspension Risks Are Real
- Amazon ODR >1% = account death
- Review manipulation = permanent ban
- IP complaints from brands = immediate suspension
- Multiple accounts = instant termination

### 6. Fee Complexity
Calculate fees exactly based on formula:
- Amazon: referral + FBA + storage + return processing + advertising
- eBay: final value (category-specific) + promoted listings + payment
- Factor returns into margin (15-30% in some categories)

### 7. Real-Time Data Required
- Quote prices exclusively using real-time searches
- Inventory and pricing change hourly
- Competitor stock levels affect optimal pricing
- Always verify current marketplace state before advising
