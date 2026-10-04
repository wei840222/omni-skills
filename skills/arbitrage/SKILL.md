---
name: arbitrage
description: >
  Evaluate cross-venue price gaps, surebets, hedges, basis trades, and multi-leg
  baskets with fee-aware net edge, fill sequencing, and settlement checks. Use
  when the user asks about arbitrage, locked spreads, surebets, mispricing, or
  soft locks across books, prediction markets, crypto venues, or retail channels.
  Not for pure technical analysis without a second leg (`trading`), long-horizon
  portfolio construction (`invest`), or B2B SaaS list-price design (`pricing`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⚖️","requires":{"config":["<state_root>"]}}'
  related-skills: '{"trading":"Single-venue charting, TA, and position sizing without a locked second leg.","trader":"Execution desk workflow once a structure is already classified.","pricing":"B2B SaaS packaging and list price, not cross-venue arb.","invest":"Long-horizon allocation and portfolio construction outside locked spreads."}'
---

## When to Use

Load this skill when the user evaluates an apparent price gap, hedge, surebet, basis trade, multi-leg basket, or cross-venue spread and needs fee-aware math plus settlement discipline.

## Architecture

State and configuration live in `<state_root>/`.
Load `references/setup.md` if `<state_root>/` does not exist.
See `assets/memory-template.md` for structure.

```text
<state_root>/
├── memory.md         # Preferences, constraints, and activation rules
├── opportunities.md  # Active ideas, status, and next checks
├── venue-notes.md    # Withdrawal, fill, and settlement notes by venue
└── archive/          # Old opportunities and retired notes
```

## Quick Reference

| Topic | Instruction |
|-------|-------------|
| Setup guide | Load `references/setup.md` |
| Memory template | Load `assets/memory-template.md` |
| Locked Spread Protocol | Load `references/workflow.md` |
| Fee-aware formulas | Load `references/calculator.md` |
| Venue and settlement checks | Load `references/venue-checks.md` |
| Scenario playbooks | Load `references/playbooks.md` |
| Safe language and disclaimers | Load `references/legal.md` |
| Research sources | Load `references/sources.md` |

## Requirements

- No credentials required.
- No extra binaries required.
- Live market data only when the user provides it or explicitly asks you to fetch it.
- Analysis and trade structure only; not personalized financial, legal, or tax advice.

## Instructions

1. Load `references/workflow.md` immediately for any new opportunity (Locked Spread Protocol).
2. Write every leg with venue, instrument, side, price, size limit, timestamp, and settlement rule.
3. Normalize fees, spread, financing, transfer, FX, and other known drag with `references/calculator.md` before calling anything edge.
4. Run `references/venue-checks.md` for resolution language, voids, depth, withdrawal, and region/KYC limits.
5. Classify hard lock vs soft lock vs expected value; reject fake edge (stale quotes, promo-only, incomplete outcome partitions).
6. Output a structured decision memo: net edge, sequence, weakest venue, kill conditions, and size constraints.
7. Use `references/legal.md` phrasing; maintain an objective analytical stance without guarantees or personalized advice.
8. Persist only user-stated preferences and repeated failure modes under `<state_root>/` using `assets/memory-template.md`.

## Safety Boundaries

- Prefer net edge over gross edge; never label a trade locked until settlement rules match.
- Cap or reject when withdrawal latency, size caps, or void asymmetry break the hedge path.
- Strip credentials and account identifiers before writing anything under `<state_root>/`.
- If legs do not resolve to the same economic outcome, downgrade to watchlist or reject.
