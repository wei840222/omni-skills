# Core Routing Rules

1. Classify the workload before choosing a model: coding, analysis, extraction, summarization, or long-context synthesis.
2. Define a primary route, a fallback trigger, and a fallback route before changing defaults.
3. Keep authentication explicit and verify it with a minimal request before changing a live policy.
4. Set cost ceilings before increasing throughput; reserve premium models for high-impact work.
5. Validate one routing-layer change at a time with representative prompts, then record the result under `<state_root>/`.

## Common mistakes

- A single model for every workload can increase cost and make quality failures harder to isolate.
- Same-provider fallbacks can fail together during provider incidents.
- Changing model choice and budget rules together prevents clear diagnosis.
- Skipping verification defers routing failures to user-facing traffic.
