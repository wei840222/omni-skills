---
name: price
description: Track prices, detect dynamic pricing manipulation, time purchases, and assess fair market value for consumer and B2B goods. Use when the user asks about good deals, price drops, or timing a purchase.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💰"}'
---

## When to Use

User asks: "is this a good price?", "should I buy now or wait?", "track this price", "price history", "is this sale real?", "hidden fees", "compare prices", "price alert", "shrinkflation", "fair market value".

For setting prices as a seller, use `pricing` instead. For the general buying process, use `buy` instead.

## Quick Reference

| Area | File | When to load |
|------|------|--------------|
| Domain Knowledge | `references/domain-knowledge.md` | For general pricing concepts and tactics. |
| Retail & electronics | `references/retail.md` | For consumer electronics, apparel, and daily goods pricing. |
| Travel & hospitality | `references/travel.md` | For flights, hotels, and vacation packages pricing. |
| B2B & enterprise | `references/b2b.md` | For software licenses, bulk materials, and enterprise services. |
| Collectibles & investments | `references/collectibles.md` | For rare items, art, trading cards, and speculative goods. |
| Manipulation detection | `references/manipulation.md` | When evaluating a sale or discount for inflated anchor prices or shrinkflation. |
| Price tracking setup | `references/tracking.md` | When setting up alerts or active price monitoring. |

## Workspace Structure

All data lives in <state_root>/price/:

```
<state_root>/price/
├── config.md           # Preferred retailers, alert thresholds
├── watchlist.md        # Items being tracked with targets
├── history/            # Price history by item
├── alerts.md           # Active price alerts
└── purchases.md        # Past decisions for learning
```

## Core Operations

**Evaluate price:** Current price + item → Check historical range → Calculate vs 90-day low → Factor total cost → Verdict with confidence level.

**Set alert:** Item + target price → Add to watchlist → Monitor across retailers → Notify when hit.

**Track item:** Product URL/name → Poll price periodically → Log to history → Detect changes.

**Time purchase:** Category + timeframe → Check seasonal patterns → Recommend buy/wait → Explain reasoning.

## Price Assessment Framework

For EVERY price evaluation:

1. **Historical context** — Current vs 90-day low, all-time low, typical range
2. **Total cost** — Add shipping, tax, fees, warranty, hidden costs
3. **Timing factors** — Seasonal patterns, upcoming sales, event-driven spikes
4. **Manipulation check** — Inflated "was" price, dynamic pricing, fake urgency

## Output Format

```
## Price Assessment: [Item]

**Current:** $X | **90-day low:** $Y | **All-time low:** $Z
**Total cost:** $W (includes: shipping, tax, fees)
**Verdict:** [Good deal | Fair | Wait | Overpriced]

**Why:** [Data-backed reasoning]
**Action:** [Buy now | Set alert for $X | Wait until Y]
**Confidence:** [High | Medium | Low] — [data quality note]
```

## Critical Rules (ALWAYS Apply)

- **Show data sources** — Always cite the specific data source when providing price history
- **Include total cost** — Always add shipping, tax, and fees to the listed price to calculate the total cost
- **State confidence level** — Be honest about data quality and limitations
- **Explain "why now"** — If recommending buy, explain what makes timing good
- **Flag manipulation** — Always check for inflated comparisons, dynamic pricing

## On First Use

1. Ask what categories user buys frequently
2. Set up preferred retailers list
3. Configure alert notification preferences
4. Explain price history data sources available
5. Add first items to watchlist
