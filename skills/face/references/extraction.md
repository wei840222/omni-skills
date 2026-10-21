# Extraction and recovery

## Prefer HTML fetch over a browser

Gallery cards embed:

- `/face/...` detail paths
- `data-image-id`
- `https://images.generated.photos/...` preview URLs

Transparent variants are often present only inside the SSR `window.__NUXT__`
payload as image URL string pairs (preview, then transparent). Transparent CDN
paths commonly contain the base64 fragment `cmFuc3BhcmVud` (`transparent`).

## Extractor

```python
python3 - <<'PY'
import json
import re
from urllib.request import Request, urlopen

url = "https://generated.photos/faces/beautified/female/young-adult"
raw = urlopen(
    Request(url, headers={"User-Agent": "Mozilla/5.0"}),
    timeout=30,
).read().decode("utf-8", "replace")

cards = re.findall(
    r'href="(/face/[^"]+)".*?data-image-id="([^"]+)".*?src="(https://images\.generated\.photos[^"]+)"',
    raw,
    re.S,
)

payload_match = re.search(r"window\.__NUXT__=(.*?)</script>", raw, re.S)
transparent_by_preview = {}
if payload_match:
    payload = payload_match.group(1)
    raw_urls = re.findall(
        r'"((?:https:)?\\u002F\\u002Fimages\.generated\.photos[^"]+)"',
        payload,
    )
    decoded = []
    for item in raw_urls:
        value = item.encode("utf-8").decode("unicode_escape")
        if value.startswith("//"):
            value = "https:" + value
        decoded.append(value)
    index = 0
    while index + 1 < len(decoded):
        preview, candidate = decoded[index], decoded[index + 1]
        if "cmFuc3BhcmVud" in candidate:
            transparent_by_preview[preview] = candidate
            index += 2
        else:
            index += 1

for n, (detail, image_id, thumb) in enumerate(cards[:6], 1):
    print(
        json.dumps(
            {
                "n": n,
                "detail": "https://generated.photos" + detail,
                "image_id": image_id,
                "thumb": thumb,
                "transparent": transparent_by_preview.get(thumb),
            }
        )
    )
PY
```

## Detail page previews

After the user picks one option, open the detail URL if a larger preview is
needed. Pages expose `og:image` / `twitter:image`; verify the returned size
rather than assuming 512px.

## Rate limits and empty results

- HTTP 429 is common on anonymous gallery traffic. Wait and retry with backoff;
  tell the user when options could not be fetched.
- Never invent faces or mark a failed fetch as a passing test.
- If HTML structure changes and cards are empty, stop and report the extraction
  miss instead of guessing URLs.

## Applying a chosen face

Only after explicit approval:

1. Keep the detail URL as the durable reference.
2. Optionally write `<state_root>/chosen-face.md` with the detail URL, preview,
   transparent URL if any, and timestamp.
3. Offer to update host identity/avatar surfaces separately; do not write
   outside `<state_root>` without consent.
