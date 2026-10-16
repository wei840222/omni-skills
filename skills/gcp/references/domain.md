# GCP domain guide

Operational rules, failure signatures, design limits, cost reflexes, security baselines, and service defaults for the `gcp` skill. Verify time-sensitive prices and quotas on Google Cloud docs / Billing before committing money. Primary URLs live in `references/sources.md`.

## Core rules

1. **Inventory before architecture.** Avoid proposing infrastructure into an unknown project — and avoid rediscovering a project already mapped. Read stored inventory first: `## Current Infrastructure` in `<state_root>/memory.md`, whatever its `## Boxes` line points to, and `<state_root>/servers/servers.md`. Then discover only what is missing or older than the last recorded pass. Minimum discovery: `gcloud config list`, `gcloud projects list`, `gcloud asset search-all-resources --scope=projects/<id>`, and 30 days of cost grouped by service. Asset Inventory answers “what exists here” across APIs in one call.
2. **Billing export and a budget before the first resource.** On a fresh project the first deploy is a Cloud Billing export to BigQuery plus a budget, not a VM. The export is the only SKU-level source and **reports forward only** — a month without it is unanalyzable forever. Budget thresholds: alert at 50%, 90%, and 100% of actual plus 100% of forecast. **A budget does not cap spend**; a hard stop needs a Pub/Sub-triggered function that detaches the billing account (stops every resource in the project).
3. **A monthly number with every recommendation.** Rough stages (us-central1, on-demand — **verify current pricing before committing**):

   | Stage | Recommended stack | Monthly (order of magnitude) |
   |-------|-------------------|------------------------------|
   | MVP (<1k users) | Cloud Run scaling to zero + smallest Cloud SQL, no HA | ~tens |
   | Growth (1–10k) | Cloud Run min-instances 1 + Cloud SQL HA + Memorystore | ~low hundreds |
   | Scale (10k+) | GKE Autopilot or Cloud Run + AlloyDB/Cloud SQL HA + global ALB + Cloud CDN | ~hundreds+ |

   Default to the smallest viable machine. Prefer `gcloud recommender` before guessing. Where no recommendation exists: avg CPU <20% over 14 days → step down one size; sustained >70% → step up or scale out. CPU alone under-diagnoses memory-bound workloads.
4. **Smallest blast radius, decided at creation.** One dedicated service account per workload — never the default Compute Engine service account (Editor unless org policy stops it). Databases on private IP; buckets with uniform bucket-level access and public access prevention; CMEK chosen at creation. Hard-to-undo: bucket location, Cloud SQL private-IP network, shrinking a subnet primary range, project ID.
5. **Everything in code, nothing console-only.** Console explores; `gcloud` is imperative and forgets. Anything that survives the session goes into the configured `iac_tool`. Plan must come back clean before change, or a console hotfix becomes accidental state.
6. **Label at creation, and only after the export exists.** Labels reach billing export from the moment both the label and the export exist — never backfilled. Keys are lowercase; ≤64 labels per resource. Minimum set: `env`, `team`, `service`.
7. **Project and region are decisions, not leftovers.** State both in every command and price quote. A project ID is globally unique and permanent — cannot be renamed, and after deletion can never be reused. A VPC is global while every subnet, disk, and Cloud SQL instance is regional/zonal. While `default_project` or `default_region` is unset, say what you are assuming before acting.
8. **Name the first quota and the first timeout.** Quotas are per project **and** per region; GPUs, TPUs, and some newer families often start at zero until requested (approval can take days). Every scaling design states which limit it hits first and its current value.

## Quick reference

| Situation | First play |
|-----------|------------|
| Bill jumped | Billing export in BigQuery by service, then SKU; map delta start to a deploy |
| Fresh project | Billing export + budget alerts before the first resource |
| Inherited / unknown project | Asset Inventory sweep, then security baseline top-to-bottom |
| 403 `SERVICE_DISABLED` | Enable the API — most common false IAM alarm |
| 403 `PERMISSION_DENIED` | API enablement → binding level → deny policy → VPC-SC |
| Cannot reach Cloud SQL / VM / Google API | Firewall → route → Private Google Access → PSC/peering → DNS |
| LB 502/503/504 | Backend keep-alive vs timeout; health-check source ranges `35.191.0.0/16` and `130.211.0.0/22` |
| Cloud Run will not go live | PORT=`$PORT` (8080) on `0.0.0.0`; startup probe; concurrency; min instances |
| GKE Autopilot `Unschedulable` | CPU:memory ratio / features Autopilot rounds or rejects |
| BigQuery 100× estimate | Dry-run first; partition/cluster; avoid `SELECT *` |
| Spot VM gone ~30s after notice | Handle `SIGTERM` fast, or leave Spot |
| Alert never fired in a real outage | Alert on absence of data explicitly |

## Failure signatures

Decode rule: in GCP the error string names the subsystem more reliably than the status code. A 403 is three unrelated problems wearing one number; a “quota” message may be capacity, not quota.

| Signature | Most likely cause | First move |
|-----------|-------------------|------------|
| 403 `SERVICE_DISABLED` / “API has not been used…” | API not enabled | Enable the service |
| 403 `PERMISSION_DENIED` with the right role granted | Wrong resource level, propagation lag, deny policy, or VPC-SC | Policy Troubleshooter with exact principal/resource/permission |
| 403 mentioning VPC Service Controls / unique request id | Perimeter blocked the call | Read VPC-SC audit log entry |
| `iam.serviceAccounts.actAs` denied | Caller may create the resource but not attach that SA | `roles/iam.serviceAccountUser` on the exact SA |
| 429 `RESOURCE_EXHAUSTED` | Rate quota per project/region | Backoff with jitter; check whether default is zero |
| `ZONE_RESOURCE_POOL_EXHAUSTED` | No capacity in that zone now — not a quota | Other zone / machine family / reservation |
| Cloud Run “container failed to start and listen on the port” | Not listening on `$PORT` / `0.0.0.0`, or slower than startup probe | PORT contract first |
| LB 502 with healthy-looking backends | Keep-alive closed under LB, or backend service timeout (30s default) | Raise backend keep-alive above LB, then timeout |
| LB 503 “no healthy upstream” | Health checks blocked | Allow health-check ranges in firewall |
| `Connection timed out` to Cloud SQL | Network path, not credentials | Firewall / private IP / peering first |
| Cloud SQL “remaining connection slots are reserved” | Connection ceiling (often serverless fan-out) | Auth Proxy + pooler; ceiling derives from tier memory |
| BigQuery query costs 100× estimate | Wide `SELECT *`, no usable partition filter | Dry-run every query |
| GKE Autopilot pod `Unschedulable` | Ratio/feature Autopilot rejects | Autopilot resource rules |
| VM vanishes ~30s after notice | Spot preemption (30s notice) | Fast `SIGTERM` handling or leave Spot |
| Alert never fired during outage | Metric stopped publishing | Alert on absence of data |

## Limits that force designs

| Service | Design-shaping limit |
|---------|----------------------|
| Cloud Run | 60 min max request timeout · default concurrency 80/instance (max 1000) · max instances default 100 · stream large uploads to Cloud Storage |
| Cloud Run functions | Gen1 caps at 9 min; gen2 HTTP reaches 60 min (gen2 is Cloud Run under another UI) |
| Pub/Sub | Ack deadline 10s default / 600s max · retention up to 31 days · ordering keys serialize a key’s throughput |
| BigQuery | On-demand bills bytes **scanned**, never rows returned · `LIMIT` does not reduce scan · streaming inserts cost far more per GB than free batch loads |
| Firestore | Sustained writes to one document ~1/s · sequential IDs hotspot indexes |
| Bigtable | One-node floor · row key is the only index and cannot be changed later |
| Spanner | Floor from 100 processing units · schema interleaving is a creation-time decision |
| Cloud SQL | Storage grows and never shrinks · HA is zone-level standby · connection ceiling from tier memory |
| VPC | Global VPC; subnet primary range can expand but never shrink · GKE secondary ranges sized at creation |
| VPC peering | Non-transitive — why Private Service Connect exists |
| Load balancing | Backend service timeout defaults to 30s · global external ALB needs Premium network tier |
| Projects | Project ID globally unique and permanently unreusable · 30-day deletion recovery · quotas are per project |
| Cloud KMS | Key rings/keys cannot be deleted — only versions destroyed after a delay |

## Cost reflexes

Ratios are more stable than absolute list prices — **re-check Billing / price pages** before quotes. Reference region: us-central1, on-demand.

| Driver | Why it bites | Do instead |
|--------|--------------|------------|
| BigQuery on-demand scans | Bytes scanned pricing; wide `SELECT *` scans every column | Partition, cluster, select columns, dry-run; consider editions when scan cost stabilizes high |
| Cloud NAT | Hourly gateway + per-GB processed; Google API traffic through NAT is waste | Private Google Access (free) + Private Service Connect |
| Cloud Logging ingestion | Paid after free allowance; org-wide Data Access logs are a common cause | Exclusion filters; enable Data Access only where the data lives |
| External IPv4 addresses | Billed attached or reserved; unused reserved often costs more | Count/release orphans; put workloads behind LB without public VM IPs |
| Idle Vertex AI endpoints | Node-hours at zero traffic; GPU hours expensive | Undeploy between experiments; batch prediction for offline work |
| E2 chosen for list price | E2 earns **no** sustained-use discount | Compare discounted N-series for always-on workloads |
| Orphaned disks / snapshot chains | VM delete may leave disks; snapshot chains keep deleted data alive | Sweep unattached disks; snapshot retention policy |
| Cross-zone / internet egress | Same-zone free; cross-zone and internet cost | Co-locate chatty pairs; serve public assets via Cloud CDN |
| Cloud Composer | Small Airflow environment has a high floor idle or busy | Scheduler + Workflows until real DAGs/backfills are needed |
| Bigtable / Spanner floors | Minimum capacity bills like a subscription | Firestore or Cloud SQL until the access pattern demands them |

## Security baseline

Anything unchecked here outranks feature work.

| Check | Passing looks like |
|-------|--------------------|
| Domain-restricted sharing | `constraints/iam.allowedPolicyMemberDomains` enforced |
| Default service account | Workloads use dedicated SAs; default Compute Engine account has no Editor and ideally no bindings |
| Service account keys | None created; `constraints/iam.disableServiceAccountKeyCreation` enforced; CI uses Workload Identity Federation |
| Primitive roles | No `roles/owner` / `roles/editor` on humans or workloads outside break-glass |
| Buckets | `constraints/storage.publicAccessPrevention` org-wide; uniform bucket-level access on |
| Databases | Cloud SQL private IP only; `constraints/sql.restrictPublicIp` enforced |
| VM access | No external IPs (`constraints/compute.vmExternalIpAccess`); OS Login; shell via IAP TCP forwarding |
| Audit trail | Admin Activity always on; Data Access deliberately enabled where the data is |
| Data residency | `constraints/gcp.resourceLocations` when a regime/contract names allowed regions |

## Service defaults

| Need | Default | Switch when |
|------|---------|-------------|
| Static site | Cloud Storage behind global external ALB + Cloud CDN | Never use a public bucket as the public origin |
| API backend | Cloud Run | Node-level control / sidecars / existing Kubernetes ecosystem → GKE Autopilot |
| Event handler | Cloud Run function via Eventarc | Work exceeds HTTP ceiling → Cloud Run job or Batch |
| Container orchestration | GKE Autopilot | Privileged pods, custom kernel, fine-grained GPU packing → GKE Standard |
| Relational database | Cloud SQL for PostgreSQL | Global strong consistency → Spanner; heavy analytics on live OLTP → AlloyDB |
| Document database | Firestore Native mode | Petabyte scale with one known row-key pattern → Bigtable |
| Cache / sessions | Memorystore | Idle cost matters more than sub-ms latency → Firestore |
| Messaging | Pub/Sub | Per-task scheduling/retries → Cloud Tasks; multi-step state machines → Workflows |
| Warehouse | BigQuery | — |
| Job orchestration | Cloud Scheduler + Workflows | Real DAGs with backfills → Composer (price the floor in) |
| Secrets | Secret Manager | — |
| Container images | Artifact Registry | (`gcr.io` now resolves to Artifact Registry) |
| Config / IaC | Whatever `iac_tool` says | — |

## Output gates

Before delivering an architecture, policy, or command:

- State the monthly cost of what you recommended, in the region it will actually run (verify before money commits).
- Name the blast radius (project, folder, org, data class).
- Name the first quota and first timeout the design hits.
- Prefer read-only / plan output; keep destructive commands behind an explicit confirmation gate.
- If anything durable was produced, write it to the correct box before ending (`references/state.md`).

## Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| Treating a budget as a spending cap | Budgets only notify | Alerts at 50/90/100%; hard cap = detach billing and stop everything |
| Fixing every 403 by granting a broader role | Most are disabled APIs or deny policies | Policy Troubleshooter first |
| Running as the default Compute Engine SA | Editor on the whole project | One SA per workload with only needed roles |
| Creating SA keys because a tutorial did | Permanent credential, ends up in git | Workload Identity Federation / impersonation / attached SAs |
| Assuming VPC peering is transitive | Peering does not chain | Private Service Connect or full mesh before the second spoke |
| Enabling every security product on day one | SCC Premium + org-wide Data Access can outspend the workload | Free baseline first; paid detection when there is something to detect |
| Deleting a project to “clean up” | Project ID burned forever; 30-day window hides live deps | Delete resources, keep project, or set a lien |

## Where experts disagree

- **Cloud Run vs GKE.** Request-shaped variable traffic → Cloud Run for idle cost and surface. Platform team / operators / per-node GPU packing → GKE. Autopilot removed much node toil, so the question is often “do you need Kubernetes APIs?”.
- **Project-per-env vs folder-per-team.** Solo builder → project-per-env is enough. Any team or demonstrable isolation regime → folders with inherited org policies early.
- **BigQuery on-demand vs editions.** On-demand rewards sparse unpredictable querying; editions rewards steady load. Break-even is a monthly scan number, not a preference.
