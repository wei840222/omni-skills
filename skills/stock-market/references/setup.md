# Setup — Stock Market

Read this when `<state_root>` is missing or empty.

## First-Run Transparency

Tell the user what can be created locally:
- Workspace path: `<state_root>`
- Decision memory: `<state_root>/memory.md`
- Optional planning files for watchlists, briefings, and risk rules

Create files only after user confirmation.

## First Conversation Flow

### 1. Situation mapping
Collect minimum context before recommendations:
- Trading horizon (intraday, swing, long-term)
- Preferred instruments (single stocks, ETFs, sectors)
- User-approved risk amount or percentage, if sizing is requested
- Tools already used (broker, screener, research workflow)

### 2. Scope the immediate objective
Clarify the single priority for this session:
- Build watchlist
- Validate a specific ticker thesis
- Prepare pre-market or post-market briefing
- Review completed trades and improve rules

Then execute only that objective with clear next steps.

## Allowed Learning

Store only explicit user information that improves future decisions:
- Confirmed horizon and risk limits
- Approved setup filters and catalyst preferences
- Past mistakes and rule updates the user agrees to keep

Use only explicit user preferences; do not infer hidden preferences from passive behavior.

## Boundaries

- Keep local files inside `<state_root>`
- Keep execution outside this skill; it neither connects to brokers nor places orders.
- Ask before creating or modifying any local planning file.
