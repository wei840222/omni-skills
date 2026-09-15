---
name: usmle
description: Manage USMLE study schedules, track question bank performance, and analyze weak areas to optimize residency match prospects. Use when the user asks for USMLE Step 1/2 CK/3 planning, Q-bank tracking, NBME analysis, IMG/retaker adaptations, or residency score targeting. Do not load for general medical advice, non-USMLE coursework systems, or clinical diagnosis.
metadata:
  openclaw: '{"emoji":"🩺"}'
---

## When to load references

Load the following references on-demand when user needs specific guidance:
- `references/exam-config.md`: Load when configuring exam timelines or explaining scoring.
- `references/tracking.md`: Load when setting up tracking for Q-banks or practice tests.
- `references/study-methods.md`: Load when suggesting learning strategies or dedicated periods.
- `references/wellbeing.md`: Load when burnout signs appear or stress management is needed.
- `references/targets.md`: Load when setting score goals for specific specialties.
- `references/user-types.md`: Load when adapting the plan for IMGs, US DOs, or retakers.
- `references/sources.md`: Load when verifying format, scoring, eligibility, or calendar claims against primary authorities.

## State location

USMLE state may exist in `<workspace>/usmle/`, `<workspace>/memory/usmle/`, or `~/usmle/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/usmle/`, `<workspace>/memory/usmle/`, `~/usmle/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and state must be created, default to `<workspace>/usmle/`.

Use the selected `<state_root>` for every state operation in this skill. Never write runtime state into this skill package. Do not store credentials, portal passwords, or payment details under `<state_root>/`.

## Data Storage

User data lives in `<state_root>/`:
```
<state_root>/
├── profile.md       # Goals, target score, exam dates, user type
├── steps/           # Per-step progress (step1, step2ck, step3)
├── sessions/        # Study session logs
├── assessments/     # NBME, UWorld self-assessments, practice tests
├── qbank/           # Question bank tracking (UWorld, Amboss, etc.)
└── feedback.md      # What works, what doesn't
```

If older notes still live only at `~/usmle/` or `~/Clawic/data/usmle/`, migrate into the resolved `<state_root>` on request and keep a one-line pointer of the move.

## Decision Checklist

Before study planning, gather:
- [ ] Target Step (1, 2 CK, or 3)
- [ ] Exam date and days remaining
- [ ] User type (US MD, US DO, IMG, retaker)
- [ ] Target score range or specialty
- [ ] Current baseline (NBME/UWSA score if available)
- [ ] Resources in use (UWorld, First Aid, Anki, etc.)

## Critical Rules

- **ROI-first** — Prioritize organ systems with highest points-per-hour potential for this user's gaps
- **Track everything** — Log sessions, scores, wrong questions to `<state_root>/`
- **Adapt to user type** — US MDs need Step timing for M3; IMGs need score maximization for competitiveness; retakers need targeted remediation
- **Step 1 is P/F** — Since 2022, Step 1 is pass/fail. Step 2 CK score is now critical for residency
- **Question-first** — UWorld questions teach better than passive reading
- **Wellbeing matters** — Monitor for burnout; dedicated study periods are intense
- **Verify live policy** — Before quoting fees, calendars, cut scores, or ECFMG pathways, open `references/sources.md` primary URLs
- **Scope boundary** — This skill coaches exam prep and match planning; it is not clinical diagnosis or medical advice

## Common traps

- Treating Step 1 three-digit folklore as current scored output after the pass/fail transition
- Ignoring burnout when Q-bank averages drop and pushing more volume instead of recovery
- Giving IMG pathway or match advice without checking ECFMG / NRMP primary pages
- Writing state into the skill package or a hardcoded Clawic path
