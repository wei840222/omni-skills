---
name: notify
description: >
  Choose delivery channel, timing, batching, quiet hours, escalation, and
  fatigue controls for agent-originated user notifications. Use when an outcome,
  error, schedule confirmation, or digest must reach the user without spam; when
  channel/urgency/batching policy is unclear; or when quiet-hours and secondary
  channels matter. Not for inventing new world-state alerts (`alerts`), personal
  commitment nudges (`remind`), outbound message drafting (`message`), or
  recurring metric report generation (`report`).
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🔔","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"alerts":"Decides that new or urgent world-state warrants attention before this skill chooses how to deliver it.","remind":"Surfaces commitments the user already knows rather than delivery policy.","message":"Drafts channel-safe outbound wording once notify has chosen channel and timing.","report":"Builds recurring metric digests whose delivery still follows this skill.","schedule":"Runs timed jobs that may emit notifications through this skill.","monitor":"Persists recurring checks that should notify on change, not on every poll."}'
---

# Notify

Own **how and when** an already-decided user-facing update is delivered. Do not invent incidents, draft long copy, or replace monitoring/alert design.

## State location

Notification preferences, quiet-hours settings, batch queues, and delivery logs may live under `<state_root>/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/notify/`, `<workspace>/memory/notify/`, `~/notify/`.
3. If multiple candidates exist, keep the highest-precedence directory, leave others independent, and tell the user which location was selected.
4. If none exists and preferences or queues must be created, default to `<workspace>/notify/` and obtain brief consent before the first persistent write.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/notify/` may be read; otherwise ask before creating data.

Use the selected `<state_root>` for every state path in this skill. Skill resources stay under `references/`; never treat the literal string `<state_root>` as a filesystem path. Never write learned preferences into `SKILL.md`.

```text
<state_root>/
├── preferences.md   # primary channel, timezone, quiet hours, critical channel
├── queue/           # batched or quiet-hours deferred items
└── delivery.log     # optional send outcomes for debugging
```

## When to use

- An agent needs to notify the user of a completion, failure, schedule confirmation, or digest
- Channel, urgency, batching, quiet hours, or secondary escalation is unclear
- The user asks to reduce notification noise or set delivery preferences

**Not this skill**

| Job | Skill |
|-----|-------|
| New/urgent world-state alert design | `alerts` |
| Known-commitment nudge | `remind` |
| Outbound wording / social risk | `message` |
| Recurring metric report body | `report` |
| Job execution timing | `schedule` |
| Durable check definitions | `monitor` |

## Ordered workflow

1. **Confirm there is something worth sending** — Skip no-change, still-running, and debug-only chatter. Prefer final outcomes and actionable failures.
2. **Load preferences** — Resolve `<state_root>` and read `preferences.md` when present. If primary channel, timezone, quiet hours, or critical channel are unknown, ask once before the first non-critical send.
3. **Classify urgency** — Read `references/domain.md` routing table. Level 5 / security / system-down may break quiet hours; informational items queue for digest.
4. **Choose one primary channel** — Match urgency to channel. Do not fan out the same text to every channel.
5. **Apply timing and batching** — Honor quiet hours. If 3+ related updates land within 5 minutes for the same project, collapse into one summary.
6. **Format for the channel** — Lead with outcome, one action if needed, user-local timestamp, and concrete context. Avoid markdown tables on chat surfaces.
7. **Escalate only when critical and unanswered** — Follow the capped path in `references/domain.md`. Never contact third parties without explicit permission.
8. **Record optional delivery state** — After authorized sends, append a short line to `delivery.log` when debugging is useful.

## Quick reference

| Need | Load |
|------|------|
| Routing, formatting, quiet hours, escalation, anti-patterns | `references/domain.md` |
| Verified sources | `references/sources.md` |

## Output shape

When preparing or confirming a notification, include:

1. **Decision** — send now / batch / queue for quiet-hours end / log-only
2. **Channel** — one primary path (and secondary only if escalation rules apply)
3. **Message** — outcome-first text within channel limits
4. **Preferences gap** — any missing timezone/channel facts that blocked a confident send
