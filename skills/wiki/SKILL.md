---
name: wiki
description: >
  Structure, write, cross-link, and maintain wiki pages people can navigate
  without prior context. Use when creating or auditing a wiki, designing page
  templates and Getting Started maps, fixing broken internal links or redirects
  after renames, organizing categories/tags, or refreshing stale content. Prefer
  `documentation` for product/README/API doc systems (Diátaxis), `wiki-js` for
  Wiki.js deploy/config traps, `pkm` for personal atomic-note knowledge bases,
  `notes` for capture into note apps, and `markdown` for syntax/parser issues.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📚"}'
  related-skills: '{"documentation":"Product/README/API documentation systems and Diátaxis structure rather than wiki page craft.","wiki-js":"Wiki.js deployment, editor, permission, and sync traps.","pkm":"Personal atomic-note knowledge bases where the link graph is the product.","notes":"Capture and retrieval across note apps rather than wiki information architecture.","markdown":"Markdown syntax and parser compatibility under wiki content."}'
---

# Wiki

Build and maintain **navigable wikis**: focused pages, consistent templates,
aggressive internal linking, redirects on rename, and freshness signals.
This skill is **stateless** — it does not store wiki content, credentials, or
local config.

## When to use

- Creating a new wiki or Getting Started / map-of-content page
- Drafting or rewriting a page with title, one-sentence summary, and last-updated date
- Cross-linking concepts, adding categories/tags, or repairing broken internal links
- Renaming pages with redirects so existing links keep working
- Auditing stale, orphaned, or over-long pages (>~500 words → split)
- Prefer `documentation` for product docs architecture (tutorials / how-to / reference / explanation)
- Prefer `wiki-js` when the ask is Wiki.js site URL, editor, permissions, or Git sync
- Prefer `pkm` for personal Zettelkasten / atomic-note growth
- Prefer `notes` for meeting/decision capture into note apps
- Prefer `markdown` when the failure is fence/table/parser syntax

## Quick reference

| Situation | Play | Depth |
|-----------|------|-------|
| New wiki or empty structure | Create Getting Started map + page template first | `references/structure.md` |
| New page request | Title + one-line summary + last-updated + standard sections | `references/structure.md` |
| Procedure content | Numbered steps; zero assumed context; examples | `references/guidelines.md` |
| Concept mentioned elsewhere | Link every mention; keep link graph dense | `references/guidelines.md`, `references/domain.md` |
| Rename | Add redirect / stub at old path before deleting | `references/domain.md` |
| Stale or conflicting facts | Grep all mentions; update every hit; mark `[needs verification]` when unsure | `references/guidelines.md` |
| Orphans / broken links | Periodic cleanup pass; fix or remove | `references/guidelines.md` |
| Platform-specific wiki (GitHub / MediaWiki / Wiki.js) | Apply host link/redirect rules from sources | `references/sources.md`, `wiki-js` skill |

## Page structure (must-have)

Every page includes:

1. Clear title (matches the topic)
2. One-sentence summary under the title
3. Last-updated date (or equivalent freshness signal)
4. Focused body — one topic; split past ~500 words
5. Links to related pages

The wiki also needs a **Getting Started** (or equivalent map) page that lists the major sections and entry points.

## Writing and maintenance

Read [Wiki Guidelines](references/guidelines.md) for writing, linking, and maintenance rules. Read [Structure](references/structure.md) for templates and Getting Started maps. Read [Domain rules](references/domain.md) for redirects, categories, and host constraints. Read [Sources](references/sources.md) before asserting platform-specific behavior.

## Quality control

- Review new pages for template compliance and link accuracy
- Periodic cleanup of orphaned pages and broken internal links
- Prefer version control for history and revert
- Keep a changelog or "recently updated" surface for team visibility
- Never invent undocumented host behavior — check `references/sources.md`

## Success metrics

- Users find the answer in fewer than three clicks from Getting Started
- Each page answers its topic without requiring prior wiki knowledge
- Freshness signals and redirects keep the graph honest after renames
