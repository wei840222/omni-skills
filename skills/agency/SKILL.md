---
name: agency
description: Manage service agency operations including client onboarding, project tracking, proposal pricing, and team coordination. Use when managing, scaling, or structuring an agency business.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🏢"}'
---

## When to Use

User wants to start or scale a service agency: marketing, development, design, consulting, content, automation, or any service business. Agent handles operations so human focuses on clients and strategy.

## Quick Reference

| Area | File | When to load |
|------|------|--------------|
| Client onboarding | `references/onboarding.md` | When starting a new client engagement or intake process |
| Pricing and proposals | `references/pricing.md` | When estimating scope, calculating costs, or generating proposals |
| Project management | `references/projects.md` | When checking status, updating timelines, or tracking active work |
| Client communication | `references/communication.md` | When drafting updates, responding to feedback, or addressing issues |
| Deliverables workflow | `references/deliverables.md` | When producing, reviewing, or delivering final work to a client |
| Team coordination | `references/team.md` | When assigning tasks, checking capacity, or briefing team members |
| Agency-type specifics | `references/by-type.md` | When you need metrics or common deliverables for a specific niche |
| Learning system | `references/feedback.md` | When reviewing completed projects, logging estimates, or updating SOPs |

## State location

Agency state may exist in `<workspace>/agency/`, `<workspace>/memory/agency/`, or `~/agency/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/agency/`, `<workspace>/memory/agency/`, `~/agency/`.
3. If none exists and state must be created, default to `<workspace>/agency/`.

Use the selected `<state_root>` for every state operation in this skill.

## Workspace Structure

Agency data lives in `<state_root>/`:

```
<state_root>/
├── clients/           # One file per client
│   ├── index.md       # Client list with status
│   └── [name].md      # Client profile, history, preferences
├── projects/          # Active project tracking
├── templates/         # Reusable proposals, briefs, reports
├── knowledge/         # SOPs, learnings, case studies
└── config.md          # Rates, margins, team structure
```

## Operating sequence

1. Identify the agency operation and load the matching reference from Quick Reference.
2. Resolve `<state_root>` before reading or recording agency data.
3. Draft the requested plan, proposal, status update, or deliverable using the relevant reference.
4. Present external client communications and proposals for human approval before sending.

## Core Operations

**Client intake:** Brief arrives (audio, email, doc) → Extract scope, budget, timeline → Generate structured brief → Identify and flag risk factors (e.g., scope creep, unrealistic deadlines) → Create client folder.

**Pricing:** Given scope → Apply rate card from config → Calculate estimate with complexity multipliers → Generate proposal PDF → Compare with historical similar projects.

**Project tracking:** Maintain unified board of all active projects → Alert on deadlines → Detect stalled projects → Generate weekly status by client.

**Deliverables:** Transform rough notes/input → Structured deliverable → Review against brief → Adapt to multiple formats if needed.

## Safety and quality boundaries

- Present proposals and client communications for explicit human approval before sending.
- Surface a budget overrun or deadline risk with its impact and a proposed recovery path.
- Record approved corrections in the relevant template or knowledge record.
- Use prior client history to preserve context while keeping each new decision traceable.

## Config Fields

Create `<state_root>/config.md` with rates, team, and margins. See `references/pricing.md` for format.
