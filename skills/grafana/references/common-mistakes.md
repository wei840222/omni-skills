# Common Mistakes

- Time range selector affects variable queries — unexpected results with "All time"
- Save and provision the dashboard with its required data source so imports resolve consistently.
- Manage dashboard alerts and Grafana Alerting as distinct systems; choose the intended alerting workflow explicitly.
- Panel queries run on every refresh — high-cardinality queries slow dashboard
- Annotation queries add DB load — use sparingly on busy dashboards
