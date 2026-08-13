---
name: folders
description: Find, index, organize, or clean up project folders and build artifacts safely. Use when the user asks where a directory is, wants a folder inventory, or requests a folder operation.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📂"}'
---

## Workflow

1. Clarify the requested outcome: locate, inventory, index, organize, or remove a folder or artifact.
2. For lookups, resolve the existing folder index first. If it has no match, run targeted discovery rather than a broad filesystem scan.
3. Before changing an index, moving content, or removing content, present the exact targets, expected effects, and recovery path; proceed only after the user confirms.
4. For a deletion request, use the platform trash or recycle bin. State what can be restored and what can be regenerated.

Read [references/index-and-discovery.md](references/index-and-discovery.md) before resolving state, searching for folders, or editing the index. Read [references/safe-operations.md](references/safe-operations.md) before moving or removing anything.

## Outcome checks

- A lookup reports either matching canonical paths or that no match was found in the checked locations.
- An index update reports the selected state root and the exact added, changed, or removed record.
- A folder operation reports every affected path, whether it was completed, and its recovery method.
- If path resolution, permission checks, or the requested confirmation fails, leave the filesystem and index unchanged and explain the blocking condition.
