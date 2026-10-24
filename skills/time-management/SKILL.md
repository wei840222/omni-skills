---
name: time-management
description: Plan days, prioritize Most Important Tasks, protect deep-work blocks, run weekly reviews, and keep energy-aware schedules under portable local state. Use when the user asks how to organize a day, feels meeting-overloaded, needs prioritization or time blocking, or wants a Sunday/Monday weekly review. Route whole-life capacity and overwhelm triage to `productivity`, recurring behavior design to `habits`, job/cron execution to `schedule`, commitment nudges to `remind`, and calendar conflict repair to `calendar-planner`.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"⏰"}'
  related-skills: '{"calendar-planner": "Repairs calendar conflicts and meeting placement once the day plan exists.", "habits": "Owns recurring behavior design, streaks, and relapse plans rather than one-day blocking.", "productivity": "Diagnoses whole-life capacity, overwhelm, and sustainable plans beyond a single day schedule.", "remind": "Surfaces known commitments at the right time; time-management decides what deserves a protected block.", "schedule": "Programs recurring or one-time jobs; time-management plans the human day those jobs sit inside."}'
---

## State location

Resolve `<state_root>` before reading or writing time-management data:

1. Use a host- or user-configured time-management path when one is explicitly supplied.
2. Otherwise use the first existing directory in this order: `<workspace>/time-management/`, `<workspace>/memory/time-management/`, then `~/time-management/`.
3. If none exists and the user asks to persist preferences or review notes, create `<workspace>/time-management/`.

Use only the selected `<state_root>` for this invocation. Do not hardcode absolute paths. If more than one candidate exists, use the highest-precedence directory and report the conflict; keep the directories separate rather than merging or moving data.

```text
<state_root>/
├── memory.md            # Preferences, energy pattern, current MITs
├── weekly-review.md     # Latest weekly review notes
└── templates/           # Optional user-custom planning templates
```

## Quick Reference

| Resource | Description | When to load |
|----------|-------------|--------------|
| `references/setup.md` | First-run integration questions and attitude. | State is empty or the user is new to this skill. |
| `references/memory-template.md` | Canonical shape for `<state_root>/memory.md`. | Creating or repairing persisted preferences. |
| `references/time-blocking.md` | Day-planning and buffer rules. | User asks to organize a day or protect focus time. |
| `references/prioritization.md` | MIT / Eisenhower / frog-first frameworks. | User is overloaded and needs ranking help. |
| `references/weekly-review.md` | Retrospective + next-week planning script. | Sunday/Monday review or week-reset requests. |
| `references/traps.md` | Common failure modes and recoveries. | Plan keeps slipping or user repeats a known trap. |
| `references/domain-knowledge.md` | Cited time-blocking / prioritization / GTD notes. | Explaining why a method works or citing sources. |

## When to use

- Plan or replan a day with 1–3 Most Important Tasks (MITs).
- Protect deep work from meeting sprawl and reactive email.
- Match hard work to peak energy and batch similar tasks.
- Run a weekly review and set next-week priorities.
- Persist only preferences the user explicitly asks to keep.

This skill owns day/week planning advice and local preference memory. It does not own calendar APIs, cron job execution, habit streak math, or whole-life productivity diagnosis.

## Core workflow

1. Resolve `<state_root>`. Read `<state_root>/memory.md` and `<state_root>/weekly-review.md` only when they exist.
2. If state is empty, load `references/setup.md` silently and start helping; do not narrate file names.
3. For day planning, identify 1–3 MITs, propose explicit time blocks with buffers, and protect the first deep-work block.
4. For overload, load `references/prioritization.md` and ask what will be deferred or declined before adding work.
5. For weekly review, load `references/weekly-review.md`, capture notes under `<state_root>/weekly-review.md`, and refresh Current Focus in memory when the user consents.
6. Persist changes only after an explicit save request. Load `references/traps.md` when the same failure repeats.
7. Before closing, restate the next protected block and any explicit decline/defer trade-off in one short checklist.

## Core rules

### 1. Default to time blocking

When the user asks how to organize the day:

1. Identify 1–3 MITs.
2. Assign specific clock blocks (not vague “morning”).
3. Add 15–30 minute buffers between blocks.
4. Protect the first deep-work block.

Example shape:

```text
09:00-11:00 — [MIT #1] deep work
11:00-11:30 — Buffer / email
11:30-12:30 — [MIT #2]
12:30-13:30 — Lunch
13:30-15:00 — Meetings / calls
15:00-16:30 — [MIT #3 or admin]
16:30-17:00 — Plan tomorrow
```

### 2. Energy-aware scheduling

| Window | Typical energy | Prefer |
|--------|----------------|--------|
| First 2–4 hours | Peak | Creative work, hard problems, writing |
| Mid-day | Moderate | Meetings, collaboration, admin |
| Afternoon | Lower | Routine tasks, email, planning |

If the user’s peak differs, ask once and adapt from `<state_root>/memory.md`.

### 3. Protect deep work

- First block of the day defaults to deep work.
- Prefer at least 90 minutes for meaningful progress.
- Suggest no-meeting protection before 11:00 when the calendar is controllable.
- Flag back-to-back meetings that erase focus blocks.

### 4. Weekly review habit

Suggest Sunday evening or Monday morning:

1. What worked last week?
2. What did not?
3. Top 3 priorities for this week?
4. Which blocks must stay protected?

Store notes in `<state_root>/weekly-review.md` only when the user wants them saved.

### 5. Decline by design

Before adding a commitment, ask what will be dropped or deferred to make room. Prefer protecting existing commitments over absorbing new ones without a trade-off.

### 6. Batch similar tasks

Group calls, email, and admin into dedicated blocks. Treat constant context switching as lost time.

### 7. Plan tomorrow tonight

End-of-day ritual: review completions, move unfinished work, set tomorrow’s top 3, and write the first block explicitly.

## Failure modes

| Situation | Response |
|-----------|----------|
| No MITs stated | Ask for 1–3 outcomes before inventing a full schedule. |
| Calendar is externally controlled | Plan around fixed meetings; protect remaining contiguous focus windows. |
| Empty state tree | Help immediately; create files only after an explicit save request. |
| User wants calendar API / cron changes | Route to `calendar-planner` or `schedule`; keep this skill on the human plan. |
| Repeated slip into the same trap | Load `references/traps.md` and change one condition, not the whole system. |

## Anti-patterns

- Do not invent calendar events, meeting acceptances, or productivity metrics the user never shared.
- Do not force a complex system when the user asked for one next block.
- Do not monitor activity, scrape email/calendar, or write state without an explicit request.
- Do not shame missed plans; recover with a smaller next block and a clear trade-off.
- Do not dump every reference file into the reply; load only the branch that applies.
- Do not treat a missed morning block as a failed day; rebuild from the next available quiet window.

## Scope

This skill ONLY:

- Provides time-management advice when asked.
- Helps plan days and weeks.
- Stores preferences the user explicitly provides.
- Reads included reference files on demand.

This skill NEVER:

- Accesses calendar, email, or any external service on its own.
- Tracks or monitors user activity.
- Makes network requests.
- Modifies files without an explicit user request.

## External endpoints

This skill makes no external network requests.

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

## Security and privacy

- Preferences and review notes stay in the selected `<state_root>/`.
- Save only what the user explicitly asks to keep; the user may delete the tree anytime.
- Keep operation offline and local unless the host separately provides another approved tool.