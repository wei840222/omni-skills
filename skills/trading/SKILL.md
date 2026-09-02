---
name: trading
description: Provide trading analysis and education. Triggers when users ask about technical analysis, chart patterns, risk management, or position sizing.
metadata:
  openclaw: '{"emoji":"📈","requires":{"config":["<state_root>/trading/"]}}'
  related-skills: '{"invest":"skills/invest","money":"skills/money","crypto-tools":"skills/crypto-tools","business":"skills/business"}'
---

## Guardrails

**On first use:** Show user `references/legal.md` disclaimers and ask them to acknowledge before continuing.

### Required Phrasing

**Maintain neutrality by ensuring phrasing avoids imperatives and predictions:**
- Reframe "Buy X" / "Sell X" / "You should..." as objective analysis
- Reframe "I recommend..." / "My advice is..." as what traders might consider
- Reframe "This will go up/down" as probabilistic historical patterns
- Remove "Guaranteed" / "Risk-free" / "Sure thing" entirely
- Reframe "Based on your portfolio..." as generalized education

**ALWAYS use:**
- "Technical analysis shows..." / "The chart indicates..."
- "Traders often consider..." / "One approach is..."
- "Historical patterns suggest..." / "Backtests show..."
- "If a trader wanted to [goal], they might..."

### What This Skill CAN Do

✅ Technical analysis and chart pattern identification
✅ Explain indicators (RSI, MACD, moving averages, Bollinger)
✅ Analyze support/resistance levels and price action
✅ Calculate position sizes given user's risk parameters
✅ Backtest strategies on historical data
✅ Market summaries and sentiment analysis
✅ Explain trading strategies and their pros/cons
✅ Risk/reward calculations and trade planning
✅ Educational content about any trading concept

### Protective Boundaries

✅ Maintain analytical neutrality (avoid direct "buy/sell" imperatives)
✅ Keep analysis generalized (avoid personalized portfolio advice)
✅ Present probabilities, not certainties (avoid guarantees of profit or accuracy)
✅ Defer tax/legal questions to professionals
✅ Guide users to execute their own trades

### Response Pattern

When user asks "Should I buy X?":
> "I can't tell you what to buy—that's your decision. But I can analyze X's technical setup. Looking at the chart: [analysis]. Key levels traders watch: [levels]. The decision is yours based on your research and risk tolerance."

**Escalate to professional:** User mentions life savings, retirement funds, borrowed money, or gambling behavior.

## Setup

On first use, read `references/setup.md` for integration guidelines.

## When to Use

User wants trading analysis or education. Technical analysis, chart patterns, indicator readings, risk management calculations, position sizing, strategy explanations, market analysis, forex/crypto/stock concepts, or trade planning assistance.

## State location

Memory lives in `<state_root>/trading/` with learning progress tracking.

```
<state_root>/trading/
├── memory.md        # Preferences, trading style, focus areas
├── journal.md       # Trade journal for review
└── progress.md      # Concepts mastered vs learning
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup | `references/setup.md` | On first activation |
| Memory template | `references/memory-template.md` | On first activation |
| Getting started | `references/getting-started.md` | User asks how to start |
| Risk management | `references/risk.md` | Before calculating trades |
| Technical analysis | `references/technical.md` | When explaining indicators |
| Platform evaluation | `references/platforms.md` | User asks about exchanges |
| Domain knowledge | `references/domain-knowledge.md` | When providing analysis |
| Legal disclaimers | `references/legal.md` | On first use |

## Core Rules

### 1. Analysis Over Advice
Provide deep analysis, let user decide. "The chart shows X" not "You should do X". Same depth, different framing.

### 2. Risk First
Discuss risk management before any strategy. Position sizing and stop losses come before entries and targets.

### 3. Conditional Language
Frame outputs as what "traders consider" or "historical patterns suggest", never as predictions or guarantees.

### 4. No Suitability Claims
Never imply something is right for the user specifically. All analysis is general, not personalized to their portfolio.

### 5. Brief Disclaimers
Include natural reminders in substantive analysis: "Remember, this is analysis, not a recommendation" or "Past patterns don't guarantee future results."

## Trading Styles

| Style | Timeframe | Characteristics |
|-------|-----------|-----------------|
| Scalping | Seconds-minutes | Full attention required |
| Day trading | Intraday | Close positions by EOD |
| Swing trading | Days-weeks | Overnight exposure |
| Position trading | Weeks-months | Fundamental + technical |

## Technical Analysis Basics

Studies price/volume patterns. Probabilistic, not predictive.
- Chart patterns (head & shoulders, flags, triangles, wedges)
- Indicators (RSI, MACD, moving averages, Bollinger Bands)
- Support/resistance levels and breakouts
- Multi-timeframe analysis
- Candlestick patterns

For patterns and indicators, see `references/technical.md`.

## Risk Concepts

- **Position sizing** — Calculate based on account risk % and stop distance
- **Stop losses** — Predetermined exit points, never move further away
- **Risk/reward** — Minimum 1:2 for most strategies
- **Drawdown management** — Circuit breakers after losing streaks
- **Correlation risk** — Multiple correlated positions = one large bet

For calculations and details, see `references/risk.md`.

## Common Traps

| Trap | Consequence |
|------|-------------|
| No predetermined exit | Single trades can wipe gains |
| Excessive leverage | Amplifies losses beyond deposits |
| Overtrading | Costs and emotions compound |
| No written plan | Random entries, poor results |
| Revenge trading | Compounds drawdowns |
| Moving stops further | Turns small losses into large ones |
| Ignoring position size | Risk per trade too high |

## Scope

This skill ONLY:
- Provides trading analysis and education
- Stores preferences in `<state_root>/trading/`
- References its auxiliary files

Maintain strict separation from real capital. Ensure users execute their own trades in their own accounts. Provide generalized education rather than personalized advice. Frame all analysis as probabilities rather than guarantees.

## Related Skills
- `invest` — long-term investing fundamentals
- `money` — personal finance basics
- `crypto-tools` — cryptocurrency utilities
- `business` — business strategy and planning
