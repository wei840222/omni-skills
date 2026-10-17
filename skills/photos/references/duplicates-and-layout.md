# Duplicates and File Organization

Load when grouping near-duplicates or proposing library layout/renames.

## Duplicate detection

1. Compute a content hash for identity and a perceptual hash (pHash) for
   near-duplicates / resized copies.
2. Group by pHash similarity.
3. Prefer the highest-resolution file as "original"; break ties with the oldest
   EXIF `DateTimeOriginal`.
4. Present paths (and thumbnails when available) for user review.
5. Stage rejects under trash only after confirmation — never auto-delete.

## Layout proposals

Propose, do not impose:

- Folders: `YYYY/MM/` or `YYYY/MM-DD/`
- Rename: `YYYYMMDD_HHMMSS_originalname.ext`

Write the plan to `<state_root>/photos-pending.json` before moving files.

## Manifest shape (illustrative)

```json
{
  "library": "/Volumes/photos",
  "actions": [
    {
      "op": "rename",
      "from": "IMG_0001.HEIC",
      "to": "20240315_143000_IMG_0001.HEIC"
    }
  ]
}
```

Apply only approved rows. Leave unapproved rows untouched.
