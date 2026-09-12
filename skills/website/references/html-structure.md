# HTML structure

Load when shaping documents, landmarks, interactive semantics, or link safety.

## Document skeleton

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Page title</title>
  </head>
  <body>
    <header>…</header>
    <nav aria-label="Primary">…</nav>
    <main id="main">
      <h1>Page title</h1>
      …
    </main>
    <footer>…</footer>
  </body>
</html>
```

## Landmarks and headings

- Prefer one `<main>` per page.
- Label multiple `<nav>` regions (`aria-label`) so AT can distinguish them.
- `<h1>` matches the page purpose; section headings descend without skips.
- Use `<section>` when the section has a heading; avoid div soup for major regions.

## Interactive semantics

| Intent | Element |
|---|---|
| Navigate to a URL | `<a href>` |
| In-page action (submit-less button, toggle, open dialog) | `<button type="button">` |
| Submit a form | `<button type="submit">` or input submit |
| Disclosure | native `<details>`/`<summary>` when enough |

Do not recreate buttons/links with `<div onclick>` — you lose keyboard and AT behavior for free.

## Links and safety

- New-tab links: `rel="noopener noreferrer"` with `target="_blank"`.
- Distinguish visited/external affordances in UI copy when it reduces surprise.
- Downloadable files use clear link text (`Download report (PDF)`), not “click here”.

## Validation mindset

- Unclosed tags and mis-nested interactive elements break accessibility trees.
- Prefer native controls before ARIA; ARIA authoring errors can make things worse.
- For deep form/dialog/email-HTML cases, escalate to `html`.
