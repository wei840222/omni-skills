---
name: b2b
description: >
  Qualify enterprise deals, research prospects, personalize outreach, and run
  pipeline or forecast reviews with MEDDIC/MEDDPICC, multi-threading, and next-step
  discipline. Use when the user is prospecting, drafting cold outreach, scoring a
  deal, unblocking a stalled opportunity, coaching a pipeline review, or defending
  a commit forecast. Not for CRM schema/import hygiene (`crm`), multi-channel
  campaign copy outside deal context (`outreach`), or Salesforce API/SOQL work
  (`salesforce-api-integration`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🤝"}'
  related-skills: '{"crm":"Contact/company/deal records, stage hygiene, and local CRM ops once qualification decisions need durable storage.","outreach":"Campaign-level sequences and multi-channel copy when the job is volume outreach rather than a single deal strategy.","salesforce-api-integration":"SOQL, Bulk, and org API mechanics when the blocker is Salesforce data access rather than sales judgment."}'
---

## When to use

Load for **enterprise B2B sales judgment**:

- Prospect research and buying-signal detection before first touch
- Cold email / call framing tied to a named account
- Deal qualification (MEDDIC / MEDDPICC / BANT as a prioritization lens)
- Multi-threading and champion development
- Pipeline hygiene, stalled-deal recovery, and forecast honesty

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| CRM records, imports, do-not-contact, tool setup | `crm` |
| Campaign sequences across many accounts | `outreach` |
| Salesforce API, SOQL, Bulk load, OAuth | `salesforce-api-integration` |

## Scope

Knowledge-only coaching. This skill does **not** own persistent CRM state. If the user needs durable deal records, resolve storage through `crm` (or their existing CRM) after the sales recommendation is clear.

## Primary workflow

Execute in order. Stop early when a missing input blocks a safe recommendation.

1. **Classify the ask** — prospecting, outreach draft, qualification, stalled-deal recovery, pipeline review, or forecast defense.
2. **Inventory known facts** — account, persona, stage, last activity date, next step, stakeholders named, quantified pain, economic buyer access, paper-process status. Label unknowns explicitly; do not invent customers, metrics, or internal politics.
3. **Load only the reference that owns the bottleneck**:

| Bottleneck | Load |
|------------|------|
| Framework choice / element gaps (MEDDIC, BANT, SPIN, Gap, Challenger) | `references/frameworks.md` |
| Cold email, call, subject lines, follow-up cadence | `references/outreach.md` |
| Coverage math, stage hygiene, commit vs best-case | `references/pipeline.md` |
| Verified sources used in this package | `references/sources.md` |

4. **Apply core operating rules** (below) to the known facts.
5. **Produce an evidence-bound output** — recommendation, missing-data asks, and one concrete next step with owner + date when the user wants action. If research depth is insufficient for claims, say what is missing instead of fabricating proof points.

## Core rules

### 1. Research before outreach

- Gather at least three verifiable insights when public data exists: recent news, hiring or org signals, tech stack, funding, or initiative language from the prospect.
- Map decision makers **and** influencers; treat a single name as incomplete coverage.
- Prefer buying signals (leadership change, expansion, competitor pain) over generic role flattery.
- When fewer than three solid insights are available, say so, ask for the missing inputs, and keep outreach narrowly tied to what is verified.

### 2. Qualify with MEDDIC depth

Use MEDDIC elements as the default enterprise checklist (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify/Implicate Pain, Champion). For complex late-stage deals, also cover **Paper Process** and **Competition** (MEDDPICC). Load `references/frameworks.md` for definitions and red flags.

- BANT (Budget, Authority, Need, Timeline) may prioritize early SMB conversations; use it to order effort, not to hard-disqualify on the first incomplete answer.
- Record element status as `known` / `unknown` / `at-risk` rather than a single gut-feel stage label.

### 3. Multi-thread every material deal

- Require coverage beyond one contact: Champion, Economic Buyer, Technical Evaluator, and End Users as applicable.
- Ask who else must agree before a decision sticks.
- If the only engaged contact goes dark, treat the deal as fragile and reopen other threads before adding forecast confidence.

### 4. End every interaction with a dated next step

- A valid next step names **action + owner + date**.
- “I’ll follow up” is a placeholder, not a next step.
- Complex deals benefit from a mutual action plan shared with the buyer side.
- Missing next step ⇒ classify the opportunity as stalled until one is set or the user declines scheduling.

### 5. Validate stage with evidence, not CRM labels

- Confirm recent activity, a scheduled next step, and an engaged champion before trusting “Negotiation” or similar labels.
- Long dwell time is a review signal (example heuristic: ~60 days still in pure Discovery without progress). Calibrate to the team’s median cycle when known.
- Weighted pipeline is only useful when stage probabilities match observed win rates.

### 6. Build champions, not only contacts

- A champion sells internally when you are absent and can restate value without a script.
- Arm them with ROI math, competitive contrast, and an internal pitch they can deliver.
- If they cannot articulate value alone, keep developing the champion before treating the deal as late-stage safe.

## Common traps (and replacements)

| Weak pattern | Do this instead |
|--------------|-----------------|
| Name-only personalization | Lead with a verified initiative, metric, or trigger event |
| Feature tour before pain | Document the problem and success metric first |
| Single-threaded enthusiasm | Map the buying committee and open a second thread |
| “Great call” with no commit | Leave with a dated mutual next step |
| Volume over ICP fit | Prefer fewer accounts that match the ideal customer profile |
| Pricing before budget/authority signals | Validate commercial path before a formal proposal |
| Dropping the champion after signature | Plan post-close enablement to protect expansion/renewal |
| One message for CEO and end user | Match value prop to each stakeholder’s job-to-be-done |

## Forecasting review signals

Treat these as **review triggers**, not automatic disqualifiers. Adjust thresholds to the team’s median cycle when the user supplies it:

- Cycle length ≈ 3× the team’s average without a clear paper-process path
- No meaningful activity for ~14 days on an active opportunity
- Single-threaded coverage
- Verbal yes without paperwork motion
- Champion repeatedly unavailable for the next meeting
- Late stage without procurement/legal/security engagement when those gates apply
- Commit date slipped more than once without a rewritten mutual plan

## Output contract

Default structure unless the user asks for a different format:

1. **Situation read** — stage/risk in one short paragraph from known facts only
2. **Gaps** — MEDDIC/MEDDPICC elements still unknown
3. **Recommended moves** — ordered actions with owners
4. **Next step** — single dated commit, or an explicit ask if the user must choose
5. **Sources / confidence** — mark heuristics vs user-provided metrics

## Quick reference

| Topic | File | Load when |
|-------|------|-----------|
| Frameworks | `references/frameworks.md` | Choosing or scoring qualification methods |
| Outreach | `references/outreach.md` | Drafting or reviewing prospecting touches |
| Pipeline | `references/pipeline.md` | Coverage, stage hygiene, forecast categories |
| Sources | `references/sources.md` | Re-checking citations before changing facts |
