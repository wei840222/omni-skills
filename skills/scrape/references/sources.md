# Sources for scrape checks

Prefer opening the live page over memorized rules when validating format, legal boundaries, or HTTP politeness claims.

## Agent Skills specification

- Document index — https://agentskills.io/llms.txt
- Normative specification — https://agentskills.io/specification
- Optional directories — https://agentskills.io/specification#optional-directories
- Progressive disclosure — https://agentskills.io/specification#progressive-disclosure
- File references — https://agentskills.io/specification#file-references
- Reference validator package — https://github.com/agentskills/agentskills/tree/main/skills-ref

Reproducible validate command used in this repository:

```bash
uvx --from skills-ref agentskills validate skills/<slug>
```

## OpenClaw skill metadata (when the host is OpenClaw)

- OpenClaw skills overview — https://docs.openclaw.ai/tools/skills
- Creating skills — https://docs.openclaw.ai/tools/creating-skills

Confirm field support on the live docs before encoding `metadata.openclaw` keys.

## robots.txt and crawl politeness

- RFC 9309 — Robots Exclusion Protocol — https://www.rfc-editor.org/rfc/rfc9309.html
- Google robots.txt introduction — https://developers.google.com/search/docs/crawling-indexing/robots/intro
- Google robots.txt specifications overview — https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt
- Python `urllib.robotparser` — https://docs.python.org/3/library/urllib.robotparser.html

## HTTP rate limits and client behavior

- MDN HTTP 429 Too Many Requests — https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
- MDN Retry-After — https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After
- RFC 9110 HTTP Semantics (status codes) — https://www.rfc-editor.org/rfc/rfc9110.html

## Legal and privacy orientation (not legal advice)

- hiQ Labs v. LinkedIn (9th Cir. 2022) opinion context — https://cdn.ca9.uscourts.gov/datastore/opinions/2022/04/18/17-16783.pdf
- Van Buren v. United States (U.S. 2021) opinion — https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf
- GDPR official text (EUR-Lex) — https://eur-lex.europa.eu/eli/reg/2016/679/oj
- California CCPA/CPRA overview (California AG) — https://oag.ca.gov/privacy/ccpa

These orient compliance checklists; they do not replace counsel. For structured IRAC framing use the in-repo `legal` skill.

## Local repository contracts

When working inside `omni-skills`, also honor:

- `.agents/AGENTS.md`
- `.agents/workflows/skill-refactor.md`
- `.agents/workflows/skill-review.md`
