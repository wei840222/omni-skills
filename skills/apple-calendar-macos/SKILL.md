---
name: apple-calendar-macos
description: >
  Manage macOS Calendar events locally (iCloud, Google, Exchange, CalDAV) via
  CLI. Triggers on requests to lookup, create, update, or delete calendar
  events on macOS without requiring external API keys.
metadata:
  openclaw: '{"emoji": "📅"}'
  related-skills: '{"macos": "Apply macOS-specific system administration, BSD/GNU CLI traps, Homebrew path differences, Keychain secrets, launchd agents, TCC privacy permissions, and automation with defaults/osascript", "schedule": "Program recurring or one-time jobs the user defines, persist them under portable state, and fire them at the right local time"}'
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

This skill manages persistent operational state.

**Candidate locations (in order of preference):**
1. `<state_root>/memory.md` (Status, defaults, and confirmation behavior)
2. `<state_root>/command-paths.md` (Detected CLI path and fallback status)
3. `<state_root>/timezone-defaults.md` (Preferred timezone and date style)
4. `<state_root>/safety-log.md` (Deletions, bulk edits, and rollback notes)

Before modifying state, ask for explicit confirmation and verify the target path exists.
