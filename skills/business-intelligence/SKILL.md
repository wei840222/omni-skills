---
name: business-intelligence
description: >
  Establish business intelligence systems, define KPIs, and structure metric
  trees to drive data-informed executive decisions. Trigger this when building
  dashboards, defining metric contracts, or setting up review cadences.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📊","os":["linux","darwin","win32"],"displayName":"Business Intelligence"}'
  related-skills: '{"analytics":"Performance pattern analysis after KPI contracts exist.","data-analysis":"Trend, segment, and causal modeling underneath BI trees.","dashboard":"Visualization implementation once metric contracts are fixed.","strategy":"Outcome framing that BI trees and cadence must serve.","report":"Stakeholder narrative packaging for decision briefs."}'
---

## When to load

Load this skill to structure business intelligence workflows, establish KPI contracts, map metric trees, design executive dashboards, or define operating review rituals.

Prefer adjacent skills when they fit better:

- Raw trend / segment modeling without executive cadence → `data-analysis` or `analytics`
- Chart implementation after contracts exist → `dashboard`
- Strategy framing before metrics → `strategy`
- Stakeholder narrative packaging → `report`

## Setup

On first use, read `references/setup.md` for integration behavior and memory initialization.

## State location

Business-intelligence state may exist in `<workspace>/business-intelligence/`,
`<workspace>/memory/business-intelligence/`, or `~/business-intelligence/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/business-intelligence/`, `<workspace>/memory/business-intelligence/`, `~/business-intelligence/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to `<workspace>/business-intelligence/`.

Use the selected `<state_root>` for every state operation in this skill.
Never write runtime state into this skill package.
Do not store credentials, customer PII dumps, financial account numbers, or unrestricted raw data extracts under `<state_root>/`.

If older data lives at `~/Clawic/data/business-intelligence/`, migrate it into the
resolved `<state_root>/` and state the move in one line.

Optional layout:

```text
<state_root>/
├── memory.md                # HOT: goals, KPI ownership, active decisions
├── metric-tree/             # WARM: objective -> driver -> metric maps
├── kpi-contracts/           # WARM: metric definitions and formula versions
├── dashboard-specs/         # WARM: visualization and drill-down specifications
├── insight-briefs/          # WARM: weekly and monthly decision briefs
├── operating-cadence/       # WARM: review rituals and escalation rules
└── archive/                 # COLD: retired KPIs and past planning cycles
```

## Architecture

Working memory lives under the resolved `<state_root>/`. See `assets/memory-template.md` for base structure and status behavior.

## Quick Reference

Load only the file needed for the current task to keep context focused.

| Topic | File |
|-------|------|
| Setup and integration | `references/setup.md` |
| Memory schema | `assets/memory-template.md` |
| Objective and metric tree design | `references/metric-tree.md` |
| KPI definition contracts | `references/kpi-dictionary.md` |
| Dashboard and drill-down design | `references/dashboard-specs.md` |
| Decision brief templates | `references/insight-briefs.md` |
| Review rituals and escalation rules | `references/decision-cadence.md` |
| Source quality and data contracts | `references/data-contracts.md` |
| Research sources | `references/sources.md` |

## Core Rules

### 1. Start from Decision Questions, Not Charts
Every BI request must begin with one decision question and one owner.

If there is no decision owner, the output is reporting noise and should be reframed before building metrics.

### 2. Build a Metric Tree Before Dashboard Design
Map each business objective to drivers, then drivers to measurable KPIs.

Always build a metric tree prior to dashboard design. Dashboards without a metric tree create disconnected charts and contradictory narratives.

### 3. Enforce KPI Contracts
Each KPI needs a written contract: definition, formula, grain, source, refresh cadence, owner, and valid interpretation window.

Ensure formulas and source logic remain consistent across periods before comparing KPI values, or provide clear annotations explaining any variance.

### 4. Separate Leading and Lagging Indicators
For every lagging KPI, define at least one leading indicator that signals future movement.

If the system only tracks lagging outcomes, intervention happens too late.

### 5. Brief Insights in Decision Format
Every insight output must include:
- What changed
- Why it changed
- Confidence level
- Recommended action
- Action owner and due date

A BI summary without an action owner is incomplete.

### 6. Standardize Dashboard Specs Across Teams
Use consistent metric naming, time windows, segment logic, color semantics, and drill-down paths.

Inconsistent dashboard specs make cross-team comparisons invalid.

### 7. Run a Fixed Operating Cadence
Define daily, weekly, monthly, and quarterly BI rituals with clear participants and escalation triggers.

Without a fixed cadence, KPI review becomes reactive and decision quality degrades.

## Business Intelligence Traps

- Starting with visualization tooling before KPI contracts -> expensive dashboards with weak decisions.
- Tracking too many KPIs per objective -> teams lose focus on actual drivers.
- Blending forecast assumptions with actuals in one number -> executives make false confidence calls.
- Changing formulas without version notes -> historical trend comparisons become invalid.
- Reporting movement without attribution depth -> teams cannot identify correct interventions.
- Sending BI updates without action owners -> insights stay informational and never convert into execution.

## External Endpoints

This skill makes NO external network requests.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

No data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Nothing by default.

**Data that stays local:**
- BI context, KPI contracts, and reporting notes under `<state_root>/`.
- Decision cadence and retrospective notes stored locally when memory is enabled.

**This skill does NOT:**
- Access files outside `<state_root>/` for memory storage.
- Transmit metrics or business data to third-party APIs by default.
- Create background automations without explicit user confirmation.
- Modify its own skill definition files.
