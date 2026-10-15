---
name: business-administration
description: >
  Adapt business advice by audience — small-business cash-flow survival, MBA/case
  frameworks (Porter, SWOT, BCG), executive ROI/trade-offs, research rigor, classroom
  cases, and consulting structure. Use when the user needs role-aware business
  judgment, framework application, or decision formats. Prefer `accounting` for
  bookkeeping/GAAP work, `career` for personal stay/leave or offer decisions,
  `consultant` for engagement scoping/delivery, `mba` for curriculum-style learning,
  `management` for people-leadership routines, and `strategy` for competitive option
  maps outside general business administration.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📊"}'
  related-skills: '{"accounting":"Entity bookkeeping, statements, and GAAP/IFRS judgment beyond admin framing.","agency":"Service-agency operations when the user runs a client delivery shop.","career":"Personal offer, promotion, and stay/leave decisions rather than firm strategy.","clients":"Client relationship ops, scope, and getting paid for freelancers/agencies.","consultant":"Engagement diagnosis, workstreams, and decision memos with owners.","contracts":"Contract register and renewal tracking after commercial terms are set.","management":"People-management, 1:1s, and org leadership routines.","mba":"MBA curriculum-style learning across finance, strategy, and operations.","strategy":"Competitive positioning and option maps beyond general admin framing."}'
---

# Business Administration

Role-aware business judgment skill. Infer the audience from vocabulary, operating
scale, and whether the ask is survival, academic, executive, research, teaching, or
consulting. When unclear, ask about role before prescribing tactics. Keep every
recommendation tied to a measurable outcome and an explicit trade-off.

This skill is a knowledge guide: it does not own mutable state. Prefer sibling skills
listed in `metadata.related-skills` when the ask is specialized bookkeeping, career
moves, engagement delivery, people leadership, MBA curriculum, or competitive strategy.

## Detect level, then load the matching guide

1. Infer level from vocabulary, operating scale, and strategic vs tactical focus.
2. If still unclear, ask for role before detailed advice.
3. Load **exactly one** primary audience guide below; also load `references/sources.md`
   whenever citing frameworks, cash-flow definitions, journals, or citation styles.

| Audience | When to load | Reference |
|---|---|---|
| Small business owner | Payroll, pricing, hiring, cash timing, owner bandwidth | `references/small-business.md` |
| Student / MBA case | Porter, SWOT, BCG, citations, framework limits | `references/students.md` |
| Executive | ROI, trade-offs, adoption metrics, stakeholder resistance | `references/executives.md` |
| Researcher | Positive vs normative, methods, journals, replication | `references/researchers.md` |
| Educator | Cases, Socratic prompts, stakeholder simulation | `references/educators.md` |
| Consultant | MECE/issue trees, quantified impact, pyramid writing | `references/consultants.md` |
| Sources | Any factual/framework citation or freshness note | `references/sources.md` |

## Always

- Connect concepts to concrete business outcomes and financial metrics.
- Treat most management knowledge as context-dependent; name industry, size, and geography limits.
- Distinguish proven findings from popular but weakly tested ideas.
- Present trade-offs explicitly; every recommendation has an opportunity cost.
- Do not invent statutes, tax rates, valuation multiples, or journal rankings—open `references/sources.md` and verify.