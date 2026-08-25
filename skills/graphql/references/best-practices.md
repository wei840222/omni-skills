# GraphQL Best Practices (2026 Update)

## Federation and Gateway Architecture

Apollo Federation 2 has largely superseded Schema Stitching for microservice composition. When splitting a graph, use Federation `@key` and `@external` directives over ad-hoc stitched resolvers.

Sources:
- Apollo Federation overview — https://www.apollographql.com/docs/federation/
- GraphQL Foundation GraphQL over HTTP — https://graphql.github.io/graphql-over-http/draft/

## Security

Disable introspection in production environments. Rate-limit and apply query depth / complexity analysis (for example GraphQL Armor or equivalent validation rules) to prevent abusive deep nested queries. Prefer trusted documents for unknown public clients.

Sources:
- OWASP GraphQL Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html
- GraphQL.org security considerations — https://graphql.org/learn/security/

## Pagination

Relay-style cursor connections are the industry standard over offset/limit pagination, providing robust support for real-time insertions and stable iteration over changing datasets.

Sources:
- Relay Cursor Connections Spec — https://relay.dev/graphql/connections.htm
- GraphQL.org pagination — https://graphql.org/learn/pagination/
