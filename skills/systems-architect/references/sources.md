# Verified Primary Sources

Full URLs used for Gate 6 fact checks. Prefer these over memory when restating framework pillars, nines math, or SLO framing.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- Agent Skills best practices — https://agentskills.io/skill-creation/best-practices
- Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions

## Reliability and SRE

- Google SRE Book — Embracing Risk (error budgets, enough reliability not maximum) — https://sre.google/sre-book/embracing-risk/
- Google SRE Book — Service Level Objectives — https://sre.google/sre-book/service-level-objectives/
- Google SRE Book — Availability table (nines vs downtime) — https://sre.google/sre-book/availability-table/
- Google SRE Book — Monitoring distributed systems (golden signals) — https://sre.google/sre-book/monitoring-distributed-systems/
- Google SRE Workbook — https://sre.google/workbook/table-of-contents/

## Cloud architecture frameworks

- AWS Well-Architected Framework (operational excellence, security, reliability, performance efficiency, cost optimization, sustainability) — https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- AWS Well-Architected Reliability Pillar — https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
- Google Cloud Well-Architected Framework — https://docs.cloud.google.com/architecture/framework
- Microsoft Azure Well-Architected Framework pillars — https://learn.microsoft.com/en-us/azure/well-architected/

## Notes on claim freshness

- Framework pillar names and SRE error-budget framing are **stable-domain** and were verified reachable on 2026-10-08.
- Provider product SKUs, prices, and regional service inventories are **time-sensitive**; do not hard-code prices here — look up the provider skill or live docs at decision time.
- Availability minute budgets above are arithmetic from annual minutes; request-based SLIs remain preferred for globally distributed serving systems per SRE guidance.
