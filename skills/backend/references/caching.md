## Caching Strategy

- Cache invalidation strategy decided upfront—TTL, event-based, or both
- Cache at right layer: query result, computed value, HTTP response
- Cache stampede prevention—lock or probabilistic early expiration
- Monitor hit rate—low hit rate = wasted resources
