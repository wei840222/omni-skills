---
name: monitor
description: Define user-requested recurring HTTP, TLS expiry, process, disk, port, or custom checks with persisted results and change-only alerts. Use when the user specifies what to monitor and an interval; scheduling requires an available host scheduler. Broad observability architecture belongs to monitoring rather than individual monitor definitions.
metadata:
  version: "1.0.3"
  openclaw: '{"emoji":"📡","requires":{"bins":["curl"]}}'
  related-skills: '{"monitoring":"Design metrics, logs, traces, and observability stacks beyond individual periodic checks."}'
---

## State location

Monitor state may exist in `<workspace>/monitor/`, `<workspace>/memory/monitor/`, or `~/monitor/`.
Resolve `<state_root>` before the first state operation:

1. Use an explicit user/host-configured path if supplied; resolve it to an actual absolute directory.
2. Otherwise select the first existing directory in the candidate order above.
3. If multiple candidates exist, use only the highest-precedence directory, report the conflict, and leave the others unchanged.
4. If none exists and the user authorizes persistence, create `<workspace>/monitor/` by default.
5. `<workspace>` comes from the host/runtime, not the shell current directory. If it is unavailable, an existing `~/monitor/` may be read; otherwise request an explicit root before creation.
6. Keep the selected root fixed for this invocation. State belongs outside the skill package and version-controlled paths.

Bind the actual selected path to the shell variable `state_root` before copying examples. `<state_root>` in prose is notation, not a literal shell pathname. Create only the needed child directories after consent:

```bash
# state_root contains the actual absolute directory resolved above.
: "${state_root:?Resolve the monitor state root first}"
mkdir -p -- "$state_root/logs"
```

Legacy state is a migration source only. A separate authorized migration must copy, validate, cut over, and retain a rollback copy; existing state remains untouched during skill refactoring.

## Data Storage

- `<state_root>/monitors.json`: required when the first monitor definition is saved; keyed definitions of checks, interval, and grants.
- `<state_root>/config.json`: optional; create when alert preferences are configured, storing credential references rather than values.
- `<state_root>/logs/{name}/YYYY-MM.jsonl`: optional; create the monitor/month log on the first recorded check.
- `<state_root>/alerts/state.json`: optional; create when transition suppression is enabled, recording previous status, failure streak, and last delivered alert.

Choose monitor names matching `[a-zA-Z0-9_-]+` before using them as path components. Read existing JSON before scoped updates; preserve other monitors. Parse errors require recovery from a known-good copy or an explicit user decision, not replacement with an empty object.

## Scope

This skill stores monitor definitions, coordinates user-defined periodic checks through an available host scheduler, and sends status-change alerts through authorized channels.

Execution model:

- The user defines **WHAT** to check and **HOW** to perform the check.
- The user grants endpoint, host, command, scheduler, and notification access.
- This skill coordinates **WHEN**, result persistence, and **ALERTING**.
- Credentials remain in the host's secret/environment mechanism; persisted state stores references only.

A definition file is configuration, not a scheduler. Claims that a monitor is running require a verified durable job and observed execution. Missing host capabilities leave a draft/pending monitor with the exact blocker.

## Requirements

- Required: `curl` for HTTP checks.
- Available as needed: `openssl` for TLS certificate checks, `pgrep` for processes, `df` for disk capacity, `nc` for ports, `jq` for result analysis.
- Optional alert credentials: `PUSHOVER_TOKEN` and `PUSHOVER_USER`, injected through the host secret route; an authorized webhook destination may be supplied instead.
- Recurring execution: an exposed host scheduler with inspect/create/update/read-back support. Its syntax and permissions come from the host, not this package.
- Shell examples target a POSIX shell; check local tool variants before use. Native Windows requires a supported shell or an explicitly verified adapter.

Inspect capabilities first. Missing binaries or adapters produce an actionable blocker; installation is a separate authorization decision.

## Quick Reference

Load only resources needed for the current branch. Paths resolve from this skill root.

| Resource | Load when |
| --- | --- |
| `references/templates.md` | Selecting or executing HTTP, TLS, process, disk, port, custom, or remote checks |
| `assets/monitor-examples.json` | Drafting a monitor definition; static examples require replacement with user-confirmed targets |
| `references/alerts.md` | Choosing thresholds/channels, sending an alert, recording recovery, or diagnosing delivery |
| `assets/alert-examples.json` | Drafting optional alert configuration, failure payload, or recovery payload |
| `references/insights.md` | Calculating sampled availability/latency, detecting patterns, or suggesting additional monitors |
| `assets/weekly-summary.md` | Writing a weekly report from observed logs |

## Core Rules

### 1. User Defines Everything

For each monitor:

1. **WHAT**: capture the exact target and desired signal.
2. **HOW**: capture the method, success predicate, required tools, and access grants.
3. **WHEN**: capture the interval/timezone and verify an available durable scheduler.
4. **ALERT**: confirm status-change policy, failure threshold, destination, and disclosure scope.

Example:

```text
User: "Monitor my API at api.example.com every 5 minutes."
Agent: "Should success mean HTTP 200? Which channel should receive failure and recovery alerts?"
User: "Use my approved channel, and check certificate expiry too."
Agent: "I will verify tools, scheduler, and both checks before marking it active."
```

### 2. Monitor Definition

Save the confirmed definition under `<state_root>/monitors.json`:

```json
{
  "api_prod": {
    "description": "User's API health",
    "checks": [
      {"type": "http", "target": "https://api.example.com/health", "expect": 200},
      {"type": "ssl", "target": "api.example.com", "warn_days": 14}
    ],
    "interval": "5m",
    "alert_on": "change",
    "requires": [],
    "status": "pending",
    "created": "2024-03-15"
  }
}
```

Dates and targets above are examples, not observed user facts. Mark `active` only after verifying the scheduler's job identifier, schedule, check result, and authorized delivery configuration. Preserve the scheduler identifier for later inspect/cancel actions.

### 3. Common Check Types

| Type | Signal | Tool |
| --- | --- | --- |
| `http` | HTTP status and latency | `curl` |
| `ssl` | Certificate expiry | `openssl` |
| `process` | Named process exists | `pgrep` |
| `disk` | Capacity usage/free space | `df` |
| `port` | TCP connection succeeds | Verified `nc` variant |
| `custom` | Explicit user-defined predicate | Reviewed user-provided command |

User-defined methods remain subject to host safety policy. Inspect custom commands and side effects before execution. Missing permissions produce `unknown`/blocked, not evidence that the service is down.

### 4. Confirmation Format

```text
Monitor: [description]
Checks: [targets, methods, and success predicates]
Interval: [interval and timezone]
Alert: [transition policy, threshold, and authorized destination]
Requires: [verified tools and explicit access grants]
State: [resolved actual location]
Status: [pending / active / blocked]
Job: [verified scheduler ID, or not created]
Evidence: [check result, delivery result, and schedule read-back]
```

### 5. Alert on Change

- Send one failure notification on the eligible `ok` → `fail` transition after the configured consecutive-failure threshold; include failure count.
- Send a recovery message on `fail` → `ok`, including the observed outage duration.
- Repeated same-status checks update results and counters while suppressing duplicate notifications.
- Establish the first known observation as the baseline unless the user explicitly requests an initial alert.
- Keep transport/check errors distinct from a validated success/failure predicate. Detailed transition and delivery behavior lives in `references/alerts.md`.

### 6. Permissions

The definition's `requires` field records granted capabilities:

- `[]`: basic local checks only within the already-authorized target scope; it is not blanket access permission.
- `["ssh:server1"]`: explicit SSH grant for that exact host.
- `["docker"]`: explicit Docker grant for the selected context.

Verify actual access independently of the recorded grant. Notification destinations and scheduler mutations require explicit authorization too. A missing grant leaves the definition pending and names the permission needed.
