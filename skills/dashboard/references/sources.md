# Data Sources by Use Case

Patterns only — verify provider docs and auth models before coding field names.

## Business / SaaS metrics

- **Stripe / Paddle:** balance, customers, subscriptions, invoices via official APIs; MRR/churn usually need subscription + invoice aggregation or a metrics export, not the balance endpoint alone
- **Product analytics:** Mixpanel, Amplitude, PostHog, Google Analytics exports/APIs
- **CRM:** HubSpot, Pipedrive pipeline snapshots
- **Custom DB:** read-only PostgreSQL/MySQL queries the user authorizes

## Infrastructure / DevOps

- **Containers:** `docker stats`, compose status, restart counts
- **Servers:** CPU, RAM, disk via SSH or a metrics agent the user runs
- **CI/CD:** GitHub Actions / GitLab pipeline status APIs
- **Logs:** container stdout/stderr or app log tails the user permits
- **Monitoring:** Prometheus/HTTP metrics endpoints when available (optional)
- **TLS:** certificate expiration checks the user schedules

## IoT / home automation

- **Home Assistant:** REST or WebSocket with a user-provided long-lived token
- **Sensors:** temperature, humidity, motion, contact
- **Energy:** meter readings the user exports or exposes
- **Cameras:** snapshot URLs the user owns (no credential embedding in HTML)

## Financial / trading

- **Exchanges:** user-supplied API keys with least privilege
- **Brokers:** only where an API exists and the user opts in
- **On-chain:** public address balances; never request seed phrases
- **Price feeds:** CoinGecko, Yahoo Finance, or user-chosen market data
- **Manual entry:** CSV for assets without APIs

## Content creator

- **YouTube / social:** official analytics APIs or exported CSVs
- **Monetization:** AdSense/sponsorship tracking (often manual)

## Universal

- **CSV upload:** manual or exported datasets
- **Google Sheets:** user-authorized live reads
- **REST endpoints:** generic JSON the user can authenticate
- **Webhooks:** push into a local collector the user hosts
