## Self-Hosting

- Self-host when GDPR or first-party delivery requirements make CDN Google Fonts unacceptable, because visitor browsers otherwise request Google servers and expose IPs.
- Use `google-webfonts-helper` to download only the families, weights, and subsets you need.
- Declare `@font-face` with `font-display: swap` and serve the files from your origin or trusted CDN.
- Keep the fallback stack explicit so layout remains readable before custom fonts activate.
