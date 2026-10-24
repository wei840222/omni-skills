---
name: hosting
description: Choose and operate web hosting for websites and applications. Use when users need to select a host, deploy a project, configure a domain or DNS, plan backups, or migrate hosting without managing a server.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌍"}'
---

# Web Hosting Guidance

## Start Here

1. Classify the workload: static site, application backend, WordPress/PHP, or e-commerce.
2. Match the provider and region to the workload, expected traffic, and operational skill level.
3. Before production, verify the deployment, HTTPS, backup scope, restore procedure, and billing limits.

Use managed hosting for people who do not want to administer servers. Use a VPS only when its operational responsibility is intentional and supported.

## Hosting Choices

- **Static site:** Vercel, Netlify, Cloudflare Pages, or GitHub Pages are suitable for HTML, CSS, and JavaScript sites.
- **Application backend:** Railway, Render, or Fly.io can operate application services without direct server administration.
- **WordPress or PHP:** Use managed WordPress hosting or conventional shared hosting when its constraints fit the application.
- **E-commerce:** Prefer Shopify or a platform designed for payments; confirm payment-security and compliance responsibilities before launch.

## Common Constraints

- Shared-hosting “unlimited” plans have fair-use limits. Check the terms, SSH access, cron/background-process policy, and performance limits before choosing one.
- Keep the application and database in nearby regions to reduce latency. Serverless database access often needs connection pooling.
- Treat preview deployments as a release checkpoint before production.
- Store deployment secrets in the platform’s managed secret configuration, not in the repository.

## Checkpoint Before Production

Confirm all of the following before moving traffic:

- [ ] The domain points to the intended service and HTTPS succeeds.
- [ ] The backup covers both files and data, has a documented retention period, and a restore has been tested.
- [ ] Usage, bandwidth, build, and function limits match the expected workload.
- [ ] The rollback and migration overlap plan is documented.

## Load Detailed Guidance

| Situation | Read |
|---|---|
| Comparing platform hosts, databases, free-tier limits, and portability | `references/providers.md` |
| Configuring DNS, email, backups, billing, or a migration | `references/operations.md` |

## Avoid These Failure Modes

- Do not select hosting on price alone; support, recovery, and usage limits matter when a service fails.
- Do not direct email through a web host by default; use a dedicated mail provider when reliability matters.
- Do not assume a provider backup is recoverable; verify scope, retention, and restoration first.
- Do not add orchestration complexity to a small site without a concrete operational need.
