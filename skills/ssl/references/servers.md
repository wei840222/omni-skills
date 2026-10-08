# TLS configuration by server

Prefer Mozilla [SSL Configuration Generator](https://ssl-config.mozilla.org/) profiles (`modern` = TLS 1.3 only; `intermediate` = TLS 1.2+1.3) when hardening ciphers. Snippets below focus on certificate paths and minimal safe listeners.

## Nginx

Modern Nginx enables HTTP/2 with the `http2` directive (not the legacy `listen ... http2` flag):

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    http2 on;
    server_name example.com www.example.com;

    ssl_certificate     /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;

    add_header Strict-Transport-Security "max-age=63072000" always;
}
```

Use `fullchain.pem` so intermediates are sent. After edits: `nginx -t && systemctl reload nginx`.

## Apache httpd 2.4

```apache
<VirtualHost *:80>
    ServerName example.com
    Redirect permanent / https://example.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName example.com

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/example.com/cert.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
    SSLCertificateChainFile /etc/letsencrypt/live/example.com/chain.pem

    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
</VirtualHost>
```

Some distributions expose a combined `SSLCertificateFile` pointing at fullchain; keep chain and leaf consistent with the package layout you actually deploy.

## Caddy

Caddy obtains and renews certificates automatically when the site address is HTTPS-capable:

```caddyfile
example.com {
    reverse_proxy localhost:3000
}
```

Custom material:

```caddyfile
example.com {
    tls /path/to/fullchain.pem /path/to/privkey.pem
    reverse_proxy localhost:3000
}
```

## Node.js / Express

```javascript
const https = require('https');
const http = require('http');
const fs = require('fs');
const express = require('express');

const app = express();
const options = {
  key: fs.readFileSync('/etc/letsencrypt/live/example.com/privkey.pem'),
  cert: fs.readFileSync('/etc/letsencrypt/live/example.com/fullchain.pem'),
};

https.createServer(options, app).listen(443);
http.createServer((req, res) => {
  res.writeHead(301, { Location: `https://${req.headers.host}${req.url}` });
  res.end();
}).listen(80);
```

## Traefik

```yaml
# static config excerpt
entryPoints:
  web:
    address: ":80"
    http:
      redirections:
        entryPoint:
          to: websecure
          scheme: https
  websecure:
    address: ":443"

certificatesResolvers:
  letsencrypt:
    acme:
      email: admin@example.com
      storage: /letsencrypt/acme.json
      httpChallenge:
        entryPoint: web
```

```yaml
# router labels
labels:
  - "traefik.http.routers.myapp.rule=Host(`example.com`)"
  - "traefik.http.routers.myapp.tls.certresolver=letsencrypt"
```

Protect `acme.json` permissions (`600`). See Traefik ACME docs for DNS/TLS challenge variants.

## HAProxy

```haproxy
frontend https_front
    bind *:443 ssl crt /etc/haproxy/certs/example.com.pem
    default_backend app_servers

frontend http_front
    bind *:80
    redirect scheme https code 301
```

HAProxy expects leaf + intermediates + key in one PEM:

```bash
cat fullchain.pem privkey.pem > /etc/haproxy/certs/example.com.pem
chmod 600 /etc/haproxy/certs/example.com.pem
```
