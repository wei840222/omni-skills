# Sources — Meal Planner

Live-checked on 2026-10-18 during the omni-skills repair of Jules session
`11290837867027231559`. Prefer these URLs over memorized figures. If a URL
fails at runtime, say the claim is unverified and avoid inventing official
dollar amounts.

## Agent Skills format

- Specification: https://agentskills.io/specification.md
- Best practices: https://agentskills.io/skill-creation/best-practices.md
- Description optimization: https://agentskills.io/skill-creation/optimizing-descriptions.md

## Food planning, diet quality, and waste

- Dietary Guidelines for Americans hub: https://www.dietaryguidelines.gov/
- NHS balanced-diet overview: https://www.nhs.uk/live-well/eat-well/how-to-eat-a-balanced-diet/eating-a-balanced-diet/
- EPA preventing wasted food at home: https://www.epa.gov/recycle/preventing-wasted-food-home
- USDA ERS fruit and vegetable prices: https://www.ers.usda.gov/data-products/fruit-and-vegetable-prices

## Budget and official cost-of-food series

Official USDA Food Plans / CNPP monthly cost-of-food pages returned HTTP 403 to
this repair runner on 2026-10-18. Treat any thrifty/moderate/liberal dollar
bands in `references/budget-tips.md` as **local planning heuristics**, not as
verbatim USDA Food Plans figures, until a reachable official series is cited
again.

Failed or unavailable during this repair (do not cite as verified):

- `https://www.fns.usda.gov/cnpp/usda-food-plans-cost-food-reports-monthly-reports` → HTTP 403
- `https://www.fns.usda.gov/cnpp/usda-food-plans-cost-food` → HTTP 403
- `https://www.foodsafety.gov/food-safety-charts/cold-food-storage-charts` → HTTP 403
- `https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperature-chart` → HTTP 403
- `https://www.myplate.gov/eat-healthy/what-is-myplate` → DNS failure
- `https://www.bls.gov/cex/` → HTTP 403

## Claim handling rules

1. Prefer user-stated budgets over any heuristic table.
2. Seasonal/produce savings may point to ERS fruit-and-vegetable prices without
   inventing exact percent savings.
3. Leftover and waste guidance may cite EPA preventing wasted food at home.
4. Balanced-plate language may cite Dietary Guidelines / NHS pages above; do
   not invent micronutrient therapy (hand to `nutrition` / `dietitian`).
