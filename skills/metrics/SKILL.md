---
name: metrics
description: Load this skill to define, track, and report metrics using reusable dimensions
  and standardized formulas. Do not load it for general data entry.
metadata:
  openclaw: '{"emoji":"📊"}'
---
## State location

Metrics contracts, formulas, reports, and automation policies are persistent user state. Before reading or writing them, resolve `<state_root>` once for this invocation:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order: `<workspace>/metrics/`, `<workspace>/memory/metrics/`, then `~/metrics/`.
3. If more than one candidate exists, use only the highest-precedence directory and report the duplicate state locations; do not merge or synchronize them.
4. If none exists and the user confirms saving metrics data, create `<workspace>/metrics/`. If `<workspace>` is unavailable, ask for a state root instead of guessing from the current directory.

Use the selected `<state_root>` for every metrics read or write under `<state_root>/metrics/`. Keep skill resources under `references/`; never treat them as mutable user state.

## Setup

On first use, read `references/setup.md` for integration behavior and memory initialization.

## When to load

Load this skill when the user explicitly requests to define a metric contract, compute a standardized formula, or generate a structured report. Do not load this skill for general query generation unless metric tracking is explicitly required.

## Architecture

Working memory lives in `<state_root>/metrics/`. See `references/memory-template.md` for base structure and status behavior.

```
<state_root>/metrics/
├── memory.md              # HOT: goals, active metrics, reporting cadence
├── registry/              # WARM: metric contracts and dimension dictionaries
├── formulas/              # WARM: formula specs with version history
├── reports/               # WARM: report outputs by cadence and stakeholder
├── automations/           # WARM: scheduled checks and alert policies
└── archive/               # COLD: retired metrics and old report cycles
```

## Quick Reference

Load only the file needed for the current task to keep context focused.

| Topic | File |
|-------|------|
| Setup and integration | `references/setup.md` |
| Memory schema | `references/memory-template.md` |
| Metric contract design | `references/metric-registry.md` |
| Formula design and governance | `references/formula-playbook.md` |
| Report cadences and templates | `references/reporting-pack.md` |
| Automation and alerting patterns | `references/automation-patterns.md` |
| Data validation and quality gates | `references/data-quality.md` |
| Research sources | `references/sources.md` |

## Core Rules

### 1. Define a Metric Contract Before Any Calculation
Every metric must have one clear contract: business meaning, numerator, denominator, source tables, update latency, and owner.

Verify the metric contract is present and unambiguous before computing or comparing metrics.

### 2. Separate Raw Signals from Derived Metrics
Raw events are evidence. Metrics are interpreted aggregates. Keep them separate.

Store and reason in this order:
1. Raw signal
2. Normalized base metric
3. Derived metric
4. Decision recommendation

### 3. Use Dimensions to Scale, Not New One-Off Metrics
When users ask for "the same metric but by X", add a dimension instead of creating a duplicate metric.

Common high-value dimensions:
- Time grain
- Source/channel
- Segment/persona
- Geography
- Product or workflow stage

### 4. Version Formulas and Annotate Breaking Changes
Formulas evolve. Comparability fails when formula changes are not tracked.

For every formula update, store:
- version
- change reason
- impact expectation
- backfill policy
- first report date with new logic

### 5. Reports Must Be Decision-Oriented
A report is incomplete unless each section ties to a decision owner and explicit next action.

Minimum output block for every report:
- What changed
- Why it changed
- What to do now
- Who owns the action
- When to review again

### 6. Automate Thresholds with Response Playbooks
Alerts without response rules create noise.

Each threshold must include:
- trigger condition
- severity level
- owner
- first response action
- escalation condition

### 7. Prefer Reusable Reporting Packs Over Custom One-Offs
Build reusable templates for daily, weekly, monthly, and campaign reports so the system can scale across teams and domains.

Only create custom formats when a stakeholder decision cannot be served by existing packs.

## Common Traps

- Mixing different metric definitions under one name -> trend lines become invalid.
- Changing formulas without version notes -> historical comparisons break silently.
- Reporting totals without segment cuts -> root causes remain hidden.
- Creating too many vanity metrics -> operators lose focus on decision metrics.
- Sending alerts without action ownership -> teams ignore notifications.
- Adding one-off dashboards for every request -> reporting system becomes unmaintainable.

## Security & Privacy

**Data that leaves your machine:**
- None by default.

**Data that stays local:**
- Metrics context and definitions under `<state_root>/metrics/`.
- Formula versions, report logs, and alert policies stored locally.

**This skill does NOT:**
- Access files outside `<state_root>/metrics/` for memory storage.
- Send metrics to third-party APIs by default.
- Create background automations without explicit user confirmation.
