---
name: cpa
description: >
  Prepare for the US CPA exam with Core+Discipline section strategy, 30-month
  credit-window tracking, NTS timing, score-report retake plans, and state
  eligibility checks. Use when the user is scheduling CPA sections, choosing
  AUD/FAR/REG plus BAR/ISC/TCP, tracking credit expiration, or asking about
  CPA Evolution updates. Prefer `exam` for generic quizzes from supplied notes,
  `accounting` for GAAP/IFRS teaching outside exam logistics, `accountant` for
  entity bookkeeping close, and `bar-exam` for US Bar prep.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📊"}'
  related-skills: '{"exam":"Generic practice questions, flashcards, and mock exams from supplied study material rather than CPA section logistics.","accounting":"GAAP/IFRS teaching and judgment outside CPA exam scheduling and credit windows.","accountant":"Entity bookkeeping that closes ledgers rather than CPA exam prep.","bar-exam":"US Bar Exam MBE/essay prep instead of CPA Core+Discipline workflows.","personal-finance-tracker":"Personal cashflow tracking outside CPA exam fees and NTS planning.","study":"Semester coursework systems beyond CPA section sequencing."}'
---

## State location

CPA candidate state may exist in
`<workspace>/cpa/`, `<workspace>/memory/cpa/`, or `~/cpa/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/cpa/`, `<workspace>/memory/cpa/`, `~/cpa/`.
3. If none exists and durable candidate state must be created, default to
   `<workspace>/cpa/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/cpa/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

Legacy path `~/Clawic/data/cpa/` is a migration source only. Copy, validate,
and cut over only after the user chooses migration; do not write there by
default.

Host-shared memory such as workspace `MEMORY.md` is outside `<state_root>` and
needs separate consent. Do not store SSN, full passport numbers, payment
details, NASBA credentials, or third-party private data in CPA state.

```text
<state_root>/
├── profile.md       # Target dates, jurisdiction, current progress
├── sections/        # Per-section progress (AUD, FAR, REG, Discipline)
├── practice/        # Practice results and error analysis
├── nts/             # Notice to Schedule tracking
├── passed/          # Passed sections with credit expiration dates
└── feedback.md      # Study methods that worked or failed for this candidate
```

## When to Use

- Planning US CPA section order under the Core + Discipline model
- Tracking the rolling credit window (commonly 30 months; confirm the Board of Accountancy rule for the candidate's jurisdiction)
- Managing NTS timing, score-report retakes, and state eligibility
- Advising international candidates on evaluation and jurisdiction choice
- Not for generic quiz generation (`exam`), GAAP teaching (`accounting`), entity close (`accountant`), or US Bar prep (`bar-exam`)

## Core path

1. Resolve `<state_root>` before any state read/write.
2. Confirm the candidate's Board of Accountancy / jurisdiction before treating credit-window length, education thresholds, or ethics requirements as fixed.
3. Load only the `references/` leaf needed for the current decision.
4. Open `references/research-sources.md` and re-check the live official page before stating exam structure, blueprints, fees, or credit-window policy as current fact.
5. Keep durable progress under `<state_root>/` when the user wants continuity across sessions.

## Quick Reference

| Topic | File | Load when |
|-------|------|-----------|
| Exam structure and scoring | `references/exam-format.md` | Core/Discipline map, scoring, NTS basics |
| Progress tracking system | `references/tracking.md` | Profile, section files, alerts |
| Study strategies and section order | `references/strategies.md` | Sequencing, retake targeting, busy-season pacing |
| International candidate guide | `references/international.md` | Foreign degree evaluation and state fit |
| User type adaptations | `references/user-types.md` | First-timer, retaker, working pro, international |
| Research anchors | `references/research-sources.md` | Before asserting current official policy |

## Core Capabilities

1. **Section order planning** — Recommend Core and Discipline sequence from background and timeline
2. **Credit-window tracking** — Monitor passed sections and jurisdiction-specific expiration risk
3. **Score analysis** — Parse weaker/comparable/stronger report bands into a retake plan
4. **NTS management** — Track Notice to Schedule validity and schedule readiness
5. **State eligibility** — Match education and experience rules to the candidate's Board
6. **Progress tracking** — MCQ accuracy, simulations practice, hours by section
7. **Retake strategy** — Target weak areas instead of restudying everything

## Decision Checklist

Before creating a study plan, gather:

- [ ] Board of Accountancy / state applying to
- [ ] Current education status (credits, accounting hours)
- [ ] Work situation (full-time, part-time, student)
- [ ] Target timeline for all 4 sections (3 Core + 1 Discipline)
- [ ] Previous CPA attempts with scores, if any
- [ ] Review course in use (Becker, Roger, Surgent, etc.)
- [ ] Candidate type (first-timer, retaker, international, working professional)

## Quality checks

- Confirm jurisdiction before quoting a credit-window length; many Boards moved to 30 months after CPA Evolution, but local rules still control.
- Apply for an NTS only when the candidate can test inside the NTS validity window.
- Treat 75 as the passing threshold for a section; a 74 requires a full retake of that section.
- Prefer positive next actions over stop-only warnings: calculate the cliff date, then propose the next schedulable section.
- Re-check official NASBA / AICPA / Board pages when money, eligibility, or expiration claims matter.
