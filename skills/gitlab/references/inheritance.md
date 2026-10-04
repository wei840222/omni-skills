# Inheritance and Reuse

## `extends` merge behavior

GitLab performs a reverse deep merge on **keys** when applying `extends`. It does **not** deep-merge the **values** of those keys:

- If both parent and child define `script`, `services`, or similar array/scalar keywords, the child's value replaces the parent's for that key.
- Nested hash maps can still combine at deeper keys, but list-valued keywords are replacement semantics in practice for job composition.

Do not document or assume “arrays are appended by `extends`.”

## Composing scripts safely

Prefer `!reference` when a child job must keep parent script steps and add more:

```yaml
.base:
  script:
    - echo "setup"

test:
  script:
    - !reference [.base, script]
    - echo "test"
```

## `include` and anchors

- Multiple `include` sources can override the same keys; later configuration wins under GitLab's include merge rules (deep merge for hash maps). Inspect the fully expanded config in the pipeline editor when overrides surprise you.
- YAML anchors (`&` / `*`) apply only within the same file. For cross-file reuse, use `include` plus `extends` or CI/CD components — not anchors alone.

## Debug checklist

1. Expand the configuration (pipeline editor / CI lint) before blaming the runner.
2. For missing parent `script` lines after `extends`, switch to `!reference` composition.
3. For cross-file reuse failures, verify the symbol lives in an included file reachable by `extends`/`!reference`, not an anchor alias.
