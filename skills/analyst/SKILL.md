---
name: analyst
description: >
  Extract insights from datasets with SQL, visualization, and clear stakeholder
  communication. Use when framing data questions, validating quality before
  aggregates, writing readable queries, choosing charts, or turning findings into
  decisions. Not for product analytics product setup (Umami/Plausible/PostHog),
  pure CSV dialect repair, or spreadsheet workbook editing as the primary task.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔍"}'
  related-skills: '{"spreadsheet":"Workbook or sheet analysis when the primary surface is Excel/Sheets cells rather than SQL or BI queries.","csv":"Delimiter, encoding, and RFC 4180 interchange when the hard problem is file dialect rather than insight.","sql":"Deep SQL dialect, schema design, or engine-specific optimization beyond analysis patterns.","statistics":"Formal statistical tests, power, and inference when the ask is methods-first rather than business analysis.","data":"General data plumbing, pipelines, and warehouse ops outside decision-facing analysis.","analytics":"Product analytics tooling deployment and privacy APIs (Umami/Plausible/PostHog), not ad-hoc insight work."}'
---

## State location

This skill is primarily **stateless routing knowledge**. Optional analysis notes may exist in `<workspace>/analyst/`, `<workspace>/memory/analyst/`, or `~/analyst/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/analyst/`, `<workspace>/memory/analyst/`, `~/analyst/`.
3. If none exists and the user wants notes kept, create `<workspace>/analyst/` after confirmation.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/analyst/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants durable assumptions, metric definitions, or open questions kept across sessions. Never write the literal string `<state_root>` to disk. Legacy `~/Clawic/data/analyst/` is a migration source only—keep it out of the active lookup order.

## When to load

Load for decision-facing **data analysis** work:

- framing the decision, hypothesis, and success metric before querying
- data-quality checks (row counts, date ranges, nulls, duplicates, source definitions)
- readable SQL (CTEs, aggregate-before-join, windows, CASE)
- cohorts, time series with seasonality, segmentation
- chart/table choice and stakeholder-ready findings
- common analysis failure modes (wrong question, cherry-picking, overfitting, dashboard noise)

Route away when the primary task is:

- product analytics product install / GDPR API setup → `analytics`
- CSV/TSV dialect repair or generation → `csv`
- native workbook cell edits and format preservation → `spreadsheet`
- engine-level SQL schema design or deep optimizer work → `sql`
- formal hypothesis tests as the main deliverable → `statistics`
- pipeline/warehouse ops → `data`

Read `references/sources.md` before repeating industry benchmarks, statistical rules of thumb, or vendor-specific SQL extensions as hard facts. Prefer live schema/docs for the user's warehouse.

## When to load references

Load the smallest reference that matches the current need; keep this file as the entry point.

| Need | File |
|------|------|
| Verified source URLs (Gate 6) | `references/sources.md` |
| Framing questions and scope | `references/framing.md` |
| Data quality checklist | `references/data-quality.md` |
| SQL patterns | `references/sql-patterns.md` |
| Analysis approaches (cohorts, seasonality, segments) | `references/analysis-approach.md` |
| Charts and tables | `references/visualization.md` |
| Stakeholder communication | `references/communication.md` |
| Tools and reproducibility | `references/tools.md` |
| Common mistakes blacklist | `references/mistakes.md` |

## Operating rules

1. **Decision first** — restate the decision, who acts, and what would change their mind before heavy querying.
2. **Quality before aggregates** — check row counts, date coverage, null rates, join fan-out, and metric definitions.
3. **Readable SQL** — prefer CTEs; aggregate before joining when cardinality allows; comment non-obvious filters.
4. **Simple cuts first** — start with the coarsest useful slice; add cohorts/segments only when they change the answer.
5. **Seasonality-aware time series** — compare like periods; flag holidays, launches, and incomplete trailing days.
6. **One message per chart** — match chart type to the question; use tables when exact values matter.
7. **Lead with the insight** — answer so-what / now-what; label recommendations as opinions; state confidence limits.
8. **Reproducibility** — prefer scripts and versioned queries over one-off clicks for recurring work.

## Safety and data boundaries

- Do not exfiltrate PII, credentials, warehouse connection strings, or production dumps into chat logs or skill files.
- Prefer aggregated or redacted samples in examples; use unmistakable placeholders for real customer identifiers.
- Do not run destructive warehouse writes, drop tables, or grant broad access without explicit authorization.
- Treat correlation as a lead, not proof of causation; do not oversell noisy or underpowered results.
- When metric definitions disagree across teams, surface the conflict instead of silently picking one.

## Core loop

1. Lock framing (`references/framing.md`): decision, hypothesis, scope, success metric.
2. Run data-quality checks (`references/data-quality.md`) on the candidate tables/files.
3. Write the smallest readable query (`references/sql-patterns.md`); expand only if needed.
4. Choose analysis cut and visualization (`references/analysis-approach.md`, `references/visualization.md`).
5. Deliver findings (`references/communication.md`) with confidence and next actions.
6. Optionally persist metric definitions and open questions under `<state_root>/memory.md` after approval.
