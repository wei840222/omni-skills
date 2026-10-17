# Wiki.js Troubleshooting Guide

Check these failure modes before changing the host, database, or proxy.

## Connectivity and assets

- **Login redirect loops**: almost always Site URL scheme/host mismatch after
  HTTPS or domain changes. Set Site URL to the exact public URL browsers use
  (`https://docs.example.com`), including path prefix if any.
- **Assets fail to load / mixed content**: Site URL must match the access URL.
  If TLS terminates at nginx/Caddy, Wiki.js can stay on HTTP internally while
  Site URL remains `https://…`.

## Page management

- **404 right after create**: prefer lowercase alphanumeric path segments.
  Special characters and awkward casing commonly break routing; rewrite to a
  safe slug such as `/engineering/system-architecture-v1`.

## Performance

- **Slow after bulk import**: search reindex runs in the background. Check
  Admin → Utilities before assuming the node or database is unhealthy.
- **PostgreSQL search empty/odd**: confirm `pg_trgm` is available on the host
  (required for the PostgreSQL search module).

## Sources

- https://docs.requarks.io/install/config
- https://docs.requarks.io/install/requirements
- https://docs.requarks.io/groups
