# Authentication and API Rules

## Auth collections

Enable the relevant auth methods on the specific auth collection before using them. The collection is application-defined:

```js
const authData = await pb.collection('users').authWithPassword(
  'person@example.com',
  'PASSWORD_FROM_A_SECURE_INPUT',
);
```

OAuth2 requires a provider configured in PocketBase and a registered redirect URL. The JavaScript SDK's `authWithOAuth2` flow opens a browser popup and relies on a short-lived realtime connection; start it directly from a user interaction so browser popup controls do not block it.

## Rules and superusers

API rules are collection-specific. A `null` rule blocks the action, while an empty-string rule allows anyone; write an explicit rule when access is intended to be conditional. Test a rule with an unauthenticated client and with each relevant auth role before releasing it.

Superusers bypass collection API rules. Authenticate them through the `_superusers` collection only in trusted server-side code. Use the least-privileged auth collection or a scoped server integration for normal application work.

## Recovery checks

- If password authentication fails, first confirm the collection has Identity/Password enabled and that the configured identity field matches the supplied value.
- If an OAuth popup fails, confirm the provider and redirect URL configuration, then retry from a synchronous user-initiated click handler.
- If a rule yields unexpected access, inspect the rule value (`null`, empty, or expression) and reproduce with a minimal client for the affected role.

## Source

- https://pocketbase.io/docs/authentication/
- https://pocketbase.io/docs/api-rules-and-filters/
