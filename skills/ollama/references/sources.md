# Sources - Ollama

Verified public anchors used for Gate 6 domain refresh. Prefer live CLI inspection (`ollama list`, `ollama show`, `ollama ps`) over stale memory.

## Official product and API

- **Ollama docs home** — install, run, and product overview via https://ollama.com/
- **Ollama GitHub repository** — releases, issues, and runtime source via https://github.com/ollama/ollama
- **Modelfile reference** — FROM / PARAMETER / SYSTEM / ADAPTER syntax via https://github.com/ollama/ollama/blob/main/docs/modelfile.md
- **OpenAI compatibility** — `/v1` chat and embeddings mapping notes via https://github.com/ollama/ollama/blob/main/docs/openai.md
- **API endpoints** — `/api/generate`, `/api/chat`, `/api/embeddings`, `/api/show` via https://github.com/ollama/ollama/blob/main/docs/api.md

## Local operations practice

- Bind to localhost by default; treat `OLLAMA_HOST=0.0.0.0` / port `11434` exposure as an explicit trust-boundary change with no native auth.
- Pin exact model tags for reproducible work; inspect real context/quant/capabilities with `ollama show` before claiming them.
- Tune context, batching, and keep-alive before assuming a hardware upgrade is required.

## Obsolete knowledge corrected in this refactor

- Removed clawic.com homepage, feedback, and install promo loops.
- Replaced hard-coded `~/Clawic/data/ollama/` with portable `<state_root>` resolution.
- Deleted `_meta.json` package registry metadata.
