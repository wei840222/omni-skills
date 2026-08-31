---
name: betting
description: Evaluate betting opportunities with line shopping, bankroll discipline, market checks, and risk filters before any stake is placed.
metadata:
  openclaw: '{"requires":{"config":["<state_root>/betting/"]}}'
  related-skills: '{"decide":"structure tradeoffs and pass-or-proceed decisions without hype","legal":"tighten wording when the user asks about compliance, terms, or risk boundaries","pricing":"reason about price quality when the user needs cleaner expected value language","trader":"frame discipline, journaling, and risk control for repeated decision making"}'
---

## When to Use

Betting questions involving sports, props, parlays, exchanges, or prediction-style tickets where price, edge, and stake size matter. Agent handles market normalization, implied probability math, line comparison, sizing discipline, and quick rejection of bad bets.

## State location

This skill uses stateful configuration to store user preferences and ticket tracking:
- Candidate location: `<state_root>/betting/` (e.g., `workspace/.state/betting/`).
- Lookup order: Follows standard workspace-first state convention.
- Behavior: If the directory does not exist, initialize it using `references/setup.md`.

## Architecture

Memory lives in `<state_root>/betting/`. If `<state_root>/betting/` does not exist, run `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/betting/
├── memory.md        # Preferences, books, and activation rules
├── tickets.md       # Active or reviewed bets and follow-ups
├── market-notes.md  # Sports, books, and recurring edge notes
└── archive/         # Old tickets and retired observations
```

## Data Storage

- `<state_root>/betting/memory.md` stores activation rules, preferred sports, and user-stated constraints
- `<state_root>/betting/tickets.md` stores active or reviewed ticket notes when the user wants tracking
- `<state_root>/betting/market-notes.md` stores recurring market observations that improve future analysis
- `<state_root>/betting/archive/` stores older notes that no longer need to stay hot

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup guide | `references/setup.md` | When setting up or initializing state |
| Memory template | `references/memory-template.md` | When formatting state notes |
| Clean Ticket Protocol | `references/workflow.md` | When analyzing a new ticket |
| Market integrity checks | `references/market-checks.md` | When verifying market validity |
| Bankroll and sizing rules | `references/sizing.md` | When deciding bet size |
| Reusable ticket memo | `references/ticket-template.md` | When formatting ticket output |
| Fast rejection list | `references/red-flags.md` | When checking for immediate rejects |
| Domain knowledge | `references/domain.md` | When reasoning about probability or Kelly sizing |
| Core rules | `references/core-rules.md` | When needing fundamental betting principles |
| Market Lens | `references/market-lens.md` | When analyzing specific market types |
| Common Traps | `references/common-traps.md` | When reviewing potential analytical errors |
| Legal and responsible use | `references/legal.md` | When dealing with legal, terms, or compliance |

## Requirements

- No account auth required
- No extra binaries required
- Live odds or injury news only when the user provides data or explicitly asks to fetch public information
- The user is responsible for legal age, jurisdiction, operator rules, and local compliance

## Clean Ticket Protocol

Use the full workflow in `references/workflow.md`. Every ticket should pass this order:

1. Define the exact market, book, line, price, stake, and settlement rule
2. Normalize odds and break-even probability with `references/sizing.md`
3. Check market integrity, limits, and void rules with `references/market-checks.md`
4. Run the fast rejection list in `references/red-flags.md`
5. Return an analysis memo using `references/ticket-template.md`: positive edge, reduce size, wait, or pass









## Scope

This skill ONLY:
- Analyzes bets, prices, and sizing discipline
- Stores user-stated preferences and notes in `<state_root>/betting/`
- Uses `references/workflow.md`, `references/market-checks.md`, `references/sizing.md`, `references/ticket-template.md`, and `references/red-flags.md` for repeatable analysis
- Identifies when the right answer is no bet, smaller size, or wait

Out of scope capabilities:
- Places bets, logs into books, or moves funds
- Stores login details, wallet recovery phrases, or account recovery data
- Helps bypass age, jurisdiction, KYC, AML, or self-exclusion controls
- Promotes profit, certainty, or personalized financial suitability
- Hides uncertainty when lines, rules, or data are incomplete

## Security & Privacy

**Data that leaves your machine:**
- None by default
- If the user explicitly asks for live public information, only the markets, teams, players, or books needed for that request

**Data that stays local:**
- Preferences, tickets, and notes in `<state_root>/betting/`

**This skill does NOT:**
- Store login details
- Read unrelated files
- Make undeclared network requests

