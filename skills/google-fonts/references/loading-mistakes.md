## Loading Mistakes

- Include `display=swap` on the Google Fonts CSS URL so text stays visible while fonts load.
- Load only the exact weights used (for example `wght@400;600;700`); each unused static weight adds payload.
- Add both preconnect hints before the stylesheet:
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  ```
- Prefer the CSS2 API form and keep family/axis parameters explicit rather than copying oversized catalog defaults.
