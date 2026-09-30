# AI Guidelines

Operational defaults for common AI engineering questions. Mutable numbers (price, VRAM, rank) must still be re-checked via `references/sources.md` before hard claims.

## Reduce hallucinations

Do not stop at “use RAG.” Specify a stack:

1. **Grounding** — retrieve from verified sources the user trusts; refuse when evidence is missing.
2. **Structured output** — JSON Schema / constrained decoding when the consumer needs machine-checkable fields.
3. **Low temperature** — use temperature `0` (or the provider’s deterministic setting) for factual extraction.
4. **Citations** — require source IDs or URLs in the system prompt and reject answers without them when stakes are high.
5. **Eval loop** — keep a small regression set of known Q/A pairs and re-run after prompt or model changes.

## RAG vs fine-tuning

- **Default to RAG** when facts change, sources must be cited, or the corpus is external documents.
- **Fine-tune** only when you need stable style, format, or domain vocabulary that retrieval repeatedly fails to supply — and you can own training data, evals, and drift monitoring.
- Hybrid is common: RAG for facts + light adapter for voice. Hand off deep design to `rag` or `fine-tuning`.

## Local hardware (order-of-magnitude)

Dense **FP16-class** VRAM ballparks often used in practitioner guides (not a guarantee; quantization, KV cache, context length, and framework overhead dominate):

| Params (approx.) | Ballpark VRAM (dense FP16-ish) |
| --- | --- |
| 7B | ~8–14 GB |
| 13B | ~16–28 GB |
| 70B | ~140 GB dense; **Q4-class quants** often land near ~35–48 GB+ depending on context and runtime |

Always:

- Prefer the model card / runtime docs for the exact quant and context.
- Treat “Q4 halves requirements” as a **rough** rule, not a law.
- For Ollama-specific install and GPU fallback, load `ollama`.

## Local vs API

**Prefer local (Ollama, LM Studio, etc.)** when privacy, offline, air-gap, or predictable unit cost at high volume matters and the user has suitable hardware.

**Prefer API** when the user needs frontier capability, has no GPU headroom, is prototyping, or must follow a provider SLA.

Re-check spend thresholds with the user’s actual token mix; do not treat a single dollar cutoff as universal.

## Token counting

English prose is often ~4 characters/token as a **coarse** intuition only. Code, non-English text, and special tokens vary widely.

When the user needs a real budget: count with `tiktoken`, the provider tokenizer, or the runtime’s token API — never ship a production limit from character division alone.

## Outages and “is the model broken?”

Before blaming user code or prompts, check the provider status page and recent rank/price moves that might indicate a model swap. See `references/sources.md`.