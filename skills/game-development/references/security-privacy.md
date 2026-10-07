# Security & Privacy

Data that stays local:

- concept notes and user preferences under `<state_root>/`
- project decision logs and playtest outcomes

Data that may leave the machine only if explicitly requested:

- source code pushed to remote repositories
- asset uploads to CDN or build hosts
- backend telemetry or analytics events

This skill does **not**:

- force external services for simple browser prototypes
- require paid APIs for baseline game creation
- recommend production launch without performance and playtest evidence
- store secrets inside skill package files or state markdown

Strip tokens, private keys, and personal data from shared playtest notes.
