# Memory Template - Yahoo

Create `<state_root>/yahoo/memory.md` with this structure:

```markdown
# Yahoo Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Activation Preferences
- Trigger phrases:
- Use automatically or on request:

## Market Scope
- Instruments:
- Regions:
- Benchmarks:
- Exclusions:

## Watchlist Defaults
- Core watchlist:
- Priority names:
- Event names:

## Decision Boundaries
- Allowed depth:
- Risk limits:
- Things to avoid:

## Output Style
- Preferred format:
- Target length:
- When to ask a follow-up:

## Review Notes
- Repeated thesis patterns worth remembering
```

Optional companion files under the same `<state_root>/yahoo/` tree:

```markdown
# watchlist.md
- Ranked tickers, benchmarks, and catalyst windows

# briefing-log.md
- Dated pre-market / post-market / event briefs

# decisions.md
- Thesis, invalidation, and review notes
```

Keep every file compact. Do not store broker credentials, precise holdings, tax
records, or one-off searches that will not matter later.
