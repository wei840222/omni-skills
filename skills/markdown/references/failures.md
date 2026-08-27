## Render Failures

Decode rule: **the symptom names the layer**. Text bleeding into the wrong block is a boundary problem; text disappearing is an escape or a sanitizer; text rendering literally is an extension the parser does not have.

| Symptom | Most likely cause | First move |
|---|---|---|
| Everything from line N to the end is a code block | Unclosed fence, or the closing run is shorter than the opening one | Count backticks on both fences; also check for a stray 4-space indent |
| List items all on one line, or as a single paragraph | No blank line before the list, or `loose vs tight` — a blank line between items adds `<p>` and the spacing you were fighting | structure rules |
| Sub-items are flat, or turned into code | Indent below the content column, or ≥ content column + 4 (Rule 3) | structure rules |
| Half the doc is italic from one point on | Unescaped `*` or `_` — often a filename, a glob, or `2*3` | Escape it, or wrap it in a code span |
| Table shows literal `\|` characters | Missing delimiter row, no blank line above, or the header/delimiter cell counts differ | tables rules |
| A cell splits in the middle of code | Unescaped pipe inside backticks | tables rules |
| Link text renders but the URL is dead | Space, `(`, or `)` in the destination | `<…>` around the destination, or percent-encode |
| `[text][ref]` renders literally | The `[ref]: url` definition is missing or misspelled — reference links fail silently | links rules |
| Anchor scrolls nowhere | Slug computed by a different rule than the one you assumed (Rule 8) | links rules |
| Image is a broken icon off-GitHub | Repo-relative path resolved by npm, PyPI, or the site against a different root | readmes rules |
| `---` at the top renders as a horizontal rule and a heading | The target does not consume frontmatter | frontmatter rules |
| HTML tag shows as escaped text, or vanishes | Sanitizer allowlist (GitHub, PyPI), or `unsafe: false` (Hugo/Goldmark) | flavors rules, docs-sites rules |
| `:tada:`, `[!NOTE]`, `[^1]` render as plain text | Extension absent in this parser | Support Matrix, then extensions rules |
| Renders in the editor preview, breaks on the site | VS Code preview is markdown-it, not the target's parser | Preview in the real target before shipping (Output Gates) |
| Invisible characters break a code sample or a build | Zero-width, bidi, or non-breaking spaces pasted from chat, a PDF, or a word processor | security rules |
| Anything else | Bisect: halve the document until the break disappears, then change one character at a time | — |
