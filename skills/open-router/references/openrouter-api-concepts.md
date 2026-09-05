# OpenRouter API Concepts

OpenRouter provides an OpenAI-compatible API for requests to supported models and providers. Authenticate with an `Authorization: Bearer` header containing the locally managed `OPENROUTER_API_KEY`.

## Routing controls

Select a model in the request. When provider selection matters, use the current OpenRouter provider-routing documentation to construct the request; provider availability and supported routing parameters are mutable.

## Failure handling

Use the models endpoint to inspect currently available models before pinning a route. For rate limits, timeouts, or provider outages, apply a verified fallback policy from `references/fallback-reliability.md`; do not assume a client accepts an arbitrary array of model IDs as a fallback mechanism.

Sources: https://openrouter.ai/docs/api-reference/overview and https://openrouter.ai/docs/guides/routing/provider-routing
