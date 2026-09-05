# Authorization Knowledge and Source Notes

## Decision framework

Select the simplest model that represents the access relationship without duplicating policy logic:

- Use **ACLs** for a small, resource-local sharing list.
- Use **RBAC** for stable job functions and auditable permission bundles.
- Add **ABAC** when decisions depend on attributes such as tenant, resource classification, or request context.
- Use **ReBAC** when sharing and nested relationships are first-class data, such as teams, folders, and document collaborators.

A hybrid design can combine these models, but evaluate every request through one centralized decision point. Resolve explicit denies before allows and return a default denial when no policy grants access.

## Policy-as-code and ReBAC

OPA evaluates policy separately from application code and documents Rego as its policy language. Keep the application responsible for assembling a complete input document; keep authorization rules in the policy layer; test both the allow and deny paths before deployment.

Google Zanzibar describes relationship-based authorization at large scale. A ReBAC model should make relations and tuple consistency explicit rather than deriving access from scattered application conditionals.

Casbin documents ACL, RBAC, and ABAC model support. Its model and policy files are an implementation option, not a substitute for defining enforcement points, resource ownership, and revocation behavior.

## Enforcement and recovery checks

- Authenticate first, then load the target resource, then evaluate authorization before exposing or mutating the resource.
- Enforce the same authorization decision server-side for every read and mutation path; UI visibility is only a usability aid.
- When permission data is cached, invalidate it after role, team, or sharing changes. If invalidation cannot be confirmed for a sensitive action, re-evaluate from the source of truth.
- Log denials and administrative grants with the actor, action, resource identifier, outcome, and policy reason. Keep logs free of tokens and unnecessary personal data.

## Sources

### Relationship-based authorization

- Google Research, *Zanzibar: Google’s Consistent, Global Authorization System* — https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/
  - Defines relationship tuples and consistency considerations for a global authorization system.

### Policy-as-code

- Open Policy Agent, *Policy Language* — https://www.openpolicyagent.org/docs/latest/policy-language/
  - Documents Rego and policy evaluation concepts.
- Casbin, *Overview* — https://casbin.org/docs/overview
  - Documents supported authorization models and the model/policy split.

### Enforcement guidance

- OWASP, *Authorization Cheat Sheet* — https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
  - Recommends least privilege, deny-by-default, server-side enforcement, and validating permissions on every request.
