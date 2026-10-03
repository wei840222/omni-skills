# Script patterns

Robust patterns for `osascript` on macOS.

## Preferred argument transport (`on run argv`)

Pass user-controlled strings as argv so they are not interpolated into AppleScript source:

```bash
osascript \
  -e 'on run argv' \
  -e 'set noteTitle to item 1 of argv' \
  -e 'set noteBody to item 2 of argv' \
  -e 'tell application "Notes"' \
  -e '  make new note at folder "Notes" with properties {name:noteTitle, body:noteBody}' \
  -e '  return name of note noteTitle' \
  -e 'end tell' \
  -e 'end run' \
  -- "Project Ideas" "Brainstorming session"
```

Rules:

- Build multi-line scripts with repeated `-e` flags or a temp `.applescript` file under a secure temp directory.
- Keep user values in argv positions, not inside the `-e` text.
- Reject input that must act as AppleScript source rather than data.

## When shell fragments are required

If a value must enter a shell command from AppleScript, use AppleScript's `quoted form` of text (Language Guide) before `do shell script`. Prefer avoiding `do shell script` when dictionary commands suffice.

## Read-only probe

```applescript
tell application "System Events"
  get name of every application process whose background only is false
end tell
```

Use first to verify Automation permission and baseline execution.

## Read-before-write

```applescript
-- 1) Read target state / identity
-- 2) Apply change
-- 3) Read back final state
```

Always execute steps 1 and 3 for write operations.

## Timeout and wait

- Bounded retries for app launch readiness (explicit max attempts).
- Short delays only; stop with diagnostics when exhausted.
- For UI scripting, target `process "AppName"` under System Events after the process exists ([Apple — Automate the User Interface](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AutomatetheUserInterface.html)).

## Output normalization

- Concise, parse-friendly text.
- One record per line for lists.
- Include identifiers that allow verification.
