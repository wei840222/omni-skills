# SSL troubleshooting

## Diagnostic commands

```bash
# Full handshake + chain (quit after print)
openssl s_client -connect example.com:443 -servername example.com </dev/null

# Dates + identity
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -dates -subject -ext subjectAltName

# Full decoded leaf
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -text -noout

# Protocol probes
openssl s_client -connect example.com:443 -servername example.com -tls1_2 </dev/null
openssl s_client -connect example.com:443 -servername example.com -tls1_3 </dev/null

# Cipher inventory (when nmap NSE is available)
nmap --script ssl-enum-ciphers -p 443 example.com
```

Always pass `-servername` (SNI) for name-based virtual hosts.

## Incomplete certificate chain

**Symptoms:** Chrome OK, curl/wget fail; `unable to verify the first certificate`.

**Check**

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null
# Verify return code: 21 (unable to verify the first certificate) → chain gap
```

**Fix:** Configure the server to send intermediates. Let's Encrypt layouts: use `fullchain.pem` rather than leaf-only `cert.pem`. Reload and re-run until return code is `0 (ok)`.

## Certificate expired

**Symptoms:** `NET::ERR_CERT_DATE_INVALID`, padlock error, clients reject `notAfter`.

**Check**

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -dates
```

**Fix**

```bash
certbot renew
# only when intentionally replacing a stuck lineage:
certbot certonly --nginx -d example.com --force-renewal
systemctl reload nginx   # or the actual unit for this host
```

## Hostname mismatch

**Symptoms:** `SSL_ERROR_BAD_CERT_DOMAIN`, certificate not valid for requested resource.

**Check**

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -subject -ext subjectAltName
```

**Fix:** Re-issue with every name clients type (apex, `www`, API hosts). Wildcard covers one label only (`*.example.com` does not cover `example.com` itself).

## Mixed content

**Symptoms:** Console mixed-content warnings; partial asset blocks; broken padlock.

**Fix**

1. DevTools → Console / Network to list `http://` subresources.
2. Switch those URLs to `https://` (or root-relative / `//` only when both schemes are intentional).
3. Optionally send `Content-Security-Policy: upgrade-insecure-requests` while cleaning stragglers.

## Renewal failing

**Check**

```bash
certbot renew --dry-run
sudo tail -n 200 /var/log/letsencrypt/letsencrypt.log
```

**Common causes**

- Port 80 closed or wrong vhost for HTTP-01
- DNS not pointing at the challenge responder (HTTP-01 / DNS-01)
- Stale ACME client; prefer current certbot from distro or eff docs
- Server config fails `nginx -t` / `apachectl configtest` so reload never picks new files
- Production rate limits while testing — switch to staging

## Permission denied reading keys

**Symptoms:** web server error log shows permission denied on `privkey.pem` / `acme.json`.

**Fix**

```bash
# illustrative Let's Encrypt layout — adjust group to the unit's runtime user
chmod 644 /etc/letsencrypt/live/example.com/fullchain.pem
chmod 600 /etc/letsencrypt/live/example.com/privkey.pem
# ensure the master process user can traverse /etc/letsencrypt/live and read the key
```

Never chmod private keys world-readable to "make it work."
