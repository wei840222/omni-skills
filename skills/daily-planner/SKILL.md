---
name: daily-planner
description: "Execute daily planning, time blocking, and commitment tracking to protect time and achieve top priorities."
metadata:
  openclaw: '{"emoji":"📆"}'
---

## Reference Loading

| File | Purpose | When to load |
|------|---------|--------------|
| `references/profiles.md` | Configure by user type (exec, freelancer, parent, student, founder) | Load on first use to determine user profile or when the user changes their profile context. |
| `references/routines.md` | Morning briefing, evening review, weekly planning | Load when performing a morning, evening, or weekly review. |
| `references/priorities.md` | Top 3 system, urgent vs important matrix | Load when generating priorities or filtering tasks by importance. |
| `references/calendar.md` | Time blocking, deep work protection, conflict detection | Load when blocking time or scheduling tasks in the calendar. |
| `references/tracking.md` | Commitment tracking, follow-up reminders | Load when the user makes a commitment, or when checking for overdue promises. |
| `references/research.md` | Background domain knowledge | Load when explaining the rationale behind time management practices. |

## Storage

Resolve `<state_root>` from the runtime-approved writable state location; if no state location is available, ask the user before creating persistent planner data. Store planner state in `<state_root>/planner/`:
- **config** — Profile, energy windows, constraints
- **today** — Current day plan (regenerated daily)
- **commitments** — Open commitments and follow-ups
- **weekly** — Week overview with deadlines
- **archive/** — Past plans for patterns

## What the Agent Does

| User Says | Agent Action |
|-----------|--------------|
| "Plan my day" | Generate time-blocked schedule based on priorities and energy |
| "What's urgent?" | Filter top 3 from calendar/tasks, show deadline proximity |
| "Protect my morning" | Propose a deep-work block, defer non-critical work, and prepare DND actions for confirmation |
| "I promised X to Y" | Propose a commitment record and follow-up reminder; save or schedule only with authorization |
| "Am I overcommitted?" | Analyze week, flag conflicts, suggest cuts |
| "Weekly review" | Summarize done/pending, adjust next week, archive completed |

## Core Loop

**Morning (configurable time):**
1. Pull calendar events, pending tasks, and open commitments only from connected tools the runtime makes available.
2. If calendar or task access is unavailable, ask the user for their fixed commitments and task list; produce a planning draft from supplied information rather than claiming a live check.
3. Apply profile rules (energy windows, constraints).
4. Generate Top 3 priorities (what MUST happen today).
5. Produce briefing: 5 bullets max, critical first.

**During day:**
- Propose new commitments from conversations; persist them only with the authorization described below.
- Surface deadline proximity (48h, 24h, 2h) from available authorized data.
- Batch interruptions and filter by configured urgency.

**Evening:**
- What got done, what moved forward
- Commitments made today logged
- Tomorrow's preview

Load `references/routines.md` for full workflow details.

## Priority Rules

- **Top 3 only** — if user lists >3, force ranking
- **Important > Urgent** — deadline pressure ≠ high impact
- **Energy match** — hard tasks to peak hours, admin to low-energy
- **Buffer mandatory** — keep schedule to a maximum of 80% capacity, leaving 20% slack

Load `references/priorities.md` for prioritization framework.

## Profile-Based Behavior

The agent adapts to user type. On first use, ask or infer profile:

- **Executive**: Calendar-driven, meeting prep, delegation suggestions
- **Freelancer**: Project-based, deadline tracking, client context
- **Parent**: Family-work balance, coordination, contingency plans  
- **Student**: Academic calendar, exam periods, study sessions
- **Founder**: Multi-area tracking, interruption filtering, deep work protection

Load `references/profiles.md` for profile-specific behaviors.

## Commitment Tracking

When the user authorizes persistent tracking and a writable `<state_root>` is available:
- Extract a promise from conversation, such as "I'll send you X by Y".
- Add it to the commitments file with its deadline.
- Remind before the deadline (configurable: 24h, 48h).
- Flag overdue commitments until resolved.

Otherwise, return the proposed commitment and deadline for the user to confirm or save.

Load `references/tracking.md` for commitment workflow.
