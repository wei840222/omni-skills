# Sources (Gate 6)

Full URLs checked while refactoring this skill (2026-10-14). Re-open before
restating Scholar UI labels, access behavior, ranking claims, or coverage numbers.

## Agent skill format

- Agent Skills specification: https://agentskills.io/specification
- Agent Skills llms.txt: https://agentskills.io/llms.txt
- Agent Skills best practices: https://agentskills.io/skill-creation/best-practices
- Agent Skills optimizing descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- skills-ref validator: https://github.com/agentskills/agentskills/tree/main/skills-ref

## Google Scholar official

- Google Scholar home: https://scholar.google.com/
- Search Help (queries, recent papers, full text, alerts, advanced search, case law):
  https://scholar.google.com/intl/en/scholar/help.html
- About Google Scholar (scope and ranking aims):
  https://scholar.google.com/intl/en/scholar/about.html
- Profiles / citations help:
  https://scholar.google.com/intl/en/scholar/citations.html
- Inclusion guidelines for publishers/sites:
  https://scholar.google.com/intl/en/scholar/inclusion.html

## Background and risk context (secondary)

- Wikipedia — Google Scholar (history, coverage discussion, predatory-journal criticism overview):
  https://en.wikipedia.org/wiki/Google_Scholar
- Unpaywall (legal OA discovery browser extension / API context):
  https://unpaywall.org/

## Claim audit

| Claim in skill | Source support | Notes |
| --- | --- | --- |
| Default sort is relevance, not date | Scholar Search Help — Finding recent papers | Use Since Year / Sort by date deliberately |
| `author:` operator forms | Scholar Search Help — Searching | Examples use quoted author names |
| Quoted title search | Scholar Search Help — title FAQ | Exact title in quotes |
| Since Year vs Sort by date | Scholar Search Help | Relevance-within-year often preferred |
| Library / [PDF] / [HTML] / All versions / Related / Cited by | Scholar Search Help — Access | Legitimate access paths only |
| Off-campus subscription link behavior | Scholar Search Help — Off-campus access | Product behavior; confirm if UI changes |
| Ranking weighs text, venue, authors, citation frequency/recency | About Google Scholar | High-level aim only — not a full algorithm spec |
| Profiles, metrics, curation of wrong articles | Profiles help | Authors must clean mismatches |
| Case law mode + Select courts; not legal advice | Search Help + About disclaimer | Informational only |
| Predatory / unvetted venues can appear | Wikipedia summary + public reporting cited there | Risk posture, not a tally of bad journals |
| Unpaywall as legal OA helper | unpaywall.org | Optional aid; not required |

## Fragile claims — do not invent

- Exact index size, percent coverage of “all” scholarship, or guaranteed recall.
- That every result’s full text is searchable or that ranking weights are public.
- Live subscription pricing, publisher deal status, or a user’s library entitlements.
- Pirate or credential-sharing bypasses for paywalled PDFs.
- That citation count, h-index, or impact factor equals paper quality.
- Stable machine-automation guarantees against Scholar bot checks or ToS limits.
