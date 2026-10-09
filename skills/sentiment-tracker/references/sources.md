# Sources — Sentiment method & platform caveats

Verified reference URLs for Gate 6 research. Prefer these when refreshing
method language; do not invent API pricing or vendor limits from memory.

## Sentiment analysis method

- Pang & Lee opinion mining survey (foundational polarity/subjectivity framing)
  — https://www.cs.cornell.edu/home/llee/opinion-mining-sentiment-analysis-survey.html
- Liu, *Sentiment Analysis and Opinion Mining* (Morgan & Claypool overview)
  — https://www.cs.uic.edu/~liub/FBS/SentimentAnalysis-and-OpinionMining.pdf
- NIST TREC blog/opinion evaluation context (public retrieval evaluation)
  — https://trec.nist.gov/

## Platform / sampling caveats

- X/Twitter developer platform docs (API access and product changes)
  — https://developer.x.com/en/docs
- Reddit Data API wiki
  — https://www.reddit.com/wiki/api/
- YouTube Data API overview
  — https://developers.google.com/youtube/v3
- Hacker News API (Firebase)
  — https://github.com/HackerNews/API
- TikTok Research API overview
  — https://developers.tiktok.com/products/research-api/

## Practice notes encoded in SKILL.md

- Multi-source sampling and explicit time windows follow standard opinion-mining
  advice to avoid single-channel bias and undated claims.
- Baseline-relative alerts (>20% negative share move, viral outliers, new themes)
  keep monitoring actionable without alert fatigue.
- This skill defaults to host `web_search` / `web_fetch` style public sampling
  rather than requiring vendor API keys; when a user supplies authenticated
  access, document the grant and still keep secrets out of `<state_root>/`.
