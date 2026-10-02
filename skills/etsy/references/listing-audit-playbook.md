# Listing Audit Playbook - Etsy

Use this workflow when a user asks why a listing is underperforming.

## 1. Intake snapshot

Collect a compact baseline before suggesting edits:

- Product category and buyer segment
- Current title, first image, and price point (item + shipping)
- Recent views, favorites, carts, and conversions
- Shipping ETA / processing time and return policy summary
- Production model (made-to-order, stocked, digital, vintage)

If metrics are missing, ask for them; do not invent conversion rates.

## 2. Diagnose by funnel stage

Evaluate each stage separately so fixes stay controlled:

| Stage | Signal | Common failure |
|-------|--------|----------------|
| Search visibility | Low impressions/views | Weak keyword intent match; title opening not buyer language |
| Click-through | Low visits per impression | Thumbnail/title mismatch; cluttered first image |
| Consideration | Low favorites/carts | Offer unclear vs alternatives; weak proof or use-context photos |
| Conversion | Low orders per visit | Price/shipping friction, trust gaps, slow processing promises |

A high-view / low-sale pattern is usually consideration or conversion, not "need more tags."

## 3. Prioritize fixes by expected impact

Use this order for most Etsy listings:

1. Main image and title opening clarity
2. Shipping promise and processing transparency
3. Price architecture and bundle logic (after fee-aware margin check)
4. Description opening and objection handling
5. Supporting tags and long-tail coverage

## 4. Build one-variable experiments

Keep experiments auditable:

- Change exactly one major variable per cycle
- Define minimum window (7 to 14 days unless traffic is very high)
- Track views, favorites, carts, conversion, and revenue per visit
- Log plan and outcome in `<state_root>/listing-experiments.md` when persistence is allowed

## 5. Decide with rules, not intuition

- **Keep** if conversion improves with stable margin
- **Revert** if traffic increases but conversion collapses
- **Iterate** if metrics move in opposite directions and the bottleneck shifts

## 6. Escalation triggers

Recommend deeper review when:

- Conversion remains flat after two clean experiments
- Listing metrics are unstable due to stockouts or shipping delays
- Policy or IP risk appears in title, tags, claims, or photos
- Fee schedule or category rules may have changed (re-open `references/sources.md`)
