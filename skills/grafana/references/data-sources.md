# Data Sources

- "Server" mode proxies through Grafana — hides credentials from browser
- "Browser" mode direct from browser — faster but exposes URL/auth
- Test connection catches most issues — but not query-specific problems
- TLS skip verify for self-signed — but fix proper certs for production

## Connection Troubleshooting

Use the data source connection test before debugging a panel query. A successful test verifies basic connectivity but not every query, permission, or time-range behavior; inspect the query response next. Use server-side access when credentials must remain outside the browser, and use a verified TLS certificate for production endpoints.

Source: [Grafana data source documentation](https://grafana.com/docs/grafana/latest/datasources/).
