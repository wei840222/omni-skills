---
name: seo
description: >
  Run technical SEO audits, keyword research, on-page and content optimization,
  competitor gap analysis, migrations, and Google Search Console recovery to improve
  organic visibility. Use when rankings or organic traffic drop, pages are not
  indexed or get deindexed, crawl/index errors appear in Search Console, a migration
  or redesign is planned, content must rank for a target query, Core Web Vitals fail,
  schema/rich results need work, or local/ecommerce/international SEO is in scope.
  Not for paid search ads/PPC bidding (`ads`/`ppc` workflows) or content planning with
  no search target (`content-marketing`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔍"}'
  related-skills: '{"content-marketing":"Content strategy and calendars when there is no ranking target.","analytics":"Traffic and conversion analysis beyond Search Console SEO signals.","market-research":"Broader competitive and market research outside SERP gap work.","html":"Deep semantic markup, forms, and sanitization beyond on-page SEO tags.","web":"General web build, deploy, and CWV engineering under the ranking layer."}'
---

## State location

Resolve `<state_root>` once per invocation before any read/write:

1. Explicit user/host state path for this skill, if provided.
2. Existing candidates, first hit wins: `<workspace>/seo/`, `<workspace>/memory/seo/`, `~/seo/`.
3. If none exist, create `<workspace>/seo/` when the host provides a workspace; otherwise create `~/seo/`.

Use that single `<state_root>` for config, memory, audits, and drafts. If older data exists only under legacy paths such as a prior vendor data folder, move it into `<state_root>/` and state the move in one line. Skill resources stay under `references/` and `assets/` — never mix them with `<state_root>`.

On first use, read `references/setup.md`. File formats live in `assets/memory-template.md`.

```
<state_root>/
├── config.yaml
├── memory.md
├── audits/
└── content/
```

## When to load

Load this skill for **organic search work**:

- site audits: indexing, technical health, on-page, content, links, structure
- ranking or organic traffic drops, deindex events, core-update hits, manual actions
- writing, refreshing, or consolidating pages to rank for a target query
- keyword research, opportunity sizing, competitor SERP gaps, cannibalization
- migrations, redesigns, hreflang, faceted navigation, programmatic page systems
- snippets, packs, AI Overviews, schema/rich results, local/ecommerce/publisher SEO
- Search Console diagnosis, CWV field-data coaching tied to ranking risk

Route away when the ask is mainly:

- paid search ads, bidding, Quality Score → non-SEO ads workflows
- content calendar / brand storytelling with no search target → `content-marketing`
- general analytics dashboards without ranking/index work → `analytics`
- pure HTML/ARIA widget craft → `html`
- general web bugs, hosting, or stack choice without ranking intent → `web`

## Operating loop

1. **Resolve state** — pick `<state_root>`; load `references/setup.md` defaults.
2. **Audit before prescribing** — manual actions → indexing → intent → technical → content → links.
3. **Treat the SERP as the spec** — search the exact query in `target_market` before format advice.
4. **Open only the needed reference** from the table below; keep this file as the always-on router.
5. **Size the prize** — expected clicks before recommending net-new pages or heavy builds.
6. **Ship named fixes** — exact URL + exact change; log outcomes in `<state_root>/memory.md`.

## Quick reference

| Need | Load |
|------|------|
| Setup, defaults, preference loading | `references/setup.md` |
| Audit checklist, timing ranges, config, traps | `references/core-processes.md` |
| Traffic/rank drop recovery, manual actions | `references/recovery.md` |
| Full audit scoping and deliverable shape | `references/audits.md` |
| Keywords, gaps, cannibalization | `references/keywords.md` |
| Content intent, E-E-A-T, refresh/prune | `references/content.md` |
| Alternatives / vs / best-of / pricing pages | `references/commercial-pages.md` |
| Titles, meta, headings, URLs, alt text | `references/on-page.md` |
| IA, clusters, click depth, index bloat | `references/architecture.md` |
| robots, canonicals, sitemaps, status codes | `references/technical.md` |
| LCP / INP / CLS, lab vs field | `references/performance.md` |
| JS/SPA rendering gaps, soft 404s | `references/javascript.md` |
| JSON-LD, rich results, product feeds | `references/schema.md` |
| Internal links, backlinks, disavow | `references/links.md` |
| GBP, map pack, service-area SEO | `references/local.md` |
| Categories, facets, variants, stock | `references/ecommerce.md` |
| hreflang, markets, translated duplicates | `references/international.md` |
| Domain/platform/URL migrations | `references/migrations.md` |
| Snippets, PAA, sitelinks, packs | `references/serp-features.md` |
| AI Overviews, assistant citations, llms.txt | `references/ai-search.md` |
| GSC reports, exports, proving changes | `references/search-console.md` |
| Bing, IndexNow, other engines | `references/other-engines.md` |
| News, Discover, Top Stories | `references/news-discover.md` |
| Templated page systems at scale | `references/programmatic.md` |
| WordPress / Shopify / Webflow / Wix / Next | `references/cms-platforms.md` |
| Gate 6 source URLs | `references/sources.md` |

## Core rules

1. **Audit before prescribing.** Order: manual actions → indexing → intent match → technical → content → links. Content quality work on a never-indexed URL wastes the cycle.
2. **The SERP is the spec.** Search the exact query in the target market. Page 1 sets format, depth, and freshness. Product-grid SERPs will not reward a 3,000-word guide.
3. **Improve before you create.** GSC positions 4–15 with impressions ≥ `min_impressions` (default 100/month in `references/core-processes.md`) are highest ROI: snippet, content gaps, internal links. Add a URL only when no existing page owns the intent.
4. **One intent per page.** Alternating URLs for one query means cannibalization — 301/merge the weaker into the stronger. Map by intent, not string equality.
5. **Technical floor.** CrUX p75 “good”: LCP < 2.5s, INP < 200ms, CLS < 0.1. HTTPS, mobile-first, self-referencing canonicals, clean sitemap. Technical debt caps content gains.
6. **E-E-A-T is demonstrated, not scored.** Author credentials, first-hand evidence, citations, contact/about pages — decisive on YMYL (health, finance, legal, safety).
7. **Links: earn exclusively.** Paid/PBN patterns risk manual actions. Spend internal links before outreach.
8. **Iterate from Search Console.** Low CTR at solid position → rewrite snippet. Impressions, no clicks → intent/SERP-feature mismatch. No impressions → indexing or relevance.
9. **Size the prize first.** `expected monthly clicks ≈ volume × realistic CTR × (1 − feature discount)`. Example: 2,000 × 0.07 × 0.6 ≈ 84 clicks/mo. If that does not justify the build, say so before writing.

## Ranking drop triage

Stop at the first confirmed cause:

1. GSC Manual Actions + Security Issues → `references/recovery.md`.
2. URL Inspection: still indexed? Google-selected canonical changed?
3. Recent deploys: robots.txt, noindex, redirects, template changes near the drop.
4. Drop date vs announced Google updates → sitewide quality reassessment.
5. SERP format change (AI Overview, ads, packs) at the same rank.
6. Backlink losses or competitor gains.
7. Seasonality / tracking breakage (tag, bot filter, property change).
8. Else gap-compare replacement pages via `references/keywords.md`.

## Output gates

Before delivering recommendations or draft copy:

- Did I search the actual query in the target market?
- Did I check for an existing intent-owning URL before recommending a new page?
- Are cited numbers from this skill, GSC, or the user’s data — not improvised?
- Does each fix name exact URL + exact change?
- Did I size expected clicks so the user can refuse the work?
- Am I avoiding hard ship dates? State mechanism + range from `references/core-processes.md` “What Takes How Long”.
- Am I stating the next diagnostic check as a positive action rather than a pile of prohibitions?

## Progressive disclosure

Keep this file as the always-on entry. Load `references/*` only when the task needs depth beyond the rules above. Persist only user-declared preferences and observed site facts under `<state_root>/`. Prefer one reference file at a time unless triage names a chain.
