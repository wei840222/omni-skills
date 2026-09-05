# Setup — OpenRouter

Load this reference for first-time configuration or when activation boundaries are unknown.

1. Resolve `<state_root>` using `SKILL.md`; do not create it until the user authorizes persistent state.
2. Capture only decisions that change routing: client API compatibility, workload classes, latency and quality targets, fallback tolerance, and budget limits.
3. Store activation boundaries, verified models, routing policy, and incidents in the corresponding `<state_root>/` files.
4. Verify credentials with the minimal request in `auth-and-provider.md` before applying a live routing policy.

Keep changes small and reversible: update either model selection, fallback policy, or budget limits in one iteration, then record the observed result.
