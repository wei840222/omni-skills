---
name: legal
description: Structure jurisdiction-first IRAC legal analysis with issue spotting,
  risk ranking, and next actions. Use for claim-viability drills, multi-issue fact
  patterns, and exam-style reasoning. Not for counsel redlines (lawyer), primary-authority
  research (law), or contract draft/register work (contract/contracts).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji": "⚖️"}'
  related-skills: '{"law":"Jurisdiction-aware legal research and education across roles when the task is authority lookup rather than IRAC issue spotting.","lawyer":"Counsel-style redlines, negotiation, and matter workflow when an agreement or filing needs markup rather than an analysis drill.","contract":"Blank-page contract drafting with guided intake when the user wants a new agreement written.","contracts":"Contract register, renewal alerts, and clause lookup for executed agreements."}'
---

## When to load

Load this skill when the user wants structured legal **analysis**, not drafting or matter management:

- issue spotting across a fact pattern
- claim / defense viability ranking
- IRAC or exam-style legal reasoning
- jurisdiction + risk + next-action framing before talking to counsel

Keep this skill secondary when the user mainly needs:

- primary-authority research by audience → `law`
- redlines, negotiation, or counsel workflow → `lawyer`
- drafting a new agreement from scratch → `contract`
- tracking signed contracts and renewals → `contracts`

## Core constraints

1. Lead with **jurisdiction** and **role** (who is being advised, what outcome they want).
2. Provide **legal information and structured analysis**, not licensed advice for a specific person. State the boundary when the user could confuse the two.
3. Prefer **probabilistic positions** (strong / moderate / weak) over outcome guarantees.
4. Separate **facts**, **issues**, **rules**, **application**, **risks**, and **actions**.
5. Escalate to a licensed attorney for criminal exposure, custody, immigration, eviction, rights waivers, served papers, high-value stakes, or closing deadlines.
6. Stay inside lawful, authorized assistance; route requests to evade law, court orders, professional duties, or confidentiality to a clear refusal.

## Workflow

Execute in order. Load references only when the step needs them.

### 1. Bound the problem

- Confirm country / state-province / forum and the date of the facts.
- Name the user's role and goal in one line.
- If jurisdiction is missing, state the assumption used and mark confidence lower.
- For urgent safety or irreversible deadlines, give only harm-minimizing first steps and point to local counsel or legal aid.

### 2. Gather facts

Use the checklist in `references/fact-intake.md`.

- Separate proven facts from interpretations and missing data.
- Build a dated timeline; sequence changes legal analysis.
- Ask for documents when material terms or notices matter.

### 3. Spot issues

Use `references/issue-spotting.md`.

- List **all** plausible issues, not only the user's favorite claim.
- Include defenses, counterclaims, and procedural bars (standing, notice, limitations).
- Rank issues by materiality to the user's goal.

### 4. Apply IRAC per material issue

Use `references/irac.md`.

| Step | Question | Output |
|------|----------|--------|
| **Issue** | What is the legal question? | One-sentence framing |
| **Rule** | What law applies? | Statute / case / regulation + source class |
| **Application** | How do the facts map? | Element-by-element analysis |
| **Conclusion** | What is the working answer? | Position + confidence |

When a current citation, limitation period, or local rule is material, verify starting points in `references/sources.md` and record retrieval assumptions.

### 5. Score risk and recommend action

Use `references/risk-and-action.md`.

- Score each material issue: strong / moderate / weak.
- Name key vulnerabilities and what evidence would change the score.
- Give one reversible next action with a deadline when known.
- State the escalation trigger for licensed counsel.

## Output shape

Default response skeleton (adapt tone to the user):

```text
⚖️ JURISDICTION: [forum + law family assumed]
👤 ROLE / GOAL: [who + desired outcome]
📋 ISSUES: [prioritized list]
📖 RULE: [governing rule per top issue]
🔍 APPLICATION: [facts → elements]
⚠️ RISKS: [what defeats the position]
➡️ ACTION: [next step + deadline if known]
🚨 ESCALATE IF: [licensed-counsel triggers]
```

One-line position form:

> You likely [possess/lack] a viable claim on [issue] because [controlling reason], confidence [strong/moderate/weak].

## Quick reference

| Topic | File |
|-------|------|
| Fact intake checklist | `references/fact-intake.md` |
| Issue-spotting method | `references/issue-spotting.md` |
| IRAC detail | `references/irac.md` |
| Risk matrix and actions | `references/risk-and-action.md` |
| Source starting points | `references/sources.md` |
| Common traps | `references/traps.md` |

## Traps (summary)

Read `references/traps.md` before giving high-confidence conclusions.

- Jurisdiction assumption (US ≠ UK ≠ EU ≠ other systems)
- Single-issue tunnel vision
- Certainty theater ("you will win")
- Crossing from information into licensed advice without saying so
- Outdated rules or unverified deadlines
- Treating verbal history as equal to written proof
