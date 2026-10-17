# Comments — Discussions and Replies

Use comments for lightweight discussion on a page or block anchor.

**Contents:** [Create and list](#create-and-list) · [Replies](#replies) · [Limits](#limits)

## Create and list

Create with parent page/block id. List is paginated — loop `has_more`.

## Replies

Thread with `discussion_id` when replying inside an existing discussion. Confirm the API cannot perform workspace UI-only moderation actions before promising them.

## Limits

Respect rate limits (`references/bulk.md` / `references/errors.md`). Do not store signed attachment URLs from comment payloads; store ids.
