# Sources - Yahoo

Verified during the 2026-10-19 handoff. Prefer these over model memory for
Yahoo Finance access patterns and Agent Skills packaging rules.

## Yahoo Finance data access

- [yfinance on PyPI](https://pypi.org/project/yfinance/) — packaging and usage
  notes for Yahoo Finance market data helpers (HTTP 200 on 2026-10-18).
- [yfinance documentation](https://ranaroussi.github.io/yfinance/index.html) —
  reliability, quote helpers, and library guidance (HTTP 200 on 2026-10-18).

## Agent Skills packaging

- [Agent Skills specification](https://agentskills.io/specification) — normative
  frontmatter, progressive disclosure, and packaging rules (HTTP 200 on
  2026-10-18).

## Live script checks

Package scripts were executed against Yahoo endpoints with browser-like headers:

- `python3 skills/yahoo/assets/yahoo_search.py 'Nvidia'` → exit 0, primary `NVDA`
- `python3 skills/yahoo/assets/yahoo_quote.py AAPL` → exit 0, priced quote with
  market-state line
- `python3 skills/yahoo/assets/yahoo_brief.py MSFT AAPL GOOGL` → exit 0, ranked
  movers brief

A direct `curl` to `https://finance.yahoo.com/quote/AAPL` returned HTTP 429 once
from this runner. Treat HTML scrape rate limits as an operational risk; keep
market-state / timestamp warnings and do not claim broker connectivity.
