# Software strings, catalogs, and ICU

Load when translating UI catalogs, placeholders, plurals, or expansion budgets.

## Placeholders are payload

Preserve placeholder **set, count, and names**. When target word order changes, prefer positional forms (`%1$s`, `{0}`) over reordering bare `%s`.

Supported families commonly seen in catalogs:

- ICU MessageFormat / FormatJS
- printf / Posix
- Mustache / Handlebars
- i18next

One user-visible message equals one string. Building sentences by concatenating `"Deleted " + n + " items"` freezes English word order and hides agreement required by many languages.

## Plural categories from CLDR

Use CLDR plural categories for the **target** locale, not a mirror of English `one/other`.

Examples (confirm on the live CLDR chart before shipping):

- English: `one`, `other`
- Russian / Polish / Czech: additional few/many distinctions
- Arabic: up to six categories
- Japanese / Chinese / Korean / Thai / Vietnamese: typically `other` only

Exact-zero marketing copy uses an `=0` exact match when needed; do not invent a CLDR `zero` category merely because the count is 0 in English.

Primary references:

- https://cldr.unicode.org/index/cldr-spec/plural-rules
- https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
- https://formatjs.io/docs/core-concepts/icu-plurals/

## Expansion planning

Short English UI strings expand most in translation. Re-check live W3C text-size guidance when quoting budgets; treat legacy IBM globalization tables as historical defaults, not immutable law.

Practical planning posture before layout freeze:

- Very short labels need the largest spare capacity
- German / Finnish / Russian often sit toward the high end of expansion
- CJK often contracts in characters but needs more line height and font coverage

Primary reference: https://www.w3.org/International/articles/article-text-size/

## Catalog hygiene

- Prefer semantic keys plus `msgctxt` / translator comments over English-text keys
- Group work by screen/feature before alphabetical sweeps
- Report catalogs whose keys are the English source string as a maintainability defect
