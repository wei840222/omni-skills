---
name: apple-maps
description: >
  Search places, open nearby results, and launch driving, walking, or transit
  routes in Apple Maps on macOS through Maps URL schemes and local CLI fallbacks.
  Use when the user asks to find a place, center a map, get directions, or open
  Apple Maps from the terminal with explicit confirmation for bulk or share actions.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🗺️","os":["darwin"],"requires":{"anyBins":["open","shortcuts","osascript"]}}'
  related-skills: '{"car-rental":"Route-linked transport planning adjacent to map destinations.","macos":"macOS command workflows and automation patterns used by Maps launches.","restaurants":"Food venue discovery and shortlist workflows that often hand off to Maps.","travel":"Travel-planning flows and destination strategy that need map or route opens."}'
---
## State location

Apple-maps state may exist in `<workspace>/apple-maps/`, `<workspace>/memory/apple-maps/`, or `~/apple-maps/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/apple-maps/`, `<workspace>/memory/apple-maps/`, `~/apple-maps/`.
3. If none exists and state must be created, default to `<workspace>/apple-maps/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, follow `references/setup.md` to establish scope, preferred command path, and safety defaults before routing or sharing actions.

## When to Use

User wants to search places, categories, addresses, and routes in Apple Maps from macOS using dedicated native apps instead of browser workflows.
Agent handles place search, nearby category lookup, route launching, and reusable map-link generation.

## Requirements

- macOS with Maps.app installed.
- At least one working command path: `open`, `shortcuts`, or `osascript` fallback.
- Network access to Apple Maps for live place and route results.
- Explicit confirmation before sharing links externally or launching bulk actions.

## Architecture

Memory lives in `<state_root>/`. See `references/memory.md` for structure.

```text
<state_root>/
├── memory.md             # Status, defaults, and validated command path
├── command-paths.md      # Command priority, probes, and URL strategy
├── safety-log.md         # Confirmations for high-impact actions
└── operation-log.md      # Search and route operation IDs with outcomes
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup and first-run behavior | `references/setup.md` |
| Memory structure | `references/memory.md` |
| Command hierarchy and probes | `references/command-paths.md` |
| Deterministic operation flows | `references/operation-patterns.md` |
| Safety checklist before action | `references/safety-checklist.md` |
| Failure handling and recovery | `references/troubleshooting.md` |
| Verified research sources | `references/sources.md` |

## Data Storage

All skill files are stored in `<state_root>/`.
Before creating or changing local files, describe the planned write and ask for confirmation.

## Core Rules

### 1. Use Apple Maps URL Workflows as Primary Interface
- Build map requests as explicit Apple Maps URLs and launch with `open -a Maps`.
- Prefer documented URL parameters instead of UI-only automation.

### 2. Probe Command Path Before Operations
- Verify command availability in strict order: `open`, `shortcuts`, `osascript`.
- If only fallback paths are available, explain capability limits before executing.

### 3. Keep Searches Bounded and Deterministic
- Require clear intent: query text, optional area, and optional map zoom/context.
- For ambiguous requests like "best restaurants", ask for location context before launching Maps.

### 4. Preview Generated URL Before Execution
- For every action, show the final URL and explain major parameters.
- If the query contains user-sensitive text, confirm before opening or sharing.

### 5. Confirm High-Impact Actions
- Require explicit confirmation for route launches with destination changes, share-link generation, and repeated bulk opens.
- For repeated actions, present a count and require a second confirmation.

### 6. Verify Result State After Launch
- After opening Maps, summarize expected visible outcome (query, destination, mode).
- If result does not match intent, refine parameters instead of retrying blindly.

### 7. Minimize Data Exposure
- Use minimal query strings needed for the requested task.
- Limit map queries exclusively to declared Apple Maps APIs.

## Common Traps

- Launching vague searches without area context -> ask for city/neighborhood, then relaunch with `near`.
- Sharing raw links that include private notes -> preview the URL and require explicit share approval.
- Using UI scripting as default path -> prefer `open -a Maps` URL workflows; keep `osascript` as last fallback.
- Opening many candidate links at once -> shortlist in text first; open one link unless the user confirms bulk.
- Assuming route mode without confirmation -> confirm driving/walking/transit, set `dirflg`, then launch.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://maps.apple.com | Search text, optional coordinates, routing parameters | Retrieve map, place, and route results in Apple Maps |

No other external endpoint is required by default.

## Security & Privacy

**Data that stays local:**
- Operational defaults, safety choices, and command reliability notes in `<state_root>/`.

**Data that may leave your machine:**
- Place queries, route origins/destinations, and map parameters sent to Apple Maps when opening URLs.

**This skill is designed to:**
- Execute only explicitly declared Apple Maps API calls.
- Persist sensitive location context only after explicit user approval.
- Run bulk opens or share actions only after explicit user confirmation.

## Trust

By using this skill, map queries and route parameters are sent to Apple Maps.
Only use this workflow if you trust Apple Maps with that data.
