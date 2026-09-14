---
name: ielts
description: >
  Prepare for IELTS Academic or General Training with diagnostics, mock tests,
  band score targeting, and study planning. Use when the user needs IELTS
  section strategy, Writing/Speaking band feedback, CLB/university score targets,
  or progress tracking. Route general English polish to `english`, TOEFL iBT to
  `toefl`, generic quiz generation from notes to `exam`, semester coursework to
  `study`, Digital SAT to `sat`, and ACT prep to `act-prep`.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎓"}'
  related-skills: '{"english":"General native-style English writing and correction outside IELTS band criteria.","toefl":"TOEFL iBT structure, scoring, and admissions prep instead of IELTS.","exam":"Generate practice questions or mock exams from supplied notes rather than IELTS-format workflows.","study":"Semester coursework schedules beyond IELTS-focused prep.","sat":"Digital SAT structure and admissions prep instead of IELTS.","act-prep":"ACT section strategy and college targeting instead of IELTS.","tutor":"General multi-subject tutoring outside IELTS band descriptors."}'
---

## When to load

Load when the user is preparing for the IELTS (International English Language Testing System) exam. Trigger for diagnostic assessment, practice test generation, essay evaluation against official band criteria, speaking mock interviews, or band score gap analysis.

Only load when the focus is strictly on the IELTS format, avoiding general English learning.

## State location

IELTS prep state may exist under portable roots. Resolve `<state_root>` once per invocation before any read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/ielts/`, `<workspace>/memory/ielts/`, `~/ielts/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and state must be created, default to `<workspace>/ielts/`.

If data sits at an old location (`~/Clawic/data/ielts/` or `~/clawic/ielts/`), move it into the selected `<state_root>/` layout below and say in one line that you moved it and from where.

User data lives in `<state_root>/ielts/`:

```text
<state_root>/ielts/
├── profile.md       # Goals, target band, exam date, test type
├── sections/        # Per-section progress (listening, reading, writing, speaking)
├── sessions/        # Study session logs
├── mocks/           # Practice test results and analysis
├── essays/          # Writing samples with feedback
└── speaking/        # Speaking recordings and transcripts
```

## Quick Reference

Load these reference files when specific context is required:

| Topic | When to load | File |
|-------|--------------|------|
| Exam structure and scoring | User needs rules for Academic/GT test formats and band score calculation. | `references/exam-config.md` |
| Progress tracking system | Establishing or reviewing the user's progress tracking in `<state_root>/ielts/`. | `references/tracking.md` |
| Study methods and practice | Planning study sessions or addressing specific weaknesses in a skill. | `references/study-methods.md` |
| Score targets by purpose | User needs target bands for university, immigration (CLB), or professional registration. | `references/targets.md` |
| User type adaptations | Adapting agent tone and focus based on user profile (retaker, professional, student). | `references/user-types.md` |
| Self-improvement tracking | Identifying recurring error patterns and determining if the user is ready to test. | `references/feedback.md` |
| Official sources | Verifying format, band descriptors, One Skill Retake, or CLB mapping claims. | `references/sources.md` |

## Core Capabilities

1. **Diagnostic assessment** — Identify current band level and weak sections
2. **Band gap analysis** — Compare current vs target scores, calculate points needed
3. **Practice generation** — Create fresh tasks for any section (charts, essays, prompts)
4. **Writing evaluation** — Score essays against IELTS criteria (TA, CC, LR, GRA)
5. **Speaking simulation** — Run timed mock interviews with feedback
6. **Progress tracking** — Monitor scores, time spent, improvement trends
7. **Target guidance** — Match scores to university/immigration requirements

## Decision Checklist

Before study planning, gather:
- [ ] Test type: Academic or General Training
- [ ] Exam date and days remaining
- [ ] Target overall band and per-section minimums
- [ ] Purpose (university, immigration, professional registration)
- [ ] User type (first-timer, retaker, professional, student)
- [ ] Current estimated band from diagnostic or prior attempt

## Critical Rules

- **Academic vs GT** — Writing Task 1 differs completely (graph vs letter). Confirm type first.
- **No section below minimum** — Many targets require ALL bands at threshold (e.g., 6.5 each)
- **2-year validity** — Scores expire. Plan retakes if immigration timeline extends.
- **One Skill Retake** — Available within 60 days of original test on eligible dates/centers. Suggest when one section drags overall down; verify current eligibility on official IELTS pages before advising.
- **Band descriptors** — Use official criteria for Writing/Speaking feedback, not impressions.
- **Source freshness** — Re-check `references/sources.md` anchors before quoting hard band cutoffs, CLB mappings, fees, or retake windows.
