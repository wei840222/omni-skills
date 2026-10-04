# Setup — Atlassian Cloud APIs + CLIs

Read this when `<state_root>/` is absent or empty. Help the user get useful Atlassian automation quickly without turning the conversation into a credential checklist.

## Attitude

Stay practical and precise. Atlassian estates are usually messy: multiple sites, mixed permissions, overlapping products, and risky write paths. Reduce confusion, narrow scope fast, and make the next safe action obvious.

Start with the single product needed right now. Expand the inventory only when it improves the current task.

## Priority order

### 1. First: integration preferences

Early in the conversation, clarify when this should activate:

- whenever they mention Jira, Confluence, Bitbucket, Trello, or Atlassian admin work
- only for terminal and API tasks
- always read-only unless they clearly ask for a write action

Save those activation rules in the user's main memory only after the user agrees that the behavior should persist.

### 2. Then: understand their Atlassian footprint

Learn the smallest set of facts that unblock real work:

- Cloud or Data Center
- Which product is in scope now
- Site URL, org, workspace, or page if relevant
- Whether they are an org admin, site admin, project admin, or regular user

If the user sounds uncertain, default to discovery and read-only inspection first.

### 3. Finally: capture useful defaults

Only save defaults that reduce repeated friction and only when the user wants them remembered:

- default Jira site or project key
- default Confluence site or space
- default Bitbucket workspace or repository
- default Trello board or list
- admin org, Compass cloud, Statuspage page, or Opsgenie region identifiers

## What is saved internally

- Activation preferences in main memory when the user opts in
- In `<state_root>/memory.md`: products in use, preferred auth modes, and write-safety preferences
- Only the smallest set of site or object identifiers that the user explicitly wants remembered

Record which auth method exists and where the user prefers to source it. Keep raw tokens, API keys, and passwords out of skill memory.
