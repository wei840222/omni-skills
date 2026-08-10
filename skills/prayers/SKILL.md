---
name: prayers
description: Manage personal prayer routines across faith traditions. Use to configure prayer schedules, track intentions, log reflections, and receive spiritual reminders.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🙏"}'
---

## State location

Prayers state may exist in `$WORKSPACE/prayers/`, `$WORKSPACE/memory/prayers/`, or `~/prayers/`.
Before reading or writing state, resolve `$STATE_ROOT` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `$WORKSPACE/prayers/`, `$WORKSPACE/memory/prayers/`, `~/prayers/`.
3. If none exists and state must be created, default to `$WORKSPACE/prayers/`.

Use the selected `$STATE_ROOT` for every state operation in this skill.

## Core Behavior
- Support any faith tradition without assumption
- Help with prayer schedules and reminders
- Log prayers and spiritual reflections privately (100% offline, local to `$STATE_ROOT/`)
- Create `$STATE_ROOT/` as workspace
- Deeply respectful, never prescriptive

## File Structure
```
$STATE_ROOT/
├── practice.md       # User's tradition and preferences
├── schedule.md       # Prayer times and routines
├── log/
│   └── YYYY/MM/DD.md
├── prayers/          # Saved prayers and texts
├── intentions.md     # Prayer intentions
└── reflections.md
```

## Initial Setup
Ask gently:
- "What faith tradition do you follow, if any?"
- "Do you have set prayer times or is it flexible?"
- "Would you like reminders?"
- "How would you like to use this?"

## Asset Loading Instructions
When creating or updating files in `$STATE_ROOT/`, strictly follow the formats defined in the corresponding template files located in `assets/`. Read these files on-demand as needed:

- For user's tradition and preferences (`$STATE_ROOT/practice.md`), read `assets/practice-template.md`.
- For prayer times and routines (`$STATE_ROOT/schedule.md`), read `assets/schedule-template.md`.
- For logging daily prayers (`$STATE_ROOT/log/`), read `assets/log-template.md`.
- For tracking intentions (`$STATE_ROOT/intentions.md`), read `assets/intentions-template.md`.
- For saving favorite texts (`$STATE_ROOT/prayers/`), read `assets/saved-prayers-template.md`.
- For recording reflections (`$STATE_ROOT/reflections.md`), read `assets/reflections-template.md`.

## What To Pray
When user asks "what should I pray" or "help me pray":
- Ask situation if not clear (anxious, grateful, grieving, seeking guidance)
- Offer specific prayer from their tradition — actual text, not just name
- Adapt to their level (full prayer or shorter version)
- Walk through step by step if learning

## What To Surface
- "Maghrib in 15 minutes"
- "You've prayed 7 days consecutively"
- "Intention from last month — still active?"
- "Today is [holy day] in your tradition"

## Proactive Support
- Prayer time reminders (if wanted)
- Holy days and observances in their tradition
- Fasting periods
- "You usually pray at this time"

## What To Track
- Prayer completed (simple check-in, do not induce guilt for missed streaks)
- Duration (optional)
- Intentions held
- State/quality (optional, personal)
- Reflections (optional, strictly private and local)

## Engagement Principles
- Ask gently about their tradition
- Support all levels of practice
- Wait for requests to provide specific prayers
- Be supportive and encouraging
- Treat all traditions equally
