# Integration — Umami

Tracker embed, SPA behavior, and custom events. Prefer official collect-data / tracker docs when APIs drift.

## Tracking script

1. In Umami, edit the website → copy **Tracking code**.
2. Place the script in the document **`<head>`** (defer). Example shape:

```html
<script
  defer
  src="https://your-umami.example.com/script.js"
  data-website-id="YOUR-WEBSITE-ID"
></script>
```

3. `data-website-id` must match that website exactly — mismatches produce **silent zero data**.
4. Optional attributes (see Tracker configuration): `data-host-url`, `data-auto-track`, `data-auto-pageview`, `data-domains`, `data-tag`, `data-distinct-id`.

## SPA and frameworks

Official guidance: React, Next.js, Vue, Nuxt, Angular and similar SPAs work **out of the box**. The tracker watches `pushState` / `replaceState` / `popstate` and records client-side navigations automatically.

- **Do not** require manual `umami.track()` solely for normal SPA pageviews.
- Call `umami.track()` for pageviews only when auto pageviews were disabled (`data-auto-pageview="false"`) or you need a custom payload.
- Before calling tracker APIs from components, ensure `window.umami` exists (script may load after mount).

### Next.js

- App Router: put the script in the root layout `<head>`, **or** use `next/script`:

```tsx
import Script from 'next/script';

<Script
  src="https://your-umami.example.com/script.js"
  data-website-id="YOUR-WEBSITE-ID"
  strategy="afterInteractive"
/>
```

- There is **no** supported official npm package named `@umami/next` for this integration. Do not invent one.

### React (Vite / CRA)

Add the script tag to `index.html` `<head>`.

### Vue / Nuxt

- Nuxt: `nuxt.config` `app.head.script` entry with `src`, `defer`, and `data-website-id`.
- Plain Vue: `index.html` `<head>` like React.

## Custom events

Two supported styles:

1. **Data attributes:** `data-umami-event="Signup button"` plus optional `data-umami-event-*` properties (values stored as strings).
2. **JavaScript:** `umami.track('signup-button')` or `umami.track('signup-button', { plan: 'newsletter' })`.

Also available: `umami.identify(...)` for distinct IDs / session data (see tracker functions docs).

Event name length and event-data limits are defined in official Track events / Tracker functions pages — re-read those before citing numeric caps in answers.

## Ad blockers

Even privacy-first trackers get blocked. Prefer same-site proxy of `script.js` and the collect endpoint, custom script name, and/or `COLLECT_API_ENDPOINT` / `data-host-url` so requests stay on the first-party domain. See Bypass ad blockers.
