---
name: inspiration
description: >
  Retrieve visual design, UI pattern, landing-page, and AI-art inspiration from
  curated galleries and screenshot libraries. Use when the user needs
  references for UI/UX, mobile flows, landing pages, AI image styles/prompts,
  colors, typography, icons, or motion. Prefer `design` for quantified visual
  critique, `colors` for WCAG palettes/tokens, `ui` for component patterns,
  `image-generation` for running generation workflows, and `frontend` for
  implementation.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"✨"}'
  related-skills: '{"colors":"Build accessible palettes and tokens after inspiration picks a visual direction.","design":"Apply quantified hierarchy, spacing, and critique rules to a chosen reference.","frontend":"Implement approved visual direction in interface code.","image-generation":"Run text-to-image or edit workflows once style references are chosen.","ui":"Map inspiration screens into reusable component and interaction patterns."}'
---

## State location

Inspiration preferences may exist in `<workspace>/inspiration/`, `<workspace>/memory/inspiration/`, or `~/inspiration/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/inspiration/`, `<workspace>/memory/inspiration/`, `~/inspiration/`.
3. If several candidate directories exist, use only the highest-precedence one and report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create `<workspace>/inspiration/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/inspiration/` only; otherwise ask for a state root before creating data.

Use the selected `<state_root>` for every state operation in this invocation. Create or update `<state_root>/preferences.md` only when the user wants preference continuity. Legacy `~/Clawic/data/inspiration/` is a migration source only—keep it out of active lookup; move only with explicit user consent (copy, validate, cutover).

This skill is otherwise a knowledge guide: gallery browsing does not require state.

## Setup

On first use, or when the user asks how to narrow references, read `references/setup.md`.

## When to use

Use for **visual reference retrieval**: UI/UX screens and flows, landing pages, AI art galleries/prompts, illustration/mood boards, color/type/icon/motion inspiration catalogs.

Do **not** use as the sole skill for quantified design critique (`design`), WCAG token systems (`colors`), component-library conventions (`ui`), running image models (`image-generation`), or shipping frontend code (`frontend`).

Ask only for the next missing filter that changes the source set: platform (web/mobile/desktop), style, purpose (production vs concept), and category.

## Resource loading

| Need | Load |
|------|------|
| Clarifying questions and matching attitude | `references/setup.md` |
| Full 100+ source directory by category | `references/sources.md` |
| AI model/gallery deep dive | `references/ai-galleries.md` |
| Mobile screenshot and flow research | `references/mobile-screenshots.md` |
| Optional preference template | `assets/data-templates.md` |

Load one deep reference when the request needs that depth. Prefer actively maintained galleries over stale showcases.

## Core rules

1. **Match source to need** — UI patterns → Mobbin / Screenlane / Page Flows; visual design → Dribbble / Behance / Awwwards / Godly; AI art → Midjourney Showcase / Civitai / PromptHero / Lexica; landing pages → Landingfolio / Lapa Ninja / SaaS Pages.
2. **Give actionable links** — Return direct URLs and one sentence on why each source fits this request.
3. **Filter with context** — Collect platform, style, and purpose before dumping a long list.
4. **Go deep when needed** — For AI prompts, mobile flows, or niche industries, load the matching reference file instead of expanding every table in-chat.
5. **Prefer live galleries** — Prioritize Mobbin, Godly, Awwwards, Civitai, PromptHero, and similar actively updated catalogs when freshness matters.
6. **Treat aspirational boards carefully** — Dribbble/Behance are strong for concepts; call out when a reference is aspirational rather than production-ready.

## Quick start — top sources

### UI/UX

| Source | Best for | URL |
|--------|----------|-----|
| Mobbin | Mobile screenshots and flows | https://mobbin.com |
| Screenlane | Mobile UI patterns | https://screenlane.com |
| Page Flows | User-flow recordings | https://pageflows.com |
| Collect UI | Curated UI components | https://collectui.com |
| Godly | Modern web design | https://godly.website |

### Landing pages and web

| Source | Best for | URL |
|--------|----------|-----|
| Landingfolio | SaaS landing pages | https://landingfolio.com |
| Lapa Ninja | Landing page gallery | https://lapa.ninja |
| SaaS Pages | SaaS-specific layouts | https://saaspages.xyz |
| Awwwards | Award-winning sites | https://awwwards.com |
| Site Inspire | Clean web design | https://siteinspire.com |

### AI-generated art

| Source | Best for | URL |
|--------|----------|-----|
| Midjourney Showcase | Community MJ picks | https://midjourney.com/showcase |
| Civitai | SD models + images | https://civitai.com |
| PromptHero | Prompts + results | https://prompthero.com |
| Lexica | SD image search | https://lexica.art |
| OpenArt | Multi-model gallery | https://openart.ai |
| Krea | AI design inspiration | https://krea.ai |

### Visual design, color, type, icons, motion

| Source | Best for | URL |
|--------|----------|-----|
| Dribbble | Designer portfolios | https://dribbble.com |
| Behance | Creative projects | https://behance.net |
| Coolors | Palette generator | https://coolors.co |
| Color Hunt | Curated palettes | https://colorhunt.co |
| Typewolf | Font recommendations | https://typewolf.com |
| Fonts In Use | Real-world type | https://fontsinuse.com |
| Lucide / Heroicons | Icon sets | https://lucide.dev / https://heroicons.com |
| unDraw / Storyset | Illustrations | https://undraw.co / https://storyset.com |
| Lottie Files | Motion JSON | https://lottiefiles.com |
| UI Movement | UI animation refs | https://uimovement.com |

For the complete catalog, load `references/sources.md`.

## Prefer / watch-outs

- Prefer clarifying platform/style/purpose over answering "show me inspiration" with a generic dump.
- Prefer production-oriented libraries (Mobbin, Page Flows) when the user is shipping UI; keep Dribbble/Behance for concept exploration.
- Prefer AI-specific galleries when the user needs prompts, models, or style refs for generation.
- Watch for stale galleries; re-check URLs from `references/sources.md` when a site looks abandoned.
- Watch for paywalled deep archives (Mobbin, Page Flows, UI Sources); say when a free tier may be limited.

## Optional preference continuity

When the user wants remembered filters, copy `assets/data-templates.md` to `<state_root>/preferences.md` and update it after useful sessions.
