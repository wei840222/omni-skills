---
name: salesforce-api-integration
description: 'Query, load, export, and sync Salesforce data via REST, Bulk, Composite, and Metadata APIs. Use when querying standard or custom objects with SOQL/SOSL, performing record CRUD, handling Salesforce API errors (e.g. DUPLICATES_DETECTED, INVALID_SESSION_ID), setting up OAuth authentication, or migrating data from another CRM.'
metadata:
  version: "1.0.3"
  openclaw: '{"emoji":"☁️","requires":{"env":["SF_ACCESS_TOKEN","SF_INSTANCE_URL"]},"primaryEnv":"SF_ACCESS_TOKEN"}'
  related-skills: '{"sql":"Shaping the warehouse side of a Salesforce sync"}'
---
## State location

Salesforce integration state may exist in `<workspace>/salesforce-api-integration/`, `<workspace>/memory/salesforce-api-integration/`, or `~/salesforce-api-integration/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/salesforce-api-integration/`, `<workspace>/memory/salesforce-api-integration/`, `~/salesforce-api-integration/`.
3. If none exists and state must be created, default to `<workspace>/salesforce-api-integration/`.

Use the selected `<state_root>` for every state operation in this skill.

**Data.** At the start of every session, read `<state_root>/config.yaml` (declared preferences) and `<state_root>/memory.md` (observations, `## Boxes`, and `## Due`) when they exist. Resolve every `## Boxes` entry under `<state_root>/` before opening it; ignore entries outside that root. If multiple candidate state roots exist, use only the selected highest-precedence root and report the conflict. Do not automatically move, merge, or delete data in another candidate directory.

**Write before the session ends** whenever the user has authorized persistent state and the session produced something durable: an org connection or instance URL change; a discovered object or custom field; a reusable SOQL query or report ID; a load, migration, metadata deploy, or investigated error; an observed limit; or a reusable design, mapping, or runbook. `references/memory-template.md` defines the destination, format, and threshold for each item.

**No credential is ever written under `<state_root>/`** — including user-pasted material. Store only a pointer such as `env:SF_ACCESS_TOKEN`, `keychain:sf-prod`, `1password:Work/Salesforce/prod`, or `file:~/.certs/sf-jwt.key`.

Salesforce has four data APIs, a governor-limit engine underneath them, and an org whose customizations decide what happens. Name the API and why it fits, count records before choosing it, and say which limit is encountered first. Start with safe defaults; when `api_version` is unset, state the version being assumed before acting. Precedence for configuration is `<state_root>/config.yaml`, then the Configuration table default.

## When To Use

- Reading Salesforce data: SOQL, SOSL, relationship queries, reports, exports of any size
- Writing Salesforce data: create, update, upsert, delete, bulk loads, CRM migrations, backfills
- Connecting: Connected Apps, OAuth flows, sandboxes, token refresh, an integration user's permissions
- Keeping something else in step: incremental polling, Change Data Capture, Platform Events, webhooks out of Salesforce
- Diagnosing a call that should work and does not: an error code, a silent null, a job that stalls, a limit that fires
- Not for designing a personal CRM from scratch (`crm`), generic REST/OAuth mechanics on other vendors (`api`), or writing Apex classes and triggers — this covers calling them from outside

## Quick Reference

| Situation | Play | Load on demand |
|---|---|---|
| "Pull me every X where Y" | SOQL with an indexed filter; check selectivity before blaming performance | `references/soql.md` |
| Create, update, delete, or upsert a handful of records | REST sObject calls; upsert on an External ID for idempotency | `references/records.md` |
| "Which object holds this, and what is the field called" | Standard object model, relationships, record types, and person accounts | `references/objects.md` |
| Tens of thousands of rows in or out | Bulk API 2.0, CSV shape, chunking, and lock contention | `references/bulk.md` |
| Parent and children in one transaction, or up to 25 calls in one round trip | Composite, Collections, Tree, or Graph by transaction boundary | `references/composite.md` |
| "What fields does this object have" or an unfamiliar `__c` object | Describe, caching, Tooling API, and metadata deploys | `references/metadata.md` |
| An API error whose cause is not obvious | Classify auth, permission, schema, org automation, or limits | `references/errors.md` |
| Persisting a reusable result | Record only permitted state under the resolved root | `references/memory-template.md` |

The main file provides the default guardrails. Load one of the references above only when its trigger matches; each reference is rooted at this skill directory.

## Core Rules

1. **The instance URL comes from the token response, never from a config file someone typed.** Every token exchange returns `instance_url`; use that value for the call you are about to make and store it in `## Org Context` (or `<state_root>/orgs.md`) in `<state_root>/memory.md`. Orgs move instances, My Domain names change, and a hardcoded host fails as DNS or a 404 that looks like a bad path.
2. **Pin the API version; review it on a cadence.** `/services/data/vXX.0/` is a contract: Salesforce ships three releases a year (Spring, Summer, Winter), each incrementing the version by one, and retires old versions in waves — a retired version stops answering entirely rather than degrading. Pin `api_version`, record the review in the `## Due` table of `<state_root>/memory.md`, and when it is unset, say which version you are assuming before acting.
3. **Choose the API by record count, and say the count out loud.** 1 record → sObject REST. 2-200 → sObject Collections: 200 records for **one** API call. 200 to `bulk_threshold` (default 5,000) → Collections in a loop, `ceil(n ÷ 200)` calls. Above that, or any CSV-shaped job → Bulk 2.0, roughly a dozen calls whatever the volume. A per-record loop over 50,000 records is 50,000 calls against an allocation that is often 15,000/day — the job does not run slowly, it stops the org's other integrations too.
4. **Every write is idempotent or it runs twice.** Upsert against a field marked External ID **and** Unique, so a retry after a timeout updates instead of duplicating. If the source system has no key in Salesforce, create the external ID field *before* the load — after it, you are deduplicating by fuzzy name match (a dependency-ordered migration plan).
5. **Trigger chunking decides batch size, not your request size.** Salesforce hands DML to Apex triggers in chunks of up to 200 records, and each chunk is one transaction with 100 SOQL queries, 150 DML statements and 10s of CPU. A trigger with one query per record dies at record 101 of the chunk. When one record succeeds and the load fails, the ceiling is in the org's automation, not in your payload (`references/bulk.md`).
6. **Normalize ids to 18 characters at the boundary.** The API returns 18-char case-insensitive ids; reports, the URL bar and older exports carry the 15-char case-sensitive form, which is the same id with the case-checksum suffix removed. Joining one against the other misses rows silently, and lowercasing a 15-char id destroys it. Store 18, compare 18.
7. **A field you cannot see and a field you misspelled return the same error.** Without field-level-security read on a field, `SELECT` it and Salesforce answers `INVALID_FIELD: No such column` — indistinguishable from a typo. Check the integration user's permission set before re-reading the query (`references/metadata.md`). The same rule silently drops fields from a describe: an object's schema is what *this* user can see.
8. **Sandbox first for anything that writes at scale or touches metadata.** Bulk loads, deletes, ownership changes and deploys are rehearsed in a sandbox while `sandbox_first` is true; the row counts and the failure list from the rehearsal are what make the production run predictable. Escape hatch: read-only queries and single-record fixes go straight to production.
9. **Read the allocation before a job that could consume it.** `/limits` reports `DailyApiRequests` used and remaining against a rolling 24-hour window, not a midnight reset — so an exhausted allocation stays exhausted for a full day from the calls that spent it. Before any job above ~10% of the remaining allowance, state the estimated call count and the remaining balance (`/limits`).

## Failure Signatures

Decode rule: the error's *layer* names the fix. An HTTP 401 is the session; a 403 is either permission or allocation and the code says which; a 400 with a field name is schema or validation; a 400 with no field is org automation.

| Signature | Most likely cause | First move |
|---|---|---|
| 401 `INVALID_SESSION_ID` | Access token expired, or a sandbox token sent to production | Refresh; if refresh also fails, the login host is wrong (`test.salesforce.com` for sandboxes) |
| 400 `invalid_grant` at the token endpoint | JWT `aud`, `sub` or clock; or the user is not pre-authorized on the Connected App | Check `aud` matches the environment and that the user's profile is on the app (authentication setup) |
| 400 `INVALID_FIELD` on a field you can see in the UI | Field-level security on the integration user, or the label instead of the API name | Rule 7 — check FLS first, then `describe` for the real API name |
| 400 `MALFORMED_QUERY` | Syntax, or a relationship name used where a field name belongs | `Account.Name` traverses, `AccountId` is the field; child subqueries use the plural relationship name |
| 403 `REQUEST_LIMIT_EXCEEDED` | Daily allocation, rolling 24h | Stop; report remaining from `/limits`. Retrying is what turns a slow day into an outage |
| 503, or 403 with a concurrency message | More than 25 requests running over 20 seconds at once | Serialize the long ones; make the query selective so it stops being long (`/limits`) |
| `UNABLE_TO_LOCK_ROW` in a bulk load | Parallel batches touching the same parent record | Sort the file by parent id so one parent lands in one chunk (`references/bulk.md`) |
| `DUPLICATES_DETECTED` | An org duplicate rule, not a unique constraint | Decide deliberately: fix the data, or send the duplicate-rule header with the reason recorded in `## Gotchas` |
| `CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY` | A trigger or flow threw — the message carries its class name | Read past the wrapper to the inner message; this is the org's code, not your call (`references/errors.md`) |
| `FIELD_CUSTOM_VALIDATION_EXCEPTION` | A validation rule the payload cannot satisfy | The rule's error message is the requirement; loads sometimes need it deactivated deliberately (a dependency-ordered migration plan) |
| `INVALID_CROSS_REFERENCE_KEY` | A lookup id that does not exist, is deleted, or belongs to the wrong object | Confirm the id's 3-char prefix matches the target object |
| `ENTITY_IS_DELETED` | Record is in the recycle bin | `queryAll` sees it; undelete or stop referencing it |
| 410 on a call that worked last year | The pinned API version was retired | Rule 2 — move the version, then re-test everything the release notes touched |
| A field simply absent from the JSON response | Null values are omitted, and unreadable fields are too | Absent ≠ empty; confirm with `describe` before writing "no data" |
| Anything else | Take the `errorCode`, not the HTTP status, to the table in `references/errors.md` | `references/errors.md` |

## Limits That Force Designs

Architecture constraints, not trivia: each one has broken a design that was already half-built. Exact allocations vary by edition and license count — `/limits` on the org is the source of truth (`/limits`).

| Surface | Limit that decides the design |
|---|---|
| SOQL over REST | 2,000 records per response page, `nextRecordsUrl` for the rest · ~120s query timeout · `Sforce-Query-Options: batchSize=200..2000` to shrink pages |
| Query selectivity | An index is used only if the filter matches a small fraction of the object — roughly 30% of the first million rows for standard indexes, ~10% for custom ones. Above that the query table-scans and eventually times out |
| sObject Collections | 200 records per request, all of one operation |
| Composite | 25 subrequests, `allOrNone` spanning all of them |
| Composite Graph | 500 nodes; **each graph is its own transaction**, which is the only way to get independent rollback in one round trip |
| sObject Tree | 200 records total across the whole nested payload |
| Bulk API 2.0 | 150 MB per upload · records processed in chunks, so triggers still see ≤200 at a time · parallel-only: no serial mode to fall back on |
| Apex governor (per transaction, applies to *your* DML through the org's triggers) | 100 SOQL · 150 DML statements · 50,000 rows retrieved · 10s CPU synchronous |
| Concurrency | 25 concurrent synchronous requests running longer than 20 seconds, org-wide |
| Daily API requests | Per-license allocation with a floor (Developer Edition 15,000/day); rolling 24h window, shared by every integration in the org |
| Data storage | Most records count as 2 KB regardless of field count — a million skinny rows is ~2 GB |
| Event bus (CDC, Platform Events) | 72-hour replay retention: a consumer down for a long weekend cannot catch up from replay id (CDC or polling guidance) |
| Replication API (`getUpdated`/`getDeleted`) | 30-day window, and start/end must be at least a minute apart |
| Reports API | 2,000 rows synchronously; anything wider is a SOQL job, not a report (Reports API guidance) |

## Output Gates

Before delivering a query, a load, or an integration design:

- Did I name which API this uses and how many calls it costs against the daily allocation?
- Is every write idempotent — upsert on an external id, or an explicit reason why insert is safe here (Rule 4)?
- Is the target org unambiguous in the answer (production vs sandbox), and did I use the `instance_url` the token returned?
- Does anything destructive (delete, hard delete, mass update, metadata deploy) carry an explicit confirmation step and a stated blast radius in records?
- Did I check what the org already told me — `## Org Context`, `## Schema Map`, `## Gotchas` in `<state_root>/memory.md` and whatever `## Boxes` points to — before describing or re-deriving it?
- **Persistence:** did anything durable come out of this? Org or instance URL, an object's fields, a query worth reusing, a load that ran, a limit observed, a cause that took work to find, an artifact worth re-reading — write it to the box `references/memory-template.md` names, and add its `## Boxes` line in the same turn.

## When to Load References

| Reference | When to Load |
|---|---|
| `references/soql.md` | When querying data or optimizing SOQL performance. |
| `references/records.md` | When performing single-record CRUD operations. |
| `references/composite.md` | When dealing with up to 200 records or related object graphs. |
| `references/bulk.md` | When loading or exporting > 5,000 records. |
| `references/metadata.md` | When describing objects, fields, or deploying metadata. |
| `references/objects.md` | When mapping standard objects or dealing with relationships. |
| `references/errors.md` | When debugging API errors or status codes. |
| `references/memory-template.md` | When writing persistent state, such as org info or integration designs. |

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| api_version | text (`vNN.0`) | none | Version segment in every URL and example; while unset, name the assumed version before acting (Rule 2) |
| default_org | text (org alias) | none | Which org in `## Org Context` / `<state_root>/orgs.md` an unqualified request means; unset means ask nothing and say which org the answer assumes |
| auth_flow | jwt-bearer \| web-server \| refresh-token \| client-credentials \| device | jwt-bearer | Which flow authentication setup walks and what the examples pass to the token endpoint |
| code_style | curl \| python \| node \| sf-cli | curl | Language of every emitted example |
| bulk_threshold | number (records) | 5000 | Switch point from sObject Collections to Bulk 2.0 in Rule 3 |
| all_or_none | bool | true | Default for Collections and Composite: whole-batch rollback vs per-record results |
| sandbox_first | bool | true | Whether bulk writes, deletes and metadata deploys are rehearsed in a sandbox before production (Rule 8) |
| pii_fields | list (field API names) | none | Fields never written into local files or example output, replaced by a `<redacted>` marker |

Preference areas — customizable dimensions; a stated preference gets recorded in `<state_root>/config.yaml` and applied from then on:

- **Tooling** — REST directly vs an SDK (jsforce, simple-salesforce, the official SDKs), the `sf` CLI for deploys and org management, Workbench for one-off validation — affects every example and the deploy path in `references/metadata.md`
- **Conventions** — external ID field naming, namespace prefix for managed packages, CSV column ordering and date format, batch file naming — affects `references/bulk.md` and a dependency-ordered migration plan
- **Environment** — which sandbox types exist and their refresh cadence, sandbox naming, whether scratch orgs are in play — affects authentication setup and the `## Due` table
- **Safety posture** — whether hard delete is permitted at all, whether duplicate rules and validation rules may be bypassed, confirmation before mass updates — affects Output Gates and a dependency-ordered migration plan
- **Data handling** — which objects and fields are off-limits for extraction, masking rules, row caps on exported files — affects `references/soql.md`, Reports API guidance and what may be stored locally
- **Output format** — raw JSON vs a summarized table, whether every answer carries a call-count estimate, timezone for date literals — affects every response
- **Sync posture** — polling interval, whether CDC or Platform Events are enabled in the org, tolerance for gaps versus cost — affects CDC or polling guidance

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Building on the username-password OAuth flow | Salesforce has been disabling it by default, new orgs first; the integration works until the org's setting flips and then nothing authenticates | JWT bearer for server-to-server, web-server flow for anything with a user (authentication setup) |
| One API call per record in a loop | Burns the daily allocation and takes hours; the org's other integrations fail alongside yours | Collections for ≤200, Bulk 2.0 above `bulk_threshold` (Rule 3) |
| `SELECT` with a leading-wildcard `LIKE '%x%'` on a large object | No index can serve it; it table-scans and eventually times out | Filter on an indexed field first, or use SOSL, which is built for text search (`references/soql.md`) |
| Trusting `LastModifiedDate` for incremental sync | It does not move for every system-level change, so rows silently stop arriving | `SystemModstamp`, which is indexed and moves for system updates too (CDC or polling guidance) |
| Empty CSV cell to clear a field in Bulk | Empty means "leave unchanged"; the field keeps its old value and nobody notices for months | `#N/A` is the explicit null in Bulk CSV; in JSON it is `"Field": null` |
| Querying `BillingAddress` or a geolocation field in Bulk | Compound fields are not supported there; the job fails or the column comes back empty | Query the components: `BillingStreet`, `BillingCity`, `BillingState`, `BillingPostalCode`, `BillingCountry` |
| Loading children before parents | Every row fails with `INVALID_CROSS_REFERENCE_KEY` and the retry loads duplicates | Load in dependency order and reference parents by external id, not Salesforce id (a dependency-ordered migration plan) |
| Assuming a `describe` is stable | Admins add fields, change picklists and flip FLS without telling the integration | Cache with `If-Modified-Since`, re-describe when a field error appears, and record the object in `## Schema Map` (`references/metadata.md`) |
| Treating a 403 as "no permission" | `REQUEST_LIMIT_EXCEEDED` is also a 403, and the fix is the opposite of granting access | Branch on `errorCode`, never on the HTTP status alone |
| Retrying a failed insert without an idempotency key | Salesforce processed the first one; the timeout was the response, not the write | Upsert on external id, or query for the record before retrying (Rule 4) |
| Mass owner changes during business hours | Sharing recalculation cascades and can lock the org for everyone | Defer sharing calculation, run off hours, and stage in a sandbox first (a dependency-ordered migration plan) |
| Storing an access token or a JWT private key in the notes file | It leaks with the first backup or screen share | Pointer only: `keychain:sf-prod`, `file:~/.certs/sf-jwt.key` |
| Testing a load against 10 records | Governor limits and lock contention only appear at chunk boundaries — 10 records never crosses one | Rehearse with at least 1,000 records, spanning more than one 200-record chunk (Rule 5) |

## Where Experts Disagree

- **Polling versus streaming.** CDC and Platform Events give near-real-time delivery and cost no query allocation, but 72-hour replay retention means an outage past the weekend is a full resync; `SystemModstamp` polling is dull, cheap to reason about, and recovers from any downtime by widening the window. Teams with an on-call rotation take streaming; teams without take polling (CDC or polling guidance).
- **Bulk 2.0 versus Collections at mid volume.** Between roughly 2,000 and 20,000 records both work. Collections gives synchronous, per-record errors you can act on immediately; Bulk gives a fraction of the API calls and a result file to reconcile later. The tie-breaker is whether a human is waiting for the answer.
- **Bypassing org automation during a load.** One camp deactivates validation rules, triggers and workflows to get the data in, then re-runs the automation deliberately; the other refuses, on the grounds that data which cannot pass the rules is data the org will reject forever. The frontier: a migration of historical records may bypass; an ongoing integration may not.
- **External IDs everywhere versus Salesforce ids.** Storing Salesforce ids in the external system is smaller and faster; storing your own key on the Salesforce record survives a sandbox refresh, a re-import and an org merge. Any data that ever gets reloaded needs the external id.

## Security & Privacy

**Credentials:** this skill calls the Salesforce APIs using a token supplied by the environment (`SF_ACCESS_TOKEN`, `SF_INSTANCE_URL`) or an OAuth flow the user runs. It does NOT store, log, copy or transmit tokens, client secrets, private keys or passwords, and never writes a credential into `<state_root>/`.

**Sent to Salesforce:** the queries and record data you ask it to send, to the org's own instance URL and its OAuth hosts. Nothing else. No third-party endpoint is contacted.

**Stays local:** org context, schema notes, saved queries, load history and preferences in `<state_root>/` — API names, ids and counts only. Record data is not copied into memory files, and any field listed in `pii_fields` is replaced by a marker before anything is written.

**Guardrails:** reads are default. Deletes, hard deletes, mass updates and metadata deploys are presented with the record count they touch and require explicit confirmation. Field-level security and sharing are never bypassed — if the integration user cannot see it, that is the answer.
