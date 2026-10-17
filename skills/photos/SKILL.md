---
name: photos
description: >
  Organize, index, and search local photo libraries with EXIF-safe metadata,
  perceptual-hash duplicate review, vision-assisted descriptions, and
  non-destructive file handling. Use when the user wants to inventory a photo
  folder, find near-duplicates, rename/sort by capture date, strip GPS before
  sharing, convert HEIC, or search by content/date/location/person tags. Prefer
  `photography` for camera technique and exposure advice, `image` /
  `image-edit` for compression or pixel edits, `stock-images` for placeholder
  URLs, `nas` for Synology/QNAP share layout, and `organize` for general
  non-photo directory hygiene.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🖼️","requires":{"bins":["exiftool"]}}'
  related-skills: '{"backups":"Backup retention and restore drills for irreplaceable photo libraries beyond local trash staging.","image":"Compress, convert formats, or optimize delivery after library organization.","image-edit":"Pixel-level edits and non-destructive edit pipelines for a single image.","nas":"Synology/QNAP/TrueNAS share layout, @eaDir quirks, and remote-access hardening for photo volumes.","organize":"General file/folder naming conventions outside photo-library workflows.","photography":"Camera settings, exposure, composition, and capture advice rather than library indexing.","stock-images":"Placeholder and free stock URLs for mockups instead of personal library search."}'
---

# Photos

Index and safely reorganize **local photo libraries**: EXIF reads, sidecar
search, duplicate review, date-based rename proposals, and GPS stripping for
share copies. Prefer manifests and trash staging over in-place deletion.

## State location

Library indexes, manifests, and config are persistent user state. Resolve
`<state_root>` once per invocation before any read or write:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/photos/`, `<workspace>/memory/photos/`, then `~/photos/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicates; do not merge them.
4. If none exists and the user confirms saving index/config state, create
   `<workspace>/photos/`. If `<workspace>` is unavailable, ask for a state root
   instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for skill state. Keep skill resources under
`references/`; never write the literal string `<state_root>` to disk.

Suggested layout:

```text
<state_root>/
├── config.json           # timezone, library roots, batch size
├── .photo-index/         # hash-keyed sidecar JSON (optional colocated)
├── photos-pending.json   # bulk-action manifest awaiting approval
└── .photo-trash/         # staged deletes with original path encoded
```

When the photo library itself is the working root, indexes may also live beside
the images as `<library>/.photo-index/` after the user confirms that location.
Treat that library-local path as an explicit override of `<state_root>` for
index sidecars only; still keep manifests and trash under the resolved
`<state_root>` unless the user asks otherwise.

## Constraints & Safety

- **Deletion boundary** — Move candidates to `<state_root>/.photo-trash/` (or a
  user-approved trash under the library) with the original path preserved in
  the filename or a sidecar; never `rm` originals in the first pass.
- **Mutation boundary** — Pixel edits and derived formats go under an `edited/`
  subfolder (or an explicit output path); leave originals untouched.
- **Bulk gate** — Before bulk rename/move/delete, write
  `<state_root>/photos-pending.json` and wait for user review.
- **Duplicate delete** — Report groups and stage trash only after confirmation;
  auto-emptying trash is out of scope.
- **EXIF writes** — Prefer writing to a copy (`exiftool -o …`) or confirm
  ExifTool's `_original` backup before using `-overwrite_original`.
- **Secrets** — Do not commit GPS tracks, face identities, or private paths into
  the skill package or public logs.

## When to use

- Index or re-index a local/NAS-mounted photo folder
- Search by description, date, GPS/city, or person tags
- Find near-duplicates with perceptual hashing and keep the best original
- Propose `YYYY/MM/` or `YYYYMMDD_HHMMSS_*` organization without forcing it
- Strip GPS from a **share copy** before publishing
- Convert HEIC → JPEG with platform-appropriate tools

## Quick workflow

1. Confirm library root, writable state location, and timezone once.
2. Ensure `exiftool` is available; stop with install guidance if missing.
3. Build or refresh the hash-keyed index incrementally.
4. Run the smallest requested action (search, duplicate review, rename plan).
5. For bulk changes, emit `photos-pending.json`, then apply only approved rows.
6. Hand off capture technique to `photography`, pixel work to `image` /
   `image-edit`, and NAS share design to `nas`.

## Routing

| Need | File |
| --- | --- |
| Index schema, vision cache, search patterns | `references/indexing.md` |
| ExifTool read/write, GPS strip, HEIC convert | `references/exif-and-formats.md` |
| Duplicate grouping and rename/layout proposals | `references/duplicates-and-layout.md` |
| NAS mounts, `@eaDir`, latency | `references/setup.md` |
| Verified Gate 6 sources | `references/sources.md` |

## Core rules

1. Index on demand; cache vision text in sidecars and reuse the cache.
2. Content hash for identity; perceptual hash (pHash) for near-duplicates.
3. Keep highest-resolution / earliest EXIF date as the preferred original in a
   duplicate group unless the user overrides.
4. EXIF dates are local camera time — store the user's timezone in
   `<state_root>/config.json` before bulk rename.
5. Skip Synology `@eaDir` and `.DS_Store` during indexing.
6. Strip GPS only on copies destined for sharing, never as a silent library-wide
   rewrite.

Load the matching reference when a rule needs commands or edge cases.
