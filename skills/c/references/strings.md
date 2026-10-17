# String Traps

- Missing NUL terminator — `strlen`, `printf %s`, and `strcpy` keep reading.
- `strncpy(dst, src, n)` omits the terminator when `src` length ≥ `n` — set `dst[n-1] = '\0'` or prefer `snprintf`.
- `gets()` was removed in C11; use bounded APIs instead.
- Prefer `snprintf` over `sprintf` for bounded formatting.
- `strtok` mutates its buffer — skip string literals and shared storage.
- String literals are read-only — `char *s = "hi"; s[0] = 'H';` is UB; use `char s[] = "hi";` when mutation is required.
- Cache `strlen` results in hot loops (`O(n)` each call).
- `strcmp` returns `<0`, `0`, `>0` — not a fixed `-1/0/1` triad.
