# GIF Sources and APIs

Load this file when searching for existing GIFs or calling provider APIs.

## Where to find GIFs

| Site | Best for | API |
|------|----------|-----|
| **Giphy** | General, trending, reactions | Yes (API key required) |
| **Tenor** | Messaging-app style results | Yes (API key required) |
| **Imgur** | Viral/community clips | Yes (separate Imgur API) |
| **Reddit r/gifs** | Niche, community-specific | No first-class GIF search API here |

Prefer provider search APIs when keys exist. Fall back to user-supplied URLs or local files when keys are absent—do not scrape login-walled content.

## Credentials

- Read `GIPHY_API_KEY` or `TENOR_API_KEY` from the environment.
- Never commit keys, paste them into skill files, or echo them in full.
- If a key is missing, say which env var is required and offer a non-API path (user URL, local file, or manual search instructions).

## Giphy search

Official docs: [Giphy API endpoints](https://developers.giphy.com/docs/api/endpoint/#search)

```bash
curl -fsS "https://api.giphy.com/v1/gifs/search?api_key=${GIPHY_API_KEY}&q=thumbs+up&limit=10&rating=pg"
```

Useful query params (verify against live docs if behavior changes):

- `q` — search string
- `limit` — page size
- `offset` — pagination
- `rating` — content rating filter when appropriate
- `lang` — language code for query interpretation

Parse JSON for `data[].images` variants (preview vs full). Prefer smaller preview renders for chat shortlists, then fetch the user-selected full asset.

## Tenor search

Official docs: [Tenor API endpoints](https://developers.google.com/tenor/guides/endpoints)

```bash
curl -fsS "https://tenor.googleapis.com/v2/search?key=${TENOR_API_KEY}&q=thumbs+up&limit=10&media_filter=gif"
```

Notes:

- Tenor v2 uses `key` and returns media objects under result items.
- Filter to GIF when the user explicitly needs `.gif`; otherwise consider mp4/webm variants if the client accepts them.
- Handle empty `results` as a soft miss: broaden query once, then report no match.

## Safe handling of results

1. Show a short shortlist (title/id + preview URL), not a bulk dump of every rendition.
2. Do not hotlink private or non-CDN URLs the user did not authorize to share externally.
3. Attribution: when the UI/context expects provider attribution, keep the provider and creator fields from the API response.
4. Redistribution and commercial use follow provider terms—do not invent license grants.

## Offline / no-key fallback

- Accept a user-provided GIF/video path and run creation/optimization instead.
- Provide the official developer portal links so the user can create keys if they want API search later.
