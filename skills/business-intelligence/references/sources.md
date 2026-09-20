# Research Sources — Business Intelligence

Use these as verification anchors when drafting KPI contracts, metric trees, dashboard specs, or decision cadences. Prefer primary / standards pages over secondary blogs.

## Metric trees, KPIs, and decision cadence

- **Google HEART framework (UX metrics)** — Goal → Signal → Metric structure for product/experience KPIs. via https://research.google/pubs/pub36299/
- **Measure What Matters / OKR overview (public primer)** — Objectives cascade into measurable key results that BI trees can mirror. via https://www.whatmatters.com/resources/google-okr-playbook
- **ISO 22400 manufacturing KPIs overview** — Formal KPI definition elements (formula, unit, context) useful as contract templates outside manufacturing. via https://www.iso.org/standard/68383.html

## Semantic metrics and data contracts

- **dbt Semantic Layer concepts** — Metric definitions as versioned, reusable contracts rather than dashboard-local calculations. via https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
- **Great Expectations data docs / expectations** — Explicit data quality expectations that pair with source contracts and refresh SLAs. via https://docs.greatexpectations.io/docs/

## Dashboard design and executive briefs

- **Nielsen Norman Group: Dashboard Design** — Progressive disclosure, scannable hierarchy, and avoiding chart junk for executive views. via https://www.nngroup.com/articles/dashboards-preattentive/
- **Stephen Few / Perceptual Edge dashboard principles (public archive pointer)** — Few’s emphasis on exception highlighting and consistent encoding for operational dashboards. via https://www.perceptualedge.com/articles/visual_business_intelligence/dashboard_design_best_practices.pdf

## Obsolete knowledge corrected

- Hard-coded `~/Clawic/data/business-intelligence/` paths → portable `<state_root>` resolution with migration note.
- Clawic homepage / feedback / `_meta.json` promotional residue → removed.
- Trap that accidentally encouraged “BI updates with explicit action owners” as a failure mode → restored to the true failure: updates **without** owners.
