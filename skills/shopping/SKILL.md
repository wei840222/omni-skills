---
name: shopping
description: Optimize purchase decisions by validating budgets, researching real reviews,
  timing purchases, and evaluating return policies. Use when the user asks for shopping
  advice, product recommendations, deal checks, or buy-vs-wait guidance.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji": "🛍️"}'
  related-skills: '{"amazon":"Amazon-specific buying, price tracking, and listing workflows after a general purchase decision.","marketplace":"Cross-platform listing, scam, fee, and sold-price research beyond a single retailer.","expenses":"Capture the purchase into household or personal spend tracking after the buy decision.","money":"Budget ceilings, cash-flow timing, and total cost of ownership before committing.","buy":"Execution-focused checkout and order placement once the recommendation is settled."}'
---

## When to load

Load this skill when the user asks for shopping advice, product recommendations, deal evaluation, comparison shopping, or whether to buy now versus wait.

## Before recommending products

1. Confirm budget range first — recommendations without budget waste time.
2. Confirm use case specifically — "laptop" means different things for gaming vs email.
3. Ask what they have already tried or owned — past experience reveals preferences.
4. Confirm timeline — urgent need vs can wait for a sale changes strategy.
5. Give one primary recommendation with reasoning; add a short runner-up only when it changes the decision.

## Research approach

- Check reviews from multiple sources — a single source can be biased or paid.
- Read 1-star reviews for product-related defects; shipping complaints are secondary signal.
- Prefer long-term reviews — 6-month updates reveal durability.
- Treat Reddit and forums as higher-signal than heavily sponsored video reviews.
- Check whether a newer model is imminent — buying at the end of a cycle accelerates obsolescence.

## When to suggest not buying

- "I might need this someday" — prioritize current needs over speculative future needs.
- Upgrading something that already works — marginal improvement at full price.
- Buying a product to solve a non-product problem — new running shoes will not create a running habit.
- Emotional purchase after a bad day — wait 48 hours before deciding.
- Sale pressure such as "70% off ends tonight" — evaluate the item at regular price first; only then decide whether the discount matters.

## Price and timing

- Track price history (CamelCamelCamel for Amazon, comparable trackers elsewhere) — a "sale" may be the normal price.
- Major sales such as Black Friday, Prime Day, and end-of-season can justify waiting when the need is not urgent.
- Refurbished or open-box often saves 20-40% with the same warranty.
- Check credit-card price protection before buying.
- Many stores will price-match competitors when asked.

## Comparison framework

| Factor | Questions |
|--------|-----------|
| Must-haves | Which features are non-negotiable? |
| Nice-to-haves | What would be bonus but not essential? |
| Deal-breakers | What would trigger a return? |
| Total cost | Accessories, subscription, maintenance? |
| Longevity | How long until replacement is likely? |

When two options are close, prefer the one with the easier return path.

## Red flags

- Many 5-star reviews with near-identical language — likely fake.
- Brand-new product with hundreds of reviews immediately — suspicious timing.
- "Amazon's Choice" is an algorithm label, not a quality guarantee.
- Influencer discount codes mean the promoter profits from the purchase.
- Countdown timers and "only 2 left" often manufacture urgency.

## Return policy awareness

- Read the return policy before buying — some categories disallow returns.
- Keep packaging until the decision is final.
- Some credit cards extend return windows by 90 days.
- Restocking fees on electronics belong in the total-cost calculation.
- "Final sale" means final.

## Category-specific guidance

- **Electronics:** refresh cycles matter; buy early in the cycle rather than at the end.
- **Clothing:** size charts vary; read size-specific reviews.
- **Furniture:** measure twice; check assembly difficulty in reviews.
- **Appliances:** weight repair-frequency ratings as heavily as feature lists.
- **Subscriptions:** calculate yearly cost and confirm cancellation ease.

## Post-purchase

- After buying, stop comparison research and use the product; continued research feeds regret.
- Found cheaper afterward? Many stores still price-match inside a short window.
- Product problem? Contact support before leaving a public review.
- Purchase is complete only when the item is actually used.

