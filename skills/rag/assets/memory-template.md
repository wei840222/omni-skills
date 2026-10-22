# RAG memory template

Use this file only when creating or reshaping `<state_root>/memory.md`.
Do not invent a second state root. Never write credentials or confidential chunk text.

## Boxes

Index every durable artifact this skill may open. One line per file; paths stay under `<state_root>/`.

| Condition | Path |
|-----------|------|
| Always when present | `<state_root>/config.yaml` |
| Always when present | `<state_root>/memory.md` |
| After first golden set | `<state_root>/goldensets/<name>-v<n>.md` |
| After each eval run | `<state_root>/evals/<year>.md` |
| After a design decision | `<state_root>/artifacts/decision-<topic>.md` |

## Index Registry

Record at build time and reread before query-side changes:

| Field | Value | Notes |
|-------|-------|-------|
| embedding_model_id | | |
| embedding_model_version | | |
| dimension | | |
| normalization | | |
| instruction_prefix | | |
| distance_metric | | |
| calibration_date | | |
| refusal_floor | | random-pair percentile |

## Corpus

| Source | Access field | Freshness | Notes |
|--------|--------------|-----------|-------|
| | | | |

## Baseline

| Date | Set | Metric | Score | Verdict |
|------|-----|--------|-------|---------|
| | | | | |

## Due

| Cadence | Next due | Owner note |
|---------|----------|------------|
| Eval regression | | |
| Corpus freshness | | |
| Permission resync | | |
| Model review | | |

## Known Failures

| Failure | Still open | Evidence |
|---------|------------|----------|
| | | |
