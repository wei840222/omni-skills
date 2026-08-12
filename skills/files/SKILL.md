---
name: files
description: Safely organize directories, find duplicate files, and run confirmed bulk rename, move, or cleanup operations. Use for reorganization, disk-space analysis, and deduplication; use normal file tooling for ordinary file creation, copying, extraction, or one-file reads.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📁"}'
---

## State location

File-operation state may exist in `<workspace>/files/`, `<workspace>/memory/files/`, or `~/files/`. Before an operation needs an undo record or hash cache, resolve one `<state_root>`:

1. Use a user- or host-configured state path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/files/`, `<workspace>/memory/files/`, `~/files/`.
3. If multiple candidates exist, use only the highest-precedence directory, report split state, and leave lower-precedence directories unchanged.
4. If none exists, show the proposed `<workspace>/files/` location and create it only after the user confirms persistent operation state.
5. If the host cannot provide `<workspace>`, use an existing `~/files/` only; otherwise ask for a state location before creating state.

Keep `<state_root>` fixed for the operation. It stores only operation metadata:

```text
<state_root>/
├── undo/<operation-id>.json  # planned and completed recoverable mutations
└── cache/hashes.jsonl        # optional digest cache keyed by path, size, and mtime
```

## Workflow

1. **Classify the request.** Use this skill only for directory analysis, duplicate detection, bulk rename/move, or cleanup. For one ordinary create, copy, extract, or read operation, use the host's normal file tooling instead.
2. **Establish the boundary.** Ask for the target when it is ambiguous. Normalize `~`, `.`, and `..`; inspect filesystem entries without following symlinks; then verify every selected target is inside the user-approved directory. `/`, OS directories, and the user's home directory as a bulk target require a narrower path.
3. **Inspect before mutating.** Report the candidate count, total size, operation type, affected paths or a paginated manifest, destination, and recovery method. For duplicates, use size grouping, a small-content digest filter, then a full digest before treating files as identical.
4. **Obtain explicit confirmation.** Every mutation—rename, move, trash, permanent deletion, state creation, manifest creation, or symlink traversal—requires confirmation after the preview. A permanent deletion requires the user to say `permanently delete` or `empty trash`.
5. **Execute in recoverable units.** After confirmation, create `<state_root>/undo/<operation-id>.json`, perform one item at a time, record each committed result, and stop on the first unexpected error. Do not claim a completed batch when a partial failure occurred.
6. **Report and recover.** State the changed, skipped, and failed paths; give the operation ID; and offer `undo <operation-id>` when the operation was recoverable.

## Safety rules

- Treat symlinks as traversal boundaries. Report each link and its target; follow one only after the user confirms that specific resolved target remains in scope.
- Keep project and user data inside the approved target boundary. If canonicalization resolves a selected entry outside that boundary, exclude it and explain why.
- For a confirmed cleanup, prefer the host's native trash interface. If unavailable, ask the user to approve a recoverable trash location under `<state_root>/trash/`; do not permanently delete as a fallback.
- Preserve original filenames unless a confirmed rename rule says otherwise.
- Store metadata, paths, timestamps, and digests in operation state; do not copy file content, credentials, or private file text into state.

## Scale and failure handling

| Condition | Required behavior |
| --- | --- |
| 1–9 planned mutations | Show each path and request confirmation. |
| 10–10,000 planned mutations | Show a summary plus a paginated manifest and request confirmation. |
| More than 10,000 planned mutations | Require the user to explicitly acknowledge the count before proceeding. |
| Manifest too large to display | Show the first and last 10 entries, total count, and page the remainder. |
| Destination lacks space or access | Stop before the first mutation and report the failed preflight check. |
| A mutation fails after earlier items succeed | Stop, preserve the undo record, list committed and failed items, and offer undo for committed items. |
| Duplicate candidates share size and prefix digest but differ on full digest | Keep both files and report that the quick filter was inconclusive. |

## Operating details

- **Organization:** inspect the directory before proposing groups; show concrete source → destination examples; create an operation manifest in `<state_root>/undo/<operation-id>.json`, not silently in the user's destination.
- **Batch rename:** preview every rename for up to 50 files; for larger batches show the first and last 10 plus total count. Detect destination-name collisions before writing.
- **Batch move:** preflight destination space and access; record each completed move in the undo record so a later failure can be recovered.
- **Duplicate cleanup:** retain one selected canonical copy, state the selection rule in the preview, and move only confirmed duplicate copies to recoverable trash.
- **Disk analysis:** report top directories, actual versus apparent size when the host can provide both, and classify cleanup suggestions by recoverability. Analysis alone does not create state.
- **Hash cache:** use it only as an optimization after `<state_root>` exists; invalidate an entry when its path, size, or mtime differs from the current file.

## Reference routing

- Read `references/knowledge-sources.md` only when explaining the digest or trash-standard basis for this skill's safety choices.
