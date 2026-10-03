# Troubleshooting

Use when AppleScript execution fails.

## 1. Capture exact failure

Collect:

- Full `osascript` argv (redact secrets)
- Exit status and exact stderr
- Target app and intended action

Classify the failure before retrying.

## 2. Permission and Automation access

- Dictionary scripting uses per-app Automation consent; UI scripting needs Accessibility for the controlling process ([Apple UI scripting guide](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AutomatetheUserInterface.html)).
- Re-run a minimal read-only probe after the user adjusts **System Settings → Privacy & Security**.
- Do not loop permission prompts without a changed system state.

## 3. Dictionary mismatch

- Re-check class and property names in Script Editor.
- Confirm app version differences.
- Replace guessed properties with verified ones; update `<state_root>/app-notes.md` after consent.

## 4. Timing and app state

- Ensure the target app or process is running and ready.
- Add bounded wait/retry for startup races.
- For UI scripting, confirm the process exists under System Events before clicking menus.

## 5. Data and quoting issues

- Re-run with argv transport from `references/script-patterns.md`.
- Test with safe sample input.
- Verify list delimiters and return values.

## 6. Recovery output

Report:

- Root-cause category (permission, dictionary, timing, quoting, other)
- Next concrete command or clarification
- Safer fallback (read-only probe, narrower scope, or dictionary instead of UI)
