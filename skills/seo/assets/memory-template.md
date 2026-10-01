# Memory Template — SEO

File formats for everything under `<state_root>/`. `config.yaml` is what the user **declared**; `memory.md` is what the agent **observed**. An observation supplements a declaration.

**Contents:** [config.yaml](#state_rootconfigyaml) · [memory.md](#state_rootmemorymd) · [Status Values](#status-values) · [Audit Report Template](#audit-report-template)

## `<state_root>/config.yaml`

Declared preferences only — what the user stated.

```yaml
site_type: ecommerce        # blog | ecommerce | saas | local | news | directory | auto
target_market: en-GB        # locale used for SERP checks and spelling
tool_access: gsc-only       # gsc-only | paid-suite
risk_posture: conservative  # conservative | standard | aggressive
cms: shopify                # wordpress | shopify | webflow | wix | headless | other | auto
voice_file: voice.md        # long-form style guide in this folder; none if unset
min_impressions: 100        # monthly impressions floor for opportunity lists

# Preference areas — keys added as the user states preferences
reporting:
  depth: priorities-only
  kpi: revenue
conventions:
  title_format: "{page} | {brand}"
scope:
  off_limits: ["/careers/", "/legal/"]
implementation:
  mode: specs               # specs | patches
measurement:
  exclude_branded: true
cadence:
  gsc_review: monthly
```

## `<state_root>/memory.md`

```markdown
# SEO Memory

## Status
status: ongoing
last: YYYY-MM-DD

## Sites

### [site-name]
- Domain: example.com
- Type / platform / market: ecommerce / Shopify / en-GB
- Search Console access: yes/no, property type
- Last audit: [date] → audits/[file]
- Open priorities: [ranked list]
- Constraints: [who ships, release cadence, what is off-limits]

## Keyword Basket

| Query | Site | URL | Position | Checked | Note |
|---|---|---|---|---|---|
| [query] | [site] | [url] | [n] | [date] | [movement, cause] |

## Timeline

| Date | Event | Type |
|---|---|---|
| YYYY-MM-DD | [shipped / Google update / migration / drop] | [ours / Google] |

## Tried And Rejected
<!-- Recommendations the user declined, and the reason. Repropose only with new evidence. -->

## Notes
<!-- Site-specific context, patterns, vocabulary the business uses -->

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning |
|-------|---------|
| `ongoing` | Still learning the site and its constraints |
| `paused` | Work stopped; resume from open priorities |
| `closed` | Engagement finished; keep history for reference |

## Audit Report Template

Save as `<state_root>/audits/YYYY-MM-DD-<site>.md`:

```markdown
# SEO Audit — [site] — YYYY-MM-DD

## Scope
- Properties / locales covered
- Tools used (GSC-only vs paid suite)
- Out of scope

## Top 5 fixes (traffic at stake)

| Rank | URL or system | Issue | Expected impact | Effort |
|---|---|---|---|---|
| 1 | | | | |

## Findings by layer
### Manual actions / security
### Indexing
### Technical / CWV
### On-page
### Content / intent
### Links / entity

## Measurement plan
- Baseline metrics and windows
- What “worked” looks like in GSC

## Appendix
- Exports, screenshots, crawler notes
```
