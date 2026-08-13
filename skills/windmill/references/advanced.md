## Official Reference Routing

Read the matching official Windmill documentation before applying an advanced configuration. Platform behavior can vary by deployment and version.

- **Python scripts and dependencies:** https://www.windmill.dev/docs/getting_started/scripts_quickstart/python
  - Scripts use a `main` entrypoint; its signature drives the generated input schema.
  - Windmill resolves Python dependencies from top-level imports.
- **Flow architecture and data exchange:** https://www.windmill.dev/docs/flows/architecture
  - Sequential modules run in order; explicit parallel branches are queued together.
  - Use `results.{id}` in an input transform to consume an earlier step result.
  - Use workspace resources or states only when data must persist beyond one flow execution.
- **Variables, secrets, and permissions:** https://www.windmill.dev/docs/core_concepts/variables_and_secrets
  - Use a secret variable for sensitive values and grant access through the intended path and permissions.
  - Do not log secret values; job logs mask tracked secret values, but scripts should still avoid exposing them.

## Safe Delivery Checks

1. Test each script with representative inputs before composing it into a flow.
2. Confirm the workspace path, execution trigger, and required permissions before deploying a script, flow, variable, or secret.
3. For schedules, webhooks, concurrency, worker topology, or external exposure, read the official documentation for that exact feature and verify the deployment's version and settings.
