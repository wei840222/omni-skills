---
name: apple-mail-macos
description: Use local CLI to manage Gmail, Outlook, iCloud, Yahoo, Fastmail, and other mail accounts synced in Apple Mail on macOS, without APIs or OAuth.
metadata:
  openclaw: '{"emoji": "\u2709\ufe0f", "requires": {"bins": null, "anyBins": ["osascript", "shortcuts", "sqlite3"], "config": ["<state_root>/"]}}'
  related-skills: '{"events": "skills/events", "macos": "skills/macos", "mail": "skills/mail", "productivity": "skills/productivity", "schedule": "skills/schedule"}'
license: MIT
---
## Setup

On first use, follow `references/setup.md` to define provider scope, command path preferences, and safety defaults before any write action.

## When to Use

User wants to control Apple Mail from CLI while keeping account sync managed by Mail.app.
Agent handles read, search, triage, draft, send, move, archive, and delete workflows across accounts already connected in Apple Mail.

## Requirements

- macOS with Mail.app account access enabled for terminal automation.
- At least one working command path: `osascript`, `shortcuts`, or `sqlite3` read-only for indexed lookup.
- Provider accounts already connected in Mail.app (Gmail, Outlook, iCloud, Yahoo, Fastmail, and Proton via Bridge if used).
- Explicit confirmation before sending, deleting, or bulk actions.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure.

```text
<state_root>/
├── memory.md               # Status, provider map, safety defaults
├── command-paths.md        # Working command path and fallback notes
├── provider-coverage.md    # Provider-specific behavior and caveats
├── safety-log.md           # Send/delete confirmations and rollback notes
└── operation-log.md        # Operation IDs, verification evidence, outcomes
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup and first-run behavior | `references/setup.md` | Load on first use to define provider scope |
| Memory structure | `references/memory-template.md` | Load to understand data storage structure |
| Command hierarchy and probes | `references/command-paths.md` | Load to probe working command paths |
| Provider behavior matrix | `references/provider-coverage.md` | Load to check provider-specific caveats |
| Safety checklist before writes | `references/safety-checklist.md` | Load before executing write actions |
| Deterministic operation patterns | `references/operation-patterns.md` | Load to view operation patterns |
| Failure handling and recovery | `references/troubleshooting.md` | Load when errors or recovery paths are needed |
| Core rules | `references/core-rules.md` | Load to understand rules of operation |
| Common traps | `references/common-traps.md` | Load to avoid pitfalls and mistakes |
| Security & Privacy | `references/security-and-privacy.md` | Load for security bounds |
| Tech notes | `references/tech.md` | Load for domain knowledge and tech context |

## State location

Apple Mail Macos state may exist in `<workspace>/apple-mail-macos/`, `<workspace>/memory/apple-mail-macos/`, or `~/apple-mail-macos/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/apple-mail-macos/`, `<workspace>/memory/apple-mail-macos/`, `~/apple-mail-macos/`.
3. If none exists and state must be created, default to `<workspace>/apple-mail-macos/`.

Use the selected `<state_root>` for every state operation in this skill.

- **Type**: Stateful
- **Default Location**: `<state_root>/`
- **Fallback Location**: `~/.apple-mail-macos/`

All skill state and operational contexts are stored locally in the state directory. No remote state is used.
