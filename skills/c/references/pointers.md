# Pointer Traps

- Dereferencing NULL is UB (often a crash, never a reliable signal).
- Pointer arithmetic past one-past-the-end is UB even without a dereference.
- `p[i]` with `i` outside the array silently corrupts or traps.
- Comparing pointers from unrelated objects is UB.
- `void*` arithmetic is not standard C (compiler extensions only).
- `char*` casts are fine for byte access; casting back may break alignment.
- Calling through a function pointer with the wrong type is UB.
- Returning `&local` creates a dangling pointer.
