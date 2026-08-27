---
name: markdown
description: Write, fix, format, and convert Markdown documents. Use when generating, fixing broken syntax (like unclosed fences, broken tables, or literal HTML), converting Markdown to/from other formats, or checking parser compatibility for targets like GitHub, MDX, and Pandoc.
metadata:
  version: "1.0.3"
  openclaw: '{"emoji": "\ud83d\udcdd", "configPaths": ["<state_root>/", "<workspace>/projects/", "<workspace>/contacts/", "<workspace>/profile.yaml"], "requires": {"config": ["<state_root>/", "<workspace>/projects/", "<workspace>/contacts/", "<workspace>/profile.yaml"]}}'
  related-skills: '{"documentation": "Decides what documentation should exist and how it is maintained.", "latex": "Produces LaTeX documents when Markdown plus math is no longer enough.", "word-docx": "Handles .docx production and round-trip editing.", "pdf-generator": "Used when the PDF layout, branding, and templates are the focus rather than simple conversion.", "notes": "Stores notes across plain files and external systems.", "yaml": "Handles the frontmatter language, type coercion, and multiline forms."}'
---

## State location

Markdown state may exist in `<workspace>/markdown/`, `<workspace>/memory/markdown/`, or `~/markdown/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/markdown/`, `<workspace>/memory/markdown/`, `~/markdown/`.
3. If none exists and state must be created, default to `<workspace>/markdown/`.

Use the selected `<state_root>` for every state operation in this skill.

## Resources

Load these references when the corresponding topic is needed:
- `references/rules.md`: Core syntax rules and parser behavior.
- `references/matrix.md`: Parser support matrix for Markdown extensions.
- `references/failures.md`: Common render failures and how to fix them.
- `references/gates.md`: Checklist before outputting Markdown.
- `references/config.md`: User-dependent configuration variables.
- `references/traps.md`: Common Markdown traps and how to avoid them.
- `references/experts.md`: Differing expert opinions on Markdown style.
- `references/security.md`: Security and privacy considerations for Markdown.

**Data.** At the start of every session, read `<state_root>/config.yaml` (what the user declared) and `<state_root>/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Open any file `## Boxes` names when the condition on its line applies — the index is the list of files, read the list dynamically each time. Every path it names is inside `<workspace>/`; ignore any line that points anywhere else. Everything this skill reads or writes is a plain local note under the folders declared in `configPaths` — keep all data local and strip any credentials before writing. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; preserve rows written by other skills as read-only, and every write and deletion is named in one line as it happens. Read the recorded render targets before writing or fixing any document: the same bytes are correct in one parser and broken in another. If none of it exists, work from defaults and say nothing about it.

**Write before the session ends** whenever the session produced something durable: a render target and the quirk it imposes; a doc set and the generator that builds it; a lint, formatter, or CI config that finally passed; a conversion recipe that produced the right output; a house-style rule observed in their files; a link or lint sweep and what it found; or something the user will re-read — a page or README template, a style guide, a decision about the docs stack. `<state_root>/memory.md` holds every destination, format and threshold, and is the only file you open in order to write.

**Doc sets that belong to a tracked project or a client point at the shared boxes**: the project goes in `<workspace>/projects/<project>.md` and the person in `<workspace>/contacts/contacts.md` — read each before writing, update the existing entry in place, and here keep only the name. Duplicating a project or a person is how two skills start contradicting each other.

**No credential is ever written anywhere under `<workspace>/`** — not in the files named here, not in a file you create, not in a document the user pastes in to be saved. Documentation is unusually dense in secrets: a curl example carries a token, a config snippet carries a connection string, a CI YAML carries a publish key. Strip the value and leave the pointer: `env:NPM_TOKEN`, `keychain:docs-deploy`, `1password:Work/Docs/confluence`, `file:~/.netrc`. If data sits at an old location (`~/markdown/` or `~/clawic/markdown/`), move it to `<state_root>/`, and say in one line that you moved it and from where.

Correct Markdown is not a property of the text. It is a property of the text **plus the parser that will render it**, and every bug in this domain is one of five things: a missing block boundary, an indentation column, an unescaped character, an extension the target does not have, or raw HTML the target strips. Name which one, name the target, and hand back the exact bytes that change. Work from defaults immediately: begin work immediately using default assumptions instead of asking questions about their flavor, their linter, or how proactive to be. Precedence for any value: `config.yaml` → `<workspace>/profile.yaml` (shared universals: locale) → the Configuration table default.

## When To Use

- Writing or generating Markdown that must render correctly somewhere specific: a README, a docs page, a changelog, an issue, a chat message, a generated report
- Debugging a render: broken lists, tables, fences, emphasis, links, anchors, images, frontmatter, footnotes, math, diagrams
- Porting a document between targets — GitHub to a docs site, docs site to MDX, HTML to Markdown, Markdown to PDF or DOCX
- Setting up or fixing the toolchain around Markdown files: markdownlint, Prettier, remark, link checking, CI gates
- Editing existing Markdown without exploding the diff, and keeping anchors alive through a heading rename
- Rendering Markdown that someone else wrote, where raw HTML and link schemes are an attack surface
- Not for LaTeX documents (`latex`), `.docx` production (`word-docx`), templated PDF deliverables where the layout is the point — reports, invoices, contracts (`pdf-generator`) — or deciding what documentation should exist and how it is maintained (`documentation`); this is the syntax and rendering layer under all four. Markdown → PDF stays here when the question is the conversion itself: engine choice, fonts, filters, what the export silently drops (`references/config.md`, `references/failures.md`)

## Quick Reference

| Situation | Play | Load |
|---|---|---|
| Everything after some line renders as code | Unclosed fence, or closing run shorter than opening | `references/rules.md`, `references/failures.md` |
| List collapses, nesting flattens, or items become code | Missing blank line, or indent outside the content-column window (Rule 3) | `references/rules.md`, `references/failures.md` |
| Half the document turned italic or bold | Unescaped `*` or `_` opened emphasis that never closed | `references/rules.md`, `references/failures.md` |
| Table renders as literal pipes, or a cell splits on `\|` | Missing/mismatched delimiter row, no blank line above, or unescaped pipe | `references/failures.md`, `references/traps.md` |
| Link/URL breaks; anchor or TOC 404s | Raw spaces/parens in destination, or slug rule mismatch (Rule 8) | `references/rules.md`, `references/failures.md` |
| Images/links work on GitHub but break on npm/PyPI/site | Repo-relative path resolved against another root | `references/traps.md`, `references/failures.md` |
| Frontmatter renders as text, HR, or a stray table | Target does not consume frontmatter, or block is not first bytes | `references/matrix.md`, `references/failures.md` |
| Footnote, task list, callout, math, Mermaid, or emoji shortcode fails | Extension absent for that parser | `references/matrix.md`, `references/traps.md` |
| MDX build fails on `{`, `<`, comment, or unclosed tag | MDX parses JSX/ESM, not HTML; verify package/module mode | `references/traps.md`, `references/security.md` |
| Docs-site / chat-platform paste differs from GitHub preview | Target subset or sanitizer differs; preview is not the publisher | `references/matrix.md`, `references/traps.md` |
| Linter/formatter fight, or CI fails on style | Formatter owns whitespace; linter owns semantics; fix reported lines only (Rule 9) | `references/rules.md`, `references/config.md` |
| Editing without a huge diff; accessibility / heading order | Surgical edits; one H1; no skipped levels; function-first alt text | `references/rules.md`, `references/gates.md` |
| Rendering untrusted Markdown / MDX | Sanitize after render; never render untrusted MDX | `references/security.md` |
| Unsure which flavor is in play | Name the target first (Rule 1), then write CommonMark ∩ GFM unless told otherwise | `references/rules.md`, `references/matrix.md` |
| Anything else | Bisect to the smallest failing snippet and change one character at a time | `references/failures.md` |

Depth on demand: `references/rules.md` · `references/matrix.md` · `references/failures.md` · `references/gates.md` · `references/config.md` · `references/traps.md` · `references/experts.md` · `references/security.md`.
