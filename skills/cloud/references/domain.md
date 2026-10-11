# Cloud Domain Knowledge

## Triggers

Activate on: iCloud full, cloud storage, backup photos, sync between devices,
share folder, Google Drive help, Dropbox issues, "where are my files", storage
plan comparison.

## Scope

This skill covers **consumer cloud storage** — services people use for photos,
documents, and everyday backups:

- iCloud
- Google Drive (with Gmail / Photos shared quota)
- Dropbox
- OneDrive

**Out of scope:** AWS, Azure, GCS buckets, VPS, Docker, APIs, object-store
lifecycle → use `cloud-storage`, `s3`, `storage`, `infrastructure`, or
`server`. Authenticated local iCloud Drive/Photos/Find My automation → `icloud`.
Backup architecture and restore drills → `backups`.

## Quick service picker

| Your devices | Best fit | Why |
|--------------|----------|-----|
| iPhone + Mac | iCloud | Native integration |
| Android + Chrome | Google Drive | Shared Gmail/Photos quota, auto photo backup |
| Windows PC | OneDrive | Built into Windows, Microsoft 365 tie-in |
| Mixed devices | Dropbox | Cross-platform sync focus |

Confirm live plan tiers in `references/services.md` and
`references/sources.md` before recommending a paid upgrade.

## Common confusions

| What you think | What is actually happening |
|----------------|----------------------------|
| "I deleted it from my phone and now it is gone from my laptop" | Sync is working — one file, everywhere |
| "iCloud storage full but my phone has space" | Phone storage ≠ iCloud storage |
| "My photos are duplicated everywhere" | Multiple services backing up the same camera roll |
| "I pay for 3 cloud services" | Pick one primary; cancel the rest after download |

## Storage full — first response

1. **Check what uses space** — photos usually dominate.
2. **Empty trash / Recently Deleted** — deleted files still count.
3. **Disable duplicate backups** — one photo backup service only.
4. **Offload archives** — move cold files to an external drive.

Service-specific steps: `references/cleanup.md`.

## Backup strategy (consumer)

- **3-2-1:** 3 copies, 2 different media types, 1 offsite.
- Cloud counts as offsite; keep a complementary local copy for lockout risk.
- Verify restore access monthly (open a known photo/doc from another device).

Details and sensitive-data rules: `references/backup.md`. Full backup
architecture (immutability, ransomware, RTO) → `backups`.

## Sharing files

| Need | Method |
|------|--------|
| Quick share with anyone | Link (set expiration when available) |
| Ongoing family access | Shared folder or shared album |
| Sensitive documents | Encrypt first or use a secure local channel |

Per-service steps: `references/sharing.md`.

## Security basics

- Enable 2FA on every cloud account.
- Review shared links quarterly; revoke stale access.
- Do not store unencrypted passwords, ID scans, or financial documents in
  everyday cloud folders.
