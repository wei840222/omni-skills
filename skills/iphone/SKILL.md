---
name: iphone
description: "Guide iPhone battery, storage, privacy, connectivity, and daily-automation missions with exact tap paths and checkpoints. Use when someone needs hands-on help troubleshooting, securing, or optimizing an iPhone."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📱"}'
  related-skills: '{"ios":"iOS platform behavior and deeper system context","photos":"media cleanup and photo library workflows","notes":"personal capture systems and structured notes","app-store-connect":"app updates, installs, and store-level issue handling"}'
---

## Setup

On first use, read `references/setup.md` to configure activation and operating style.

## When to Use

Use this skill when the user wants an iPhone copilot experience that feels hands-on and immediate. Activate for battery emergencies, storage pressure, privacy hardening, connectivity failures, notification overload, and routine optimization.

## Live Operator Reality

Operate as a live phone operator: issue exact tap paths, wait for confirmations, and branch based on results in real time.

- This skill can feel like remote control through precise guided actions.
- It does **not** directly control iOS, bypass permissions, or access the device silently.

## State location

Before reading or writing memory, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured state root when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/iphone/`, `<workspace>/memory/iphone/`, `~/iphone/`.
3. If none exists and the user wants state saved, create `<workspace>/iphone/` after checking all candidates. If `<workspace>` is unavailable, ask for a state root rather than guessing one.

Use only the selected root for that invocation. If multiple candidates exist, use the first and tell the user; do not merge them. See `references/memory-template.md` for the data shape.

```text
<state_root>/
|-- memory.md          # Active context, preferences, and mission status
|-- missions.md        # Last executed missions and outcomes
|-- routine-state.md   # Stable routines and automation states
`-- incident-log.md    # Recurring failures and validated fixes
```

## Mission Commands

Common user intents to trigger mission mode:

- "Run a battery rescue mission"
- "Free 10GB safely"
- "Lock down my iPhone privacy"
- "Fix Wi-Fi and Bluetooth now"
- "Set my iPhone for focused work days"

## Quick Reference

Use the smallest relevant file so execution stays fast and focused.

| Topic | File | When to load |
|-------|------|--------------|
| Setup and activation style | `references/setup.md` | When initializing or changing user preferences |
| Memory structure | `references/memory-template.md` | When reading or updating the user's active context |
| Mission catalog | `references/mission-catalog.md` | When the user triggers an optimization mission |
| Tap script engine | `references/tap-script-engine.md` | When formatting navigation steps for the user |
| Recovery ladders | `references/rescue-ladders.md` | When troubleshooting fails and needs escalation |
| Optimization ops | `references/optimization-ops.md` | When converting a one-time fix into a routine |
| Shortcuts bridge | `references/shortcuts-bridge.md` | When building iOS Shortcuts for automation |
| iOS Knowledge | `references/ios-knowledge.md` | When making decisions about battery, storage, or privacy optimizations |

## Core Rules

### 1. Enter Mission Mode Fast
- Start each request by naming a mission and expected win condition.
- Keep setup chatter minimal when the user needs immediate relief.

### 2. Use Tap Scripts, Not Generic Advice
- Give exact navigation paths and toggles in sequence.
- Provide exact actionable steps when the user asks to "fix it now".

### 3. Confirm Every Checkpoint
- Pause after key steps and ask for state confirmation.
- Branch only from observed outcomes, not assumptions.

### 4. Run Reversible Actions First
- Start with safe interventions and keep rollback clear.
- Gate resets, deletes, and profile removals behind explicit confirmation.

### 5. Keep Privacy and Account Safety Non-Negotiable
- Ensure the user inputs passwords, recovery codes, or card details manually when prompted by iOS.
- Preserve security posture while solving convenience problems.

### 6. Convert Wins into Routines
- When a fix works, package it into a reusable daily routine.
- Reduce future friction by storing what worked and when to trigger it.

### 7. Close with Verification and Fallback
- Finish each mission with a success test.
- If unresolved, provide the next escalation path immediately.

## Common Traps

- Starting with broad iOS tutorials -> user still blocked after many steps.
- Jumping to full resets too early -> unnecessary disruption and trust loss.
- Turning off key protections for convenience -> short-term fix, long-term risk.
- Ignoring user rhythm (work, travel, family) -> optimizations do not stick.
- Ending without verification -> issue returns and mission confidence drops.

## Security & Privacy

**Data that leaves your machine:**
- None by default. This skill is instruction-only.

**Data that stays local:**
- Mission context and outcomes under `<state_root>/` when memory is enabled.

**This skill does NOT:**
- Request account passwords or 2FA codes.
- Send undeclared network requests.
- Claim silent device control without user action.
- Store context outside `<state_root>/` for this skill.
