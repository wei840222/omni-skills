## Common Traps

- **Auth format wrong** → Must be `email/token:API_TOKEN`, not just token
- **Searching with special chars** → URL-encode queries
- **Bulk updates failing** → Check rate limits, add 100ms delay
- **Missing ticket fields** → Some fields require specific plans
- **Pagination ignored** → Results capped at 100, use `next_page` URL

