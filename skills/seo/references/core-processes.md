# Core Processes

## SEO Audit Checklist

**Indexing:**
- [ ] Important pages indexed — verify with URL Inspection and the Page indexing report, not the `site:` operator
- [ ] No important pages blocked in robots.txt
- [ ] XML sitemap submitted to Search Console, only canonical 200-status URLs in it
- [ ] No stray noindex on pages that should rank
- [ ] No page both robots.txt-blocked AND noindexed — blocked crawl means Google omits the noindex, so the page can stay indexed

**Technical:**
- [ ] Core Web Vitals passing (thresholds in rule 5)
- [ ] Mobile-friendly, HTTPS with no mixed content
- [ ] No crawl errors, no soft 404s, no server errors in Search Console
- [ ] Redirect chains ≤3 hops
- [ ] Rendered HTML contains the main content (JavaScript sites)

**On-Page:**
- [ ] Unique title tags (50-60 chars), meta descriptions (150-160 chars)
- [ ] One H1 per page with the target term; proper heading hierarchy
- [ ] Images with alt text; internal links to and from the page

**Content:**
- [ ] Search intent matched (rule 2)
- [ ] No cannibalization (rule 4)
- [ ] No thin or duplicate content; dead pages improved, consolidated, or removed

**Off-Page and Entity:**
- [ ] Google Business Profile complete (local businesses)
- [ ] Backlink profile checked for toxic patterns
- [ ] Brand queries return the right result, sitelinks, and knowledge panel where applicable


## Content Writing Process

1. **Keyword research** — target keyword, volume, SERP reality check (`keywords.md`)
2. **Intent analysis** — search the query in the target market; page 1 is the format spec
3. **Gap + gain** — cover what ranking pages cover, then add what none of them have
4. **Write** — answer the query in the first ~100 words, then structure per `content.md`
5. **Optimize** — title, meta, headers, internal links from strong pages, schema
6. **Publish** — request indexing once, log in `<state_root>/memory.md`, review GSC after a few weeks


## What Takes How Long

Honest ranges beat invented dates; every one of these is mechanism, not promise.

| Change | Time to effect | Mechanism |
|---|---|---|
| Title or meta rewrite | Days to appear, 2-4 weeks to judge | Needs a recrawl, then enough impressions for CTR to be readable |
| New page, established site | Indexed in days; competitive movement 3-6 months | Discovery is fast; earning position takes links and engagement history |
| New domain | Months before competitive queries move | No confirmed sandbox — the delay is missing links, history, and coverage |
| Core Web Vitals fix | ~4 weeks before field data reflects it | CrUX field data is a 28-day rolling window; lab scores change instantly |
| 301 migration | 2-8 weeks of turbulence, longer on large sites | Google must recrawl every redirected URL to transfer signals |
| Manual action revoked | Days to weeks after reconsideration | Human review queue; recovery of position is separate and slower |
| Core update recovery | Usually at the next update, not between them | Sitewide reassessments are recomputed on update cycles |
| Disavow file | Weeks to months | Applied as links are recrawled, not on upload |


## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| site_type | blog \| ecommerce \| saas \| local \| news \| directory \| auto | auto | Weights the audit checklist and decides which guide the router opens first; `auto` infers from URL patterns and page templates on first look |
| target_market | text (locale, e.g. en-US) | en-US | Which SERP to check, which spelling variant to write, and whether hreflang and local guidance apply |
| tool_access | gsc-only \| paid-suite | gsc-only | `gsc-only` keeps every workflow on free data (GSC, Trends, SERPs); `paid-suite` unlocks backlink-index and difficulty-score steps |
| risk_posture | conservative \| standard \| aggressive | conservative | Gates link tactics, external anchor ratios, and how much templated page generation to recommend |
| cms | wordpress \| shopify \| webflow \| wix \| headless \| other \| auto | auto | Picks the implementation path for every fix (where redirects, robots, and metadata actually live) |
| min_impressions | number (impressions/month) | 100 | Floor for every opportunity list: striking distance (rule 3, `keywords.md`, `search-console.md`) and the traffic-at-stake cutoff for the audit Top 5. Below it, a page cannot produce a readable CTR or click change — raise it on large sites |
| voice_file | path | none | Brand voice guide at `<state_root>/<file>`; governs drafted copy, retaining SEO structural control |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:

- **Reporting**: audit depth (one-page priorities vs full report), technical vs business language, which KPI leads (clicks, conversions, revenue)
- **Conventions**: URL and slug style, title formula (brand position and separator), heading patterns, internal anchor style
- **Scope boundaries**: sections that are off-limits (legal, careers, docs), staging hosts, URLs strictly excluded
- **Implementation**: whether the agent edits files and writes patches or hands over specs and tickets
- **Measurement**: reporting property, comparison window, whether branded queries are excluded from "SEO traffic"
- **Thresholds**: floors that gate what gets worked on — impressions (`min_impressions`), traffic at stake for a finding to make the Top 5, minimum sample before a test is called
- **Cadence**: rank and GSC review frequency, content refresh schedule, reporting date


## Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Writing before checking the SERP | Format mismatch = no ranking at any quality | Rule 2: the SERP is the spec |
| New article for a query an existing page ranks 4-15 for | Cannibalization splits signals | Improve the existing page (rule 3) |
| Chasing keyword density | No density threshold exists; stuffing detection is pattern-based | Cover the topic, use variants naturally |
| noindex on a robots.txt-blocked page | Google omits it, omits the noindex | Allow crawl until deindexed, then block |
| Changing URLs without 301s | Links and authority now point at 404s | Map every old URL to its closest new match |
| Buying links or PBNs | Payment and network footprints → manual action | Earn links via assets and digital PR |
| Reporting rank without checking the rendered SERP | #1 under an AI Overview and four ads earns a fraction of historical #1 clicks | Check pixel position, not just rank |
| Judging index coverage with `site:domain.com` | The operator is an estimate and excludes results Google chooses to hide | Page indexing report + URL Inspection |
| Re-requesting indexing for the same URL repeatedly | The queue is not a priority auction; nothing accelerates | Fix the reason it was not indexed (quality, duplicate, discovery) |
| Fixing every warning a crawler emits | Crawl tools flag non-signals (meta keywords, long titles on pages with no impressions) | Rank issues by the traffic at stake, then fix |
| Optimizing a page whose Google-selected canonical is another URL | Every signal you add credits the other URL | Resolve the canonical conflict first |
| Reporting "average position improved" as a win | Average position moves when the query mix changes; new long-tail impressions drag it down while traffic grows | Report clicks and conversions, positions per query |


## Where Experts Disagree

- **Word count.** Studies show correlation between length and ranking; studies focus purely on correlation. Cover the intent fully, then conclude — padding is a negative.
- **Disavow.** Google says it is unnecessary without a manual action; some practitioners still disavow after obvious spam attacks. Default: disavow strictly when a manual action names links.
- **Exact-match anchors.** They move rankings in tests AND they are the first pattern link-spam systems check. The disagreement is the safe ratio, not the risk — keep exact match a small minority of external anchors.
- **Subdomain vs subfolder.** Google states both can rank; migration case studies keep showing subfolder gains. Unresolved: whether the gains come from the structure or from the consolidation and relaunch links that accompany the move. Default subfolder for new builds; migrate working subdomains strictly for confirmed structural benefits beyond rankings.
- **Optimizing for AI Overviews.** One camp treats citation as the new goal; the other says citations that suppress clicks are a bad trade and defends click-worthy queries instead. Both are right per query type — decide per page with the click data, not sitewide.
