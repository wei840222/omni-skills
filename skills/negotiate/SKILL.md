---
name: negotiate
description: >
  Negotiate prices, contracts, marketplace deals, or salary/offer terms on behalf
  of a principal with mandatory limits, graduated autonomy, and human approval for
  commitments. Use when drafting or sending counters, defending floors/ceilings,
  or logging negotiation state. Not for pure legal drafting (`legal` / `contract`),
  freelance platform ops without deal craft (`fiverr` / `freelance`), or personal
  career coaching without an active counterparty (`career`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🤝"}'
  related-skills: '{"buy":"Buyer-side research and acquisition workflow when the task is shopping rather than live counterparty negotiation.","sell":"Seller listing and offer intake when the work is merchandising rather than active deal craft.","contract":"Contract structure and clause drafting after commercial terms are agreed.","contracts":"Multi-contract portfolio tracking beyond a single live negotiation.","marketplace":"General marketplace operations outside a specific counterparty thread.","ebay":"eBay-specific listing and buyer messaging mechanics.","facebook-marketplace":"Facebook Marketplace logistics and local meetup flow.","price":"Pricing strategy and comps when no live counterparty negotiation is underway.","fiverr":"Fiverr seller ops when the platform workflow dominates deal craft.","freelance":"Cross-platform freelancing strategy outside a single live negotiation.","legal":"Legal review when terms, jurisdiction, or enforceability need counsel.","career":"Individual career strategy when no active offer counterparty is in play.","invoice":"Invoice generation after a deal is closed and billing begins."}'
---

Orientation only. This skill helps a principal negotiate; it does not grant authority to bind them. Hard limits, walk-away rules, and autonomy upgrades must be stated by the principal. Re-check `references/sources.md` before repeating jurisdiction-specific salary, consumer-protection, or marketplace-compliance claims.

## When to load

Load when the user asks you to **negotiate on their behalf** or coach a live deal:

- domain / item / NFT purchase counters
- service or product selling price defense
- P2P marketplace threads (eBay, FB Marketplace, Wallapop-class)
- salary, consulting rate, or contract commercial terms with a counterparty

Route away when the task is mainly:

- legal clause drafting or enforceability review → `legal` / `contract`
- Fiverr/Upwork platform ops without a live price fight → `fiverr` / `freelance`
- career strategy with no active counterparty → `career`
- pricing research with no negotiation thread → `price` / `buy` / `sell`
- post-deal billing documents → `invoice`

## State location

Optional durable negotiation profile and logs may live under a portable state root.

Resolve `<state_root>` before any read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/negotiate/`, `<workspace>/memory/negotiate/`, `~/negotiate/`.
3. If none exist and the principal asked to persist a profile, create `<workspace>/negotiate/`.

| Path | Required? | Role |
|------|-----------|------|
| `<state_root>/profile.md` | optional | Confirmed limits, autonomy grants, patterns, outcomes |
| `<state_root>/logs/` | optional | Offer/counter log files when the principal wants a transcript |

Do not store secrets, payment credentials, or private counterparty PII beyond what the principal explicitly asked to keep. Skill resources stay under `references/`; never mix them into `<state_root>`.

## References and execution order

Load the smallest file that matches the current deal. Load `references/sources.md` before repeating a market, consumer-protection, or employment-benchmark claim as fact.

| Domain | File |
|--------|------|
| Buying (domains, items, NFTs, bulk) | `references/buying.md` |
| Selling (services, products) | `references/selling.md` |
| P2P marketplaces | `references/p2p.md` |
| Professional (salary, contracts, partnerships) | `references/professional.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |

## Core rules

### 1. Mandatory setup before any negotiation

Do not draft a sendable counterparty message until these are explicit:

| Parameter | Required | Example |
|-----------|----------|---------|
| Hard limit (floor/ceiling) | yes | "Maximum budget €500" / "Minimum price €80" |
| Target price | yes | "Aim for €350" |
| Walk-away threshold | yes | "If they will not go below €450, end it" |
| Approval threshold | yes | "Get my OK before accepting anything" |
| Category context | yes | "Domain purchase" / "Salary offer" |
| Autonomy level | yes | Default **Level 1** unless principal upgrades a category |

If any parameter is missing, ask once with a compact checklist. Do not invent limits.

### 2. Autonomy levels (graduated trust)

| Level | What you may do | Still needs approval |
|-------|-----------------|----------------------|
| **1 - Observer** | Draft messages, suggest responses | Everything sent externally |
| **2 - Responder** | Send routine clarifying replies | Any offer or counteroffer |
| **3 - Negotiator** | Counter within a pre-set range | Final acceptance; anything outside range |
| **4 - Closer** | Accept within stated limits | Deals above threshold; unusual terms |

Default is Level 1. Upgrade only with explicit per-category permission. Professional salary/contract threads should rarely exceed Level 2 without a written grant.

### 3. Safety rails

1. Keep floor/ceiling confidential unless the principal orders a disclosure.
2. Test flexibility on first offers when the principal authorizes a counter.
3. Require approval for commitments unless Level 4 is granted for that category.
4. Log offers, counters, timestamps, and speakers when state logging is enabled.
5. Flag manipulation: fake urgency, emotional pressure, unverifiable "other buyer" claims, off-platform payment pressure.
6. Protect sensitive leverage (current salary, other offers, true urgency) until the principal releases it.

### 4. Category routing

| Category | Key dynamics | Load |
|----------|--------------|------|
| Buying | Low anchor, patience, walk-away power | `references/buying.md` |
| Selling | Floor defense, unbundling, closing signals | `references/selling.md` |
| P2P markets | Lowballers, ghosting, meetup logistics | `references/p2p.md` |
| Professional | Relationship preservation, BATNA, benchmarks | `references/professional.md` |

### 5. Negotiation profile

When the principal wants memory across deals, read/write `<state_root>/profile.md` with confirmed lines only:

- Known limits
- Autonomy grants
- Patterns observed
- Past outcomes

Confirm before storing a new durable claim. Empty sections mean nothing learned yet.

## Critical limits

- Never bind the principal without the approval rules for the active autonomy level.
- Never fabricate comps, laws, salary bands, or "market rates"; use `references/sources.md` and mark uncertainty.
- Never coach illegal discrimination, fraud, or marketplace ToS evasion.
- Prefer a delayed correct ask over a fast irreversible commitment.
