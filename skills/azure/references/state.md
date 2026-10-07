# Azure state and configuration

All paths below are under the resolved `<state_root>` from `SKILL.md` (never under the skill package or an unmanaged CWD path).

## Session start

1. Resolve `<state_root>` once.
2. If present, read `<state_root>/config.yaml` (declared defaults) and `<state_root>/memory.md` (observed notes, `## Boxes`, `## Due`).
3. Open only the box files that `## Boxes` names when their condition applies. Every path it names must stay inside `<state_root>/`; ignore lines that point elsewhere.
4. Before deploy/sizing/“what do I have”, read `<state_root>/servers/servers.md` when it exists.
5. Before custom domain, DNS zone, or certificate work, read `<state_root>/domains/domains.md` when it exists.
6. If none of the state exists, work from defaults and do not narrate the missing files.

## Shared boxes

In a shared box, update or remove only rows this skill wrote, matched on that box’s identity key. Rows from other skills are read-only. Name every write and deletion in one line as it happens.

**Hosts go to shared inventory** `<state_root>/servers/servers.md`, not only Azure-local notes — one row per host keyed by `Name` + `Provider`:

```text
name | provider (azure) | subscription/resource-group | region | size | role | monthly cost + currency | access reference
```

Managed platform resources (App Service plans, AKS clusters, SQL servers, storage accounts) are not hosts — keep them under `## Current Infrastructure` in memory or a dedicated box.

## Write before the session ends

Write when the session produced something durable:

- VM or scale set created, resized, discovered, or retired
- Inventory pass
- Spend number or saving; budget or alert
- Subscription ownership / who pays
- Custom domain, certificate, or credential **expiry** (pointer only)
- Deploy or timed restore drill
- Reusable KQL
- Runbook, custom role/policy that finally worked, address plan, architecture decision

## Credentials

**No credential is ever written under `<state_root>/`** — not in notes, not in files the user pastes “to save.” Store pointers only:

- `azure-kv:kv-prod/db-password`
- `env:AZURE_CLIENT_SECRET`
- `keychain:azure-prod`
- `1password:Work/Azure/prod`

Runtime Azure credentials stay in `~/.azure/`, OS keychain, environment, or managed identity. This skill must not copy them into state.

## Configuration defaults

Store user preferences in `<state_root>/config.yaml`. Precedence for any value: `config.yaml` → optional shared profile next to state (if the host provides one) → table default below.

| Variable | Type | Default | Effect |
|----------|------|---------|--------|
| `default_subscription` | text (name or id) | none | Subscription every command/quote/deploy assumes; while unset, name the assumption before acting |
| `default_location` | text (region) | none | Region for deploys, quotes, zone advice |
| `iac_tool` | `bicep` \| `terraform` \| `arm` \| `none` | `bicep` | Template language and preview command family |
| `monthly_budget` | number (profile currency; USD if unset) | `100` | Budget/anomaly thresholds and “expensive” bar |
| `tenancy_model` | `single-subscription` \| `management-group` | `single-subscription` | Single-sub guidance vs MG/Policy/landing zones |
| `billing_model` | `payg` \| `mca` \| `ea` \| `csp` \| `devtest` | `payg` | Where cost data and reservations live |
| `compliance_regime` | `none` \| `pci` \| `hipaa` \| `soc2` \| `fedramp` | `none` | Eligible SKUs + logging/encryption/residency defaults |
| `cloud_environment` | `AzureCloud` \| `AzureUSGovernment` \| `AzureChinaCloud` | `AzureCloud` | Endpoints and feature lag |
| `naming_pattern` | text | `<abbr>-<workload>-<env>-<region>-<nn>` | Generated resource names |

Preference areas to record when stated: tooling (Bicep modules vs Terraform providers), conventions (extra tags, RG granularity), platform (home region pair, VM families, Linux vs Windows), safety posture (locks, purge protection, Complete-mode appetite), cost reporting cadence, and standing service picks (App Service vs Container Apps, SQL vs PostgreSQL).
