# Server Components and Actions

## Boundaries

- Server Components render on the server and ship zero client JS by default.
- `'use client'` marks a **boundary**: that module and its imports join the
  client bundle. Place it on interactive leaves; pass Server Components as
  `children`.
- Do not import server-only modules (secrets, fs, private env) into client files.

## Data and streaming

- Fetch close to the subtree that needs the data; avoid client waterfalls for
  initial page data when the framework supports server fetch.
- Use Suspense boundaries for streaming chunks users can see early.

## `use(promise)`

- May be called conditionally (exception to normal hook rules).
- Create the promise in a parent or cache — a new promise each client render
  suspends forever.

## Actions

- `useActionState(action, initial)` → `[state, formAction, pending]`.
- `useFormStatus` reads pending from form context (child of the form).
- Validate on the server; treat Action input as untrusted.
