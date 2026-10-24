---
name: apple-calendar-macos
description: >
  Manage macOS Calendar events locally (iCloud, Google, Exchange, CalDAV) via
  CLI. Triggers on requests to lookup, create, update, or delete calendar
  events on macOS without requiring external API keys.
metadata:
  openclaw: '{"emoji": "📅"}'
  related-skills: '{"macos": "Apply system administration, BSD CLI tools, and launchd scheduling.", "schedule": "Schedule and manage recurring jobs and calendar-triggered alerts."}'
---
## When to Use

User wants to manage events from the macOS Calendar stack where Google, iCloud, Exchange, and CalDAV accounts are already synced locally.
Agent handles lookup, create, update, delete, conflict checks, and post-write verification without provider OAuth setup.

## Requirements

- macOS with Calendar app access enabled for terminal tools.
- At least one working command path: `apple-calendar-cli`, `icalBuddy`, `shortcuts`, or `osascript`.
- User confirmation before destructive operations.
- Provider accounts should already be connected in Calendar.app; this skill does not run provider OAuth.

## Architecture

To reduce working memory load, read specific reference documents only when their context is needed:

| When to load | File |
|-------|------|
| **Setup & Architecture** | |
| Setup and first-run behavior | `references/setup.md` |
| Memory structure | `references/memory-template.md` |
| Command path matrix | `references/command-paths.md` |
| **Operations** | |
| Safety checklist before writes | `references/safety-checklist.md` |
| Calendar operation patterns | `references/operation-patterns.md` |
| Troubleshooting and recovery | `references/troubleshooting.md` |
| **Guidelines** | |
| Rules for execution | `references/core-rules.md` |
| Anti-patterns and mistakes | `references/common-traps.md` |
| Privacy and security details | `references/security-and-privacy.md` |

## State location

Apple Calendar Macos state may exist in `<workspace>/apple-calendar-macos/`, `<workspace>/memory/apple-calendar-macos/`, or `~/apple-calendar-macos/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/apple-calendar-macos/`, `<workspace>/memory/apple-calendar-macos/`, `~/apple-calendar-macos/`.
3. If none exists and state must be created, default to `<workspace>/apple-calendar-macos/`.

Use the selected `<state_root>` for every state operation in this skill.

State files managed:
- `<state_root>/memory.md` (Status, defaults, and confirmation behavior)
- `<state_root>/command-paths.md` (Detected CLI path and fallback status)
- `<state_root>/timezone-defaults.md` (Preferred timezone and date style)
- `<state_root>/safety-log.md` (Deletions, bulk edits, and rollback notes)

Before modifying state, ask for explicit confirmation and verify the target path exists.
