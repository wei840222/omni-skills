# EXIF Handling and Format Conversion

Load for ExifTool commands, GPS stripping, and HEIC conversion.

## Read

```bash
exiftool -json photo.jpg
exiftool -json -r /path/to/photos/
```

`-json` / `-j` emits machine-readable tags. Recursive `-r` returns an array.

## Write dates (prefer copies)

```bash
exiftool -DateTimeOriginal="2024:03:15 14:30:00" -o edited/photo.jpg photo.jpg
```

ExifTool's default write mode keeps a `*_original` backup beside the source.
Use `-overwrite_original` only after the user confirms the backup strategy.

## Strip GPS for sharing

```bash
exiftool -gps:all= -o share/photo.jpg photo.jpg
```

Operate on a copy. Clearing GPS in-place without a reviewed backup is forbidden
by this skill's mutation boundary.

## HEIC → JPEG

- macOS: `sips -s format jpeg input.heic --out output.jpg`
- Linux: `heif-convert input.heic output.jpg` (libheif)

Keep the HEIC original; write JPEG under `edited/` or an explicit output path.

## Timezone

EXIF capture times are usually local camera time without a reliable offset.
Ask once, store in `<state_root>/config.json`, and apply that offset when
proposing `YYYY/MM/` or `YYYYMMDD_HHMMSS_` names.
