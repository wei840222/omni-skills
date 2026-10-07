# Platform-Specific Formatting

Load only the section for the active channel.

## Telegram

- Markdown: bold, italic, code, code blocks, links
- Tables: avoid — they often render as broken text
- Edits are visible — consolidate corrections before send
- Silent/non-notification sends fit non-urgent late-night notes when the API supports them
- Hard limit: 4096 characters per message (Bot API `sendMessage`); split long drafts
- Pinned messages are scarce attention — use sparingly

## WhatsApp

- Basic markers: `*bold*`, `_italic_`, `~strikethrough~`, monospace
- Markdown links `[text](url)` do not render; paste bare URLs
- Voice notes are intimate — send only human-recorded audio the user authorized; never present synthetic audio as the user
- Read receipts (when enabled) show that a message was opened
- Reactions stay low-stakes
- Media may be compressed; check quality before relying on fine detail

## Slack / Teams-class chat

- Rich markdown, code blocks, blockquotes
- Prefer thread replies over new top-level channel noise
- `@channel` / org-wide pings notify broadly — reserve for true incidents
- Emoji reactions are normal culture; match the room
- Channel purpose sets tone (`#random` ≠ `#engineering`)

## Discord

- Markdown: headers, lists, code, limited embeds depending on client
- Threads fit extended discussion
- `@everyone` / `@here` notify many people — rare use only
- Channel context matters (`#announcements` ≠ `#memes`)
- Over-formal bot tone reads corporate in casual servers
- Prefer bullet lists over wide Markdown tables on mobile

## Email

- Subject lines drive open decisions — be specific
- Plain text is often safer than heavy HTML
- External mail usually needs a signature; internal may not
- Think before reply-all
- `Re:` threading vs a new subject changes who notices
- Opening/closing formality follows the relationship

## iMessage / SMS-class

- Tapbacks carry social weight (Liked vs Loved)
- Typing indicators are visible while composing
- Reacting to the wrong bubble is awkward and hard to undo
- Read receipts (when on) reveal attention

## X (Twitter)

- Default free-tier posts are short; keep the core punchy and use a thread for longer points
- Quote posts are for engagement with clear attribution
- Vary phrasing so cross-posted copy does not look automated
- Re-check live character limits before final send — product tiers change

## Cross-platform rules

- Identical verbatim posts on every network read as automation
- Audiences overlap — post sparingly when the same people are present
- Formatting that works on one client breaks on another
- Dry-run the draft in the real client when stakes are high
