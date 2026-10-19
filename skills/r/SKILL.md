---
name: r
description: >
  Diagnose and fix common R traps: 1-based indexing, silent x[0], drop=TRUE
  coercion, NA propagation, factor level / as.numeric surprises, vector
  recycling, sample(n) vs sample(c(n)), and 1:length(x) on empty input. Use when
  writing or debugging R / Rscript, when a data.frame collapses to a vector, when
  NA comparisons misbehave, when factors appear after read.table on old R, or
  when loops should be vectorized. Prefer `statistics` for inference wording,
  `pandas` / `numpy` for Python tabular or array work, `sql` for relational
  queries, and `matlab` for MATLAB indexing/NaN issues.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📊","requires":{"bins":["Rscript"]}}'
  related-skills: '{"statistics":"Probability, hypothesis tests, and inference language beyond R syntax traps.","pandas":"Python DataFrame cleaning and transforms instead of R data.frame work.","numpy":"Python ndarray vectorization and broadcasting instead of R vectors.","sql":"Relational queries and schema work outside in-memory R frames.","matlab":"MATLAB indexing, NaN, and matrix-vs-element-wise traps when the runtime is MATLAB."}'
---

# R

Practical coaching for R language gotchas that cause silent wrong answers.
Advise by default; run `Rscript` only when the environment has it and the user
asks for execution.

Load `references/sources.md` before restating indexing semantics, NA rules,
`stringsAsFactors` defaults, `sample()` length-one behavior, or tidyverse style
claims.

## State location

This skill is **stateless by default**. Optional preference notes may live under
a portable `<state_root>` only when the user wants continuity across sessions —
never inside the skill package.

Resolve `<state_root>` before reading or writing state:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/r/`, `<workspace>/memory/r/`, `~/r/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and durable notes are needed, create `<workspace>/r/` when
   `<workspace>` is available; otherwise ask for a state root before creating
   data.

Use the selected `<state_root>` for every state operation in this skill.
Keep it fixed for the rest of the invocation. Never write the literal string
`<state_root>` to disk. Do not write runtime state into this skill package.

Suggested layout once persistence is enabled:

```text
<state_root>/preferences.md
<state_root>/snippets.md
```

## When to use

- Debugging unexpected empty results, dropped dimensions, or recycled lengths
- Choosing `[` vs `[[`, `drop = FALSE`, or tibble-safe subsetting
- Handling `NA` checks and `na.rm` in summaries
- Correcting factor level / numeric-conversion mistakes
- Replacing fragile `1:length(x)` / `sample(n)` patterns
- Preferring vectorized code over slow accumulating loops

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| Hypothesis tests, CIs, p-values, estimands | `statistics` |
| Python DataFrame pipelines | `pandas` |
| Python ndarray / broadcasting | `numpy` |
| SQL / warehouse queries | `sql` |
| MATLAB array indexing and NaN | `matlab` |

## Situation detection

| Context | Load |
|---------|------|
| Indexing, `[`/`[[`, `drop`, recycling | This SKILL + Extract / Arithmetic manuals in `references/sources.md` |
| NA, factors, `stringsAsFactors` | This SKILL + NA / factor / NEWS links in `references/sources.md` |
| `sample` / `seq_along` / assignment scope | This SKILL + sample / seq manuals in `references/sources.md` |
| Verified URLs before restating defaults | `references/sources.md` |

## Prefer

- Use `is.na(x)` for missingness; use `na.rm = TRUE` on summaries that should ignore `NA`.
- Keep data.frame / tibble shape with `drop = FALSE` or tibble/`dplyr` verbs when a single column must stay tabular.
- Prefer `seq_along(x)` over `1:length(x)` for index loops.
- Prefer `sample.int(n, …)` or an explicit length check before `sample(x)` when `x` might have length 1.
- Convert factor codes with `as.numeric(as.character(f))` (or `as.integer(levels(f))[f]`) when numeric values are required.
- Prefer `<-` for assignment in examples; document R ≥ 4.0.0 `stringsAsFactors = FALSE` default and call out older hosts explicitly.
- Prefer whole-vector operations (`sum`, `lapply` / `vapply`, `purrr::map`) when they preserve correctness; profile before micro-optimizing.

## Anti-patterns

| Pattern | Safer replacement |
|---|---|
| `x == NA` | `is.na(x)` |
| `df[, 1]` when a one-column frame is required | `df[, 1, drop = FALSE]` or tibble subsetting |
| `as.numeric(factor)` for stored numeric labels | `as.numeric(as.character(factor))` |
| `1:length(x)` | `seq_along(x)` |
| `sample(5)` when sampling from the scalar 5 | `sample(c(5), …)` or `sample.int` with clear intent |
| Relying on `T` / `F` | `TRUE` / `FALSE` |
| Silent length recycling across mismatched vectors | Make lengths equal explicitly or stop on mismatch |

## Workflow

1. **Reproduce the smallest failing expression** with `str()`, `length()`, and `dim()`.
2. **Classify the trap**: indexing, `NA`, factor, recycling, sampling, or scope/assignment.
3. **Apply the narrow fix** from Prefer / Anti-patterns; state the R version assumption when defaults differ (especially pre-4.0.0 `stringsAsFactors`).
4. **Verify shape and missingness** after the change (`class`, `dim`, `sum(is.na(.))`).
5. **Optional notes**: if the user wants continuity, record host R version or preferred tidyverse vs base style under `<state_root>/preferences.md`.

## Core traps (summary)

### Indexing

- R is 1-based: first element is `x[1]`.
- `x[0]` returns an empty vector of the same type — silent, not an error.
- Negative subscripts drop positions (`x[-1]`).
- `[` subsets and may keep list structure; `[[` extracts one element.
- `df[, j]` may drop to a vector; use `drop = FALSE` to keep a data.frame.

### Recycling

- Shorter vectors recycle to the longer length in arithmetic; mismatched lengths that are not multiples emit a warning — treat unexpected recycling as a bug until proven intentional.

### NA and factors

- `NA` propagates through arithmetic and comparisons; `NA == NA` is `NA`.
- Since R 4.0.0, default `stringsAsFactors` is `FALSE`; older hosts may still coerce characters on read — verify with `getRversion()` / read arguments.
- Factor internals are integer codes; new values outside `levels` become `NA`.

### Sampling and sequences

- `sample(n)` for a single positive numeric `n` samples from `1:n`; `sample(c(n))` samples from the scalar.
- Empty `x` makes `1:length(x)` equal `c(1, 0)`; use `seq_along(x)`.

### Assignment and scope

- Idiomatic assignment is `<-`; `<<-` writes to a parent environment and is rarely appropriate in examples.
- Functions resolve free variables in parent environments — prefer explicit arguments over relying on globals.

## Verification checklist

- [ ] Indexing intent uses 1-based positions and distinguishes `[` vs `[[`
- [ ] Tabular subsetting preserves required dimensions
- [ ] Missing values use `is.na` / documented `na.rm`
- [ ] Factor conversions preserve labeled values, not codes
- [ ] Loops / samples avoid empty-length and length-one `sample` traps
- [ ] Claims about defaults cite `references/sources.md` (R version noted)

## Cognitive load notes

- Phrase guidance as Prefer / Anti-patterns tables rather than stacked "never" lists.
- Version-specific defaults (especially `stringsAsFactors`) are stated as positive R ≥ 4.0.0 behavior plus an explicit older-host check.
- Sibling routing uses a handoff table so this skill stays on language traps instead of inference or Python/MATLAB runtimes.
