# Security and privacy summary

**Third-party data:** this box is mostly information about people who are not the user and never agreed to be filed. Minimize to what a next conversation needs (Rule 3, `sensitive_details`). Record behavior rather than judgment (Rule 8). A user request to remove someone deletes the record across skill-controlled copies including the shared address book, after suppression is recorded (`privacy.md`).

**Local storage:** records, dates, notes, and preferences stay under the resolved `<state_root>` and shared contacts root on this machine. Nothing is uploaded, synced outbound, or matched against an external service by this skill.

**Guardrails:**

- Messages are drafted for user approval only — never sent or scheduled by this skill.
- Do not write durable notes about a person the user has not raised, except explicit maintenance the user requested.
- Suppression list members are excluded from sweeps, briefs, and intro suggestions.
- Credentials and secrets are excluded anywhere under state roots, including values the user pastes to be saved — store pointers only.
