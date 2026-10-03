# Setup — AppleScript

Use on first run to establish activation behavior and safety defaults.
This flow is read-only until the user confirms a persistent write.

## Attitude

Be practical, calm, and explicit so AppleScript tasks feel predictable and safe.

## Priority order

### 1. Integration preferences

Within the first exchanges, confirm:

- Should this skill activate when macOS app automation is requested?
- Should destructive warnings always appear (recommended), or only when the user asks?
- Are there apps that must stay read-only?

### 2. Automation goal

Clarify before implementation:

- Which app is the target?
- Is the work read state, create data, or edit existing data?
- What output format is most useful?

### 3. Reliability defaults

If the user wants persistent behavior, store under the resolved `<state_root>` after confirmation:

- Confirmation level for write and delete (may only raise the mandatory floor)
- Preferred output format
- Known working dictionary terms and fallbacks

If the user wants minimal setup, keep conservative in-session defaults and continue without creating files.

## What may be saved

After explicit confirmation only:

- Activation preferences and safety boundaries in `<state_root>/memory.md`
- Per-app patterns in `<state_root>/app-notes.md`
- Failure signatures in `<state_root>/failures.md`
- Reusable snippets in `<state_root>/snippets.md`

After any memory update, restate the user-visible impact in plain language.

## Consent rules

- Explain the path and content summary before the first create or update under `<state_root>/`.
- Prefer `assets/memory-template.md` as the skeleton for `<state_root>/memory.md`.
- Lifecycle and status semantics live in `references/memory.md`; do not duplicate conflicting rules in the template.
