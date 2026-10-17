# Data Templates

Copy these skeletons into the resolved `<state_root>` after consent. Do not write the literal string `<state_root>` to disk.

## memory.md

```markdown
# Word Memory

## Status
status: active
version: 1.1.0
last_verified: YYYY-MM-DD
platform: macOS
control_path: osascript
word_attach_mode: attach-existing | launch-new | mixed

## Safety Defaults
- Accept all changes: ask every time
- Reject all changes: ask every time
- Close without save: blocked unless user confirms
- Risky cleanup: prefer Save As or document copy first

## Environment Notes
- Word version:
- Default control shell:
- Typical document locations:
- Preferred export folder:
- Known review policy:

## Document Notes
- Store only document identifiers, stable paths, and non-sensitive structure notes
- Keep document contents and secrets out of this file

## Recent Incidents
- YYYY-MM-DD: short failure signature -> short fix
```

## incidents.md

```markdown
# Word Incidents

## YYYY-MM-DD
- Symptom:
- Document:
- Cause:
- Fix:
```

## document-notes.md

```markdown
# Document Notes

## Document: /absolute/path/to/file.docx
- Default view:
- Review mode:
- Export target:
- Known quirks:
```
