# App dictionary workflow

Use before writing app-specific AppleScript commands.

## 1. Confirm target and intent

- Confirm exact app name and requested action.
- Classify action as read-only, reversible write, or destructive.

## 2. Inspect the dictionary

- In Script Editor, choose **File > Open Dictionary** (or drag the app onto Script Editor) to view suites, classes, properties, and commands ([Apple — How Mac Scripting Works](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/HowMacScriptingWorks.html)).
- Record exact casing and object hierarchy.
- Prefer dictionary commands over UI scripting when both exist.

## 3. Minimal read-only probe

```applescript
tell application "TargetApp"
  -- read one known property confirmed in the dictionary
end tell
```

Run via `osascript` and keep the probe free of writes.

## 4. Expand in small steps

- Add one operation at a time.
- Validate output after each change.
- Keep each step reversible when possible.

## 5. Persist reusable notes

After user consent, store verified object names and command patterns in `<state_root>/app-notes.md`, and failed patterns with causes in `<state_root>/failures.md`.

## Red flags

- Class or property names guessed from memory.
- Multiple app versions with different dictionaries.
- UI-only actions attempted as direct dictionary commands (use System Events Processes suite only when dictionary scripting is insufficient and Accessibility is granted).
