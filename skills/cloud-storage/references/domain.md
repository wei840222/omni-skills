# Cloud Storage Domain Knowledge

## Scope

Operational cloud storage tasks across providers:

- Object: S3, GCS, Azure Blob, Backblaze B2, Cloudflare R2
- Consumer/prosumer: Google Drive, Dropbox, OneDrive/SharePoint, iCloud

Out of scope handoffs:

- Storage architecture selection → `storage`
- Deep S3 lifecycle/CORS/presign/multipart → `s3`
- Broad AWS/Azure platform work → `aws` / `azure`
- Backup policy and restore drills → `backups`

## Critical rules

1. **Verify operations completed** — API 200 ≠ success; check object exists with correct size/checksum.
2. **Calculate ALL costs before large transfers** — egress often dominates; use `references/costs.md` and confirm via `references/sources.md`.
3. **Prove restorable backup before delete** — existence alone is insufficient; restore or equivalent verification first.
4. **Handle partial failures** — long operations fail mid-way; implement checkpoints and resume logic.
5. **Respect provider rate limits** — examples: S3 prefix request budgets, Drive per-user QPS, Dropbox batch limits, Google upload daily caps where published.

## Authentication traps

- **OAuth tokens expire** — refresh before long operations, not mid-flight without a plan.
- **Service account ≠ user account** — different quotas, permissions, and audit trails.
- **Wrong region/endpoint** — a bucket in `eu-west-1` will not answer on a mismatched regional endpoint.
- **MFA / session tokens** — some paths need short-lived session credentials; plan interactive auth separately from automation.

## Multi-provider gotchas

| Concept | Translates differently |
|---------|------------------------|
| Shared folder | Drive "Shared with me" ≠ Dropbox team folders ≠ OneDrive/SharePoint libraries |
| File identity | Drive IDs; Dropbox paths (and IDs); object stores use bucket + key |
| Versioning | S3 optional; Drive revisions automatic; Dropbox keeps limited history |
| Permissions | S3 IAM/policies (+ optional ACLs); Drive roles; Dropbox links + sharing |

## Before any bulk operation

- [ ] Estimated time calculated (size ÷ effective bandwidth)
- [ ] Rate limits checked for both source AND destination
- [ ] Cost estimate including egress + API calls (orientation table + live sources)
- [ ] Checkpoint/resume strategy for failures
- [ ] Verification method defined (checksum, count, spot-check)
- [ ] Delete/cutover gated on successful verification
