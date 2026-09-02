# Common Mistakes

- Storing sensitive data in payload—it's just base64, not encrypted
- Huge payloads—JWTs go in headers; many servers limit header size to 8KB
- No expiration—indefinite tokens are security nightmares
- Same secret across environments—dev tokens work in production
- Logging tokens—they're credentials; treat as passwords
