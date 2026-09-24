# Debugging and Provider Specifics

## Debugging Commands

- `dig +trace example.com`—full resolution chain from root; reveals where problem occurs
- `dig @ns1.provider.com example.com`—query authoritative nameserver directly, bypasses cache
- Compare authoritative vs cached response—mismatch indicates propagation in progress
- Check all relevant record types—A working doesn't mean AAAA, MX, or TXT are correct

## Cloudflare Proxy Behavior

- Orange cloud (proxied) hides origin IP—breaks SSH, mail, game servers; use grey cloud for non-HTTP
- Proxied records ignore your TTL setting—Cloudflare controls caching
- CNAME flattening at apex works in Cloudflare but causes confusion when migrating away
- Universal SSL only on proxied records—DNS-only requires origin certificate
