# Sources — Etsy (Gate 6)

Verified primary references for fee, search, and policy claims. Prefer these over memory when numbers or product rules change. Etsy help pages are often bot-protected; open them in a normal browser session when quoting live fee tables.

## Fees and seller economics

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| How fees work | Etsy Help — How Fees Work on Etsy | https://help.etsy.com/hc/en-us/articles/115014476548-How-Fees-Work-on-Etsy | Listing, transaction, payment processing, and optional offsite ads are separate cost layers; always re-read the live schedule before quoting a percentage. |
| Fee schedule (legal) | Etsy — Fees & Payments Policy | https://www.etsy.com/legal/fees/ | Canonical fee policy text; region and category can change the stack. |
| Offsite ads | Etsy Help — Offsite Ads | https://help.etsy.com/hc/en-us/articles/360000343967 | Paid offsite placements are optional growth cost; do not treat them as free ranking. |

## Search, listing quality, and visibility

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Search behavior | Etsy Seller Handbook — How Etsy Search Works | https://www.etsy.com/seller-handbook/article/how-etsy-search-works/33854721807 | Titles, tags, attributes, and listing quality signals interact; stuffing is not a durable strategy. |
| Getting more views | Etsy Help — Tips for Getting More Views | https://help.etsy.com/hc/en-us/articles/360000343908-Tips-for-Getting-More-Views | Photo and title clarity remain first-order levers before tag churn. |
| Seller Handbook hub | Etsy Seller Handbook | https://www.etsy.com/seller-handbook/ | Index for current merchandising guidance; prefer handbook + Help over third-party blogs for policy-adjacent claims. |

## Policy and trust

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Seller Policy | Etsy — Seller Policy | https://www.etsy.com/legal/sellers/ | Prohibited practices and seller obligations; do not coach evasion. |
| Prohibited items | Etsy Help — Prohibited Items | https://help.etsy.com/hc/en-us/articles/115015500727 | Category and item bans change; escalate when risk appears. |
| Intellectual property | Etsy Help — Intellectual Property | https://help.etsy.com/hc/en-us/articles/360000344107 | Trademarked terms and brand hijacking are out of scope for "growth hacks." |

## Experiment design (domain-stable)

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Online controlled experiments | Kohavi et al. — Controlled experiments on the web (overview literature) | https://exp-platform.com/Documents/GuideControlledExperiments.pdf | One primary metric, sufficient runtime, and avoid peeking-driven thrash; skill default 7–14 day listing windows follow this discipline at small-shop traffic levels. |
| Agent Skills format | Agent Skills specification | https://agentskills.io/specification | Frontmatter shape, progressive disclosure, package layout. |
| Reference validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/etsy`. |

## Practice notes

- **Do not hard-code fee percentages in procedural rules.** Etsy updates listing, transaction, payment, and offsite-ads fees by region and over time. Walk the user through a margin worksheet and point at the live Help/legal pages above.
- Search ranking factors are not a public fixed formula. Treat handbook + Help guidance as directional; optimize for buyer-intent clarity and conversion, not alleged secret weights.
- Third-party "Etsy algorithm 2026" blog posts are untrusted unless they cite primary Etsy material; prefer official sources for Gate 6 claims.
