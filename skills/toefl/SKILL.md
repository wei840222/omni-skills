---
name: toefl
description: >
  Prepare for the TOEFL iBT exam with diagnostics, section strategy, mock planning,
  score targeting, and admissions/immigration timeline management. Use when the user
  needs TOEFL iBT structure (post-Jan 2026 task types and 1–6 scores with 0–120
  transition), Speaking/Writing practice, MyBest policy checks, official score-send
  timing, or progress tracking. Route general English polish to `english`, IELTS to
  `ielts`, generic quiz generation from notes to `exam`, semester coursework to
  `study`, Digital SAT to `sat`, and ACT prep to `act-prep`.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎓"}'
  related-skills: '{"english":"General native-style English writing and correction outside TOEFL task criteria.","ielts":"IELTS Academic/GT structure, band scoring, and immigration CLB mapping instead of TOEFL.","exam":"Generate practice questions or mock exams from supplied notes rather than TOEFL-format workflows.","study":"Semester coursework schedules beyond TOEFL-focused prep.","sat":"Digital SAT structure and admissions prep instead of TOEFL.","act-prep":"ACT section strategy and college targeting instead of TOEFL.","tutor":"General multi-subject tutoring outside TOEFL section tactics.","speak":"Speech-ready delivery and TTS phrasing outside scored TOEFL Speaking tasks.","grammar":"Pure correctness passes where TOEFL task strategy must not move.","writing":"Long-form drafting in the user voice outside TOEFL Writing tasks."}'
---

## When to load

Load when the user is preparing for TOEFL iBT (Test of English as a Foreign Language). Trigger for diagnostic assessment, section strategy under the current ETS task types, score-gap planning, university/immigration requirement checks, official score-send timelines, or progress tracking.

Only load when the focus is TOEFL iBT format and score logistics. Route non-exam English polish to `english` and IELTS workflows to `ielts`.

## State location

TOEFL prep state may exist under portable roots. Resolve `<state_root>` once per invocation before any read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/toefl/`, `<workspace>/memory/toefl/`, `~/toefl/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and state must be created, default to `<workspace>/toefl/`.

If data sits at an old location (`~/Clawic/data/toefl/` or `~/clawic/toefl/`), move it into the selected `<state_root>/` layout below and say in one line that you moved it and from where.

User data lives in `<state_root>/toefl/`:

```text
<state_root>/toefl/
├── profile.md       # Goals, target score/scale, test date, target schools
├── sections/        # Per-section progress (reading, listening, speaking, writing)
├── sessions/        # Study session logs
├── practice/        # Practice test results and analysis
├── vocabulary/      # Academic and campus vocabulary tracking
└── feedback.md      # What works, what does not, corrections log
```

## Quick Reference

Load these reference files when specific context is required:

| Topic | When to load | File |
|-------|--------------|------|
| Exam structure and scoring | Current ETS section task types, timing, 1–6 and 0–120 transition scores | `references/exam-config.md` |
| Progress tracking system | Establishing or reviewing progress files under `<state_root>/toefl/` | `references/tracking.md` |
| Study methods and practice | Daily plans, section tactics, mock cadence, error analysis | `references/study-methods.md` |
| University and immigration targets | School cutoffs, MyBest acceptance, score-send timing, visa notes | `references/targets.md` |
| User type adaptations | Student, professional, tutor, or retaker mode | `references/user-types.md` |
| Self-improvement tracking | Effective/ineffective tactics, plateau breaks, prediction calibration | `references/feedback.md` |
| Official sources | Verify format, fees, score release, MyBest, or send-score claims | `references/sources.md` |

## Core Capabilities

1. **Test scheduling** — Work backwards from application deadline → score delivery → score release → test date
2. **Progress tracking** — Monitor section scores, time spent, mastery, and error patterns in `<state_root>/toefl/`
3. **Weak-area identification** — Rank high-ROI task types from logged errors
4. **Score prediction** — Estimate readiness on the active score scale and flag missing evidence
5. **University / immigration research** — Look up TOEFL requirements, MyBest acceptance, waivers, and better-fit tests
6. **Score-send management** — Track free recipients, additional report fees, and delivery windows

## Decision Checklist

Before study planning, gather:
- [ ] Test date and days remaining
- [ ] Target universities/programs or immigration pathway (each has different rules)
- [ ] Current estimated section and overall scores (1–6 and/or 0–120 if the school still quotes the old scale)
- [ ] User type (student, professional, tutor, retaker)
- [ ] Time available for study per week
- [ ] Previous TOEFL attempts and whether MyBest is accepted

## Critical Rules

- **Deadlines first** — Work backwards from application deadline → recipient delivery window → score availability → test date
- **Track everything** — Log sessions, scores, and errors only under the resolved `<state_root>/toefl/`
- **Verify live ETS policy** — Open `references/sources.md` links before quoting fees, timing, task inventory, or score scales
- **Adapt to user type** — Students need admissions logistics; professionals need time-boxed ROI; tutors need multi-student tracking; retakers need gap analysis
- **Score is multi-scale during transition** — From 21 Jan 2026, official reports use section and overall 1–6 scores; a comparable 0–120 overall remains for a two-year transition. Many schools still publish 0–120 cutoffs — translate carefully and confirm the program page
- **MyBest is optional per school** — Score reports include MyBest/superscores, but many programs still require a single sitting
- **Do not invent institutional cutoffs** — Prefer the target school's current English page over memory or third-party blogs