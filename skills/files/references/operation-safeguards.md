# Extended file-operation safeguards

Read this reference before planning or executing a bulk rename, move, cleanup, or undo. Also read the relevant sections before suggesting cleanup from disk analysis, operating across a mount or platform boundary, or handling more than 10,000 candidates. These rules add operational detail to `SKILL.md`; they do not relax its confirmation or state-location requirements.

## Boundary and platform safeguards

- Canonicalize each approved path before selecting it. If canonicalization cannot complete, do not mutate that entry. A symlink remains a boundary until the user approves its specific resolved target and that target is inside the approved scope.
- Never use `/`, `/etc`, `/var`, `/usr`, `/System`, `/Library`, `C:\\Windows`, or `C:\\Program Files` as a bulk-operation target. Ask for a data-only subdirectory instead. The user's home directory also needs a narrower approved path before a bulk operation.
- On macOS, treat an `.app` bundle as one application package. Do not reorganize its internal contents unless the user explicitly scopes that bundle and confirms the consequence.
- On Windows, use the host's supported filesystem and Recycle Bin interfaces; long-path handling is host-specific, so do not construct a `\\\\?\\` path prefix speculatively.
- On Linux, native trash behavior can vary across filesystems. Prefer the host-provided trash interface; if it cannot preserve recovery information, use the confirmed `<state_root>/trash/` fallback from `SKILL.md`.
- For a remote or otherwise unreliable filesystem reported by the host, warn that rename, trash, and undo may not be atomic. Do not suggest a local copy or perform a retry as part of the operation without a new preview and confirmation.

## Recoverability and partial failures

Before the first mutation, the undo record should identify the operation, creation time, confirmed source and destination paths, completed-item results, and any available digest used for verification. Keep undo records for up to 30 days unless the user directs otherwise; warn before a planned retention cleanup removes a recoverable record. JSON metadata is sufficient—do not generate or execute shell undo scripts.

If an item fails after earlier items succeed, stop by default, retain the record, and report the completed, skipped, and failed sets. An agent may resume by skipping named failures only after showing the revised set and obtaining a new confirmation. It must not silently continue a failed batch or promise rollback that the host cannot perform.

## Scale, progress, and capacity

- For 1–9 mutations, show every proposed path and obtain the confirmation required by `SKILL.md`; the small size is not permission to skip confirmation.
- For 10–10,000 mutations, use a paginated manifest. If the manifest would be large (for example, over 10 MB), show the first and last 10 entries, total count, and page the rest.
- Above 10,000 mutations, require an explicit count acknowledgement. Above 100,000, require the user to acknowledge the exact impact with `I understand` before execution.
- Preflight destination access and capacity before moving data. Preserve at least 1% free-space headroom when the host can report capacity; otherwise state that capacity was not verifiable and do not claim the check passed.
- During a long confirmed batch, update at the less-frequent cadence of every 5% completed or every 30 seconds. Avoid per-file progress messages unless the user asks for them.

## Operation-specific detail

- **Organization:** inspect composition before proposing groups, state the grouping rule, and show concrete source-to-destination examples. Preserve filenames unless the confirmed rule changes them.
- **Batch rename:** detect destination collisions before writing. A collision is a blocker, not a reason to overwrite or auto-suffix names.
- **Duplicate cleanup:** explain the canonical-copy rule before trashing any candidate. Size and a small-content digest are filters only; a full digest is required before files are called duplicates.
- **Disk analysis:** report top directories before individual files when possible, distinguish actual and apparent size when the host provides both, and label every suggestion as read-only, recoverable, or irreversible.
- **Rebuildable directories:** entries such as `node_modules`, `__pycache__`, `.gradle`, `build`, `target`, and `Pods` can sometimes be regenerated, but directory names alone do not prove that deletion is safe. Verify project context, explain the recovery command or method, and still request confirmation.
