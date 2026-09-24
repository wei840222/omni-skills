# Parallel agents

Use more than one agent only after blast radius shows each task has an exclusive path.

## How many

| Work | Agents | Why |
|---|---|---|
| Focused feature or migration | 1 | Shared files, needs steering |
| Independent refactor | 2–4 | Separate directories |
| UI polish, tests, or docs | up to 4–6 | Small isolated edits |

A visible terminal grid helps the user steer. The grid is a habit, not a product requirement. Ghostty, iTerm2, and tmux are examples when the user asks for a terminal.

## Path split

```text
Agent 1: src/api/
Agent 2: src/components/
Agent 3: tests/
Agent 4: docs/
```

If two tasks must edit the same file, run them in sequence. Same-folder work is the default. Add a Git worktree when the user needs an isolated branch or a long-running experiment: https://git-scm.com/docs/git-worktree

## Commits

Tell each agent:

- Commit after one logical change.
- Commit only files that agent edited.
- Name the change in the message.
- Leave other agents' dirty files unstaged.

GitHub's commit guidance is the checkpoint: one logical change, one message. https://docs.github.com/en/pull-requests/reference/commits

## While one agent runs

Check another agent's diff, start a non-overlapping task, or prepare the next prompt. Waiting with no next action is the idle case this workflow is meant to avoid.

## Conflict recovery

Pause the writers first. Then:

```bash
git status
git diff
git stash push -u -m "agent overlap before reset"
git log --oneline -5
```

Reset only after the user names the commit to keep:

```bash
git reset --hard <confirmed-sha>
git stash pop
```

A hard reset without that confirmation drops uncommitted work. Small commits make the confirmed SHA easy to find.
