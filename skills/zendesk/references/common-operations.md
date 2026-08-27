## Common Operations

Set auth: `AUTH="$ZENDESK_EMAIL/token:$ZENDESK_TOKEN"` and `BASE="https://$ZENDESK_SUBDOMAIN.zendesk.com/api/v2"`

### Create Ticket
```bash
curl -X POST "$BASE/tickets.json" -u "$AUTH" -H "Content-Type: application/json" \
  -d '{"ticket":{"subject":"Issue","comment":{"body":"Description"},"priority":"normal"}}'
```

### Update Ticket Status
```bash
curl -X PUT "$BASE/tickets/$ID.json" -u "$AUTH" -H "Content-Type: application/json" \
  -d '{"ticket":{"status":"solved","comment":{"body":"Resolution","public":false}}}'
```

### Search Tickets
```bash
curl -u "$AUTH" "$BASE/search.json?query=type:ticket+status:open+priority:urgent"
```

### Get User Details
```bash
curl -u "$AUTH" "$BASE/users/search.json?query=email:user@example.com"
```

