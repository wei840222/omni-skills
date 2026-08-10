---
name: stock-market
description: Produce evidence-labelled equity research, dated market briefings, watchlists, and risk plans without broker access. Use when the user wants analysis of individual stocks or ETFs, a pre-market or post-market briefing, watchlist prioritization, thesis validation, catalyst tracking, or trade-planning support.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📈"}'
  related-skills: '{"business-intelligence":"Converts market analysis outputs into dashboards and decision reporting.","economics":"Interprets macro indicators and policy signals that move markets.","market-research":"Builds sector and theme landscape analysis that feeds stock-level thesis work.","trading":"Structures trade execution plans and operational checklists for approved candidates."}'
---

## State location

Stock market state may exist in `<workspace>/stock-market/`, `<workspace>/memory/stock-market/`, or `~/stock-market/`. `<workspace>` is the workspace root supplied by the host/runtime, not the shell's current working directory.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/stock-market/`, `<workspace>/memory/stock-market/`, `~/stock-market/`.
3. If multiple candidate directories exist, use only the first, tell the user that multiple state directories were found, and leave lower-precedence copies untouched.
4. If the host cannot supply `<workspace>`, do not substitute the shell's current working directory. Use an existing `~/stock-market/` only when it exists; otherwise ask the user or host to provide a state root before creating data.
5. If no candidate exists, default to `<workspace>/stock-market/` only after persistent state is enabled and the user approves the named first create or update.

Persistent state is enabled for an invocation only when the user explicitly requests retention or approves a named persistent write; selecting an existing `<state_root>` does not enable state or authorize a write. For every persistent create, update, or delete, name the exact path and proposed outcome and obtain the user's approval for that update. Use the selected `<state_root>` for every state operation during the invocation.

## State inventory

| Path | Role | Creation condition |
|------|------|--------------------|
| `<state_root>/memory.md` | Explicit preferences, constraints, and reusable lessons | Required once persistent state is enabled and the user approves the first memory write. |
| `<state_root>/watchlist.md` | Active tickers, setups, and ranking notes | Optional; create only when the user asks to retain a watchlist and approves that file. |
| `<state_root>/briefing-log.md` | Pre-market and post-market summaries | Optional; create only when the user asks to retain a briefing and approves that file. |
| `<state_root>/risk-rules.md` | User-approved sizing and exposure guardrails | Optional; create only when the user asks to retain risk rules and approves that file. |

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup and integration | `references/setup.md` | First run or when `<state_root>` is missing/empty |
| Memory template | `references/memory.md` | Creating or updating `<state_root>/memory.md` |
| Analysis workflow | `references/analysis.md` | Validating a ticker thesis or building a trade candidate |
| Watchlist structure | `references/watchlist.md` | Building or re-ranking the watchlist |
| Risk controls | `references/risk.md` | Before selecting position size or validating a trade |
| Daily briefing format | `references/briefing.md` | Creating pre-market or post-market briefings |
| Current-market verification | `references/market-data.md` | A request depends on live prices, news, earnings dates, or an "today" briefing |

## Core Workflow

### Step 1: Define Objective and Scope
Set the objective before analysis: intraday trade, swing setup, position build, or monitoring. Match the research horizon to that objective. This skill provides research and planning, not personalized investment advice or broker execution.

### Step 2: Separate Facts, Assumptions, and Narrative
Tag each statement as sourced market data, inferred assumption, or narrative hypothesis. Include the source and as-of time for market data. If the thesis depends on assumptions, list the proof needed before treating it as a candidate.

### Step 3: Verify Current Data and Catalyst Timing
For a live-data request, load `references/market-data.md`. Record the data source, timestamp, timezone, and nearest catalyst window (earnings, macro release, company event, or sector move). If current data cannot be verified, provide a reusable research template instead of presenting an undated plan as current.

### Step 4: Convert Thesis into Trigger and Invalidation
Define entry trigger, invalidation level, and expected path so the outcome can be judged objectively.

### Step 5: Model Position Risk
Load `references/risk.md` before calculating size. Use only a user-approved account-risk limit; if it is absent, keep the output un-sized or use clearly labelled hypothetical inputs.

### Step 6: Maintain Living Watchlist
Rank watchlist by setup quality, catalyst proximity, and risk-adjusted upside. Re-rank after major market events.

### Step 7: Post-Action Review
When persistent state is enabled and the user approves the update, log outcomes using `references/briefing.md` and record reusable lessons in `<state_root>/memory.md`.

## Pre-Trade Validation Gate

**Proceed only when all five checks pass:**

1. ✅ Thesis states its evidence sources, as-of times, assumptions, and outstanding proof
2. ✅ Entry trigger, target path, and finite positive entry/invalidation values are defined; the invalidation is below entry for a long or above entry for a short
3. ✅ Position size follows the formula in `references/risk.md` and a user-approved account-risk limit
4. ✅ Portfolio exposure and correlated risk are compared with the user's approved limits
5. ✅ The analysis is labelled planning-only; persistent logging occurs only when state is enabled and the user approves that update

**Decision heuristic when checks fail:**
| Evidence or freshness is insufficient | List the missing proof and retain the item as a watchlist hypothesis |
| Structure is unclear | Record the condition that would make the setup evaluable |

## Fallback Decision Tree

| Symptom | First-line fix | If still failing |
|---------|----------------|------------------|
| Evidence is stale or incomplete | Record missing source, timestamp, or proof | Keep the item in watchlist research |
| No clear invalidation level | Define the thesis failure condition from price structure | Leave the candidate un-sized |
| Position size exceeds liquidity or approved exposure | Reduce the share count or exclude the candidate | Preserve the original invalidation; record the constraint |
| High-volatility session | Re-evaluate the scenario with current data and approved loss limits | Defer the candidate until its risk is quantifiable |
| Daily loss cap reached | End the session's trade planning under the user's rule | Review the rule before the next session |
| Emotional override detected | Take a break and restate the written plan | Resume only after the plan and risk limits are explicit |

## Gotchas

- **Freshness is evidence**: A current-price or event claim needs a source, timestamp, and timezone; an undated claim is a hypothesis.
- **Gap risk**: Model earnings and major-event gaps separately; a stop order can become a market order once its stop price is reached, so it does not guarantee the execution price.
- **Correlation trap**: Group holdings by shared risk driver and compare their combined exposure with the user's approved portfolio limit.
- **No-trade is a decision**: Present every no-trade outcome explicitly. Log it to persistent state only when state is enabled and the user approves that update.
- **Momentum ≠ thesis**: Define the structural confirmation and invalidation before treating momentum as a candidate.
- **Emotional override**: Return to the written plan and user-approved limits before resuming analysis.

## Operational Boundaries

- Present trade execution as an external action requiring explicit user approval; this skill does not connect to brokers or place orders.
- Keep user-approved state files in `<state_root>`.
- Store explicit preferences and constraints only.
- Define an invalidation condition before calculating a size.
- Apply the user's stated sizing and portfolio limits consistently.
- Log decisions only when persistent state is enabled and the user approves that update.
- Check the relevant macro-event calendar and record the source before a time-sensitive plan.
- Pair broad market context with ticker-specific evidence.

## Security & Privacy

Keep persistent user data local in `<state_root>`. Verify external market data only when the task needs it, and identify its source and as-of time in the output. This skill produces analysis and planning artifacts only; it does not connect to brokers or place orders.
