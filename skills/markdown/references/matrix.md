## Support Matrix

What actually renders where. Blank means "not without a plugin"; check the target before using anything below the third row.

| Feature | CommonMark | GFM (github.com) | MDX v3 | Pandoc | Python-Markdown | Slack / Discord |
|---|---|---|---|---|---|---|
| Pipe tables | — | yes | with remark-gfm | `pipe_tables` | `tables` ext | — |
| Strikethrough | — | `~~x~~` | with remark-gfm | `strikeout` | `pymdownx.tilde` | `~x~` / `~~x~~` |
| Task lists | — | yes | with remark-gfm | `task_lists` | `pymdownx.tasklist` | renders as text |
| Autolinked bare URLs | — | yes | with remark-gfm | `autolink_bare_uris` | `magiclink` | yes |
| Footnotes | — | yes | with remark-gfm | yes | `footnotes` ext | — |
| Raw HTML | passes through | sanitized allowlist | must be valid JSX | `raw_html` | passes through | — |
| `$…$` math | — | yes | with remark-math | `tex_math_dollars` | `arithmatex` | — |
| Mermaid fences | — | yes | theme/plugin | filter required | `superfences` | — |
| YAML frontmatter | renders as rule + heading | shown as a table | parsed as exports | `yaml_metadata_block` | `meta` ext | — |
| Custom heading id | — | — | `{#id}` | `{#id}` | `attr_list` | — |
| Callouts / admonitions | — | `> [!NOTE]` | `:::note` (Docusaurus) | fenced div | `!!! note` | — |
