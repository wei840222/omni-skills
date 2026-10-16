---
name: gcp
description: >
  Architects, debugs, secures, and cost-optimizes Google Cloud Platform (GCP) —
  Cloud Run, GKE, Compute Engine, BigQuery, Cloud SQL, IAM, VPC, and gcloud
  context. Use when deploying or reviewing GCP resources, when a bill jumps or
  BigQuery scan cost must come down, when 403 PERMISSION_DENIED / SERVICE_DISABLED,
  RESOURCE_EXHAUSTED quota, 502/503/504, or an unreachable Cloud SQL instance has
  no obvious cause, when choosing compute or databases, hardening service accounts
  / org policies / public buckets / secrets, writing Terraform against the google
  provider, or auditing an inherited project. Prefer `k8s` for Kubernetes
  manifest authoring, `terraform` for HCL/state mechanics, `pg` for PostgreSQL
  query/index tuning inside Cloud SQL or AlloyDB, `aws` for the multi-cloud
  counterpart, and `infrastructure` for provider-agnostic framing.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌐","requires":{"anyBins":["gcloud"]}}'
  related-skills: '{"terraform":"HCL authoring, state surgery, and module design beyond GCP platform defaults.","k8s":"Kubernetes manifests and in-cluster debugging for workloads on GKE.","pg":"PostgreSQL query, index, and vacuum tuning inside Cloud SQL or AlloyDB.","aws":"Multi-cloud counterpart and common migration source estate.","infrastructure":"Provider-agnostic architecture decisions before GCP-specific services."}'
---

## When to load

Load for **GCP platform** work: service selection, VPC/Private Google Access/PSC design, IAM and org policy, cost control, failure diagnosis, Cloud Run/GKE/BigQuery/Cloud SQL operations, and project hygiene.

Prefer siblings when they own the job:

| Job | Skill |
|-----|-------|
| HCL / Terraform mechanics | `terraform` |
| Kubernetes manifests / in-cluster debug | `k8s` |
| PostgreSQL query and index tuning | `pg` |
| AWS-side multi-cloud or migration source | `aws` |
| Provider-agnostic architecture framing | `infrastructure` |

## State location

Optional GCP notes may live under `<workspace>/gcp/`, `<workspace>/memory/gcp/`, or `~/gcp/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in that order.
3. If multiple exist, use only the highest-precedence path and report duplicates — do not merge.
4. Create `<workspace>/gcp/` only with user consent when no candidate exists and durable state must be written.

Use the selected `<state_root>` for every later state path. Typical children (create only when needed):

| Path | Role |
|------|------|
| `<state_root>/config.yaml` | Defaults: project, region, IaC tool, budget, BigQuery billing model |
| `<state_root>/memory.md` | Observed inventory notes, `## Boxes` index, `## Due` expiries |
| `<state_root>/servers/servers.md` | Shared host inventory row (`Name` + `Provider=gcp`) |
| `<state_root>/domains/domains.md` | DNS zones, registered domains, certificate expiries |
| `<state_root>/contacts/contacts.md` | People who own projects (email/handle key) |
| `<state_root>/projects/<name>.md` | User-tracked projects with `status` |

Never write credentials, keys, tokens, or connection strings under `<state_root>/`. Store pointers only (`gcp-sm:…`, `env:…`, `keychain:…`, `file:~/.config/gcloud/…`). Host-owned shared memory such as workspace `MEMORY.md` is outside `<state_root>` and needs explicit consent.

## Routing

Keep `SKILL.md` as the entry point. Do not preload the full package. Load one supporting file only when the turn needs it:

- **Rules, failures, limits, cost reflexes, security baseline, service defaults, traps** → `references/domain.md`
- **State inventory, config variables, write-before-end rules** → `references/state.md`
- **Primary Google Cloud / Agent Skills URLs** → `references/sources.md`

## Workflow

1. **Resolve context** — Name project and region before acting. While defaults are unset, state the assumption (do not open with discovery questions).
2. **Inventory before architecture** — Read stored inventory under `<state_root>` when present; then live-check with `gcloud config list`, `gcloud projects list`, Asset Inventory, and 30 days of cost by service.
3. **Classify the ask** — Architecture, failure signature, cost, security, or IaC. Load `references/domain.md` for the matching table.
4. **Recommend with blast radius** — Give one default path, the first quota/timeout that binds, and a monthly cost ballpark for the named region (verify list prices before money commits).
5. **Preview before mutate** — Prefer read-only `gcloud` / `terraform plan`. Destructive actions (delete project/dataset, destroy key versions, detach billing, remove node pools) stay out of copy-paste blocks until the user confirms.
6. **Persist durable facts** — Hosts, spend figures, quota grants, decisions, and runbooks go to the correct box before the session ends (`references/state.md`).

## Core rules (summary)

1. Inventory before architecture; Asset Inventory maps estates faster than guessing APIs.
2. Billing export + budget before the first resource — export is forward-only.
3. Attach a monthly number to every recommendation; right-size before commitments.
4. Smallest blast radius at creation (dedicated SA, private IP, uniform bucket access).
5. Everything durable lives in code; console explores and reads.
6. Label at creation after the export exists — labels are not backfilled into past export months.
7. Project and region are explicit decisions; project IDs are globally unique and permanent.
8. Name the first quota and first timeout (GPUs often start at zero; Cloud Run PORT contract; LB health-check ranges).

## Output shape

Every non-trivial GCP reply should include:

1. **Assumed project + region**
2. **Diagnosis or design** with the binding limit named
3. **Cost ballpark** (verify before spend) and blast radius
4. **Next command or confirmation gate** (read-only first)
5. **State write** if anything durable was produced
