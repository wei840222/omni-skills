# R research sources

Live-checked on 2026-10-19. Prefer these URLs over memory when restating
indexing semantics, NA rules, factor conversion, recycling, `sample()` /
`seq_along()` behavior, tidyverse style, or `stringsAsFactors` defaults.

## Agent Skills packaging

| Claim area | Source | Status |
|---|---|---|
| Agent Skills specification | https://agentskills.io/specification | HTTP 200 |
| Agent Skills machine summary | https://agentskills.io/llms.txt | HTTP 200 |
| Agent Skills best practices | https://agentskills.io/skill-creation/best-practices | HTTP 200 |
| Reference validator | https://github.com/agentskills/agentskills/tree/main/skills-ref | package `skills-ref` / `agentskills` |

## Base R language (normative manuals)

| Claim area | Source | Status |
|---|---|---|
| R language definition | https://cran.r-project.org/doc/manuals/r-release/R-lang.html | HTTP 200 |
| An Introduction to R | https://cran.r-project.org/doc/manuals/r-release/R-intro.html | HTTP 200 |
| Extract / subsetting (`[`, `[[`, `drop`) | https://stat.ethz.ch/R-manual/R-devel/library/base/html/Extract.html | HTTP 200 |
| Missing values (`NA`) | https://stat.ethz.ch/R-manual/R-devel/library/base/html/NA.html | HTTP 200 |
| Factors | https://stat.ethz.ch/R-manual/R-devel/library/base/html/factor.html | HTTP 200 |
| Arithmetic / recycling | https://stat.ethz.ch/R-manual/R-devel/library/base/html/Arithmetic.html | HTTP 200 |
| `sample` | https://stat.ethz.ch/R-manual/R-devel/library/base/html/sample.html | HTTP 200 |
| `seq` / `seq_along` | https://stat.ethz.ch/R-manual/R-devel/library/base/html/seq.html | HTTP 200 |
| R NEWS (incl. 4.0.0 `stringsAsFactors`) | https://cran.r-project.org/doc/manuals/r-release/NEWS.html | HTTP 200 |
| stringsAsFactors blog (R-project) | https://developer.r-project.org/Blog/public/2020/02/16/stringsasfactors/ | HTTP 200 |

Re-open the matching manual page before asserting edge-case return types or
version-specific defaults.

## Tidyverse / style (secondary)

| Claim area | Source | Status |
|---|---|---|
| Tibbles overview | https://tibble.tidyverse.org/articles/tibble.html | HTTP 200 |
| Tidyverse style — syntax / assignment | https://style.tidyverse.org/syntax.html | HTTP 200 |

Tibble “never drops dimensions / never converts strings to factors” guidance is
tidyverse policy, not a base-R guarantee. Prefer base manuals when the user is
on plain `data.frame`.

## Notes / corrections from baseline

- Jules patch claimed R before 4.0.0 converted strings to factors by default —
  confirmed via NEWS 4.0.0 (`stringsAsFactors = FALSE` default) and the
  R-project stringsAsFactors blog (HTTP 200 on 2026-10-19).
- A tidyverse.org blog URL for tibble 2.1.1 returned HTTP 404 here; cite the
  live tibble article instead.
- No `Rscript` binary in this handoff environment; Gate 8 execution evidence is
  structural / dry-run against the manuals and package files, not live R REPL
  output.
