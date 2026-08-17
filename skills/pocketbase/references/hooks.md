# JavaScript Event Hooks

Place JavaScript server hooks in `pb_hooks/*.pb.js` beside the PocketBase executable. Hooks run in the server process, so keep handlers bounded and avoid putting secrets in output or error messages.

Use the documented event hook that matches the required layer. Record model hooks can be triggered from non-HTTP code and do not have request context; choose record request hooks when the handler needs request data, headers, query parameters, or request authentication.

Event handlers receive an event object. Call `e.next()` when the handler should allow the remaining hook chain and the underlying operation to continue; throw an error or intentionally omit `e.next()` only when the requested operation must be stopped.

## Source

- https://pocketbase.io/docs/js-event-hooks/
