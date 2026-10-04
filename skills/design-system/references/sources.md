# Design System — Domain Sources

Verified full URLs for Gate 6 claims. Prefer these over memory.

| Topic | Source | Use |
|-------|--------|-----|
| Design Tokens Community Group | [W3C Design Tokens CG](https://www.w3.org/community/design-tokens/) | Official community home for cross-tool token standards work |
| DTCG Format Editor's Draft | [Design Tokens Format Module](https://www.designtokens.org/TR/drafts/format/) | Token file shape, types, and interchange expectations |
| Alternate DTCG draft host | [tr.designtokens.org/format](https://tr.designtokens.org/format/) | Same draft lineage; use when checking redirects / mirrors |
| Style Dictionary | [Style Dictionary](https://styledictionary.com/) | Multi-platform transform/export pipeline from a single token source |
| Style Dictionary docs (transforms) | [Style Dictionary documentation](https://styledictionary.com/info/) | Platform transforms, formats, and build configuration patterns |
| WCAG 2.2 contrast | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Contrast and non-text contrast floors when tokenizing color roles |
| Material Design 3 color roles | [Material Design 3 color system](https://m3.material.io/styles/color/system/overview) | Semantic role examples (primary, surface, error) — adapt, do not copy blindly |
| Apple HIG color | [Apple Human Interface Guidelines — Color](https://developer.apple.com/design/human-interface-guidelines/color) | Native semantic color and dark appearance considerations |
| Figma variables | [Figma variables guide](https://help.figma.com/hc/en-us/articles/15339698696087-Guide-to-variables-in-Figma) | Design-tool variable collections and mode theming handoff |

## Freshness notes

- DTCG format remains a **draft**; cite the draft URL and avoid claiming final W3C REC status.
- Style Dictionary APIs evolve; confirm transform/format names against current docs before generating configs.
- Accessibility contrast floors belong in semantic token definitions; do not hard-code product-specific brand hex as “accessible” without checking contrast pairs.
- Platform HIG and Material guidance are **examples of role systems**, not mandatory token names for every product.
