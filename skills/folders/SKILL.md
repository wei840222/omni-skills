---
name: folders
description: Find, index, organize, or clean up project folders and build artifacts safely. Use when the user asks where a directory is, wants a folder inventory, or requests a folder operation.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📂"}'
---

## Choose the task path

- **Locate:** resolve the existing index first, then run targeted discovery for an index miss.
- **Inventory:** search only the user-named or user-relevant roots and present the findings before indexing them.
- **Index:** show the exact records and state root, then save only the user-confirmed change.
- **Organize or clean up:** inspect canonical targets, present effects and recovery, then complete the confirmed operation through the trash or recycle bin when removal is requested.

Read [references/index-and-discovery.md](references/index-and-discovery.md) before locating, inventorying, or indexing folders. Read [references/safe-operations.md](references/safe-operations.md) before organizing, moving, or removing anything.

## Outcome checks

- A lookup reports either matching canonical paths or that no match was found in the checked locations.
- An index update reports the selected state root and the exact added, changed, or removed record.
- A folder operation reports every affected path, whether it was completed, and its recovery method.
- If path resolution, permission checks, or the requested confirmation fails, leave the filesystem and index unchanged and explain the blocking condition.
