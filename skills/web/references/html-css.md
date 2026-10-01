# HTML and CSS patterns

Load for markup structure, CSS layout traps, viewport, and responsive basics.

## HTML

- **Semantic landmarks** — Prefer `<main>`, `<article>`, `<nav>`, `<header>`, `<footer>`; assistive tech depends on them.
- **`<button>` vs `<a>`** — Buttons for in-page actions; anchors need real `href` for navigation. Clickable `<div>` breaks keyboard and SR UX.
- **Images** — Meaningful images need descriptive `alt`; decorative images use `alt=""` (empty, not missing).
- **Self-closing** — In HTML5, `<br>` is canonical; `<div/>` is invalid (not a void element).
- **IDs unique** — Duplicate IDs break `querySelector`, labels, and ARIA.
- **`<input type="number">`** — Still allows `e`, `+`, `-` in many browsers; validate server-side.
- **Hidden content** — `display: none` removes from a11y tree; `visibility: hidden` keeps layout space.
- **`target="_blank"`** — Pair with `rel="noopener noreferrer"`.
- **`lang`** — Set `<html lang="…">` for correct pronunciation and hyphenation.
- **DOCTYPE** — Always start documents with `<!DOCTYPE html>` to avoid quirks mode.

## CSS

- **`margin: auto` centering** — Needs explicit `width` or `max-width` on block boxes.
- **`z-index`** — Only applies to positioned (or transformed/flex/grid children in modern contexts); set `position` intentionally.
- **Flex `gap`** — Supported in current evergreen browsers; prefer `gap` over margin hacks for flex/grid spacing.
- **`auto-fit` vs `auto-fill`** — `auto-fit` collapses empty tracks; `auto-fill` preserves them.
- **Viewport height** — `100vh` can include mobile browser chrome; prefer `100dvh` / `svh` when UI must fit the visible viewport.
- **`:focus-visible`** — Keep focus visible for keyboard users; do not remove outlines without a replacement.
- **Cascade layers** — `@layer` orders specificity across files without `!important` wars.
- **Custom properties** — Define tokens on `:root` (or a theme root); they cascade.
- **`calc()` spacing** — `calc(100% - 20px)` needs spaces around `+`/`-`.
- **`transform-origin`** — Default is center; set explicitly for corner pivots.

## Responsive checklist

- Require viewport meta: `width=device-width, initial-scale=1`.
- Mobile-first base styles; add complexity with `min-width` queries.
- Touch targets ≥ 44×44 CSS px when the control is primary UI.
- No horizontal scroll at **320px** width.
- Test real devices when layout depends on soft keyboards or notch safe areas.

## Common requests

- **"Make it responsive"** → Mobile-first CSS; verify 320 / 768 / 1024; fix overflow and tap targets before desktop polish.
- **"Layout breaks on mobile"** → Check viewport meta, `100vh` vs `dvh`, fixed widths, and overflow on flex children.
