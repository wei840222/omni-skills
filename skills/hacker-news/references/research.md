# Hacker News Domain Knowledge

- **Official API role**: The Firebase HN API is a read-only public API for live item graphs and ranked ID lists. Primary reference: https://github.com/HackerNews/API
- **No auth for public reads**: Official endpoints under `https://hacker-news.firebaseio.com/v0` require no API key for anonymous read access.
- **List-then-item pattern**: Ranked endpoints return up to 500 IDs; callers must fetch `/item/{id}.json` for titles, scores, and comments.
- **Algolia HN Search role**: Full-text search, tag filters, and date/score filters use `https://hn.algolia.com/api/v1`. Docs: https://hn.algolia.com/api
- **Hiring threads**: Monthly “Who is hiring?” posts are authored by `whoishiring`; query with `tags=story,author_whoishiring`.
- **Pagination ceiling**: Algolia HN Search effectively caps retrieval with `hitsPerPage * page <= 1000`; deeper offsets fail or return empty.
- **Rate-limit recovery**: Treat Algolia HTTP 429 as temporary; exponential backoff, then fall back to Firebase lists when search is unavailable.
- **Text posts**: Ask HN / Show HN often omit `url`; the body lives in `text`.
- **Moderation fields**: Items may be `deleted` or `dead`; skip them in user-facing summaries.
