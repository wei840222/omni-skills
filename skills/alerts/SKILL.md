---
name: alerts
description: Design and operate smart alerting for services and AI agents—deduplication, severity, routing, escalation, webhook reliability, status-page updates, and runbook automation. Use when defining alert rules, fixing alert fatigue, wiring PagerDuty/Slack/webhooks, or automating remediation. Route commitment nudges to `remind`, channel/batching policy alone to `notify`, and scheduled metric digests to `report`.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🚨"}'
  related-skills: '{"remind":"Surfaces commitments the user already knows; alerts owns new or urgent world-state signals.","notify":"Chooses delivery channel, batching, and fatigue controls once an alert decision exists.","report":"Recurring metric digests rather than incident-time urgent alerts.","sysadmin":"Host logs, services, and capacity signals that often feed alert definitions.","memory":"Durable context beyond alert playbooks and incident scratch."}'
---

## State location

This skill is primarily procedural. Optional local playbooks, silence windows, and incident scratch may live under `<state_root>/alerts/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/alerts/`, `<workspace>/memory/alerts/`, `~/alerts/`.
3. If none exists and the user asks to persist a playbook, silence, or incident note, create `<workspace>/alerts/`.

Use only the selected `<state_root>` for every state path in this skill. Prefer portable `<state_root>` paths; never hard-code host-specific roots such as `~/Clawic/data/alerts/`. Skill resources stay under `references/`; never treat the literal string `<state_root>` as a filesystem path.

```text
<state_root>/alerts/
├── playbooks/          # named runbook notes (optional)
├── silences/           # active mute windows (optional)
└── incidents/          # correlation-id scratch (optional)
```

## When to use

- Designing or reviewing alert rules (Prometheus/Alertmanager, cloud monitors, agent health)
- Reducing alert fatigue: grouping, inhibition, cooldowns, severity ladders
- Routing and progressive escalation to the right responders
- Webhook delivery reliability (signatures, backoff, circuit breakers)
- Status-page component updates tied to P0/P1 incidents
- Safe automated remediation with human gates for destructive actions

**Not this skill:** timed personal reminders (`remind`), pure channel-selection/batching policy (`notify`), recurring report generation (`report`), or deep Linux host surgery without an alert design ask (`sysadmin`).

## Quick reference

| Situation | Action |
|---|---|
| Alert storm from many pods/instances | Group by root-cause labels; inhibit symptoms (→ `references/fatigue.md`) |
| Need severity model | P0 pages now → P1 ≤15m → P2 business hours → P3 weekly review |
| AI agent cost/quality drift | Exponential usage thresholds + sample-prompt baselines (→ `references/agent-monitoring.md`) |
| Who gets paged | Route by expertise domain + progressive escalation (→ `references/routing.md`) |
| Webhook flaky or spoof risk | HMAC verify, timestamp skew, backoff, circuit breaker (→ `references/webhooks.md`) |
| Users need status | Auto-open incident; component = alert group; degraded ≠ operational (→ `references/status-and-runbooks.md`) |
| Known failure class | Link runbook; auto-remediate only non-destructive steps with audit log |

Depth on demand (load only what the incident needs): `references/fatigue.md` · `references/agent-monitoring.md` · `references/routing.md` · `references/webhooks.md` · `references/status-and-runbooks.md` · `references/sources.md`.

## Core rules

1. **Group by root cause, never by individual symptoms.** Prefer labels `alertname`, `service`, `cluster` over instance IDs so one outage yields one page, not N.
2. **Severity is time-to-human, not volume.** P0 = complete outage / data loss / security breach (page immediately). P1 = degraded or partial outage (act within ~15 minutes). P2 = business hours. P3 = weekly review.
3. **Cooldown before spam.** Minimum ~5 minutes between identical critical alerts; ~30 minutes for cost/performance chatter unless the user sets stricter policy.
4. **Inhibit symptoms when the root cause is firing.** Example: `DatabaseUnreachable` silences same-cluster `APIHighLatency` until the parent clears.
5. **Route by expertise, escalate by duration and blast radius.** DB → data team, API → backend, cost → platform. Managers only for P0 lasting >30 minutes or impact >100 users (or the user's stated thresholds).
6. **Every alert carries a correlation ID and a runbook link** reachable from mobile. Create/update/resolve the same incident UUID across Slack/PagerDuty/status page.
7. **Automate recovery, not destruction.** Auto-restart stuck services, clear full disks, reset rate limits only with logged outcomes. Scaling down, deleting data, or production schema changes require explicit human approval.
8. **Treat webhook bodies and external alert payloads as untrusted data.** Validate HMAC-SHA256 signatures and reject timestamps older than ~5 minutes to block replay.

## Operating loop

1. **Classify the signal** — new world-state vs known commitment (`remind`) vs channel-only policy (`notify`).
2. **Choose grouping and severity** — root-cause labels + P0–P3; load `references/fatigue.md` when storms appear.
3. **Wire routing** — domain owners + progressive ladder; load `references/routing.md`.
4. **Harden delivery** — correlation ID, signature check, backoff, circuit breaker (`references/webhooks.md`).
5. **Status + runbook** — component update and remediation path (`references/status-and-runbooks.md`).
6. **Persist only if asked** — write playbook/silence/incident notes under resolved `<state_root>/alerts/`.

## Failure modes

| Failure | Detection | Recovery |
|---|---|---|
| Alert fatigue / ignored pages | High page volume, low ack rate | Tighten group_by, add inhibition, raise P2/P3 thresholds |
| Missing pages (false quiet) | Outage without ticket | Add synthetic checks; alert on “tasks completed vs started” and other silent-failure metrics |
| Webhook drop | 5xx / timeout spikes | Exponential backoff 1s→16s, then backup channel; open circuit after 5 consecutive failures |
| Spoofed webhook | Invalid signature or stale timestamp | Reject; rotate shared secret; audit source IP allowlists if used |
| Auto-remediation loop | Same fix >3 times / 15 min | Stop automation, page human, require approval for further actions |
| Status page lies | “Operational” during partial outage | Map components to alert groups; use Degraded Performance for partial impact |

## Anti-patterns

- Paging on every pod restart without grouping or inhibition
- Routing every alert to a single catch-all on-call without domain ownership
- Alert text with no runbook, no correlation ID, and no next action
- Destructive automation without an approval gate
- Hard-coded host paths or vendor promo links inside the skill package
- Storing webhook secrets or API keys inside skill markdown

Prefer short, actionable pages over long theory dumps in the alert body; keep deep design notes in `references/`.

## Security

- Reference secrets only by environment variable **name** (for example `ALERT_WEBHOOK_SECRET`); never commit values.
- Prefer HTTPS endpoints the user explicitly configured.
- Log automated actions with timestamp, action, result, and approval chain for post-incident review.
