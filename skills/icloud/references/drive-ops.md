# iCloud Drive operations — iCloud

Use the modern `api.drive` surface. If a legacy `api.files` call returns
`Account migrated`, switch to `api.drive` (Apple migrated the account).

## Read-only preflight

```bash
python3 - <<'PY'
import getpass
from pyicloud import PyiCloudService

user = input("Apple ID: ").strip()
pwd = getpass.getpass("Apple password: ")
api = PyiCloudService(user, pwd)
print(api.drive.dir())
PY
```

If keyring/session is unavailable, recover auth first from
`references/auth-session.md`.

## Safe download pattern

1. Resolve the exact folder and filename from a read listing.
2. Download one file.
3. Verify local size (and hash when available) before continuing a batch.

## Safe upload pattern

1. Confirm destination folder and overwrite expectations.
2. Upload one file first.
3. Re-list the folder and verify file metadata.

## Write guardrails

- Require explicit confirmation before delete or rename.
- Run broad path modifications only after a pre-action snapshot listing.
- Keep operations to one verified path per step when possible.
