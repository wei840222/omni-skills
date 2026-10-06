---
name: google-reviews
description: >
  Research Google Maps and Google Shopping review signals for companies and products,
  normalize multi-source evidence, and optionally run multi-brand heartbeat monitoring
  with sentiment and decision-ready reports. Use when the user asks for Google Business
  Profile / Maps reviews, Shopping or merchant review signals, competitor reputation
  checks, rating drift, negative-theme spikes, or recurring Google review monitoring.
  Not for non-Google-only platforms unless explicitly cross-checking (yelp), generic
  map routing without review analysis (maps / apple-maps), inventing live API results,
  or posting owner replies without explicit authorization.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⭐","requires":{"bins":["curl","jq"]}}'
  related-skills: '{"alerts":"Escalation, cooldown, and alert-routing patterns once Google review thresholds fire.","analysis":"Broader trend synthesis when the ask is executive analytics beyond Google review monitoring.","apple-maps":"Directions and place confirmation after a Google-reviewed shortlist is chosen.","competitor-monitoring":"Multi-competitor watch programs that go beyond Google review surfaces.","heartbeat":"Cadence design for low-noise recurring refresh loops.","maps":"Geocoding, routing, and distance checks around reviewed places.","monitoring":"Broader monitoring architecture and incident hygiene outside Google review scope.","shopping":"Product buying-signal analysis adjacent to Shopping review interpretation.","yelp":"Cross-check Google review patterns against Yelp local-business signals."}'
---

## State location

Google Reviews state may exist in `<workspace>/google-reviews/`, `<workspace>/memory/google-reviews/`, or `~/google-reviews/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/google-reviews/`, `<workspace>/memory/google-reviews/`, `~/google-reviews/`.
3. If none exists and the user wants monitoring context kept, create `<workspace>/google-reviews/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/google-reviews/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update child paths only when the corresponding task needs them. Legacy `~/Clawic/data/google-reviews/` is a migration source only—keep it out of the active lookup order and move it only when the user asks.

### State tree

| Path | Purpose |
| --- | --- |
| `<state_root>/memory.md` | Activation preference, watchlist summary, cadence, alert policy |
| `<state_root>/brands/{brand}.md` | Per-brand scope, sources, thresholds, ownership |
| `<state_root>/snapshots/{brand}/{source}.jsonl` | Normalized review snapshots by refresh cycle |
| `<state_root>/reports/daily/` | Daily action reports |
| `<state_root>/reports/weekly/` | Weekly trend reports |
| `<state_root>/heartbeat/monitor-state.md` | Last run, cooldowns, connector health |

## When to load

Load this skill for Google Maps / Business Profile review research, Google Shopping or merchant review signals, competitor reputation due diligence on Google surfaces, rating or theme drift analysis, and optional recurring multi-brand monitoring with heartbeat refreshes.

Identify the company or product target, decision the user needs, source mode (API, export, or user-approved page check), and whether the ask is one-off research or ongoing monitoring before locking cadence.

| Need | File |
| --- | --- |
| First use / empty state | `references/setup.md` |
| Core operating rules | `references/core-rules.md` |
| Source connector matrix | `references/source-connectors.md` |
| Canonical review fields | `references/review-schema.md` |
| Sentiment and themes | `references/sentiment-rules.md` |
| Heartbeat cadence | `references/heartbeat-recipes.md` |
| Report templates | `references/reporting-playbook.md` |
| Official source map | `references/sources.md` |
| Memory template | `assets/memory-template.md` |
| Evaluation harness only | `test-prompts.json` |

## Near-miss handoffs

- Yelp-only local discovery or listing audits → `yelp`
- Directions after a shortlist is chosen → `maps` / `apple-maps`
- Product buying decision beyond review signals → `shopping`
- Multi-competitor programs beyond Google surfaces → `competitor-monitoring`
- Generic alert routing / incident hygiene → `alerts` / `monitoring`
- Executive analytics without Google-review focus → `analysis`

## Core workflow

1. Resolve mode: **research** (default) or **monitor** only after the user needs ongoing tracking.
2. Resolve identity: company, brand, location, product, or merchant entity before comparing.
3. Choose access path: authorized Business Profile / Places / Merchant workflows, user export, or user-approved public-page verification. State the source mode in the result.
4. Normalize evidence with `references/review-schema.md`; keep source-native IDs and timestamps.
5. Classify sentiment and themes with `references/sentiment-rules.md`; pair every claim with volume, recency, and snippets.
6. Answer the user question with confidence and gaps before offering monitoring setup.
7. For monitoring, load `references/heartbeat-recipes.md` and `references/reporting-playbook.md`; persist only under the resolved `<state_root>/`.

## Safe operation

- Owner replies, public posts, account changes, and external deliveries stay ask-first.
- Do not store API keys, OAuth tokens, or signed URLs in markdown state.
- Claim live monitoring only after a refresh actually ran; mark failed connectors `degraded` and continue with available sources.
- Re-check official docs in `references/sources.md` before asserting endpoint fields, reply policy, or quota behavior.

## Cognitive-load path

Keep the main path to: mode → identity → source path → normalize → answer → optional monitor.
Load one reference for the active branch rather than restating every connector matrix in the entry point.
