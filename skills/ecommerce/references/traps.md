# Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Judging a promo by revenue | Revenue always rises with a discount; margin is what decides, and it can be negative while the day looks like a record | Contribution margin at the discounted price, before launch (Rule 4) |
| Optimizing conversion rate alone | Discounting and free shipping raise CR while lowering revenue per session and margin per session | Test against revenue per session and CM per session (`conversion.md`) |
| Trusting platform-reported ROAS | Every ad platform claims the same conversion; the sum exceeds actual revenue | MER against total revenue, plus a holdout or geo test (`acquisition.md`) |
| Add-to-cart reservations with no expiry | Phantom stock accumulates until the catalog reads sold out while the warehouse is full | TTL plus a sweeper, or no reservation at all (Rule 3) |
| Free shipping "because everyone does it" | It is a discount equal to the shipping cost, applied to every order including the cheap ones | Threshold at AOV × 1.25 and only if CM at that basket covers the freight (`pricing.md`) |
| Blocking returns to protect margin | Return friction shows up as disputes and one-star reviews, which cost more than the refund | Price the return rate into CM and fight abuse per customer, not per policy (`returns.md`) |
| Launching a marketplace listing at the store price | Commission, fulfillment fees and higher return rates can take a healthy SKU negative | Rebuild CM with the channel's full fee stack before listing (`marketplaces.md`) |
| Replatforming without a redirect map | Every ranking URL 404s on cutover and organic traffic does not come back on its own | Old→new URL map and 301s in the cutover checklist (`platforms.md`) |
| Deploying during peak | The one week that pays for the quarter is not the week to find a checkout regression | Freeze window with a written exception rule (`peak.md`) |
| Discount codes without stacking rules | Codes combine with automatic promos and free shipping into orders below cost | One stacking policy, one CM floor per cart, enforced server-side |
| Reading a cohort before it has closed | A 90-day repeat rate measured at day 40 always looks catastrophic | Compare only cohorts of equal maturity (`retention.md`) |
| Manual stock edits during a sale | The edit races the checkout and produces both oversells and phantom stock | Adjustments as deltas through the same atomic path, never absolute overwrites |
| Fraud rules tuned only on chargebacks | False declines are invisible in the dashboard and usually cost more than the fraud they prevent | Track decline rate and manual-review rate alongside dispute rate (`fraud.md`) |
| Keeping customer exports "just for analysis" | Personal data in a working folder is a breach waiting for a laptop to be lost | Aggregates only; the store is the system of record (Rule 9) |
