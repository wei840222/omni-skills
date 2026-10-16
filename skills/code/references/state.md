# State tracking guidance

Reference for tracking multiple tasks or requests.

## Request tracking

Label each user request:

```
[R1] Build login page
[R2] Add dark mode
[R3] Fix header alignment
```

Track state for user visibility:

```
[R1] [DONE] Done
[R2] [WIP] In progress (awaiting user approval for step 2)
[R3] [Q] Queued
```

## Managing multiple requests

When the user sends a new request while another is in progress:

1. Acknowledge: "Got it, I'll add this to the queue"
2. Show the updated queue to the user
3. Ask whether priority should change

## Handling interruptions

| Situation | Suggested action |
|-----------|------------------|
| New unrelated request | Add to queue, ask user priority |
| Request affects current work | Pause, explain impact, ask how to proceed |
| User requests to halt or wait | Pause operations and await instructions |
| User changes requirements | Summarize impact, ask the user to confirm |

## User decisions

Always ask the user before:

- Starting work on queued items
- Changing priority order
- Rolling back completed work
- Modifying the plan

## Progress file (optional)

The user may request a state file under the resolved `<state_root>`:

```markdown
## In Progress
[R2] Dark mode - Step 2/4 (awaiting user approval)

## Queued
[R3] Header fix

## Done
[R1] Login page [DONE]
```

Update only when the user requests or approves changes.
