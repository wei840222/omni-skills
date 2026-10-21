# HTML memory destinations

Load this file before writing durable HTML state. All html-owned paths are under the selected `<state_root>`. Shared boxes use their independently resolved roots.

## Write thresholds

Write when the session produced any of:

- a page or template mapping (landmarks, LCP element, `lang`/`dir`)
- a rendering quirk that cost effort to find (Outlook collapse, Safari gap, assistive-tech announcement, CMS attribute stripping)
- an accessibility or validation pass with concrete findings
- a verified canonical host, www-vs-apex choice, or locale→hostname map
- a reusable `<head>` boilerplate, accessible component pattern, email template, sanitizer allowlist, or native-element-versus-library decision

Skip ephemeral one-off markup fixes that will not recur.

## Destinations

### `<state_root>/config.yaml`

Declared preferences from the Configuration table (`markup_flavor`, `browser_support`, `a11y_target`, `document_lang`, `structured_data`, `inline_code_policy`, `untrusted_html`, `email_client_floor`, `output_shape`, plus preference areas). Create on first stated preference; update in place.

### `<state_root>/memory.md`

Observed markup facts. Suggested headings:

```markdown
## Boxes
- artifacts/<name>.md — when a reusable pattern is worth keeping

## Due
| item | next_date | note |

## Quirks
- YYYY-MM-DD | client/engine | symptom | fix

## Patterns
- YYYY-MM-DD | pattern | why it stuck
```

### `<state_root>/artifacts/`

Optional durable boilerplates and patterns. One file per artifact; link from `## Boxes`.

### Shared boxes

- `<domains_root>/domains.md` — one row per hostname; identity is the hostname. Fields: canonical host, www-vs-apex, locale→hostname, optional verified registrar/expiry. Update only rows this skill wrote; preserve foreign headers/rows.
- `<projects_root>/<project>.md` — markup decisions for a tracked project.
- `<profile_path>` — shared locale/language universals read after `config.yaml`.

## Write rules

1. Resolve roots before the first read/write; keep them fixed for the invocation.
2. Update only rows this skill owns in shared boxes; preserve foreign rows.
3. No credentials under state roots — store pointers (`env:…`, `keychain:…`, `1password:…`, `file:…`).
4. Name every write and deletion in one line as it happens.
5. Prefer blank shapes from `assets/memory-template.md` when creating a new file.
