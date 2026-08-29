---
name: calendar-planner
description: Plan work, life, and travel across command-line calendar adapters (Google, Outlook, Apple, CalDAV). Use when reconciling cross-calendar conflicts, optimizing weekly schedules, and protecting focus time, rather than just simple scheduling.
metadata:
  related-skills: '{"daily-planner": "Daily plan shaping, sequencing, and realistic task placement.", "schedule": "General scheduling workflows when the user does not need full calendar repair.", "assistant": "Chief-of-staff style execution across tasks, messages, and planning.", "productivity": "Focus systems, prioritization, and anti-overload operating rules.", "remember": "Long-term continuity for user-stated constraints and recurring patterns."}'
  openclaw: '{"requires":{"bins":["python3","jq"],"config":["<state_root>/"]}}'
---

# Calendar Planner

Calendar planner for work, family, health, travel, deep work, and recovery across multiple command-line calendar adapters.

## State location

Calendar Planner state may exist in `<workspace>/calendar-planner/`, `<workspace>/memory/calendar-planner/`, or `~/calendar-planner/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/calendar-planner/`, `<workspace>/memory/calendar-planner/`, `~/calendar-planner/`.
3. If none exists and state must be created, ask for permission and default to `<workspace>/calendar-planner/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` for integration guidelines. Answer the immediate planning question first, ask before creating `<state_root>/`, and ask before writing to any calendar or sending invites.

## When to Use

User needs calendar planning, schedule repair, weekly planning, time blocking, meeting triage, family logistics, appointment placement, or multi-calendar cleanup. Use when the real job is reconciling commitments and constraints across Google Calendar, Outlook, Apple Calendar, and CalDAV from CLI-capable tools.

This skill should return one defended plan, explicit trade-offs, and a safe action sequence. It is stronger than generic scheduling help when calendars disagree, priorities collide, or the user needs a whole-week repair instead of one more event.

## Architecture

Local continuity is optional and only created with user consent.

```text
<state_root>/
├── memory.md        # User-stated planning rules and activation preferences
├── calendars.md     # Provider map, calendar names, and write boundaries
├── rules.md         # Buffers, focus rules, recurring constraints
├── plans.md         # Current week plans and reschedule decisions
└── inbox.md         # Loose commitments that still need placement
```

## Quick Reference

Load only what improves the current planning decision. Start with protocol and commands; add memory only if the user wants continuity.

| Topic | File | When to load |
|-------|------|--------------|
| Setup and activation | `references/setup.md` | First use, stack boundaries, or continuity consent |
| Optional continuity memory | `references/memory-template.md` | After the user opts into local persistence |
| Life Grid planning method | `references/planning-protocol.md` | Placement decisions, weekly repair, trade-off ranking |
| Domain-specific planning heuristics | `references/life-domains.md` | Work/family/health/travel conflicts |
| Core planning rules | `references/core-rules.md` | Before reshuffling commitments |
| Common traps | `references/common-traps.md` | Final review of a proposed plan |
| Domain knowledge | `references/domain-knowledge.md` | Time-management framing and buffer rationale |
| CLI adapter recipes | `references/commands.md` | Dry-run or execute through a chosen adapter |
| Merge normalized event exports | `calendar_merge.py` | Multiple calendar exports need one timeline |
| Audit overlaps and buffer failures | `calendar_guard.py` | Overlap, short-gap, or overloaded-day checks |
| Generate weekly planning summary | `week_plan.py` | Weekly repair or review summary |

## Requirements

Use the lightest adapter that matches the user's stack. Only install the provider tools needed for the current workflow.

| Need | CLI / Tool | Notes |
|------|------------|-------|
| Google Calendar | `gcalcli` | Uses Google Calendar API via the user's own OAuth client |
| Outlook / Microsoft 365 | Microsoft Graph PowerShell | Use delegated calendar scopes only |
| Apple Calendar | `osascript` | Automates Calendar.app on macOS |
| CalDAV and iCloud sync | `khal` plus `vdirsyncer` | Sync locally, then plan from local state |
| Local analysis | `python3` and `jq` | Required for merge, guard, and week review scripts |

## Core Rules

Load `references/core-rules.md` to learn about the fundamental planning rules.

## Life Grid Protocol

See `references/planning-protocol.md` for the full method.

- Intake: capture the real outcome, not just the requested event.
- Map: place each item into hard, flexible, prep, travel, or recovery.
- Defend: protect non-negotiables before offering new slots.
- Repair: if the week is already broken, show what to move, cancel, or downgrade.
- Close: leave the user with one recommended plan and the exact next command or calendar action.

## Common Traps

Load `references/common-traps.md` to avoid frequent planning mistakes and calendar chaos.

## External Endpoints

Only the adapter the user explicitly chooses should talk to a remote service. Use one provider path at a time so data movement stays understandable.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://www.googleapis.com/calendar/v3/* | event metadata for requested Google calendar reads or writes | Google Calendar operations through `gcalcli` |
| https://graph.microsoft.com/v1.0/* | event metadata for requested Outlook or Microsoft 365 reads or writes | Calendar operations through Microsoft Graph PowerShell |
| user-configured CalDAV server | event metadata for configured calendars | Calendar sync through `vdirsyncer` and local use through `khal` |

All other data must remain strictly on the local machine.

## Security & Privacy

**Data that stays local:**
- Optional planning memory in `<state_root>/`
- Normalized event exports and review outputs produced by `calendar_merge.py`, `calendar_guard.py`, and `week_plan.py`
- Apple Calendar automation through Calendar.app on macOS

**Data that may leave your machine:**
- Calendar metadata sent through the Google, Microsoft, or CalDAV adapter the user explicitly chooses

**This skill does NOT:**
- Create, move, or delete calendar items without approval
- Send invites or update shared calendars silently
- Infer hidden rules from unrelated files or conversations
- Access email, contacts, or tasks unless the user explicitly expands scope

## Trust

By using this skill with Google Calendar, Microsoft Graph, or CalDAV adapters, calendar metadata is sent to those services through the configured CLI tools. Only install if you trust those providers and the local machine running the commands.

## Scope

This skill ONLY:
- Plans and audits schedules across user-approved calendars
- Produces dry-run commands, normalized planning files, and local review reports
- Persists minimal planning context after explicit user consent

This skill MUST AVOID unauthorized calendar actions by following these rules:
- Keep `SKILL.md` immutable; only write under the resolved `<state_root>/` after consent
- Obtain explicit approval before accepting invites or rescheduling other people
- Confirm before widening access from one calendar to another
- Store only pointers and user-stated planning rules locally; never store credentials
