# Sources — alerts

Gate 6 research anchors for alerting design. Prefer vendor primary docs and SRE references over listicles. Re-verify product UI paths and API fields before quoting exact clicks or payloads.

## SRE and alert design

- [Google SRE Book — Alerting on SLOs](https://sre.google/sre-book/alerting-on-slis/) — symptom- vs cause-based alerting, burn rates, and human attention as a finite resource.
- [Google SRE Workbook — Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — practical multi-window multi-burn-rate patterns.
- [Prometheus Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) — rule syntax and annotation practices.
- [Alertmanager configuration](https://prometheus.io/docs/alerting/latest/configuration/) — `group_by`, inhibition, routes, and repeat intervals.

## Incident and webhook ecosystems

- [PagerDuty — Incident Response / event APIs overview](https://developer.pagerduty.com/docs/events-api-v2/overview/) — event semantics and severity mapping (verify current API version).
- [Slack API — messaging and authenticity](https://api.slack.com/authentication/verifying-requests-from-slack) — request signing and replay window patterns applicable to inbound webhooks.
- [OWASP — Webhook security considerations](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) — TLS, auth, and input validation posture for HTTP callbacks.

## Status communication

- [Atlassian Statuspage docs](https://support.atlassian.com/statuspage/) — component and incident update norms (or the user's chosen status product docs).

## Practice notes for this skill

- Threshold numbers in SKILL.md (5m cooldown, 85% success floor, 2× latency) are **starting defaults**; replace with the user's measured baselines.
- Agent-loop and silent-failure checks are operational heuristics, not medical or legal standards.
- Obsolete packaging removed in this refactor: Clawic homepage, top-level `slug`/`homepage`, and `_meta.json`.
