---
name: compress
description: Compress text semantically with progressive levels, format-specific strategies, and anchor validation so prompts stay shorter and recall stays sharper. Use when minimizing prompt length, fighting lost-in-the-middle recall on long contexts, or preparing system instructions for repeated reuse. Prefer `summarizer` when the deliverable is a reader-facing summary of a source; prefer `prompting` when the task is diagnosing or iterating a failing prompt rather than shrinking known text.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🗜️"}'
  related-skills: '{"prompting":"Diagnose and iterate a failing prompt instead of only shrinking text.","summarizer":"Produce a reader-facing summary of a source rather than a reusable compressed prompt artifact."}'
---

## Scope

Semantic compression preserves meaning under a reconstruction check. It is not bit-perfect lossless storage.

- L1–L2: production-ready when anchors validate
- L3–L4: experimental denser encodings; review output before reuse
- Keep medical dosages, legal text, financial figures, and other safety-critical values in the original form or an explicitly verified excerpt

## Validation loop

```
1. Compress original O → compressed C
2. Extract anchors from O (entities, numbers, dates, quoted identifiers)
3. Reconstruct C → R without seeing O
4. Verify anchors match and semantic diff is acceptable
5. If mismatch → restore only the missing pieces into C
6. Repeat until validated (max 3 iterations)
```

Convergence means verified. No convergence after 3 rounds means the chosen level is too aggressive—drop one level and retry.

## On-demand references

Load only what the current task needs:

- `references/levels.md` — choose L1–L4 intensity and when each level fits
- `references/validation.md` — run the anchor validation / reconstruction loop
- `references/formats.md` — strategies for code, Markdown, JSON, or conversations
- `references/metrics.md` — token ratios, break-even math, and cost reporting
- `references/sources.md` — pinned research and specification sources for claims in this skill

## Compression levels

| Level | Ratio | Reliability | Use case |
|-------|-------|-------------|----------|
| L1 | ~0.8x | High | Production, still human-readable |
| L2 | ~0.5x | Good | System prompts and repeated reuse |
| L3 | ~0.3x | Moderate | Experimental; review before reuse |
| L4 | ~0.15x | Low | Research densification; expect losses |

## Anchor checksum

Before compressing, extract critical facts:

```
[ANCHORS: 3 people, $42,000, 2024-03-15, "Project Alpha"]
```

Reconstruction must reproduce these exactly. Anchor mismatch means the compression failed.

## Context scaling

Large context windows do not remove the need for compression. Models still show weaker recall for facts buried mid-context, and each token still costs latency and money. Compress to tighten the working set and raise retrieval accuracy, not only to fit a hard limit.

## Core rules

1. Validate with reconstruction before trusting a compressed artifact
2. Extract numbers, names, dates, and quoted identifiers as anchors first
3. Prefer L1–L2 for production reuse; treat L3–L4 as experimental
4. Report confidence with iteration count and anchor match rate
5. Prefer an independent model for reconstruction when stakes are high

## Cost-benefit

Each compression typically costs 3–4 LLM calls. Break-even:

```
break_even_retrievals = compression_tokens / saved_tokens_per_use
```

Compression pays off when the compressed artifact will be retrieved about 6–8+ times. For one-shot text, keep the original.

## Before compressing

- [ ] Content is outside the safety-critical exclusions above, or critical values stay verbatim
- [ ] Target level chosen (L1–L2 recommended for production)
- [ ] Anchors identified (numbers, names, dates, quoted identifiers)
- [ ] ROI makes sense (multiple retrievals expected)
