---
name: html
description: >
  Write, review, and fix HTML markup: semantic structure, forms, accessibility,
  document head/metadata, media, embeds, tables, interactive widgets, HTML email,
  parsing recovery, and untrusted HTML sanitization. Use when a field never
  submits, a label does nothing, autofill picks the wrong box, validation fires
  early, a screen reader reads a filename or nothing, focus escapes a modal, the
  page jumps as images load, quirks mode or mojibake appear, link previews or
  favicons are missing, dialog/details/popover/template misbehave, iframes stay
  blank, Outlook email collapses, or user HTML must render without XSS. Prefer
  `css` for layout/styling, `javascript` for DOM/events, `seo` for ranking
  strategy, `markdown` for Markdown syntax, and `forms` for product-level form
  design beyond markup bugs.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"css":"Layout, cascade, theming, and visual styling once markup structure is correct.","javascript":"DOM scripting, events, and behavior an ARIA pattern requires beyond native elements.","forms":"Product-level form design, multi-step flows, and platform choice when the issue is not HTML structure.","seo":"Search strategy, indexing, and ranking work beyond semantic markup and head tags.","svg":"Inline vector graphics, viewBox, and icon systems embedded in markup.","markdown":"Markdown syntax and conversion when the deliverable is not HTML markup.","web":"General web build, deploy, and CWV engineering under the markup layer."}'
---

# HTML

HTML declares what things *are*. Prefer the native element whose meaning matches; the browser then supplies keyboard behavior, focus order, accessible name, and form semantics. Name the element, the attribute, and the line that changes. Prefer a surgical fix over a rewritten page when a few attributes are wrong. Start from defaults immediately and state assumptions in one clause when they matter. Preference precedence: `config.yaml` → shared profile → Configuration table defaults.

## State location

HTML state may exist in `<workspace>/html/`, `<workspace>/memory/html/`, or `~/html/`. Shared domains may exist in `<workspace>/domains/`, `<workspace>/memory/domains/`, or `~/domains/`. Shared projects may exist in `<workspace>/projects/`, `<workspace>/memory/projects/`, or `~/projects/`. Shared profile may exist as `<workspace>/profile.yaml`, `<workspace>/memory/profile.yaml`, or `~/profile.yaml`. `<workspace>` is the host/runtime workspace root (resolve from host/runtime config, not from the shell cwd alone).

Before any state read or write, resolve `<state_root>` once:

1. Use an explicitly configured path from the user or host when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/html/`, `<workspace>/memory/html/`, `~/html/`.
3. When multiple candidates exist, use only the highest-precedence one, tell the user duplicates were found, and leave the others unchanged.
4. When none exists and durable notes must be saved, propose `<workspace>/html/` (or an explicit path if no workspace is available) and obtain named consent before creating it.
5. Legacy paths `~/Clawic/data/html/`, `~/Clawic/data/domains/`, `~/Clawic/data/projects/`, and `~/Clawic/profile.yaml` are migration sources only. Copy into the selected layout only after the user names the destination; leave legacy trees untouched unless the user asks to remove them.

Resolve shared domains, projects, and profile the same way under their candidate lists above.

Use the selected `<state_root>` for every html-owned path. Keep skill resources under `references/` and `assets/` only. Write only resolved concrete paths to disk; keep `<state_root>` as a documentation placeholder.

### State tree (after resolution)

```text
<state_root>/
├── config.yaml          # declared preferences (optional until first save)
├── memory.md            # observed state, ## Boxes index, ## Due
└── artifacts/           # optional durable markup patterns / boilerplates
```

Shared (outside html root, independently resolved):

- `<domains_root>/domains.md` — hostname rows (canonical host, www-vs-apex, locale→hostname); identity = hostname
- `<projects_root>/<project>.md` — markup notes for a tracked project
- `<profile_path>` — shared locale/language defaults

Create optional children only when needed. Credentials stay outside state roots; store pointers only (`env:…`, `keychain:…`, `1password:…`, `file:…`).

## Session bootstrap

1. Resolve `<state_root>` (and domains/projects/profile roots when those boxes are needed).
2. Read `<state_root>/config.yaml` and `<state_root>/memory.md` when they exist. Open any path listed under `## Boxes` when its condition applies; ignore paths outside `<state_root>/`.
3. Before writing a canonical URL, `hreflang` set, or absolute `og:`/`twitter:` URL, read `<domains_root>/domains.md`.
4. When markup belongs to a tracked project, read `<projects_root>/<project>.md`.
5. Preference precedence: `config.yaml` → shared profile → Configuration table defaults.
6. If none of the files exist, work from defaults without narrating the gap.

**Write before the session ends** when the turn produced something durable: a page or template mapped; landmark/LCP/`lang` decisions; a rendering quirk that cost effort (Outlook collapse, Safari gap, screen-reader announcement, CMS stripping an attribute); an accessibility or validation pass and what it found; a canonical host or locale→hostname map; a reusable `<head>` boilerplate, accessible component pattern, email template, sanitizer allowlist, or native-vs-library decision. Load `references/memory.md` for destinations, formats, and thresholds; use `assets/memory-template.md` only as blank shapes to copy.

In a shared box, update or remove only rows this skill wrote (match the box identity key). Rows another skill wrote stay read-only. Name each write and deletion in one line as it happens. Record only verified registrar or expiry data in domains rows; preserve headers written by other skills.

## Progressive disclosure

| Situation | Load |
|---|---|
| State destinations, write thresholds, shared-box rules | `references/memory.md` |
| Blank templates for memory/config/domains boxes | `assets/memory-template.md` |
| Spec/standards sources and freshness notes | `references/sources.md` |

## When To Use

- Writing or reviewing markup: page skeletons, `<head>` blocks, semantic structure, forms, tables, media, embeds
- Debugging rendering and behavior that CSS and JS cannot explain: quirks mode, mojibake, foster-parented content, a control that never submits, an element that ignores an attribute
- Accessibility work at the markup layer: accessible names, landmarks, heading order, focus and modality, live regions, keyboard reachability — and deciding when a native element beats an ARIA pattern
- Metadata: canonical, favicons, manifest, Open Graph, Twitter cards, JSON-LD, `lang`/`dir`/`hreflang`
- Loading behavior owned by markup: `defer`/`async`/`type=module`, `preload`/`preconnect`, `loading`, `fetchpriority`, and the image attributes that decide layout shift
- HTML email, where almost none of the above applies and a 1998 table layout is the correct answer
- Rendering untrusted or user-generated HTML without an XSS
- Not for styling and layout (`css`), DOM scripting and event handling (`javascript`), search strategy (`seo`), or Markdown syntax (`markdown`) — this covers the markup those four sit on

## Quick Reference

| Situation | Play | Depth |
|---|---|---|
| Starting a page, or the `<head>` is a mess | Canonical head order: charset → viewport → title → the rest; charset inside the first 1024 bytes | `head` |
| Link preview blank or wrong on Slack, iMessage, WhatsApp, X | `og:image` must be absolute and crawlable; check `og:type`, size, and cache | `head` |
| Favicon or install prompt missing | The three-file floor plus the manifest, and why one `.ico` is no longer enough | `head` |
| Choosing between `<div>` and a real element | Semantic map by meaning; landmarks; heading order is a tree, not a font size | `semantics` |
| Field never submits, or submits under the wrong key | `name` submits, `id` labels — plus `disabled`, `form=`, and unchecked checkbox rules | `forms` |
| Autofill wrong, keyboard wrong, validation fires too early | Explicit `autocomplete` tokens, `inputmode`, `:user-invalid` | `forms` |
| Screen reader reads a filename, "button", or nothing | Accessible name precedence; `alt` decision table | `accessibility` |
| Focus escapes a modal, or a hidden panel is still tabbable | `showModal()`, `inert`, and the four ways to hide something | `accessibility` |
| Layout jumps while images load, or the hero loads last | `width`/`height` always; `fetchpriority="high"` on the LCP image; keep the LCP image eager | `media` |
| Which image format, `srcset`, or art direction | `sizes` correctness, `<picture>` order, AVIF/WebP fallback | `media` |
| Embed blank, or a video won't play inline | `sandbox`/`allow` combinations, frame-ancestors, `playsinline`, captions | `media` |
| Complex data table unreadable to assistive tech | `scope` while it works, `headers`+`id` when it does not; caption over heading | `tables` |
| Modal, accordion, tooltip, tabs, combobox, toast | Native element first — the element-versus-pattern table with the cost of each | `interactive` |
| Web component, slot, or SSR markup behaves oddly | Upgrade timing, slot fallback, form participation, declarative shadow DOM | `templates` |
| Email renders fine everywhere except Outlook | Word engine: tables, `<style>` limits, VML, 600px, no flex | `email` |
| Page is slow before any JS runs | Blocking scripts, hint budget, `content-visibility`, connection cost | `performance` |
| Rendering user-generated or pasted HTML | Sanitize with an allowlist, escape by context, `sandbox` for isolation | `security` |
| Half the page turns italic, or content jumps out of a table | Parser recovery: unclosed tags, nesting rules, foster parenting | `parsing` |
| Accents mojibake, RTL mirroring, or a mixed-language page | Charset, `lang`, `dir`, `bdi`, `translate`, `hreflang` | `internationalization` |
| "Is this page correct?" before shipping | Conformance vs browser tolerance; what automated tools cannot see | `auditing` |
| Anything else HTML | Name what the element *means*, check the element's content model, then check what the parser actually built (`document.body.innerHTML` after load ≠ your source) | — |

Coverage map: `head` document head and metadata · `semantics` element choice and landmarks · `forms` controls, submission, validation · `accessibility` names, focus, ARIA · `media` images, video, iframes · `tables` data tables · `interactive` native widgets · `templates` components and shadow DOM · `email` HTML email · `performance` loading and hints · `security` XSS and isolation · `parsing` parser rules and recovery · `internationalization` language, direction, encoding · `auditing` validation and review.

## Core Rules

1. **Element before ARIA.** A native element ships keyboard behavior, focus, state and a name; an ARIA role ships a promise you must then implement in JS and keep implementing. Adding `role="button"` to a `<div>` obliges you to add `tabindex="0"`, Enter *and* Space handlers, `:focus-visible` styling, and a disabled state — four things `<button>` already does. Reach for ARIA only when no element expresses the pattern (tabs, combobox, treegrid) — the list is short and it is in `interactive`.
2. **`name` submits, `id` labels, and both are silent when wrong.** A control without `name` is never sent; a `label[for]` pointing at a missing or duplicated `id` clicks nothing and names nothing. Duplicate `id` is the single most common cause of "the label works on the first one only": every `for`, `aria-labelledby`, `aria-controls` and `#fragment` resolves to the first match and silently ignores the rest.
3. **Reserve space at parse time.** Put `width` and `height` attributes on every `<img>`, `<video>` and `<iframe>` with a known ratio: the browser computes `aspect-ratio: width / height` before the bytes arrive, and the intrinsic values do not have to match the rendered size — only the ratio does. Budget: CLS ≤ 0.1 is the Core Web Vitals "good" threshold, 0.1–0.25 needs improvement, and one unsized above-the-fold image usually spends the whole budget by itself.
4. **Every control has a visible label, and the placeholder is not it.** Placeholder text disappears on first keystroke, is exempt from contrast requirements in most implementations, and is invisible to anyone returning to a half-filled form. `<label>` wrapping or `for`/`id`; `aria-label` only when the visual design genuinely has no text (an icon-only search button).
5. **Alt text is a function of the image's job, not of the image.** Informative → describe the information, not the picture. Functional (inside a link or button) → describe the *destination or action*. Decorative → `alt=""`, which is not the same as omitting `alt`: a missing `alt` makes assistive tech read the file name. Text in an image → reproduce the text. Complex chart → short `alt` plus the data in the page (`media`).
6. **Order the head by what the parser needs first.** `<meta charset>` must appear within the first 1024 bytes or the parser may restart the document with the wrong encoding; `<meta name="viewport">` before any layout-affecting resource; `<title>` early because it is the first thing a preview or a tab shows. Everything else — hints, styles, scripts — after those three (`head`).
7. **Scripts: `defer` by default, `async` only for genuinely independent code.** A bare `<script src>` in `<head>` blocks parsing at that line. `defer` keeps document order and runs before `DOMContentLoaded`; `async` runs whenever it lands, so two `async` scripts that depend on each other fail intermittently and only on slow networks. `type="module"` is deferred by definition — adding `defer` to it is a no-op, adding `async` to it is a real change.
8. **Escape by context, and let a parser do the sanitizing.** HTML text, attribute values, URLs, JS string literals and CSS are five different escaping contexts; one `escapeHtml()` used for all five is an XSS. For rich user HTML, allowlist with a real sanitizer — a blocklist of `<script>` never survives `<img onerror>`, `javascript:` URLs, or SVG event attributes (`security`).
9. **Validate the parsed DOM, not your source.** Nesting mistakes are corrected silently and asymmetrically: a `<div>` inside `<p>` closes the paragraph and yields two, and anything not in a table's content model is *foster-parented* out and rendered before the table. When rendering disagrees with the source, compare against what the parser built (`parsing`).

## Failure Signatures

Decode rule: the layer that misbehaves names the cause. Wrong *content* in the right place is a data problem; right content in the *wrong place* is a parser problem; nothing at all is usually a name, an id, or an origin.

| Signature | Most likely cause | First move |
|---|---|---|
| A field is missing from the submitted payload | No `name`, or the control is `disabled` | `disabled` omits the value entirely; `readonly` submits it (`forms`) |
| Clicking the label does nothing | `for` points at a missing id, or the id is duplicated | Search the document for the id; wrap the input in the label instead (Rule 2) |
| Checkbox missing from the payload when unchecked | Unchecked boxes are never submitted — by design | Paired `<input type="hidden">` before it, same `name` (`forms`) |
| Screen reader announces a file name | `alt` is absent, not empty | `alt=""` for decorative; a description for informative (Rule 5) |
| Screen reader announces "button" with no name | Icon-only control with no text and no `aria-label` | Accessible name precedence in `accessibility` |
| Text appears *above* a table it was written inside | Foster parenting: the content is not in the table content model | Only `caption`, `colgroup`, `thead`, `tbody`, `tfoot`, `tr` may be table children (`parsing`) |
| Half the document is italic, bold, or inside a link | One unclosed inline element; the parser's active-formatting reconstruction re-opens it | Validate; find the first unclosed tag before the affected region (`parsing`) |
| Page ignores the viewport / renders tiny on mobile | Missing `<meta name="viewport">` | `width=device-width, initial-scale=1` (`head`) |
| Accented characters render as `Ã©` | Charset declared late, or the HTTP header disagrees with the meta | Meta charset in the first 1024 bytes, UTF-8 everywhere (`internationalization`) |
| Layout behaves like it is 1998; box model wrong | Quirks mode from a missing or malformed doctype | `<!DOCTYPE html>` as the literal first bytes (`parsing`) |
| Link preview blank on Slack/X/iMessage | `og:image` relative, behind auth, or the page blocks the crawler | Absolute URL, public, ≥1200×630 (`head`) |
| Query string breaks after `&` (`?a=1&copy=2` shows ©) | Named character reference decoded in text content | In attributes it is safe; in text write `&amp;` (`parsing`) |
| `<dialog>` does not block the background | Opened with `show()` instead of `showModal()` | Only `showModal()` creates the top layer and the inert backdrop (`interactive`) |
| Focus tabs into a visually hidden panel | Hidden with opacity/transform, or `aria-hidden` only | `hidden`, `display:none`, or `inert` — the four hiding mechanisms differ (`accessibility`) |
| Iframe blank, or console mentions frame-ancestors | Site refuses framing, or `sandbox` withholds a capability | Check `X-Frame-Options`/CSP first, then the `sandbox` token list (`media`) |
| Autofill fills the wrong field | No explicit `autocomplete`; the browser guessed from the name | Use the spec token (`address-line1`, `cc-exp`, `one-time-code`) (`forms`) |
| Email fine in Gmail, collapsed in Outlook desktop | Word rendering engine: no flex, no grid, no `position` | Nested tables and inline styles (`email`) |
| Email cut off with "[Message clipped]" | Gmail clips a message past ~102 KB | Trim comments and duplicated inline CSS (`email`) |
| Anything else | Reduce to the smallest document that still shows it, then re-add one attribute at a time; the attribute that brings it back names the subsystem | `auditing` |

## Implicit Defaults

Every one of these is a default that has produced a bug report against the application code.

| Thing | Default | Why it bites |
|---|---|---|
| `<button>` inside a form | `type="submit"` | A "Cancel" or "Show password" button submits the form; write `type="button"` |
| `<form>` method | `GET` | Credentials and PII land in the URL, the history, and the referrer |
| `<form>` enctype with a file input | `application/x-www-form-urlencoded` | Only the file *name* is sent; needs `multipart/form-data` |
| `<input>` type | `text` | A typo'd type silently degrades to a text box — no keyboard, no validation |
| `<script src>` with no attribute | Parser-blocking at that line | Rule 7 |
| `<img loading>` | `eager` | Correct for the LCP image; wrong for everything below the fold |
| `<img>` with no dimensions | Reserves nothing | Rule 3 |
| `<table>` source without `<tbody>` | Parser inserts one | `table > tr` selectors and DOM walks never match |
| `<textarea>` content | Literal, whitespace preserved | Indenting the source injects leading spaces and newlines into the value |
| `autocomplete` unspecified | Browser heuristic | Right guess most of the time; wrong on address, card, and OTP fields |
| `hidden` attribute | `display: none`, but CSS wins | `hidden` plus any `display` rule renders the element visible |
| `aria-hidden="true"` | Removed from the accessibility tree only | Still focusable and still in the tab order — a focus trap for keyboard users |
| `<a target="_blank">` | Implicit `noopener` in current browsers | Older webviews and embedded browsers still leak `window.opener`; keep `rel="noopener"` |
| `<iframe>` with no `sandbox` | Full capabilities of its own origin | Scripts, forms, popups, top-level navigation all allowed |
| `<input type="number">` | Spinner, locale-dependent parsing, silent value drop on non-numeric | Use `inputmode="numeric"` + `pattern` for codes, phone numbers, and card fields |
| Missing doctype | Quirks mode | Legacy box model and dozens of divergences (`parsing`) |

## Element Defaults

One default per need, with the escape hatch and its price. Full patterns and keyboard contracts: `interactive`.

| Need | Default | Switch when |
|---|---|---|
| Modal | `<dialog>` + `showModal()` | Never for a true modal — it is the only element that gets the top layer and the inert backdrop for free |
| Transient popup, menu, tooltip | Popover attribute API | You need a focus trap (→ dialog) or must support pre-2024 browsers (→ ARIA pattern) |
| Accordion, disclosure, "read more" | `<details>` + `<summary>` | You need the panel to remain in the DOM while animating height precisely, or a single-open group with roving focus |
| Tabs | No native element — ARIA tabs pattern | — |
| Autocomplete over a short fixed list | `<input list>` + `<datalist>` | You need custom rendering, async results, or multi-select (→ combobox pattern, ~200 lines of JS) |
| Icon | Inline `<svg aria-hidden="true">` beside text | The icon *is* the control — then it needs an accessible name (Rule 4) |
| Progress and gauges | `<progress>`, `<meter>` | — |
| Date, time, color, range | Native input types | The locale or range rules cannot be expressed natively — accept the full a11y contract of a custom widget |
| On/off switch | `<input type="checkbox">` + `role="switch"` | Never the `switch` attribute alone — it is not portable yet |
| Status message | `aria-live="polite"` region present in the DOM at load | The message interrupts a task (→ `assertive`); a region injected at message time announces nothing |
| Sortable data grid | `<table>` + `aria-sort` | Editable cells or virtualized rows (→ grid pattern) |
| Anything else | The element whose name matches the meaning; `<div>` only when nothing does | — |

## Output Gates

Before emitting markup, a review, or a fix:

- Does every interactive element have an accessible name, and is every one reachable and operable by keyboard alone?
- Does every image carry the right `alt` for its job, and every `<img>`/`<video>`/`<iframe>` a `width` and `height` (Rules 3, 5)?
- Does every form control have a `name` and a real label, and is every `id` in the fragment unique (Rules 2, 4)?
- Is the heading order a tree with no skipped level, and does each landmark appear where a screen-reader user would look for it?
- Would this parse the way it reads — no block inside `<p>`, nothing loose inside a table, every element inside a valid parent (Rule 9)?
- Is any content in this markup untrusted, and if so is it escaped for its exact context or run through an allowlist sanitizer (Rule 8)?
- Does anything user-facing depend on JS that has not shipped yet — a control that is inert until hydration, a link that is a `div`?
- Did anything durable come out of this — a page or template mapped, a rendering quirk, an audit result, a canonical host, a pattern that finally worked? Then it is written to its box via `references/memory.md`, with its `## Boxes` line, in this same turn.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| markup_flavor | html \| jsx \| vue \| svelte \| jinja \| erb \| handlebars | html | Syntax of every emitted snippet: attribute casing, self-closing form, boolean attributes, and which escaping helper is named in `security` |
| browser_support | evergreen \| widely-available \| legacy | widely-available | Gates what ships bare: `evergreen` allows popover and declarative shadow DOM unqualified; `widely-available` pairs them with a fallback; `legacy` blocks them and adds the pre-2020 equivalents (`interactive`) |
| a11y_target | wcag-a \| wcag-aa \| wcag-aaa | wcag-aa | Which row of the conformance table gates output in `accessibility` and `auditing`: AA = 4.5:1 body text and 24×24 CSS px targets; AAA = 7:1 and 44×44 |
| document_lang | text (BCP-47) | en | The `lang` on every generated `<html>`, the assumed direction, and the default `hreflang` self-reference (`internationalization`) |
| structured_data | none \| json-ld \| microdata | json-ld | Format and placement of schema markup emitted by `head` |
| inline_code_policy | allowed \| nonce \| forbidden | allowed | Whether emitted markup may carry inline `<script>`, `<style>` and `on*` handlers, ships them with a `nonce` placeholder, or moves them to external files (`security`) |
| untrusted_html | escape \| sanitize \| trusted-types | escape | The default treatment of user-supplied markup and which pipeline `security` recommends |
| email_client_floor | modern \| outlook-desktop | outlook-desktop | Whether `email` emits table layout, VML and inline styles, or allows a single-column modern build |
| output_shape | fragment \| full-document | fragment | Whether an answer returns the changed elements in context or a complete document |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — formatter and linter (Prettier, html-validate, axe in CI), CMS or template engine, component library, which validator is authoritative — affects the shape of every example and the gates in `auditing`
- **Conventions** — attribute order and quoting, self-closing style on void elements, `data-*` naming, id and class conventions, comment density, one-file-per-component vs page templates — affects emitted markup
- **Platform** — target surfaces (web app, marketing site, email, print, embedded webview), device mix, whether RTL or CJK is in scope, minimum screen and pointer type — affects `media`, `email`, `internationalization`
- **Safety posture** — how loudly to flag accessibility regressions, whether third-party embeds and inline analytics may be emitted at all, appetite for `dangerously`-style raw HTML injection — affects Output Gates and `security`
- **Integrations** — analytics, consent management, icon and font providers, image CDN, the ESP an email will be sent through — affects `head`, `performance`, `email`
- **Constraints** — banned elements or embeds, a strict CSP regime, a no-JS requirement, legacy pages that must keep working, brand rules on titles and social images — affects what may be proposed at all
- **Output register** — diff vs whole file, how much of the rationale ships with the fix, whether alternatives are shown before the recommendation
- **Cadence** — accessibility re-audit, validation sweep, email client re-test, third-party embed review — every accepted cadence becomes a row in the `## Due` table of `references/memory.md`

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| `<div onclick>` as a button | No keyboard, no focus, no role, no disabled state, no form submission | `<button type="button">`; style it flat (Rule 1) |
| `aria-label` on a `<div>` or `<span>` | Names are only exposed on elements with a role that supports naming — on a bare `div` it is ignored | Give it a role that takes a name, or use the right element |
| Fixing an ARIA warning by adding more ARIA | Redundant or conflicting roles override the native semantics that were already correct | Remove the role; `role="button"` on `<button>` is noise, `role="text"` erases children |
| Headings chosen by size | `h4` used for a section under an `h2` breaks the outline every screen-reader user navigates by | Level by depth, size by CSS (`semantics`) |
| `tabindex="1"` and above | Jumps that element ahead of the entire natural order, everywhere on the page | Only `0` and `-1` are ever correct (`accessibility`) |
| `<p>` used as a layout wrapper | Any block child closes it — you get two empty paragraphs and orphaned content | `<div>` for grouping, `<p>` for prose (Rule 9) |
| Nested `<a>` or `<button>` inside `<a>` | Illegal content model; the parser un-nests them and the click target becomes unpredictable | One interactive element per interactive element |
| `<br>` for spacing | Announced as line breaks and impossible to style responsively | Margin on block elements |
| Trusting `required` and `pattern` | Client validation is a UX affordance; anything can POST to the endpoint | Validate on the server; use the attributes for the keyboard and the error timing |
| `placeholder` used as the label | Vanishes on input, low contrast, and unreadable to anyone who tabs back | Visible `<label>` (Rule 4) |
| Lazy-loading the hero image | Defers the LCP element and defeats the preload scanner — measurably slower | `loading="eager"` and `fetchpriority="high"` on the LCP image (`performance`) |
| One `.ico` as the whole favicon set | Misses dark mode, high-DPI, and every mobile install surface | The three-file floor plus a manifest (`head`) |
| Blocklist sanitizing (`strip <script>`) | `<img onerror>`, `javascript:` URLs, SVG handlers, and mutation-XSS all survive it | Allowlist sanitizer, escaped by context (Rule 8) |
| `sandbox="allow-scripts allow-same-origin"` on same-origin content | The frame can reach into its own parent document and remove the sandbox attribute | Serve framed content from a distinct origin (`security`) |
| Copying the desktop page into an email | Flex, grid, `position` and external CSS are absent from the Word engine | Table layout, inline styles, 600px (`email`) |
| A markup decision that lives only in the chat | Re-litigated every quarter by whoever inherits the template | `artifacts/` with the date and what was rejected (`references/memory.md`) |

## Where Experts Disagree

- **How much ARIA is healthy.** One school treats every ARIA attribute as debt to be justified; the other builds design-system components on ARIA patterns because the native elements do not compose. The frontier is ownership: if a component has tests and a maintainer, an ARIA pattern is fine; if it is one page written once, the native element wins because nothing will maintain the contract.
- **`<section>` vs `<div>`.** `<section>` with no accessible name adds a region nobody can navigate to and clutters the landmark list; `<section aria-labelledby>` is genuinely useful. Default: `<div>` for grouping, `<section>` only when it has a heading you would want in the landmark list.
- **Web components in content sites.** Encapsulation and portability against a hard cost: nothing renders until the definition loads, and forms, labels and CSS all need explicit bridges across the shadow boundary. Declarative shadow DOM narrows the gap but does not close it (`templates`).
- **Semantic markup and SEO.** Search engines do not rank a `<article>` above a `<div>`, and claiming they do discredits the real argument: semantics buy assistive-tech behavior, browser features, and future parsers. Make the accessibility case; the metadata that genuinely affects search is in `head`.
- **Email builders vs hand-written email.** Builders survive client quirks that a hand-written template rediscovers; hand-written wins on size, dark mode control, and not being clipped at 102 KB. The frontier is whether anyone will re-test on client updates (`email`).

## Security & Privacy

**Credentials:** this skill reads and writes markup files. Keep API keys, verification tokens, session values, and ESP credentials out of state roots: strip values found in pasted markup and store pointers only (`env:…`, `keychain:…`, `1password:…`).

**Local storage:** preferences, page and template notes, rendering quirks, audit results, and generated artifacts stay under `<state_root>/` on this machine, plus hostname rows in the shared domains box and project notes in the shared projects box. URLs, element names, and attribute names only — no secrets.

**Guardrails:** name third-party embeds with the origin they contact and the capabilities they request before proposing them. Emit markup that renders user-supplied content only after escaping for the exact context or running an allowlist sanitizer.
