---
name: automator
description: Automate macOS tasks by executing existing Automator `.workflow` files
  via the `automator` CLI or composing new workflows programmatically.
metadata:
  openclaw: '{"requires": {"config": ["<state_root>/"], "bins": ["automator", "osascript"]},
    "emoji": "A", "os": ["darwin"]}'
  related-skills:
  - applescript
  - automate
  - macos
  - workflow
---




## Setup

Load `references/setup.md` on first use to establish activation behavior and safety preferences.

## When to load

Load this skill when the user explicitly requests to run, create, or modify an Automator workflow (`.workflow` file) on macOS.

## Requirements

- macOS with `automator` and `osascript` available.
- Automator app installed at `/System/Applications/Automator.app`.
- Explicit user confirmation before destructive or bulk operations.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```text
<state_root>/
├── memory.md                # Activation rules and safety defaults
├── workflows.md             # Known workflow paths and run arguments
├── action-catalog.md        # Verified action names and categories
└── incidents.md             # Failures and proven fixes
```

## Quick Reference

Use these files when the task needs deeper detail.

| Topic | File |
|-------|------|
| Setup behavior and activation | `references/setup.md` |
| Memory structure | `assets/memory-template.md` |
| Execution path matrix | `references/interface-matrix.md` |
| Workflow authoring patterns | `references/workflow-authoring.md` |
| Write safety gates | `references/execution-guardrails.md` |
| Debug and recovery | `references/troubleshooting.md` |

## Data Storage

All local skill data stays in `<state_root>/`.
Before creating or changing local files, state the write scope and ask for confirmation.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | This skill uses local macOS interfaces only |

No other data is sent externally.

## Core Rules

### 1. Pick Interface by Intent, Not Convenience
- For running an existing `.workflow`, use `automator` CLI first.
- For composing or inspecting workflow internals, use Automator AppleScript commands from `references/workflow-authoring.md`.
- Only use `shortcuts` fallback if user explicitly asks for Shortcuts conversion.

### 2. Validate Workflow Identity Before Execution
- Require absolute workflow path and verify it exists.
- Confirm type (`.workflow`) and target operation (read, write, destructive).
- If the workflow path is ambiguous, ask one clarifying question before proceeding.

### 3. Enforce Read-Before-Write for Workflow Changes
- Before editing, inspect current action list and settings.
- Apply one mutation at a time and re-read state after each mutation.
- Apply edits to known actions incrementally.

### 4. Parameterize Inputs with Explicit Boundaries
- Use `automator -i` or `-D name=value` only with validated inputs.
- Reject unbounded stdin streams for write workflows.
- Echo resolved parameters before run so the user can verify intent.

### 5. Require Two-Step Confirmation for Destructive Runs
- Use `references/execution-guardrails.md` before delete, reset, or mass-change paths.
- Ask for explicit confirmation that includes target and scope.
- Ensure confirmation is present before running the workflow.

### 6. Keep Runs Observable and Reproducible
- Prefer verbose mode (`-v`) for first execution or after failure.
- Record command, input source, and result in concise run notes.
- Return actionable output, not only "completed" status.

### 7. Recover with Concrete Next Actions
- On failure, classify as path, permission, action mismatch, or runtime data error.
- Provide the next command to run, not generic retry advice.
- Persist only reusable fix patterns into local memory.

## Automator Traps

- Running relative paths from unknown working directories -> workflow not found.
- Guessing action names without dictionary inspection -> compile succeeds, runtime fails.
- Feeding multiline stdin into write workflows without boundaries -> unintended bulk edits.
- Mixing Automator and Shortcuts assumptions in one run -> incompatible action model.
- Treating permission prompts as transient errors -> repeated blocked execution.

## Security & Privacy

**Data that stays local:**
- Workflow paths, verified action names, and run diagnostics in `<state_root>/`.
- Command output required to complete the requested automation task.

**Data that leaves your machine:**
- None by default.

**This skill does NOT:**
- Access credentials outside the workflow request scope.
- Send workflow content to third-party services.
- Execute destructive automation without explicit confirmation.

## Related Skills
- `applescript` - Script app automation with robust quoting and pre-read checks.
- `automate` - Design reliable multi-step automation workflows.
- `macos` - Use macOS command-line and system operation patterns.
- `workflow` - Structure repeatable workflows and handoff states.
