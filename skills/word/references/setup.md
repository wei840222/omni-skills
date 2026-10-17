# Setup — Word

## First-time setup

### 1. Verify the official control path on this machine

```bash
command -v osascript
osascript -e 'tell application "Microsoft Word" to get name'
```

On non-Darwin hosts, stop: this skill requires macOS `osascript` and a local Word install.

### 2. Resolve and initialize `<state_root>`

Follow the State location procedure in `SKILL.md`. After consent to create durable state:

```bash
mkdir -p <state_root>
```

Create `<state_root>/memory.md` from `assets/data-templates.md`.

Optional companion files for repeated Word automation:

```bash
touch <state_root>/incidents.md <state_root>/document-notes.md
```

Never create a literal directory named `<state_root>`. Substitute the resolved path.

### 3. Capture the minimum environment facts

Add a few stable facts to `<state_root>/memory.md`:

- platform in use: macOS
- default control path: `osascript`
- whether Word is usually already open before automation starts
- preferred export folder for PDF or DOCX copies
- Word version when known

Store only metadata. Keep document contents, secrets, and credentials out of these notes.

### 4. Register the skill in workspace memory

Add a short note to workspace memory or AGENTS guidance that Word Desktop tasks should route to `word` when the job depends on the live app session.

Good trigger examples:

- document is already open in Word
- need comment or tracked-change actions
- need selection-aware edits
- need PDF export that matches current Word view or layout

### 5. Decide your safety defaults

Record these preferences in natural language. Preferences may raise the confirmation bar; they must not lower the mandatory floor in `references/safety-checklist.md`:

- whether accept-all or reject-all always requires confirmation
- whether close-without-save is always blocked
- whether the agent may create a copy before risky cleanup
- whether review mode changes are allowed without extra approval

### 6. First verification

Run one minimal read-only app check:

```bash
osascript <<'APPLESCRIPT'
tell application "Microsoft Word"
  if it is running then
    get name of active document
  else
    return "Word not running"
  end if
end tell
APPLESCRIPT
```

If this fails, use `references/troubleshooting.md` before attempting document changes.

## When "done"

Setup is done when:

- at least one official control path works on Darwin
- `<state_root>/memory.md` exists after consent
- safety defaults are written down
- a minimal read-only app check succeeds

## Storage rules

- Keep only reusable environment facts and safety preferences.
- Store document body text only if the user explicitly asks for a local note.
- Put repeatable failures in `<state_root>/incidents.md`.
- Put non-sensitive recurring document metadata in `<state_root>/document-notes.md`.
- Treat `~/Clawic/data/word/` as a migration source only; copy after explicit authorization.
