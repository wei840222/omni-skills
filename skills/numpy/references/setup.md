# Setup — NumPy

Read this on first use when helping with NumPy, or when the user wants optional
cross-session preferences.

## Integration (first 2–3 exchanges)

Confirm when the skill should activate:

- Always on array / numerical Python work, or only when asked?
- Save that preference to host MAIN memory only with explicit consent.

## Context to learn (optional)

- Domain: data science, scientific computing, ML preprocessing, general
- Experience: beginner / intermediate / advanced
- Library mix: pure NumPy, pandas, SciPy, PyTorch interop

## Preferences (only if offered)

- Default floating dtype: `float32` vs `float64`
- Memory vs speed bias
- Whether to include matplotlib checks by default

## State creation

If the user wants continuity, resolve `<state_root>` per `SKILL.md`, then create:

- `<state_root>/memory.md` from `assets/memory-template.md`
- `<state_root>/snippets/` only when the user asks to save a pattern

Lookup order before create: explicit override → existing
`<workspace>/numpy/` → `<workspace>/memory/numpy/` → `~/numpy/` → default create
`<workspace>/numpy/`.

Do not write outside `<state_root>/` for skill state. Do not treat the literal
string `<state_root>` as a filesystem path.

## Response shape

1. Restate the numeric goal and shape constraints in one line.
2. Give complete runnable code with `import numpy as np`.
3. Show shape/dtype or a one-line validation print.
4. Load `references/advanced.md` only for traps the user actually hit.
