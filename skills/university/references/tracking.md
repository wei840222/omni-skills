# Progress Tracking & Analytics

Paths use the resolved `<state_root>`.

## Core Metrics

### Time Invested
- Total hours per degree
- Hours per module
- Hours this week/month
- Trend: increasing, stable, declining

### Completion Progress
- Modules completed / total
- Content consumed (pages, videos, etc.)
- Exercises completed
- Percentage complete

### Mastery Level
- Per-topic mastery scores
- Overall weighted average
- Change over time
- Comparison with targets

### Retention
- Spaced repetition performance
- Forgetting rate by topic
- Items needing more review
- Long-term retention trends

## Dashboard Views

### Quick Glance
```
[Degree Name] - 34% Complete
├── This Week: 8h studied
├── Mastery: 72% average
├── Next Deadline: Exam in 12 days
└── Due Today: 15 flashcards
```

### Detailed Breakdown
- Per-module completion and mastery table
- Open weak topics with last verification date
- Upcoming calendar milestones
- Hours remaining vs plan at current velocity

## Readiness bands

Use evidence bands, not promises:

| Band | Evidence |
|------|----------|
| Not ready | Large untested gaps on high-weight topics |
| Borderline | Core topics practiced; weak areas still failing timed drills |
| Likely ready | Weighted topics show repeated retrieval success under time |
| Overdue for rest | High mastery with rising fatigue markers—protect recovery |

## Update rules

1. Log time and completion the same day when possible
2. Raise mastery only after verification (not after passive reading)
3. Lower mastery when timed drills regress
4. Write durable updates to `<state_root>/degrees/[name]/progress.md`
5. Keep multi-program rollups in `degrees/index.md` without merging raw logs
