# Translate memory template

Use only after `<state_root>` is resolved. This file is a skill asset (template), not runtime state.

## `<state_root>/config.yaml`

```yaml
source_lang: en
target_locales: []
formality: per-locale
variant_policy: regional
mt_policy: draft-only
review_stage: self-review
placeholder_style: icu
catalog_format: json
subtitle_cps: 17
deliverable_shape: target-only
cat_tool: none
```

## `<state_root>/memory.md`

```markdown
# Translate memory

## Boxes
- glossaries/en-es-419.md — open when target locale is es-419
- style/es-419.md — open when register/voice for es-419 is needed

## Locale Register
| Locale | Formality | Notes |
|---|---|---|
| es-419 | informal | product default |

## Due
| Cadence | Next due | Why |
|---|---|---|
| glossary consolidation | YYYY-MM-DD | term drift after release |

## Recent jobs
| Date | Pair | Words | Notes |
|---|---|---|---|
```

## Glossary row shape

| source | target | locale | pos | status | reason |
|---|---|---|---|---|---|
| sign in | iniciar sesión | es-419 | verb | accepted | product UI |
| sign in | ingresar | es-419 | verb | rejected | reserved for physical access |

## Shared-box identity keys

When the owning skills are installed, update existing rows in place:

- contacts: name + role/org
- projects: project slug
- finances/subscriptions: vendor + product

Write only rows this skill created; read others without rewriting them.
