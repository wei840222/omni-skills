# Research Sources — Fox News Desk

Verified during the 2026-10-22 repair pass. Re-check live before treating a URL as current.

## Official Fox surfaces

- **Fox News homepage** — current headline and live-event link discovery via <https://www.foxnews.com/>
- **Publisher RSS (latest)** — deterministic headline capture via <https://moxie.foxnews.com/google-publisher/latest.xml>
- **Publisher RSS (politics / us / world / opinion / tech / health / sports / entertainment / science)** — section feeds under `https://moxie.foxnews.com/google-publisher/<section>.xml`
- **Fox News RSS alias** — <https://www.foxnews.com/rss> returns the same latest publisher feed body
- **Section pages** — <https://www.foxnews.com/us>, <https://www.foxnews.com/world>, <https://www.foxnews.com/politics>, <https://www.foxnews.com/opinion>, <https://www.foxnews.com/video>, <https://www.foxnews.com/shows>
- **Apps / products** — <https://www.foxnews.com/apps-products/index.html>
- **Event live pages** — slug URLs under `https://www.foxnews.com/live-news/<slug>` (homepage linked examples verified; the bare `/live-news` index returned HTTP 404)

## Negative / boundary findings

- `https://www.foxnews.com/live-news` and trailing-slash variants returned HTTP 404 during verification — do not document a stable live index.
- `https://moxie.foxnews.com/google-publisher/business.xml` and `national.xml` returned HTTP 400 during verification — omit until a live probe succeeds.
- `https://help.foxnews.com` may present bot/CDN interstitial (HTTP 403 observed) — treat help content as best-effort public docs, not a hard dependency.

## Agent Skills / project contract

- Agent Skills specification index — <https://agentskills.io/llms.txt>
- Agent Skills specification — <https://agentskills.io/specification>
- Reference validator package — <https://github.com/agentskills/agentskills/tree/main/skills-ref>
