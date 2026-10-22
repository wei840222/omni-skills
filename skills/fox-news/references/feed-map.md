# Feed Map — Fox News Desk

Use official Fox-owned surfaces first. Verify a route with a live HEAD/GET before treating it as current; Fox retires some index URLs while keeping slug-based event pages.

## Primary surfaces

| Surface | URL | Use when | Notes |
|---|---|---|---|
| Latest RSS | `https://moxie.foxnews.com/google-publisher/latest.xml` | Fast top-line sweep | Broadest Fox headline mix; also mirrors at `https://www.foxnews.com/rss` |
| Politics RSS | `https://moxie.foxnews.com/google-publisher/politics.xml` | Politics monitoring | Prefer over homepage filtering |
| U.S. RSS | `https://moxie.foxnews.com/google-publisher/us.xml` | Domestic news | Pair with `/us` page when context is needed |
| World RSS | `https://moxie.foxnews.com/google-publisher/world.xml` | International coverage | Pair with `/world` page when context is needed |
| Opinion RSS | `https://moxie.foxnews.com/google-publisher/opinion.xml` | Explicit opinion/editorial asks | Keep separate from straight-news summaries |
| Tech RSS | `https://moxie.foxnews.com/google-publisher/tech.xml` | Technology section sweeps | Verified publisher feed |
| Health RSS | `https://moxie.foxnews.com/google-publisher/health.xml` | Health section sweeps | Verified publisher feed |
| Sports RSS | `https://moxie.foxnews.com/google-publisher/sports.xml` | Sports section sweeps | Verified publisher feed |
| Entertainment RSS | `https://moxie.foxnews.com/google-publisher/entertainment.xml` | Entertainment sweeps | Verified publisher feed |
| Science RSS | `https://moxie.foxnews.com/google-publisher/science.xml` | Science sweeps | Verified publisher feed |
| U.S. page | `https://www.foxnews.com/us` | Domestic page context | Use when RSS is too thin or needs section framing |
| World page | `https://www.foxnews.com/world` | International page context | Use before general search |
| Politics page | `https://www.foxnews.com/politics` | Politics page context | Complements politics RSS |
| Opinion page | `https://www.foxnews.com/opinion` | Columnist / editorial coverage | Explicit opinion asks only |
| Video page | `https://www.foxnews.com/video` | Clips, segments, show highlights | Public fallback when live TV is gated |
| Shows page | `https://www.foxnews.com/shows` | Show directory / host-focused asks | Not a substitute for straight-news RSS |
| Apps / products | `https://www.foxnews.com/apps-products/index.html` | App or device workflow questions | Pair with public help pages when available |
| Event live pages | `https://www.foxnews.com/live-news/<event-slug>` | Ongoing events still updating | There is **no** stable `/live-news` index (404); discover current slugs from homepage/section links or search, then open one event page |

## Routing rules

1. Use one surface first, not three at once.
2. Prefer RSS for deterministic headline capture; use page routes for section framing and event live pages for rolling updates.
3. Keep `opinion`, `video`, and `shows` requests explicit so they do not leak into general briefings.
4. Treat `business` / `national` publisher feed slugs as unverified until a live probe returns HTTP 200 with RSS XML — do not invent them from memory.

## Fast shell checks

```bash
curl -sS https://moxie.foxnews.com/google-publisher/latest.xml | head
curl -sS https://moxie.foxnews.com/google-publisher/politics.xml | head
curl -sS -A 'Mozilla/5.0' https://www.foxnews.com/ | rg -o 'https://www\.foxnews\.com/live-news/[^\"[:space:]]+' | head
```

Quick title extraction from RSS:

```bash
python3 - <<'PY'
import xml.etree.ElementTree as ET
import urllib.request

url = "https://moxie.foxnews.com/google-publisher/latest.xml"
root = ET.fromstring(urllib.request.urlopen(url, timeout=20).read())
for item in root.findall(".//item")[:5]:
    print(item.findtext("title", "").strip())
PY
```

Use commands only to inspect public pages and feeds. Do not automate credentialed playback or account flows.
