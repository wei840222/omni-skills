# Stock Image Providers — Reference

## Keyless placeholder services

### Lorem Picsum

Random Unsplash-derived photos by size. Docs: https://picsum.photos/

```text
https://picsum.photos/800/600
https://picsum.photos/400
https://picsum.photos/id/237/800/600
https://picsum.photos/seed/picsum/800/600
https://picsum.photos/800/600?grayscale
https://picsum.photos/800/600?blur=2
https://picsum.photos/id/870/800/600?grayscale&blur=2
https://picsum.photos/800/600.webp
https://picsum.photos/800/600.jpg
https://picsum.photos/800/600?random=1
https://picsum.photos/v2/list
https://picsum.photos/v2/list?page=2&limit=100
https://picsum.photos/id/0/info
```

### Placehold.co

Customizable placeholders (default SVG). Site/docs: https://placehold.co/

```text
https://placehold.co/800x600
https://placehold.co/400
https://placehold.co/800x600/000000/ffffff
https://placehold.co/800x600/orange/white
https://placehold.co/800x600?text=Hello+World
https://placehold.co/400x300@2x.png
https://placehold.co/800x600.png
https://placehold.co/800x600.webp
https://placehold.co/800x600/transparent/black
```

Supported formats include SVG, PNG, JPEG, GIF, WebP, and AVIF. Max size documented on the site: 4000×4000.

### PlaceKeanu

```text
https://placekeanu.com/800/600
https://placekeanu.com/g/800/600
https://placekeanu.com/y/800/600
```

### DummyImage

Fallback dimension service when Placehold is unavailable: https://dummyimage.com/

```text
https://dummyimage.com/800x600/000/fff
```

---

## Stock photo APIs (free developer tier)

### Unsplash

- Developer entry: https://unsplash.com/developers
- API documentation: https://unsplash.com/documentation
- Demo mode: **50 requests/hour** until production approval
- Auth header: `Authorization: Client-ID <UNSPLASH_ACCESS_KEY>`
- Hotlink the image URLs returned by the API (Unsplash CDN), do not rehost as the default integration path
- Do **not** generate `https://source.unsplash.com/...` URLs (live checks return HTTP 503)

### Pexels

- API signup/docs hub: https://www.pexels.com/api/
- Send the API key in the `Authorization` header for search requests
- Use only with a user-supplied or host-stored key

Example shape:

```bash
curl -H "Authorization: <PEXELS_API_KEY>" \
  "https://api.pexels.com/v1/search?query=nature&per_page=10"
```

### Pixabay

- Docs: https://pixabay.com/api/docs/
- Default rate limit: **100 requests per 60 seconds** (key + IP; see response `X-RateLimit-*` headers)
- Endpoint: `GET https://pixabay.com/api/`

```bash
curl "https://pixabay.com/api/?key=<PIXABAY_API_KEY>&q=nature&image_type=photo"
```

---

## Specialized services

### Faces and avatars

| Service | URL | Notes |
|---------|-----|-------|
| DiceBear | https://api.dicebear.com | Seeded avatar SVG/PNG API |
| Boring Avatars | https://boringavatars.com | Abstract avatars |
| This Person Does Not Exist | https://thispersondoesnotexist.com | AI face page |
| UI Faces | https://uifaces.co | Face mockup directory |
| RoboHash | https://robohash.org | Hash-based robot/alien avatars |

```text
https://api.dicebear.com/7.x/avataaars/svg?seed=username
https://robohash.org/username.png
```

### Icons

| Service | URL |
|---------|-----|
| Iconify | https://iconify.design |
| Feather | https://feathericons.com |
| Heroicons | https://heroicons.com |
| Lucide | https://lucide.dev |

### Illustrations

| Service | URL |
|---------|-----|
| unDraw | https://undraw.co |
| Open Peeps | https://www.openpeeps.com |
| Humaaans | https://www.humaaans.com |
| Open Doodles | https://www.opendoodles.com |

---

## Background removal / optimization (optional)

| Service | Entry |
|---------|-------|
| Remove.bg API | https://www.remove.bg/api |
| ReSmush.it | http://api.resmush.it/ws.php |

Use only with explicit user authorization; these call third-party processors.
