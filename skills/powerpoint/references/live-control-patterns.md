# Live Control Patterns — PowerPoint

These are operational patterns, rather than generic tutorials. Verify terminology against the local Microsoft PowerPoint dictionary on the target Mac before relying on any single verb.

## 1. Read the active presentation on macOS

```bash
osascript <<'APPLESCRIPT'
tell application "Microsoft PowerPoint"
  if not running then return "PowerPoint not running"
  if (count of presentations) is 0 then return "No open presentations"
  return name of active presentation
end tell
APPLESCRIPT
```

Why: active deck identity must be verified before slide actions.

## 2. Read the active slide index

```bash
osascript <<'APPLESCRIPT'
tell application "Microsoft PowerPoint"
  return slide index of slide range of active window
end tell
APPLESCRIPT
```

Why: slide-aware actions fail fast when you fail to confirm the active slide first.

## 3. Export the live deck to PDF

```bash
osascript -e 'tell application "Microsoft PowerPoint" to save active presentation in "/absolute/path/to/output.pdf" as save as PDF'
```

Why: this uses PowerPoint's own rendering path instead of rebuilding slides elsewhere. Use an absolute, non-colliding path; confirm before overwrite.

## 4. Leave the user's session intact

- Keep PowerPoint running if you attached to a user-owned session.
- Keep unrelated decks open.
- Report which presentation and slide were left active at the end.
