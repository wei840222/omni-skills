# Memory Template — PowerPoint

Create `<state_root>/memory.md` with this structure:

```markdown
# PowerPoint Memory

## Status
status: active
version: 1.1.0
last_verified: YYYY-MM-DD
platform: macOS
control_path: osascript
ppt_attach_mode: attach-existing | launch-new | mixed

## Safety Defaults
- Delete slide: ask every time
- Close without save: blocked unless user confirms
- Overwrite exports: ask every time
- Risky cleanup: prefer Save As or deck copy first

## Environment Notes
- PowerPoint version:
- Default control shell:
- Typical deck locations:
- Preferred export folder:
- Known slideshow policy:

## Deck Notes
- Store only presentation identifiers, stable paths, and non-sensitive structure notes
- Exclude slide contents, secrets, or personal information here

## Recent Incidents
- YYYY-MM-DD: short failure signature -> short fix
```

## Storage Rules

- Keep only reusable environment facts and safety preferences.
- Exclude slide body content unless the user explicitly asks for a local note.
- Put repeatable failures in `<state_root>/incidents.md`.
- Put non-sensitive recurring deck metadata in `<state_root>/deck-notes.md`.

## Optional Companion Files

`<state_root>/incidents.md`:

```markdown
# PowerPoint Incidents

## YYYY-MM-DD
- Symptom:
- Presentation:
- Cause:
- Fix:
```

`<state_root>/deck-notes.md`:

```markdown
# Deck Notes

## Presentation: /absolute/path/to/file.pptx
- Default view:
- Common export target:
- Known quirks:
- Slideshow notes:
```
