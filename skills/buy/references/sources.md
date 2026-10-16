# Data Sources by Category

Use these to research prices and validate deals. Re-check live pages before repeating jurisdiction-specific consumer-protection claims. Status notes below reflect HTTP checks during the 2026-10-17 refactor pass.

## Specification / skill craft

| Source | Why | Checked |
|--------|-----|---------|
| [Agent Skills llms.txt](https://agentskills.io/llms.txt) | Document index | HTTP 200 |
| [Agent Skills specification](https://agentskills.io/specification) | Normative format | HTTP 200 |
| [Best practices](https://agentskills.io/skill-creation/best-practices) | Progressive disclosure | HTTP 200 |
| [Optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) | Trigger wording | HTTP 200 |
| [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) | Reference validator | HTTP 200 |

## Price history & comps

| Tool / page | What it does | Best for | Checked |
|-------------|--------------|----------|---------|
| [Keepa](https://keepa.com/) | Multi-retailer Amazon price tracking | Electronics / Amazon SKUs | HTTP 200 |
| [eBay Buying help](https://www.ebay.com/help/buying) | Marketplace buying / sold-search orientation | Used goods | HTTP 200 |
| Google Shopping / product results | Cross-retailer comparison | General retail | Use live search; no static claim |
| CamelCamelCamel | Amazon price history | Amazon purchases | Site often bot-blocked (403); treat as optional tool the user may open |

## Vehicle history & valuation

| Source | Role | Checked |
|--------|------|---------|
| [Carfax](https://www.carfax.com/) | VIN / vehicle history | HTTP 200 |
| [AutoCheck](https://www.autocheck.com/) | Alternate VIN history | HTTP 200 |
| [VINCheck](https://vincheck.info/) | Lightweight VIN lookup orientation | HTTP 200 |
| KBB / Edmunds class valuation tools | Value ranges | Often bot-blocked (403); require live user/browser check — never invent numbers |

## Scam & consumer protection

| Source | Role | Checked |
|--------|------|---------|
| [USA.gov scams and fraud](https://www.usa.gov/scams-and-fraud) | Consumer scam orientation | HTTP 200 |
| [USA.gov consumer](https://www.usa.gov/consumer) | Consumer protection hub | HTTP 200 |
| [IC3](https://www.ic3.gov/) | Internet crime complaint center | HTTP 200 |
| [eConsumer.gov](https://www.econsumer.gov/) | Cross-border e-commerce complaints | HTTP 200 |
| [ReportFraud.ftc.gov](https://reportfraud.ftc.gov/) | FTC fraud reporting entry | HTTP 200 |
| [ICANN Lookup](https://lookup.icann.org/en) | Domain age / WHOIS orientation | HTTP 200 |
| [Google reverse image help](https://support.google.com/websearch/answer/1325808?hl=en) | Stolen listing photo checks | HTTP 200 |

BBB and many retailer marketing sites frequently return HTTP 403 to automation; do not fabricate ratings — open them interactively when needed.

## B2B / SaaS orientation

| Source | Role | Notes |
|--------|------|-------|
| Vendor quote / pricing page | List vs negotiated | Ask for written quote |
| G2 / Capterra class review hubs | Feature / UX signal | Often bot-blocked; verify live |
| Practitioner forums (for example sysadmin communities) | Implementation pain | Treat as anecdote, not proof |

## Reviews (filter for signal)

| Source | Trust posture | Watch for |
|--------|---------------|-----------|
| Long-form independent testers (for example Wirecutter-class) | Higher when methodology is clear | Affiliate incentives |
| Amazon / marketplace reviews | Medium | Fake 5-star clusters; read 2–3★ for defects |
| YouTube | Medium | Sponsorship bias |
| Reddit / forums | Variable | Real failures useful; sample size often tiny |

## Scam detection checklist

- Domain age via ICANN Lookup — brand-new domains selling expensive goods are elevated risk
- Reverse image search for stolen photos
- Payment method pressure (wire / crypto / gift card only)
- Price ≥ ~30% below verified sold comps without a documented defect
- Seller refuses written terms or independent inspection

## Obsolete / softened claims

- Do not treat any single "official" car value site as authoritative when automation cannot fetch it; always dual-source or mark unverified.
- Clawic homepage / `_meta.json` promotional residue removed in Gate 5 — not a research source.
