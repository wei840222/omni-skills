---
name: cloud-storage
description: >
  Manage multi-provider cloud file operations: upload, download, sync, migrate,
  verify checksums, estimate egress/API cost, and recover partial bulk jobs across
  S3, GCS, Azure Blob, B2, R2, Drive, Dropbox, OneDrive, and iCloud. Use when the
  user moves or audits files across cloud providers with cost and auth awareness.
  Prefer s3 for deep S3-only lifecycle/CORS/presign work, storage for architecture
  selection, aws/azure for full-cloud infra beyond object/file ops, and backups
  for backup-policy design.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"☁️"}'
  related-skills: '{"s3":"Deep S3-compatible lifecycle, CORS, presigned URLs, and multipart patterns.","storage":"Storage architecture and system selection beyond day-to-day file ops.","aws":"Broader AWS infra, IAM, and billing outside object/file transfers.","azure":"Azure platform work beyond Blob/file operations.","backups":"Backup policy, retention, and restore drills rather than one-off transfers."}'
---

# Cloud Storage

Operational guidance for **moving, verifying, and cost-checking files** across
object stores and consumer cloud drives.

This skill is **knowledge-only**. It does not create a local persistent state
tree. Do not write runtime notes into this package. Provider credentials stay in
host env/profiles; never commit secrets.

## When to use

- Upload, download, sync, or migrate files between cloud providers
- Estimate storage + egress + request cost before a bulk job
- Diagnose auth, region/endpoint, rate-limit, or partial-failure issues
- Choose object-store vs consumer-drive patterns for the same workflow

Prefer adjacent skills when they fit better:

- S3 lifecycle, CORS, presign, multipart deep dive → `s3`
- Database/object/block/CDN architecture choice → `storage`
- Broad AWS account/IAM/billing work → `aws`
- Broad Azure platform work → `azure`
- Backup policy and restore drills → `backups`

## Progressive disclosure

| Need | Load |
|------|------|
| Scope, critical rules, bulk checklist | `references/domain.md` |
| Provider-specific traps and APIs | `references/providers.md` |
| Auth setup and credential traps | `references/auth.md` |
| Cost model and orientation rates | `references/costs.md` |
| Official pricing / docs anchors | `references/sources.md` |

## Core workflows

**Object store transfer:** resolve credentials and region → dry-run path/key
mapping → cost estimate from `references/costs.md` + live `references/sources.md`
→ upload/copy with checkpointing → verify size/checksum → only then delete source
if requested.

**Cross-cloud migrate:** inventory source → estimate egress and destination PUTs
→ choose tool (CLI, Storage Transfer, AzCopy, rclone) → chunked copy with resume
→ spot-check and full count/checksum plan → cutover.

**Consumer drive ops:** confirm OAuth scopes and shared-drive ownership model →
treat shortcuts/links as non-copies → export Google Docs to concrete formats →
respect per-user rate limits.

## Critical rules

1. **Verify completion** — HTTP 200 is not enough; confirm object exists with
   expected size and checksum/ETag where the API provides one.
2. **Price the whole job first** — storage, operations, and especially egress;
   open `references/costs.md` then confirm live pages in `references/sources.md`.
3. **Restorable backup before delete** — prove backup exists and restores before
   removing the only copy.
4. **Checkpoint bulk work** — long jobs fail mid-way; design resume markers and
   idempotent retries.
5. **Match auth to the job** — service accounts/roles for automation; user OAuth
   for interactive consumer drives; refresh tokens before long runs.
6. **Route deep specialties** — do not re-implement full `s3`, `storage`, `aws`,
   or `backups` guidance inside this skill.

## Failure modes

| Symptom | Recovery |
|---------|----------|
| Bucket/object not found after correct key | Check region/endpoint and credential account; load `references/auth.md` |
| Cost quote disputed | Treat tables as orientation; open official pricing URLs in `references/sources.md` |
| Job dies at 40% | Resume from last checkpoint; avoid full restart that doubles egress |
| OAuth mid-job expiry | Refresh before start; split into shorter authenticated batches |
| User wants lifecycle/CORS/presign only | Hand off to `s3` |
| User wants DB vs object architecture | Hand off to `storage` |
