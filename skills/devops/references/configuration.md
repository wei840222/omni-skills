# Configuration detail

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| ci_platform | github-actions \| gitlab-ci \| jenkins \| buildkite \| circleci \| azure-devops \| none | none | Dialect of every pipeline example and the cache backend recommended in *Quick Reference / Core Rules (pipeline budget)*; while unset, name the platform being assumed before writing a pipeline file |
| iac_tool | terraform \| opentofu \| pulumi \| cloudformation \| cdk \| ansible \| none | terraform | Language and workflow of *Quick Reference (IaC) / Core Rule 9*, including the drift-check and policy-gate commands |
| deploy_model | push \| gitops | push | Whether deploys are pipeline-driven (*Release Strategies*) or reconciled from a repo (*Where Experts Disagree / deploy_model*) |
| environment_chain | list | [dev, staging, prod] | The promotion path in *Quick Reference (parity / ephemeral env)*; each added environment adds a gate, a config set, and a cost line |
| deploy_strategy_default | rolling \| blue-green \| canary \| recreate | rolling | Standing choice in Release Strategies and the shape of every generated deploy plan |
| version_scheme | semver \| calver \| git-sha | git-sha | Identity stamped on artifacts and releases, and what `<state_root>/releases/<year>.md` records |
| pipeline_time_budget_min | number (min, 1-120) | 10 | The PR-feedback ceiling Rule 4 enforces and the threshold for calling a pipeline slow |
| slo_target_pct | number (90-99.999) | 99.9 | Default availability target, its error budget, and every burn-rate threshold in *Error Budgets And Paging / Core Rule 7* |
| secrets_backend | vault \| aws-secrets-manager \| gcp-sm \| azure-kv \| sops \| 1password \| ci-native | ci-native | Where *Core Rule 6 / Security & Privacy* puts secrets, what the pointer scheme looks like, and how rotation is described |
| observability_stack | prometheus-grafana \| datadog \| cloudwatch \| new-relic \| elastic \| otel-generic \| none | none | Query dialect and cost model in *Quick Reference (instrumentation)* and *Error Budgets And Paging / Core Rule 7* |
| oncall_model | none \| business-hours \| rotation-24x7 \| follow-the-sun | business-hours | Rotation sizing, escalation, and severity definitions in *Quick Reference (on-call/incident)*; also whether paging advice applies at all |
| approval_gate | none \| prod-only \| all | prod-only | Where a human approval sits in the promotion path, and what evidence the pipeline must capture for it |
| compliance_regime | none \| soc2 \| iso27001 \| pci \| hipaa \| fedramp | none | Forces separation of duties, retention, and audit-evidence capture into the pipeline and the artifact list |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — artifact registry, feature-flag system, paging provider, load-testing tool, policy engine, dependency-update bot — affects which product's shape every example takes
- **Conventions** — branch model (trunk-based vs release branches), tag and release naming, environment naming, service ownership metadata, runbook location — affects generated files and *DORA Scoreboard / Core Rule 3*
- **Platform** — where workloads run (single host, VMs, containers, serverless, managed platform), cloud provider, region and data-residency constraints — affects *Quick Reference (Little's law)*, *Quick Reference (restore drills)*, and every cutover plan
- **Safety posture** — appetite for automated rollback, whether destructive commands are emitted at all, blast-radius limits per change, freeze windows — affects Output Gates and *Release Strategies*
- **Work order** — review gates, who approves what, whether migrations ship with or ahead of code, pairing on production changes — affects the promotion path in *Quick Reference (parity / ephemeral env)*
- **Compliance and restrictions** — the CVE remediation SLA per severity (*Quick Reference (provenance/CVE)*), audit-evidence and log retention floors, data-residency limits, separation-of-duties requirements, vetoed technologies or registries — recorded under a `compliance` block in `config.yaml`; `compliance_regime` sets the ones a regime dictates, the rest are the user's own
- **Cadence** — restore drills, game days, secret rotation, access review, dependency refresh, SLO and alert review, postmortem action sweeps — every accepted cadence becomes a row in the `## Due` table of `<state_root>/memory.md`
- **Output register** — plan-first vs command-first, how much reasoning to keep, whether to produce diffs or whole files, incident-comms tone — affects every answer's shape

## Writing rules

- Write a key only when the user states the preference — never from an observation alone.
- Read-modify-write: load the existing file, set only the declared key, keep every other key.
- Never invent live credentials, account IDs, or webhook URLs into `config.yaml`.
