# Official Sources Map - Naming

Use these primary sources when verifying label clarity, API resource naming, accessibility of names, developer style defaults, or trademark caution. Prefer the full URL in PR notes and user-facing citations. This skill stays vendor-neutral: sources justify principles, not a mandatory brand system.

## Clarity, IA, and findability

- **Nielsen Norman Group — Menu Design Details** — short, distinctive labels and why vague category names hurt wayfinding via https://www.nngroup.com/articles/menu-design/
- **Nielsen Norman Group — Category Names That Suck** — concrete failures of clever or overly broad navigation labels via https://www.nngroup.com/articles/category-names-suck/
- **Nielsen Norman Group — Tree Testing: Fast, Iterative Evaluation of Information Hierarchies** — validating whether users can find items under proposed labels via https://www.nngroup.com/articles/tree-testing/

## Accessibility of names and labels

- **W3C WCAG 2.2** — accessible name, label, and consistent identification expectations for UI text via https://www.w3.org/TR/WCAG22/
- **W3C Understanding SC 2.4.6 Headings and Labels** — headings/labels describe topic or purpose via https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html
- **W3C Understanding SC 3.2.4 Consistent Identification** — same functionality uses consistent names via https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html

## Developer and product language defaults

- **Google Developer Documentation Style Guide — Word list** — preferred technical wording and terms to avoid in product/docs language via https://developers.google.com/style/word-list
- **Google Developer Documentation Style Guide — Text-formatting summary** — consistency habits that affect API, UI, and docs names via https://developers.google.com/style/highlights
- **Microsoft Writing Style Guide** — product-facing terminology patterns and plain-language defaults via https://learn.microsoft.com/en-us/style-guide/welcome/

## API and resource naming

- **RFC 3986 — Uniform Resource Identifier (URI)** — path segment semantics and stable resource identity via https://www.ietf.org/rfc/rfc3986.txt
- **JSON:API specification** — resource-type naming and relationship clarity conventions via https://jsonapi.org/format/
- **REST API Tutorial — Resource Naming** — plural nouns for collections, consistent hierarchy, and verb-in-path anti-patterns via https://restfulapi.net/resource-naming/

## Trademark and collision caution (non-legal advice)

- **USPTO — Trademark basics** — why public names need clearance thinking beyond internal cleverness via https://www.uspto.gov/trademarks/basics
- **WIPO — Trademarks** — international trademark concepts and dispute framing via https://www.wipo.int/amc/en/trademark/
- **Cornell LII — Lanham Act overview (15 U.S.C. ch. 22)** — US statutory backdrop for trademark risk language; not a substitute for counsel via https://www.law.cornell.edu/uscode/text/15/chapter-22

## How to use these sources in-session

- Cite the matching group when claiming UI clarity, API consistency, accessibility of labels, or trademark caution.
- Run live domain, package-registry, app-store, or trademark searches only after telling the user which check is starting.
- Treat style guides as defaults for consistency, not as a requirement to copy a single vendor voice.
- If the user’s jurisdiction, brand system, or existing taxonomy conflicts with a general heuristic, prefer the local system and record the constraint under `<state_root>/`.
