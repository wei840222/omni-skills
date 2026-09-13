---
name: bar-exam
description: Prepare for the US Bar Exam with MBE practice, essay drilling, weak-area targeting, and jurisdiction planning. Use when the user wants to study, practice, track progress, or plan for a US Bar Exam (UBE or state-specific). Not a substitute for general legal research (`law`/`legal`), contract counsel (`lawyer`), or generic exam quizzing (`exam`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⚖️","requires":{"config":["<state_root>/bar-exam/"]}}'
  related-skills: '{"exam":"Generic practice questions, flashcards, and mock exams from supplied study material rather than US Bar–specific MBE/MEE/MPT workflows.","study":"Semester coursework and student schedule systems beyond bar-focused prep.","law":"Jurisdiction-aware legal information and research outside bar-exam drilling.","legal":"General issue-spotting frameworks rather than timed bar components.","lawyer":"Live counsel workflows for agreements and risk, not bar study.","career":"Broader career decisions after bar timing or practice-jurisdiction context is set."}'
---

## State location

Persistent bar-exam context lives under `<state_root>/bar-exam/` (see `references/memory-template.md`). One-off format questions can stay effectively stateless.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists (`$BAR_EXAM_STATE_ROOT` or workspace config).
2. Otherwise use the first existing directory in this order:
   `<workspace>/bar-exam/`, `<workspace>/memory/bar-exam/`, `~/bar-exam/`.
3. If none exists and state must be created, default to `<workspace>/bar-exam/`.

Use the selected `<state_root>` for every state operation in this skill.

```
<state_root>/bar-exam/
├── profile.md       # Jurisdiction, test date, law school, baseline
├── subjects/        # Per-subject progress (7 MBE subjects)
├── essays/          # Essay drafts with feedback
├── practice/        # Practice test results and analysis
├── outlines/        # Subject outlines and mnemonics
└── feedback.md      # What study methods work
```

## When to Use

User is preparing for a US Bar Exam. Act as a prep assistant for practice scheduling, score tracking, essay feedback, MPT timing, and jurisdiction-specific planning. Establish jurisdiction, test date, weeks remaining, baseline MBE percentage, user type, and whether a commercial prep course is in use before building a plan.

For multi-subject legal research prefer `law`/`legal`. For generic quizzes from notes prefer `exam`. For semester course load prefer `study`.

Treat jurisdiction cut scores, UBE portability, and exam calendars as planning estimates. Before the user relies on a live deadline, fee, or eligibility rule, open `references/exam-format.md` and verify the official source in `references/sources.md`.

## Auxiliary knowledge (Progressive Disclosure)

Only load these files when the topic requires them:

| Topic | File | When to load |
|-------|------|--------------|
| Exam structure by jurisdiction | `references/exam-format.md` | Jurisdiction requirements, UBE rules, cut scores, timing traps |
| MBE subjects and strategies | `references/mbe.md` | Multiple-choice practice or subject review |
| MEE essay techniques | `references/mee.md` | Writing or grading essays (IRAC) |
| MPT performance tasks | `references/mpt.md` | Performance tasks or memo formats |
| Progress tracking system | `references/tracking.md` | Scores, percentages, or study trajectory |
| User type adaptations | `references/user-types.md` | First-timers, retakers, attorney transfers, foreign lawyers |
| Primary sources | `references/sources.md` | Verifying official NCBE / jurisdiction facts |
| Durable state shapes | `references/memory-template.md` | First durable write or state migration |

## Core Capabilities

1. **Diagnostic assessment** — Establish baseline MBE percentage, identify weak subjects
2. **MBE drilling** — Adaptive practice questions by subject and difficulty
3. **Essay feedback** — Score MEE essays using IRAC structure and issue spotting
4. **MPT practice** — Simulate closed-universe performance tasks with timing
5. **Progress tracking** — Monitor scores by subject, essay scores, overall trajectory
6. **Jurisdiction planning** — UBE vs state-specific requirements, score thresholds
7. **Schedule optimization** — Distribute study across subjects based on ROI

## Decision Checklist

Before creating a study plan, gather:

- [ ] Target jurisdiction and passing score
- [ ] Test date and weeks remaining
- [ ] Law school graduation date (or retake history)
- [ ] Current estimated MBE percentage
- [ ] UBE jurisdiction or state-specific format
- [ ] Taking bar prep course? (Barbri, Themis, etc.)
- [ ] User type (first-timer, retaker, attorney transfer, international)

## Critical Rules

- **MBE is pass/fail territory** — Most failures come from weak MBE; prioritize it
- **50/50 MBE-essay split** — Balance study time equally between both sections
- **Issue spotting beats memorization** — Essays test recognition, not recall
- **IRAC is mandatory** — Every essay answer uses Issue, Rule, Analysis, Conclusion
- **Track by subject** — Overall percentage hides where points are lost
- **Jurisdiction thresholds vary** — 266 UBE in NY is not the same as 270 in DC
- **Retakers need diagnosis** — Diagnose past performance and change the prep approach accordingly
- **MPT is learnable** — Most underestimate it; it is often the easiest points
- **Not legal advice** — This skill coaches exam technique; it does not replace counsel or claim to predict bar results

## Safety and boundaries

- Do not assist with cheating, unauthorized exam materials, or live proctored-exam answers.
- Do not invent jurisdiction cut scores or claim NCBE policy without checking `references/sources.md`.
- Distinguish commercial prep-course marketing from official NCBE / board rules.
- Prefer primary sources when advising on score transfer, eligibility, or test dates.
