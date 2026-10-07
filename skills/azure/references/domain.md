# Azure domain guide

Operational rules, failure signatures, design limits, cost reflexes, and security baselines for the `azure` skill. Verify time-sensitive prices and quotas on Microsoft Learn / Cost Management before committing money. Primary URLs live in `references/sources.md`.

## Core rules

1. **Inventory before architecture.** Never propose infrastructure into an unknown subscription — and never rediscover one already mapped. Read stored inventory first: `## Current Infrastructure` in `<state_root>/memory.md`, whatever its `## Boxes` line points to, and `<state_root>/servers/servers.md`. Then discover only what is missing or older than the last recorded pass. Minimum discovery: `az account show`, one Azure Resource Graph query counting resources by type and location, and 30 days of Cost Analysis grouped by service.
2. **Budget before the first resource.** On a fresh subscription the first deployment is a budget plus an anomaly alert, not a VM. Alert at ~80% actual and 100% forecast; set anomaly sensitivity near *daily* spend (`monthly_budget ÷ 30`) because anomalies are daily events. EA/CSP budget scopes differ from pay-as-you-go.
3. **A monthly number with every recommendation.** Rough stages (West Europe, pay-as-you-go, list price — **verify before committing money**):

   | Stage | Recommended stack | Monthly (order of magnitude) |
   |-------|-------------------|------------------------------|
   | MVP (<1k users) | App Service B1 + Azure SQL serverless (auto-pause) + Storage | ~tens |
   | Growth (1–10k) | App Service P1v3 + SQL GP + Front Door Standard | ~low hundreds |
   | Scale (10k+) | Container Apps or AKS + SQL BC/Hyperscale + Redis + Front Door | ~thousands+ |

   Default to the smallest viable SKU. Right-size heuristic: avg CPU <20% over 14 days → step down; sustained >70% → step up or out. On B-series / burstable plans, check credit metrics before trusting CPU %.
4. **Smallest blast radius, decided at creation.** Narrowest RBAC scope that works; data services behind private endpoints; storage shared-key auth disabled; encryption on. Hard-to-undo choices: Cosmos partition key, some storage redundancy moves, SQL Hyperscale (one-way), AKS network plugin/node subnet, overlapping VNet address space, region.
5. **Everything in code, nothing portal-only.** Portal explores and reads; durable changes go through the configured IaC tool. Preview with ARM/Bicep what-if or Terraform plan. Incremental mode does not delete removed template resources — Complete mode can.
6. **Tag at creation; Azure does not inherit tags.** Inheritance needs Policy `Modify` plus remediation. Minimum tags: `Environment`, `Workload`, `Owner`, `CostCenter`.
7. **Subscription and region are decisions.** Name both on every command and price quote. While defaults are unset, state the assumption before acting.
8. **Name the first quota and the first timeout.** App Service inbound HTTP ~230s; per-family vCPU quotas; LB SNAT default ports per instance; Cosmos logical partition 20 GB; subscription role-assignment caps.

## Quick reference

| Situation | First play |
|-----------|------------|
| Bill jumped | Cost Analysis by service, then resource; map delta start to a deploy |
| Fresh subscription | Budget + anomaly alert, then smallest stage stack |
| Inherited tenant | Resource Graph inventory, then security baseline top-to-bottom |
| `AuthorizationFailed` | Classify: wrong scope, wrong subscription context, propagation, data-plane role, deny assignment — never widen first |
| Private endpoint still public | DNS zone link → NSG → route → service firewall → probe from inside VNet |
| 502/504 / hang | Layer that emits the code; ~230s ⇒ App Service front-end idle timeout |
| Function silent | Hosting plan, dependent storage account, trigger scaling, poison queue |
| `SkuNotAvailable` / `AllocationFailed` | Regional/zonal capacity or family; try zone/size/Flexible orchestration; check quotas |
| Cosmos/Storage 429 | RU or account throttle; read charge + retry-after; fix partition/indexing |
| `MissingSubscriptionRegistration` | Register resource provider in **this** subscription |
| AKS `ImagePullBackOff` | ACR attach, private DNS, AcrPull on kubelet identity |

## Failure signatures

Decode rule: HTTP from a front door/gateway is about the *connection*; ARM strings are *permissions/quota/state*; bare timeouts often *routing/SNAT*. Activity Log + correlation ID is ground truth for control-plane calls.

| Signature | Likely cause | First move |
|-----------|--------------|------------|
| `AuthorizationFailed` despite portal role | Wrong scope, wrong subscription context, or control-plane vs data-plane role | Classify before adding roles |
| Portal works, code fails | Missing data-plane role (Contributor ≠ Storage Blob Data Contributor) | Assign data role to the app identity |
| Role still denied after ~20 min | Propagation (can take tens of minutes) | Fresh token; do not stack assignments |
| PE exists, app hits public IP | Private DNS missing/unlinked or custom DNS override | Resolve FQDN from inside the VNet |
| Timeouts only under load | SNAT exhaustion on default outbound | NAT Gateway; know default SNAT port budget |
| App Gateway 502 | Backend probe or hostname mismatch | Backend health → host name setting → NSG |
| Dies at ~230s | App Service front-end idle timeout (not app-configurable) | Make work async |
| Cosmos/Storage HTTP 429 | RU/s or account request-rate throttle | Charge + `x-ms-retry-after-ms` |
| `SkuNotAvailable` / zonal allocation | Capacity, not always quota | Other zone/size; then quota |
| Function stopped with no errors | Storage unreachable or keys rotated | Host state lives in that storage account |
| Spot VM gone / surprise reboot | Eviction or platform maintenance | IMDS Scheduled Events |

## Limits that force designs

| Service | Design-shaping limit |
|---------|----------------------|
| App Service | ~230s hard inbound HTTP timeout; plan is the scale unit; Linux/Windows apps do not share a plan; Always On unavailable on Free/Shared |
| Functions | Consumption short max timeout / no VNet; Premium/Flex longer; storage account is a hard dependency |
| Cosmos DB | 20 GB per logical partition key value; 2 MB item; partition key immutable; autoscale pricing/floor semantics differ from manual |
| Azure SQL | Hyperscale one-way; connection limits scale with SKU; serverless auto-pause has minimum idle delay |
| Storage account | Account (not container) is the throttle boundary; cool/cold/archive minimum retention + early-deletion fees |
| Managed disks | Size/IOPS tiers round up (Premium SSD v2 exception); disks do not shrink |
| VNet / subnet | Azure reserves 5 IPs/subnet; no overlapping peer address space; peering non-transitive; in-use subnet hard to shrink |
| AKS | Non-overlay Azure CNI: `nodes × (max_pods + 1)` must fit; minor versions leave support on a finite clock |
| Load Balancer | Default SNAT ports per instance; short idle timeout on outbound flows |
| Subscription | Role-assignment and RG/deployment-history ceilings |
| Key Vault | Soft-delete mandatory; purge protection is one-way once enabled |
| Entra ID | Moving a subscription to another tenant drops role assignments and system-assigned managed identities |

## Cost reflexes

Ratios are more stable than absolute list prices — **re-check Cost Management / price pages** before quotes.

| Driver | Why it bites | Do instead |
|--------|--------------|------------|
| Azure Firewall on a tiny VNet | Fixed hourly before traffic | NSG + NAT Gateway for many estates; Firewall when inspection is required |
| Front Door Premium “for WAF” | Premium base ≫ Standard | Standard + WAF unless Private Link origins / deeper managed rules needed |
| App Gateway / VPN / Bastion idle | Fixed hourly at zero traffic | JIT / Bastion Developer / tear down lab edges |
| Portal “Stopped” VM | Still allocated → compute bills | Deallocate; disks and static public IPs still bill |
| Log Analytics ingestion | Per-GB, often dominates | Daily cap, Basic Logs, DCR drop transforms |
| Cosmos provisioned RU idle | Bills whether queried; default index-all | Serverless / sane autoscale floor / exclude paths |
| Orphan disks / NICs / public IPs | VM delete does not always cascade | Monthly unattached sweep |
| Premium SSD default | Portal bias | Match IOPS need; consider Standard SSD for dev |
| Cross-region + peering | Egress and both-sides peering charges | Co-locate chatty pairs; Private Link carefully |
| Reservations before right-size | Locks waste for 1–3 years | Right-size, observe, then commit; diary term end in `## Due` |

## Security baseline

| Check | Passing looks like |
|-------|--------------------|
| Global Administrator | Few, MFA, not daily-drive; monitored break-glass excluded from blocking CA |
| Human access | Entra ID + CA + MFA; privileged roles eligible via PIM, not standing |
| Workload credentials | Managed identity first; federated CI credentials; client secrets last + expiry in `## Due` |
| Storage | Shared-key disabled; public blob access off; short-lived user-delegation SAS |
| Key Vault | RBAC data plane; purge protection for production material; PE or tight firewall |
| Inbound | No `*`/`Internet` on 22/3389/1433/3306/5432; Bastion or JIT for admin |
| Azure SQL “Allow Azure services” | Off — `0.0.0.0` admits other tenants’ Azure resources |
| Data at rest | Platform encryption; host/CMK where regime requires |
| Audit | Diagnostic settings for Activity Log + critical resource logs; Defender free tier minimum |

## Service defaults

| Need | Default | Switch when |
|------|---------|-------------|
| Web app | App Service (Linux) | Scale-to-zero per request → Container Apps; K8s primitives → AKS |
| Event-driven code | Functions (Flex/Consumption as fit) | Long sustained duty cycle already in containers |
| Containers without K8s ops | Container Apps | Operators, meshes, multi-tenant NS → AKS |
| Relational DB | Azure SQL (serverless small / GP steady) | Engine/extensions (e.g. pgvector) → PostgreSQL Flexible Server |
| Global key-value | Cosmos DB | Heavy joins/reporting → Azure SQL |
| Cache / sessions | Azure Cache for Redis Standard | Persistence/cluster/PE needs → higher tier |
| Queue | Service Bus | Cheapest unordered → Storage Queue; streams → Event Hubs; fan-out → Event Grid |
| Global HTTP entry | Front Door Standard | Regional L7 + autoscaling backends → Application Gateway |
| Secrets | Key Vault + RBAC | Non-secrets stay in app configuration |
| Templates | Configured `iac_tool` | — |

## Output gates

Prefer the smallest safe next command that proves the claim. Before delivering architecture, policy, template, or command:

- Monthly cost stated for the **actual** region/subscription?
- Stored inventory **and** live subscription checked?
- Any data plane open to public internet or “all Azure services”?
- First quota and first timeout named?
- Immutable-at-create choices correct (partition key, redundancy, CNI, address space, region, Hyperscale)?
- Destructive commands isolated behind explicit confirmation?
- Durable session outputs written to the correct box?

## Traps

| Trap | Better move |
|------|-------------|
| Resource group as security boundary | NSG + PE + subscription isolation |
| Contributor to “fix access” | Classify denial; data-plane roles are separate |
| Client secrets for S2S | Managed identity / federated credentials; diary expiry if unavoidable |
| “Allow Azure services” on SQL/Storage | PE or explicit VNet rules |
| Portal VM delete = gone | Sweep disks/NICs/public IPs |
| Portal hotfix on IaC resources | Fix in code; preview every change |
| Complete-mode at wide scope | Incremental + deployment stacks / deny settings |
| Azure CNI on a tiny node subnet | Pre-compute IP need or use CNI Overlay |
| DR by reading the runbook only | Timed restore into a scratch RG |
| Quota request mid-incident | Request headroom before launch |
| Current-month Cost Analysis total only | Group by service/resource; prefer closed months |
| One giant RG | Split by lifecycle (platform / data / app) |
| Every Defender plan on day one | Free tier + secure score first; pay where detection value exists |

## Where experts disagree

- **Bicep vs Terraform** — Bicep: no state file, fast Azure resource coverage, live what-if. Terraform: multi-cloud, module ecosystems, existing remote-state discipline. Both beat portal-only.
- **AKS vs Container Apps** — Few always-on containers without operators → Container Apps; CRDs/meshes/multi-tenant NS → AKS. Break-even math, not taste.
- **Hub-and-spoke + Azure Firewall** — Right for regulated estates; often oversized for two-subscription startups. Start NSG + NAT + documented address plan.
- **Subscription-per-env vs RG-per-env** — Subscriptions win on hard isolation and showback; RGs keep small estates simple. Moving live resources across subscriptions later is a migration.
