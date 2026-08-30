# Setup preferences

Use setup only when the user asks to save Apple News preferences or command reliability notes.

1. Resolve `<state_root>` using the entrypoint's State location procedure.
2. Describe the proposed `<state_root>/memory.md` write and obtain confirmation.
3. Ask only for preferences that affect future behavior:
   - whether the skill should activate for News.app launches and `apple.news` links;
   - whether a second confirmation is required for multiple links;
   - whether Shortcut workflows remain disabled until explicitly requested;
   - the preferred preview detail before external actions.
4. Probe `open` and `/System/Applications/News.app` before recording a command path as working.
5. Record a Shortcut only after the user supplies its exact name and confirms its expected side effects.
6. Summarize the saved preferences after the approved write.
