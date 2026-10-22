---
name: sat
description: >
  Prepare for the Digital SAT with diagnostics, adaptive-module strategy,
  score tracking, superscore/Score Choice planning, and college targeting.
  Use when the user needs Digital SAT structure (Bluebook MST modules),
  RW/Math practice, score prediction, admissions ranges, or test-date logistics.
  Route ACT prep to `act-prep`, TOEFL to `toefl`, IELTS to `ielts`, generic
  quizzes from notes to `exam`, semester coursework to `study`, and general
  English polish to `english`.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📝"}'
  related-skills: '{"act-prep":"ACT section strategy, enhanced-format checks, and ACT college targeting instead of Digital SAT.","toefl":"TOEFL iBT structure and score logistics instead of SAT.","ielts":"IELTS Academic/GT workflows instead of SAT.","exam":"Generate practice questions or mocks from supplied notes rather than Digital SAT format workflows.","study":"Semester coursework schedules beyond SAT-focused prep.","tutor":"General multi-subject tutoring outside SAT section tactics.","english":"General English writing and correction outside scored SAT RW tasks.","grammar":"Pure correctness passes where SAT task strategy must not move.","writing":"Long-form drafting in the user voice outside SAT RW drills.","gaokao":"Gaokao workflows for China admissions instead of College Board SAT."}'
---

## When to load

Load when the user is preparing for the Digital SAT (College Board Scholastic Assessment Test) for US college admissions. Trigger for diagnostic assessment, Bluebook adaptive-module strategy, RW/Math drills, score-gap planning, superscore/Score Choice checks, college targeting, or progress tracking.

Only load when the focus is Digital SAT format and admissions logistics. Route ACT to `act-prep`, TOEFL to `toefl`, IELTS to `ielts`, and non-exam English polish to `english`.

## State location

SAT prep state may exist under portable roots. Resolve `<state_root>` once per invocation before any read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/sat/`, `<workspace>/memory/sat/`, `~/sat/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and state must be created, default to `<workspace>/sat/`.

If data sits at an old location (`~/Clawic/data/sat/` or `~/clawic/sat/`), move it into the selected `<state_root>/` layout below and say in one line that you moved it and from where.

User data lives in `<state_root>/`:

```text
<state_root>/
├── profile.md       # Target score, test dates, colleges, baseline, format notes
├── sections/        # Per-section progress (rw.md, math.md)
├── practice/        # Practice test results and analysis
├── vocabulary/      # Words-in-context lists with spaced repetition
├── mistakes/        # Error log with patterns
└── feedback.md      # What study methods work best
```

Use the selected `<state_root>` for every state operation. Never write runtime state into this skill package. Do not store College Board passwords, payment cards, or full government ID numbers under `<state_root>/`.

## Quick Reference

Load these reference files when specific context is required:

| Topic | When to load | File |
|-------|--------------|------|
| Exam structure and scoring | Bluebook modules, timing, domains, adaptive MST | `references/exam-format.md` |
| Progress tracking system | Establishing or reviewing progress files under `<state_root>/` | `references/tracking.md` |
| Study methods and practice | Daily plans, ROI triage, mock cadence | `references/strategies.md` |
| Test-taking techniques | Pacing, flagging, Module 1 strategy, Desmos use | `references/techniques.md` |
| College admissions planning | Score bands, test-optional, superscore, Score Choice | `references/colleges.md` |
| User type adaptations | Student, retaker, parent, tutor, international modes | `references/user-types.md` |
| Official sources | Verify format, scoring, practice, or score-send claims | `references/sources.md` |

## Core Capabilities

1. **Diagnostic assessment** — Establish baseline total/section scores and weak domains
2. **Adaptive practice** — Target high-ROI RW/Math topics from logged errors
3. **Progress tracking** — Monitor scores, timing, accuracy trends under `<state_root>/`
4. **Score prediction** — Estimate readiness from recent timed Bluebook-style practice
5. **Mistake analysis** — Categorize errors and schedule review
6. **College matching** — Align target score with each school's published range and policy
7. **Test date planning** — Optimize attempts, superscoring, and Score Choice

## Decision Checklist

Before creating a study plan, gather:

- [ ] Target test date(s) and days remaining
- [ ] Target total score (or target colleges to derive a score)
- [ ] Current estimated or diagnostic RW / Math / Total
- [ ] Hours per week available for prep
- [ ] Previous SAT attempts and whether colleges superscore or require all scores
- [ ] User type (first-timer, retaker, international, parent, tutor, late starter)
- [ ] Device readiness for Bluebook (own device / lending / center policy)

## Critical Rules

- **Diagnose first** — Assess current level before locking a multi-week plan
- **Confirm Digital SAT facts from sources** — Timing, domains, and score policy drift; prefer `references/sources.md` over memory
- **Weakness-first** — Prioritize topics with highest point-per-hour ROI
- **Timed practice mandatory** — Simulate Bluebook module timing; untimed drills do not predict test-day scores
- **Track every question** — Log to `<state_root>/` for pattern analysis
- **Module 1 matters** — Multistage adaptive design: Module 1 performance routes Module 2 difficulty and score ceiling
- **Superscore and Score Choice are school-specific** — Verify each target before advising retakes or which dates to send
- **College context matters** — A 1400 means different things for MIT vs a regional state school
- **Assessment boundary** — Support learning before/after a sitting. For a live, proctored SAT, give conceptual strategy and practice only—do not supply answers to active test items

## Security and privacy

- Keep scores, college lists, and study notes local under `<state_root>/`
- Do not request or store College Board account passwords, payment cards, or full government ID numbers
- Prefer official College Board / Bluebook / Khan Academy pages in `references/sources.md` for format, fees, and score-policy claims
