---
name: hacker-news
description: Search Hacker News, fetch top stories, read comments, and browse user profiles or hiring threads. Use when the user wants live HN frontpage data, Algolia full-text search, Who is hiring threads, or user/item lookups.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🟠"}'
  related-skills: '{"api":"Use for general third-party API client patterns (auth, pagination, retries) outside HN-specific endpoints.","http":"Use for HTTP caching, redirects, and status-code behavior that is not HN-specific.","news":"Use for personalized multi-source news briefings rather than live Hacker News API access."}'
---

## State location

This skill is stateless and does not store local configuration. Prefer in-memory results for the current turn; do not write HN caches unless the user explicitly requests a separate host-owned path.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| API endpoints | `references/api.md` | Fetching story lists, items, users, or Algolia item/user lookups |
| Search patterns | `references/search.md` | Full-text search, tag filters, date/points filters, hiring threads |
| Domain knowledge | `references/research.md` | Confirming API roles, rate-limit claims, or pagination limits |
| Research sources | `references/sources.md` | Citing or refreshing official HN / Algolia documentation |

## Workflow

1. Decide the data need: live lists/items → Firebase Official API; full-text / filters / hiring threads → Algolia HN Search.
2. Load only the matching reference file; keep `SKILL.md` as the control plane.
3. For Official API lists, fetch ID arrays first, then parallelize `/item/{id}.json` for the requested slice.
4. For Algolia, set `tags` and `numericFilters` explicitly; keep `hitsPerPage * page <= 1000`.
5. On Algolia HTTP 429, exponential backoff; if Algolia is unreachable, fall back to recent Firebase lists and say the search filter was skipped.
6. Skip `deleted` / `dead` items; for Ask/Show HN without `url`, use the `text` field.

## Core Rules

### 1. Two APIs Available
| API | Use Case | Base URL |
|-----|----------|----------|
| Official HN API | Single items, real-time lists | `https://hacker-news.firebaseio.com/v0` |
| Algolia Search | Full-text search, filters | `https://hn.algolia.com/api/v1` |

### 2. Official API Endpoints
- `/topstories.json` — top 500 story IDs
- `/newstories.json` — newest 500 story IDs
- `/beststories.json` — best stories
- `/askstories.json` — Ask HN
- `/showstories.json` — Show HN
- `/jobstories.json` — job postings
- `/item/{id}.json` — story/comment details
- `/user/{username}.json` — user profile

### 3. Algolia Search Syntax
```
/search?query=TERM&tags=TAG&numericFilters=FILTER
```

**Tags (combinable with AND):**
- `story`, `comment`, `poll`, `job`, `ask_hn`, `show_hn`
- `author_USERNAME` — posts by user
- `story_ID` — comments on story

**Numeric filters:**
- `created_at_i>TIMESTAMP` — after date
- `points>N` — minimum points
- `num_comments>N` — minimum comments

### 4. Common Patterns
| Request | Endpoint |
|---------|----------|
| Frontpage | Official `/topstories.json` → fetch first N items |
| Search posts | Algolia `/search?query=X&tags=story` |
| User's posts | Algolia `/search?tags=author_USERNAME` |
| Who is hiring? | Algolia `/search?query=who is hiring&tags=story,author_whoishiring` |
| Comments on story | Algolia `/search?tags=comment,story_ID` |
| This week's top | Algolia `/search?tags=story&numericFilters=created_at_i>WEEK_TS` |

### 5. Response Handling
- Official API returns IDs → batch fetch items (parallelize)
- Algolia returns full objects with `hits[]`
- Story object: `id`, `title`, `url`, `score`, `by`, `time`, `descendants`
- Comment object: `id`, `text`, `by`, `parent`, `time`

### 6. Rate Limits and Recovery
- Official API: anonymous access, generous limits
- Algolia: about 10,000 requests/hour without a key; on HTTP 429 use exponential backoff
- Always paginate with `page` / `hitsPerPage`; Algolia rejects deep pages beyond `hitsPerPage * page <= 1000`
- Fallback: if Algolia is unreachable, use Firebase recent/top lists and disclose that keyword filters were unavailable

### 7. Gotchas
- `url` is null for Ask HN/Show HN text posts — use `text`
- `deleted` and `dead` items exist — check before displaying
- Timestamps are Unix seconds, not milliseconds
- Algolia `objectID` equals HN item `id` as a string
