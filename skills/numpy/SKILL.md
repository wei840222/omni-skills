---
name: numpy
description: >
  Write fast, memory-efficient numerical Python with NumPy arrays, broadcasting,
  vectorization, dtypes, views vs copies, axis reductions, and linear algebra.
  Use when the user asks for array operations, matrix math, vectorized loops,
  shape/broadcast fixes, or NumPy performance/memory guidance. Prefer `scipy`
  for optimize/stats/signal modules, `pytorch` for training loops/devices, and
  `statistics` for inference wording outside array code.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔢","requires":{"bins":["python3"]}}'
  related-skills: '{"data":"Broader data lifecycle cleaning and reporting around array work.","math":"Concept and proof explanations without NumPy APIs.","pytorch":"Tensor training, devices, and autograd once the task leaves plain ndarrays.","scipy":"Optimization, stats, signal, and sparse routines built on NumPy arrays.","statistics":"Hypothesis testing and inference language beyond array reductions."}'
---

# NumPy

Practical NumPy coaching for array creation, broadcasting, vectorization,
dtype/memory choices, view-vs-copy safety, axis-aware reductions, and
`np.linalg` basics. Prefer complete, runnable snippets with imports over
pseudocode.

This skill is **stateless by default**. Optional preference notes may live under
a resolved `<state_root>` only when the user wants continuity across sessions —
never inside the skill package.

## When to use

- Vectorize slow Python loops over numeric data
- Fix shape / broadcasting / axis mistakes
- Choose dtypes and avoid silent integer truncation
- Decide view vs copy before mutating slices
- Write small linear-algebra or reduction snippets with NumPy

Prefer `scipy` for `optimize` / `stats` / `signal` / sparse workflows, `pytorch`
for model training and CUDA device plumbing, `statistics` for hypothesis-test
wording, `math` for pure math explanations, and `data` for end-to-end tabular
pipelines.

## State location

Optional preference state may exist in `<workspace>/numpy/`,
`<workspace>/memory/numpy/`, or `~/numpy/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/numpy/`, `<workspace>/memory/numpy/`, `~/numpy/`.
3. If none exists and state must be created, default to `<workspace>/numpy/`.

Use the selected `<state_root>` for every state operation in this skill.
Create state only after the user wants continuity. Store preferences and
optional snippets only — never secrets.

## Quick workflow

1. **Import + shape first** — start from `import numpy as np` and print
   `.shape` / `.dtype` before mutating.
2. **Vectorize** — replace element Python loops with ufuncs, broadcasting, or
   reductions.
3. **Pick dtype intentionally** — set `dtype=` at creation when floats or narrow
   integers matter.
4. **Mutate only after view/copy check** — slicing shares memory; fancy index
   and many advanced paths return copies.
5. **Load depth on demand** — open `references/advanced.md` for traps and
   pattern tables; open `references/sources.md` before restating API facts.
6. **Validate** — show a tiny assert or printed shape/value check with the code.

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/setup.md` | First-use integration and optional preference capture |
| `references/advanced.md` | Shape traps, view/copy, essential creation/stack patterns |
| `references/sources.md` | Official NumPy / Agent Skills URLs before citing facts |
| `assets/memory-template.md` | Only when creating `<state_root>/memory.md` |
| `test-prompts.json` | Evaluation harness only — do not load during normal help |

## Operating rules

### 1. Vectorize first

Use vectorized ufuncs and broadcasting instead of Python loops over array
elements. NumPy loops in C for those paths and is typically much faster.

```python
import numpy as np

arr = np.arange(5)
# Prefer:
result = arr * 2
# Instead of appending inside a Python for-loop over arr
```

### 2. Understand broadcasting

Align dimensions from the right. Size-1 axes stretch; missing leading axes act
like size 1. Incompatible axes raise `ValueError` rather than guessing.

```python
import numpy as np

a = np.array([[1], [2], [3]])  # (3, 1)
b = np.array([10, 20, 30, 40])  # (4,)
result = a + b  # (3, 4)
```

### 3. Prefer views, copy on purpose

Basic slicing returns a view into the same memory. Call `.copy()` when the
caller needs an independent buffer. Fancy integer indexing returns a copy.

```python
import numpy as np

a = np.arange(6)
view = a[::2]       # view — writes affect a
independent = a[::2].copy()
fancy = a[[0, 2, 4]]  # copy
```

### 4. Choose dtypes deliberately

Default integer arrays truncate assigned floats. Declare `dtype=` when the
domain needs floats, narrow integers, or memory bounds.

```python
import numpy as np

arr = np.array([1, 2, 3], dtype=np.float64)
pixels = np.array(data, dtype=np.uint8)  # 0–255 domain
```

### 5. Be axis-aware

For 2-D arrays, `axis=0` reduces down rows (per column), `axis=1` reduces across
columns (per row), and omitting `axis` flattens first.

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
np.sum(arr, axis=0)  # [4, 6]
np.sum(arr, axis=1)  # [3, 7]
```

### 6. Prefer built-in routines

| Need | Use |
|------|-----|
| Element-wise math | `np.sin`, `np.exp`, `np.log` |
| Statistics | `np.mean`, `np.std`, `np.median` |
| Linear algebra | `np.dot`, `a @ b`, `np.linalg.*` |
| Sorting | `np.sort`, `np.argsort` |
| Searching | `np.where`, `np.searchsorted` |

### 7. Ship working snippets

Every code answer includes imports, a realistic tiny input, and a printed or
asserted check. Prefer `a @ b` or `np.matmul` for matmul clarity alongside
`np.dot` when ranks differ.

## Safety and boundaries

- Keep all numeric work local unless the user explicitly authorizes network I/O.
- Read/write optional state only under the resolved `<state_root>/`.
- Do not execute untrusted pasted arrays as code without review.
- Use placeholders for private datasets; do not commit user arrays into the
  skill package.
- Requires `python3` and a user-provided NumPy install in their environment.

## Optional state layout

```text
<state_root>/
├── memory.md   # preferences + common patterns (optional)
└── snippets/   # user-saved patterns (optional)
```
