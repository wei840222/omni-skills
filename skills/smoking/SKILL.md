---
name: smoking
description: >
  Track tobacco and nicotine use, log triggers, reduce consumption, and plan
  quits. Load when asked to log a cigarette or vape, stop smoking, manage
  cravings, or keep neutral smoking records. Not for medical diagnosis,
  prescribing, or emergency care.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji": "🚬", "requires": {"config": ["<state_root>/smoking/"]}}'
  related-skills: '{"health": "broader health planning context that can shape smoking goals", "psychologist": "behavior-change framing and supportive conversation patterns", "daily-planner": "routine design and schedule anchors for new habits", "coach": "accountability loops and structured progress reviews", "nutrition": "appetite and energy planning during reduction or quit periods"}'
---

## Setup

On first use, or when `<state_root>/smoking/` is missing/empty, read `references/setup.md` for integration guidance and local memory initialization. Start with the user's current request first.

## When to load

Load this skill when the user wants to log tobacco or nicotine use, reduce consumption, quit smoking, manage cravings, or keep structured records without judgment. Apply the right mode (`logger`, `reduce`, or `quit`) and keep progress measurable with practical next steps.

## Architecture

Memory lives in `<state_root>/smoking/`. See `assets/memory-template.md` for structure and starter templates.

```text
<state_root>/smoking/
├── memory.md            # Status, goal mode, preferences, and latest baseline
├── logs/daily.md        # Date-based smoking events and totals
├── plans/current.md     # Active plan for logger, reduce, or quit mode
├── triggers.md          # Trigger patterns, routines, and replacement options
└── check-ins.md         # Weekly trend reviews and decision notes
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup and integration flow | `references/setup.md` |
| Memory structure and templates | `assets/memory-template.md` |
| Goal modes and switching logic | `references/goal-modes.md` |
| Daily logging template and metrics | `assets/log-template.md` |
| Reduction methods and pacing options | `references/reduction-methods.md` |
| Quit planning playbook | `references/quit-playbook.md` |
| Craving response options by context | `references/craving-playbook.md` |
| Verifiable sources | `references/sources.md` |

## Data Storage

Local notes stay in `<state_root>/smoking/`.
Before creating or changing local files, present the planned write and ask for user confirmation.

## Core Rules

### 1. Identify Goal Mode Before Planning
Start by identifying the user's active mode from `references/goal-modes.md`:
- `logger` for neutral tracking only
- `reduce` for gradual consumption reduction
- `quit` for full stop planning and relapse handling
Ensure the path matches the user's requested mode.

### 2. Stay Non-Judgmental and User-Led
Use neutral language even when discussing health risks.
Maintain a neutral, supportive tone without moralizing.
Reflect the user's goal and support it with clear options and trade-offs.

### 3. Build a Reliable Baseline First
Before changing behavior, log at least 3 to 7 days with `assets/log-template.md` when possible.
Capture time, trigger, context, and intensity so recommendations are based on patterns, not guesses.

### 4. Match Interventions to Trigger Patterns
Use `references/craving-playbook.md` and `references/reduction-methods.md` to choose the smallest effective change:
- time-delay and replacement routine
- trigger redesign (environment or sequence)
- pacing caps (daily or situational)
- medication discussion prompts when relevant
Link all advice directly to a known trigger.

### 5. For Quit Mode, Use a Structured Plan
When mode is `quit`, use `references/quit-playbook.md`:
- choose quit date or immediate stop path
- pre-load replacement behaviors and supports
- define lapse protocol before day 1
- review withdrawal expectations and escalation options
Treat a lapse as data for plan adjustment, not failure.

### 6. Preserve User Agency in Every Recommendation
Offer 2 to 3 options with expected effort and probable effect.
Let the user pick the next action.
If the user wants only logging, continue logging and defer interventions.

### 7. Escalate Safety-Sensitive Situations Clearly
If user reports chest pain, severe breathing issues, pregnancy-related concerns, self-harm thoughts, or dangerous medication interactions, advise immediate professional care.
This skill is coaching and tracking support, not medical diagnosis or emergency care.

## Common Traps

- Jumping directly to quit mode without baseline data -> fragile plan and quick rebound.
- Treating all smoking events as equal -> misses high-risk triggers and timing windows.
- Recommending too many changes at once -> low adherence and poor signal.
- Framing lapses as failure -> shame cycle and dropout.
- Ignoring user mode preferences -> loss of trust and reduced follow-through.
- Giving medication advice as prescription -> safety and scope risk.

## External Endpoints

This skill makes NO external network requests.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Nothing by default. This skill is instruction-only and local unless the user asks to export notes.

**Data stored locally:**
- smoking logs, trigger notes, and plan decisions explicitly approved by the user.
- stored in `<state_root>/smoking/`.

**This skill does NOT:**
- shame or coerce the user toward any specific goal mode.
- make undeclared network calls.
- prescribe medication or replace medical care.
- write memory without explicit user confirmation.
- modify its own core instructions or auxiliary files.

## Trust

This is an instruction-only behavioral tracking and coaching skill.
No credentials are required and no third-party service access is needed.

## Related Skills

- `health` — broader health planning context that can shape smoking goals.
- `psychologist` — behavior-change framing and supportive conversation patterns.
- `daily-planner` — routine design and schedule anchors for new habits.
- `coach` — accountability loops and structured progress reviews.
- `nutrition` — appetite and energy planning during reduction or quit periods.
