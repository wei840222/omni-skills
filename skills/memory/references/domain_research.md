# Memory Agent Systems & Context Management Research

## Vector Databases vs. Plain Files
Recent trends indicate that while plain Markdown files are extremely portable (like Obsidian), when the number of memories grows large, plain grep approaches hit limits with fuzzy recall. Integrating lightweight embedded vector stores (like Chroma or LanceDB) or using BM25 alongside Markdown is a common architectural pattern to bridge the gap.
For `memory`, keeping the baseline as plain text `<state_root>/` is optimal for portability, but the `scaling.md` guide correctly identifies that past 500 entries, naive string matching degrades.

## Hierarchical Memory Systems
Research on LLM agent memory (e.g., MemGPT) suggests a tiered memory approach:
1. Working context (session)
2. Episodic memory (conversational history)
3. Semantic/declarative memory (durable facts - which is what this skill provides)
It is a known best practice to explicitly instruct the agent on which tier to update, which `memory` implements by cleanly separating from the "built-in" session state.

## Trust and Expiration
A known pattern in long-term memory agents is the need to supersede or forget outdated facts (the "white bear" problem of obsolete data). The rule in `conflicts.md` (supersede rather than just archive) aligns with current research on maintaining trust in agentic semantic memory systems.

## Key Sources Consulted
- **Topic: LLM Agent Memory Architectures:** MemGPT and Hierarchical Context (https://arxiv.org/abs/2310.08560)
- **Topic: Markdown as durable knowledge:** Portable Knowledge Graphs in plain text (https://obsidian.md/about)
