## Rate Limiting

- Per-user/IP limits on expensive operations—login, signup, search
- Different limits for different operations—read vs write
- Return Retry-After header—tell clients when to retry
- Rate limit early in request pipeline—save resources
