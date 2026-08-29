---
name: schedule
description: Program recurring or one-time jobs the user defines, persist them under portable state, and fire them at the right local time. Use when the user asks to schedule, cron, remind-later as a job, cancel or list scheduled work, set a timezone for jobs, or asks how a cron expression should run; not for calendar conflict repair (`calendar-planner`) or surfacing known commitments (`remind`).
metadata:
  version: "1.0.3"
  openclaw: '{"emoji":"📅","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"remind":"Lead-time nudges for commitments the user already knows, not job execution","calendar-planner":"Cross-calendar conflict repair and focus-block planning","daily-planner":"Day shaping and top-priority protection before jobs are stored","productivity":"Diagnose overload and pick the smallest sustainable plan before scheduling","time-management":"Time-blocking mechanics when the need is planning, not a durable job store"}'
---

## State location

Schedule state may exist in `<workspace>/schedule/`, `<workspace>/memory/schedule/`, or `~/schedule/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/schedule/`, `<workspace>/memory/schedule/`, `~/schedule/`.
3. If none exists and state must be created, ask for permission and default to `<workspace>/schedule/`.

Use the selected `<state_root>` for every state operation in this skill.

Directory structure after resolution:

```text
<state_root>/
├── jobs.json           # Job definitions
├── preferences.json    # Timezone, preferred times
└── history/            # Execution logs
    └── YYYY-MM.jsonl
```

Create `<state_root>/history/` only when an execution log must be written. Do not pre-create empty history files.

If data still sits at a legacy path such as `~/Clawic/data/schedule/`, treat it as a migration source only: copy after consent, validate, then cut over. Do not keep the legacy path in active lookup order.

## Scope

This skill:

- Stores scheduled job definitions in `<state_root>/`
- Triggers jobs at the scheduled local time
- Learns timezone and preferred morning/evening times from explicit user answers

Execution model:

- The user defines WHAT the job does
- The user grants any permissions the job needs
- This skill only handles WHEN

Operating constraints:

- Request access to mail, calendar, shell, or other external services only when the job needs them
- Persist and fire jobs through this skill's state files; leave system crontab, launchd, and systemd timers untouched
- Execute a job only when it has a user-defined task string and an explicit grant for every required skill

## Quick Reference

Load only the file needed for the current step; keep `SKILL.md` as the control plane.

| Topic | File | When to load |
|-------|------|--------------|
| Cron expression syntax | `references/patterns.md` | Building or validating a cron / interval / one-shot expression |
| Common mistakes | `references/traps.md` | Before create/cancel when timezone, DST, or confirmation is uncertain |
| Job format | `references/jobs.md` | Writing or editing `<state_root>/jobs.json` |
| Domain knowledge | `references/cron_basics.md` | Explaining cron fields, DST, or timezone semantics to the user |

## Core Rules

### 1. User Defines Everything

When the user requests a scheduled task:

1. **WHAT**: User specifies the action (may require other skills/permissions)
2. **WHEN**: This skill handles timing
3. **HOW**: User grants any needed access explicitly

Example flow:

```text
User: "Every morning, summarize my emails"
Agent: "I'll schedule this for 8am. This will need email access —
        do you want me to use the mail skill for this?"
User: "Yes"
→ Job stored with explicit reference to mail skill
```

### 2. Simple Requests

| Request | Action |
|---------|--------|
| "Remind me to X at Y" as a stored job | Store job, confirm |
| "Every morning do X" | Ask time, store job |
| "Cancel X" | Remove from `<state_root>/jobs.json` |

If the user wants a lead-time nudge about a commitment they already know, hand off to `remind` instead of storing an execution job here.

### 3. Confirmation Format

```text
✅ [what user requested]
📅 [when] ([timezone])
🔧 [permissions/skills needed, if any]
🆔 [id]
```

### 4. Job Persistence

In `<state_root>/jobs.json`:

```json
{
  "daily_review": {
    "cron": "0 9 * * 1-5",
    "task": "User-defined task description",
    "requires": ["mail"],
    "created": "2024-03-15",
    "timezone": "Europe/Madrid",
    "status": "active"
  }
}
```

The `requires` field lists only skills/access the user explicitly granted.

### 5. Execution

When the scheduled time arrives:

- Execute only the stored user-defined task
- Use only permissions listed in `requires`
- Append the result to `<state_root>/history/YYYY-MM.jsonl`

### 6. Preferences

After the first job, store in `<state_root>/preferences.json`:

- Timezone
- Preferred "morning" / "evening" times
- Default notification style
