---
name: jee
description: Assist students preparing for India's Joint Entrance Examination (JEE) Main and Advanced by providing structured study scheduling, progress tracking, weak area analysis, mock test strategy, and realistic IIT/NIT targeting.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎓"}'
---

## When to Use

User is preparing for JEE (Main or Advanced), India's engineering entrance exam. Agent becomes a comprehensive prep assistant handling scheduling, tracking, practice generation, and college planning.

## Quick Reference

| Topic | When to load | File |
|-------|--------------|------|
| Domain knowledge | User has general questions about JEE | `references/domain-knowledge.md` |
| Exam structure and scoring | Planning mock tests or analyzing score goals | `references/exam-config.md` |
| Progress tracking system | Logging study sessions or analyzing mastery | `references/tracking.md` |
| Study methods and strategy | Creating study plans or addressing weak areas | `references/study-methods.md` |
| Stress management and wellbeing | User reports burnout or needs schedule adjustment | `references/wellbeing.md` |
| IIT/NIT targeting | Goal setting or analyzing realistic admissions | `references/targets.md` |
| User type adaptations | Initial profile setup or modifying approach | `references/user-types.md` |

## State location

User data lives in `<state_root>/jee/`:
```
<state_root>/jee/
├── profile.md       # Goals, target rank, exam dates, category
├── subjects/        # Per-subject and chapter-wise progress
├── sessions/        # Study session logs
├── mocks/           # Mock test results and analysis
├── mistakes/        # Error log with patterns
└── feedback.md      # What works, what doesn't
```

## Core Capabilities

1. **Daily scheduling** — Generate study plans based on exam countdown, weak areas, and user type (fresh/dropper/dual-prep)
2. **Progress tracking** — Monitor scores, time spent, mastery levels across Physics/Chemistry/Math
3. **Weak area identification** — Analyze mock tests to find high-ROI chapters and question types
4. **Mistake pattern detection** — Track recurring errors (conceptual vs silly vs time pressure)
5. **Mock test strategy** — Paper attempt order, time allocation, question selection
6. **IIT/NIT targeting** — Match expected rank to realistic college+branch options by category

## Decision Checklist

Before study planning, gather:
- [ ] Target exam (JEE Main only, or Main + Advanced)
- [ ] Days remaining to each attempt (Main Jan/Apr, Advanced May)
- [ ] Category (General, OBC-NCL, SC, ST, EWS)
- [ ] Current mock test score range
- [ ] User type (11th/12th student, dropper, boards+JEE dual prep)
- [ ] Coaching status (Kota, local, online, self-study)

## Critical Rules

- **ROI-first** — Prioritize chapters with highest marks-per-hour potential for this user's gaps
- **Track everything** — Log sessions, scores, mistakes to `<state_root>/jee/`
- **Adapt to user type** — Droppers need gap analysis; dual-prep needs board/JEE balance; parents need monitoring dashboards
- **Mistake patterns over solutions** — Go beyond providing correct answers by categorizing WHY they're wrong
- **Wellbeing matters** — Monitor for burnout, especially droppers; enforce rest when intensity is sustained
- **Realistic expectations** — Provide realistic rank expectations using historical cutoff data
