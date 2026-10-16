# Official Source Pins — Walmart

Verified during the 2026-10-16 handoff. Prefer these live URLs over remembered
hostnames. Bot-mitigated or 4xx/403 hosts remain discovery clues only until an
authenticated session confirms them.

## Specification and format

| Source | Verified | Notes |
|--------|----------|-------|
| https://agentskills.io/llms.txt | HTTP 200 | Agent Skills document index |
| https://agentskills.io/specification | HTTP 200 | Normative Agent Skills format (Gate 1) |
| https://agentskills.io/skill-creation/best-practices | HTTP 200 | Progressive disclosure / scope guidance |
| https://agentskills.io/skill-creation/optimizing-descriptions | HTTP 200 | Description routing guidance |
| https://github.com/agentskills/agentskills/tree/main/skills-ref | live repo | Reference validator package (`skills-ref` / `agentskills`) |

## Consumer Walmart surfaces

| Source | Verified | Notes |
|--------|----------|-------|
| https://www.walmart.com/ | HTTP 200 | Primary consumer browse / cart / fulfillment surface |
| https://www.walmart.com/my-items | HTTP 200 → site root without session | My Items reorder entry; authenticated UI required for real lists |
| https://www.walmart.com/pharmacy | HTTP 200 → `/health-and-wellness/cp/pharmacy/5431` | Pharmacy / health hub entry |
| https://www.walmart.com/help | HTTP 200 | Help center for order support / policy discovery |
| https://corporate.walmart.com/ | HTTP 200 | Corporate context only; not a grocery API |

Unauthenticated `https://www.walmart.com/account/order-history` returned HTTP
404 in this check. Treat Purchase History as an authenticated account path, not
a public deep link.

## Marketplace / seller developer docs

| Source | Verified | Notes |
|--------|----------|-------|
| https://developer.walmart.com/ | HTTP 200 | Walmart Developer Portal home |
| https://developer.walmart.com/us-marketplace | HTTP 200 | US Marketplace partner docs hub |
| https://developer.walmart.com/us-marketplace/docs/delegated-access-authorization | HTTP 200 | Marketplace delegated-access / auth docs |
| https://developer.walmart.com/us-marketplace/reference/tokenapi | HTTP 200 | Token / OAuth reference docs |
| https://developer.walmart.com/us-marketplace/docs/marketplace-recipes | HTTP 200 | Seller recipes for items, orders, inventory |

## API host caveats

| Host / path | Observed | Interpretation |
|-------------|----------|----------------|
| `https://marketplace.walmartapis.com` (root) | HTTP 404 | Not a public consumer docs page; do not cite as browseable grocery API |
| `https://marketplace.walmartapis.com/v3/token` | HTTP 400 without partner credentials | Seller OAuth endpoint; requires Marketplace partner registration |

**Domain fact retained:** official consumer grocery / pickup automation remains
browser-mediated account UI. Marketplace APIs documented on
`developer.walmart.com/us-marketplace` target sellers and solution providers
(items, inventory, orders, pricing, returns, shipping, reports)—not ordinary
household shopping accounts.
