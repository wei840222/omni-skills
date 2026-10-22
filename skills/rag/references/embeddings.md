# Embeddings — fingerprint first

**Load when** scores collapse after a model swap, or long chunks silently truncate.

## Fingerprint (must match query side)

1. embedding model id
2. model version / revision
3. output dimension
4. normalization
5. instruction prefix
6. distance metric

Write them to `## Index Registry` in `<state_root>/memory.md` at build time.

## Practical defaults

- Hosted default: OpenAI `text-embedding-3-small` at **1536** dims unless the user forbids data egress (`references/sources.md`).
- Asymmetric models: E5 uses `query: ` / `passage: `; BGE adds a query instruction and **no** passage instruction.
- A model change is a full reindex (blue-green), never an in-place overwrite of mixed spaces.
- Check max sequence length against actual chunk lengths; many sentence-transformer models cut at 512 tokens and still return a vector.
