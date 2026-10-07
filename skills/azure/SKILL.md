---
name: azure
description: >
  Architect, debug, secure, and cost-optimize Azure workloads — VMs, App Service,
  Functions, AKS, Container Apps, Azure SQL, Cosmos DB, Entra ID, VNets, Storage,
  Key Vault, and az CLI context. Use when deploying or reviewing Azure resources,
  when a bill jumps or spend must come down, when AuthorizationFailed, RBAC lag,
  private-endpoint DNS, Application Gateway 502, App Service ~230s timeout, Cosmos
  429, SNAT exhaustion, or SkuNotAvailable/AllocationFailed has no obvious cause,
  when choosing compute or database options, hardening managed identities and
  storage exposure, writing Bicep/ARM/Terraform against Azure, or auditing an
  inherited subscription. Not for Kubernetes manifest authoring (`k8s`), Terraform
  language mechanics (`terraform`), or SQL query/index tuning (`sql`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔷","requires":{"anyBins":["az"]}}'
  related-skills: '{"terraform":"HCL authoring, state surgery, and module design beyond Azure platform defaults.","k8s":"Kubernetes manifests and cluster debugging for workloads on AKS.","aws":"Multi-cloud counterpart and common migration source estate.","sql":"Query and index tuning inside Azure SQL or PostgreSQL Flexible Server.","infrastructure":"Provider-agnostic architecture decisions before Azure-specific SKUs."}'
---

## When to load

Load for **Azure platform** work: service selection, VNet/Private Link design, RBAC and Entra ID, cost control, failure diagnosis, Bicep/ARM/`az` operations, and subscription hygiene.

Prefer siblings when they own the job:

| Job | Skill |
|-----|-------|
| HCL / Terraform mechanics | `terraform` |
| Kubernetes manifests / in-cluster debug | `k8s` |
| AWS-side multi-cloud or migration source | `aws` |
| SQL query and index tuning | `sql` |
| Provider-agnostic architecture framing | `infrastructure` |

## State location

Optional Azure notes may live under `<workspace>/azure/`, `<workspace>/memory/azure/`, or `~/azure/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in that order.
3. If multiple exist, use only the highest-precedence path and report duplicates — do not merge.
4. Create `<workspace>/azure/` only with user consent when no candidate exists and durable state must be written.

Use the selected `<state_root>` for every later state path. Typical children (create only when needed):

| Path | Role |
|------|------|
| `<state_root>/config.yaml` | Defaults: subscription, location, IaC tool, budget, billing model |
| `<state_root>/memory.md` | Observed inventory notes, `## Boxes` index, `## Due` expiries |
| `<state_root>/servers/servers.md` | Shared host inventory row (`Name` + `Provider=azure`) |
| `<state_root>/domains/domains.md` | Custom domains, DNS zones, certificate expiries |

Never write credentials, keys, tokens, or connection strings under `<state_root>/`. Store pointers only (`azure-kv:…`, `env:…`, `keychain:…`). Host-owned shared memory such as workspace `MEMORY.md` is outside `<state_root>` and needs explicit consent.

## Routing

Keep `SKILL.md` as the entry point. Load supporting files only when needed:

- **Rules, failures, limits, cost reflexes, security baseline** → `references/domain.md`
- **State inventory, config variables, write-before-end rules** → `references/state.md`
- **Gate 6 primary sources** → `references/sources.md`

## Workflow

1. **Resolve context** — Name subscription and region before acting. While defaults are unset, state the assumption (do not open with discovery questions).
2. **Inventory before architecture** — Read stored inventory under `<state_root>` when present; then live-check with `az account show`, Resource Graph counts, and Cost Analysis by service.
3. **Classify the ask** — Architecture, failure signature, cost, security, or IaC. Load `references/domain.md` for the matching table.
4. **Recommend with blast radius** — Give one default path, the first quota/timeout that binds, and a monthly cost ballpark for the named region (verify list prices before money commits).
5. **Preview before mutate** — Prefer read-only `az` / `what-if` / `terraform plan`. Destructive actions (delete, purge, Complete-mode deploy, lock removal) stay out of copy-paste blocks until the user confirms.
6. **Persist durable facts** — Hosts, spend figures, expiries, decisions, and reusable KQL go to the correct box before the session ends (`references/state.md`).

## Core rules (summary)

1. Inventory before architecture; spend maps estates faster than portal tours.
2. Budget before the first resource — budget + anomaly alert on a fresh subscription.
3. Attach a monthly number to every recommendation; right-size before reservations.
4. Smallest blast radius at creation (RBAC scope, private endpoints, no shared-key storage).
5. Everything durable lives in code; portal is for explore/read.
6. Tag at creation — Azure does not inherit resource-group tags without Policy.
7. Subscription and region are explicit decisions, not ambient CLI leftover context.
8. Name the first quota and first timeout (App Service ~230s HTTP, SNAT ports, Cosmos 20 GB logical partition, role-assignment caps).

## Output shape

Every non-trivial Azure reply should include:

1. **Assumed subscription + region**
2. **Diagnosis or design** with the binding limit named
3. **Cost ballpark** (verify before spend) and blast radius
4. **Next command or confirmation gate** (read-only first)
5. **State write** if anything durable was produced
