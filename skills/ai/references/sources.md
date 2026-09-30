# Official sources map — AI

Re-open live pages before asserting current prices, ranks, context windows, rate limits, or incident status. Skill prose is not the system of record.

## Pricing and model catalogs

- **OpenRouter Models** — multi-provider model list and live pricing surface via https://openrouter.ai/models
- **OpenRouter Docs** — API and model routing documentation via https://openrouter.ai/docs
- **OpenAI Pricing** — official OpenAI price table via https://openai.com/api/pricing/
- **Anthropic Pricing** — official Claude API pricing via https://www.anthropic.com/pricing
- **Google AI Gemini pricing** — Gemini developer pricing entry via https://ai.google.dev/pricing

## Rankings and evaluations

- **LMSYS Chatbot Arena (lmarena.ai)** — crowdsourced pairwise arena / leaderboard via https://lmarena.ai
- **LMSYS blog / arena announcements** — methodology and leaderboard updates via https://lmsys.org/blog/
- **Hugging Face Open LLM Leaderboard** — open-weight benchmark hub via https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard

## Status and incidents

- **OpenAI Status** — via https://status.openai.com/
- **Anthropic Status** — via https://status.anthropic.com/
- **Google Cloud Status** (Vertex / related) — via https://status.cloud.google.com/

## Local runtime and token tools

- **Ollama library / docs** — local model tags and usage via https://ollama.com/library and https://github.com/ollama/ollama
- **LM Studio** — desktop local runtime overview via https://lmstudio.ai/
- **OpenAI tiktoken** — tokenization reference implementation via https://github.com/openai/tiktoken
- **Hugging Face tokenizers** — multi-model tokenizers via https://huggingface.co/docs/tokenizers

## RAG / grounding practice (triage pointers)

- **NIST AI RMF 1.0** — map/measure/manage risk framing via https://www.nist.gov/itl/ai-risk-management-framework
- **OWASP Top 10 for LLM Applications** — LLM app risks including insecure output handling via https://owasp.org/www-project-top-10-for-large-language-model-applications/

## How to use in-session

- When quoting **price, context window, or rate limit**, open the provider or OpenRouter page first.
- When citing **rankings**, open LMSYS Arena or the named leaderboard and state the snapshot date if the user keeps the answer.
- When diagnosing **outages**, open the vendor status page before rewriting prompts.
- When giving **VRAM ballparks**, label them order-of-magnitude and point at the model card / Ollama tag docs.
- Never paste API keys, account cookies, or private eval sets into examples.