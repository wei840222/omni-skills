---
name: stock-images
description: >
  Source free stock photos and generate placeholder image URLs for mockups,
  prototypes, websites, and presentations. Use when the user needs Lorem Picsum
  or Placehold.co placeholders, consistent image IDs across reloads, Unsplash /
  Pexels / Pixabay stock photos via official APIs, avatar/icon illustration URLs,
  or guidance after deprecated source.unsplash.com links fail. Not for generative
  image models (`image-generation`) or binary image compression/format work (`image`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📸"}'
  related-skills: '{"design":"Visual design direction before picking photo subjects or placeholder style.","frontend":"Embed returned URLs into layouts, components, and responsive image tags.","image":"Compress, convert, or optimize the final asset after a URL is chosen.","image-generation":"Create original AI images when stock/placeholder libraries are not enough.","ui":"UI kits and interface patterns that consume the selected image assets."}'
---

## State location

This skill is **stateless by default**. Prefer returning ready-to-use URLs with no disk writes.

If the user asks to remember preferred providers, sizes, style, or saved URLs, resolve `<state_root>` once per invocation before any read/write:

1. Explicit user/host state path for this skill, if provided.
2. Existing candidates, first hit wins: `<workspace>/stock-images/`, `<workspace>/memory/stock-images/`, `~/stock-images/`.
3. If none exist, create `<workspace>/stock-images/` when the host provides a workspace; otherwise create `~/stock-images/`.

Use that single `<state_root>` for optional preference memory only. Skill resources stay under `references/` and `assets/` — never mix them with `<state_root>`. Template: `assets/memory-template.md`.

```
<state_root>/
└── memory.md
```

## Execution

On first use, load `references/setup.md` for the selection workflow. Load `references/providers.md` when you need full provider URL catalogs, API notes, or specialized avatar/icon endpoints. Load `references/sources.md` when citing licenses, deprecations, or rate limits.

## When to use

- Mockups and wireframes that need immediate placeholder dimensions
- Prototypes that must keep the **same** photo across reloads (`/id/` or `/seed/`)
- Production-bound free stock search via Unsplash / Pexels / Pixabay APIs
- Avatar, icon, or illustration URL suggestions for UI shells
- Repairing broken `source.unsplash.com` hotlinks

## Quick reference

| Need | First choice | Notes |
|------|--------------|-------|
| Random photo by size | Lorem Picsum | No API key |
| Stable photo across reloads | Picsum `/id/{n}/` or `/seed/{s}/` | Prefer over `?random=` |
| Colored box + text | Placehold.co | SVG default; PNG/JPEG/WebP/AVIF supported |
| Subject search (nature, office…) | Unsplash / Pexels / Pixabay APIs | Requires free developer key |
| Deprecated Unsplash Source URL | Do not emit `source.unsplash.com` | Live endpoint returns HTTP 503 |

## Core rules

### 1. Prefer keyless direct URLs for mockups

Return a concrete URL first, then optional alternatives.

```text
https://picsum.photos/800/600
https://picsum.photos/id/237/800/600
https://picsum.photos/seed/layout-a/800/600
https://placehold.co/800x600
https://placehold.co/800x600/EEE/31343C?text=Hero
https://placekeanu.com/800/600
```

### 2. Match provider to intent

| Intent | Provider |
|--------|----------|
| Generic photo placeholder | Lorem Picsum |
| Dimension/color/text box | Placehold.co |
| Named subject stock photo | Unsplash, Pexels, or Pixabay API |
| Face / avatar seed | DiceBear, RoboHash, Boring Avatars, thispersondoesnotexist |
| Icons | Iconify, Lucide, Heroicons, Feather |

### 3. Keep prototypes consistent

- Use Picsum `id` or `seed` when the layout must not reshuffle images.
- Save the final redirected Unsplash CDN URL only after an official API response.
- Use `?random=N` only when intentional variety is required.

### 4. Official APIs for production stock

- **Unsplash**: register an application; demo mode is **50 requests/hour**; send `Authorization: Client-ID <access_key>`; hotlink the image URLs returned by the API. Docs: https://unsplash.com/documentation
- **Pexels**: free API key via https://www.pexels.com/api/
- **Pixabay**: default **100 requests / 60 seconds** per key+IP; `GET https://pixabay.com/api/`. Docs: https://pixabay.com/api/docs/

Never invent API keys. Use host secrets or placeholders such as `<UNSPLASH_ACCESS_KEY>`.

### 5. Licensing and attribution

Before commercial shipping, open the provider license page for the chosen asset. Unsplash API apps must follow Unsplash API guidelines including photographer attribution requirements for API usage. Prefer linking the photo page when attribution is required or appreciated.

### 6. Performance defaults

- Request the exact width/height the layout needs.
- Prefer WebP/AVIF when the consumer supports it (`https://picsum.photos/800/600.webp`, Placehold format suffixes).
- Placehold retina: append `@2x` / `@3x` on raster formats only.

## Common traps

| Trap | Better path |
|------|-------------|
| Emit `https://source.unsplash.com/...` | Explain deprecation (HTTP 503) and switch to Picsum or Unsplash API |
| Random Picsum URL in a multi-screen mock | Switch to `/id/` or `/seed/` |
| Treat placeholders as final brand photography | Mark as mock-only; upgrade to licensed stock or owned assets |
| Oversized downloads for a 320px card | Request the displayed size (or 2x max) |
| Paste real API keys into chat or git | Keep keys in host secret storage |

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| `picsum.photos` | dimensions, optional id/seed/flags | keyless photos |
| `placehold.co` | dimensions, colors, text, format | keyless placeholders |
| `placekeanu.com` | dimensions, optional flags | keyless Keanu placeholders |
| `api.unsplash.com` | Client-ID + query | official Unsplash search/random |
| `api.pexels.com` | API key + query | official Pexels search |
| `pixabay.com/api` | key + query | official Pixabay search |

Anonymous placeholder endpoints need no user account data. Official stock APIs send only the registered application credentials and search parameters you choose.

## Security and privacy

- Do not store provider credentials inside the skill package.
- Do not log or commit access keys, bearer tokens, or private photo downloads.
- Optional preference memory under `<state_root>/memory.md` stores only user-approved style notes and public URLs.
- Hotlinking is intentional for Unsplash API image URLs; still respect each provider's terms.

## Output shape

When fulfilling a request, return:

1. One primary ready-to-paste URL (or a small set if the user asked for N images)
2. Provider name and whether an API key is required
3. Consistency tip (`id` / `seed` / saved CDN URL) when relevant
4. License/attribution reminder for production use
