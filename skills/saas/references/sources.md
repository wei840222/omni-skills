# Research Sources — saas

Gate 6 anchors for SaaS subscription metrics, packaging, retention, enterprise readiness, and margin discipline. Prefer primary standards, regulator guidance, and vendor docs over secondary growth blogs when rules conflict.

## Subscription metrics and revenue recognition

- **SaaS Capital — SaaS Metrics Guide** — MRR/ARR movement vocabulary and common KPI definitions via https://www.saas-capital.com/blog-posts/saas-metrics/
- **ChartMogul — SaaS metrics** — MRR movement components and churn framing via https://chartmogul.com/saas-metrics/
- **ProfitWell / Paddle — SaaS metrics** — retention and monetization KPI context via https://www.paddle.com/resources/saas-metrics
- **FASB ASC 606 overview (revenue from contracts with customers)** — deferred vs recognized revenue framing via https://www.fasb.org/page/PageContent?pageId=/standards/accounting-standards-updates.html
- **IFRS 15 revenue from contracts with customers** — contract revenue recognition baseline via https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/

## Packaging, entitlements, metering

- **Stripe — Billing / subscriptions** — subscription lifecycle, proration, and customer portal patterns via https://docs.stripe.com/billing/subscriptions/overview
- **Stripe — Usage-based billing** — meter events and aggregation patterns via https://docs.stripe.com/billing/subscriptions/usage-based-billing
- **Stripe — Entitlements** — feature access tied to products/prices via https://docs.stripe.com/billing/entitlements
- **OpenView — Product-led growth / packaging essays** — packaging and expansion framing via https://openviewpartners.com/blog/

## Trials, dunning, involuntary churn

- **Stripe — Smart Retries / dunning** — failed-payment retry and recovery patterns via https://docs.stripe.com/billing/revenue-recovery
- **Stripe — Customer emails for failed payments** — dunning communication baseline via https://docs.stripe.com/billing/revenue-recovery/customer-emails
- **Recurly — Dunning management** — retry windows and involuntary churn operations via https://docs.recurly.com/docs/dunning
- **Chargebee — Dunning** — failed-payment recovery configuration patterns via https://www.chargebee.com/docs/2.0/dunning.html

## Enterprise readiness, security, compliance

- **OWASP Application Security Verification Standard** — control baseline language for SaaS security reviews via https://owasp.org/www-project-application-security-verification-standard/
- **AICPA — SOC 2** — Trust Services Criteria entry for enterprise procurement via https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
- **Cloud Security Alliance — CCM** — cloud control catalogue often referenced in vendor reviews via https://cloudsecurityalliance.org/research/cloud-controls-matrix
- **GDPR official text** — personal-data processing baseline for EU buyers via https://eur-lex.europa.eu/eli/reg/2016/679/oj
- **NIST SP 800-53** — control families commonly mapped in security questionnaires via https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

## Multi-tenant isolation and cost-to-serve

- **NIST SP 800-145 — Cloud computing definition** — shared-responsibility / tenancy vocabulary via https://csrc.nist.gov/publications/detail/sp/800-145/final
- **AWS — SaaS Lens / Well-Architected** — multi-tenant isolation and noisy-neighbor framing via https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html
- **Google Cloud — Architecture framework** — multi-tenant design considerations via https://cloud.google.com/architecture/framework

## Sales tax / merchant-of-record caveats

- **Stripe Tax** — automated tax collection patterns vs self-registration via https://docs.stripe.com/tax
- **Paddle — Merchant of record** — MoR versus direct tax registration tradeoffs via https://www.paddle.com/help/start/intro-to-paddle/what-is-a-merchant-of-record

## Notes for agents

- Keep **SaaS business operations** (this skill) separate from list-price design (`pricing`), acquisition funnels (`growth`), payment implementation (`billing`), company finance (`cfo`), and single-deal closing (`b2b`).
- Quote every metric with formula and as-of date; rebuild the MRR movement bridge before trusting a dashboard total.
- Treat involuntary churn as a payments-recovery problem measured separately from voluntary cancel reasons.
- Prefer primary SOC/GDPR/NIST/vendor billing docs when enterprise procurement or tax nexus is in scope.
- Local state stays under portable `<state_root>/saas/` (plus shared contacts/projects); store credential **pointers** only.

## Obsolete / removed coupling

- Removed clawic.com homepage and `_meta.json` package registry metadata (Gate 5).
- Replaced hardcoded `~/Clawic/data/...` paths with portable `<state_root>/...` (Gate 3).
- Domain playbooks remain progressive sections inside `SKILL.md` (original package had no separate reference corpus beyond the entry skill); research anchors live in this file (Gate 6 / Gate 7).
