# Conversation — rewrite before retrieve

**Load when** follow-up questions retrieve nonsense.

1. Resolve pronouns and ellipsis into a standalone query **before** embedding.
2. Do not embed the raw chat turn if it depends on prior entities.
3. Carry filter/tenant context from the session server-side; never trust the rewriter's output for permissions.
4. If the user changes topic, drop stale entities rather than stuffing the whole history into the query.
