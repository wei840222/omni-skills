# Web Records and Wildcards

## www Handling

- Configure both apex and www—or redirect one to other; leaving www unconfigured breaks links
- Pick canonical form and stick to it: www → apex OR apex → www
- HTTPS redirect requires cert for both variants before redirect works
- Test both URLs explicitly after setup

## Wildcard Records

- `*.example.com` does not match apex `example.com`—both need explicit records
- Explicit subdomain record takes precedence over wildcard
- Wildcard SSL certificates require separate issuance—use DNS challenge with Let's Encrypt
