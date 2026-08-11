---
name: prayers
description: Manage personal prayer routines across faith traditions. Use to configure prayer schedules, track intentions, log reflections, and receive spiritual reminders.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🙏"}'
---

## State location

Prayers state may exist in `<workspace>/prayers/`, `<workspace>/memory/prayers/`, or `~/prayers/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/prayers/`, `<workspace>/memory/prayers/`, `~/prayers/`.
3. If none exists and state must be created, default to `<workspace>/prayers/`.

Use the selected `<state_root>` for every state operation in this skill. If multiple candidate directories exist, use only the highest-precedence directory, report that choice, and keep the directories independent rather than merging or synchronizing them.

## Core Behavior
- Support any faith tradition without assumption
- Help with prayer schedules and reminders
- Keep optional prayer records in `<state_root>/` after the user consents to persistent tracking
- Create `<state_root>/` only when persistent tracking is requested
- Deeply respectful, never prescriptive

## File Structure
```
<state_root>/
├── practice.md       # User's tradition and preferences
├── schedule.md       # Prayer times and routines
├── log/
│   └── YYYY/MM/DD.md
├── prayers/          # Saved prayers and texts
├── intentions.md     # Prayer intentions
└── reflections.md
```

## Initial Setup
Before creating persistent records, confirm that the user wants prayer data retained in `<state_root>/`; otherwise keep the exchange session-only.

Ask gently:
- "What faith tradition do you follow, if any?"
- "Do you have set prayer times or is it flexible?"
- "Would you like reminders?"
- "How would you like to use this?"

## Asset Loading Instructions
When creating or updating files in `<state_root>/`, follow the corresponding templates in `assets/` and load only the template needed for that file:

- For user's tradition and preferences (`<state_root>/practice.md`), read `assets/practice-template.md`.
- For prayer times and routines (`<state_root>/schedule.md`), read `assets/schedule-template.md`.
- For logging daily prayers (`<state_root>/log/`), read `assets/log-template.md`.
- For tracking intentions (`<state_root>/intentions.md`), read `assets/intentions-template.md`.
- For saving favorite texts (`<state_root>/prayers/`), read `assets/saved-prayers-template.md`.
- For recording reflections (`<state_root>/reflections.md`), read `assets/reflections-template.md`.

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
