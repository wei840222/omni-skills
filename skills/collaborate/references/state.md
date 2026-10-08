## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
| --- | --- | --- | --- |
| round_cap | number (1-5) | 3 | Hard halt in Running the Exchange; the two-round no-movement rule still fires first |
| budget_share | number (% of task estimate) | 10 | Scales Rule 3's exchange budget; the 5 min floor and 30 min cap stay fixed |
| solo_undo_threshold | number (minutes) | 15 | Undo cost below this (with blast radius limited to you) routes to solo in the routing checks |
| counterpart_mode | auto \| recruit \| simulate | auto | auto recruits a real human or agent when one is reachable, otherwise simulates the counter-mindset; recruit/simulate force one side |
| log_decisions | bool | true | Append every convergence record to `<state_root>/decisions.md` |

Preference areas to record as the user reveals them:

- **counterpart pool** — who is recruitable (teammates, review groups, other agents, nobody) — resolves `counterpart_mode` and shapes Counterpart Selection
- **record conventions** — where decisions live (team ADRs, repo docs, the decision log) and their format — affects Convergence and `decision-log.md`
- **escalation path** — who breaks deadlocks and what counts as blocking — affects `deadlock.md`
- **critique register** — how blunt critique to and from humans should be — affects `with-humans.md` and `group-review.md`

## State files

| Path | Purpose |
| --- | --- |
| `<state_root>/config.yaml` | Persisted configuration overrides |
| `<state_root>/decisions.md` | Convergence / disagree-and-commit records |

Do not write skill package resources into `<state_root>`. Resolve `<state_root>` once per invocation using the State location section in `SKILL.md`.
