---
name: product
description: >
  Build and launch digital or physical products end-to-end: validate demand,
  prioritize features (RICE/ICE/Kano), track PMF and SaaS metrics, price with
  fee-aware margins, generate AI product imagery, and meet Amazon/Etsy/POD
  listing specs. Use when the user needs product strategy plus marketplace or
  visual execution in one flow. Prefer product-manager for pure PM process,
  pricing for deep B2B list-price math, saas for subscription ops metrics,
  amazon/etsy for channel-only ops, and indie-hacker for solo bootstrap sequencing.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📦","displayName":"Product"}'
  related-skills: '{"product-manager":"Pure PM discovery, roadmaps, and PRD craft without marketplace imagery.","pricing":"Deep B2B/SaaS list-price design and WTP research beyond fee-aware product margins.","saas":"Subscription MRR/NRR ops and packaging once the product is recurring.","indie-hacker":"Solo founder validation and time protection for side projects.","amazon":"Amazon buyer/seller ops beyond product listing image and FBA launch checklists.","etsy":"Etsy listing diagnostics and shop growth beyond cross-channel product launch.","product-launch":"Launch sequencing and go-to-market when the build is already decided.","growth":"Acquisition funnels after PMF and retention math are sound."}'
---

# Product

Own **product creation workflows** that span validation → prioritization → metrics → pricing → AI visuals → marketplace listing specs for SaaS and physical goods.

This skill is **knowledge-only**. It does not create or require a persistent state tree. Do not write runtime notes into this package.

## When to use

- Validating an idea, running Mom Test interviews, or checking Sean Ellis PMF
- Prioritizing features with RICE, ICE, MoSCoW, or Kano
- Tracking SaaS metrics (MRR, NRR, LTV:CAC) or stage-based focus
- Fee-aware pricing for Amazon, Etsy, Shopify, or POD margins
- AI product photography, mockups, and platform image specs
- Amazon FBA listing basics, Etsy SEO structure, or multi-platform POD export

Prefer adjacent skills when they fit better:

- Pure PM process / PRDs / stakeholder craft → `product-manager`
- Deep list-price math and WTP studies → `pricing`
- Subscription billing ops and NRR movement → `saas`
- Solo bootstrap time protection → `indie-hacker`
- Amazon-only or Etsy-only shop ops → `amazon` / `etsy`

## Progressive disclosure

| Need | Load |
|------|------|
| Core workflows and critical rules | `references/domain.md` |
| Idea validation, Mom Test, PMF survey | `references/validation.md` |
| Feature prioritization frameworks | `references/prioritization.md` |
| Revenue, retention, engagement metrics | `references/metrics.md` |
| Pricing models and platform fee math | `references/pricing.md` |
| AI imagery tool selection | `references/ai-tools.md` |
| Product photo prompt templates | `references/prompts.md` |
| Platform image dimensions | `references/specs.md` |
| Amazon FBA listing and PPC basics | `references/amazon.md` |
| Etsy listing, fees, ranking | `references/etsy.md` |
| Print-on-demand multi-platform | `references/pod.md` |
| Manufacturing compliance by region | `references/compliance.md` |
| Gate 6 research anchors | `references/sources.md` |

## Core workflows

**Digital (SaaS):** validate → define one-value MVP → prioritize → beta → measure PMF (Sean Ellis 40%+ very disappointed) before scaling spend.

**Physical goods:** DFM-aware design → regional compliance → photography → platform listing specs → limited launch.

**Merch / POD:** highest-res master → AI mockups → platform-specific export sizes → multi-channel list with fee-aware price.

## Critical rules

1. **Validate before building** — past behavior and paid signal beat compliments.
2. **Platform specs are hard gates** — wrong dimensions or white-background rules reject listings.
3. **Price after fees** — quote retail only after Amazon/Etsy/POD cuts and desired margin.
4. **PMF before scale** — treat Sean Ellis ≥40% "very disappointed" (adequate sample) as a scale gate, not a slogan.
5. **Verify live vendor limits** — fee tables, image minima, and tool pricing change; open `references/sources.md` and the linked official page before locking a number in a customer-facing answer.
6. **Route deep specialties** — do not re-implement `pricing`, `saas`, `amazon`, or `etsy` full ops inside this skill.

## Failure modes

| Symptom | Recovery |
|---------|----------|
| User wants only roadmap/PRD craft | Hand off to `product-manager` |
| User needs Stripe/dunning/NRR rebuild | Hand off to `saas` / `billing` |
| Exact Amazon/Etsy fee or image rule disputed | Open official Seller Central / Etsy policy URL from `references/sources.md`; do not invent |
| AI tool tier price quoted from memory | Treat as orientation; confirm on vendor pricing page |
| Feature priority without a metric | Require Reach/Impact/Effort inputs or switch to MoSCoW for release scope |
