---
name: heartbeat
description: Automate proactive monitoring, reactive workflows, and safe cron handoffs. Use when the user requests a heartbeat configuration or recurring monitoring cycle.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"💓"}'
  related-skills: '{"alerts":"Alert routing and escalation hygiene.","copilot":"Proactive assistant patterns with controlled autonomy.","monitoring":"Monitoring strategies and alert design.","schedule":"Scheduling patterns for recurring workflows.","workflow":"Multi-step workflow orchestration."}'
---

# Heartbeat 💓

Build reliable heartbeat playbooks for OpenClaw agents without noisy checks, missed signals, or runaway costs.

## Setup

On first use, follow `references/setup.md` to capture timezone, active hours, precision needs, and risk tolerance.

## State location

Heartbeat state may exist in `<workspace>/heartbeat/`, `<workspace>/memory/heartbeat/`, or `~/heartbeat/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/heartbeat/`, `<workspace>/memory/heartbeat/`, `~/heartbeat/`.
3. If none exists and state must be created, default to `<workspace>/heartbeat/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>/`. See `references/memory.md` for the structure and fields.

```text
<state_root>/
├── memory.md              # Preferences, cadence profile, and last tuning decisions
├── drafts/                # Candidate heartbeat variants
└── snapshots/             # Previous heartbeat versions for rollback
```

## Execution rules

Load detailed behavior rules only when their specific triggers occur:
- **First use:** Read `references/setup.md`.
- **Interval tuning:** Read `references/intervals.md` and `references/triggers.md`.
- **Use cases:** Check `references/use-cases.md` to design hybrid cron patterns.
- **Production template:** Use `assets/heartbeat-template.md` to generate the file.
- **Validation:** Always verify the new file against `references/qa-checklist.md` before applying.

## Core Rules

### 1. Scope the heartbeat before writing anything
Define one mission sentence and 1-3 monitored signals first.

If scope is broad, split into explicit sections (`critical`, `important`, `nice-to-have`) and only automate the first two.

### 2. Keep output contract strict
If nothing actionable is found, heartbeat must return exactly `HEARTBEAT_OK`.

Do not emit summaries on empty cycles. This prevents noisy loops and keeps heartbeat cheap.

### 3. Tune cadence with timezone and active hours
Start from OpenClaw defaults and adapt: use a moderate baseline interval, then tighten only during active windows.

Always encode timezone and active hours in the heartbeat file to ensure waking only occurs during active hours.

### 4. Use cron for exact timing, heartbeat for adaptive timing
If a task must run at exact wall-clock times, move it to cron.

If a task should react to changing context or event probability, keep it in heartbeat.

### 5. Add cost guards to every expensive check
Use a two-stage pattern: cheap precheck first, expensive action only on threshold hit.

Call paid APIs only when the user explicitly accepts the cost. Implement rate limits or burst throttling for all external API hooks to maintain cost control during incident loops.

### 6. Define escalation and cooldown rules
Each alert condition must have trigger threshold, escalation route, and cooldown period.

No escalation path means no alert. No cooldown means likely alert spam.

### 7. Validate with dry runs and rollback path
Before finalizing, run at least one dry simulation against the checklist in `references/qa-checklist.md`.

Keep a snapshot of the previous heartbeat so the user can rollback in one step.

## Common Traps

- Polling everything every cycle -> high token/API burn with low signal quality.
- Using heartbeat for exact 09:00 jobs -> drift and missed exact-time expectations.
- Missing timezone in heartbeat config -> notifications at the wrong local time.
- No active-hours filter -> overnight wakeups and user fatigue.
- No `HEARTBEAT_OK` fallback -> verbose no-op loops.
- No cooldown on alerts -> duplicate escalations during noisy incidents.
- Missing rate limits on API calls -> runaway API billing during stuck loops.

## Security & Privacy

Data that stays local:
- Heartbeat preferences and tuning notes in `<state_root>/`
- Draft and snapshot files for heartbeat definitions

This skill does NOT:
- Require credentials by default
- Trigger external APIs without user-approved instructions
- Edit unrelated files outside the heartbeat workflow
