---
name: home-buying
description: Buy a home with budget guardrails, listing scorecards, offer strategy,
  due diligence triage, and closing readiness checks.
metadata:
  openclaw: '{"emoji": "🏠", "requires": {"config": ["<state_root>/"]}}'
  related-skills: '{"real-estate-skill":"Broader real-estate transaction guidance across roles and stages when the task is not a primary-home purchase decision system.","property-valuation":"Comparable and income-based valuation support when pricing or appraisal gaps dominate.","contract":"Contract structure and clause review when offer language or contingencies need legal-structure scrutiny.","rental":"Rental economics when the user should compare buy vs rent or landlord/tenant economics instead.","house":"Post-purchase home ownership operations after closing."}'
---
## Setup

If `<state_root>/` does not exist or is empty, read `references/setup.md`, explain what will be stored, and ask for confirmation before creating files.

## When to load

Load this skill when a user explicitly asks for help buying a home, organizing real estate budgets, evaluating property listings, or preparing to close on a house. Load this only when a purchase intent exists (exclude general market trends).

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure and status fields.

```text
<state_root>/
|-- memory.md             # Decision defaults, status, and recurring constraints
|-- active-deals.md       # Deal pipeline with stage and risk notes
|-- offer-log.md          # Offer ladder history and outcomes
`-- closing-checks.md     # Lender, title, insurance, and final walkthrough status
```


## Reference Loading

When you need to perform specific tasks, read the corresponding reference file before proceeding:
- For calculating budgets and limits: read `references/budget-guardrails.md`
- For evaluating new property listings: read `references/listing-scorecard.md`
- For building offer strategies and negotiation limits: read `references/offer-ladder.md`
- For prioritizing inspections and contingencies: read `references/due-diligence.md`
- For final walkthroughs and closing checks: read `references/closing-readiness.md`
- For source-backed affordability, inspection, or closing claims: read `references/domain-knowledge.md`

## Quick Start

Use this workflow in order:
1. Define `buy-box` and monthly guardrails.
2. Score listings using one scoring rubric.
3. Build a tiered offer ladder before writing any offer.
4. Run inspection and document risk transfer plan.
5. Gate closing on a readiness checklist.

## Quick Reference

Use the smallest relevant file for the current step.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory template | `references/memory-template.md` |
| Budget math and guardrails | `references/budget-guardrails.md` |
| Listing scoring rubric | `references/listing-scorecard.md` |
| Offer strategy and concessions | `references/offer-ladder.md` |
| Inspection and contingency triage | `references/due-diligence.md` |
| Closing readiness gates | `references/closing-readiness.md` |
| Domain sources (Gate 6) | `references/domain-knowledge.md` |

## Core Rules

### 1. Build the Buy Box Before Browsing
- Define non-negotiables (location radius, bedroom count, commute cap, property type) before reviewing listings.
- Add hard no-go criteria and keep them fixed for at least one week to reduce impulse drift.

### 2. Underwrite Total Monthly Cost, Not List Price
- Use all-in monthly cost: principal, interest, taxes, insurance, HOA, utilities estimate, and maintenance reserve.
- Reject properties that break the monthly guardrail unless the user explicitly approves a revised ceiling.

### 3. Score Listings With One Rubric
- Apply the same weighted scorecard to every candidate property.
- If a listing is selected against scorecard output, mark it as an exception and document the reason.

### 4. Use a Tiered Offer Ladder
- Build Plan A, Plan B, and walk-away offer numbers before contacting seller side.
- Each tier must include price, contingency set, credits target, and maximum concession risk.

### 5. Treat Due Diligence as Risk Transfer
- Convert each inspection issue into one of three actions: seller fix, seller credit, or buyer accepts risk.
- No unresolved high-severity issue should survive to final commitment without explicit sign-off.

### 6. Protect Timeline and Financing Certainty
- Keep a dated checklist for lender docs, appraisal milestones, title items, and insurance binders.
- Flag any critical path delay immediately and propose a concrete recovery action.

### 7. Keep a Decision Log for Every Deal
- Store offers, counter terms, rejected options, and post-mortem notes in memory.
- Reuse these patterns to improve future offers and prevent repeating avoidable mistakes.

## Home-Buying Traps

- Shopping first, budgeting later -> overexposure and rushed compromises.
- Chasing low rate headlines without full closing-cost math -> misleading affordability.
- Waiving inspection blindly in competitive markets -> asymmetric downside.
- Negotiating only on price -> missed credits, repairs, or timeline value.
- Ignoring neighborhood-level signals (insurance trends, HOA health, permit patterns) -> hidden future cost.
- Accepting lender or title delays as "normal" -> preventable closing failures.

## Data Storage

- Local notes only in `<state_root>/` for active deals, scorecards, and decision history.
- Store concise operational data, not full personal identity packages.
- Ask before saving sensitive personal or financial details.

## Security & Privacy

Data that leaves your machine:
- None by default. This skill is workflow guidance and local-memory only.

Data that stays local:
- Decision context, deal notes, and checklist state under `<state_root>/`.

This skill does NOT:
- Submit offers automatically.
- Call lender, MLS, escrow, or title APIs automatically.
- Share user data with external services by default.
- Modify files outside `<state_root>/` for memory.
- Maintain its own skill definition file as read-only.
