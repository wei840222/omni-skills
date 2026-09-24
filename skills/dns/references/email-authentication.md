# Email Authentication

## Email Authentication (All Three Required)

- SPF alone is incomplete—DKIM and DMARC are also required for deliverability
- DMARC record: `_dmarc.example.com TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com"`
- SPF must be a single TXT record—multiple SPF records are invalid; use `include:` for multiple sources
- SPF ending: use `-all` (reject) or `~all` (soft fail) exclusively
- Verify the complete setup with mail-tester.com after configuration
