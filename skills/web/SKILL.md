---
name: web
description: >
  Build, debug, and deploy general web work across HTML, CSS, JavaScript, React/Next.js,
  Core Web Vitals, SEO basics, accessibility, and production hosting. Use when the user
  asks to fix a site bug, choose a stack, ship to Vercel/Netlify/Cloudflare/VPS, tune LCP
  or CLS or INP, stop CORS or mixed-content failures, or harden forms and env exposure.
  Not for pure ranking campaigns (`seo`), stylesheet-only debugging (`css`), deep markup
  ARIA (`html`), React UI polish alone (`frontend`/`react`/`nextjs`), or image pipelines (`image`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"css":"Cascade, layout bugs, and stylesheet architecture beyond quick web traps.","deploy":"Host-specific deploy runbooks when the platform is already chosen.","frontend":"React/Next/Tailwind UI systems and component polish.","html":"Deep semantic markup, forms, dialogs, and sanitization details.","icons":"Accessible SVG icon patterns and touch targets.","image":"Format choice, compression, and responsive image delivery.","javascript":"Language-only JS patterns outside DOM/web delivery context.","nextjs":"App Router, caching, and Next-specific deployment depth.","react":"Component model and hooks beyond the short web traps list.","seo":"Organic ranking strategy and Search Console recovery beyond launch tags.","typography":"Measure, leading, and type scale for readable pages.","website":"Content-site IA, launch checklist, and static-site CWV coaching."}'
---

## When to load

Load this skill for **general web development** that spans markup, styling, client JS, frameworks, performance, and deploy:

- fix HTML/CSS/JS bugs that block a page from shipping
- choose or justify a stack (static HTML, Astro, Next.js, Remix, Vite SPA)
- deploy or debug Vercel / Netlify / Cloudflare Pages / Railway / Render / VPS
- Core Web Vitals coaching (LCP, CLS, **INP** — not FID)
- CORS, mixed content, env-var leakage, form submit reloads
- lightweight SEO/a11y launch hygiene before handing off specialists

Route away when the ask is mainly:

- ranking recovery, keyword research, schema campaigns → `seo`
- cascade/specificity deep dives only → `css`
- ARIA widgets, dialogs, complex forms only → `html`
- React/Next UI system polish → `frontend` / `react` / `nextjs`
- image encode/compress pipelines → `image`
- pure language JS without DOM/deploy → `javascript`
- brochure/content site launch checklist only → `website`

## Operating loop

1. **Clarify surface** — static page, multi-page site, SPA, or full-stack app; keep advice proportional.
2. **Preserve working paths** — progressive enhancement; core content should work without JS when feasible.
3. **Load depth on demand** — open only the matching `references/` file from the table below.
4. **Ship measurable fixes** — name the failure (metric, console error, a11y gap), the change, and how to re-check.
5. **Hand off specialists** — do not recreate full `seo`/`css`/`frontend` curricula here.

## Quick reference

| Need | Load |
|------|------|
| Semantic HTML, CSS traps, viewport, responsive | `references/html-css.md` |
| Type coercion, async, DOM safety, forms | `references/javascript.md` |
| React hooks traps, Next.js App Router, SPA hydration | `references/frameworks.md` |
| Vercel/Netlify/CF/VPS, DNS, env, CORS, HTTPS | `references/deploy.md` |
| LCP/CLS/INP, images, SEO tags, a11y checklist | `references/performance.md` |
| Gate 6 source URLs | `references/sources.md` |

## Core rules (always on)

1. **DOCTYPE** — Missing `<!DOCTYPE html>` triggers quirks mode; layouts break unpredictably.
2. **Specificity over `!important`** — Prefer fixing cascade; `.class` beats element selectors regardless of order.
3. **`===` not `==`** — Type coercion makes `"0" == false` true.
4. **Await correctly** — `forEach` does not await; use `for...of` or `Promise.all`.
5. **CORS is server-side** — Browsers enforce it; configure `Access-Control-Allow-Origin` (or same-origin proxy). No pure client-side fix.
6. **Viewport meta** — Require `<meta name="viewport" content="width=device-width, initial-scale=1">`.
7. **Forms** — Call `event.preventDefault()` on submit handlers when staying on-page.
8. **Image dimensions** — Set `width`/`height` or CSS `aspect-ratio` to protect CLS.
9. **HTTPS** — Mixed content (HTTP assets on HTTPS pages) is blocked; use HTTPS or scheme-relative URLs.
10. **Env exposure** — `NEXT_PUBLIC_*` (and similar public prefixes) ship to the client; never prefix secrets.
11. **INP not FID** — Interaction responsiveness uses **INP**; treat FID guidance as obsolete.
12. **Buttons vs links** — `<button>` for actions; `<a href>` for navigation.

## Framework decision tree

- **Static content, fast builds** → Astro or plain HTML
- **Blog/docs with MDX** → Astro or Next.js App Router
- **Interactive app with auth** → Next.js or Remix
- **Full SSR/ISR control** → Next.js
- **Simple SPA, weak SEO need** → Vite + React/Vue

## Common requests

| Ask | First move |
|-----|------------|
| Make it responsive | Mobile-first CSS; test 320 / 768 / 1024; verify viewport meta |
| Deploy to production | `references/deploy.md` — match platform timeouts, build cmd, output dir, env |
| Fix CORS | Server headers or same-origin proxy; never “disable CORS in browser” as a product fix |
| Improve performance | Lighthouse clean profile; prioritize LCP image, CLS space, INP long tasks |
| Add SEO basics | Unique title/description, semantic headings, canonical, OG, sitemap/robots — deep ranking → `seo` |

## Progressive disclosure

Keep this file as the always-on entry. Load reference files only when the task needs depth beyond the rules above. Do not invent a filesystem state root for this package — it is **stateless** knowledge.
