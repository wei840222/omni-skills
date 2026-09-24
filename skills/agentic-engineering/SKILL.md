---
name: agentic-engineering
description: >
  Coordinate work with CLI coding agents using blast-radius sizing, parallel
  terminals, and atomic commits. Use when the user is driving Claude Code,
  Codex CLI, or a similar coding agent and asks how to split, steer, or recover
  that work. Not for building an agent runtime, MCP server, or orchestration
  framework.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🤖","requires":{"bins":["git"]}}'
  related-skills: '{"agentic-coding":"Apply coding-loop tactics once a single agent task is already scoped.","git":"Inspect history, commits, and recovery commands when agents share one working tree."}'
---

## When to load

Load this skill when the user is already working with a CLI coding agent and wants to split, steer, or recover that work. Load `references/sources.md` before repeating a vendor limit, pricing figure, or product recommendation. Load one workflow reference for the task at hand:

- `references/blast-radius.md` before estimating how many files a prompt will touch.
- `references/parallel.md` when more than one agent will run at once.
- `references/context.md` when writing or steering a prompt.
- `references/tools.md` when choosing a CLI, terminal, or review tool.

## State location

This skill does not persist notes. If the user wants a reusable local playbook, resolve `<state_root>` before the first write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/agentic-engineering/`, `<workspace>/memory/agentic-engineering/`.
3. If more than one exists, use only the highest-precedence directory and tell the user the other copies exist.
4. If none exists and the user wants the playbook saved, create `<workspace>/agentic-engineering/`.
5. If `<workspace>` cannot be resolved, ask for a state root before creating files.

Use that `<state_root>` for every later state operation in this invocation. Keep agent transcripts, credentials, and repository secrets out of it.

## Workflow

1. Name the task: size a change, run agents in parallel, write a prompt, pick a tool, or recover a conflict.
2. Estimate blast radius before launching extra agents. See `references/blast-radius.md`.
3. Give each agent a non-overlapping path and one commit per logical change. See `references/parallel.md`.
4. Keep the prompt short, point at files, and interrupt when the work drifts. See `references/context.md`.
5. Prefer a CLI the agent already knows. Record the choice in the repo's agent instructions, not in a new framework. See `references/tools.md`.

## Core rules

- Size first. A one-file change can run beside other work. A migration, auth rewrite, or shared-file edit gets one agent and a plan before edits.
- Same checkout is the default. Use a Git worktree when the user needs an isolated branch or a long-running experiment, not as the default for every prompt.
- Each agent commits only files it edited, after one logical change, with a message that names that change.
- Spend a slice of the session on duplication, dead code, and tests, still through the same blast-radius check.
- Put tool preferences in one line of `AGENTS.md` or `CLAUDE.md`, for example `logs: use the vercel CLI`.
- Attach a screenshot when the task is visual. Point at the file when it is not.
- Pause a drifting agent, ask for status, then choose help, redirect, or abort. A pause is cheaper than unwinding a wide diff.

## Recovery

When two agents edit the same checkout:

1. Pause the writers.
2. Read `git status` and `git diff` before any reset.
3. Keep the user's uncommitted work. Stash only after naming what will be saved.
4. Reset only to a commit the user confirms. Then reapply the stash and resolve the overlap.

Commands and the confirmation gate are in `references/parallel.md`.

## Scope

This skill coaches the person driving coding agents. It does not implement an agent, call external systems, or edit files outside the task the user just named. Building a runtime, MCP server, or orchestration framework is a separate product task, not a step in this workflow.
