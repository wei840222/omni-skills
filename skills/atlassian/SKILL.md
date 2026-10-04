---
name: atlassian
description: >
  Operate Atlassian Cloud APIs and CLIs across Jira, Confluence, Bitbucket,
  Trello, Cloud Admin, Forge, Compass, Opsgenie, and Statuspage. Use when the
  user needs to manage, automate, search, report, or administer Atlassian Cloud
  products from terminal or API workflows. Not for generic REST design without
  Atlassian products (`rest-api`), broad software-engineering process (`developer`),
  multi-cloud API catalogs (`api`), or GitLab-specific workflows (`gitlab`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧩"}'
  related-skills: '{"api":"Generic multi-vendor API catalogs when the task is not Atlassian-specific.","rest-api":"REST design and HTTP mechanics outside Atlassian product surfaces.","developer":"Broad engineering process and tooling beyond Atlassian Cloud automation.","devops":"Delivery pipelines and ops culture when Atlassian is only one integration point.","gitlab":"GitLab-native issues/MR/CI when the user is not on Bitbucket/Jira."}'
---

# Atlassian

Route Atlassian Cloud work to the correct first-party API or CLI, match auth to that surface, and treat every write as high-impact.

## State location

Optional Atlassian defaults may live under a portable state root. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/atlassian/`, `<workspace>/memory/atlassian/`, `~/atlassian/`.
3. If multiple candidates exist, use the highest-precedence one only. Do not merge lower-precedence directories; tell the user that multiple copies were detected.
4. If none exists and state must be created, default to `<workspace>/atlassian/`.
5. If the host cannot supply `<workspace>`, do not impersonate it with the current working directory. An existing `~/atlassian/` may be read; if it also does not exist, ask the user or host to specify a state root before creating data.
6. Once selected, `<state_root>` stays fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. The skill works without persistent memory; save defaults only when the user wants repeatable shortcuts. If `<state_root>/` is absent, run `references/setup.md`. See `assets/memory-template.md` for structure.

### State tree

| Path | Purpose |
|---|---|
| `<state_root>/memory.md` | Optional saved sites, products, auth preferences, and write-safety defaults |

## When to load

Load this skill when the request is **Atlassian product automation**, for example:

- create, transition, search, or report on Jira issues, boards, or service requests
- Confluence page/space automation
- Bitbucket repositories, pull requests, or pipelines
- Trello boards/cards
- Cloud Admin org/user policy work
- Compass components/scorecards, Statuspage incidents, or Opsgenie alerts
- choosing between `acli`, `forge`, REST, and GraphQL for an Atlassian task

Prefer sibling skills when the problem is already broader: `rest-api` for generic HTTP design, `api` for multi-vendor catalogs, `developer`/`devops` for process outside Atlassian, `gitlab` for GitLab-native flows.

## Quick workflow

1. **Pick the exact surface** — Jira Platform vs Software vs Service Management, Confluence, Bitbucket, Trello, Admin, Compass, Statuspage, Opsgenie, or GraphQL.
2. **Match auth to that surface** — only the credential family needed (see `references/auth-and-clis.md`).
3. **Resolve targets before writes** — site, org, project, board, space, page, list, workspace, component, or page IDs.
4. **Prefer first-party paths** — official REST, GraphQL, `acli`, or `forge` before partner CLIs.
5. **Paginate and back off** — follow product-specific pagination; retry on HTTP 429 with backoff.
6. **Confirm bulk/destructive actions** — show the exact target set and get user confirmation before create/update/archive/delete at scale.
7. **Verify freshness** — version-sensitive claims against URLs in `references/sources.md`.

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/setup.md` | Initialize or capture optional state defaults |
| `assets/memory-template.md` | Schema for `<state_root>/memory.md` |
| `references/product-map.md` | Map product → API host, auth, CLI path |
| `references/jira-suite.md` | Jira Platform, Software, and Service Management |
| `references/content-dev-collab.md` | Confluence, Bitbucket, and Trello |
| `references/admin-ops.md` | Cloud Admin, Compass, Statuspage, Opsgenie, GraphQL |
| `references/auth-and-clis.md` | Auth matrix, `acli`, and `forge` |
| `references/sources.md` | Official docs used for Gate 6 freshness |
| `test-prompts.json` | Evaluation harness only — do not load during normal user assistance |

## Scope

Cloud-first coverage of publicly documented Atlassian automation surfaces current as of the sources listed in `references/sources.md`. Prefer first-party REST, GraphQL, `acli`, and `forge` when they exist. If the user is on Data Center or a product without public Cloud automation docs, say that explicitly before acting.

## Core rules

### 1. Pick the exact Atlassian surface first

- Jira splits across platform, software, and service management APIs.
- Confluence, Bitbucket, Trello, Cloud Admin, Compass, Statuspage, and Opsgenie each have different auth and URL rules.
- Keep Cloud and Data Center docs separate unless the user explicitly confirms Data Center.

### 2. Ask only for the credential family the chosen surface needs

- Jira, Confluence, GraphQL, and Forge commonly use API token plus email, OAuth 2.0, or Forge auth.
- Bitbucket uses access tokens, app passwords, or OAuth.
- Trello uses key plus token; Statuspage uses an API token; Opsgenie uses an API key; Cloud Admin uses an admin API key.

### 3. Prefer first-party surfaces before partner CLIs

- Start with official REST, GraphQL, `acli`, or `forge`.
- Use partner CLIs only when Atlassian has no first-party CLI for that product or the user explicitly asks for that toolchain.

### 4. Treat every write as high-impact

- Resolve site, org, project, board, space, page, list, workspace, or component IDs before create, update, archive, or delete.
- For bulk or destructive actions, show the exact target set first and get user confirmation.

### 5. Respect product-specific data formats

- Jira rich text often requires Atlassian Document Format (ADF).
- Confluence body representations differ from Jira fields.
- Bitbucket relies on slugs, UUIDs, and `next` pagination.
- Trello auth often lives in query parameters; Statuspage nests many write payloads.

### 6. Handle rate limits and pagination every time

- Follow `next` links, cursors, `pagelen`, `limit`, `startAt`, or page tokens depending on the product.
- Back off on HTTP 429 and surface partial failures on bulk writes.

### 7. Be explicit about CLI support gaps

- Official Atlassian CLI currently exposes `admin`, `jira`, and `rovodev`.
- Official Forge CLI builds and deploys Forge apps; it is not a general product CRUD CLI.
- Confluence, Bitbucket, Trello, Statuspage, and Opsgenie still route mainly through APIs or partner CLIs.

## Common traps

- Using Jira Platform endpoints for boards or sprints → use Jira Software `/rest/agile/1.0`.
- Sending plain text into Jira rich fields without checking ADF support → malformed descriptions or comments.
- Forgetting `/wiki` in Confluence Cloud URLs → wrong host or 404.
- Assuming `acli` covers every Atlassian product → today it is mostly Jira, Admin, and Rovo Dev.
- Mixing Bitbucket auth with Atlassian tenant auth → valid token, wrong endpoint family.
- Treating Opsgenie as a long-term target without checking migration plans → official docs point many users to Jira Service Management or Compass.
- Reusing tenant GraphQL paths for non-tenant products → Bitbucket and Trello use different gateway hosts.

## External endpoints

Route requests only to the endpoint family that matches the active Atlassian product.

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| `https://{site}.atlassian.net/rest/api/*` | Jira issue, project, workflow, user, and search payloads | Jira Cloud platform operations |
| `https://{site}.atlassian.net/rest/agile/1.0/*` and `https://{site}.atlassian.net/rest/servicedeskapi/*` | Board, sprint, backlog, request, customer, and queue payloads | Jira Software and Jira Service Management |
| `https://{site}.atlassian.net/wiki/api/v2/*` | Confluence page, space, comment, label, attachment metadata | Confluence Cloud |
| `https://api.atlassian.com/admin/*`, `https://api.atlassian.com/graphql`, and product GraphQL gateways | Organization, policy, graph, Compass, and app payloads | Cloud Admin, GraphQL, and Compass |
| `https://api.bitbucket.org/2.0/*` and `https://api.trello.com/1/*` | Repository, pull request, pipeline, board, list, card, and webhook data | Bitbucket Cloud and Trello |
| `https://api.statuspage.io/v1/*`, `https://api.opsgenie.com/*`, and `https://api.eu.opsgenie.com/*` | Incident, component, metric, alert, schedule, and on-call payloads | Statuspage and Opsgenie |

No other first-party Atlassian endpoints are targeted by default. If the user chooses a partner CLI, review that tool's own endpoints before using it.

## Security and privacy

**Data that leaves the machine**

- Only the Atlassian request payloads, identifiers, and auth material needed for the chosen product surface
- CLI and API requests sent to the declared Atlassian or explicitly chosen partner endpoints

**Data that stays local**

- Only the defaults the user explicitly wants remembered in `<state_root>/`
- Notes about whether the user prefers read-only, review-first, or bulk automation workflows

**Safe defaults**

- Request only the credential family required for the active surface
- Keep reads and writes limited to the declared Atlassian or explicitly chosen partner endpoints
- Store auth-method notes and non-secret identifiers only when the user opts in; keep raw tokens, API keys, and passwords out of skill memory
- Confirm write permission separately from successful reads

## Trust

By using this skill, data is sent to Atlassian services and any explicitly chosen partner CLI. Install only when those parties are trusted for the task.
