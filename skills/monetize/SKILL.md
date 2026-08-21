---
name: monetize
description: Build evidence-based pricing, launch, and revenue plans for indie products, SaaS, mobile apps, and creators. Use when a user needs to choose a monetization model, price or package an offer, prepare a launch, measure unit economics, or evaluate a revenue experiment; use finance, legal, or implementation-specific guidance for tax, legal, or SDK decisions.
metadata:
  openclaw: '{"emoji":"💰"}'
---

# Monetize

Turn a product and its evidence into a testable revenue decision. Start with the user's market, customer, product value, current traction, costs, region, and constraints; ask for the missing inputs that change the recommendation.

## Workflow

1. **Classify the request.** Read one matching guide: mobile app → `references/mobile-apps.md`; SaaS/subscription → `references/saas.md`; creator sponsorships or audience products → `references/creator.md`; pricing → `references/pricing.md`; launch → `references/launch.md`; reusable copy → `references/templates.md`.
2. **Collect decision inputs.** Capture customer, job-to-be-done, value evidence, current alternatives, costs, market/region, capacity, and constraints. Mark unknown inputs rather than inventing them. Use `references/success.md` for operating patterns, not forecasts.
3. **Recommend one testable offer.** Specify package, price or range, value metric, and why it matches the evidence. Use `references/pricing.md` for the economics and `references/industry-benchmarks.md` for current policy-sensitive assumptions.
4. **Define the learning loop.** Set a primary metric, a guardrail (such as refunds, churn, support load, or complaint rate), audience/eligibility, decision rule, and review date. Change one material variable at a time.
5. **Return a decision packet.** Include recommendation, assumptions, math, test plan, launch sequence or template, risks, and next measurement date. Describe uncertainty plainly when evidence is thin.

### Output format

```text
Decision: [offer, price/range, and customer]
Evidence and assumptions: [known facts + explicit unknowns]
Economics: [formula inputs and result]
Experiment: [hypothesis, primary metric, guardrail, audience, decision rule]
Execution: [launch steps or selected template]
Risks and next review: [policy/compliance/capacity checks + date]
```

## Decision Principles

- Package outcomes and constraints before optimizing a price number.
- Treat stated interest as a lead; use completed payments or other defined commitment events as validation evidence.
- Keep offers, scarcity, guarantees, and testimonials truthful and operationally supportable.
- Preserve a customer path to manage billing, cancellation, refunds, and support.
- Use current platform documentation and jurisdiction-specific professional advice for payments, taxes, consumer protection, privacy, and advertising disclosures.

## Reference map

| Need | Read |
|---|---|
| Pricing research, economics, packaging, experiments | `references/pricing.md` |
| SaaS model, value metric, expansion, churn | `references/saas.md` |
| Mobile store model, paywall, offers, platform checks | `references/mobile-apps.md` |
| Audience products, sponsorships, memberships | `references/creator.md` |
| Validation and launch sequence | `references/launch.md` |
| Adaptable customer copy | `references/templates.md` |
| Operating patterns and limits of anecdotal advice | `references/success.md` |
| Freshness classes and authoritative research links | `references/research-sources.md` |

## Trigger boundary

Use this skill for a product or offer revenue decision. Route tax filing, legal interpretation, payment integration, financial reporting, and ad-buy execution to the relevant specialist guidance; this skill can supply the commercial brief those tasks need.
