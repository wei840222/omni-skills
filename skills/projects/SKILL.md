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

## Core Behavior
- User mentions a project → help define scope, create folder in `$STATE_ROOT/$PROJECT_NAME/`
- User adds tasks → capture in project context
- Regular review prompts → surface stalled projects
- Everything this skill reads or writes is a plain local note. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; a row another skill wrote is read, never rewritten and never deleted, and every write and deletion is named in one line as it happens.

## References
- When managing project life cycles, reading or creating templates, load `references/structure.md`.
- When starting, reviewing, capturing tasks, or finishing a project, load `references/workflow.md`.
