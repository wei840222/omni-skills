## Core Rules

### 1. Authenticate Before Operations
Credentials from environment variables (ZENDESK_SUBDOMAIN, ZENDESK_EMAIL, ZENDESK_TOKEN) or `<state_root>/memory.md`.
```bash
# Test auth
curl -u "$ZENDESK_EMAIL/token:$ZENDESK_TOKEN" "https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2/users/me.json"
```

### 2. Search Before Create
Always search existing tickets before creating new ones to avoid duplicates.
```bash
curl -u "$AUTH" "$BASE/search.json?query=type:ticket+subject:issue"
```

### 3. Use Views for Efficiency
List tickets using specific views to return relevant subsets efficiently.
| View | Use Case |
|------|----------|
| `/views/active` | Get available views |
| `/views/{id}/tickets` | Tickets in specific view |
| `/tickets/recent` | Recently updated |

### 4. Preserve Ticket History
When updating, add internal notes explaining changes. Preserve all ticket data by keeping historical records.

### 5. Rate Limits
Zendesk limits: 700 requests/minute (Enterprise), 200/minute (others). Add delays for bulk operations.

### 6. Always Confirm Destructive Actions
Before closing, merging, or deleting tickets, confirm with user and summarize what will happen.

