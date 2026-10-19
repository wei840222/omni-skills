# Memory Template - ChatGPT

Create `<state_root>/memory.md` with this structure only after `<state_root>` is
resolved. Do not treat the literal string `<state_root>` as a filesystem path.

```markdown
# ChatGPT Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending

## Workflow Defaults
<!-- Preferred surfaces: standard chat, Temporary Chat, Projects, GPTs/plugins -->
<!-- Preferred prompt packet size, draft depth, and revision style -->

## Privacy Boundaries
<!-- Data categories that should exclude remembered chats or uploads -->
<!-- Rules for when to prefer Temporary Chat (Personalized vs Unpersonalized) -->

## Active Patterns
<!-- Prompt packet shapes, QA checklists, and pass order that work repeatedly -->
<!-- Durable custom instruction patterns that are actually helpful -->

## Failure Modes
<!-- Repeated problems: too generic, ignores constraints, stale context, hallucinations -->
<!-- Best fixes that worked -->

## Notes
<!-- Stable observations worth reusing -->

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Default learning state | Keep refining ChatGPT workflow defaults from active use |
| `complete` | Stable workflow established | Reuse defaults unless the user changes them |
| `paused` | User wants fewer setup questions | Ask only when a critical ChatGPT choice is missing |
| `skip_asking` | User rejected setup prompts | Stop prompting and work from the task only |

## Integration values

| Value | Meaning |
|-------|---------|
| `pending` | Activation preference not confirmed |
| `done` | Activation preference confirmed |
| `declined` | User wants manual activation only |

## Optional sibling files

Create only when needed:

| Path | Purpose |
|------|---------|
| `<state_root>/workflows.md` | Reusable prompt packet patterns |
| `<state_root>/projects.md` | Active project briefs and decision logs |
| `<state_root>/gpts.md` | GPT / plugin roles and limitations |
| `<state_root>/qa.md` | Recurring output failures and fixes |

## Key principles

- Store only patterns that improve future ChatGPT sessions.
- Keep notes operational and short.
- Save workflow boundaries, not raw user content.
- Update `last` whenever memory changes.
- Never write these files into the skill package tree.
