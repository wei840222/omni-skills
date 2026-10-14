# Beszel Domain Knowledge

## Product anchors

- Treat Beszel as a **hub + agent** monitoring system, not a generic Prometheus replacement.
- Prefer official docs in `sources.md` for installation modes, notification channels, reverse-proxy needs, and known disconnect causes.
- Keep skill state under `<state_root>/`; keep agent tokens, hub keys, and webhook secrets out of notes.

## Core Rules

### 1. Define Monitoring Scope Before Installation
- Confirm which hosts, services, and failure modes matter most before recommending a layout.
- Prioritize high-impact systems first so coverage is meaningful from day one.
- Separate hub placement from agent placement: one hub, many agents.

### 2. Keep Agent Access Minimal
- Use least privilege for monitored hosts and prevent broad root-level automation by default.
- Treat onboarding credentials, universal tokens, and notification endpoints as sensitive; keep them out of workspace notes.
- Prefer unix-socket local pairing or documented secure remote paths over exposing agent ports casually.

### 3. Baseline First, Then Tune Alerts
- Collect a short baseline period before applying strict thresholds.
- Tune alert levels with operating context such as business hours, maintenance windows, and expected burst patterns.
- Require explicit user approval before enabling new external notification destinations.

### 4. Troubleshoot with a Fixed Sequence
- Validate hub reachability, agent connectivity (WebSocket/TCP), clock sync, firewall/reverse-proxy behavior, and resource pressure in a consistent order.
- Isolate one variable at a time to prevent changing many factors during an active incident.
- For same-host Docker hub+agent setups, prefer unix socket pairing; `localhost` across separate container networks is a common false path.

### 5. Make Upgrades Reversible
- Require backup and rollback steps before version changes.
- Upgrade one environment at a time and confirm health before broader rollout.
- Prevent simultaneous hub and agent upgrades when diagnosing version skew.

### 6. Keep Operations Memory Current
- Record node ownership, alert intent, and previous incidents after meaningful changes.
- Convert repeated incidents into prevention rules and adjust thresholds accordingly.

## Common Traps

- Enrolling many agents before defining alert ownership -> noisy incidents with unclear responders.
- Copying thresholds from another environment -> chronic false positives or missed real failures.
- Upgrading hub and agents simultaneously -> hard-to-debug version mismatch issues.
- Ignoring host clock drift -> misleading timelines and confusing incident analysis.
- Logging sensitive credentials in notes -> unnecessary security exposure.
- Assuming `localhost` works between separate Docker networks on the same host -> agent stays disconnected.
- Enabling gzip/encoding on SSE (`text/event-stream`) at the reverse proxy -> realtime stats or saves break.

## Security & Privacy

**Data that may leave your machine (only when user configures external integrations):**
- Monitoring notifications sent to selected channels or alerting tools.
- Metadata required by external notification endpoints chosen by the user.

**Data that stays local by default:**
- Monitoring topology, node notes, threshold history, and incident logs in `<state_root>/`.

**Skill boundaries:**
- Require explicit user approval before enabling external alert destinations.
- Require explicit user approval before creating new credentials.
- Limit network requests only to declared endpoints and official documentation fetches.
