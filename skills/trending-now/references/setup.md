# Setup - Trending Now

Use this file when `<state_root>/` is missing or empty.

## Operating Priorities

- Answer the immediate user request first.
- Lock integration behavior in early exchanges.
- Confirm what topics should be monitored and what should be ignored.
- Keep setup short and practical.

## First Activation Flow

1. Confirm integration behavior early:
- Should this activate whenever the user asks what is trending?
- Should it run proactively on heartbeat or only when directly requested?
- Are there topics or sources this skill should never monitor?

2. Confirm monitoring scope:
- topics to watch (brands, markets, creators, products, events)
- geography and language boundaries
- source priorities, with X as optional fast-signal source

3. Confirm alert behavior:
- active hours and timezone
- strictness level (conservative, balanced, aggressive)
- message style (brief alerts or richer mini-briefs)

4. If setup context is approved, initialize local workspace after resolving
   `<state_root>` (see `SKILL.md` State location):

```bash
mkdir -p <state_root>
touch <state_root>/{memory.md,topics.md,runs.md,alerts.md}
chmod 700 <state_root>
chmod 600 <state_root>/{memory.md,topics.md,runs.md,alerts.md}
```

Replace `<state_root>` with the resolved absolute path before running shell
commands. Never create a directory literally named `<state_root>`.

5. If `memory.md` is empty, initialize it from `assets/data-templates.md`.
   Seed heartbeat thresholds from `assets/HEARTBEAT.md` when the user wants a
   recurring cadence.

## Integration Defaults

- Start in conservative mode unless the user requests aggressive monitoring.
- Prefer no-op output (`HEARTBEAT_OK`) over low-quality alerts.
- Require at least two independent source families before sending alerts.
- Keep focus tight: fewer topics with higher signal quality.

## What to Save

- activation and suppression preferences
- topic definitions and boundaries
- run cadence, active hours, and strictness mode
- alert outcomes and false-positive patterns

## Guardrails

- State certainty conditionally, based strictly on source evidence and timestamps.
- Keep local notes free of secrets or private credentials.
- Require explicit user confirmation before posting to any social network.
