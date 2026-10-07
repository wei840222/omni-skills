# Requirements

- Runtime for local preview scripts: `node`
- Optional tools for offline asset processing: `python3`
- Browser target for quick iterations: Chromium, Firefox, or Safari family

Prefer local and static workflows first. Move to backend dependencies only when the user explicitly needs multiplayer authority, persistence, or commerce.

Document unavoidable platform limits (mobile GPU, iOS Safari memory, audio autoplay policies) instead of hiding them behind “works everywhere” claims.
