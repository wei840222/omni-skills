# LaTeX syntax and document structure

## Characters, text, and math

- Escape reserved text characters with `\# \$ \% \& \_ \{ \} \textbackslash`; represent literal tilde and caret with `\textasciitilde` and `\textasciicircum`.
- Use `` `` `` and `''` for TeX quotation marks; use `-`, `--`, and `---` for hyphen, en dash, and em dash. Put mathematical minus signs in math mode.
- Use `$...$` or `\(...\)` inline, and `\[...\]` or an `equation` environment for display math. Use `align` for aligned multiline equations.
- Use `\text{...}` for prose in math, pair `\left` with `\right`, and separate a command from following text with `{}` or `\ `, as in `\LaTeX{}`.
- Use `~` for non-breaking number–unit spaces and `\,`, `\:`, `\;`, `\quad`, or `\qquad` for deliberate math spacing.

## Preamble and packages

- Put document class, packages, and shared settings before `\begin{document}`. Use `article` for short documents, `report` for chapter-oriented work, and `book` for book-length work.
- Add packages for a demonstrated need: `amsmath` for advanced math, `graphicx` for images, `booktabs` for tables, and `microtype` for typographic refinement.
- Load `hyperref` late and verify it against the project’s existing package order; package conflicts appear in the log and should be resolved at the conflicting package boundary.

## Labels, floats, tables, and images

- Place `\label` immediately after `\caption` in numbered floats so `\ref` binds to the intended counter.
- Treat `[htbp]` as placement preferences. Use `[H]` only when the `float` package is present and fixed placement is genuinely required.
- Use `\centering` in a figure or table. Prefer `booktabs` rules (`\toprule`, `\midrule`, `\bottomrule`) and avoid vertical rules for ordinary data tables.
- Resolve image paths relative to the main document or declare `\graphicspath`; choose graphics formats supported by the selected engine.
