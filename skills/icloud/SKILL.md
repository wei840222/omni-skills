---
name: icloud
description: >
  Operate a personal iCloud account for Find My device discovery, iCloud Drive
  listing/transfer, and Photos album inspection through local pyicloud auth with
  interactive 2FA. Use when listing devices by stable ID, playing a sound or
  enabling Lost Mode after confirmation, downloading or uploading a single Drive
  path, or sampling Photos albums — never for chat-pasted Apple passwords or
  bypassing Apple security. Prefer `photos` for local library indexing,
  `cloud-storage` for cross-provider transfers, and `ios`/`macos` for device
  settings outside the iCloud web session.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"☁️","requires":{"bins":["python3"]},"install":[{"id":"pyicloud","kind":"pip","package":"pyicloud==2026.10.1","label":"Install pyicloud 2026.10.1 (pip)"}]}'
  related-skills: '{"cloud-storage": "Cross-provider storage workflows and transfer safety when the work spans Drive plus another provider.", "ios": "Apple device settings, permissions, and account behavior outside the iCloud web session.", "macos": "macOS keychain, SIP, and local runtime diagnostics for Apple tooling.", "photos": "Local photo-library indexing and EXIF-safe organization when the workload is not iCloud Photos API access."}'
---

# iCloud

Operate **your own** iCloud account through `pyicloud`: Find My device IDs,
Drive path listing/transfer, and Photos album inspection. Auth stays on the
local terminal; risky writes need an explicit confirmation gate and a second
read-back.

## State location

Optional operational notes are persistent user state. Resolve `<state_root>`
once per invocation before any read or write:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/icloud/`, `<workspace>/memory/icloud/`, then `~/icloud/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicates; do not merge them.
4. If none exists and the user confirms saving operational notes, create
   `<workspace>/icloud/`. If `<workspace>` is unavailable, ask for a state root
   instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation. Never write the literal string
   `<state_root>` to disk.

```text
<state_root>/
|-- memory.md           # Status, integration mode, account scope (no secrets)
|-- operations-log.md   # Executed commands, result checks, rollback notes
|-- device-map.md       # Known device aliases and stable IDs
|-- drive-map.md        # Verified iCloud Drive roots and paths
`-- safety-events.md    # Confirmed risky actions and explicit approvals
```

If older notes exist under a legacy Clawic iCloud data directory, migrate them
into the resolved `<state_root>/` on first write and say in one line that you
moved them and from where. Seed new memory from `assets/memory-template.md`.

## When to use

- List Find My devices and map display names to stable device IDs
- Play a sound, display a message, or enable Lost Mode after confirmation
- Inspect iCloud Drive folders; download or upload one verified path
- List Photos albums / sample one asset before any bulk download
- Recover from expired sessions or 2FA challenges with local prompts only

Prefer other skills when the ask is mainly:

- local photo library indexing / EXIF / duplicates → `photos`
- cross-provider copy or transfer policy → `cloud-storage`
- device settings, permissions, or App Review → `ios`
- keychain / SIP / launchd diagnostics → `macos`

## Progressive disclosure

| Topic | File | Load when |
|-------|------|-----------|
| First activation / install | `references/setup.md` | No `<state_root>/memory.md`, missing `pyicloud`, or first session |
| Memory template | `assets/memory-template.md` | Creating or reshaping `<state_root>/memory.md` |
| Auth / 2FA / session | `references/auth-session.md` | Login, 2FA, China mainland accounts, session expiry |
| Find My actions | `references/findmy-ops.md` | Device list, locate, play sound, Lost Mode |
| Drive operations | `references/drive-ops.md` | Drive listing, download, upload, rename/delete gates |
| Photos operations | `references/photos-ops.md` | Album list, sample download, bulk-download gates |
| Confirmation gates | `references/safety-boundaries.md` | Any risky write or bulk action |
| Verified sources | `references/sources.md` | Before changing the pyicloud pin, endpoints, or API claims |

## Core rules

1. **Local auth only** — Collect Apple ID, password, and 2FA codes through
   interactive local prompts (`input` / `getpass` / host-secure prompt). Keep
   credentials out of chat logs and out of `<state_root>/`.
2. **Read first** — Discover account reachability, device list, folder listing,
   or album metadata before any write.
3. **Confirm risky writes** — Lost Mode, display message, play sound, erase,
   Drive rename/delete, and bulk Photos download need an explicit confirmation
   that names the target ID/path, effect, and rollback note.
4. **Verify by re-read** — After every mutation, run a second read and report
   from that evidence. Exit codes alone are not success.
5. **Narrow scope** — Prefer one device ID or one Drive path per step. Avoid
   wildcard bulk mutations.
6. **Treat auth expiry as normal** — On session failure, pause writes, re-auth
   locally, then resume only after a successful read check.
7. **Minimal persistence** — Store only stable IDs, verified paths, and last-good
   patterns under `<state_root>/`. Never store passwords, tokens, or 2FA codes.

## Common traps

- Pasting an Apple password or 2FA code into chat
- Targeting a device by display name when two devices share a similar name
- Calling legacy `api.files` after Apple migrated the account to iCloud Drive
  (`Account migrated` → use `api.drive`)
- Pinning an obsolete `pyicloud` wheel while the maintained package has moved on
- Claiming success from a command exit code without a post-action listing
- Bulk Drive/Photos changes without a pre-action snapshot

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| `https://idmsa.apple.com` | Apple account auth during login | Apple ID authentication |
| `https://setup.icloud.com` | Session / webservice negotiation | iCloud bootstrap |
| `https://www.icloud.com` | Service API requests | Drive / Photos / Find My |
| `https://idmsa.apple.com.cn` | Auth payload (China mainland) | Regional Apple ID auth |
| `https://setup.icloud.com.cn` | Session negotiation (China mainland) | Regional bootstrap |
| `https://pypi.org` / `https://files.pythonhosted.org` | Package metadata/download | Install `pyicloud` only |

No other external destinations are part of this skill's documented workflow.

## Security & trust

Data that leaves the machine: Apple authentication and the iCloud API calls
needed for the requested operation, plus optional package install traffic.

Data that stays local: optional notes under `<state_root>/`, and keyring entries
if the user opts into password storage via `pyicloud` / the `icloud` CLI.

This skill does not bypass Apple 2FA, request undeclared credentials in chat, or
modify its own package files at runtime. Using it means trusting Apple iCloud
endpoints and the `pyicloud` package for the requested personal-account work.
