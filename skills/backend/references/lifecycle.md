## Health Checks

- Liveness: is process running—restart if fails
- Readiness: can handle traffic—remove from load balancer if fails
- Startup probe for slow-starting services—don't kill during init
- Health checks fast and cheap—don't hit database on every probe

## Graceful Shutdown

- Stop accepting new requests first—drain load balancer
- Wait for in-flight requests to complete—with timeout
- Close database connections cleanly—prevent connection leaks
- SIGTERM handling: graceful; SIGKILL after timeout
