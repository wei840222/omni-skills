# Authentication and session — iCloud

Minimize auth errors and keep credentials off chat transcripts.

Pinned client for this skill: `pyicloud==2026.10.1` (requires Python ≥ 3.10).
See `references/sources.md` for the PyPI / GitHub anchors.

## Safe authentication sequence

1. Verify dependency import:

```bash
python3 - <<'PY'
from pyicloud import PyiCloudService
print("pyicloud import OK")
PY
```

2. Start login with local prompts only:

```bash
python3 - <<'PY'
import getpass
from pyicloud import PyiCloudService

user = input("Apple ID: ").strip()
pwd = getpass.getpass("Apple password: ")
# China mainland Apple ID region: pass china_mainland=True
api = PyiCloudService(user, pwd)
print("Session loaded:", bool(getattr(api, "data", None) is not None or api.requires_2fa or api.requires_2sa))
print("requires_2fa:", getattr(api, "requires_2fa", False))
print("requires_2sa:", getattr(api, "requires_2sa", False))
PY
```

3. If 2FA / 2SA is required, complete the code in the same local prompt flow
   (never paste the code into chat). Follow the maintained Authentication guide
   for `validate_2fa_code` / trusted-session steps:
   https://github.com/timlaing/pyicloud/blob/main/docs/guides/authentication.md

4. Optional: store the password in the system keyring via the `icloud` CLI.
   Keep secrets out of plain-text files under `<state_root>/`.

5. Re-run a read-only command (device list or Drive `dir`) to confirm the
   trusted session is active before any write.

## China mainland accounts

Pass `china_mainland=True` so auth/bootstrap use the `.apple.com.cn` /
`.icloud.com.cn` endpoints documented by pyicloud.

## Long-running sessions

For daemons, configure `refresh_interval` (default 5 minutes) or disable the
background monitor with `refresh_interval=None`. Still treat sudden auth failures
as a normal state: pause writes and re-auth.

## Session failure recovery

| Symptom | Cause | Safe recovery |
|---------|-------|---------------|
| Auth/API failures after earlier success | Session expired | Re-auth with the same local flow |
| 2FA loop repeats | Session not trusted | Complete trust step; retry a read-only command |
| Unexpected password prompt | Missing keyring entry | Interactive re-auth, then continue |

## Hard boundaries

- Collect passwords and 2FA codes only through interactive local prompts.
- Keep credential material out of `<state_root>/` files and chat logs.
- Stop write operations immediately when session health is uncertain.
