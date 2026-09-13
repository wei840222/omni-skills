---
name: report
description: Create, schedule, format, and deliver automated recurring reports from user-defined data sources. Use when the user wants recurring summaries, metric digests, standup/status reports, PDF/HTML/chat report delivery, or on-demand regeneration of a named report. Not for one-off PDF generation without a report config (`pdf-generator`), commitment reminders (`remind`), or generic notification channel selection (`notify`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📊","requires":{"config":["<state_root>/report/"]}}'
  related-skills: '{"schedule":"Cron/job scheduling execution after a report cadence is chosen.","notify":"Delivery channel, batching, and fatigue controls for report alerts.","pdf-generator":"One-off or template PDF generation without a recurring report config.","alerts":"Urgent new-information notifications rather than scheduled metric digests.","memory":"Durable user context beyond report configs and generated archives.","analytics":"Broader analytics querying when the ask is analysis rather than scheduled delivery."}'
---

## State location

Persistent report configs, history, and generated artifacts live under `<state_root>/report/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/report/`, `<workspace>/memory/report/`, `~/report/`.
3. If none exists and state must be created, default to `<workspace>/report/`.

Use the selected `<state_root>` for every state operation in this skill. Prefer portable `<state_root>` paths; never hard-code `~/Clawic/data/report/` or other host-specific roots.

```text
<state_root>/report/
├── memory.md               # Index + preferences
├── {name}/
│   ├── config.md           # Report configuration
│   ├── data.jsonl          # Historical data
│   └── generated/          # Past reports
└── delivery logs under {name}/delivery.log when needed
```

Create on first use: `mkdir -p <state_root>/report`

## When to use

- User wants a recurring report (daily/weekly/monthly/on-demand) with defined metrics
- Need to configure format (chat/pdf/html/json) and delivery (chat/telegram/file/email/webhook)
- Pause, list, regenerate, or archive an existing named report
- Route away for pure PDF authoring (`pdf-generator`), commitment nudges (`remind`), or channel-policy-only work (`notify`)

## Scope

This skill:

- Stores report configurations in `<state_root>/report/`
- Generates reports on schedule or on demand
- Delivers via channels the user configures

**User-driven model:**

- User defines WHAT data to include
- User grants access to any needed sources
- User provides API keys if external data is needed
- Skill handles SCHEDULING and FORMATTING

Required protections:

- Require user-provided credentials via environment variables for API access
- Restrict data collection to sources the user explicitly specified
- Store only environment variable **names** in configuration; never store secret values
- Do not access APIs without those credentials, and do not invent sources the user did not request

## Environment variables

No fixed required secrets. User provides API keys as needed:

```bash
# Example: if user wants Stripe data
export STRIPE_API_KEY="sk_..."

# Example: if user wants GitHub data
export GITHUB_TOKEN="ghp_..."
```

Config must reference the env var name only. Raw values stay in the environment.

## Delivery security

External delivery (Telegram/webhook/email) sends report content off-device.

- User explicitly configures each channel
- User is responsible for trusting the destination
- `file` delivery stays local (`<state_root>/report/{name}/generated/`)

## Quick reference

| Task | File | When to load |
|------|------|--------------|
| Configuration schema | `references/schema.md` | Creating or updating a report configuration |
| Output formats | `references/formats.md` | Formatting a report for delivery |
| Delivery options | `references/delivery.md` | Configuring schedule/cron jobs or executing delivery |
| Verified sources | `references/sources.md` | Citing scheduling/format guidance or refreshing domain notes |

## Operating loop

1. **Clarify the report** — name, metrics, cadence, format, delivery channel, timezone.
2. **Resolve state** — pick `<state_root>` before creating or editing files.
3. **Write config** — `config.md` under `<state_root>/report/{name}/`; update `memory.md` index.
4. **Schedule if needed** — use host cron/automation with an isolated agent turn; see `references/delivery.md`.
5. **Generate & deliver** — load format/delivery refs only as needed; fall back to local file on channel failure.
6. **Manage lifecycle** — list/pause/run-now/archive via `memory.md` + config status.

## Core rules

### 1. User defines data sources

When creating a report:

1. User specifies what data to track
2. If an external API is needed, user provides credentials
3. Credentials are stored as env var references, not values

Example:

```text
User: "Weekly report on my Stripe revenue"
Agent: "I'll need Stripe API access. Please set
        STRIPE_API_KEY in your environment."
User: "Done"
→ Config stores source.type=api and source.env=STRIPE_API_KEY
```

### 2. Report configuration

In `<state_root>/report/{name}/config.md`:

```yaml
name: weekly-revenue
schedule: "0 9 * * 1"  # Monday 9am
sources:
  - type: api
    env: STRIPE_API_KEY  # User provides
format: chat
delivery: telegram
```

For full field options, alerts, and multi-schedule layouts, load `references/schema.md`.

### 3. Scheduling

| Frequency | Cron | Example |
|-----------|------|---------|
| Daily | `0 9 * * *` | 9am daily |
| Weekly | `0 9 * * 1` | Monday 9am |
| Monthly | `0 9 1 * *` | 1st of month |
| On-demand | - | When user asks |

### 4. Delivery channels

User configures in `config.md`:

- `chat` — Reply in conversation
- `telegram` — Send to Telegram (user provides chat ID)
- `file` — Save to `<state_root>/report/{name}/generated/`
- `email` — Send via user's configured mail
- `webhook` — POST JSON to a user-provided URL

### 5. Managing reports

```text
"List my reports" → Read <state_root>/report/memory.md
"Pause X report" → Update config status
"Run X now" → Generate on-demand with latest data
```

## Failure modes

| Failure | Recovery |
|---------|----------|
| Missing API credential | Pause generation; ask for env var name + confirm it is set; do not invent values |
| Delivery channel fails | Retry once after 5 minutes; fall back to `file`; log under `{name}/delivery.log` |
| Duplicate report name | Refuse create; offer rename or update existing config |
| Ambiguous schedule/timezone | Ask one clarifying question before writing cron |
| Empty metrics / no data | Produce a short “no data” report rather than fabricating numbers |

## Anti-patterns

- Hard-coding `~/Clawic/...` or other host-specific state roots
- Storing API keys, tokens, or chat secrets inside `config.md`
- Pulling APIs or private sources the user did not authorize
- Generating fabricated metric values when inputs are missing
- Loading every reference file on simple list/pause requests
