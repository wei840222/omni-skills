# Sources and freshness

Gate 6 research notes for `notes`. Re-open these URLs before quoting mutable API versions, rate limits, or CLI behavior. Automation fetch status recorded 2026-10-16.

## Agent Skills / packaging

- Agent Skills specification — https://agentskills.io/specification (HTTP 200)
- Agent Skills llms index — https://agentskills.io/llms.txt (HTTP 200)

## Notion

- Notion API intro — https://developers.notion.com/reference/intro (HTTP 200)
- Notion API versioning — https://developers.notion.com/reference/versioning (HTTP 200; includes `2025-09-03` among published versions; newer dates also appear — pin intentionally and re-check)
- Notion request limits — https://developers.notion.com/reference/request-limits (HTTP 200; do not hard-code a rate number from memory)
- Create integrations help — https://www.notion.com/help/create-integrations-with-the-notion-api (HTTP 200)

## Obsidian / Apple Notes / Evernote / Bear

- Obsidian manage notes — https://help.obsidian.md/Files+and+folders/Manage+notes (HTTP 200)
- Apple Notes Mac guide — https://support.apple.com/guide/notes/welcome/mac (HTTP 200)
- Evernote developer docs — https://dev.evernote.com/doc/ (HTTP 200)
- Bear FAQ index — https://bear.app/faq/ (HTTP 200)
- Bear notes location FAQ — https://bear.app/faq/where-are-bears-notes-located/ (HTTP 200)
- Older Bear "API Token and Callback URL" deep link returned HTTP 404 to automation on 2026-10-16 — treat callback/token details as browser-verified before relying on them

## Practice claims kept as stable-domain (not vendor SLA)

- Claim titles beat topic titles for retrieval
- Absolute dates on action items
- Inbox triage within days, not indefinite parking
- Index maintenance cost dominates under ~30 notes
