# Photos operations — iCloud

Access iCloud Photos with explicit album scope and controlled downloads.
Prefer the maintained Photos service / CLI documented by pyicloud for modern
CloudKit-backed libraries.

## Basic access pattern

```bash
python3 - <<'PY'
import getpass
from pyicloud import PyiCloudService

user = input("Apple ID: ").strip()
pwd = getpass.getpass("Apple password: ")
api = PyiCloudService(user, pwd)
albums = list(api.photos.albums.keys())
print(albums[:10])
print("album_count:", len(albums))
PY
```

## Download safety pattern

1. Select an album and sample one asset first.
2. Download the requested variant (`original`, `thumb`, or equivalent).
3. Verify file integrity before scaling up.
4. Treat bulk download as a risky write: confirm destination path and quota.

## Reliability checks

| Check | Why it matters |
|-------|----------------|
| Album exists before iteration | Prevents null/empty loops |
| Asset count matches expectation | Avoids partial assumptions |
| Version choice is explicit | Prevents wrong-quality output |

## Boundaries

- Bulk download only after a user-approved destination and quota check.
- Keep remote photo deletion out of this workflow.
- For organizing a **local** library (EXIF, duplicates, rename plans), hand off
  to the `photos` skill.
