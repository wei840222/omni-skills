# Memory write protocol

Only file used when deciding **where** and **how** to persist durable growth outputs.

## Growth box — `<state_root>/growth/`

| Artifact | Destination | Threshold |
|---|---|---|
| Funnel / retention number | `memory.md` or dated metrics note | Include as-of date + definition |
| Channel start/scale/kill | `memory.md` | CAC, payback, kill number outcome |
| Experiment readout | `memory.md` / experiments log | Metric, horizon, decision |
| Loop named/falsified | `memory.md` | Steps + cycle time |
| Metric definition | `artifacts/metric-definitions.md` | Denominator/window/anchor |
| Forecast / target | `artifacts/` or `memory.md` | Assumptions listed |
| Config overrides | `config.yaml` | User-stated preferences only |

Maintain `memory.md` sections `## Boxes` (index of related files + conditions) and `## Due` (cadence rows).

## Shared boxes

| Kind | Path | Identity key |
|---|---|---|
| Paid spend | `<state_root>/finances/budget.md` | line item / period |
| Growth tooling cost | `<state_root>/finances/subscriptions.md` | tool name |
| Launch / initiative | `<state_root>/projects/<project>.md` | project slug |
| Agency / partner / interviewee | `<state_root>/contacts/contacts.md` | `Key` |

In shared boxes, update or delete **only rows this skill wrote**, matched on the identity key. Preserve foreign rows; announce each write/delete in one line.

## Credentials

Never store secrets. Pointers only. Drop PII-bearing raw exports; keep aggregates.
