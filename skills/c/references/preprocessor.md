# Preprocessor Traps

- `#define MAX(a,b) a>b?a:b` breaks in `MAX(x,y)+1` — parenthesize the whole expansion and each argument.
- `#define SQ(x) ((x)*(x))` still double-evaluates `SQ(i++)` — prefer inline functions when side effects matter.
- Missing include guards cause redefinition errors.
- `#if MACRO` with an undefined macro is `0`, not a diagnostic.
- Multi-statement macros belong in `do { ... } while (0)`.
- Distinguish `#define FOO` from `#define FOO 1` (`#ifdef` vs `#if`).
- `#x` stringify and `a##b` paste often need a second macro layer for expansion.
