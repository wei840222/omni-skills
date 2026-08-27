## Database Practices

- Connection pooling: reuse connections—creating is expensive
- Transactions scoped minimal—hold locks briefly
- Read replicas for read-heavy workloads—separate read/write traffic
- Prepared statements always—SQL injection prevention, query plan cache
