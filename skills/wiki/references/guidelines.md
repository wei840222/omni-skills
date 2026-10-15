# Wiki Guidelines

## Writing

- Write for **zero-context readers** — define terms or link the defining page on first use.
- Write procedures as **numbered steps**, not narrative paragraphs.
- Include **examples** (and diagrams when the host supports them). A wiki without examples is a glossary.
- Mark uncertain content explicitly with `[needs verification]` or `[outdated]`.
- Prefer imperative mood and present tense for procedures.

## Linking and organization

- Cross-link aggressively — every mention of another concept should link to its page when the page exists.
- Use categories/tags for discoverability beyond the link graph (host-dependent; see `sources.md`).
- Create **redirect pages** (or host-native redirects) when renaming — never leave broken inbound links.
- Maintain link integrity when restructuring; grep for old titles/paths before deleting a page.

## Content maintenance

- When updating a fact, update **all** pages that reference it (search the wiki corpus).
- Maintain a changelog or "recently updated" page for team visibility.
- Run regular content audits — mark outdated information before it misleads.
- Enforce consistent formatting and section order across contributors (same template).
- Delete or archive orphaned pages that no longer have inbound links or a map entry.

## Anti-patterns

- Walls of text without headings or steps
- "See X" with no link
- Renaming without a redirect
- Assuming readers already know the house jargon
- Mixing product-doc Diátaxis architecture into a wiki without saying so — hand that to `documentation`
