---
name: neet
description: Plan NEET-UG preparation, track study and mock-test progress, identify weak areas, and explain official admission or counselling guidance. Use when a learner, parent, or tutor asks about NEET, medical entrance preparation, AIIMS, mock scores, or counselling; verify current cutoffs and rules from official sources before giving them.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎓"}'
---

## Use this skill

Use this skill for NEET-UG study planning, progress review, mock analysis, wellbeing support, and official-counselling navigation. Ask for the exam year, current score or subject breakdown, category, domicile, and learner role before making a personalised plan. Treat historical score-to-rank tables, cutoffs, seat counts, schedules, and eligibility as context—not current facts—and verify them from the current NTA, MCC, and relevant state-counselling notices.

## State location

Resolve `<state_root>` once before any state operation. Use an explicit host-provided override first; otherwise inspect these candidates in order and use the first existing directory:

1. `<workspace>/neet/`
2. `<workspace>/memory/neet/`
3. `~/neet/`

`<workspace>` comes from the host/runtime, not the shell working directory. If several candidates exist, use only the highest-precedence one and report the conflict; do not merge or synchronise them. Create `<workspace>/neet/` only when no candidate exists and the user asks to save progress. Keep all later reads and writes under the resolved `<state_root>`; never migrate legacy paths automatically.

## Reference routing

| Need | Load |
|---|---|
| Current exam pattern, eligibility, registrations, or official notices | `references/exam-config.md` and the linked official notice for the exam year |
| Study plan, weak-area work, revision, or mock strategy | `references/study-methods.md` |
| Saving or reviewing progress and mock results | `references/tracking.md` |
| Stress, burnout, sleep, or parent support | `references/wellbeing.md` |
| Counselling, seats, colleges, fees, or cutoffs | `references/targets.md`; then current MCC/state notices |
| Student, parent, dropper, repeater, or tutor adaptation | `references/user-types.md` |
| Source verification and annual-update rules | `references/domain.md` |

## Working flow

1. Identify the user role and goal; gather only the missing decision inputs.
2. For planning or score review, load the relevant study and tracking references. Prioritise a small next action, an error category, and a sustainable review cadence over an unsupported rank prediction.
3. For exam rules, cutoffs, eligibility, counselling, or college claims, consult the current official notice before answering. State the notice year and distinguish qualifying cutoffs from college-closing ranks.
4. For distress, load `references/wellbeing.md`, respond supportively, and prioritise immediate safety support when self-harm or imminent danger is mentioned.
5. Create state only with user intent. Store profile, subjects, sessions, mocks, and flashcards beneath `<state_root>/` as needed.

## Data layout

```text
<state_root>/
├── profile.md       # goals, exam year, category, domicile
├── subjects/        # progress and weak areas
├── sessions/        # study logs
├── mocks/           # results and error analysis
├── flashcards/      # review material and schedule
└── feedback.md      # plan adjustments
```

## Core rules

- Prioritise accuracy, sustainable study, and error analysis over generic high-hour targets.
- Use NCERT and the current official syllabus as the primary study baseline; verify any changed syllabus or rule against NTA material.
- Log a score, error type, and next review action when tracking a mock.
- Never present approximate historical cutoffs, ranks, fees, seats, or dates as a current guarantee.
- Keep wellbeing and autonomy central; a study plan is adjustable, not a mandate.
