---
name: notion-calendar
description: Manage Notion databases as date-aware calendars. Use for schema discovery, time-window queries, page creation, and rescheduling.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"N","requires":{"env":["NOTION_API_KEY"]}}'
  related-skills: '{"api":"Use for general REST auth, pagination, and HTTP error patterns when a Notion call fails outside this calendar workflow.","dates":"Use for date math and timezone ranges before writing a Notion date property.","pkm":"Use when the task is broader workspace organization rather than a dated database view.","productivity":"Use when dated Notion rows need to feed a task or execution system.","schedule":"Use when a request becomes multi-step planning beyond one Notion calendar window."}'
---

## When to load

Load this skill when the user wants a Notion database treated as a calendar, editorial plan, launch schedule, content calendar, or dated task board. Handle schema discovery, time-window queries, page creation, rescheduling, and status updates for pages that appear in those views.

## State location

Calendar memory may exist in `<workspace>/notion-calendar/`, `<workspace>/memory/notion-calendar/`, or `~/notion-calendar/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/notion-calendar/`, `<workspace>/memory/notion-calendar/`, `~/notion-calendar/`.
3. If more than one exists, use only the highest-precedence directory and tell the user that other copies were found. Do not merge them.
4. If none exists and the user wants memory saved, create `<workspace>/notion-calendar/`.
5. If `<workspace>` cannot be resolved and `~/notion-calendar/` is also missing, ask for a state root before creating files.

Use that `<state_root>` for every state operation in this invocation. A legacy `~/Clawic/data/notion-calendar/` tree is a migration source only; copy it only after the user asks, then leave the original in place.

## Requirements

- `NOTION_API_KEY` for official API access. Keep the token in the host environment, never in skill memory.
- A Notion integration shared with the target database. An unshared database returns 404, not a useful empty list.
- Optional community CLI: `notion` from FroeMic/notion-cli for quick search and CRUD on the older `2022-06-28` shape.

## Architecture

After `<state_root>` is resolved, local memory uses this tree. See `assets/memory-template.md` for the file shape.

```text
<state_root>/
|-- memory.md        # Status, timezone defaults, and workspace context
|-- calendars.md     # Database and data source IDs plus property mappings
|-- templates.md     # Reusable page payload patterns
`-- safety-log.md    # Ambiguous matches, destructive confirmations, and rollbacks
```

| Path | Role | Creation condition |
|------|------|--------------------|
| `<state_root>/memory.md` | Status, timezone, write policy | First time the user wants defaults to persist |
| `<state_root>/calendars.md` | Verified IDs and property names | After a database mapping is confirmed |
| `<state_root>/templates.md` | Reusable payloads | When the user asks to reuse a page shape |
| `<state_root>/safety-log.md` | Ambiguous matches and confirmed destructive actions | When a match is ambiguous or a destructive change is confirmed |

Create a child only when that feature is needed. Do not pre-create empty files.

## Quick Reference

Load only the file the current step needs:

| Topic | File |
|-------|------|
| Setup and first-run behavior | `references/setup.md` |
| Memory structure | `assets/memory-template.md` |
| Calendar source mapping | `references/calendars.md` |
| Reusable payload templates | `assets/templates.md` |
| Optional CLI patterns | `references/cli-patterns.md` |
| Calendar database schema guidance | `references/calendar-schema.md` |
| Query, create, and reschedule flows | `references/query-playbook.md` |
| Common failures and fixes | `references/troubleshooting.md` |
| Core rules, endpoints, and security | `references/rules.md` |
