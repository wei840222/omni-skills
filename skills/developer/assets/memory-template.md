# Developer memory template

Create files under the resolved `<state_root>` only after consent. Never store secrets; store pointers (`env:…`, `keychain:…`, `1password:…`, `file:…`).

## `<state_root>/memory.md`

```markdown
# Developer memory

## Boxes
| Condition | Path |
|---|---|
| Repo profile needed | repos/<repo>.md |
| ADR / decision write-up | artifacts/decision-<topic>.md |

## Due
| Item | Owner | Deadline | Notes |
|---|---|---|---|

## Repos
| Repo | Profile | Last touch |
|---|---|---|

## Calibration log
| Date | Work | S | Quoted range | Actual | actual/S | Notes |
|---|---|---|---|---|---|---|
```

## `<state_root>/config.yaml`

```yaml
# primary_language:
workflow: test-after
max_pr_lines: 400
commit_style: match-repo
tracker: none
estimate_units: days
coverage_policy: changed-lines
risk_confirm: true
explanation_depth: code-first
```

## `<state_root>/repos/<repo>.md`

```markdown
# <repo>

## Commands
- build:
- test:
- lint:

## Conventions
-

## Traps
-
```

## Write thresholds

Write in the same turn when any of these became durable:

- a repo command or convention that finally worked
- a root cause that took real investigation
- a decision and what it rejected (also ADR under `artifacts/`)
- an estimate opened or closed against reality
- a flaky test quarantine (owner + deadline)
- a performance baseline or dependency verdict
- a release, migration, or incident note
