# Data Sources

- "Server" mode proxies through Grafana — hides credentials from browser
- "Browser" mode direct from browser — faster but exposes URL/auth
- Test connection catches most issues — but not query-specific problems
- TLS skip verify for self-signed — but fix proper certs for production
