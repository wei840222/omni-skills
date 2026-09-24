# Prompts and context

Match prompt length to uncertainty. A familiar one-file edit needs one or two sentences. A new area needs a file pointer plus the expected check. An architecture choice starts in discussion, not in a patch.

## Visual tasks

When the change is on screen, attach a screenshot instead of describing coordinates. On macOS, Cmd-Shift-4 captures a region; drag the image into the CLI. Ask the agent to match the visible string or element to a file. Skip the screenshot when the task is already a named file and a named function.

## Discussion before edits

Use a plan prompt when the radius is medium or larger:

```text
List two approaches and the files each would touch. Wait for a choice before editing.
```

Queue the next related prompt only after the current one has a path lock. Example: finish the endpoint, then add the loading state, then update the error copy.

## Steering

If output drifts:

1. Pause generation.
2. Send the corrected path and the check that must pass.
3. Continue from the corrected scope.

Interrupt early. Waiting for a finished wrong diff costs more than a pause.

## What to put in agent instructions

Keep `AGENTS.md` or `CLAUDE.md` to scar tissue: validation library, error shape, test location, and the CLI for logs or the database. Point at `src/api/README.md` instead of pasting the API into the prompt.

Leave out instructions the model already follows and any secret value. A connection example belongs in the repo's ignored env sample, not in the skill.

## Session length

| Situation | Action |
|---|---|
| New feature, no relevant history | Fresh session |
| Next iteration on the same change | Continue |
| Context is long and the next task is unrelated | Summarize the decisions, then start fresh |
| Same bug, history still useful | Continue |

Claude Code's context guidance treats a long or irrelevant thread as a reason to summarize and reset, not as a reason to restart every successful session. https://code.claude.com/docs/en/best-practices

## When the agent stalls

Ask it to read the related files, state two hypotheses, and name the check that would distinguish them. That is a deeper pass on the same task, not a new feature.
