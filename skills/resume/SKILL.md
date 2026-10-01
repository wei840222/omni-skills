---
name: resume
description: >
  Diagnose resume gaps, tailor bullets to a job description, pass ATS parse checks,
  and calibrate seniority/length so impact is scannable in seconds. Use when the user
  asks why they are not getting callbacks, wants a resume rewritten for a posting,
  needs ATS-safe formatting, is changing careers, or must condense a long career into
  one or two pages. Not for offer/equity strategy without a document rewrite (`career`),
  full application pipeline tracking (`job-search`), or general prose voice work (`writing`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📄"}'
  related-skills: '{"career":"Offer evaluation, promotion, pivot, and layoff strategy when the document itself is not the deliverable.","job-search":"Application pipeline, company research, and interview prep beyond a single resume draft.","writing":"General prose voice and editing when the artifact is not a resume/CV.","negotiate":"Live salary or offer counters after the resume has done its job."}'
---

# Resume

This skill is **mostly stateless guidance**. It rewrites and diagnoses resume content the user provides. Optional drafts may live under a portable `<state_root>` only when the user asks to save versions.

## State location

Resolve `<state_root>` before any read/write of saved drafts:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory: `<workspace>/resume/`, `<workspace>/memory/resume/`, `~/resume/`.
3. If none exist and the user asked to persist a draft, create `<workspace>/resume/`.

| Path | Required? | Role |
|------|-----------|------|
| `<state_root>/drafts/` | optional | Versioned resume/CV drafts the user asked to keep |
| `<state_root>/notes.md` | optional | Target roles, constraints, approved phrasing |

Do not store secrets, full government IDs, or unredacted contact data beyond what the user put in the resume. Skill resources stay under `references/`; never mix them into `<state_root>`.

## When to load

Load this skill when the request is about **resume/CV craft**:

- why applications get no interviews or callbacks
- tailoring one resume to a specific job description
- ATS parseability, keywords, and safe layout
- career-change narrative and transferable-skill framing
- seniority calibration (junior through executive length/tone)
- turning responsibility lists into quantified achievements

Route away when the ask is mainly:

- offer, equity, promotion, or stay-vs-leave strategy → `career`
- multi-company application tracking / interview loops → `job-search`
- general email, essay, or social prose → `writing`
- live counterparty salary negotiation → `negotiate`

Re-check `references/sources.md` before repeating ATS rejection rates, recruiter scan-time claims, or jurisdiction-specific CV photo rules as hard facts.

## Quick reference

| Need | Load |
|------|------|
| No callbacks / gap diagnosis | `references/diagnosis.md` |
| Job-specific rewrite / career change | `references/tailoring.md` |
| ATS layout and parse safety | `references/ats.md` |
| Level, length, executive condensation | `references/seniority.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |

## Operating loop

1. **Clarify target** — role title, seniority, geography/market, and whether a JD is available.
2. **Six-second scan** — title clarity, top three impacts visible, relevance obvious, clean single-column scan path.
3. **Diagnose or tailor** — load the matching reference; prefer evidence over generic polish.
4. **Achievement pass** — every bullet: action verb + specific result + quantified impact when the user can support the number.
5. **ATS pass** — standard headers, text-layer PDF/DOCX, exact JD terms integrated naturally.
6. **Seniority pass** — length and tone match target level; older roles condensed when needed.
7. **Sources** — if stating industry benchmarks, open `references/sources.md` and prefer linked primaries.

## Core rules

### 1. Six-second test (before deep rewrite)

Recruiters often give a resume only a few seconds on first pass. Fix these first:

1. **Title clarity** — current or target role is obvious at the top.
2. **Impact visible** — top three achievements stand out without hunting.
3. **Relevance clear** — match to the target role is evident.
4. **Clean format** — single column, no visual clutter that slows the scan.

If any fail, fix them before keyword stuffing or section reshuffles.

### 2. Responsibilities → achievements

Listing tasks without outcomes is the primary weak pattern.

Transform patterns:

- "Responsible for..." → "Achieved X resulting in Y"
- "Managed team of..." → "Built team from X to Y, delivering Z"
- "Worked on..." → "Led/contributed to X, increasing Y by Z%"

Every bullet needs: **action verb + specific result + quantified impact when evidence exists**. Do not invent metrics; ask once for missing numbers or mark them as unknown.

### 3. Tailoring workflow (when a JD exists)

1. Extract must-haves vs nice-to-haves from the posting.
2. Map the user's real achievements to each requirement.
3. Name gaps honestly; reframe only when the underlying experience is real.
4. Inject exact JD terms naturally (include spelled-out + acronym forms when both appear).
5. Reorder so the most relevant experience appears first.

Details: `references/tailoring.md`.

### 4. Career changers

1. Translate vocabulary into the target industry's language.
2. Surface transferable competencies (for example budget management → P&L ownership when accurate).
3. Write a short narrative bridge (2–3 sentences) connecting past to target.
4. Consider skills/summary before deep chronology when it helps the reader.
5. Drop phrases that signal direction confusion; keep a coherent arc.

### 5. Senior / long-career calibration

For roughly 15+ years of experience:

1. One coherent career arc, not a disconnected role list.
2. Weight the last 5–7 years; condense earlier roles.
3. Omit outdated tech and irrelevant roles when they add noise.
4. Show how leadership happened, not only that a title existed.
5. If targeting a lower level, tone down scope signals that trigger "overqualified" filters.

Details: `references/seniority.md`.

### 6. Red flags to repair

- Unexplained gaps — add brief context the user approves.
- Short stints without framing — position scope, contract nature, or outcome.
- Tech-name typos and inconsistent product spelling.
- Generic objectives ("seeking challenging opportunity") — replace with a targeted summary or remove.
- Skills claimed without supporting bullets.

### 7. Format defaults

| Topic | Default |
|-------|---------|
| Length | <10 years → 1 page; 10–20 → up to 2; executive → 2–3 when needed |
| Files | Keep PDF (text layer), DOCX, and plain text ready |
| Layout | Single column; standard fonts; minimal color; no critical info only in headers/footers |
| Dates | One consistent scheme (MM/YYYY or Month YYYY) |
| Photos | Omit for US applications; follow local norm only when the user confirms the market |

ATS-specific rules: `references/ats.md`.

## Safety and honesty

- Never fabricate employers, titles, dates, degrees, or metrics.
- Mark uncertain claims; prefer user-confirmed numbers.
- Jurisdiction-specific photo, age, or personal-data norms vary — verify via `references/sources.md` and the user's market.
- This skill drafts and coaches; the user owns the final submission.
