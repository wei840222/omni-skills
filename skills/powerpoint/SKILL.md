---
name: powerpoint
description: >
  Control Microsoft PowerPoint live app sessions on macOS via osascript:
  attach/launch, identify active presentation and slide, read/write slides and
  notes, export PDF from the live deck, start/stop slideshow, and recover clean
  session ownership. Use when the job depends on an open PowerPoint window or
  presenter state. Prefer `powerpoint-pptx` for offline PPTX generation or
  structural file edits; `applescript` for deeper dictionary design; `office`
  for cross-app Office routing; `documents` for general document prep that
  feeds a deck.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📽️","os":["darwin"],"requires":{"bins":["osascript"]}}'
  related-skills: '{"applescript":"Deeper AppleScript/dictionary design beyond known-good PowerPoint snippets.","documents":"General document prep workflows that often feed deck content.","office":"Cross-app Office routing across documents, spreadsheets, and presentations.","powerpoint-pptx":"Offline PPTX generation and structural file editing without a live app session."}'
---

# PowerPoint

Own **live Microsoft PowerPoint control on macOS** through `osascript` and the app scripting dictionary: session attach, presentation/slide identity, notes, export, slideshow, and clean recovery. This skill does not rebuild decks as static `.pptx` files.

## State location

PowerPoint state may exist in `<workspace>/powerpoint/`, `<workspace>/memory/powerpoint/`, or `~/powerpoint/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/powerpoint/`, `<workspace>/memory/powerpoint/`, `~/powerpoint/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and state must be created, default to `<workspace>/powerpoint/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/powerpoint/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Do not treat the literal string `<state_root>` as a filesystem path. Do not write presentation body content, passwords, cloud tokens, or learned preferences into `SKILL.md` or package files.

Default note files (create on first authorized write):

| File | Purpose |
| --- | --- |
| `<state_root>/memory.md` | Environment facts, safe defaults, last working control path |
| `<state_root>/incidents.md` | Reusable failures and proven recovery steps |
| `<state_root>/deck-notes.md` | Non-sensitive identifiers, paths, layout quirks, export targets |

Load `references/memory-template.md` for templates. Load `references/setup.md` only when onboarding or `<state_root>` is empty.

## When to use

- Deck is already open in Microsoft PowerPoint and the job needs live app state
- Read or update slides, notes, or view/slideshow state through the app
- Export PDF (or similar) that must match the current live rendering
- Start/stop slideshow or presenter-adjacent control
- Recover from attach ambiguity, wrong slide, modal dialogs, or orphaned sessions

Prefer adjacent skills when they fit better:

- Offline PPTX create/edit without a live window → `powerpoint-pptx`
- Deeper AppleScript design beyond known-good snippets → `applescript`
- Cross-app Office routing → `office`
- General document prep feeding a deck → `documents`

## Workflow

1. Classify: attach-existing vs launch-new vs save-copy-first (see `references/execution-matrix.md`).
2. Resolve `<state_root>` only when memory/incidents matter; otherwise stay stateless for one-shot reads.
3. Preflight the lowest-risk read: PowerPoint running → open presentations count → active presentation name → active slide index/view.
4. One mutation → one verification (re-read name, slide index, notes, export path, or slideshow state).
5. Re-open `references/sources.md` before restating version-sensitive PowerPoint dictionary or export claims.
6. End with provenance: which deck, which slide, attach vs launched, export path, what stayed open.

| Need | Load |
| --- | --- |
| Interface selection by job | `references/execution-matrix.md` |
| Known-good osascript patterns | `references/live-control-patterns.md` |
| Destructive action preflight | `references/safety-checklist.md` |
| Onboarding and activation | `references/setup.md` |
| State file templates | `references/memory-template.md` |
| Failure ladder and recovery | `references/troubleshooting.md` |
| Verified official sources | `references/sources.md` |

## Minimum viable defaults

1. **Live app path first** — use `osascript` against Microsoft PowerPoint when the job depends on current presenter/edit state; do not silently switch to offline PPTX libraries.
2. **Identity before mutation** — confirm presentation name/path and slide index (or ID) before add/move/delete/notes/export.
3. **Read → act → re-read** — exit code 0 is not proof the visible deck reached the requested state.
4. **Separate reversible vs destructive** — view changes, slideshow start/stop, and non-overwrite export are usually reversible; delete slide, bulk notes replace, overwrite export, close-without-save need explicit confirmation.
5. **Session ownership** — if you attached to a user session, keep unrelated decks open and leave PowerPoint running unless quit was approved; if you launched only for this task, close only what you created after reporting results.
6. **Route adjacencies** — file-only PPTX → `powerpoint-pptx`; deep scripting → `applescript`; multi-app Office → `office`.

## Core rules

### 1. Choose the app-control path by presentation state

- Prefer `osascript` for live control through PowerPoint's scripting dictionary.
- Keep automation inside the live session when notes, animations, slideshow, or current view matter.
- Hand off to `powerpoint-pptx` only when the artifact is offline file structure, not live window state.

### 2. Identify the exact presentation, slide, and window before acting

- Confirm active presentation vs named open deck vs path to open now.
- Read slide index, view mode, and slideshow state before mutating or exporting.
- Re-verify frontmost deck identity; do not trust selection alone.

### 3. Read before write, then verify the final state

- Pre-read presentation name, active slide, notes state, or export target.
- After edits, exports, or slideshow commands, re-read the affected state and report it.
- If PowerPoint does not reach the requested state, halt and diagnose instead of stacking actions.

### 4. Treat slide-order and layout actions as high-risk

- Move, duplicate, delete, or reorder can break references, animations, and presenter flow.
- Prefer explicit slide numbers or slide IDs over current selection.
- If slide identity is ambiguous, clarify first.

### 5. Separate reversible view actions from destructive deck cleanup

- View mode, slideshow start/stop, and export-to-new-path are usually reversible.
- Delete slide, overwrite save/export targets, bulk notes replace, close without save, and deck-wide cleanup require explicit confirmation.
- Preserve slide show setup, notes, and speaker flow unless the user asked to change them.

### 6. Keep provenance explicit

- State whether the deck was already open or opened for this task.
- Report presentation changed, active slide, and export destinations.
- Leave user-owned open decks outside the task scope untouched.

### 7. Recover cleanly and prevent orphaned app sessions

- Close only sessions/decks you created for the task, after verification.
- On attach-existing, keep PowerPoint running and unrelated decks open unless quit was approved.
- On failure, record the blocker: missing slide, modal dialog, protected file, unsupported layout, or slideshow mismatch (`references/troubleshooting.md`).

## Failure branches

| Condition | Action |
| --- | --- |
| PowerPoint not running / no presentations | Launch intentionally or wait for an open deck; rerun name/count probe |
| Wrong slide or deck mutated risk | Halt writes; re-read active presentation + slide index; prefer explicit slide refs |
| Slideshow commands no-op | Confirm view/slideshow state first; rerun only after expected deck/slide reported |
| PDF export looks stale | Verify final slide order/notes/view; export only after app reflects final state |
| osascript dictionary/term errors | Shorten script; validate identity; retry after PowerPoint is frontmost with an open deck |
| Modal / protected file | Surface dialog or protection; do not bypass prompts; ask user or stop |

## Safety defaults

- Requires macOS + Microsoft PowerPoint + `osascript` (`darwin`). Document platform honestly.
- No cloud slide APIs or OAuth from this skill. Linked media / autosave / add-ins may still contact external systems via PowerPoint itself—report when relevant.
- Do not disable presentation warnings silently or bypass protection prompts.
- Keep writes inside resolved `<state_root>/` with consent; never commit runtime memory into the package.
- Load at most one deep reference per step; keep always-on defaults in this file only.

## PowerPoint traps

- Treating a live deck like a static `.pptx` → notes, presenter state, animations, and export context drift.
- Reordering/deleting without verifying the active deck → wrong presentation altered.
- Editing by current selection only → wrong slide or shape.
- Exporting before notes/slide numbers/final view are verified → stale output delivered as final.
- Closing an attached user session after automation → unrelated work interrupted.
- Ignoring slideshow state → commands hit edit view instead of presenter view.
