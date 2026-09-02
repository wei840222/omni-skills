# Storage

- httpOnly cookie: immune to XSS, but needs CSRF protection
- localStorage: vulnerable to XSS, but simpler for SPAs
- Memory only: most secure, but lost on page refresh
- Keep tokens out of URL parameters—visible in logs, history, referrer headers
