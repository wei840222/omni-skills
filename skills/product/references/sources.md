# Research sources (Gate 6)

Verify mutable numbers (fees, image minima, storage rates, tool tiers) against these pages at answer time. Grouped by topic.

## Agent Skills format

- Agent Skills specification — frontmatter, name, description, resource layout via https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref validator package — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Product-market fit and validation

- First Round Review — Superhuman PMF engine and Sean Ellis-style survey practice via https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
- pmfsurvey.com — Sean Ellis survey instrument orientation via https://pmfsurvey.com/
- SVPG — product/market fit framing via https://www.svpg.com/product-market-fit/
- Y Combinator Library — real product-market fit essay via https://www.ycombinator.com/library/5z-the-real-product-market-fit
- Wikipedia — Product/market fit overview (secondary) via https://en.wikipedia.org/wiki/Product/market_fit

## Prioritization and shaping

- Intercom / RICE origin context is historical; prefer current team definitions when scoring
- Basecamp Shape Up — appetite and shaping instead of pure backlog ranking via https://basecamp.com/shapeup
- SVPG continuous discovery habits companion context via https://www.svpg.com/continuous-discovery/ (when discovery, not score math, is the bottleneck)

## Amazon listing and images

- Amazon Seller Central help hub reference for product image requirements (node G200339940) via https://sellercentral.amazon.com/help/hub/reference/external/G200339940
- Alternate Seller Central help entry for the same topic via https://sellercentral.amazon.com/gp/help/help.html?itemID=G200339940
- Amazon customer help — image guidelines node 201953210 via https://www.amazon.com/gp/help/customer/display.html?nodeId=201953210
- Sell on Amazon overview via https://sell.amazon.com/sell

Treat fee tables in `amazon.md` / `pricing.md` as **orientation ranges**. Live referral, FBA fulfillment, and storage rates must be confirmed in the seller’s category fee schedule inside Seller Central for the active marketplace.

## Etsy and marketplace fees

- Etsy seller/legal fee policy pages change URL shape and may block automated fetch; open the in-product **Seller Handbook / Fees** entry while logged into the shop, or the public legal fees page from etsy.com navigation, before quoting listing, transaction, or offsite-ads rates.
- Orientation fee ranges in `etsy.md` are not a substitute for the shop’s current fee schedule.

## Print-on-demand and export sizes

- Printful custom products and size guidance entry via https://www.printful.com/custom-products
- Confirm per-SKU template dimensions inside the chosen POD provider dashboard (Printful, Printify, Gelato, Amazon Merch) before production upload; `specs.md` / `pod.md` sizes are starting points.

## SaaS metrics definitions

- Use `saas` skill + its sources when rebuilding MRR movement bridges; definitions in `metrics.md` here are orientation formulas only (NRR, LTV:CAC, quick ratio).

## Refresh notes

- Last verified reachable in this refactor pass: agentskills.io specification + llms.txt; First Round Superhuman PMF article; pmfsurvey.com; SVPG PMF; YC PMF essay; Wikipedia PMF; Basecamp Shape Up; Amazon Seller Central G200339940 help references; sell.amazon.com/sell; Printful custom-products.
- Etsy public fee URLs returned HTTP 403 to automated clients in this pass — human browser confirmation required before customer-facing fee quotes.
