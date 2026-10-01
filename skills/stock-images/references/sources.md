# Sources — Stock Images (Gate 6)

Verified during the 2026-10-02 refactor handoff. Prefer these URLs in PR notes and agent explanations.

## Placeholder and photo utilities

- **Lorem Picsum** — size, id, seed, grayscale, blur, format, list API patterns via https://picsum.photos/
- **Picsum implementation reference** — https://github.com/DMarby/picsum-photos
- **Placehold.co** — size, color, text, format, retina rules via https://placehold.co/
- **DummyImage** — alternate keyless dimensions via https://dummyimage.com/
- **PlaceKeanu** — live keyless Keanu placeholders via https://placekeanu.com/800/600 (HTTP 200 at verification time)

## Official stock APIs

- **Unsplash developers hub** — https://unsplash.com/developers
- **Unsplash API documentation** — demo rate limit 50 req/hour, Client-ID auth, hotlinking requirement via https://unsplash.com/documentation
- **Unsplash JS client** — https://github.com/unsplash/unsplash-js
- **Pexels API hub** — https://www.pexels.com/api/
- **Pixabay API docs** — endpoint, required `key`, default 100 req/60s via https://pixabay.com/api/docs/

## Deprecation / breakage evidence

- Live probe: `https://source.unsplash.com/800x600/?nature` → **HTTP 503** (verified 2026-10-02)
- Historical Source host snapshots remain on the Wayback Machine index: https://web.archive.org/web/*/https://source.unsplash.com/
- Community discussion of Source outages: https://news.ycombinator.com/item?id=30892841

Do not cite the deleted blog slug `https://unsplash.com/blog/the-end-of-source-unsplash-com/` (HTTP 404 at verification time).

## Specialized endpoints checked reachable

- https://api.dicebear.com
- https://boringavatars.com
- https://thispersondoesnotexist.com
- https://uifaces.co
- https://iconify.design
- https://feathericons.com
- https://heroicons.com
- https://lucide.dev
- https://undraw.co
- https://www.remove.bg/api

## License reminder

Always open the provider's current license/API guideline page before asserting commercial reuse rights. Unsplash API integrations must follow https://help.unsplash.com/api-guidelines/unsplash-api-guidelines and attribution guidance linked from the API docs.
