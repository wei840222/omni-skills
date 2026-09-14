---
name: dhgate
description: >
  Evaluate DHgate listings, vet suppliers, calculate landed costs, and manage
  shipping disputes. Use when the user wants DHgate sourcing, seller screening,
  unit-economics checks, tracking triage, dispute evidence prep, or counterfeit-risk
  control. Not for multi-store shopping (`shopping`), general price timing (`price`),
  Amazon-only buys (`amazon`), or full marketplace ops (`marketplace`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛒","requires":{"config":["<state_root>/dhgate/"]}}'
  related-skills: '{"shopping":"Broader multi-store purchase research and deal timing outside DHgate.","marketplace":"Cross-platform marketplace rules when DHgate should be compared against other channels.","amazon":"Local-retail convenience baseline versus import risk and lead times.","price":"Structured pricing logic for margin checks, bundle comparisons, and offer framing."}'
---

## When to load

Load this skill when the user needs help buying, sourcing, comparing, or disputing products on DHgate: seller screening, lot economics, shipping-risk triage, evidence prep, or safer category selection for personal buying or resale.

Route elsewhere when:
- the question is multi-store purchase research without a DHgate lock-in → `shopping`
- the work is full marketplace ops beyond one channel → `marketplace`
- the comparison is Amazon-local convenience only → `amazon`
- the ask is pure price-history / buy-now-vs-wait without DHgate sourcing → `price`

## State location

User preferences and sourcing notes live under `<state_root>/dhgate/` (see `references/setup.md` on first use, `references/memory-template.md` for file formats).

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/dhgate/`, `<workspace>/memory/dhgate/`, `<workspace>/Clawic/data/dhgate/`, `~/Clawic/data/dhgate/`, `~/dhgate/`.
3. If none exists and state must be created, default to `<workspace>/dhgate/`.
4. If you find data only at a legacy location, move it into the chosen `<state_root>/dhgate/` and say in one line that you moved it and from where.

Use the selected `<state_root>/dhgate/` for every state operation in this skill.

```text
<state_root>/dhgate/
├── memory.md        # Status, buying profile, active constraints
├── shortlist.md     # Candidate listings, rankings, next checks
├── sourcing.md      # Seller replies, negotiation points, MOQ notes
├── orders.md        # Tracking state, ETA assumptions, follow-ups
└── disputes.md      # Evidence checklist, timeline, decision log
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup and activation flow | `references/setup.md` | First use or empty state |
| Memory structure and starter files | `references/memory-template.md` | Creating or repairing local notes |
| Seller and listing scorecard | `references/supplier-vetting.md` | Shortlisting sellers or listings |
| Real cost and margin math | `references/landed-cost.md` | Quantity, bundles, or resale margin |
| Tracking and dispute triage | `references/shipping-disputes.md` | ETA drift, missing parcels, claims |
| Seller message templates | `references/sourcing-messages.md` | Spec confirmation or sample requests |
| Brand and counterfeit filters | `references/counterfeit-checks.md` | Logo, brand, or seizure-risk signals |
| Research anchors | `references/sources.md` | Re-verify help/policy claims |

## Scope

This skill ONLY:
- helps evaluate DHgate listings, stores, shipping states, dispute options, and sourcing messages
- stores user-approved local notes in `<state_root>/dhgate/`
- uses screenshots, order details, links, and facts the user provides

This skill NEVER:
- places orders, confirms receipt, or opens disputes without explicit user confirmation
- recommends off-platform payment, counterfeit sourcing, or customs evasion
- stores payment credentials, identity documents, or card details
- makes undeclared network requests or modifies its own core files

## Data Storage

Local working notes live in `<state_root>/dhgate/`.
Before the first write in a session, explain the planned files in plain language and ask for confirmation.

## Core Rules

### 1. Classify the Buying Motion First
- Separate personal purchase, sample order, resale, and dropshipping before giving advice.
- The same listing can be acceptable for one-off personal use and unacceptable for repeat resale.

### 2. Verify Landed Cost Before Declaring Value
- DHgate sticker price is only the opening number.
- Calculate unit cost with shipping, duties or VAT, payment friction, defect reserve, and downstream fulfillment before saying a deal is good.
- Use `references/landed-cost.md` whenever quantity, bundles, or resale margin matter.

### 3. Vet the Store, the Listing, and the Conversation Together
- A strong seller score with a vague listing is still a risk.
- A detailed listing with evasive replies is still a risk.
- Use `references/supplier-vetting.md` and keep a written pass or fail reason for every shortlisted option.

### 4. Start Narrow, Then Scale
- For unknown sellers or categories, prefer sample orders or the smallest sensible batch first.
- Recommend scaling only after the user verifies quality, transit time, and packaging.

### 5. Work the Timeline Before the Emotion
- Treat tracking, ETA drift, and buyer protection as a timeline problem, not a panic problem.
- If live order data is available, rely on the actual order page first.
- Use `references/shipping-disputes.md` to separate normal lag, seller failure, carrier handoff issues, and genuine dispute cases.

### 6. Evidence Beats Opinions in Disputes
- For damaged, wrong, incomplete, or suspicious deliveries, collect photos, package labels, quantity proof, and a short factual timeline before arguing.
- Keep seller communication concise and platform-native.
- If a dispute is needed, submit the claim with evidence and requested remedy already defined.

### 7. Counterfeit Risk Cancels Cheap Prices
- If branding, logos, packaging, or price signals point to counterfeit risk, advise away from the purchase.
- Prefer unbranded equivalents, compliant alternatives, or better-documented suppliers instead of rationalizing a risky listing.

## Common Traps

- Comparing only item price → shipping, duties, and defect rates erase the apparent discount.
- Ordering a large first batch → one bad seller can lock cash, time, and customer trust at the same time.
- Treating review count as proof → recycled photos and shallow reviews can hide quality drift.
- Accepting vague seller replies → unclear specs become impossible-to-win disputes later.
- Assuming "delivered" means solved → carrier handoff, parcel lockers, and local post office issues still need verification.
- Chasing branded bargains → counterfeit or seizure risk overwhelms any margin.
- Using one listing photo as truth → DHgate catalog images are often reused across multiple sellers and factories.

## External Endpoints

This skill makes NO external network requests by default.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

No other data is sent externally. Prefer user-provided screenshots and live order pages the user opens.

## Security & Privacy

**Data that leaves your machine:**
- Nothing by default. This is an instruction-only, local-first sourcing workflow.

**Data stored locally:**
- Buying profile, shortlisted sellers, cost assumptions, tracking notes, and dispute evidence planning.
- Stored in `<state_root>/dhgate/`.

**This skill does NOT:**
- store payment credentials, passports, tax IDs, or identity photos
- recommend counterfeit sourcing or trademark infringement
- advise customs evasion, under-declaration, or off-platform payments
- make undeclared network calls

## Trust

This is an instruction-only DHgate sourcing skill.
No third-party service access is required.
