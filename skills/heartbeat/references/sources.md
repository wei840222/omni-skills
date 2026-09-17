# Sources - Heartbeat skill

Last checked: 2026-09-18

Use these primary references when designing heartbeat cadence, quiet no-ops, and cron handoffs. Prefer the live docs over memorized defaults.

## OpenClaw heartbeat and scheduling
- OpenClaw Docs — Heartbeats: interval loops, timezone/active hours, and quiet no-op contract via https://docs.openclaw.ai/gateway/heartbeat
- OpenClaw Docs — Cron jobs: exact wall-clock schedules and one-shot reminders that should leave heartbeat via https://docs.openclaw.ai/automation/cron-jobs
- OpenClaw Docs — Automation / agent loop context for proactive checks without chat spam via https://docs.openclaw.ai/

## Operational patterns applied here
- Quiet empty cycles must return exactly `HEARTBEAT_OK` (or the configured no-op token) instead of narrative filler.
- Exact-time work belongs on cron; adaptive/reactive monitoring stays on heartbeat.
- Cheap precheck → expensive action only on threshold hit; add cooldown and rate limits for external/API hooks.
- Encode timezone and active hours so overnight wakeups are intentional, not accidental.

## Local state and rollback
- Keep preferences, drafts, and snapshots under a portable `<state_root>` resolved from workspace paths, not hard-coded vendor home directories.
- Snapshot the previous heartbeat file before replacing it so rollback is one step.

## Operational note
Product defaults, CLI surface, and automation docs change. Re-open the current OpenClaw heartbeat and cron pages before changing interval floors, no-op tokens, or handoff rules.
