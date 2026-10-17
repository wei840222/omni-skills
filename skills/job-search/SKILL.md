---
name: job-search
description: >
  Manage job hunting with structured application tracking, company research,
  offer diligence, and interview prep. Use when starting a search, logging
  applications, researching employers, preparing interviews, or evaluating
  remote/comp claims. Prefer `cv` or `resume` for resume drafting itself, and
  `career` for longer-horizon career strategy outside an active hunt.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"💼"}'
  related-skills: '{"cv":"Tailor the actual resume/CV and bullet evidence for a target role.","resume":"Resume structure and ATS-aware rewriting when the artifact itself is the task.","career":"Longer-horizon career strategy, role sequencing, and growth planning outside an active application cycle."}'
---

## State location

Resolve `<state_root>` before the first state operation using this order:

1. `<workspace>/job-search/`
2. `<workspace>/memory/job-search/`
3. `~/job-search/`

Never write hunt state into the skill package. Create directories only under the resolved `<state_root>`.

## Purpose

Use this skill when the user is actively job hunting: track opportunities, research target companies, organize application materials, prepare interviews, and keep next actions current.

## Architecture

Memory lives in `<state_root>/`. Load `references/setup.md` before first setup, then copy templates from `assets/data-templates.md`.

```text
<state_root>/
├── memory.md          # HOT: preferences, target criteria
├── applications.md    # Active pipeline
├── companies.md       # Research on target companies
├── materials/         # CV versions, cover letters
└── archive/           # Closed applications
```

## Quick Reference

| Topic | File | Load when |
|-------|------|-----------|
| Memory setup | `references/setup.md` | First use or missing state files |
| Research patterns | `references/research.md` | Company diligence, offer/comp checks |
| Interview prep | `references/interviews.md` | Upcoming interview or thank-you/follow-up |
| Verified sources | `references/sources.md` | Citing market, legal, or freshness-sensitive claims |

## Core Rules

### 1. Quality Over Volume
- Prefer a small set of tailored applications over mass spray.
- Customize each packet to the company and role.
- Keep reputation intact by targeting precise fits.

### 2. Verify "Remote" Claims
Before recommending remote roles, confirm:
- Geographic or work-authorization limits ("US only", "EU timezone")
- Tax/legal fine print
- Real timezone overlap expectations

### 3. Detect Red Flags
| Signal | Likely Meaning |
|--------|----------------|
| Posted 3+ months | Ghost job or high turnover |
| "Rockstar/ninja" language | Overwork culture risk |
| Vague salary ("competitive") | Below-market risk |
| "Young dynamic team" | Age-bias risk |
| Recent mass layoffs | Instability |

Load `references/sources.md` before presenting discrimination-risk or job-scam guidance as settled fact.

### 4. Preserve User Voice
- Materials must sound like the user, not generic AI.
- Ask for writing samples when tone matching matters.
- Balance keywords with authentic voice.
- Recruiters detect AI-written content; personalization wins.

### 5. Track Application State
Maintain `<state_root>/applications.md` with:
- Company, role, date applied
- Current status, next action
- Contacts, interview dates
- Follow-up reminders

### 6. Research Before Applying
For each target company, gather:
- Financial health (funding, revenue trends)
- Review sentiment filtered for recency
- Recent news (layoffs, acquisitions)
- Hiring-manager profile when findable

Use `references/research.md` for the diligence checklist and `references/sources.md` for freshness-sensitive sources.

### 7. Adjust for User Context
| User Type | Priority |
|-----------|----------|
| Senior (10+ yrs) | Network activation, discretion, salary negotiation |
| Junior/New grad | Quality with enough volume, entry-friendly companies |
| Career changer | Transferable-skills narrative, bridge roles |
| Urgent need | Speed, temporary options, immediate income |

## Common Traps

- **ATS stuffing** — keywords that pass filters but read robotic to humans
- **Stale salary data** — verify ranges are current, not multi-year snapshots
- **"Perfect match" overconfidence** — partial requirement fit still often rejects
- **Cold networking without context** — outreach needs a warm path or specific hook
- **Long-term advice for urgent needs** — brand-building does not replace this month's rent
