# DNS Migration and TTL

## Pre-Migration TTL

- Lower TTL to 300s at least 48h before changing records—current TTL must expire first
- Check current cached TTL before planning: `dig +nocmd +noall +answer example.com`
- After migration stable 24h, raise TTL back to 3600-86400s
- Test with multiple resolvers: Google (8.8.8.8), Cloudflare (1.1.1.1), local ISP—they cache independently
