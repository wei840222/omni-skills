# Common Traps — Authorization

- Checking roles instead of permissions → brittle when roles change
- OR logic in permissions → "can edit OR is admin" creates backdoors
- Caching permissions too long → stale grants after role changes
- Frontend-only checks → always verify server-side
- God roles → split "admin" into specific permission sets
- Circular inheritance → A inherits B inherits A crashes system
