# DNS Security and CAA Records

## CAA Records

- Limits which Certificate Authorities can issue certs for domain—prevents unauthorized issuance
- Basic: `example.com. CAA 0 issue "letsencrypt.org"`
- Wildcard requires separate entry: `CAA 0 issuewild "letsencrypt.org"`
- Incident reporting: `CAA 0 iodef "mailto:security@example.com"`
- Without CAA, any CA can issue—set explicitly for security-conscious domains
