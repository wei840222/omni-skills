# Common Mistakes

- Time range selector affects variable queries — unexpected results with "All time"
- Dashboard saved but datasource not — works locally, breaks on import
- Alert rule in dashboard vs Grafana alerting — different systems, don't mix
- Panel queries run on every refresh — high-cardinality queries slow dashboard
- Annotation queries add DB load — use sparingly on busy dashboards
