# Advanced — structured, multimodal, agentic

**Load when** text retrieval cannot answer the question class.

## Structured / SQL / graph

- Numbers from tables or databases: route to SQL or a warehouse query; text RAG cannot aggregate reliably.
- Graph RAG helps multi-hop relational questions ("who approved every exception in Q3") and adds an extraction pipeline you must re-run as documents change. Use when questions are genuinely relational, not merely multi-part.

## Multimodal

- Images/charts/slides: caption-and-index versus a native multimodal embedding. Pick one fingerprint and stick to it.

## Agentic retrieval

- Decompose → retrieve per sub-question → verify → retry within a budget.
- Do not make every easy query pay for the hardest loop; route by complexity.
