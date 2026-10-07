# DevOps sources (Gate 6)

Checked 2026-10-07. Re-open the live page before restating benchmarks, UI labels, product limits, or numerical defaults as if they were universal SLOs.

## Agent Skills format

- **Agent Skills specification** — normative skill format.
  - https://agentskills.io/specification
- **Document index (llms.txt)** — entry map for the spec set.
  - https://agentskills.io/llms.txt
- **skills-ref validator** — reference validation tooling.
  - https://github.com/agentskills/agentskills/tree/main/skills-ref

## DORA and delivery performance

- **DORA research program** — four key metrics framing and research entry.
  - https://dora.dev/research/
- **DORA 2024 Accelerate State of DevOps report announcement** — current public report pointer (re-open before quoting band numbers as certification thresholds).
  - https://cloud.google.com/blog/products/devops-sre/announcing-dora-2024-accelerate-state-of-devops-report

## SRE, SLOs, and alerting

- **Google SRE Book (ToC)** — foundational reliability concepts.
  - https://sre.google/sre-book/table-of-contents/
- **Google SRE Workbook (ToC)** — practical workbook entry.
  - https://sre.google/workbook/table-of-contents/
- **Alerting on SLOs (SRE Workbook)** — burn-rate multi-window alerting model used as teaching default in this skill.
  - https://sre.google/workbook/alerting-on-slos/

## Pipeline identity and deploy hardening

- **GitHub Actions — security hardening with OpenID Connect** — OIDC federation for cloud deploys; token lifetime and trust boundary are product-specific — verify on the live page before stating durations as universal.
  - https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- **SLSA specification v1.0 levels** — provenance maturity levels for artifacts.
  - https://slsa.dev/spec/v1.0/levels

## Feature flags, GitOps, and IaC orientation

- **OpenFeature** — vendor-neutral feature-flag standard orientation.
  - https://openfeature.dev/
- **OpenTofu documentation** — open Terraform-compatible IaC tooling.
  - https://opentofu.org/docs/
- **CNCF Argo** — GitOps project family entry.
  - https://www.cncf.io/projects/argo/
- **Flux** — GitOps continuous delivery.
  - https://fluxcd.io/flux/

## Security baseline cross-check

- **OWASP Top Ten** — application risk classes that often surface in delivery and dependency pipelines.
  - https://owasp.org/www-project-top-ten/

## What this skill does not treat as a live measurement

DORA elite-band orientations, canary "rule of three" sample sizing, default `pipeline_time_budget_min` (10), default SLO 99.9% burn-rate table, and OIDC "~1h job token" language are **teaching defaults** drawn from the sources above or common platform behavior — not universal certifications or guarantees. Product token lifetimes, list prices, UI labels, and report band cutoffs move; quote them only after opening the live page.
