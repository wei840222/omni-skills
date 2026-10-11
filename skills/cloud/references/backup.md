# Cloud Backup Strategy

## The 3-2-1 rule (consumer)

- **3** copies of important files
- **2** different storage types (for example cloud + local drive)
- **1** offsite copy (cloud usually counts)

Cloud is convenient but not a complete backup by itself. Account lockout,
accidental sync deletes, and vendor outages still happen. Keep a complementary
local copy of irreplaceable data.

For ransomware-resistant, immutable, or multi-region backup architecture, load
the `backups` skill instead of stretching this guide.

## What to back up

### High priority (irreplaceable)

- Family photos and videos
- Tax returns, contracts, ID scans (encrypted)
- Original creative work
- Financial export archives

### Medium priority

- Active work documents
- School or research materials
- Purchased PDFs/ebooks you cannot re-download easily

### Low priority

- Re-downloadable media
- Installers and caches

## Risky data for unencrypted cloud storage

- Password lists (use a password manager)
- Bank account credentials
- Passport / driver-license scans
- Medical records
- Anything catastrophic if leaked

If these must live in cloud storage, encrypt first (password-protected archive
at minimum) and restrict sharing.

## Photo backup setup

**Pick ONE service:**

- iPhone-centric → iCloud Photos
- Android-centric → Google Photos
- Mixed → Google Photos or Dropbox Camera Uploads

**Disable the others** to prevent duplicate libraries.

**Settings to enable:**

- Auto-upload on Wi-Fi
- Optimize device storage when local space is tight (originals stay in cloud)

**Monthly check:** open the Photos app, confirm backup/status text, and spot-open
an older album from another device.

## Document backup

Desktop/Documents folder sync (iCloud Drive, Google Drive for Desktop, or
OneDrive) is the lowest-friction option on Mac/Windows. Before disabling sync,
download anything that exists only in the cloud.

## Backup checklist

- [ ] Photos auto-upload to exactly one service
- [ ] Documents folder syncing or scheduled copy in place
- [ ] External drive (or other local) copy for irreplaceable data
- [ ] 2FA on every cloud account
- [ ] Restore test from a second device succeeded

## Recovery test

Twice a year, pretend the primary phone/laptop is gone:

1. Sign in from another device or browser
2. Retrieve a specific photo from ~6 months ago
3. Retrieve a specific document
4. If either fails, fix the backup before trusting it
