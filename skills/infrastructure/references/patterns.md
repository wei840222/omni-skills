# Architecture Patterns by Stage

## MVP Stage (<1K users, <$50/month)

```
┌─────────────────────────────────┐
│         Single VPS              │
│  ┌─────────┐  ┌─────────┐      │
│  │   App   │  │   DB    │      │
│  │ (Docker)│  │(Postgres)│     │
│  └─────────┘  └─────────┘      │
│         Caddy (reverse proxy)   │
└─────────────────────────────────┘
```

**Setup:**
- One VPS (Hetzner CAX11 €4/mo or equivalent)
- Docker Compose for app + db
- Caddy for auto-SSL and reverse proxy
- Daily pg_dump to S3/B2

**When to upgrade:** CPU consistently >70%, RAM consistently >80%, or need zero-downtime deploys.

---

## Growth Stage (1K-50K users, $50-500/month)

```
┌─────────────┐     ┌─────────────┐
│  App Server │     │  DB Server  │
│  (Docker)   │────▶│ (Managed or │
│  + Caddy    │     │  dedicated) │
└─────────────┘     └─────────────┘
       │
       ▼
┌─────────────┐
│   Workers   │ (background jobs, optional)
└─────────────┘
```

**Changes from MVP:**
- Separate database (managed recommended: Supabase, Neon, or dedicated VPS)
- Optional: worker server for background jobs
- Add monitoring (Uptime Kuma self-hosted or external)
- Automated backups with retention policy

**When to upgrade:** Need high availability, multiple app instances, or geographic distribution.

---

## Scale Stage (50K+ users, $500+/month)

```
                    ┌─────────────┐
                    │     CDN     │
                    │ (Cloudflare)│
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ Load Balancer│
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           │               │               │
    ┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
    │  App Node 1 │ │  App Node 2 │ │  App Node 3 │
    └─────────────┘ └─────────────┘ └─────────────┘
           │               │               │
           └───────────────┴───────────────┘
                           │
                    ┌──────▼──────┐
                    │ DB Cluster  │
                    │ (Primary +  │
                    │  Replicas)  │
                    └─────────────┘
```

**Changes from Growth:**
- Load balancer (cloud-native or HAProxy)
- Multiple app nodes (auto-scaling optional)
- Database replication (read replicas)
- CDN for static assets
- Full observability stack (Prometheus + Grafana or managed)
- Multi-region for latency-sensitive apps

---

## Core Practices

| Core Practice | Rationale | Recommended Approach |
|--------------|--------------|-----------------|
| Simple Orchestration | Operational overhead kills velocity | Use Docker Compose until orchestration is strictly required |
| Monolith First | Distributed debugging is hard | Build a modular monolith, split later |
| Single Cloud Focus | Double complexity yields little benefit | Pick one provider and maintain an exit plan |
| Right-sizing | Over-provisioning wastes resources | Start small and scale up as needed |
| Automated Backups | One mistake can cause data loss | Automate backups from day 1 |
