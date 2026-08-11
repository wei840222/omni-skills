---
name: airdrop
description: Send local files, exports, screenshots, or review artifacts to nearby Apple devices through AirDrop. Use when the user asks to "airdrop", "share locally", or hand off files to an iPhone, iPad, or Mac.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"A"}'
  related-skills: '{"applescript":"Finder and app automation when AirDrop workflows need UI scripting around local files.","files":"File selection, packaging, renaming, and cleanup before sharing the final payload.","macos":"General macOS command workflows, permissions checks, and native app automation patterns.","photos":"Exporting and converting image assets before sending them to another Apple device."}'
---

## State location

AirDrop state may exist in `<workspace>/airdrop/`, `<workspace>/memory/airdrop/`, or `~/airdrop/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/airdrop/`, `<workspace>/memory/airdrop/`, `~/airdrop/`.
3. If none exists and state must be created, default to `<workspace>/airdrop/`.

Use the selected `<state_root>` for every state operation in this skill.
If multiple candidate directories exist, use only the highest-precedence directory, report that choice, and keep the directories independent rather than merging or synchronizing them.

## When to Use

User wants the agent to send a local file, export, screenshot, log bundle, or review artifact to a nearby Apple device with AirDrop.
Agent handles file staging, confirmation, local handoff, and mode selection between direct AppKit launch and Shortcut fallback.

## Requirements

- macOS with AirDrop enabled in Finder.
- Nearby Apple recipient available and visible to the current Mac.
- Direct mode uses `xcrun swift` or `swift` to run `scripts/airdrop-send.swift`.
- Shortcut mode uses the built-in `shortcuts` CLI and a user-owned shortcut that accepts file input.

## Core Rules

### 1. Resolve Exact Files Before Sharing
- Work only with explicit local file paths.
- For generated text or mixed output, stage to a user-approved file first, then share that file.
- If the user requests to send vague targets like "the project", refuse execution and ask the user to explicitly list the files.

### 2. Use the Smallest Safe Payload
- Target the exact artifact the recipient needs: one PDF, one ZIP, one screenshot set, one installer.
- When the source is a directory, curate or archive the approved subset before launch.
- Exclude hidden files, secrets, and unrelated workspace state.

### 3. Keep Recipient Choice Interactive
- AirDrop recipient selection stays in the macOS share UI.
- Always keep recipient selection interactive in the macOS share UI and verify success manually.
- If the user wants zero-click routing, use Shortcut mode only when they already built that behavior locally.

### 4. Pick the Right Execution Mode
- Execute `scripts/airdrop-send.sh` for direct local handoff because it launches the native AirDrop sharing service without inventing unsupported CLI verbs.
- Execute Shortcut mode when the user already has a Shortcut that renames, compresses, or routes files before AirDrop.
- If `swift` is unavailable and the user does not have a configured Shortcut, report failure and instruct the user to run `xcode-select --install`.

### 5. Confirm Sensitive Shares
- Before launching AirDrop for logs, source bundles, contracts, exports, or anything private, list the exact files and request confirmation from the user.
- If the user requests "only the final artifact", strip extras before sharing.
- Only include credential files, env files, database dumps, or hidden config if the user explicitly authorizes them.

### 6. Report Handoff Honestly
- Report success only when the AirDrop chooser launches with the requested files.
- Say the transfer is complete only when the user confirms it on-device.
- If launch succeeds but the device does not appear, instruct the user to read `references/troubleshooting.md`.

## Negative Examples

- Attempting silent background delivery or machine-verifiable recipient identity targeting.
- Sharing unrelated workspace files, secrets, or unapproved payload items.
- Assuming transfer completion before the user confirms it.
- Retrying blindly without diagnosing the visibility issue if the device does not appear.

## Architecture

Memory lives in `<state_root>/`. When the user wants persistent behavior and `<state_root>/` does not exist, read `references/setup.md`; read `references/memory.md` for the state structure.

```text
<state_root>/
|- memory.md          # Activation and confirmation preferences
`- staging/           # Optional user-approved temp exports before sharing
```

## Quick Reference

| Topic | File |
|-------|------|
| First-run behavior and activation | `references/setup.md` |
| Memory structure | `references/memory.md` |
| Direct CLI wrapper | `scripts/airdrop-send.sh` |
| AppKit AirDrop launcher | `scripts/airdrop-send.swift` |
| Common execution patterns | `references/workflow-recipes.md` |
| Recovery and diagnostics | `references/troubleshooting.md` |

## Common Traps

| Trap | Why It Fails | Better Move |
|------|--------------|-------------|
| Treating AirDrop like `scp` | No stable official recipient CLI targeting | Launch native chooser and keep recipient selection interactive |
| Sending raw text directly | AirDrop works on shareable items, not vague chat content | Write the text to a file, then share that file |
| Sharing whole folders by reflex | Leaks unrelated files and slows discovery | Zip or curate the exact approved subset first |
| Claiming delivery success too early | Launching the chooser is not transfer confirmation | Report "handoff started" until the user confirms receipt |
| Retrying with the same bad payload | Hidden files or unsupported items keep failing | Reduce to one known-good file and retry once |

## Data Storage

This skill can operate with no persistent local state.
If the user wants repeatable behavior, store only activation, confirmation, and staging preferences in `<state_root>/memory.md`.
Create `<state_root>/staging/` only with user approval when temporary share files are useful.

## Security & Privacy

**Data that stays local:**
- Skill memory and optional staging files in `<state_root>/`
- The source files until the user chooses a nearby AirDrop recipient

**Data that may leave your machine:**
- Only the specific files the user approved for AirDrop
- Discovery and transfer metadata handled by macOS AirDrop services with nearby Apple devices

**This skill does NOT:**
- Upload files to undeclared cloud services
- Select recipients silently in the background
- Confirm transfer completion without user-visible evidence
- Read or share files outside the approved payload list
