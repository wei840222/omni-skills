---
name: real-estate-investing
description: Evaluate buy-and-hold, BRRRR, flip, and value-add real estate investments with conservative underwriting, debt stress tests, and diligence gates. Use when choosing or comparing investment properties.
metadata:
  openclaw: '{"emoji":"🏘️"}'
---

## State location

State may exist in `<workspace>/real-estate-investing/`, `<workspace>/memory/real-estate-investing/`, or `~/real-estate-investing/`. Before any state operation, use an explicitly configured path when available; otherwise select the first existing directory in that order. If none exists and persistent state is needed, create `<workspace>/real-estate-investing/`. Use the selected `<state_root>` consistently for this invocation; if multiple candidates exist, use only the highest-precedence directory and report the conflict.

## When to Use

Use this skill when a user is evaluating real estate investing decisions such as buy-and-hold rentals, value-add deals, BRRRR projects, flips, or house hacks.

Agent handles strategy selection, return targets, deal triage, underwriting, financing pressure tests, diligence sequencing, portfolio fit, and exit discipline.

## Architecture

Memory lives in `<state_root>/`. If `<state_root>/` does not exist, run `references/setup.md`. See `references/memory-template.md` for the baseline structures.

```text
<state_root>/
├── memory.md         # Strategy, guardrails, and active priorities
├── pipeline.md       # Deals under review with current stage and blockers
├── markets.md        # Market notes, rent assumptions, and local risks
├── decisions.md      # Won/lost deals, post-mortems, and pattern updates
└── archive/          # Inactive ideas and old deal records
```

## Quick Reference

| Topic | File | Use it for | When to load |
|-------|------|------------|--------------|
| Execution rules, loops, and traps | `references/execution-rules.md` | Core rules, deal loops, and traps to avoid | When executing a deal analysis |
| First-run activation | `references/setup.md` | Consent-aware activation and state setup | When the user wants recurring deal tracking |
| Memory baseline | `references/memory-template.md` | Initialize state files and data semantics | When creating persistent state |
| Strategy and buy box | `references/thesis-and-box.md` | Define goals, market focus, and non-negotiable filters | During specific task execution |
| Strategy fit and return targets | `references/strategy-selection.md` | Match investing styles to capital, time, and risk | During specific task execution |
| 30-second screening | `references/deal-triage.md` | Reject weak deals before deep work | During specific task execution |
| Underwriting model | `references/underwriting.md` | Revenue, expenses, reserves, and scenario stress tests | During specific task execution |
| Debt and downside | `references/financing-and-risk.md` | Loan structure, DSCR, reserves, and refinance risk | During specific task execution |
| Diligence workflow | `references/diligence-and-red-flags.md` | Documents to request and kill-shot risks | During specific task execution |
| Operations and exits | `references/portfolio-ops.md` | Management, capex planning, and sell-or-hold triggers | During specific task execution |

## Requirements

- No credentials or external services required by default.
- Ask before storing exact addresses, personal legal names, lender documents, or tax IDs.
- Treat legal, tax, insurance, and lending guidance as decision support, not licensed advice.

## Investor Lane

This skill is for investment decisions, not broad real-estate generalism.

- Use this skill for return-driven property choices, capital allocation, rentability, strategy fit, leverage risk, and portfolio growth decisions.
- Route requests for generic buyer, seller, agent, or landlord workflows that are not investment-led.
- If the user mainly needs transaction help outside investing, route to `real-estate-skill`, `home-buying`, or `rental` as appropriate.

## Data Storage

Local state lives in `<state_root>/`:

- the local strategy memory file for buy box and recurring guardrails
- the local pipeline file for active deals and blockers
- the local market-notes file for rents and recurring local risks
- the local decisions log for won/lost deals and post-mortems
- `archive/` for inactive opportunities and old decision logs

## Security & Privacy

**Data that stays local:**
- strategy preferences, underwriting assumptions, market notes, and decision logs in `<state_root>/`

**Data that leaves your machine:**
- None by default. Always ask for explicit permission before sending data out.

**Restricted actions (route elsewhere):**
- place offers, sign contracts, or move money
- claim jurisdiction-specific legal or tax certainty without source material
- submit lender or insurance applications automatically
- store secrets, bank logins, or full identity packages
- modify its own `SKILL.md`

## Scope

This skill ONLY:
- helps choose the right investing strategy before analyzing properties
- helps analyze and compare real estate investment opportunities
- keeps local memory about strategy, markets, and deal outcomes
- improves decisions through explicit assumptions, stress tests, and post-mortems

Restricted actions (route elsewhere):
- act as a generic buyer, seller, or agent assistant
- guarantee returns
- replace licensed legal, tax, insurance, or lending advice
- recommend a deal without stating key assumptions and failure points
