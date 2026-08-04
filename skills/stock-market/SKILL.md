---
name: stock-market
description: Analyze stocks with thesis validation, catalyst timing, position sizing, and explicit trade or no-trade decisions. Use when the user wants stock analysis, pre-market or post-market briefings, watchlist planning, trade thesis validation, catalyst tracking, or risk-managed execution planning for individual equities or ETFs.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📈"}'
  related-skills: '{"business-intelligence":"Converts market analysis outputs into dashboards and decision reporting.","economics":"Interprets macro indicators and policy signals that move markets.","market-research":"Builds sector and theme landscape analysis that feeds stock-level thesis work.","trading":"Structures trade execution plans and operational checklists for approved candidates."}'
---

## State location

Stock market state may exist in `<workspace>/stock-market/`, `<workspace>/memory/stock-market/`, or `~/stock-market/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/stock-market/`, `<workspace>/memory/stock-market/`, `~/stock-market/`.
3. If none exists and state must be created, default to `<workspace>/stock-market/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>`. See `references/memory.md` for structure.

```
<state_root>/
├── memory.md         # Status, constraints, and recurring preferences
├── watchlist.md      # Active tickers and setup notes
├── briefing-log.md   # Pre-market and post-market summaries
└── risk-rules.md     # Position sizing and risk guardrails
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup and integration | `references/setup.md` | First run or when `<state_root>` is missing/empty |
| Memory template | `references/memory.md` | Creating or updating `<state_root>/memory.md` |
| Analysis workflow | `references/analysis.md` | Validating a ticker thesis or building a trade candidate |
| Watchlist structure | `references/watchlist.md` | Building or re-ranking the watchlist |
| Risk controls | `references/risk.md` | Before selecting position size or validating a trade |
| Daily briefing format | `references/briefing.md` | Creating pre-market or post-market briefings |

## Core Workflow

### Step 1: Define Objective
Set the objective before analysis: intraday trade, swing setup, position build, or no-trade monitoring. Every recommendation must match the selected horizon.

### Step 2: Separate Facts, Assumptions, and Narrative
Tag each statement as market data, inferred assumption, or narrative hypothesis. If the thesis depends on assumptions, list the proof needed before execution.

### Step 3: Anchor to Catalyst and Timing
Document the nearest catalyst window (earnings, macro release, company event, sector move) and timing risk. Require a clear catalyst or structural setup before entry.

### Step 4: Convert Thesis into Trigger and Invalidation
Define entry trigger, invalidation level, and expected path so the outcome can be judged objectively.

### Step 5: Enforce Position Risk
Load `references/risk.md` before selecting size. Apply the 2% rule: risk no more than 2% of account on any single trade.

### Step 6: Maintain Living Watchlist
Rank watchlist by setup quality, catalyst proximity, and risk-adjusted upside. Re-rank after major market events.

### Step 7: Post-Action Review
Log outcomes using `references/briefing.md` format and update `<state_root>/memory.md` with reusable lessons.

## 🔴 Pre-Trade Validation Gate

**Proceed only when all five checks pass:**

1. ✅ Thesis has ≥2 `A`-grade evidence lines (or 1× `A` + near-term catalyst)
2. ✅ Entry trigger, invalidation level, and target path are defined
3. ✅ Position size calculated via `references/risk.md` formula (max 2% account risk per trade)
4. ✅ Total open risk ≤ 5-6% of account, max 2-3 correlated positions
5. ✅ Decision logged in `<state_root>/briefing-log.md`

**Decision heuristic when checks fail:**
- Evidence insufficient → revise thesis, downgrade to watchlist
- Structure unclear → mark no-trade until clarity emerges

## Fallback Decision Tree

| Symptom | First-line fix | If still failing |
|---------|----------------|------------------|
| Thesis lacks `A`-grade evidence | Downgrade to watchlist-only | Wait for catalyst confirmation |
| No clear invalidation level | Use ATR-based stop (2× ATR from entry) | Mark no-trade until structure clarifies |
| Position size exceeds liquidity | Halve size, widen invalidation | Skip trade entirely |
| High volatility session | Cut size 30-50%, use limit orders only | Mark no-trade |
| Daily loss cap hit | Stop trading for session | Review rules before next session |
| Emotional override detected | Mark no-trade immediately | Take break, review process |

## Gotchas

- **Time commitment**: Allocate 5-10 hours for thorough thesis validation per company.
- **Gap risk**: Before earnings or major events, halve position size to account for overnight gap risk.
- **Correlation trap**: Max 2-3 concurrent correlated positions. Two tech stocks with the same risk driver count as one bet.
- **No-trade is a decision**: Log every no-trade outcome explicitly. This builds the learning loop from avoided losses.
- **Momentum ≠ thesis**: Require structural setup for momentum-based entries; define invalidation before entry.
- **Emotional override**: When daily loss cap is hit or emotional state overrides process, mark no-trade until next session.

## Operational Boundaries

- Require explicit user approval before executing trades
- Confine all file operations to `<state_root>`
- Store only explicit user preferences, not inferred ones
- Define invalidation level before proceeding with any trade
- Maintain consistent position sizing regardless of recent outcomes
- Log every trade and no-trade decision
- Check macro event calendar before entry
- Require ticker-specific evidence beyond broad market direction

## Security & Privacy

All data stays local in `<state_root>`. This skill produces analysis and planning artifacts only — it does not connect to brokers, place orders, or transmit data externally.
