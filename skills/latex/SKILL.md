---
name: latex
description: Create, compile, debug, and review LaTeX `.tex` documents with correct math, citations, floats, tables, and package setup. Use when producing or troubleshooting LaTeX source or its PDF build.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📐"}'
---

## Quick workflow

1. Identify the engine and build command already used by the project; preserve its document class and package conventions.
2. Write or edit the smallest relevant `.tex` unit, keeping structure, labels, and package declarations in their proper locations.
3. Build with `latexmk` when available: `latexmk -pdf document.tex`. It coordinates repeat passes and bibliography tools.
4. Treat the compiler log as the diagnosis: repair the first actionable error, then rebuild until cross-references and citations resolve.
5. Inspect the generated PDF for layout issues such as overfull boxes, misplaced floats, and incorrect table or figure references.

## Resource routing

| Resource | Load when |
|---|---|
| `references/syntax.md` | Writing or reviewing syntax, math, spacing, packages, floats, tables, images, labels, or document structure. |
| `references/build-and-recovery.md` | Choosing a compiler, configuring `latexmk`, resolving bibliography or cross-reference output, or diagnosing build failures. |

## Build checkpoints

- Keep the project’s selected engine unless the document requirements require a change; verify package compatibility before changing engines.
- For a missing citation or reference, run the appropriate complete build cycle and inspect the first relevant `.log` message before editing source.
- For a float or line-break problem, confirm the PDF result after a focused source change rather than forcing broad global layout settings.

## State location

This skill is stateless and does not store local configuration or persistent user state.
