---
name: workouts
description: Build a personal workout tracking system with exercises, routines,
  progression, and PRs.
metadata:
  clawdbot: '{"emoji": "💪", "requires": {"bins": [], "config": ["<state_root>/"]},
    "os": ["linux", "darwin", "win32"], "configPaths": ["<state_root>/"], "displayName":
    "Workouts"}'
  openclaw: '{"requires": {"config": ["<state_root>/"]}}'
  related-skills:
  - habits
  - health
  - calendar
  - goals
  - fitness
---

## When to load

Load this skill when the user wants to log a workout, track exercises, check progression, create routines, or build a personal fitness tracking system.

## Core Behavior

- User logs a workout → record exercises, sets, reps, weight
- Track progression → surface PRs, trends, plateaus
- Suggest based on history → "last time you did 3x8 at 60kg"
- Create `<state_root>/` as workspace

## Workout Logging

See [workout-logging.md](references/workout-logging.md) for detailed logging format.

## Progression and PRs

See [progression-tracking.md](references/progression-tracking.md) for tracking personal records and trends.

## Workflow Guidelines

See [workflow-guidelines.md](references/workflow-guidelines.md) for progressive enhancement and proactive suggestions.

## Directory Structure

```
<state_root>/
├── logs/
│   ├── 2024-03-15.md
│   └── 2024-03-17.md
├── routines/
│   ├── push-day.md
│   └── pull-day.md
├── exercises.md
└── prs.md
```

## Integration Points

- Habits: "workout 4x/week" as habit
- Calendar: schedule workout days
- Health: weight, measurements if tracking body composition

## What NOT To Suggest

- Complex periodization before basics are consistent
- Calorie/macro tracking in workout log — separate concern
- App with features they won't use
- Comparing to others — track personal progress only
