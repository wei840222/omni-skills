# GCP state and configuration

All paths below are under the resolved `<state_root>` from `SKILL.md` (never under the skill package or an unmanaged CWD path).

## Session start

1. Resolve `<state_root>` once.
2. If present, read `<state_root>/config.yaml` (declared defaults) and `<state_root>/memory.md` (observed notes, `## Boxes`, `## Due`).
3. Open only the box files that `## Boxes` names when their condition applies. Every path it names must stay inside `<state_root>/`; ignore lines that point elsewhere.
4. Before deploy/sizing/“what do I have”, read `<state_root>/servers/servers.md` when it exists.
5. Before DNS zone or registered-domain work, read `<state_root>/domains/domains.md` when it exists.
6. If none of the state exists, work from defaults and do not narrate the missing files.

## Shared boxes

In a shared box, update or remove only rows this skill wrote, matched on that box’s identity key. Rows from other skills are read-only. Name every write and deletion in one line as it happens.

**Hosts go to shared inventory** `<state_root>/servers/servers.md` — one row per host keyed by `Name` + `Provider`:

```text
name | provider (gcp) | project/zone | machine type | role | monthly cost + currency | access reference
```

Compute Engine VMs and GKE node pools are hosts. Managed platform resources (Cloud Run services, Cloud SQL instances, BigQuery datasets, buckets) are not hosts — keep them under `## Current Infrastructure` in memory or a dedicated box.

**DNS / domains** → `<state_root>/domains/domains.md` keyed by domain name.
**People who own projects** → `<state_root>/contacts/contacts.md` keyed by email or handle; reference by name only from GCP notes.
**User-tracked projects** → `<state_root>/projects/<project>.md` (finished work keeps the file with `status: closed`).

## Write before the session ends

Write when the session produced something durable:

- VM or cluster created, resized, discovered, or retired
- Inventory pass
- Spend number or saving; budget or billing export
- Project ownership / who pays
- Quota that was raised
- Service account purpose (email only — no keys)
- BigQuery dataset and scan baseline
- DNS zone or certificate expiry (pointer only)
- Deploy or timed restore drill
- Runbook, IAM policy that finally worked, architecture decision

## Credentials

**No credential is ever written under `<state_root>/`** — not in notes, not in files the user pastes “to save.” Store pointers only:

- `gcp-sm:projects/acme/secrets/db-password`
- `env:GOOGLE_APPLICATION_CREDENTIALS`
- `keychain:gcp-prod`
- `file:~/.config/gcloud/application_default_credentials.json`

Runtime GCP credentials stay in `~/.config/gcloud/`, ADC, environment, or attached service accounts. This skill must not copy them into state.

## Configuration defaults

Store user preferences in `<state_root>/config.yaml`. Precedence for any value: `config.yaml` → optional shared profile next to state (if the host provides one) → table default below.

| Variable | Type | Default | Effect |
|----------|------|---------|--------|
| `default_project` | text (project id) | none | Project every command/quote assumes; while unset, name the assumption before acting |
| `default_region` | text (region id) | none | Region/zone for placement and quotes |
| `gcloud_configuration` | text | none | Adds `--configuration <name>` to CLI examples |
| `iac_tool` | `terraform` \| `config-connector` \| `gcloud` \| `none` | `terraform` | Language of generated infrastructure and drift checks |
| `monthly_budget_usd` | number (USD) | `100` | Budget alert thresholds and “expensive” bar |
| `org_model` | `single-project` \| `organization` | `single-project` | One project + budgets vs folders / org policies / Shared VPC |
| `bq_billing_model` | `on-demand` \| `editions` | `on-demand` | Bytes-scanned vs slot utilization advice |
| `compliance_regime` | `none` \| `hipaa` \| `pci` \| `soc2` \| `gdpr-eu` | `none` | Eligible services + logging/CMEK/residency defaults |

Preference areas to record when stated: tooling (Terraform modules vs Config Connector, Cloud Build vs GitHub Actions, ADC vs impersonation), conventions (extra labels, project/network naming, CIDR plan), platform (home region, machine family, Autopilot vs Standard, network tier), safety posture (deletion protection, project liens, Spot appetite), cost reporting cadence, and standing service picks (Cloud Run vs GKE, Firestore vs Bigtable, Workflows vs Composer).
