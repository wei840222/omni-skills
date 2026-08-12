---
name: kanban
description: Create, update, and manage multi-project Kanban boards with deterministic rules, persistent routing, and consistent task processing across sessions. Use when the user wants to organize tasks visually, manage project queues, or track status of ongoing work.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📋"}'
  related-skills: '{"daily-planner":"Incorporates Kanban tasks into daily planning and time block execution.","delegate":"Handles owner assignment and task handoff protocols for items on the board.","projects":"Manages cross-project governance that feeds into specific Kanban boards.","workflow":"Provides operational workflow design and execution loops connected to Kanban tasks."}'
---

## State location

Kanban state may exist in `<workspace>/kanban/`, `<workspace>/memory/kanban/`, or `~/kanban/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/kanban/`, `<workspace>/memory/kanban/`, `~/kanban/`.
3. If none exists and state must be created, default to `<workspace>/kanban/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

If `<state_root>` does not exist or is empty, read `references/setup.md` silently and initialize only after user confirmation.

## Architecture

Memory lives in `<state_root>`. See `references/memory.md` for base files, `assets/kanban-data-templates.md` for board structure templates, and `references/discovery-protocol.md` for project routing.

```
<state_root>/
├── memory.md                  # Global status, integration, defaults
├── index.md                   # Project registry and board location map
└── projects/
    └── {project-id}/
        ├── board.md           # Active board for this project
        ├── rules.md           # Project-specific lane and policy definitions
        ├── log.md             # Board write log
        └── archive/
```

Optional project-local mode:

```
{workspace}/.kanban/
├── board.md
├── rules.md
└── log.md
```

## Quick Reference

Use the smallest relevant file for the current task.

| Topic | File |
|-------|------|
| Setup behavior | `references/setup.md` |
| Memory and registry structure | `references/memory.md` |
| Board schema and templates | `assets/kanban-data-templates.md` |
| Where to find each project board | `references/discovery-protocol.md` |
| How to process and update cards | `references/processing-rules.md` |

## Core Rules

### 1. Resolve Project Context Before Reading or Writing
- Run the discovery sequence in `references/discovery-protocol.md` at the start of each conversation.
- If project scope is ambiguous, ask once before writing.

### 2. Persist Routing So Any Agent Can Continue
- Keep the Kanban index file updated with workspace path, project aliases, and primary board path.
- After each successful write, update `last_used` for the project entry.

### 3. Allow Custom Board Shapes with a Stable Core Schema
- Users can rename lanes or add custom columns per project in the project rules file.
- Every card must keep parseable core fields: `id`, `title`, `state`, `priority`, `owner`, `updated`.

### 4. Process Cards Deterministically
- Follow the exact decision order in `references/processing-rules.md` for prioritization and movement.
- Ensure blockers, dependencies, and explicit WIP limits are respected.

### 5. Keep Writes Atomic and Logged
- Update the board file and append one line to the project log in the same operation cycle.
- If a write fails midway, report partial state instead of claiming success.

### 6. Keep Project Boards Isolated
- Move or edit cards across different project boards only with explicit user intent.
- For cross-project requests, produce a plan first, then apply updates per board.

### 7. Preserve Continuity Across Conversations
- On first message of a new conversation, resolve board location and load current state before proposing work.
- If no board exists, initialize from `assets/kanban-data-templates.md`, register it in the index file, and continue.

## Common Traps

- Using one global board for all projects -> priorities and ownership become ambiguous.
- Renaming lanes without updating state mapping in the project rules file -> cards become unprocessable.
- Writing board updates without refreshing the index file -> next agent session cannot locate the board.
- Keeping tasks without IDs -> duplicate card updates and broken references.
- Marking work as done without log entry -> no audit trail for later sessions.

## Security & Privacy

**Data that stays local:**
- Board files and project registry in `<state_root>` or `{workspace}/.kanban/`.

**Data that leaves your machine:**
- None by default.

**This skill ensures to:**
- Avoid undeclared network requests.
- Restrict file modifications to the selected Kanban scope.
- Maintain board history accurately when logs are missing, rather than fabricating entries.
