---
name: competing
description: Trigger when the user wants to analyze a loss or track progress in a competitive domain. Improve systematically by studying winners and applying deliberate practice.
metadata:
  openclaw: '{"emoji": "🏆"}'
---

## Core Framework

Competition is a learning accelerator. Every loss contains the lesson that wins don't.

1. **Analyze the Loss** — Extract lessons from every loss to understand WHY
2. **Study the Winner** — What did they do that you didn't?
3. **Track the Delta** — Measure the gap, watch it shrink
4. **Iterate** — Apply lessons, compete again, repeat

---

## The Post-Loss Protocol

After any competitive loss, extract value:

| Question | Purpose |
|----------|---------|
| At what moment did the outcome shift? | Find the decision point |
| What did they do that I didn't? | Identify the winning move |
| What would I do differently? | Formulate the lesson |
| Is this a pattern? | Check history for repeats |

Maintain objectivity. Focus on internal choices and extract the actionable insight.

---


## State location

This skill uses the following paths for persistent state tracking:

- `<state_root>/competing/domains/`: Directory for per-domain tracking files.
- `<state_root>/competing/rivals.md`: Opponent profiles.
- `<state_root>/competing/log.md`: Win/loss log with lessons.
- `<state_root>/competing/progress.md`: Metrics over time.

Ensure these files are created or read from `<state_root>/competing/`. Always use the dynamic `<state_root>` prefix for paths.

## Tracking (What to Measure)

Create a tracking folder in the user's workspace:

```
<state_root>/competing/
├── domains/           # Per-domain tracking
├── rivals.md          # Opponent profiles
├── log.md             # Win/loss log with lessons
└── progress.md        # Metrics over time
```

For each domain, track:
- Win/loss record with dates
- Specific losses analyzed (who, why, lesson)
- Patterns identified (recurring weaknesses)
- Progress metrics (are lessons translating to wins?)

---

## Rival Intelligence

Know your competition:
- **Profile rivals** — Their strengths, weaknesses, tendencies
- **Monitor changes** — When they improve or change strategy
- **Find their edge** — What specifically makes them beat you?
- **Study up** — Find examples of them losing, analyze what worked

---

## Quick Reference

| Situation | Action |
|-----------|--------|
| Just lost | Run post-loss protocol, add to log |
| Pattern emerging | Document it, create drill/fix |
| Preparing for known rival | Review their profile, past matches |
| Plateau in progress | Analyze recent losses for new patterns |
| Won against usual winner | Document what changed, replicate |

---

## Load Reference

| Need | File | When to load |
|------|------|--------------|
| Domain-specific strategies | `references/domains.md` | When adapting the framework for specific fields like gaming, sports, or business. |
| Deep loss analysis framework | `references/analysis.md` | When conducting a thorough post-loss breakdown to identify root causes. |
| Progress tracking templates | `references/tracking.md` | When establishing or updating progress dashboards and metrics. |
| Feedback loop mechanics | `references/feedback.md` | When verifying that fixes are working and breaking through plateaus. |
| Competitive research | `references/research.md` | When seeking formal methodologies like the AAR framework or Deliberate Practice. |
