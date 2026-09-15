---
name: gaokao
description: Track Gaokao scores, weak areas, spaced repetition, and university targeting for China's national college entrance exam. Use when the user needs Gaokao study planning, mock analysis, 志愿填报 ranges, or parent/tutor support for 高考. Route generic quizzes from notes to exam, semester coursework systems to study, classroom systems to school, broader parenting coaching to parenting, and ACT/SAT prep to act-prep/sat.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎓"}'
  related-skills: '{"exam":"Generate practice questions or mocks from supplied material rather than Gaokao-specific workflows.","study":"Semester coursework schedules beyond Gaokao-focused prep.","school":"Curriculum or classroom systems beyond Gaokao planning.","parenting":"Broader parenting coaching when the request is not Gaokao support.","habits":"Routine design once a Gaokao study habit is chosen.","daily-planner":"Day packing once Gaokao priorities are set.","act-prep":"ACT structure and admissions prep instead of Gaokao.","sat":"Digital SAT prep instead of Gaokao.","math":"Deep math topic tutoring outside Gaokao section strategy.","chinese":"General Chinese language study outside Gaokao 语文 workflows."}'
---

## When to load

Load this skill when the user explicitly requests 高考 / Gaokao prep, daily Gaokao schedules, mock-exam analysis, weak-area ROI planning, spaced-repetition for Gaokao content, university/major targeting, or parent/tutor support around Gaokao.

## State location

Gaokao state may exist in `<workspace>/gaokao/`, `<workspace>/memory/gaokao/`, or `~/gaokao/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/gaokao/`, `<workspace>/memory/gaokao/`, `~/gaokao/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and state must be created, default to `<workspace>/gaokao/`.

Use the selected `<state_root>` for every state operation in this skill. Never write runtime state into this skill package. Do not store credentials, portal passwords, or payment details under `<state_root>/`.

## Progressive disclosure

| Topic | File | Load when |
|-------|------|-----------|
| Exam structure and scoring | `references/exam-config.md` | Province model, subject weights, timeline, cutoff tiers |
| Progress tracking system | `references/tracking.md` | Profile, sessions, mocks, mastery logs |
| Study methods and spaced repetition | `references/study-methods.md` | Daily plans, ROI ordering, flashcards |
| Stress management and wellbeing | `references/wellbeing.md` | Burnout, sleep, parent communication |
| University and major targeting | `references/targets.md` | 志愿填报 ranges, major fit, application timeline |
| User type adaptations | `references/user-types.md` | Student / parent / tutor / retaker voice |
| Primary sources | `references/sources.md` | Gate 6 verification URLs before overriding facts |

## Data Storage

User data lives in `<state_root>/`:
```
<state_root>/
├── profile.md       # Goals, target score, exam date, province
├── subjects/        # Per-subject progress and weak areas
├── sessions/        # Study session logs
├── mocks/           # Mock exam results and analysis
├── flashcards/      # Spaced repetition cards
└── feedback.md      # What works, what doesn't
```

## Core Capabilities

1. **Daily scheduling** — Generate study plans based on exam countdown and weak areas
2. **Progress tracking** — Monitor scores, time spent, mastery levels across all subjects
3. **Weak area identification** — Analyze errors to find high-ROI topics
4. **Spaced repetition** — Manage flashcards for vocabulary, formulas, 古诗词
5. **Mock exam analysis** — Score prediction, error pattern recognition
6. **University targeting** — Match scores to admission requirements

## Decision Checklist

Before study planning, gather:
- [ ] Exam date and days remaining
- [ ] Province (affects cutoffs and curriculum)
- [ ] Subject combination (3+1+2 or 3+3)
- [ ] Target universities and majors
- [ ] Current estimated score range
- [ ] User type (student, parent, tutor, retaker)

## Critical Rules

- **ROI-first** — Prioritize topics with highest points-per-hour potential
- **Track everything** — Log sessions, scores, errors to `<state_root>/`
- **Adapt to user type** — Students need scheduling; parents need monitoring; tutors need multi-student
- **Spaced repetition** — Distribute review evenly over time instead of cramming
- **Wellbeing matters** — Monitor for burnout; suggest breaks
- **Verify live cutoffs** — Province 一分一段表 and university 招生计划 change yearly; confirm via `references/sources.md` before hard score advice
