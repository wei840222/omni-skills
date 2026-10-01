# Research sources (Gate 6)

Primary URLs used while refactoring `web`. Prefer these over memory when citing metrics, security rules, or platform behavior. Re-verify vendor timeouts and plan limits at use time — they change.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification
- Optional directories — https://agentskills.io/specification#optional-directories
- Progressive disclosure — https://agentskills.io/specification#progressive-disclosure
- File references — https://agentskills.io/specification#file-references
- skills-ref validator package — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Core Web Vitals and performance

- web.dev — Core Web Vitals overview (LCP, INP, CLS) — https://web.dev/articles/vitals
- web.dev — Optimize LCP — https://web.dev/articles/optimize-lcp
- web.dev — Optimize CLS — https://web.dev/articles/optimize-cls
- web.dev — Optimize INP — https://web.dev/articles/optimize-inp
- web.dev — FID is deprecated in favor of INP (see vitals article and Chrome documentation trail)

## HTML / CSS / JS platform

- HTML Living Standard — https://html.spec.whatwg.org/
- MDN — Viewport meta element — https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_element
- MDN — Link type `noopener` — https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener
- MDN — CSP / XSS orientation via `innerHTML` guidance — https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML
- MDN — CORS overview — https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- MDN — Mixed content — https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content

## Accessibility

- W3C WAI — WCAG 2.2 — https://www.w3.org/TR/WCAG22/
- W3C WAI — Images tutorial — https://www.w3.org/WAI/tutorials/images/
- WebAIM — Contrast and color accessibility — https://webaim.org/articles/contrast/

## Frameworks (verify current docs when advising)

- React docs — You Might Not Need an Effect / hooks rules — https://react.dev/learn/you-might-not-need-an-effect
- Next.js docs — App Router — https://nextjs.org/docs/app
- Next.js docs — Environment variables — https://nextjs.org/docs/app/building-your-application/configuring/environment-variables

## Hosting (plan limits change — re-check before quoting numbers)

- Vercel documentation hub — https://vercel.com/docs
- Netlify documentation hub — https://docs.netlify.com/
- Cloudflare Pages docs — https://developers.cloudflare.com/pages/

## Obsolete knowledge corrected

- **FID as a current Core Web Vital** — replaced with **INP** per web.dev vitals guidance.
- **Clawic packaging** — removed `homepage: clawic.com`, `_meta.json`, nested `metadata.clawdbot`, top-level `slug`/`version`.
- **Hard-coded host timeouts as eternal facts** — kept comparative gotchas; instruct agents to verify live vendor docs before citing exact seconds.
- **Root-level reference files** — moved under `references/` per progressive disclosure.
