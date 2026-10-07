# Memory Template — DevOps

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — Configuration table keys and preference areas | `<state_root>/config.yaml` | Key by key, read-modify-write |
| Delivery observations, pain points, box index, due cadences | `<state_root>/memory.md` | Rewritten in place; stays small |
| Machines / runtime targets | shared `servers/servers.md` (beside state root or explicit path) | One row per host; pointer by name in devops files |
| People who own a service or carry a pager | shared `contacts/contacts.md` | One row per person; reference by name only |
| Tracked delivery work | shared `projects/<project>.md` | Summary only; procedures stay in artifacts |
| Hostnames and certificate expiry | shared `domains/domains.md` | One row per name |
| Delivery-tool spend | shared `finances/subscriptions.md` | One row per subscription |
| Service and environment map | `<state_root>/services/<service>.md` and/or `## Services` in memory until split | Born when first mapped |
| Releases with artifact identity and previous identity | `<state_root>/releases/<year>.md` | Append-only by year |
| Incidents, severities, postmortems | `<state_root>/incidents/<year>.md` | Append-only by year |
| SLOs and error-budget policy | `<state_root>/slos/<service>.md` | One file per service SLO set |
| Runbooks, cutover plans, pipeline files that finally worked, decisions | `<state_root>/artifacts/<kebab-name>.md` | Born as its own file |
| Credentials of any kind | Nowhere under `<state_root>/` or shared boxes | Pointer only |

## When to write

No permission needed beyond ordinary session consent; every write is announced in one line that names the file. In a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| A service or environment was mapped | Service/env note + `## Boxes` line |
| A pipeline was reshaped or a time budget accepted | `memory.md` pain/decision note and/or artifact |
| A release shipped, rolled back, or promoted | `<state_root>/releases/<year>.md` with artifact digests |
| An incident opened or closed | `<state_root>/incidents/<year>.md` |
| An SLO or error-budget policy was agreed | `<state_root>/slos/<service>.md` |
| A cadence was scheduled or run | `## Due` in `<state_root>/memory.md` |
| A runbook, cutover plan, or decision was produced | `<state_root>/artifacts/` |
| A preference was declared | `<state_root>/config.yaml` only |

## memory.md starter shape

```markdown
# DevOps Memory

## Status
status: ongoing
last: YYYY-MM-DD

## Boxes
<!-- dynamic index: condition — path under <state_root>/ -->

## Due
<!-- cadence | last run | owner | next -->

## Pain Points
<!-- recurring delivery friction -->

## Services
<!-- short pointers; split to services/ when long -->

## Preferences observed
<!-- never overrides config.yaml -->
```

## releases/<year>.md row

```markdown
| When | Service | Env | Artifact | Previous | Result | Notes |
|---|---|---|---|---|---|---|
| ISO-8601 | payments | prod | sha256:... / tag | sha256:... | ok \| rollback \| hotfix | link to incident/artifact |
```

## Secrets

Store pointers only: `env:DEPLOY_TOKEN` · `vault:secret/ci/deploy` · `1password:Work/CI/prod` · `ssm:/prod/db/password` · `file:~/.ssh/id_ed25519`.

**Keep:** service names, env names, digests, versions, dates, non-secret URLs, owner names. **Strip:** tokens, private keys, passwords, `.env` values, webhook secrets, connection strings with credentials.
