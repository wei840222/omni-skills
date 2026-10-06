# CDN Best Practices

## Cache-Control Checklist

Before deploying, verify:
- [ ] Hashed assets (JS/CSS) → `Cache-Control: public, max-age=31536000, immutable`
- [ ] HTML pages → Short TTL or `no-cache` with revalidation
- [ ] Images → Long TTL with content-based URLs or versioning
- [ ] API responses → Usually `no-store` unless explicitly cacheable
- [ ] User-specific content → `private` or `no-store`

## Security Checklist

- [ ] TLS 1.2+ enforced, weak ciphers disabled
- [ ] HSTS enabled with appropriate max-age
- [ ] Origin IPs hidden, authenticated origin pulls configured
- [ ] Rate limiting on sensitive endpoints (login, API)
- [ ] Security headers: CSP, X-Frame-Options, X-Content-Type-Options

## Common Mistakes

- Serving user-specific responses (auth tokens, personalized content) from shared edge cache
- Using `max-age` without `immutable` for versioned assets
- Defaulting to full-cache purge when a path or tag purge would suffice
- Ignoring `Vary` headers (cache poisoning risk)
- Leaving origin open to direct public access (CDN controls skipped)

## Decision: Do I Need a CDN?

Ask about:
- Geographic distribution of users
- Current page load times and Core Web Vitals
- Static vs dynamic content ratio
- Traffic volume and patterns

If users are mostly local and traffic is low → CDN may add complexity without benefit.
If global users OR heavy static assets OR need DDoS protection → CDN adds value.
