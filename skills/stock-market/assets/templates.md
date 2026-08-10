# Stock Market Templates

Use these templates when creating state files in `<state_root>`.

## Memory Template (`<state_root>/memory.md`)

```markdown
# Stock Market Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Market Profile
<!-- Horizon, instruments, preferred sectors, and constraints -->

## Risk Rules
<!-- User-approved max risk per trade, max daily loss, correlated-exposure method, and un-sized-candidate conditions -->

## Active Watchlist Focus
<!-- Current priority tickers and why they are tracked -->

## Open Hypotheses
<!-- Assumptions pending confirmation, with evidence required -->

## Decisions
<!-- Approved playbooks, rejected setups, and rationale -->

## Review Notes
<!-- Lessons from wins, losses, and skipped trades -->

---
*Updated: YYYY-MM-DD*
```

## Watchlist Template (`<state_root>/watchlist.md`)

```markdown
# Watchlist

## Date
YYYY-MM-DD

## Priority A (Actionable Soon)
| Ticker | Setup | Catalyst Window | Trigger | Invalidation | Notes |
|--------|-------|-----------------|---------|--------------|-------|
|        |       |                 |         |              |       |

## Priority B (Needs Confirmation)
| Ticker | Missing Evidence | Next Check | Risk Note |
|--------|------------------|------------|-----------|
|        |                  |            |           |

## Priority C (Theme Tracking)
| Ticker/Sector | Theme | Why Track | Revisit Date |
|---------------|-------|-----------|--------------|
|               |       |           |              |

## Deprioritized
| Ticker | Reason Removed | Date |
|--------|----------------|------|
|        |                |      |
```

## Briefing Template (`<state_root>/briefing-log.md`)

```markdown
# Market Briefing

## Session
date: YYYY-MM-DD
type: pre-market | post-market

## Macro and Market Regime
- Overnight market performance:
- Key catalysts since last session:
- Index trend:
- Volatility state:
- Liquidity notes:
- Upcoming macro events:

## Priority Watchlist Notes
| Ticker | Thesis | Trigger Status | Action |
|--------|--------|----------------|--------|
|        |        |                |        |

## Risk Controls
- Daily risk limit (user approved):
- Max risk per idea (user approved):
- Max total open risk (user approved):
- Gap risk adjustment (if applicable):
- No-trade conditions active:

## Decisions
- Trade candidate(s):
- Watchlist-only candidate(s):
- Explicit no-trade call(s):

## Review (post-market required)
- What worked:
- What failed:
- Rule changes for next session:
```
