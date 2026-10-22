# Debug — symptom to cause

**Load when** the failure mode is unclear.

1. Log query text, active filter, candidate ids, scores, reranked order, and final context.
2. Place retrieved chunks beside the question (Core Rule 1).
3. Walk the fingerprint fields if scores look uniformly wrong.
4. Check ingestion counts and empty-page asserts before blaming the embedder.
5. For user-specific empties, query for chunks missing the access field.

| Symptom | Likely cause |
|---------|--------------|
| Good in dev, bad in prod | Different corpus, filter, or index fingerprint |
| Scores stuck near 0.7–0.8 | Uncalibrated cosine baseline—not relevance |
| Long doc never matches | Silent truncation at model max sequence length |
| Five near-identical hits | Overlap + near-duplicate corpus |
| Quality drop, no deploy | Corpus drift or silent provider model update |
