---
name: enterprise
description: >
  Navigate enterprise software delivery: legacy integration (strangler fig,
  anti-corruption layer, CDC sync), compliance-aware design (SOC 2, PCI, HIPAA,
  GDPR), stakeholder translation, ADRs, and buy-vs-build architecture trade-offs.
  Use when wrapping or replacing legacy systems, classifying data for audits,
  writing ADRs, or reconciling eng/product/security/finance/legal constraints at
  scale. Prefer `saas` for SaaS MRR/packaging/procurement checklists, `devops`
  for CI/CD and release mechanics, `b2b` for closing a named enterprise deal,
  `cybersecurity`/`security-best-practices` for deep control design, and
  `observability` for metrics/logs/tracing stacks once SLIs are chosen.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏢"}'
  related-skills: '{"b2b": "Qualify and close a named enterprise deal once architecture and compliance posture are clear.", "cloud": "Provider-specific Well-Architected or IAM detail after the enterprise topology decision.", "cybersecurity": "Deep control design, threat modeling, and security program detail beyond enterprise defaults.", "devops": "CI/CD, release, rollback, and change-management execution under the enterprise change policy.", "observability": "Metrics, logs, tracing, and alert routing once SLI/SLO targets are set.", "saas": "SaaS subscription metrics, packaging, and buyer procurement readiness (SSO/SCIM/SOC 2).", "security-best-practices": "General secure-defaults checklist when the ask is not enterprise process or legacy wrap."}'
---

This skill is **stateless knowledge guidance**. It does not store credentials, audit evidence, or durable customer data in the package. Treat compliance and architecture claims as time-sensitive; load `references/sources.md` and verify primary sources before irreversible decisions.

## When to load

Load for **enterprise software judgment**:

- Legacy wrap vs replace (strangler fig, ACL, CDC/database sync)
- Compliance implications of a data or architecture change (SOC 2, PCI DSS, HIPAA, GDPR)
- Stakeholder translation across engineering, product, security, finance, and legal
- ADR-backed buy-vs-build, monolith/microservices/serverless, sync vs async decisions
- Enterprise traps: internal-tool exemptions, missing rollback, undocumented commitments

Do **not** load as the primary skill for SaaS MRR/packaging math (`saas`), pipeline YAML or DORA mechanics (`devops`), a single named deal (`b2b`), deep threat modeling (`cybersecurity`), generic secure coding checklists (`security-best-practices`), or metrics stack wiring (`observability`). Building-code / IBC architecture (`architecture`) is a different domain.

## Workflow

1. Name the decision class: legacy integration, compliance/data class, stakeholder alignment, or architecture trade-off.
2. Inventory owners, dependents, SLA, docs, and data classification before proposing a change.
3. Load only the matching reference below; answer with the affirmative pattern, blast radius, and rollback path.
4. For irreversible cutovers, migrations, or compliance attestations, restate the exact change and wait for explicit authorization.

## Progressive disclosure

| Area | File | Load when |
|------|------|-----------|
| Legacy integration | `references/legacy.md` | Wrap/replace, strangler fig, ACL, CDC sync, assessment questions |
| Compliance design | `references/compliance.md` | SOC 2 / PCI / HIPAA / GDPR, data class, audit trails, residency |
| Architecture decisions | `references/architecture.md` | ADRs, buy-vs-build, sync/async, monolith vs services, anti-patterns |
| Sources | `references/sources.md` | Primary URLs and Gate 6 provenance before locking a claim |

## Core rules

1. **Legacy first** — assume existing systems until proven otherwise; integration cost usually dominates greenfield rewrite cost.
2. **Assess before touch** — owner, last deploy, dependents, docs, and SLA before any wrap or rewrite.
3. **Classify data early** — Public / Internal / Confidential / Restricted drives auth, encryption, DLP, and audit requirements.
4. **Translate stakeholders** — same decision restated in eng, product, security, finance, and legal language.
5. **Change with a rollback** — feature flags, migration path, and documented blast radius before hard switches.
6. **Compliance is design input** — ask who audits this and what evidence they need before shipping.
7. **Document decisions** — ADRs for major choices; undocumented commitments become silent liabilities.
8. **Secrets stay in vault** — store pointers (`env:…`, `vault:…`); keep secret values out of skill files and tickets.
9. **Observability from day one** — correlation IDs, SLI/SLO definitions, and alert budgets before launch.

## Delivery checklist

Before finishing:

- [ ] Decision class named; matching reference loaded
- [ ] Owner, dependents, SLA, and data class stated when relevant
- [ ] Rollback / migration path present for irreversible changes
- [ ] Compliance regime and evidence need named when data is in scope
- [ ] Adjacent skill used when the ask is SaaS metrics, CI/CD, deal close, or deep security
- [ ] Source claims re-checked via `references/sources.md` when statutes or frameworks matter

## Output shape

Lead with the recommended pattern, decision, or risk call. Put assessment tables, ADR drafts, and source citations after the deliverable unless the user only asked for a plan.

## On first use

1. Name the decision class and data class in one line.
2. Load only the matching reference; keep other references closed.
3. Answer with pattern + rollback; attach sources when statutes or frameworks are in play.
