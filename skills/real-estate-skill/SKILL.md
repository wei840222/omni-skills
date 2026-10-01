---
name: real-estate-skill
description: >
  Guide property decisions for buyers, sellers, landlords, tenants, investors,
  or agents with role protocols, deal metrics, negotiation framing, and fair-housing
  safe boundaries. Use for general real-estate process coaching across jurisdictions;
  prefer `real-estate-investing` for deep underwriting, `real-estate-agent` for listing
  CRM state, and `negotiate` for live counterparty deal craft outside property closings.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏡","displayName":"Real Estate"}'
  related-skills: '{"real-estate-investing":"Deep buy-and-hold, BRRRR, flip, and underwriting when the task is investment analysis rather than general transaction coaching.","real-estate-agent":"Listing CRM, client profile, and property tracking state when the user wants durable agent workflow memory.","negotiate":"Live counterparty offer/counter craft with hard limits when the thread is pure deal messaging.","home-buying":"Owner-occupant purchase focus when the user is only buying a primary home.","rental":"Tenant-landlord operations and leasing details beyond high-level landlord protocol.","legal":"Contract and enforceability review when counsel-level document work is the primary need.","invest":"Broader capital allocation when property is one option among many asset classes.","property-valuation":"Comp-driven market value checks against a price thesis."}'
---

This skill is **stateless process knowledge**: it routes role, stage, and jurisdiction-aware coaching. It does not store client CRM files or durable deal ledgers. For persistent listing/client memory load `real-estate-agent`; for investment underwriting load `real-estate-investing`. Re-open URLs in `references/sources.md` before stating jurisdiction-specific legal, disclosure, or lending claims as current fact.

## When to load

Load when the user needs **general real-estate decision coaching**:

- first-time or repeat home buying process
- selling prep, pricing posture, and listing readiness
- landlord screening / lease essentials orientation
- investor screening metrics (cap rate, CoC, GRM, 1% rule) before deep underwriting
- offer, contingency, and repair-negotiation framing on a property deal
- fair-housing and licensing boundary checks in property conversations

Route away when the task is mainly:

- full investment underwriting, DSCR, BRRRR model → `real-estate-investing`
- durable client/listing CRM state → `real-estate-agent`
- live multi-round counterparty messaging with hard limits → `negotiate`
- pure legal drafting / enforceability → `legal`
- owner-occupant home-buying only with no other roles → `home-buying`
- day-to-day rental operations → `rental`

## First: clarify context

Before substantive guidance, lock three facts (ask once if missing):

1. **Role** — buyer, seller, landlord, tenant, investor, or agent
2. **Jurisdiction** — country, state/province, city (laws differ sharply)
3. **Stage** — exploring, searching, under contract, closing, or post-purchase

Every response that gives location-specific steps includes the jurisdiction disclaimer from `references/legal-compliance.md` and recommends licensed local professionals for contracts, financing, and tax.

## Role protocols (load detail on demand)

| Role | High-level flow | Load |
|------|------------------|------|
| Buyer | Affordability → pre-approval → search → offer → diligence → close | `references/buyer-guide.md` |
| Seller | Pricing → prep → list → showings → negotiate → close | `references/seller-landlord.md` |
| Investor | Source → analyze → finance → acquire → operate → exit | `references/investor-toolkit.md` |
| Landlord | Screen → lease → manage → maintain → renew/terminate | `references/seller-landlord.md` |
| Agent | Listing copy, client comms, negotiation prep, market updates | role refs + `references/negotiation.md` |
| Deal messaging | Offers, counters, repairs, concessions | `references/negotiation.md` |
| Compliance | Disclaimers, fair housing, licensing limits | `references/legal-compliance.md` |
| Sources | Verified orientation URLs (Gate 6) | `references/sources.md` |

## Investor quick metrics

Use as **screening only**; full underwriting belongs in `real-estate-investing`.

| Metric | Formula | Note |
|--------|---------|------|
| Cap Rate | NOI / Purchase Price | Ignores financing |
| Cash-on-Cash | Annual cash flow / Cash invested | Needs debt assumptions |
| GRM | Price / Gross annual rent | Rough screen |
| 1% Rule | Monthly rent ≥ 1% of price | Coarse filter, not proof of a good deal |

Stress incomplete expense inputs before calling a deal “good.”

## Compliance and hard limits

Non-negotiable on every substantive answer:

- jurisdiction variance disclaimer
- professional consultation for contracts, financing, tax
- fair-housing compliance (zero tolerance for discriminatory steering)

This skill **does not**:

- supply binding contract templates (educational outlines only)
- recommend specific mortgage products (licensing boundary)
- give personalized securities advice on REITs or syndications
- provide or verify wire-transfer instructions (direct users to closing attorney / title company)

Load `references/legal-compliance.md` whenever the user asks for contracts, protected-class neighborhood guidance, eviction steps, or wire/payment handling.

## Execution order

1. Clarify role, jurisdiction, stage.
2. Load the smallest matching reference file.
3. Re-check `references/sources.md` before repeating a statutory or agency claim.
4. Keep answers educational; surface the next licensed-human handoff when stakes are high.
