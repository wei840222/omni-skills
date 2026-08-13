---
name: projects
description: Manage projects, define scopes, capture tasks, review progress, and organize project folders. Trigger when starting, managing, reviewing, or completing a project.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"📁"}'
  related-skills: '{"calendar-planner":"Integrates project deadlines and milestones into the calendar.","goals":"Connects individual projects to larger personal goals.","invoice":"Used for client projects that require billing.","invoices":"Used for client projects that require billing."}'
---

## State location

Projects state may exist in `$WORKSPACE/projects/`, `$WORKSPACE/memory/projects/`, or `~/projects/`.
Before reading or writing state, resolve `$STATE_ROOT` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `$WORKSPACE/projects/`, `$WORKSPACE/memory/projects/`, `~/projects/`.
3. If none exists and state must be created, default to `$WORKSPACE/projects/`.

Use the selected `$STATE_ROOT` for every state operation in this skill.

## Core behavior

- When the user names a project, help define scope and create `$STATE_ROOT/$PROJECT_NAME/` only with the requested state change. Capture added tasks in that project context and surface stalled projects during a review.
- Everything this skill reads or writes is a plain local note. In a shared box, update or remove only rows written by this skill and matched by their identity key; read, but never rewrite or delete, another skill's rows. Name every write and deletion as it happens.

## First question

- Define success before starting: “What does done look like?”
- Establish boundaries on day one. If success cannot be defined, the project is not ready to start.

## Project types

- **One-time goal:** clear end state, then archive (for example, moving apartments or planning a trip).
- **Ongoing area:** maintained continuously, such as health or career.
- **Client work:** external deadline, deliverables, and often billing.
- **Learning:** skill acquisition that may create projects.
- **Creative:** writing, art, or building where process matters as much as output.

## Project structure

Create only the files the project needs:

```text
$STATE_ROOT/$PROJECT_NAME/
├── README.md  # what, why, done criteria, and deadline if any
├── tasks.md   # simple checklist, extended as work is discovered
└── notes.md   # decisions, research, and reference material
```

For larger projects, group work into phases or areas, note dependencies and owners, and keep an archive directory. More than 15 tasks, multiple workstreams, or active dependencies are signals to add structure rather than to make one flat list.

## Starting and capturing work

- Ask for a one-sentence description, a deadline or “no deadline,” and the next physical action.
- Create the project README from those answers. Tasks are concrete actions: “Research options” is actionable; “figure out renovation” is not.
- Estimate size only when useful (small/medium/large or hours). For client work, record deadlines, contacts, rates when applicable, deliverables, and material approvals.

## WIP and Someday

- Suggest no more than three to five active projects. Distinguish this week's active work from intentionally parked work.
- Put parked projects in `$STATE_ROOT/_someday/`; review them quarterly to activate, archive, or remove with confirmation.
- A long Someday list is a valid holding pen. Do not guilt the user for “this would be cool, but not now.”

## Review, completion, and metrics

- In a weekly review, ask what progressed, identify the next action for each active project, flag projects with no completion for two or more weeks, and reconsider Someday items.
- For a stalled project, ask whether it remains a priority. The user may push it forward, park it, or end it; ending zombie projects is healthy.
- Define a done checklist in the README. When complete, review what worked, archive to `$STATE_ROOT/_archive/<year>/`, and acknowledge completion before moving on.
- Track duration or completion rate only when the user finds it useful; never turn personal project work into compulsive measurement.

## Guardrails and integration

- Do not recommend a complex project-management application until local files fail, impose a rigid methodology, propose Gantt charts for ordinary personal projects, or require time tracking for non-billable work.
- Coordinate explicit requests with calendars for deadlines, contacts for collaborators, invoices for client billing, and goals for higher-level outcomes. The related skill remains the owner of its own state.
