# Setup - Kanban

Read this when `<state_root>` does not exist, is empty, or the current project has no registered board.

## Operating Attitude

- Keep the experience lightweight: answer immediate user needs while building structure in parallel.
- Favor continuity: every decision should make the next session easier for any agent.
- Be explicit about scope: project-local board or shared home board.

## Priority Order

### 1. Integration First

In the first natural exchanges, confirm when this system should activate:
- Always when task planning appears
- Only when user explicitly asks for Kanban
- Only for selected projects

After the user confirms persistent state, save this behavior in `<state_root>/memory.md`.

### 2. Route Each Project Once

For each project, resolve and store:
- Project id (stable slug)
- Workspace root (if available)
- Preferred board mode: `workspace-local` or `home-shared`
- Primary board path
- Aliases users might use in chat

After the user confirms the board location and write, record this registry entry in `<state_root>/index.md`.

### 3. Initialize the Board Skeleton

For a confirmed `home-shared` board, create only the required files under `<state_root>/projects/{project-id}/` using `assets/kanban-data-templates.md`:
- `<state_root>/projects/{project-id}/board.md`
- `<state_root>/projects/{project-id}/rules.md`
- `<state_root>/projects/{project-id}/log.md`

For confirmed `workspace-local` mode, use the host-supplied `<workspace>/.kanban/` path and create only its `board.md`, `rules.md`, and `log.md` files. Record the project-local paths in `<state_root>/index.md`; never infer `<workspace>` from the shell working directory.

If the user already has a preferred structure, preserve it and only add missing core fields.

### 4. Start with Real Work

After the user confirms board creation, capture the first actionable tasks:
- Add backlog cards
- Assign initial priority and owner
- Move at least one card to ready or in progress if clear

## What You Save Internally

- `<state_root>/memory.md`: integration preference, defaults, and operating notes
- `<state_root>/index.md`: per-project routing table and last-used timestamps
- `<state_root>/projects/{project-id}/` or the confirmed `<workspace>/.kanban/`: board state and write log

## Guardrails

- Ensure to claim setup completion only if files were created.
- Obtain explicit user approval before overwriting existing boards.
- If routing is unclear, ask one direct question, then continue.
