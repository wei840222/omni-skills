---
name: applescript
description: >
  Write and run safe AppleScript automation on macOS with osascript, dictionary
  discovery, robust argument transport, and read-before-write verification. Use
  when controlling scriptable Mac apps, extracting local app data, or automating
  UI via System Events on Darwin. Not for Linux/Windows hosts, pure shell tasks
  (bash), general macOS admin without AppleEvents (macos), or note-taking apps
  as a content skill (notes).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🍎","os":["darwin"],"requires":{"bins":["osascript"]}}'
  related-skills: '{"automate":"General automation reliability and workflow design around AppleScript steps.","bash":"Shell wrappers, quoting, and process control when invoking osascript from scripts.","files":"Safe bulk file operations outside app dictionaries.","macos":"Darwin host admin, TCC privacy gates, and non-AppleEvent system tooling.","notes":"Structured note capture when the target is knowledge content rather than Notes.app scripting."}'
---

## State location

AppleScript skill state may exist in `<workspace>/applescript/`, `<workspace>/memory/applescript/`, or `~/applescript/`. Before any state read or write, resolve one `<state_root>`:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order: `<workspace>/applescript/`, `<workspace>/memory/applescript/`, `~/applescript/`.
3. If multiple candidates exist, use only the highest-precedence directory, report the split, and leave lower-precedence copies unchanged.
4. If none exists and persistent state is needed, propose `<workspace>/applescript/` and create it only after the user confirms.
5. If the host cannot supply `<workspace>`, read an existing `~/applescript/` only; otherwise ask for a state root before creating data.

Keep the selected `<state_root>` fixed for the invocation. After resolution it holds optional domain files:

```text
<state_root>/
├── memory.md      # preferences, safety floor, last working patterns (create on first durable save)
├── snippets.md    # reusable verified script fragments (create when a pattern is reused)
├── failures.md    # error signatures and fixes (create on first captured failure)
└── app-notes.md   # per-app dictionary terms and behavior (create when an app is probed)
```

Legacy vendor path `~/Clawic/data/applescript/` is a migration source only. Do not put it in active lookup order. Copy into `<state_root>` only after explicit user authorization with validation and rollback.

## When to use

- User needs AppleScript or `osascript` on a Mac for app control, local data extraction, or scripted UI.
- Target app is installed and scriptable, or UI automation via System Events is explicitly requested.
- Prefer `macos` for TCC/Keychain/launchd admin without AppleEvents; prefer `bash` for shell-only work; prefer `notes` when the product is note content rather than Notes.app automation.

## Requirements

- Darwin host with `osascript` available (`/usr/bin/osascript`).
- Target app installed and scriptable for dictionary-based automation; UI scripting additionally needs Accessibility permission for the controlling process.
- Explicit user confirmation before destructive, bulk, send, or irreversible actions.
- Automation permission prompts accepted for each controlling app when macOS requires them.

## References

Load only when the current step needs them:

| File | Load when |
| --- | --- |
| `references/setup.md` | First use, activation preferences, or consent for persistent state |
| `references/app-dictionary-workflow.md` | Before scripting an unfamiliar app or inventing class/property names |
| `references/script-patterns.md` | Building `osascript` invocations, safe argument transport, read-modify-verify |
| `references/safety-checklist.md` | Before delete, bulk edit, send, or irreversible app actions |
| `references/troubleshooting.md` | `osascript` failure, permission denial, dictionary mismatch, or timing errors |
| `references/memory.md` | Creating or updating durable preferences and app profiles under `<state_root>` |
| `references/sources.md` | Verifying domain claims or citing primary Apple documentation |
| `assets/memory-template.md` | Copying the static memory skeleton into `<state_root>/memory.md` after consent |

## Core rules

1. **Classify scope first.** Label the request read-only, reversible write, or destructive write. If unclear, ask one disambiguation question before execution.
2. **Confirm platform and binary.** On non-Darwin hosts, stop and say `osascript` is unavailable. On Darwin, verify `command -v osascript` before running scripts.
3. **Discover vocabulary.** For app automation, follow `references/app-dictionary-workflow.md` and record verified terms in `<state_root>/app-notes.md` after consent. Do not invent classes, properties, or commands.
4. **Transport values safely.** Pass dynamic text through argv into an AppleScript `on run argv` handler, or use AppleScript `quoted form` when a shell fragment is unavoidable. Prefer argv over string concatenation into `-e` scripts. Details: `references/script-patterns.md`.
5. **Keep scripts bounded and observable.** Prefer short scripts with explicit targets and concise structured output (one record per line when listing).
6. **Read before write; verify after write.** Pre-read target identity for creates/updates; read back final state and report it.
7. **Destructive floor is mandatory.** Apply `references/safety-checklist.md`. Require two-step confirmation for delete, bulk edit, empty trash, send, or irreversible actions. Preference files may raise the confirmation bar; they must not lower it below this floor.
8. **Fail with recovery.** Capture the exact `osascript` command, exit status, and stderr. Use `references/troubleshooting.md` and append durable failure notes to `<state_root>/failures.md` only after consent.
9. **Stay local by default.** Keep snippets, outputs, and troubleshooting notes on-machine. Do not read unrelated credentials or send automation data to third parties unless the user explicitly authorizes a separate channel.

## Security and privacy

**Stays local by default:** script snippets, runtime notes, command output needed for the task, and optional state under `<state_root>/`.

**Does not leave the machine by default:** no third-party upload of automation data.

**This skill does not:**

- Read unrelated authentication values or Keychain secrets for convenience.
- Execute destructive app actions without explicit confirmation.
- Treat UI scripting (Accessibility) as equivalent to dictionary scripting; name the permission class in use.

## Common traps

- Guessing dictionary terms → compiles then fails at runtime; probe first.
- Embedding raw user text in `-e` strings → quote breaks and wrong targets; use `on run argv`.
- Writing without pre-read on duplicate names → wrong object modified.
- UI automation immediately after launch → intermittent misses; wait for process readiness with a bounded retry.
- Treating every error as a TCC denial → re-check dictionary, app state, and quoting before permission loops.
- Lowering safety defaults in memory templates → mandatory confirmation floor still applies.
