---
name: cloud
description: >
  Choose, organize, sync, share, and back up personal files across iCloud,
  Google Drive, Dropbox, and OneDrive. Use for consumer storage-full cleanup,
  photo backup setup, cross-device sync confusions, family sharing links, and
  plan comparisons—not object-store transfers (`cloud-storage`), backup
  architecture (`backups`), or storage system design (`storage`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"☁️","displayName":"Cloud"}'
  related-skills: '{"cloud-storage":"Provider upload/download/sync ops and egress cost across object stores and drives.","backups":"3-2-1-1-0 backup architecture and verified restore drills.","storage":"Application storage architecture beyond consumer file sync.","icloud":"Authenticated local iCloud Drive/Photos/Find My operations.","s3":"S3-compatible object storage deep dive outside consumer plans."}'
---

## When to use

Consumer cloud storage questions: iCloud/Google Drive/Dropbox/OneDrive full,
photo backups, device sync surprises, share-link setup, plan comparison, and
what not to store unencrypted in the cloud.

Prefer adjacent skills when they fit better:

- Bulk object-store / multi-provider file ops and cost → `cloud-storage`
- Backup policy, immutability, restore testing → `backups`
- App/database/object/block architecture → `storage`
- Local authenticated iCloud Drive/Photos/Find My actions → `icloud`
- S3 lifecycle, CORS, presign → `s3`

## Stateless

This skill is knowledge-only. It does not create a local persistent state tree.
Do not write runtime notes into this package.

## Progressive disclosure

| Need | Load |
|------|------|
| Scope, confusions, security basics | `references/domain.md` |
| Plan comparison and switching | `references/services.md` |
| Freeing space per provider | `references/cleanup.md` |
| 3-2-1 backup and sensitive data | `references/backup.md` |
| Share links and permissions | `references/sharing.md` |
| Official pricing / docs anchors | `references/sources.md` |

## Core workflows

**Storage full:** separate device storage from cloud quota → open the provider
usage page → empty trash / Recently Deleted → stop duplicate photo backups →
offload archives. Use `references/cleanup.md`.

**Pick a primary service:** match the device ecosystem in
`references/domain.md`, confirm live tiers in `references/services.md` +
`references/sources.md`, cancel redundant paid plans after download.

**Photo backup:** choose exactly one auto-upload service; disable the others;
verify “backed up” status monthly (`references/backup.md`).

**Share a file:** minimum permission, expiration when available, encrypt
sensitive docs first (`references/sharing.md`).

## Critical rules

1. **Phone storage ≠ cloud quota** — iCloud/Drive full can happen while the
   device still has free space.
2. **One photo backup service** — multiple auto-uploads create duplicates and
   burn quota.
3. **Deleted ≠ gone** — empty trash / Recently Deleted on every provider.
4. **Encrypt before storing IDs, financial, or medical scans** — or keep them
   off cloud links entirely.
5. **Re-open live pricing pages** before quoting plan prices
   (`references/sources.md`); marketing pages change.
6. **Route deep specialties** — do not re-implement `cloud-storage`,
   `backups`, `storage`, or authenticated `icloud` ops here.
