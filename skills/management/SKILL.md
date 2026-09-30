---
name: management
description: >
  Apply people-management judgment, team leadership routines, and organizational
  frameworks. Use when the user asks about 1:1s, feedback, performance reviews,
  PIPs, delegation, conflict, hiring interviews, change management, MBA case
  analysis, or upward career navigation with a manager. Not for product roadmap
  craft (`product-manager`), pure coaching sessions (`coach`), clinical care
  (`psychologist`), or personal productivity systems (`productivity`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"👔"}'
  related-skills: '{"coach":"1:1 coaching craft, questions, and commitment design rather than managerial authority.","product-manager":"Product discovery, prioritization, and roadmap artifacts rather than people management.","career":"Individual career strategy and role moves without day-to-day team leadership.","meetings":"Meeting design and facilitation mechanics beyond manager 1:1 agendas.","legal":"Employment-law review when discipline, termination, or protected activity is in scope.","ethics":"Ethical framing when decisions affect livelihoods, fairness, or trust.","productivity":"Personal task systems rather than team leadership systems."}'
---

# Management

This skill is **stateless**. It does not create local configuration or durable user state under a workspace path. Keep notes the user explicitly asks to save in the location they name.

## When to load

Load this skill when the request is about **people and organizational management**:

- manager 1:1s, feedback, performance reviews, PIPs, or delegation
- team conflict, remote/hybrid fairness, hiring interview design
- change management, succession, 360 feedback, org design
- MBA/case frameworks (SWOT, Porter, McKinsey 7S, PESTEL, BCG) applied to a situation
- navigating upward: escalation, promotion cases, reading review language

Route away when the task is mainly:

- product discovery / roadmap / PRD → `product-manager`
- pure coaching without managerial authority → `coach`
- career decision analysis for an IC path → `career`
- meeting logistics only → `meetings`
- clinical distress or crisis → human care + `psychologist` safeguards
- personal todo/habit systems → `productivity` / `habits`

## When to load references

Keep `SKILL.md` as the entry point. Load supporting files only when needed:

| Reference | Load when |
|---|---|
| `references/audience-playbooks.md` | Role-specific checklists for ICs, practicing managers, students, researchers, educators, or HR/OD |
| `references/frameworks.md` | Choosing or applying strategy/org frameworks and citing classic sources carefully |
| `references/safety-and-escalation.md` | Discipline, PIP, termination, protected activity, retaliation risk, or legal/HR handoff |
| `references/sources.md` | Verifying frameworks, change models, or research-methods claims against primary URLs |

## Operating loop

1. **Clarify role and stakes** — Who is the user (IC, manager, student, HR)? What decision is live, and who is affected?
2. **Name the management problem** — execution, people development, conflict, structure, or strategy framing—not a generic pep talk.
3. **Load the matching reference** — audience playbook and/or frameworks; add safety reference before any discipline or termination advice.
4. **Give a concrete next move** — agenda bullets, talking points, decision criteria, or case structure with ownership and timeline.
5. **Surface ethics and limits** — fairness, documentation, and when to involve HR/legal; keep prescriptions contextual.

## Core rules

- Treat management as **contextual**: industry, culture, company stage, and team composition change the answer.
- Separate **leadership** (direction, change, inspiration) from **management** (execution, systems, stability) when the user confuses them.
- Prefer **behavior + evidence** over personality labels in feedback, reviews, and conflict work.
- For performance issues: define the gap, support offered, timeline, and metrics before drafting a PIP tone.
- For case/academic work: pick a framework that fits the question, challenge missing data, and make recommendations actionable.
- For upward navigation: decode organizational pressure before drafting confrontation or escalation.
- When livelihoods, protected characteristics, harassment, accommodations, or retaliation risk appear, load `references/safety-and-escalation.md` and recommend HR/legal paths rather than freestyle discipline scripts.
- Tailor prescriptions to the specific people and constraints in the prompt; generic universal advice is a miss.

## Quick routing

| User need | First move |
|---|---|
| Underperforming report / overdue feedback | Manager playbook + behavior-based talking points; check PIP readiness only if formal |
| 1:1 feels empty | Build agenda from recent work, career theme, and open commitments |
| Team conflict signals | Describe observable dynamics; mediation steps before structural blame |
| Case / strategy homework | Frameworks reference; Issue–Analysis–Recommendation; flag missing evidence |
| Promotion or difficult upward talk | IC playbook; manager-pressure decode; evidence plan |
| Reorg / change stall | Kotter / ADKAR / Bridges diagnostic questions from frameworks + HR playbook |
| Interview loop design | Behavioral questions tied to role; illegal-question warnings from safety reference |
