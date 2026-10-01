# Session structure — Learning

Single session loop: Diagnose (2 probes) → Teach (1 concept, 1 anchor, core Rule 2 cap) → Check (generation prompt) → repeat → Close with 2-3 retrieval questions spanning the whole session.

Multi-session:

- Open with retrieval from the topic log before new content. Session-open checks should land at the bottom of the 70-90% band: zero misses across sessions means the questions are too easy (core Rule 4); mostly misses means last session overshot.
- Log every miss in `<state_root>/memory.md` as the first review target for the next session.
- After 3+ concepts are learned, mix checks across concepts instead of drilling one at a time. In a classic result, interleaved math practice scored 63% versus 20% for blocked practice on a delayed test (Rohrer and Taylor); blocked practice feels smoother and performs worse. Cite `references/sources.md` when quoting figures.
- Timing of checks: a check immediately after explaining is near-guaranteed to succeed and predicts nothing. Put weight on the session-close and next-session-open checks; those are the ones that measure learning.
