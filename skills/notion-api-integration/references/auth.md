# Auth — Tokens, Sharing, and OAuth

Access failures dominate Notion API debugging. A valid token that cannot see a page returns the same 404 shape as a missing object.

**Contents:** [Credential kinds](#credential-kinds) · [Headers](#headers) · [Share before call](#share-before-call) · [OAuth outline](#oauth-outline) · [Capabilities](#capabilities) · [Debug ladder](#debug-ladder)

## Credential kinds

| Kind | When | Notes |
|---|---|---|
| Internal integration token | Single workspace automation you own | Static secret from Developer portal Configuration |
| Public OAuth access token | Multi-workspace install | Authorization-code flow; store access + refresh pointers only |
| Personal access token (PAT) | Script acting as a specific user | User-scoped; no page picker; uses that user's permissions |

Never write the raw token into `<state_root>/`. Store `env:NOTION_API_KEY`, `keychain:…`, or `1password:…` pointers only.

## Headers

Every non-SDK request needs:

```http
Authorization: Bearer <token>
Notion-Version: <pinned-version>
Content-Type: application/json
```

Omit `Notion-Version` → 400. Pin one version per codebase. Official docs currently document versions including `2025-09-03` (data sources) and newer; state the assumed version before acting if `api_version` is unset.

## Share before call

Internal connections only see pages/databases explicitly shared with them (or under a shared ancestor). Order of checks on 404/`object_not_found`:

1. Is the integration connected to this page or an ancestor?
2. Is the id the object type this endpoint expects? (URL `?v=` is a *view* id, not the database/data-source id.)
3. Does the object still exist / is it trashed?

Ids work with or without dashes.

## OAuth outline

Public connections: send user to authorization URL → receive `code` on redirect → `POST` token exchange → store tokens as pointers → refresh when expired. Cancel redirects include `error=access_denied`. Page picker only lists resources the user can fully share.

## Capabilities

Capability grants bound what the token may do (read content, update content, insert comments, etc.). A 403 after a valid 401-free auth usually means a missing capability, not a bad token.

## Debug ladder

1. Print status, `code`, and `message` from the error body.
2. Confirm `Notion-Version` and Authorization header present.
3. Confirm share / ancestor connection.
4. Confirm object type vs endpoint.
5. Only then assume the object is gone.

Official sources: Authorization guide, Create a connection, Status codes.
