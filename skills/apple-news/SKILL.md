---
name: apple-news
description: "Execute reading workflows on macOS using deterministic CLI commands to launch Apple News, open articles, and fallback to shortcut-based search."
compatibility: "darwin"
metadata:
  version: "1.0.0"
  openclaw: '{"emoji": "\ud83d\udcf0", "requires": {"anyBins": ["open", "osascript", "shortcuts"], "config": ["<state_root>"]}, "os": ["darwin"], "configPaths": ["<state_root>"], "displayName": "Apple News (MacOS)"}'
  related-skills: '{"macos": "macOS command workflows and automation patterns.", "news": "general news workflows and monitoring patterns.", "travel": "location and context workflows for news around destinations.", "reading": "reading queue and prioritization workflows.", "productivity": "execution frameworks for daily information intake."}'
---

## Setup

On first use, follow `setup.md` to define command-path preferences, link-opening behavior, and search fallback strategy before bulk actions.

## When to Use

User wants to open Apple News, read specific Apple News articles, or run repeatable News reading workflows from macOS.
Agent handles app launch, article and feed link opening, reading queue workflows, and optional shortcut-based topic search.

## Requirements

- macOS with News.app installed at `/System/Applications/News.app`.
- At least one working command path: `open`, `osascript`, or `shortcuts`.
- Apple News links when opening specific articles (`https://apple.news/...`).
- Explicit confirmation before opening multiple links or running broad shortcut workflows.

## Architecture

Memory lives in `<state_root>`. See `memory-template.md` for structure.

```text
<state_root>
├── memory.md             # Status, defaults, and preferred workflows
├── command-paths.md      # Command probes and validated launch paths
├── safety-log.md         # Multi-link confirmations and sensitive link notes
└── operation-log.md      # Open operations, shortcut calls, and outcomes
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Domain Knowledge | `references/domain-knowledge.md` | Load when requesting background on Apple News. |
| Common Traps | `references/common-traps.md` | Load when debugging unexpected behavior. |
| Core Rules | `references/core-rules.md` | Load when understanding behavioral constraints. |
| Setup and first-run behavior | `setup.md` | Load during initialization or setup phase. |
| Memory structure | `memory-template.md` | Load when initializing or modifying the user's configuration memory. |
| Command hierarchy and probes | `command-paths.md` | Load when finding the path to execute a command. |
| Deterministic operation flows | `operation-patterns.md` | Load when launching or navigating inside the Apple News app. |
| Safety checklist before action | `safety-checklist.md` | Load before opening multiple links. |
| Failure handling and recovery | `troubleshooting.md` | Load when an execution failure occurs. |

## State location

1. Workspace configuration: `<state_root>`
2. Fallback: `~/.config/apple-news`

Create the state directory if it does not exist before writing any configuration.

## Data Storage

All skill files are stored in `<state_root>`.
Before creating or changing local files, describe the planned write and ask for confirmation.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://apple.news | Apple News article/feed URL parameters | Open Apple News content in News.app |

No other external endpoint is required by default.

## Security & Privacy

**Data that stays local:**
- Operational defaults, safety choices, and command reliability notes in `<state_root>`.

**Data that may leave your machine:**
- Apple News links opened through `https://apple.news`.
- Any network requests triggered by user-owned Shortcuts if user enables them.

**This skill does NOT:**
- Execute undeclared API calls by default.
- Persist sensitive reading context without user approval.
- Run bulk opens without explicit confirmation.

## Trust

By using this skill, links are opened against Apple News.
If you enable shortcut-based search, those shortcuts may call additional services defined by the user.
