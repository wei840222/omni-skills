---
name: gradio
description: >
  Build and debug Gradio demos with Blocks, per-session State, queues, file
  access, auth, and production hosting. Use when writing or fixing Gradio apps,
  event handlers, Chatbot history, share links, or reverse-proxy routes. Not
  for Streamlit, FastAPI-only APIs, or model training.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎨","requires":{"bins":["python3"]}}'
  related-skills: '{"fastapi":"Mount Gradio inside FastAPI when you need custom routes or external OAuth.","flask":"Serve a Flask app instead of a Gradio demo.","hugging-face":"Publish the demo on Spaces or pick Hub models and datasets.","mlops":"Production model serving, monitoring, and rollout beyond a demo UI.","py":"Plain Python packaging and typing outside the Gradio app."}'
---

## When to load

Load this skill to construct or debug a Gradio demo: Interface vs Blocks, per-session state, queues, file uploads, Chatbot history, auth, share links, or hosting behind a proxy.

Load one reference when the task needs that detail:

| Need | File |
| --- | --- |
| Blocks, State, events, Chatbot messages | `references/blocks-and-state.md` |
| Queue, batching, generators, startup cost | `references/queue-and-performance.md` |
| Uploads, downloads, allowed paths | `references/files.md` |
| Auth, share links, proxy, Spaces | `references/deploy-and-auth.md` |
| Official sources for version-sensitive claims | `references/sources.md` |

## Core rules

1. Use `gr.Interface` for one function and a fixed layout. Use `gr.Blocks` when the app has multiple steps, conditional UI, or custom layout. Keep one pattern per app.
2. Keep user-specific data in `gr.State()`. Pass that State as both an input and an output of the handler that updates it. Module-level globals are shared across users.
3. Store only JSON-serializable values in State (numbers, strings, lists, dicts). A custom class without a serializer is dropped.
4. Event listeners already have a queue. Set `concurrency_limit` on GPU-bound handlers, and call `demo.queue(default_concurrency_limit=...)` only to change the app-wide default.
5. Return Gradio 6 Chatbot history as a list of `{"role", "content"}` dicts. The tuple format `[(user, bot), ...]` is removed.
6. Copy uploaded temp files before the request ends if the app must keep them. Return a path the component can serve; set `max_file_size` on `launch()` before exposing uploads.
7. Put credentials in an auth callable or Space OAuth, not a plaintext `auth=("user", "pass")` tuple in source. Treat `share=True` as a public one-week proxy, not production hosting.
8. Bind `server_name="0.0.0.0"` only when external clients must reach the process. Behind a subpath proxy, set `root_path` so assets and API routes resolve.

## Failure branches

| If this happens | Do this |
| --- | --- |
| Second user hangs on a GPU call | Set `concurrency_limit=1` or a shared `concurrency_id`; queue is already on |
| Counter resets after a click | Include `gr.State` in that handler's `outputs` |
| Chatbot renders blank on Gradio 6 | Return `{"role", "content"}` dicts, not `(user, bot)` tuples |
| Download 404s behind a subpath | Set `root_path` to the public prefix |
| Upload path vanishes after the handler | Copy the temp file before returning |

## Do not

- Call `demo.queue()` as the only fix for concurrency. Listeners already queue; set `concurrency_limit`.
- Store user data in a module global. That value is shared across sessions.
- Return Chatbot tuples on Gradio 6. That format was removed.
- Ship `share=True` or `auth=("user", "pass")` as the production gate.
- Return a user-supplied path from a text box into `gr.File`. That copies an allowed file into the cache.

## Output gates

Before calling a Gradio change done:

- Layout choice is Interface or Blocks, not a mix
- User-specific values live in `gr.State` and round-trip as input and output
- Chatbot history uses message dicts when targeting Gradio 6
- Queue concurrency is set on the handler that needs it
- Uploads have a size cap and a persistence copy when files must outlive the request
- Public share links and plaintext auth tuples are absent from the production path
