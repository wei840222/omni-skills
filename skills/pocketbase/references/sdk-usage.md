# JavaScript SDK Usage

## Client and records

Create one client per backend URL and use the configured collection name:

```js
import PocketBase from 'pocketbase';

const pb = new PocketBase('https://api.example.com');
const page = await pb.collection('posts').getList(1, 20, {
  expand: 'author',
  filter: 'status = "published"',
});
```

Read expanded relations from `record.expand.<field>`. Build filters with the SDK's filter facilities or a documented PocketBase filter expression; never concatenate untrusted input into a filter string.

## Auth state

After a successful SDK authentication call, inspect `pb.authStore.isValid`, `pb.authStore.token`, and `pb.authStore.record`. Clear locally held authentication state with `pb.authStore.clear()` when the user signs out. For a third-party token that must be checked with the server, use the documented auth-refresh flow for that auth collection.

## Realtime and files

Subscribe only to the topic needed and release it during component or process cleanup:

```js
await pb.collection('posts').subscribe('*', ({ action, record }) => {
  console.log(action, record.id);
});

await pb.collection('posts').unsubscribe('*');
```

Send file fields with the SDK's documented `FormData` or object input for the installed SDK version. Generate public or protected file URLs with `pb.files.getURL(record, record.filename)` rather than constructing paths by hand.

## Source

- https://github.com/pocketbase/js-sdk
- https://pocketbase.io/docs/

## Server runtimes and duplicate requests

In Node.js, provide an `EventSource` implementation before using realtime subscriptions. The SDK automatically cancels duplicate in-flight requests by default; set a unique `requestKey` or `requestKey: null` only when concurrent requests are intentionally distinct. For server-side rendering, create a PocketBase client for each incoming request and load/export its auth state with the framework's cookie boundary rather than sharing one auth store across users.
