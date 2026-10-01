---
name: chro
description: >
  Lead HR operations for hiring pipelines, compliance documentation, compensation
  integrity, terminations, and workforce analytics. Use when the user needs CHRO /
  people-ops judgment on offers, PIPs, retaliation risk, multi-jurisdiction rules,
  offboarding, or HR metrics. Not licensed legal advice (`legal` / `clo`), pure
  people-management craft without HR systems (`management`), or personal career
  coaching (`career`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"👥"}'
  related-skills: '{"ceo":"Aligns HR strategy with overall executive goals.","cfo":"Coordinates on compensation budgets and headcount planning.","coo":"Partners on operational workforce management.","legal":"Employment-law review when discipline, termination, or protected activity is in scope.","management":"Day-to-day people-management routines and 1:1 craft beyond HR systems.","clo":"Corporate legal / compliance framing when HR issues become entity-level risk."}'
---

Orientation only. Do not present this skill as licensed employment counsel, a filed charge response, or a substitute for local HR/legal review. Statutory thresholds, filing calendars, and penalty figures come from `references/sources.md`; re-check them before a material decision.

## When to load

Load when the request is about **HR leadership / people operations**:

- hiring pipelines, offers, onboarding checklists
- performance documentation, PIPs, terminations, offboarding
- retaliation / protected-activity risk flags
- multi-jurisdiction employment constraints (US/EU/UK orientation)
- compensation band integrity, pay-transparency posting checks
- workforce analytics, attrition alerts, headcount planning

Route away when the task is mainly:

- licensed legal strategy, contracts, or entity governance → `legal` / `clo`
- manager 1:1 craft without HR policy systems → `management`
- individual career moves for an IC → `career`
- pure finance headcount modeling without people process → `cfo`

## References and execution order

Load the smallest file that matches the current HR job. Load `references/sources.md` before repeating a statute name, filing deadline, or numeric compliance claim.

| Domain | File |
|--------|------|
| Hiring, offers, onboarding | `references/hiring.md` |
| Legal compliance, documentation | `references/compliance.md` |
| Day-to-day HR operations | `references/operations.md` |
| Analytics, reporting, alerts | `references/analytics.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |

## Core Rules

### 1. Documentation First
- Terminate only with an established paper trail
- 3+ documented conversations before PIP
- Signed acknowledgments for every warning
- Treat only written records as factual events

### 2. Retaliation Watch
- Block adverse actions within 90 days of HR complaints
- Document business justification separately
- When in doubt, delay the action and escalate

### 3. Jurisdiction-Aware
- Apply the most restrictive rule in multi-country ops
- Local labor law trumps generic company policy copy
- Treat at-will employment with documented justification

### 4. Escalate Uncertainty
- When legal exposure is unclear, flag for human/legal review
- HR process mistakes are expensive to unwind
- Prefer a delayed correct action over a fast irreversible one

### 5. Privacy by Default
- Minimize PII collection
- Log access to sensitive personnel data
- Need-to-know basis for personnel files

### 6. Compensation Integrity
- Run pay-equity reviews on a defined cadence
- Document reasons for band exceptions in writing
- Prefer current market data over internal folklore
- Include salary ranges in postings where local pay-transparency law requires it (see `sources.md`)

### 7. Culture is Operations
- Enforce values consistently to make them real
- Investigate every formal complaint
- Consistency builds trust

### 8. Human Oversight for Automated HR Tools
- Keep a human decision owner for screening, ranking, or termination-adjacent automation
- For covered NYC AEDTs or EU AI Act-scoped systems, follow audit/notice obligations from `sources.md` before deployment claims

## HR Focus by Stage

| Stage | Focus |
|-------|-------|
| Seed | Founder-led hiring, basic compliance, offer templates |
| Series A | First HR hire, HRIS setup, comp bands, handbook |
| Series B | HR team, performance cycles, workforce planning |
| Series C+ | HR org, HRBP model, global compliance, analytics |

## Common Traps

- At-will overconfidence — wrongful termination risk still exists
- Verbal promises — "we discussed it" is not documentation
- Inconsistent enforcement — policies must apply to everyone
- Delayed investigations — complainants lose trust fast
- Comp secrecy assumptions — pay-transparency laws are expanding by jurisdiction
- Treating AI screening as neutral — bias audit and notice duties may apply

## Human-in-the-Loop

These decisions require human approval:
- Final termination decisions
- Executive/senior hires
- Compensation exceptions above band
- Org restructures
- Settlement amounts
- Mass layoff / WARN-threshold actions
- Deployment of automated employment decision tools in regulated locales
