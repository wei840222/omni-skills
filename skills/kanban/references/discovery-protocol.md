# Discovery Protocol - Kanban

Run this sequence at the start of each conversation before touching tasks.

## Step 1: Detect Context

Collect available signals:
- current workspace root
- explicit project name in user message
- aliases in user message

## Step 2: Resolve Project Entry

Search `<state_root>/index.md` in this order:
1. exact workspace root match
2. alias match
3. explicit project id match
4. most recent project (`last_used`) with one confirmation question

If no entry matches, propose the project identifier and board mode, then obtain confirmation before creating an index entry or board files.

## Step 3: Resolve Board Path

Use `board_mode` from the resolved entry:
- `workspace-local` -> `{workspace}/.kanban/board.md`
- `home-shared` -> `<state_root>/projects/{project-id}/board.md`

If the board file is missing, show the resolved path and create it from `assets/kanban-data-templates.md` only after the user confirms the persistent write.

## Step 4: Load and Validate

Validate the board has:
- `Meta`
- `Lanes`
- `Cards` table

If malformed, report the missing sections and obtain confirmation before a non-destructive repair:
- keep existing content
- restore missing required sections
- write a repair note to the resolved board log (`<state_root>/projects/{project-id}/log.md` for `home-shared`, or the confirmed `<workspace>/.kanban/log.md` for `workspace-local`)

## Step 5: Confirm Scope for Multi-Project Requests

If the user request spans multiple projects:
- list candidate projects
- ask which boards should be updated
- apply changes one project at a time

## Step 6: Update Registry

After every successful write:
- update `last_used` in `<state_root>/index.md`
- update `last` in `<state_root>/memory.md`
- append the action to the resolved project log
