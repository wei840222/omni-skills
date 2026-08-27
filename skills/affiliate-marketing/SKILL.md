---
name: affiliate-marketing
description: Design and optimize affiliate programs with partner scoring, commission economics, tracking QA, fraud controls, and compliance reviews. Trigger when the user needs affiliate marketing management, partner recruitment, affiliate tracking, or affiliate operations.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🤝","requires":{"configPaths":["<state_root>/"]}}'
  related-skills: '{"cmo":"Channel strategy, demand generation, and marketing leadership.","content-marketing":"Content partner enablement and repurposing systems.","email-marketing":"Nurture sequences and owned-audience conversion.","growth-hacker":"Acquisition experiments and growth loops.","market-research":"Partner landscape, vertical mapping, and competitor analysis."}'
---

## State location

Affiliate Marketing state may exist in `<workspace>/affiliate-marketing/`, `<workspace>/memory/affiliate-marketing/`, or `~/affiliate-marketing/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/affiliate-marketing/`, `<workspace>/memory/affiliate-marketing/`, `~/affiliate-marketing/`.
3. If none exists and state must be created, default to `<workspace>/affiliate-marketing/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` for integration guidelines. This skill works without local storage. Only create `<state_root>/` if the user wants persistent partner and program continuity.

## When to Use

User needs affiliate marketing, affiliate program management, partner recruitment, affiliate tracking, or affiliate operations. Agent handles program design, partner scoring, outreach packs, commission economics, tracking QA, attribution conflicts, fraud review, and reporting.

Use this when the problem is operating an affiliate channel end to end, not just generating links or listing networks. The goal is to turn partner revenue into a controlled acquisition engine with better unit economics and lower compliance risk.

This skill is especially strong for ecommerce, SaaS, creators with affiliate offers, and brands running publishers, coupon partners, creators, or referral-style affiliates under one program.

## Architecture

Local workspace is optional and only created with user consent.

```
<state_root>/
├── memory.md        # Program context, approved rules, active constraints
├── partners.md      # Pipeline, status, offer history, next actions
├── economics.md     # Commission ceilings, margins, payout scenarios
└── incidents.md     # Fraud flags, attribution disputes, compliance notes
```

## Quick Reference

| Topic | When to load | File |
|-------|--------------|------|
| Setup and activation | On first use to learn constraints and optional state. | `references/setup.md` |
| Continuity memory | When user wants persistent state across sessions. | `references/memory.md` |
| Program design and offer structure | Before approving partner outreach or changing commissions. | `references/program-design.md` |
| Partner sourcing and outreach pipeline | When evaluating, recruiting, or ranking affiliates. | `references/partner-pipeline.md` |
| Commission economics and payout logic | Before recommending higher payouts or analyzing margins. | `references/economics.md` |
| Tracking, attribution, and compliance | When validating campaigns, handling attribution disputes, or launching. | `references/tracking-compliance.md` |
| Fraud detection and payout QA | Before approving payouts or investigating abnormal volume spikes. | `references/fraud-qa.md` |
| Lifecycle management and reporting | For weekly reviews, program ops, and partner segmentation. | `references/lifecycle-reporting.md` |
| Launch and recovery playbooks | When taking immediate execution actions for sprints. | `references/playbooks.md` |

## Core Rules

### 1. Design the program before recruiting partners
- Define partner types, payout model, approval rules, attribution window, restricted traffic sources, and clawback rules first.
- Recruitment without governance creates low-quality growth, conflict with other channels, and messy payouts.
- Use `references/program-design.md` before approving partner outreach or commissions.

### 2. Score partners on fit, economics, and risk together
- Evaluate audience fit, traffic quality, historical credibility, commission appetite, and brand safety at the same time.
- A partner with reach but bad economics or compliance risk is not a win.
- Use `references/partner-pipeline.md` to rank who should be recruited, activated, paused, or rejected.

### 3. Protect margin before scaling payouts
- Model gross margin, refund rate, AOV, LTV, clawbacks, and cannibalization before recommending higher commissions.
- Raw affiliate revenue can hide unprofitable traffic or orders that would have converted anyway.
- Use `references/economics.md` to set commission ceilings and bonus rules.

### 4. Treat tracking QA as launch-critical
- Validate links, coupon mapping, attribution logic, landing destinations, and UTM naming before traffic goes live.
- Broken tracking destroys trust with partners and makes optimization impossible.
- Use `references/tracking-compliance.md` whenever a campaign, offer, or payout structure changes.

### 5. Block fraud and leakage early
- Watch for self-referrals, trademark bidding, cookie stuffing, coupon leakage, bot traffic, fake leads, and suspicious payout spikes.
- Proactively audit for abuse and halt suspicious payouts before budgets are depleted.
- Use `references/fraud-qa.md` before approving payouts or scale decisions.

### 6. Run affiliate lifecycle as an operating system
- Manage recruitment, onboarding, activation, creative refresh, performance coaching, reactivation, and offboarding as one loop.
- The skill should always know the next best action for each partner and segment.
- Use `references/lifecycle-reporting.md` for weekly reviews and partner portfolio decisions.

### 7. Escalate claims, disclosures, and restricted actions
- Treat trademark use, hard earnings claims, regulated verticals, SMS/email consent, and geo-specific disclosure rules as approval moments.
- Ensure all claims use verifiable proof, clearly disclose incentive relationships, and reflect genuine urgency.
- Use `references/tracking-compliance.md` and `references/playbooks.md` for review gates before launch.

## Operating Rhythm

### Before launch
- Lock partner type, offer structure, landing path, attribution method, and disclosure rules.
- Validate links, payouts, and restricted terms before any partner goes live.

### Weekly
- Review recruitment pipeline, activations, partner quality, conversion quality, reversals, and payout exposure.
- End each week with keep, fix, scale, pause, and remove decisions.

### Monthly
- Re-price commissions, reclassify partner tiers, and audit whether affiliate revenue is incremental or cannibalized.
- Refresh creative, landing pages, and partner enablement before adding more partners.

## Common Traps

- Recruiting everyone with traffic -> partner count rises while quality and margin collapse.
- Paying high commissions without incrementality checks -> revenue grows on paper but profit weakens.
- Letting coupons, creators, and content affiliates share one sloppy attribution model -> channel conflict and payout disputes.
- Ignoring disclosure and trademark rules -> legal exposure and program trust damage.
- Launching with broken links or weak landing pages -> partner confidence drops and traffic is wasted.
- Looking only at clicks or affiliate-attributed revenue -> hides refunds, fraud, leakage, and cannibalization.

## Security & Privacy

**Data that stays local when the user opts in:**
- Program rules, partner notes, commission assumptions, and payout concerns in `<state_root>/`
- Fraud flags, compliance notes, and reporting summaries in local markdown files

**This skill does NOT:**
- Automatically create affiliate accounts, send outreach, or change payouts
- Create local files without explicit user consent
- Access networks, ESPs, analytics tools, or payment systems unless the user explicitly requests a separate approved tool workflow
- Make undeclared network requests

**Guardrails:**
- Treat sensitive partner data, payout details, and customer-level data as restricted
- Escalate legal or policy-sensitive promotions for review before launch
