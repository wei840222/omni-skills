# NumPy advanced reference

Load when the user hits shape errors, silent casts, view/copy confusion, or
needs a compact pattern sheet. Re-check `references/sources.md` before citing
version-sensitive API behavior.

## Traps

### Shape mismatches

```python
import numpy as np

a = np.array([1, 2, 3])        # (3,)
b = np.array([[1, 2, 3]])      # (1, 3)
c = np.array([[1], [2], [3]])  # (3, 1)

a.reshape(-1, 1)   # (3, 1)
a[np.newaxis, :]   # (1, 3)
```

### Silent integer truncation

```python
import numpy as np

arr = np.array([1, 2, 3])  # int64 by default on most platforms
arr[0] = 1.9               # becomes 1
arr = np.array([1, 2, 3], dtype=np.float64)
```

### View vs copy

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
view = arr[1:4]       # view — writes affect arr
copy = arr[[1, 2, 3]] # fancy index → copy
```

NumPy documents that basic slicing yields views into the original array, while
operations that cannot guarantee contiguity (including advanced indexing)
return copies. See sources for the authoritative wording.

### Broadcasting failures

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([1, 2])
# a + b  → ValueError: operands could not be broadcast together

m = np.zeros((3, 4))
row = np.array([1, 2, 3])
# m + row → error; m + row.reshape(-1, 1) works → (3, 4)
```

Broadcasting compares shapes right-to-left; axes are compatible when equal or
one of them is 1.

### In-place vs out-of-place

```python
import numpy as np

arr = np.array([3, 1, 2])
np.sort(arr)   # returns sorted copy
arr.sort()     # sorts in place
arr = np.sort(arr)  # explicit rebind when a copy is intended
```

## Essential patterns

### Create

```python
import numpy as np

np.zeros((3, 4))
np.ones((3, 4))
np.full((3, 4), 7)
np.eye(3)
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
rng = np.random.default_rng(0)
rng.random((3, 4))
rng.standard_normal((3, 4))
```

Prefer `np.random.default_rng` for new code; legacy `np.random.rand` /
`np.random.randn` remain common in older snippets.

### Reshape and stack

```python
import numpy as np

arr = np.arange(12)
arr.reshape(2, 6)
arr.ravel()    # 1-D view when possible
arr.flatten()  # 1-D copy
np.concatenate([a, b], axis=0)
np.stack([a, b], axis=0)
np.vstack([a, b])
np.hstack([a, b])
```

### Boolean indexing

```python
import numpy as np

arr = np.array([1, 5, 3, 8, 2])
arr[arr > 3]           # [5, 8]
out = arr.copy()
out[out > 3] = 0
np.where(arr > 3, 1, 0)
```

### Linear algebra

```python
import numpy as np

a @ b
np.dot(a, b)
np.linalg.inv(a)
np.linalg.det(a)
np.linalg.eig(a)
np.linalg.solve(a, b)
```

For 1-D × 1-D, `np.dot` is an inner product; for 2-D, prefer `a @ b` for
matrix multiplication clarity.
