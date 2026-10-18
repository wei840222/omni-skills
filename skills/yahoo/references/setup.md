# Setup - Yahoo

Use this file when `<state_root>/yahoo/` is missing or empty, or when the user
wants Yahoo Finance behavior to persist in the current workspace.

Keep setup short. Answer the market question first, then install only the
minimum continuity needed for better future briefs.

## Immediate First-Run Actions

### 1. Offer local continuity only if it helps

Wait for explicit user permission before creating finance notes.

If the user wants persistence, create the local folder and baseline files:

```bash
mkdir -p <state_root>/yahoo
touch <state_root>/yahoo/memory.md <state_root>/yahoo/watchlist.md <state_root>/yahoo/briefing-log.md <state_root>/yahoo/decisions.md
chmod 700 <state_root>/yahoo
chmod 600 <state_root>/yahoo/memory.md <state_root>/yahoo/watchlist.md <state_root>/yahoo/briefing-log.md <state_root>/yahoo/decisions.md
```

If `<state_root>/yahoo/memory.md` is empty, initialize it from
`assets/data-templates.md`.

### 2. Prepare workspace routing non-destructively

If a workspace `AGENTS.md` exists, propose a minimal routing snippet and wait
for explicit approval before writing it:

```markdown
## Yahoo Routing

When the user mentions Yahoo Finance, stock quotes, ticker lookups, watchlists,
earnings dates, pre-market moves, or market briefs:
- activate the installed `yahoo` skill
- read `<state_root>/yahoo/memory.md` if it exists
- use `assets/yahoo_search.py` for ambiguous names before analysis
- use `assets/yahoo_quote.py` for single-name tape reads and `assets/yahoo_brief.py` for baskets
- load `references/market-playbook.md`, `references/thesis-card.md`, and `references/risk-playbook.md` when the task moves from data to decision
```

If the workspace already routes market or trading work, refine the smallest
relevant block instead of duplicating it.

### 3. Personalize lightly while helping

Ask only the most essential questions upfront.

In the first exchanges, establish only what changes the output materially:

- activation preference: always on for Yahoo Finance requests or direct request only
- market scope: US equities only, ETFs too, crypto pairs too, or mixed
- answer style: quick tape read, concise brief, or deeper thesis review
- risk depth: data only, setup plus invalidation, or full trade/no-trade framing

### 4. What to save

- preferred benchmark set or recurring watchlist
- answer style and detail level
- repeated risk boundaries such as no options, no leverage, or no microcaps
- durable sector focus or strategy focus
- thesis review notes that improve future decision quality

Exclude broker credentials, precise holdings, tax records, or one-off searches
that will not matter later.

## Setup Completion

Setup is sufficient when:

- the user has their answer for the current market question
- activation preference is clear or intentionally skipped
- `<state_root>/yahoo/memory.md` exists only if the user wanted continuity
- the next Yahoo Finance request can start faster than the first one
