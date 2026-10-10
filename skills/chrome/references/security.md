# Security contexts for Chrome debugging advice

## Secure context

Many powerful web APIs (Clipboard write, File System Access, and others) require a [secure context](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts): typically HTTPS or localhost, often plus a user gesture.

Check `window.isSecureContext === true` before blaming the API.

## Mixed content

HTTPS documents cannot freely load active HTTP subresources. Compare `location.protocol` with resource URLs. MDN: https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content

## CORS

Cross-origin `fetch` failures often surface as generic `TypeError` in page JS. Read the Network panel / CORS error detail rather than inventing a root cause. MDN: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS

## CDP trust

Anyone who can speak CDP to a browser profile can instrument that profile. Do not expose remote debugging ports on untrusted networks; do not paste cookies or tokens into skill state.
