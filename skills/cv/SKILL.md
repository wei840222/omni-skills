---
name: cv
description: >
  Draft and diagnose ATS-aware resumes and academic/professional CVs with
  structure, quantified bullets, length calibration, and market-specific
  document choice. Use when the user needs resume vs CV selection, CAR
  achievement bullets, ATS-safe layout, tech/design packaging, or a scannable
  draft for a target role. Prefer `resume` for deep callback diagnosis and
  JD-tailoring workflows already specialized there, `job-search` for application
  pipeline tracking, and `career` for offer/equity/stay-leave strategy.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📄"}'
  related-skills: '{"resume":"Deep resume diagnosis, JD tailoring, and seniority calibration when that specialized workflow is the primary ask.","job-search":"Application pipeline, company research, and interview prep beyond drafting the document.","career":"Offer evaluation, promotion, pivot, and layoff strategy when the document itself is not the deliverable.","writing":"General prose voice work when the artifact is not a resume/CV."}'
---

# CV / Resume Craft

Advise-and-draft mode for resume and CV documents the user supplies or requests.
Produce scannable, ATS-aware content with quantified impact. Optional draft
versions may live under a portable `<state_root>` only when the user asks to
save them. Keep metrics, credentials, and employment dates user-evidenced.

## State location

Resolve `<state_root>` before any read/write of saved drafts:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/cv/`, `<workspace>/memory/cv/`, `~/cv/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and the user asked to persist a draft, create
   `<workspace>/cv/` when `<workspace>` is available; otherwise ask for a path.

| Path | Required? | Role |
|------|-----------|------|
| `<state_root>/drafts/` | optional | Versioned resume/CV drafts the user asked to keep |
| `<state_root>/notes.md` | optional | Target roles, approved phrasing, market constraints |

Write runtime drafts only under the resolved `<state_root>`. Keep secrets, government IDs,
and unredacted personal data out of saved notes beyond what the user placed in
the document. Destructive clear/reset of drafts stays under
`<state_root>/drafts/` and requires explicit user consent.

## When to load

Load this skill when the ask is **document craft**:

- resume vs CV choice for a market or role type
- structure, professional summary, and achievement bullets
- ATS-safe formatting and keyword fit
- tech or design packaging (GitHub, portfolio, skills taxonomy)
- length calibration by experience band

Route away when the ask is mainly:

- deep callback diagnosis / specialized JD rewrite loop → `resume`
- multi-company hunt tracking / interview loops → `job-search`
- offer, equity, promotion, stay-vs-leave → `career`
- general essay or social prose → `writing`

Re-check `references/sources.md` before repeating ATS rejection-rate or
recruiter scan-time heuristics as hard facts. Confirm local photo / personal-data
norms with the user before adding fields outside U.S.-style applications.

## Quick reference

Load only the matching reference for the current step; keep `SKILL.md` as the entry point.

| Need | Load |
|------|------|
| Resume vs CV, structure, summaries, bullets | `references/document-craft.md` |
| ATS layout, keywords, export hygiene | `references/ats.md` |
| Tech / design packaging patterns | `references/industry.md` |
| Length bands and pre-submit checks | `references/length-checklist.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |
| Optional draft note shapes | `assets/draft-template.md` |

## Operating loop

1. **Clarify target** — role, seniority, geography/market, resume vs CV need, and whether a JD exists.
2. **Choose document type** — load `references/document-craft.md` when resume vs CV is ambiguous.
3. **Structure pass** — contact → summary → experience/education order matched to experience level.
4. **Achievement pass** — CAR (Action Verb + Task + Result with Metrics); ask once for missing numbers; mark unknowns instead of fabricating.
5. **ATS pass** — load `references/ats.md`; prefer single-column, standard headers, text-layer PDF/DOCX.
6. **Industry pass** — load `references/industry.md` for tech/design extras when relevant.
7. **Length + checklist** — load `references/length-checklist.md` before finalizing.
8. **Persist only on request** — resolve `<state_root>` and use `assets/draft-template.md` shapes when saving.

## Core rules

### 1. Document choice before polish

- **Resume**: industry jobs (US/Canada and many corporate roles); typically 1–2 pages; tailored snapshot.
- **CV**: academia, research, medicine, many EU/UK applications, grants/fellowships; complete history; length follows content.
- When the posting says "resume", prefer resume structure unless the user confirms an academic/EU CV expectation.

### 2. Achievement bullets (CAR)

Every experience bullet aims for: **action verb + concrete task + result with evidence**.

Transform patterns:

- "Responsible for managing the team" → "Led an N-person engineering team, delivering X on schedule"
- "Helped improve sales" → "Increased enterprise sales by $Y (Z% YoY) through …"
- "Worked on checkout" → "Reduced checkout abandonment from A% to B% by …"

Limit about 3–5 bullets per role; lead with the strongest evidence. Prefer user-supplied metrics; mark unknowns instead of fabricating.

### 3. Professional summary over objectives

Use a short summary (title, years/domain, one quantified highlight, top skills, target) rather than a self-focused objective statement.

### 4. U.S.-style personal-data default

For U.S.-style applications, omit photo, birth date, marital status, religion, and full street address (city + region is enough). Confirm local convention before adding those fields for other markets. See EEOC-oriented notes in `references/sources.md`.

### 5. Honesty and recovery

- Keep employers, titles, dates, degrees, and metrics user-evidenced only.
- If ATS claims or scan-time heuristics are requested as precise statistics, open `references/sources.md` and treat them as industry heuristics unless a live primary supports the number.
- If draft save fails or multiple state roots exist, report the path conflict and wait for user choice before writing.
