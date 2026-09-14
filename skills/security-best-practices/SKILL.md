---
name: security-best-practices
description: >
  Review code with secure-by-default standards, prioritize exploitable risks,
  and deliver evidence-backed minimal-diff fixes. Use for security reviews,
  hardening guidance, severity scoring, and safe remediation planning. Prefer
  `auth`, `authorization`, `encryption`, `firewall`, or `devops` when the task
  is domain-specific rather than a general security review.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛡️"}'
  related-skills: '{"auth":"Authentication design and session hardening when the finding is authn-specific.","authorization":"Access-control and permission-boundary design when the finding is authz-specific.","encryption":"Key management and cryptographic hygiene beyond generic secret handling.","firewall":"Network exposure and policy controls outside application-layer review.","devops":"Secure delivery, CI checks, and operational safeguards for shipping fixes."}'
---

## When to load

Load this skill to enforce secure-by-default standards, prioritize exploitable risks, and provide actionable security guidance or remediations.

## State location

Optional review preferences, findings history, and accepted-risk notes may live under `<state_root>/security-best-practices/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/security-best-practices/`, `<workspace>/memory/security-best-practices/`, `~/security-best-practices/`.
3. If none exists and the user asks to persist review context, create `<workspace>/security-best-practices/` after explicit consent.

On first use, read `references/setup.md` for integration guidelines.
If local memory is needed, ask for consent before creating files under the resolved state root. See `references/memory-template.md`.

```text
<state_root>/security-best-practices/
|- memory.md        # Stable context, preferences, and activation boundaries
|- findings-log.md  # Findings registry with severity and status
`- exceptions.md    # Approved security exceptions and review dates
```

## Quick Reference

Load only the minimum file needed for the current request.

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `references/memory-template.md` |
| Full review workflow | `references/review-playbook.md` |
| Severity model and scoring | `references/severity-model.md` |
| Safe remediation patterns | `references/remediation-patterns.md` |
| Risk exception guidance | `references/exceptions.md` |

## Core Rules

### 1. Establish Scope and Evidence First
Before any conclusions, confirm:
- System boundary (service, module, endpoint, or workflow)
- Stack evidence (language, framework, deployment context)
- Threat assumptions (external attacker, internal misuse, privilege level)

No evidence, no finding.

### 2. Map Risks to a Repeatable Baseline
Evaluate every review against a consistent baseline:
- Authn/authz boundaries
- Input validation and output encoding
- Secrets handling and configuration safety
- Dependency and supply chain posture
- Logging, error handling, and data exposure controls

Use `references/review-playbook.md` to keep scans systematic instead of ad hoc.

### 3. Produce Findings That Are Verifiable
Each finding must include:
- Severity from `references/severity-model.md`
- File path and line references
- Concrete evidence snippet
- Impact statement in plain language
- Minimal safe fix direction

Ensure all findings are strictly backed by verifiable repository evidence.

### 4. Prioritize Exploitability Over Theory
Rank by practical risk, not by checklist volume:
- Reachability from untrusted inputs
- Privilege required by attacker
- Blast radius if exploited
- Ease of abuse and repeatability

High confidence, exploitable issues come first.

### 5. Remediate With Minimal Product Risk
Fix one finding at a time:
- Prefer small diffs that preserve existing behavior
- Add tests when security fixes alter code paths
- Flag expected behavior changes before implementing
- Re-run project validation after each fix batch

Use `references/remediation-patterns.md` for safe rollouts.

### 6. Respect Explicit Exceptions and Ownership
If the user accepts a known risk:
- Record rationale in the local exceptions log under the resolved state root (template in `references/exceptions.md`)
- Define expiry or next review date
- Keep the exception scoped to the specific context

Require explicit, scoped justification for every override.

## Security Review Traps

- Reporting generic best practices without file evidence -> low-trust output that teams cannot action.
- Flooding with low-severity noise -> critical vulnerabilities get ignored.
- Proposing major refactors as "quick fixes" -> teams reject security work due to delivery risk.
- Ignoring framework defaults and deployment context -> false positives and wrong remediations.
- Declaring a system "secure" after one pass -> hidden regressions remain untested.

## Security & Privacy

**Data that leaves your machine:**
- None by default from this skill itself.

**Data that stays local:**
- Review preferences and finding history under the resolved state root.
- Exception rationale in local memory files only.

**This skill does NOT:**
- Exfiltrate source code to undeclared third-party endpoints.
- Mark unresolved risks as fixed.
- Perform hidden destructive changes.
