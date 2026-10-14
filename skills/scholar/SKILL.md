---
name: scholar
description: >
  Search academic literature with Google Scholar using operators, date filters,
  Cited by / Related articles trails, full-text access paths, and citation hygiene.
  Use when finding papers, authors, or court opinions on Scholar, building precise
  queries, checking who cited a work, or locating PDF/HTML/library versions. Prefer
  `pubmed` for biomedical MeSH/PICO appraisal, `multi-engine-web-search` for general
  multi-index web discovery, and `in-depth-research` for full multi-source investigations.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎓"}'
  related-skills: '{"pubmed":"Biomedical literature with MeSH, PICO, and clinical study hierarchy.","multi-engine-web-search":"Cross-engine web discovery when Scholar alone is not enough.","in-depth-research":"Structured multi-source investigation after candidate papers are found.","literature":"Literary analysis and critical essays rather than scholarly search.","web":"Open and inspect a selected page after Scholar discovery.","digest":"Recurring monitoring feeds instead of one-shot Scholar lookup.","synthesize":"Combine user-supplied documents without new external search."}'
---

# Google Scholar

Search **Google Scholar** for scholarly literature: articles, theses, books,
abstracts, preprints, technical reports, patents, and court opinions. Help the
user form precise queries, read result signals, follow citation trails, and reach
readable full text without treating citation count as quality.

This skill is **stateless**. It does not store Google accounts, saved libraries,
alerts, proxy credentials, or personal reading lists in the package.

## When to use

- Build or refine Google Scholar queries (author, title, source, phrases, OR)
- Find recent work with **Since Year** or **Sort by date**, or set up alerts
- Follow **Cited by**, **Related articles**, and **All versions**
- Locate full text via library links, [PDF]/[HTML], repositories, or Unpaywall-style paths
- Read author profiles and citation metrics with appropriate caveats
- Prefer `pubmed` for clinical/biomedical evidence hierarchies and MeSH
- Prefer `multi-engine-web-search` when the question is general web fact-finding
- Prefer `in-depth-research` when methodology, triangulation, and halt criteria dominate

## Safety order (always)

1. Treat Scholar results as an unvetted index: predatory journals, preprints, and
   gray literature can appear beside peer-reviewed work.
2. Do not invent paywall bypasses, credentials, institutional logins, or scraped
   bulk downloads. Prefer legal library, open-access, author, or repository paths.
3. Never store Google account passwords, library proxy secrets, or personal Scholar
   library contents in skill files or reusable logs.
4. Case-law results are informational only — not legal advice (Google Scholar disclaimer).
5. Verify retracted or corrected papers before citing; citation count ≠ trustworthiness.

## Quick workflow

1. Clarify topic, author/title constraints, recency need, and field (STEM, law, humanities).
2. Start with a precise query; use quotes, `author:`, title phrases, and uppercase `OR`.
3. Apply **Since Year** for recent-but-still-relevance-ranked results; use **Sort by date**
   only when newest additions matter more than influence.
4. Open strong candidates; check venue, authors, date, abstract signals, and versions.
5. Expand with **Cited by** (forward), references/backward reading, and **Related articles**.
6. Resolve full text via library link, [PDF]/[HTML], All versions, or author request —
   not cracked mirrors.
7. Hand off to `pubmed`, `in-depth-research`, or `web` when the remaining work leaves Scholar.

## Routing

| Need | File |
| --- | --- |
| Operators, filters, result reading, full text, mistakes | `references/domain.md` |
| Verified official URLs and claim audit (Gate 6) | `references/sources.md` |

## Core rules (summary)

1. Default sort is **relevance**, not date — use sidebar **Since Year** / **Sort by date**.
2. `author:"name"`, quoted titles, and advanced author/title/publication fields beat vague keywords.
3. **Cited by** and **Related articles** are primary expansion tools; snowball from one good paper.
4. Citation count and h-index measure influence/productivity proxies, not correctness.
5. Full text: library links, [PDF]/[HTML], All versions, campus/off-campus library access.
6. Combine Scholar with field databases (PubMed, IEEE, etc.) when coverage or quality filters matter.
7. Preprints and dissertations are useful but preliminary or gray — label them.
8. Do not stop at page one or the abstract alone when the decision is high-stakes.

Load `references/domain.md` before giving detailed operator recipes or access steps.
Load `references/sources.md` when restating product behavior, coverage limits, or metrics claims.
