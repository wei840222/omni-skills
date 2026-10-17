# Live Control Patterns — Word

Keep each script short, identify the document first, and verify after mutation.

## 1. Attach and identify

```applescript
tell application "Microsoft Word"
  if not (it is running) then return "Word not running"
  set docName to name of active document
  return docName
end tell
```

Why: every later write must bind to a verified document identity, not an assumed front window.

## 2. Read selection and review context before edit

Pre-read:

- active document name / path when available
- selection text or story range summary
- track-changes / protection signals the host exposes
- comment count when comments are in scope

If the selection is empty or ambiguous, clarify before writing.

## 3. Prefer object anchors over bare insertion point

When the user names a heading, bookmark, comment, or paragraph, resolve that object and act on it. Cursor-only writes are high-risk because the insertion point can sit in headers, footers, text boxes, or comment balloons.

## 4. Export through Word's own layout engine

For PDF that must match the live layout, use Word's export/save path after updating fields or TOC when those objects exist. Prefer absolute export paths. Confirm the destination file after export.

Useful primary references: Word `Document` / `ExportAsFixedFormat` APIs and `WdSaveFormat` enumerations on learn.microsoft.com.

## 5. Leave the user's session intact

- Keep Word running if you attached to a user-owned session.
- Leave unrelated documents open.
- Report which document and view were left active at the end.

## 6. Transport dynamic text safely

When inserting user-supplied text, prefer argv into an `on run argv` handler or AppleScript `quoted form` rather than concatenating raw text into `osascript -e` strings. See the sibling `applescript` skill for general transport patterns.
