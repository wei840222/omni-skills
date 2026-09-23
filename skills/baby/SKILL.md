---
name: baby
description: >
  Track baby feeds, sleep, diapers, symptoms, and growth with caregiver continuity,
  pediatric visit summaries, and safety-first triage alerts. Load for day-to-day infant
  care logs, handoffs between caregivers, and clinician-ready prep — not diagnosis or treatment.
metadata:
  openclaw: '{"emoji":"👶","requires":{"config":["<state_root>/baby/"]}}'
  related-skills: '{"doctor":"Structured preparation for pediatric or family medical visits beyond daily infant tracking.","health":"Broader health planning and longitudinal family tracking outside infant day-to-day ops.","nutrition":"Meal, hydration, and solids planning once food logistics dominate over core infant tracking.","parenting":"Broader parenting support beyond daily operational infant tracking.","sleep":"Deeper sleep-routine support when sleep becomes the main problem."}'
---
## When to load

Load this skill when the user requests help tracking a baby's feeds, sleep, diapers, growth, or medical symptoms, or when managing a caregiver handoff or pediatric appointment.

## Architecture

Memory lives in `<state_root>/baby/`. If `<state_root>/baby/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure.

```text
<state_root>/baby/
|-- memory.md                 # Status, baby profile, modules, and active priorities
|-- logs/daily-log.md         # Timestamped daily care events across caregivers
|-- handoff/current.md        # Shift handoff and open loops for the next caregiver
|-- summaries/weekly.md       # Weekly summary with trends and unresolved concerns
|-- summaries/visit-prep.md   # Pediatric visit prep, questions, and data packet
|-- alerts/events.md          # Red and amber events with actions and outcomes
`-- preferences/thresholds.md # User-specific routines, alert preferences, and scope
```

## Quick Reference

Use these files to switch between lightweight daily tracking, escalation support, and pediatric visit prep without changing the core workflow.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory structure and starter files | `assets/memory-template.md` |
| Modular care tracking framework | `references/tracking-framework.md` |
| Metrics, units, and event vocabulary | `references/metric-catalog.md` |
| Data quality and continuity rules | `references/data-quality.md` |
| Red and amber triage rules | `references/triage-rules.md` |
| Caregiver handoff format | `references/caregiver-handoff.md` |
| Routine planning by baby stage | `references/routine-blueprints.md` |
| Weekly and visit summary format | `assets/visit-summary-template.md` |

## Data Storage

Local notes stay in `<state_root>/baby/`.
Before creating or changing local files, present the planned write and ask for user confirmation.

## Core Rules

### 1. Define Baby Stage and Care Scope First
Start with the smallest context that changes decisions:
- baby age or corrected age
- feeding mode and current schedule pressure
- known medical context, medications, or care-team instructions
- which modules matter now: feeds, sleep, diapers, symptoms, growth, solids, routines, appointments, or development notes
Enable only the modules that are currently necessary.

### 2. Run a Modular Tracker, Not a Rigid App Flow
Use `references/tracking-framework.md` to keep a core continuity block plus optional modules:
- core continuity for feeds, sleep, diapers, and active concerns
- optional modules for pumping, solids, medications, growth, appointments, milestones, or custom routines
- simplified mode for overwhelmed caregivers
Adapt depth to real life instead of demanding perfect tracking.

### 3. Preserve Caregiver Continuity
Use `references/caregiver-handoff.md` whenever multiple adults share care.
Every meaningful update should make the next caregiver faster, safer, and less likely to miss:
- last important events
- what is due next
- what changed from baseline
- what needs escalation or follow-up

### 4. Keep Data Clinically Useful
Use `references/metric-catalog.md` and `references/data-quality.md`:
- always record timestamps, units, and amount or duration when relevant
- distinguish observed facts from caregiver interpretation
- normalize repeated measures to one unit system
- capture baseline versus today when discussing changes
If an entry is too vague to be actionable, ask for missing context.

### 5. Generate Pediatric-Ready Summaries
Use `assets/visit-summary-template.md` to compress logs into:
- pattern changes
- intake, output, sleep, or symptom concerns
- medications and care actions tried
- concise questions for the pediatrician
Summaries should be short enough to use during a real visit or call.

### 6. Apply Safety-First Triage
Use `references/triage-rules.md` for red and amber conditions.
If urgent signs appear, give escalation guidance first and pause routine coaching.
Provide urgent care instructions first, and pause optimization, scheduling, or reassurance until urgent care is clear.

### 7. Stay in Support Scope and Protect Privacy
This skill supports organization, continuity, and escalation cues.
It does not diagnose, prescribe, interpret tests, or replace pediatric judgment.
Track only what improves care, allow simplified mode, and ensure all tracking is visible and explicitly requested.

## Common Traps

- Treating every day like a full logging day -> caregivers quit tracking.
- Missing timestamps on feeds, meds, or fever -> summaries lose clinical value.
- Mixing what happened with why it happened -> patterns become unreliable.
- Ignoring caregiver handoff context -> duplicated feeds, missed meds, or sleep confusion.
- Reassuring through red flags -> delayed urgent care.
- Letting milestone anxiety dominate routine support -> more stress, worse decisions.

## External Endpoints

This skill makes NO external network requests.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Nothing by default. This skill is instruction-only and local unless the user explicitly requests export.

**Data stored locally:**
- care logs, handoff notes, weekly summaries, alert events, and pediatric question lists approved by the user.
- stored in `<state_root>/baby/`.

**Scope boundary:**
- Stay within tracking, continuity, triage cues, and visit prep — diagnosis and emergency treatment belong to clinicians.
- Keep network use at zero unless the user explicitly asks to export or share.
- Write local files only after the user confirms the planned change.
- Store only baby-care details that improve continuity.

## Trust

This is an instruction-only baby tracking and visit-prep skill.
No credentials are required and no third-party service access is needed.
