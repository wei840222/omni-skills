---
name: homepod
description: Set up, troubleshoot, and optimize HomePod and Home audio workflows. Use when diagnosing Siri, Home app, automation, multiroom playback, or direct HomePod/Apple TV control; use general audio guidance when Apple Home ecosystem constraints do not drive the issue.
metadata:
  openclaw: '{"emoji":"H"}'
  related-skills: '{"audio":"Handles general audio routing and playback reliability beyond Apple Home environments.","ios":"Covers iPhone and iPad configuration that affects Home app control.","siri":"Diagnoses Siri intent and response behavior outside HomePod-specific workflows.","smart-home":"Provides cross-vendor smart-home architecture and reliability patterns.","wifi":"Diagnoses local network latency, packet loss, and Wi-Fi conditions."}'
---

## State location

HomePod state may exist in `<workspace>/homepod/`, `<workspace>/memory/homepod/`, or `~/homepod/`. Before reading or writing state:

1. Use an explicitly configured path when one exists.
2. Otherwise select the first existing directory in this order: `<workspace>/homepod/`, `<workspace>/memory/homepod/`, then `~/homepod/`.
3. If several directories exist, use only the highest-precedence one and report the duplicate state locations.
4. If none exists and the user wants persistent notes, create `<workspace>/homepod/`.

Use the selected `<state_root>` for this invocation. State files are optional: `<state_root>/memory.md` stores preferences and incident summaries; `<state_root>/homes.md` stores device topology; `<state_root>/automation-log.md` records automation tests; `<state_root>/network-notes.md` records network observations. The resolver selects a location; ask before creating or modifying persistent notes.

## When to use

Use this skill for HomePod setup, direct playback control, Siri failures on a HomePod, Home app automations, and multiroom audio stability. For each incident, identify the affected device or room, capture the current software and home-hub state, apply the narrowest reversible fix, then rerun the same validation.

## Quick reference

| Topic | File | When to load |
|---|---|---|
| Setup and persistent notes | `references/setup.md` | First-use configuration or when creating notes |
| State-note template | `references/memory-template.md` | Writing HomePod state under `<state_root>/` |
| Direct connection and control | `references/direct-control.md` | The user requests active playback control |
| Network triage flow | `references/network-diagnostics.md` | Connectivity, discovery, sync, or Siri timeout issues |
| Automation reliability playbook | `references/automation-playbook.md` | An automation is intermittent, delayed, or non-deterministic |
| Siri failure recovery map | `references/siri-recovery.md` | Siri hears a request but does not complete the intended Home action |
| Core operating rules | `references/core-rules.md` | Before recommending a fix or a reset |
| Common traps | `references/common-traps.md` | During troubleshooting or automation work |
| Apple documentation and hardware facts | `references/domain-knowledge.md` | Verifying current platform behavior or a reset path |

## Security and privacy

- Keep notes to device state, failures, and validation evidence; exclude voice transcripts and unrelated household content.
- Explain the impact and obtain confirmation before an account-level action, persistent-state write, direct control command, or reset.
- Use one verified target for a mutating command and record its pre- and post-command state when the user elects to keep notes.
- Keep pairing credentials in the platform's secure pairing flow, not in `<state_root>/` or this skill package.
