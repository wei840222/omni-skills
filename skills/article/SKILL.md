---
name: article
description: >
  Draft news, feature, and opinion articles with journalistic structure,
  source hierarchy, fact-check discipline, audience-calibrated readability,
  and people-first on-page SEO. Use when writing or rewriting a published
  article, long-form post, reported feature, op-ed, or editorial package;
  when a draft needs a stronger lead, inverted-pyramid news structure,
  attribution, subheads, or scannable digital layout; when audience grade
  level, active voice, or meta title/description must be tuned; or when
  reviewing article drafts for source balance and claim safety. Not for
  personal voice drafting across formats (writing), marketing/sales copy
  (copywriting), search-engine technical audits (seo), versioned multi-draft
  workspaces (write), robotic-prose cleanup alone (writer), personal journals
  (journal), or news briefings/digests (news/digest).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📰"}'
  related-skills: '{"writing":"General prose drafting and voice matching across emails, posts, and memos.","copywriting":"Persuasive marketing and conversion copy rather than journalistic articles.","seo":"Technical SEO, crawl/index, and keyword research beyond article on-page tuning.","write":"Versioned draft workspaces, briefs, and audit scripts for multi-revision pieces.","writer":"Diagnose and rewrite robotic AI prose patterns after the article structure is set.","content-marketing":"Editorial calendars, funnel strategy, and distribution around finished articles.","storytelling":"Narrative arc craft for stories that are not reported articles.","journal":"Private reflective journaling rather than publishable articles.","grammar":"Grammar and mechanics-only proofreading.","news":"Recurring personalized news briefings instead of single article drafts.","digest":"Curated multi-source digests rather than one authored article.","newsletter":"Subscriber newsletter growth and issue packaging."}'
---

# Article

Produce publishable **articles** — news reports, features, and opinion pieces —
with source discipline first and polish second. Prefer verified structure over
clever wording. Do not invent quotes, statistics, or eyewitness detail.

This skill is **stateless**. Optional user preference notes may live under a
host-provided path outside the skill package; never store drafts or sources
inside `skills/article/`.

## When to use

- Draft or rewrite a news story, feature, explainers, or opinion/editorial piece
- Strengthen lead hooks, inverted-pyramid news leads, or delayed-feature openings
- Enforce source hierarchy, attribution format, and three-layer fact checks
- Tune readability for general, professional, or technical audiences
- Add scannable subheads, short paragraphs, and people-first SEO metadata
- Review a draft for claim safety, balance, and voice fit (news vs opinion vs feature)

Hand off elsewhere when the job is really:

- multi-format personal voice work → `writing`
- ads/landing conversion copy → `copywriting`
- crawl, index, CWV, keyword systems → `seo`
- versioned workspace + scripts → `write`
- AI-prose pattern cleanup only → `writer`
- calendar/funnel strategy → `content-marketing`
- private journaling → `journal`
- briefing/digest products → `news` / `digest`

## Quick workflow

1. **Brief** — Capture audience, purpose (news / feature / opinion), length target, publication channel, and non-negotiable facts the user already owns.
2. **Load references** — Open only what the task needs from the table below.
3. **Structure** — Choose form: inverted pyramid (news), narrative feature, or opinion with position + counterpoint.
4. **Draft** — Lead first; then body with attribution; keep paragraphs short and scannable for digital.
5. **Verify claims** — Run the three-layer fact-check; mark unknowns instead of inventing sources.
6. **Calibrate** — Match readability band, active-voice floor, and voice rules for the chosen form.
7. **Package** — Title, meta description, subheads, and external-link budget when the piece will be published on the web.
8. **Deliver** — Return the article, then a short production note (form used, open claim risks, SEO package).

## Progressive disclosure

| Resource | Load when |
|---|---|
| `references/writing-standards.md` | Lead formulas, source hierarchy, attribution, fact-check protocol, red flags |
| `references/optimization.md` | Readability bands, engagement layout, SEO packaging, publication-voice rules |
| `references/sources.md` | Verified external standards used to set thresholds and packaging guidance |

## Core rules

1. **Truth over polish** — Do not fabricate quotes, numbers, titles, or primary-source access. If evidence is missing, say so and ask or hedge.
2. **Form follows assignment** — News stays objective with multiple perspectives; opinion states a clear position and acknowledges counterpoints; features may use scene and character but still attribute facts.
3. **Lead earns the next line** — First sentence ≤25 words when possible; core who/what/why (or the opinion stake) appears within the first ~100 words.
4. **Sources have ranks** — Prefer primary documentation and named participants; experts next; other journalism last. Attribute every non-obvious claim.
5. **Scan-friendly body** — Digital pieces use meaningful subheads, short paragraphs (about 2–3 sentences), and one idea per paragraph (NN/g scanning research).
6. **People-first SEO** — Write the article for humans first; titles and meta descriptions summarize honestly without shock bait (Google Search Central).
7. **Active voice default** — Prefer active constructions; keep passive for unknown actor or deliberate emphasis (plain-language guidance).
8. **No promotional residue** — Do not inject skill-catalog marketing, vendor homepages, or self-promotional marketplace links into article outputs.

## Output contract

Unless the user asks otherwise, return:

1. **Title**
2. **Article body** (with subheads when length warrants)
3. **Optional SEO package** — meta title suggestion and meta description when web publishing is in scope
4. **Production note** — form used (news/feature/opinion), audience band, unresolved claim risks, sources the user still must supply

## Failure modes

| Symptom | Response |
|---|---|
| User wants ads/landing CTA copy | Redirect to `copywriting`; do not stretch article rules into conversion copy |
| No facts provided for a reported piece | Ask for source material or write only clearly labeled analysis/opinion without invented evidence |
| Conflicting brief (news tone + hard sell) | Clarify primary form; refuse to blend undisclosed advertorial |
| Technical SEO crawl/index issues | Hand off to `seo` |
| Draft is structured but sounds robotic | Finish article rules, then offer `writer` for prose cleanup |
