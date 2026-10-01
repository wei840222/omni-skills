# Setup — Stock Images

Read this on first use, then execute. Placeholder services work immediately; stock APIs need a free developer key only when the user wants subject search beyond keyless providers.

## Attitude

Act like a resource librarian: return a usable URL quickly, then refine provider choice from intent.

## Workflow

1. **Clarify intent** — mockup placeholder, stable prototype asset, production stock, avatar/icon, or broken Unsplash Source repair.
2. **Keyless first** — Lorem Picsum, Placehold.co, or PlaceKeanu when no subject API is required.
3. **Stable layout** — switch to Picsum `/id/` or `/seed/` when the same image must survive reloads.
4. **Subject search** — guide the user to Unsplash / Pexels / Pixabay developer signup, then call the official API with host-provided secrets.
5. **Hand off** — give paste-ready URLs; load `references/providers.md` for full catalogs and `references/sources.md` for licenses or deprecation evidence.

## Common scenarios

### "I need a placeholder image"

```text
https://picsum.photos/800/600
https://placehold.co/800x600/EEE/31343C?text=Hero
```

### "I need consistent images for a mockup"

```text
https://picsum.photos/id/237/400/300
https://picsum.photos/id/238/400/300
https://picsum.photos/id/239/400/300
```

or seed-based:

```text
https://picsum.photos/seed/hero/1200/630
https://picsum.photos/seed/card-a/600/400
https://picsum.photos/seed/card-b/600/400
```

### "I need professional stock photos for production"

1. Confirm commercial license needs.
2. Use Unsplash, Pexels, or Pixabay **API** (not `source.unsplash.com`).
3. Return the provider image page + embeddable image URL from the API payload.
4. Include attribution guidance required by that provider's API rules.

### "source.unsplash.com links are broken"

State that the live `source.unsplash.com` endpoint currently returns **HTTP 503**, then offer Picsum/Placehold immediately and Unsplash API if a searchable Unsplash photo is still required.

## Optional memory

Only if the user wants remembered preferences, resolve `<state_root>` per `SKILL.md` and create `<state_root>/memory.md` from `assets/memory-template.md`.
