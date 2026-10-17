---
name: word
description: >
  Control live Microsoft Word on macOS with osascript: attach or launch sessions,
  identify the exact document and view, selection-aware edits, comments, track
  changes, field/TOC refresh, PDF/DOCX export, and clean recovery. Use when the
  document is already open in Word, review markup or cursor state matters, or
  export must match the live layout. Prefer `word-docx` for offline OOXML file
  work, `office` for cross-app Office routing, and `applescript` when the task
  is general Mac scripting rather than Word Desktop control.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📝","os":["darwin"],"requires":{"bins":["osascript"]}}'
  related-skills: '{"word-docx":"Offline DOCX/OOXML generation and structural edits when Word does not need to stay open.","office":"Broader Office task routing across documents, spreadsheets, and presentations.","applescript":"General macOS osascript patterns, dictionary discovery, and argv transport outside Word-specific workflows."}'
---

# Word

Operate **live Microsoft Word Desktop** through `osascript` and Word's scripting
dictionary. Keep automation inside the current app session; do not fall back to
offline DOCX libraries when the job depends on live selection, comments, track
changes, or Word's own layout/export path.

## State location

Word memory, incidents, and document notes are persistent user state. Resolve
`<state_root>` once per invocation before any read or write:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/word/`, `<workspace>/memory/word/`, then `~/word/`.
3. If more than one candidate exists, use only the highest-precedence directory,
   report the duplicates, and leave lower-precedence copies unchanged.
4. If none exists and durable Word state is needed, propose
   `<workspace>/word/` and create it only after the user confirms. If
   `<workspace>` is unavailable, read an existing `~/word/` only; otherwise ask
   for a state root before creating data.
5. Keep `<state_root>` fixed for the invocation.

After resolution, optional domain files live under:

```text
<state_root>/
├── memory.md             # Environment facts, safe defaults, last working control path
├── incidents.md          # Reusable failures and proven recovery steps
└── document-notes.md     # Non-sensitive notes about trusted documents, views, exports
```

Legacy vendor path `~/Clawic/data/word/` is a migration source only. Do not put
it in active lookup order. Copy into `<state_root>` only after explicit user
authorization with validation and rollback. Never write the literal string
`<state_root>` to disk.

## When to use

- The document is already open in Word, or the job depends on live app state.
- Selection-aware edits, comments, track changes, or review-mode actions.
- Field/TOC refresh and PDF/DOCX export that must match the live Word layout.
- Prefer `word-docx` for offline structural DOCX work; prefer `office` for
  cross-app routing; prefer `applescript` for non-Word Mac automation.

## Requirements

- Darwin host with `osascript` available (`/usr/bin/osascript`).
- Microsoft Word installed locally and scriptable.
- Explicit confirmation before destructive document actions (accept/reject all,
  bulk comment deletion, close without save, overwrite exports, whole-document
  replace).
- Automation permission prompts accepted when macOS requires them for the
  controlling process.

## References

Progressive disclosure: keep `SKILL.md` as the routing surface and load only
the smallest reference that matches the current Word task and risk level:

| File | Load when |
| --- | --- |
| `references/setup.md` | First use, state-root consent, or safety-default capture |
| `references/execution-matrix.md` | Choosing attach / launch / save-copy-first or live vs `word-docx` |
| `references/live-control-patterns.md` | Building bounded Word `osascript` read/write/export scripts |
| `references/safety-checklist.md` | Before accept/reject-all, bulk cleanup, close-without-save, overwrite |
| `references/troubleshooting.md` | Attach failures, wrong selection, silent review errors, stale PDF export |
| `references/sources.md` | Verifying Word/osascript domain claims against primary docs |
| `assets/data-templates.md` | Copying memory/incidents/document-notes skeletons into `<state_root>` |

## Core rules

1. **Choose the app-control path by document state.** Use `osascript` for live
   Word dictionary control. Keep automation inside the live session when the
   requested job depends on current app state; route offline structural DOCX
   work to `word-docx` via `references/execution-matrix.md`.
2. **Identify the exact document and view before acting.** Confirm whether the
   target is the active document, a named open document, or a path to open now.
   Read the current view, selection, and review mode before edits tied to cursor
   position or markup. Verify the frontmost Word window is the intended document.
3. **Read before write, then verify the final state.** Pre-read document name,
   selection, target paragraph, comment count, or export target before mutation.
   After edits, comments, accept/reject actions, or exports, re-read the affected
   state and report what changed. If Word does not reach the requested state,
   diagnose instead of layering more edits.
4. **Treat selection-driven actions as high-risk.** Selection commands can land
   in the wrong paragraph, story range, header, or comment balloon. Prefer
   object-based anchors over the bare insertion point. If selection context is
   ambiguous, clarify first.
5. **Separate reversible review actions from destructive cleanup.** Comments,
   view changes, and exports are usually reversible. Accept all / reject all /
   remove comments / close without save / overwrite exports require explicit
   confirmation per `references/safety-checklist.md`. Preserve track changes and
   display settings unless the user explicitly asks to change them.
6. **Keep provenance explicit.** State whether the target was already open or
   opened for this task. Report the document changed, the review mode in force,
   and where exports were written. Preserve user-owned open documents outside
   the task scope.
7. **Recover cleanly and leave attached sessions intact.** If you opened Word
   for this task, close only what you created. If you attached to an existing
   session, keep unrelated documents open and leave Word running unless the user
   explicitly approves quitting. On failure, record the exact blocker: protected
   document, modal dialog, compatibility mode, track changes mismatch, or missing
   permissions; append durable notes to `<state_root>/incidents.md` only after
   consent.

## Word traps

- Treating a live document like a static `.docx` file → review state, comments,
  fields, and view context drift apart.
- Writing relative to the current cursor without verifying selection → text lands
  in the wrong story range.
- Accepting or rejecting changes globally when only one section was intended →
  irreversible editorial loss.
- Exporting before fields, references, or TOC are updated → stale output delivered
  as final.
- Closing an attached user session after automation → unrelated writing work is
  interrupted.
- Ignoring protected view or tracked-change mode → edits silently fail or create
  the wrong markup history.
- Guessing Word dictionary terms → prefer short verified scripts and
  `applescript` dictionary discovery when terminology is unknown.

## Security and privacy

**Data that stays local:** document paths, environment notes, reusable fixes under
`<state_root>/`, and document contents accessed through local Word automation.

**Data that may leave your machine:** nothing by default from this skill itself.
A document's own links, add-ins, macros, or cloud-backed autosave behavior may
contact external systems.

**This skill does not:**

- Use Microsoft Graph, cloud document APIs, or OAuth flows.
- Disable review warnings silently.
- Accept destructive document-wide changes without explicit confirmation.
- Bypass Word protection prompts.
- Lower the mandatory confirmation floor via memory preferences.
