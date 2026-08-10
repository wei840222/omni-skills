# Analysis Framework — Stock Market

Use this framework to turn broad market commentary into a decision-ready setup.

Scale research depth to the decision horizon and amount at risk. State which evidence is current and which remains unverified.

## 1) Context Snapshot

Capture market context with a source and as-of time:
- Index trend: up, down, range
- Liquidity regime: normal, thin, event-driven
- Volatility regime: compressed, normal, expanding
- Sector leadership: risk-on, defensive, mixed

If context is unstable or undated, keep the candidate un-sized until the current-data and risk checks are complete.

## 2) Ticker Thesis Card

| Field | Prompt |
|------|--------|
| Setup type | Breakout, pullback, mean reversion, event repricing |
| Time horizon | Intraday, swing, position |
| Catalyst | Earnings, macro print, company event, sector flow |
| Base case | Most likely path if thesis is right |
| Failure mode | What invalidates the thesis |

Complete a valid failure mode before assigning a position size.

## 3) Evidence and Freshness

For each evidence line, record:
- source and as-of time;
- whether it is observed data, an inference, or a hypothesis;
- the next proof needed when it remains incomplete.

Use the user's stated eligibility rule when one exists. Without one, retain an incomplete thesis as a watchlist hypothesis rather than presenting it as a trade-ready conclusion.

## 4) Scenario Map

| Scenario | Trigger | Action |
|----------|---------|--------|
| Bull case | Price meets the pre-defined confirmation rule | Present the planned entry and risk calculation for user review |
| Neutral case | Price stalls in range | Hold watchlist status |
| Bear case | Invalidation condition is met | Record the invalidation and leave execution to the user |

Keep scenarios explicit to preserve process discipline during live moves.

## 5) Decision Output

End analysis with one of:
- `Trade candidate` with trigger, invalidation, and target path
- `Watchlist candidate` with what to wait for
- `No-trade` with concrete reason

A missing decision label means analysis is incomplete.
