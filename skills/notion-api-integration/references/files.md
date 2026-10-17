# Files — Upload, Attach, and Expiring URLs

Notion-hosted file URLs returned by the API are signed and short-lived. Store block/file ids, never the URL, under `<state_root>/`.

**Contents:** [Upload methods](#upload-methods) · [Size limits](#size-limits) · [Attach](#attach) · [Retrieve](#retrieve) · [Traps](#traps)

## Upload methods

1. **Direct upload** (≤ 20 MiB) — multipart send after creating a file upload object.
2. **Multi-part direct upload** — required above 20 MiB.
3. **Indirect import** — import from a publicly reachable URL (migrations).

Supported media attaches to `file` / `image` / `pdf` / `audio` / `video` blocks, `files` properties, and page icon/cover (type constraints still apply).

## Size limits

From official Working with files and media (live-checked 2026-10-17):

- Free workspaces: **5 MiB** per file.
- Paid workspaces: up to **5 GiB** per file.
- API multi-part required above **20 MiB**.
- Filename length max **900 bytes** (prefer shorter).

Read `bot.workspace_limits.max_file_upload_size_in_bytes` when the plan is unknown.

## Attach

After upload completes, attach the returned file reference to the target block or `files` property. Do not invent property write shapes — mirror `references/properties.md`.

## Retrieve

When a previously saved URL returns 403, refetch the block/property for a fresh signed URL. Persistence key = block id or file upload id.

## Traps

- Storing signed URLs in mappings or runbooks.
- Using a video MIME on an image block (or PDF as icon).
- Ignoring plan-based size limits until validation_error.

Official source: Working with files and media.
