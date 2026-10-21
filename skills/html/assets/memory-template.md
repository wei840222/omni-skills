# Memory templates — html

Copy these shapes only after consent to create durable state. Replace placeholders; do not commit filled user data into the skill package.

## `<state_root>/config.yaml`

```yaml
markup_flavor: html
browser_support: widely-available
a11y_target: wcag-aa
document_lang: en
structured_data: json-ld
inline_code_policy: allowed
untrusted_html: escape
email_client_floor: outlook-desktop
output_shape: fragment
```

## `<state_root>/memory.md`

```markdown
## Boxes
<!-- path — when to open -->

## Due
| item | next_date | note |
| --- | --- | --- |

## Quirks
<!-- YYYY-MM-DD | client/engine | symptom | fix -->

## Patterns
<!-- YYYY-MM-DD | pattern | why it stuck -->
```

## `<domains_root>/domains.md`

```markdown
| hostname | canonical | www_policy | locale_map | notes |
| --- | --- | --- | --- | --- |
| example.com | https://www.example.com | www | en→www.example.com | |
```
