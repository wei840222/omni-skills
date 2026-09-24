# Sources — Google Workspace CLI

Verify a limit, default, or error reason against these pages before repeating it as current API behavior. The numbers in `SKILL.md` Per-API Limits are the skill's working set as of 2026-09-24; if a primary page disagrees, the primary page wins and the skill note should be updated.

## gws CLI

- npm package `@googleworkspace/cli` — install name, binary `gws`, and current version: https://www.npmjs.com/package/@googleworkspace/cli
- Upstream repository and generated helper index: https://github.com/googleworkspace/cli
- CLI authentication, including `gws auth setup` / `gws auth login` and credentials under the gws config directory: https://github.com/googleworkspace/cli/blob/main/docs/skills.md

## API limits used by this skill

- Drive `files.list` `pageSize` default 100, maximum 1000: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- Drive `files.export` 10 MB export cap: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/export
- Gmail `messages.list` `maxResults` maximum 500: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- Gmail per-user quota units and daily send limits: https://developers.google.com/workspace/gmail/api/reference/quota
- Gmail `batchModify` up to 1,000 message ids: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/batchModify
- Calendar `events.list` `maxResults` default 250, maximum 2500: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
- Calendar `sendUpdates` default `false` on insert (the API emails nobody unless asked): https://developers.google.com/workspace/calendar/api/v3/reference/events/insert
- Admin SDK deleted-user restore window of 20 days: https://developers.google.com/workspace/admin/directory/reference/rest/v1/users/undelete
- Sheets spreadsheet size of 10 million cells: https://developers.google.com/workspace/sheets/api/limits
- OAuth clients in Testing publish status: refresh tokens expire after 7 days, and the consent screen allows up to 100 test users: https://support.google.com/cloud/answer/15549257

## Behavior this skill treats as stable

- Drive `permissions.create` `sendNotificationEmail` defaults to true for user and group grantees: https://developers.google.com/workspace/drive/api/reference/rest/v3/permissions/create
- Drive `files.delete` and Gmail `messages.delete` skip trash. Trash forms are `files.update` with `trashed: true` and `messages.trash`.
- `gws` owns `~/.config/gws/` (encrypted credentials and a 24-hour discovery cache). This skill does not relocate those files into `<state_root>`.
