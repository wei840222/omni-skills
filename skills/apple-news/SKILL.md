---
name: apple-news
description: Launch Apple News, open Apple News article links, and run user-owned News Shortcuts on macOS. Use when the user asks to open News.app, read an `apple.news` link, or use a configured Apple News Shortcut.
compatibility: Requires macOS with News.app and the `open` command. Shortcut workflows additionally require the `shortcuts` command and a user-owned Shortcut.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📰","os":["darwin"],"requires":{"bins":["open"]}}'
  related-skills: '{"macos":"Provides macOS command workflows and automation patterns.","news":"Provides general news workflows and monitoring patterns.","productivity":"Provides frameworks for daily information intake.","reading":"Provides reading-queue and prioritization workflows.","travel":"Provides location and destination context for news."}'
---

## State location

Apple News state may exist in `<workspace>/apple-news/`, `<workspace>/memory/apple-news/`, or `~/apple-news/`. Before reading or writing state:

1. Use an explicitly configured state path when the user or host supplies one.
2. Otherwise, select the first existing directory in this order: `<workspace>/apple-news/`, `<workspace>/memory/apple-news/`, then `~/apple-news/`.
3. When more than one candidate exists, use only the highest-precedence directory and tell the user that separate copies exist.
4. When none exists and the user wants saved preferences, describe the proposed write, obtain confirmation, then create `<workspace>/apple-news/`.
5. Keep the resolved `<state_root>` fixed for the invocation and use it for every state operation.

## Workflow

1. Confirm whether the user wants to launch News.app, open one Apple News link, open several links, or run a Shortcut.
2. Read `references/command-paths.md` before the first command in an invocation.
3. Read `references/operation-patterns.md` for the matching operation. Read `references/safety-checklist.md` before any Shortcut or multi-link action.
4. Execute only the confirmed action. Use `assets/memory-template.md` when creating `<state_root>/memory.md` after confirmation.
5. Observe the command result, report the outcome, and use `references/troubleshooting.md` when the selected path fails.

## Requirements

- macOS with News.app present at `/System/Applications/News.app`.
- `open` for launching News.app or handing an Apple News URL to the registered handler.
- A user-owned Shortcut for topic search or automation; inspect it and confirm its side effects before execution.
- Apple News article or feed URLs use `https://apple.news/...`.

## Resource map

| Topic | File | Load when |
|---|---|---|
| Apple News facts and sources | `references/domain-knowledge.md` | Checking product scope or regional availability. |
| Command selection and probes | `references/command-paths.md` | Before the first launch or link command. |
| Operation flows | `references/operation-patterns.md` | Launching News.app, opening links, searching, or handling failure. |
| Safety controls | `references/safety-checklist.md` | Opening multiple links or running a Shortcut. |
| Recovery | `references/troubleshooting.md` | A command, URL, or Shortcut fails. |
| Setup preferences | `references/setup.md` | Initializing saved preferences. |
| Core constraints | `references/core-rules.md` | Checking behavioral or privacy boundaries. |
| Common mistakes | `references/common-traps.md` | Diagnosing an unexpected result. |
| Persistent preference template | `assets/memory-template.md` | Creating or updating `<state_root>/memory.md`. |

## Data and external effects

Persist only reusable command preferences, approved safety defaults, and proven recovery notes in `<state_root>`. Before a persistent write, describe the file and content scope and obtain confirmation.

Launching News.app, opening an `https://apple.news/...` URL, and running a Shortcut are external actions. Preview the exact URL or Shortcut name first. A Shortcut can contact services defined by its owner; confirm its expected side effects before running it.

For more than one link, present the link count and exact targets, then obtain two explicit confirmations before opening them.
