# Sources (Gate 6)

Full URLs verified during this refactor. Re-check before restating API behavior
or version-sensitive defaults.

## Agent skill format

- Agent Skills specification index: https://agentskills.io/llms.txt
- Agent Skills specification: https://agentskills.io/specification
- Reference validator package: https://github.com/agentskills/agentskills/tree/main/skills-ref

## NumPy core documentation

- NumPy documentation home: https://numpy.org/doc/stable/
  Takeaway: canonical entry for array programming guidance and API reference.
- NumPy absolute beginners guide:
  https://numpy.org/doc/stable/user/absolute_beginners.html
  Takeaways: array creation basics; vectorized operations preferred over Python
  element loops; indexing and slicing fundamentals.
- Broadcasting rules:
  https://numpy.org/doc/stable/user/basics.broadcasting.html
  Takeaways: dimensions compare from the trailing axis; axes compatible when
  equal or one is 1; result shape is the broadcast shape.
- Copies and views:
  https://numpy.org/doc/stable/user/basics.copies.html
  Takeaways: basic slicing generally returns views; advanced indexing and many
  functions return copies; use `.copy()` when independence is required.
- `ndarray.view` reference:
  https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html
  Takeaway: views reinterpret or share memory without guaranteeing a deep copy.
- Linear algebra routines:
  https://numpy.org/doc/stable/reference/routines.linalg.html
  Takeaways: `numpy.linalg` covers solve, inv, eig, det, and related helpers;
  matrix product operators complement `np.dot` depending on operand ranks.
- Random Generator API:
  https://numpy.org/doc/stable/reference/random/generator.html
  Takeaway: `np.random.default_rng` is the recommended modern Generator entry.

## Claim inventory

| Claim in skill | Source basis |
|---|---|
| Prefer vectorized ufuncs over Python element loops | absolute beginners + performance practice |
| Broadcasting right-align / size-1 stretch | basics.broadcasting |
| Basic slice → view; fancy index → copy | basics.copies |
| Integer dtype truncates float assigns | dtype semantics / beginners guide |
| `np.linalg.*` for solve/inv/eig/det | routines.linalg |
| Prefer `default_rng` for new random code | random Generator docs |

## Notes

- Speedup ranges such as “10–100×” are workload-dependent illustrations, not
  guaranteed benchmarks — measure on the user’s data when performance is the
  acceptance criterion.
- Default integer width is platform/NumPy-build dependent; always print
  `.dtype` when teaching truncation.
