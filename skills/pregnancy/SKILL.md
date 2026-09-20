---
name: pregnancy
description: >
  Track pregnancy metrics, symptoms, and prenatal routines. Load when the user wants
  flexible daily logs, weekly clinician-ready summaries, visit-prep questions, or
  safety-first red/amber triage for maternity follow-up. Supports organization and
  escalation cues only — not diagnosis, prescribing, or replacing clinician care.
metadata:
  openclaw: '{"emoji":"🤰","requires":{"bins":[]},"config":["<state_root>/pregnancy/"],"os":["darwin","linux","win32"],"displayName":"Pregnancy (Tracker, Journal, Triage, Visit Prep)"}'
  related-skills: '{"doctor":"General symptom triage and medication/lab review outside maternity-specific tracking.","nutrition":"Micronutrient adequacy and pregnancy diet context after triage is clear.","period":"Cycle history context before or around conception tracking.","baby":"Postpartum/infant day-to-day tracking after delivery handoff.","therapist":"Mental-health support once crisis routing and clinical handoff are handled.","sleep":"Sleep quality patterns that affect prenatal wellness logs.","fitness":"Activity load context when symptoms relate to exertion.","dietitian":"Therapeutic meal construction after clinician guidance."}'
---

## When to load

Load this skill when the user asks to track pregnancy symptoms, log daily prenatal routines, or prepare summaries for doctor visits.

Read `references/setup.md` on first initialization.
## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure and starter templates.

```text
<state_root>/
|-- memory.md                 # Status, context, and active tracking modules
|-- logs/daily-log.md         # Day-by-day entries with timestamps and units
|-- summaries/weekly.md       # Weekly clinical summary and trend notes
|-- summaries/visit-prep.md   # Questions and priorities for the next appointment
|-- alerts/events.md          # Red and amber events with trigger reasons
`-- preferences/thresholds.md # User-specific tracking scope and escalation choices
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory structure and templates | `assets/memory-template.md` |
| Flexible tracking framework | `references/tracking-framework.md` |
| Metric catalog and units | `references/metric-catalog.md` |
| Data quality and validation rules | `references/data-quality.md` |
| Red and amber triage rules | `references/triage-rules.md` |
| Weekly and visit summary format | `assets/visit-summary-template.md` |

## Data Storage

Local notes stay in `<state_root>/`.
Before creating or changing local files, present the planned write and ask for user confirmation.

## Core Rules

### 1. Define Scope Before Logging
Start with user intent and care context:
- basic wellness tracking only
- clinician-facing pregnancy tracking
- high-risk monitoring support
Enable only modules the user wants, then expand gradually.

### 2. Keep Tracking Flexible but Structured
Use `references/tracking-framework.md` to run modular tracking:
- core daily block for minimum continuity
- optional blocks for symptoms, medications, appointments, mood, sleep, nutrition, fetal movement, or glucose
- custom user-defined blocks when needed
Enable modules gradually based on user requests.

### 3. Preserve Clinical Utility of Data
Use `references/metric-catalog.md` and `references/data-quality.md`:
- always record timestamp, unit, and context
- normalize values to one unit system
- separate observed facts from interpretation
Reject ambiguous entries and ask for missing context.

### 4. Generate Visit-Ready Summaries
At least weekly, generate a concise summary using `assets/visit-summary-template.md`:
- trend overview
- out-of-range or concerning events
- unresolved questions for clinician
Keep summaries short enough for prenatal visit use.

### 5. Apply Safety-First Triage
Use `references/triage-rules.md` for red and amber conditions.
If emergency signs appear, provide immediate emergency guidance first.
Provide urgent escalation guidance immediately before continuing routine coaching.

### 6. Stay in Support Scope, Not Diagnosis Scope
This skill supports organization, tracking, and escalation cues.
It does not diagnose, prescribe, interpret imaging, or replace clinician judgment.
For medication changes or treatment decisions, route user to their care team.

### 7. Protect Privacy and User Agency
Track only pregnancy-relevant information needed for user goals.
Offer opt-in detail levels and allow pause, simplify, or delete requests.
Only track data explicitly approved by the user.

## Common Traps

- Logging too much too soon -> dropout and inconsistent data quality.
- Missing timestamps or units -> trends become unreliable for clinicians.
- Mixing reassurance with warning signs -> delayed urgent care.
- Treating optional consumer metrics as clinical truth -> noisy decisions.
- Summaries with raw dumps only -> poor usability during appointments.
- Giving treatment advice beyond scope -> safety and trust risk.


## Sources

Gate 6 domain references used for triage wording and visit-prep safety scope:

- ACOG — Pregnancy Complications FAQ via https://www.acog.org/womens-health/faqs/pregnancy-complications
- CDC Hear Her — Urgent Maternal Warning Signs via https://www.cdc.gov/hearher/maternal-warning-signs/index.html
- March of Dimes — Warning Signs During Pregnancy via https://www.marchofdimes.org/find-support/topics/pregnancy/warning-signs-during-pregnancy

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
- tracking logs, weekly summaries, alert events, and clinician question lists approved by the user.
- stored in `<state_root>/`.

**This skill does NOT:**
- diagnose pregnancy conditions or provide emergency medical treatment.
- make undeclared network calls.
- modify files without explicit user confirmation.
- collect unrelated personal data.

## Trust

This is an instruction-only pregnancy tracking and visit-prep skill.
No credentials are required and no third-party service access is needed.
