# Find My operations — iCloud

Use Find My workflows with stable device IDs and explicit confirmation.

## Read-only discovery

```bash
python3 - <<'PY'
import getpass
from pyicloud import PyiCloudService

user = input("Apple ID: ").strip()
pwd = getpass.getpass("Apple password: ")
api = PyiCloudService(user, pwd, with_family=True)
for dev_id, dev in api.devices.items():
    content = getattr(dev, "content", {}) or {}
    print(dev_id, content.get("name") or dev)
PY
```

Persist only stable identifiers (device ID ↔ display-name mapping) under
`<state_root>/device-map.md` after consent.

Access a device by ID (preferred) or index. Do not rely on display name alone
when more than one device could match.

## Controlled actions

Treat these as risky writes:

- `play_sound()`
- `display_message(...)`
- `lost_device(...)` / Lost Mode
- erase / remote wipe equivalents exposed by the client

Before any risky action, confirm with the user:

1. exact device ID,
2. action effect,
3. rollback / recovery expectation.

## Post-action verification

1. Re-run the read-only device listing.
2. Validate the target device state from that listing.
3. Append a concise result line to `<state_root>/operations-log.md` when
   persistence is enabled.

## Failure pattern

Name-only targeting causes wrong-device actions → always resolve and confirm
the device ID first.
