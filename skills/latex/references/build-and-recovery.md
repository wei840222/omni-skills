# LaTeX compilation and recovery

## Default build path

Use the project’s existing build instructions first. For a conventional PDF build, run:

```bash
latexmk -pdf document.tex
```

`latexmk` reruns the compiler as needed and invokes bibliography and index tools when its configuration and document declarations require them. For a `biblatex` document using the usual `biber` backend, use `latexmk` or run the engine, `biber`, then the engine twice.

## Diagnose from the log

1. Start with the first error in `document.log`; later errors often follow from it.
2. For `Undefined control sequence`, check spelling and the package that defines the command.
3. For `LaTeX Error: File ... not found`, correct the package installation or the project-relative asset path, then rerun the same build.
4. For unresolved references or citations, complete the required build cycle and confirm auxiliary files are writable in the project build directory.
5. For `Overfull \hbox`, inspect the reported line in the PDF and prefer a local text, URL, table-column, or image-width adjustment. Use global looseness settings only after checking their document-wide effect.

## Engine compatibility

Select the engine from project requirements: `pdflatex` for established PDF workflows, `xelatex` or `lualatex` when the document requires modern system fonts or Unicode-oriented font tooling. Confirm package support and rebuild from clean auxiliary output only when the project’s build process documents that recovery step.

## Sources

- LaTeX Project documentation — https://www.latex-project.org/help/documentation/
- LaTeX2e unofficial reference manual — https://latexref.xyz/
- CTAN: latexmk — https://ctan.org/pkg/latexmk
- CTAN: biblatex — https://ctan.org/pkg/biblatex
