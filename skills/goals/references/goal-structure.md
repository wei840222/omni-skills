# Goal structure

## Classify the request

- **Goal:** a desired outcome, such as completing a marathon, saving €10k, or reaching Spanish B1.
- **Project:** a defined end state delivered through coordinated work, such as planning a wedding.
- **Habit:** a recurring behavior, such as exercising four times per week.

Goals can create projects and habits. Keep the current request at its natural level: use a project plan for the work, a habit tracker for repetition, and this skill for the outcome and its review.

## Goal file

Store one saved goal at `<state_root>/active/<goal-name>.md` with:

- **Outcome:** specific success condition.
- **Why:** the user’s motivation and meaning.
- **Target date:** a date or an explicitly open-ended horizon.
- **Milestones:** observable checkpoints.
- **Current status:** on track, behind, ahead, paused, or blocked.
- **Progress log:** concise dated evidence, blockers, and breakthroughs.

## State tree

```text
<state_root>/
├── active/
│   └── <goal-name>.md
├── achieved/
├── abandoned/
└── someday.md
```

Create a child path only when it is needed. A completed goal moves to `<state_root>/achieved/`; a consciously reprioritized goal moves to `<state_root>/abandoned/` with a short reason.

## Milestones

Break a large outcome into checkable milestones that show meaningful progress. For example:

- Marathon: 5k → 10k → half marathon → full marathon.
- Savings: €2.5k per quarter toward €10k.
- Language learning: A1 → A2 → B1.

Use categories such as health, career, finances, relationships, learning, or creative work only when they make the user’s review easier.
