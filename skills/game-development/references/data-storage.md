# Data Storage

Local notes stay under the resolved `<state_root>/` and should capture:

- the current game concept and loop assumptions
- user preferences and non-negotiable constraints
- technical architecture choices with reasons
- playtest findings, balancing deltas, and release decisions

Keep notes concise and operational. Store decisions and outcomes, not long transcripts.

Never write the placeholder string `<state_root>` to disk. Credentials stay outside state roots; store pointers only (`env:…`, `keychain:…`, `1password:…`, `file:…`).
