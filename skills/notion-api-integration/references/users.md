# Users — People, Guests, and Bots

`people` properties and `/v1/users` reflect integration capabilities. Missing fields usually mean missing capability, not a parsing bug.

**Contents:** [List and retrieve](#list-and-retrieve) · [People properties](#people-properties) · [Contacts boundary](#contacts-boundary)

## List and retrieve

Paginate `GET /v1/users`. Bot users expose `workspace_limits` (including max upload size). Do not dump the entire workspace directory into the shared contacts box.

## People properties

Inside a page object, people values can be truncated; use the property-item endpoint and paginate when you need the full set (see SKILL Rule 8 / `references/properties.md`).

## Contacts boundary

Shared contacts (`<workspace>/contacts/…`) hold people the user deals with — clients, owners — identified by email/handle. `/v1/users` output is workspace inventory, not an automatic contacts import.
