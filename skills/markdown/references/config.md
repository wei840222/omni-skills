## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| target_flavor | commonmark \| gfm \| mdx \| pandoc \| kramdown \| goldmark \| python-markdown \| obsidian | gfm | The parser every rule and every generated document is written against; drives the Support Matrix row set and Rule 1 |
| docs_generator | none \| docusaurus \| mkdocs-material \| jekyll \| hugo \| sphinx-myst \| astro-starlight \| vitepress \| quarto | none | Frontmatter schema, admonition syntax, link resolution and build commands in docs-sites rules |
| lint_tool | markdownlint \| remark \| prettier \| none | markdownlint | Which rule ids are cited, which config file linting rules emits, and which CI snippet |
| line_wrap | none \| sentence \| number (columns 60-120) | none | How generated and edited prose is wrapped; `sentence` = one sentence per line for reviewable diffs (editing rules) |
| list_indent | 2 \| 4 | 4 | Spaces per nesting level in generated lists (Rule 3); 2 is safe only for GFM-family targets |
| list_marker | - \| * \| + | - | Bullet character in generated lists; must match lint rule MD004 if the repo enforces one |
| raw_html | allow \| avoid \| forbid | avoid | Whether fallbacks may use HTML (`<br>`, `<details>`, `<img width>`, HTML tables) or must stay pure Markdown; `forbid` for targets that strip it |
| frontmatter_format | yaml \| toml \| json \| none | yaml | Fence and syntax of generated metadata blocks (frontmatter rules) |
| link_style | inline \| reference | inline | Whether long documents keep destinations inline or collect them as `[ref]: url` definitions at the bottom |
| table_style | padded \| compact | padded | Whether generated tables pad cells to align pipes; `compact` keeps diffs small in files many people edit |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Conventions** — heading case (sentence vs title), emphasis and strong markers, fence character and length, ordered-list numbering style, one-H1 rule, file naming, whether a TOC is generated and to what depth
- **Tooling** — editor and preview engine, format-on-save, link checker, TOC generator, spell checker, whether CI blocks or only warns
- **Platform** — the set of targets they actually publish to, generator versions, image hosting and dark-mode variants, whether repos are private (image proxying differs)
- **Safety posture** — whether an autofixer may rewrite whole files, whether generated or vendored `.md` is off-limits, how strictly untrusted Markdown is sanitized
- **Output register** — corrected file vs diff vs explanation-first, how much of the reasoning to keep, whether to show the rendered result
- **Accessibility bar** — alt text required or optional, heading-order enforcement, whether complex tables may fall back to HTML
- **Localization** — locale, RTL content, smart quotes and typographic substitution, non-breaking spaces, CJK line-break behavior
- **Cadence** — link check, lint sweep, badge and version refresh, stale-page review; every accepted cadence becomes a row in the `## Due` table of `<state_root>/memory.md`
