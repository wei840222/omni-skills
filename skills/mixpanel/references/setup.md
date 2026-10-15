# Setup — Mixpanel

Read this when `<state_root>/` does not exist, or when `<state_root>/memory.md` is
missing or empty. Keep the conversation focused on insights, not credential theater.

## Attitude

Help the user get answers from product analytics. Ask only what unblocks the next
query. Prefer learning event names from successful pulls over requesting inventory
dumps.

## Priority order

### 1. Integration preference

Ask whether Mixpanel help should activate whenever they mention funnels, retention,
cohorts, or product metrics. Record the preference in `<state_root>/memory.md`.

### 2. Product context

Learn incrementally:

- What the product is (SaaS, mobile, commerce)
- Events that matter (signup, purchase, activation)
- Metrics they care about (conversion, retention, engagement)

### 3. Credentials

When a live query is needed:

1. Check env for `MP_SERVICE_ACCOUNT`, `MP_SERVICE_SECRET`, `MP_PROJECT_ID`.
2. If missing, guide creation from Mixpanel Organization Settings → Service Accounts
   (`https://mixpanel.com/settings/org#serviceaccounts`) or the project Service
   Accounts tab. Owner/Admin permission is required.
3. Store the secret once shown — Mixpanel will not redisplay it.
4. Point to environment variables; do not ask them to paste secrets into chat.

Service Account auth for Query API requires `project_id` on each request. Optional
`workspace_id` applies when Data Views are in use.

### 4. Initialize state

After consent, create `<state_root>/memory.md` from `assets/data-templates.md`.
Add `<state_root>/queries/` only when they want saved query notes.

## What you save locally

In `<state_root>/memory.md`:

- Product context
- Key events and cohort ids they reuse
- Useful query patterns and insights

Never store Service Account secrets in files.
