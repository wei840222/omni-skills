# Launch checklist

Load before shipping or when auditing “is this production-ready?”

## Must-pass items

- [ ] Primary forms submit and show success/error states
- [ ] Custom 404 exists and links back to home/search
- [ ] Favicon present (at least one real icon; no endless 404)
- [ ] `<html lang>` set; document `title` unique per key template
- [ ] HTTPS only; no active mixed content
- [ ] Open Graph (and Twitter/X card if relevant) preview verified
- [ ] `robots.txt` and XML sitemap coherent; sitemap submitted when Search Console is in use
- [ ] Uptime or synthetic check on the production origin
- [ ] Analytics/consent tags load without breaking content

## Content and SEO basics (not a full SEO campaign)

- Unique titles and meta descriptions on indexable templates
- Canonical URL strategy clear (www vs apex)
- Internal links reach important pages; no accidental `noindex` on money pages
- For ranking drops, migrations, or keyword programs → hand off to `seo`

## Security hygiene (site level)

- External `target="_blank"` uses `noopener`
- No secrets in client HTML/JS
- Dependency/third-party tags reviewed for necessity
- Cookie/consent banners do not block keyboard access to the page

## Sign-off note

Record what was tested (device/browser), Lighthouse/a11y highlights, and any accepted risk. Prefer a short evidence list over “looks fine”.
