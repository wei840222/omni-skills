---
name: chat-rooom
description: Coordinate multiple AI agents through local, file-backed chat rooms with channels, mentions, task claims, and durable summaries. Use when work needs explicit ownership, auditable handoffs, or lightweight multi-agent collaboration in one workspace.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💭"}'
---

## Start here

1. Choose a room name for one objective, incident, or milestone.
2. Create the minimal room structure with `references/operations.md`.
3. Record the first owner, current status, and next action in `summary.md`.

## Setup

Before using persistent room preferences, resolve `<state_root>` to a user-approved, writable directory outside the skill package (for example, `<workspace>/.state/chat-rooom`). If it is missing or empty, read `references/setup.md`. Default to local-first coordination and keep persistence light until the user confirms they want a durable room workflow.

## When to Use

Use this skill when multiple agents need to coordinate, debate, claim work, share evidence, or hand off a task without copying terminal output. Use local channels, mentions, lightweight ownership, and an auditable shared log in the current workspace.

## Architecture

Skill memory lives in `<state_root>/`. Active rooms live in the current workspace at `.chat-rooom/`. See `references/memory-template.md` for both templates.

```text
<state_root>/
|- memory.md       # Activation defaults and durable preferences
|- rooms.md        # Recent room names, roles, and conventions
`- patterns.md     # Coordination patterns that repeatedly worked well

<workspace>/.chat-rooom/
`- rooms/<room>/
   |- room.md              # Purpose, roster, channels, status
   |- summary.md           # Snapshot, decisions, next actions
   |- jobs.md              # Work items with owner and state
   |- claims.md            # File, task, or test ownership
   |- channels/general.md  # Shared timeline
   |- channels/review.md   # Critique and approval requests
   `- inbox/<agent>.md     # Pending mentions and directed asks
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | When setting up the skill state for the first time |
| Agent communication | `references/agent-communication.md` | When deciding how agents should exchange messages |
| Memory template | `references/memory-template.md` | When initializing or updating state structures |
| Room protocol | `references/protocol.md` | When participating in a room to follow standard layout and message format |
| Daily operations | `references/operations.md` | When opening, joining, writing to, or closing a room |
| Example room patterns | `references/patterns.md` | When planning coordination structures for a new task |

## Core Rules

### 1. Start Coordination Inside a Named Room
- Create or join one named room before multi-agent work starts.
- Keep one room per objective, incident, or milestone so decisions stay discoverable.
- Centralize all coordination within the named room to maintain a single source of truth.

### 2. Make Every Message Addressable
- Each message should carry one primary intent: ask, update, proposal, decision, block, or handoff.
- Use `@agent` mentions for directed work. Use `@all` only for blocking context changes or final checkpoints.
- Link exact paths, commands, or commits instead of pasting large blobs that bury the action item.

### 3. Claim Shared Surfaces Before Editing Them
- Update the claims table before touching the same file, test target, or subtask as another agent.
- Claim the smallest useful surface to reduce idle waiting.
- Refresh or release stale claims when work is done, blocked, or handed off.

### 4. Read the Summary First and Repair It Often
- On join, read the room summary before scrolling the whole channel history.
- When a thread pauses, update summary with status, decisions, open questions, and next owner.
- If summary and channel history diverge, trust the newer timestamp and fix the summary immediately.

### 5. Separate Channels by Intent
- Keep `general` for status, `review` for critique, `build` for execution details, and `incident` for live recovery.
- Create a new channel when one topic would bury another.
- Once a task becomes active, separate debate and execution into distinct channels.

### 6. Keep the Room Local and Auditable
- Prefer workspace files and local tools over a hosted chat backend unless the user explicitly asks for one.
- Treat the room as a shared operational log, not private memory.
- Keep secrets, tokens, and unrelated personal data out of room files.

## Recovery patterns

- If the objective or roster is unclear, add both to `room.md` before assigning work.
- If an update buries its action item, replace it with a short directed `ask` or `handoff` block.
- If two agents need the same surface, record the smallest claim and split or sequence the work.
- If a room pauses, refresh `summary.md` and `jobs.md` so the next agent can resume from the snapshot.
- If routine traffic is noisy, address the responsible agent instead of broadcasting with `@all`.

## Security & Privacy

**Data that leaves your machine:**
- None from this skill itself

**Data that stays local:**
- Room logs and defaults in `<state_root>/` and `.chat-rooom/` inside the active workspace

**This skill does not:**
- Require a hosted backend
- Access undeclared folders outside the active workspace and `<state_root>/`
- Store credentials or secrets in room logs

## Scope

This skill ONLY:
- Sets up local chatroom coordination patterns for multiple agents
- Keeps channels, claims, jobs, and summaries consistent
- Helps agents talk through room files instead of terminal copy-paste

This skill does not replace version control or formal code review. It records local coordination and does not promise real-time transport.

## Related Skills
No related skills are required for this package.

## State location
This skill relies on local persistent state.
1. Primary: `<state_root>/`
2. Secondary: If not configured, prompt the user for a workspace location.
