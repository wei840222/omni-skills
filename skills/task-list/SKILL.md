---
name: task-list
description: Capture, clarify, organize, and review a conversational task list with stable views, projects, recurrence, and waiting work. Use when the user wants to add, update, prioritize, defer, or review tasks; not for calendar-service automation or broad productivity diagnosis.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📋"}'
  related-skills: "{\"assistant\":\"Coordinates broader chief-of-staff work that may include tasks, messages, and follow-through.\",\"daily-planner\":\"Turns a selected task list into a realistic day plan with focus blocks.\",\"memory\":\"Maintains broader durable context outside the task-list state root.\",\"plan\":\"Builds a structured initiative plan when a task expands beyond list management.\",\"projects\":\"Provides deeper project tracking when task-list project records are insufficient.\"}"
---

## State location

Task-list state may exist in `<workspace>/task-list/`, `<workspace>/memory/task-list/`, or `~/task-list/`.

Resolve `<state_root>` before the first state operation in an invocation:

1. Use an explicit user- or host-configured state path when available.
2. Otherwise use the first existing directory in this order: `<workspace>/task-list/`, `<workspace>/memory/task-list/`, `~/task-list/`.
3. When several candidates exist, use the highest-precedence directory, report the split state, and leave other candidates unchanged.
4. When no candidate exists and the user requests persistent task-list state, create `<workspace>/task-list/`.

When the host cannot identify `<workspace>`, use an existing `~/task-list/`; otherwise request a state location before creating notes. Use the selected `<state_root>` consistently for the rest of the invocation.

## Workflow

1. Handle the user’s immediate request first. For a raw capture, create an Inbox item without requiring metadata.
2. Clarify only information that changes execution: next action, due versus start date, recurrence anchor, project boundary, or waiting owner.
3. Keep projects (finite outcomes), areas (ongoing responsibilities), and waiting work as distinct records.
4. Apply the deterministic view rules before listing tasks. Today is a focused working set, not an archive of overdue work.
5. Treat an explicit request to add or update a named task as consent for that non-destructive edit. Confirm deletion, completion, recurrence changes, rescheduling, and bulk moves before writing.
6. State exactly what changed after each state update. Load `references/state-guide.md` before creating, migrating, or maintaining persistent files.

## Reference routing

- Read `references/capture.md` for brain dumps, title rewrites, or uncertainty about which fields to ask for.
- Read `references/views.md` before presenting Inbox, Today, Upcoming, Anytime, Someday, or Waiting.
- Read `references/recurrence-and-waiting.md` for dates, snoozes, recurring tasks, blocked work, or follow-up dates.
- Read `references/reviews.md` for daily triage, weekly reset, stale tasks, or overload.
- Read `references/state-guide.md` for first-time setup, persistent storage, migration, or file updates; copy formats from `assets/task-file-templates.md` only when creating the corresponding state file.
- Read `references/knowledge-sources.md` only when auditing date and recurrence semantics or explaining their interoperability limits.

## Boundaries

Use `daily-planner` after the user has selected work to schedule. Use `plan` or `projects` when a request needs initiative-level planning rather than task-list maintenance. Keep secrets, private third-party notes, and unrelated durable history out of `<state_root>`.
