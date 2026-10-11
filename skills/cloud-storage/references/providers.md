# Provider-Specific Patterns

## Object storage (S3-compatible and cousins)

### AWS S3

- **Presigned URLs** — SigV4; include required headers (for example `Content-Type`) for browser uploads.
- **Consistency** — modern S3 offers strong read-after-write for new objects; still design clients for retries and eventual listing lag in large inventories.
- **Lifecycle rules** — transitions and expirations can conflict; review rule order and filters.
- **Request budgets** — plan around prefix throughput (commonly discussed ~3,500 writes/s and ~5,500 reads/s per prefix); scale with key design or partitions.

### Google Cloud Storage

- **Signed URLs** — need a signer with `signBlob` (or equivalent) permission; service account common.
- **Object holds** — temporary/legal holds block deletion even for owners.
- **Compose** — composite objects have component limits; large composes need staged strategy.
- **Transfer** — Storage Transfer Service is preferred for multi-TB cloud-to-cloud when available.

### Azure Blob

- **SAS tokens** — account vs container vs blob scope; keep short TTL and least privilege.
- **Access tiers** — Hot/Cool/Cold/Archive; archive rehydrate can take hours—plan RTO.
- **Soft delete** — often enabled on new accounts; check retention before assuming permanent delete.
- **AzCopy** — primary bulk tool; use checkpoints/journals for resume.

### Backblaze B2

- **S3-compatible API** — many S3 tools work with the B2 S3 endpoint for the account region.
- **Application keys** — bucket-restricted keys for least privilege.
- **Small-file billing** — very small objects may be billed at a minimum size; confirm current product docs.
- **Egress allowance** — product pricing often includes a multiple of stored data as free egress; verify live page before quoting.

### Cloudflare R2

- **Egress to Internet** — R2 documents free egress bandwidth for standard serving patterns; still pay storage and Class A/B operations.
- **S3 compatibility** — common ops work; advanced S3 features may be missing—test the exact API surface.
- **Workers** — in-network access patterns can avoid extra egress hops.
- **Infrequent Access** — separate storage class with retrieval fees and minimum duration; do not assume Standard free-tier rules apply.

## Consumer / prosumer storage

### Google Drive

- **Shortcuts vs files** — operations on shortcuts affect the target; copying a shortcut is not copying bytes.
- **Shared drives** — organization ownership model differs from My Drive.
- **Quotas** — plan around per-user query budgets; batch where the API allows.
- **Export** — Google Docs/Sheets export to DOCX/PDF/etc., not a proprietary native file blob.

### Dropbox

- **Team folders** — admin policy can override member expectations.
- **Paper** — separate surface from file storage APIs.
- **Upload limits** — API single-request limits differ from desktop client chunking; use upload sessions for large files.

### OneDrive / SharePoint

- **Personal vs Business** — different Graph capabilities and admin controls.
- **Conflicts** — clients may rename (`file (1).txt`) rather than fail closed.
- **SharePoint libraries** — permission inheritance is easy to misread; verify effective access.
- **Delta queries** — prefer delta for change detection over full tree walks.

### iCloud

- **No general public file API** comparable to Drive/Dropbox for arbitrary user files.
- **CloudKit** — app data sync, not a generic user-file manager replacement.
- **Optimized storage** — local stubs may need download before checksum or migrate.
- **Family sharing** — sharing rules are narrower than full collaborative drives.
