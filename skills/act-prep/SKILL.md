---
name: act-prep
description: Prepare for the ACT with study plans, section pacing, score tracking, superscore strategy, and college targeting. Use when the user asks for ACT prep, ACT practice schedules, ACT score analysis, or ACT college ranges. Route generic quizzes from notes to exam, semester coursework systems to study, Digital SAT prep to sat, classroom systems to school, and clinical parenting support to parenting.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📝"}'
  related-skills: '{"exam":"Generate practice questions, flashcards, or mock exams from supplied study material rather than ACT-specific workflows.","study":"Semester coursework schedules and student systems beyond ACT-focused prep.","sat":"Digital SAT structure, scoring, and admissions prep instead of ACT.","school":"Curriculum or classroom systems beyond parent-side ACT planning.","parenting":"Broader parenting coaching when the request is not ACT prep.","habits":"Routine design once an ACT study habit is chosen.","tutor":"General multi-subject tutoring workflows outside ACT section strategy."}'
---

## When to load

Load this skill when the user explicitly requests ACT (American College Testing) prep, ACT study schedules, ACT section strategy, ACT score tracking, superscore planning, or ACT-oriented college targeting.

## State location

ACT prep state may exist under portable roots. Resolve `<state_root>` once per invocation before any read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/act/`, `<workspace>/memory/act/`, `~/act/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and the user asks to persist prep data, create `<workspace>/act/`.

Use the selected `<state_root>` for every state operation. Never write runtime state into this skill package. Do not store credentials, portal passwords, or payment details under `<state_root>/`.

```text
<state_root>/
├── profile.md       # Target score, test date, colleges, baseline, format choice
├── sections/        # Per-section progress (english, math, reading, science)
├── practice/        # Practice test results and error analysis
├── vocab/           # Vocabulary and grammar flashcards
├── formulas/        # Math formulas and science concepts
└── feedback.md      # Successful and unsuccessful strategies
```

If older notes still live only at `~/act/`, migrate into the resolved `<state_root>` on request and keep a one-line pointer of the move.

## Quick Reference

| Topic | File |
|-------|------|
| Exam structure and scoring | `references/exam-config.md` |
| Section-specific strategies | `references/sections.md` |
| Progress tracking system | `references/tracking.md` |
| Study methods and pacing | `references/study-methods.md` |
| College targeting | `references/targets.md` |
| User type adaptations | `references/user-types.md` |
| Verified primary sources | `references/sources.md` |

## Core Capabilities

1. **Practice scheduling** — Generate study plans from test date, available hours, and weak sections
2. **Score tracking** — Monitor section scores, composite, superscore potential
3. **Weak area identification** — Analyze errors for high-ROI topics
4. **Timed practice** — Simulate real conditions with pacing feedback
5. **Strategy coaching** — Section tactics for time-pressured questions
6. **College targeting** — Match scores to admission ranges and scholarship cutoffs

## Decision Checklist

Before study planning, gather:

- [ ] Test date and weeks remaining
- [ ] Target composite score
- [ ] Baseline scores (per section if available)
- [ ] Target colleges and their score ranges
- [ ] Paper vs online format, and whether Science / Writing add-ons are required by targets
- [ ] User type (student, parent, tutor, adult retaker)
- [ ] Available study hours per week

## Critical Rules

- **Confirm current ACT format first** — Enhanced ACT shortens core English/Math/Reading and treats Science as optional; verify the examinee's registration before locking a plan (`references/exam-config.md`, `references/sources.md`)
- **Pacing is half the score** — Practice under real section timing
- **Track by section** — Composite hides where points are lost
- **Error analysis** — Log why items were missed, not only that they were
- **Superscore strategy** — Plan retakes to raise individual sections when colleges superscore
- **Writing only when needed** — Prep Writing only if target colleges require or recommend it
- **Adapt to user type** — Students need drills; parents need trajectory summaries; tutors need multi-student patterns
- **Assessment boundary** — Support learning before/after a test. For a live, proctored ACT sitting, give conceptual strategy and practice only—do not supply answers to active test items

## Security and privacy

- Keep scores, college lists, and study notes local under `<state_root>/`
- Do not request or store MyACT passwords, payment cards, or full government ID numbers
- Prefer official ACT pages in `references/sources.md` over memory for format, timing, and score-policy claims
