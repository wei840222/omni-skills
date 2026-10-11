# Research sources (Gate 6)

Verify mutable numbers (storage rates, egress, request prices, free tiers,
minimum durations) against these pages at answer time.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref validator — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Object storage pricing and classes

- Amazon S3 pricing — https://aws.amazon.com/s3/pricing/
- Amazon S3 storage classes (minimum durations, retrieval behavior) — https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
- Amazon S3 storage class overview marketing page — https://aws.amazon.com/s3/storage-classes/
- Google Cloud Storage pricing — https://cloud.google.com/storage/pricing
- Azure Blob Storage pricing — https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
- Backblaze B2 Cloud Storage pricing — https://www.backblaze.com/cloud-storage/pricing
- Cloudflare R2 pricing (Standard storage $0.015/GB-month; free egress bandwidth; Class A/B ops) — https://developers.cloudflare.com/r2/pricing/

## Transfer and operations guidance

- Prefer vendor transfer products when migrating multi-TB between clouds (for example GCS Storage Transfer Service, AWS DataSync/S3 Batch, Azure AzCopy) — confirm the current product doc for the chosen pair rather than assuming CLI copy is cheapest or safest.
- S3 request-rate and prefix scaling guidance lives in current AWS S3 performance docs; treat “3500/5500 per prefix” figures as engineering planning heuristics and verify against the live performance documentation for the API you call.

## Consumer drive platforms

- Google Drive API / Google Identity OAuth scope docs (minimal scopes, shared drives) — start from Google API Console + current Drive API documentation for the project.
- Dropbox HTTP API upload session docs — use for large-file chunking limits.
- Microsoft Graph OneDrive/SharePoint diff/delta docs — use for change detection instead of full walks.
- Apple CloudKit documentation — app data sync; not a generic user-file migration API.

## Refresh notes (this refactor pass)

- Reachable with HTTP 200 during research: S3 pricing, S3 storage-classes intro, GCS pricing, Azure Blob pricing, Backblaze B2 pricing, Cloudflare R2 pricing docs.
- R2 docs explicitly list Standard storage **$0.015/GB-month**, free egress to Internet, and Class A/B operation pricing; free tier applies to Standard, not Infrequent Access.
- Backblaze public pricing materials emphasize low storage rates and egress allowances (including calculator logic consistent with low $/TB storage and free egress multiples); always re-open the live page before quoting.
- Hyperscaler pages are region/SKU dynamic and heavily scripted; orientation cents-per-GB figures in `costs.md` are planning baselines only.
