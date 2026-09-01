# Security & Privacy

This skill is documentation: endpoint reference, auth patterns, and example requests for the external services listed above. Example endpoints belong to the respective providers (Stripe, OpenAI, etc.).

It does NOT:
- Store or manage API keys or secrets — it references env-var names; values are kept out of logs and output
- Make API calls on its own — the user runs the requests
- Send data to any external service

Guardrails:
- Credential discovery lists variable NAMES, exclude values (`references/credentials.md` Selection Rules)
- Sandbox/test credentials by default; live keys only on explicit user request
- Generated webhook handlers always verify signatures before parsing the payload
