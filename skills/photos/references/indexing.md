# Indexing, Vision Cache, and Search

Load when building or querying the photo index.

## Index layout

- Prefer `<library>/.photo-index/` beside the library when the user wants
  portable sidecars, otherwise `<state_root>/.photo-index/`.
- Sidecar name: `{content-hash}.json` so renames do not orphan metadata.
- Minimum fields: `hash`, `phash`, `path`, `date_taken`, `camera`, `gps`,
  `description`, `tags`, `indexed_at`.
- Incremental mode: skip files whose content hash already has a sidecar with the
  same hash.

## Vision analysis

- Defer vision calls until search or an explicit request needs a description.
- Cache the description permanently in the sidecar; do not re-analyze the same
  content hash.
- Batch large jobs (about 20 files) with progress updates.
- Concise prompt: "Describe this photo in 2-3 sentences. List people, objects,
  location, activity."
- Skip likely screenshots/memes (extreme aspect ratio + missing camera EXIF)
  unless the user asks for them.

## Search patterns

| Intent | Approach |
| --- | --- |
| By content | Text-match sidecar `description` / `tags` first; vision only on misses |
| By date | Prefer EXIF `DateTimeOriginal`; fall back to file mtime |
| By location | Reverse-geocode GPS once; store city/country text in the sidecar |
| By person | When the user identifies someone once, tag matching faces in the index |

Store AI descriptions in the sidecar JSON, not by rewriting EXIF description
fields, so originals stay non-destructive.
