## Timeouts Everywhere

- Database queries: set timeout, typically 5-30s
- External HTTP calls: connect timeout + read timeout—don't wait forever
- Overall request timeout—gateway or middleware level
- Background jobs: max execution time—prevent zombie processes

## Retry Patterns

- Exponential backoff: 1s, 2s, 4s, 8s...—prevents thundering herd
- Add jitter: randomize delay—prevents synchronized retries
- Idempotency keys for non-idempotent operations—safe to retry
- Circuit breaker for failing dependencies—stop hammering, fail fast

## Circuit Breaker Implementation Guidance

- Implement standard states: Closed (normal), Open (failing, return error immediately), Half-Open (testing recovery).
- Base Open state transition on a configurable failure rate threshold over a sliding window (e.g., 50% failure rate over 100 requests).
- Use a dedicated thread pool or semaphore for dependencies to prevent thread starvation during cascading failures.
- Recommended wait time in Open state before transitioning to Half-Open: 5 to 60 seconds, potentially with exponential backoff.
