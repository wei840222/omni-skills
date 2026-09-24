# Sources

Version-sensitive claims in this package were checked against these pages on 2026-09-24. Re-read the page before stating a default that may have moved.

## Queue

- **Queuing** — every event listener already has a queue; default concurrency is 1; configure with `concurrency_limit`, `default_concurrency_limit`, and `concurrency_id`. https://www.gradio.app/guides/queuing

## Chatbot history

- **Gradio 6 Migration Guide** — tuple chatbot history is removed; use message dicts with `role` and `content`. https://www.gradio.app/guides/gradio-6-migration-guide

## Files

- **Security and File Access** — serving is limited to the working directory, Gradio cache, and `allowed_paths`; `max_file_size` is an explicit `launch()` cap (examples use 5 MB). https://www.gradio.app/guides/file-access

## Sharing and auth

- **Sharing Your App** — share links expire after 1 week; built-in auth is a basic gate; Spaces OAuth uses `hf_oauth: true`. https://www.gradio.app/guides/sharing-your-app

## Corrected claims

| Old package claim | Replacement |
| --- | --- |
| Call `demo.queue()` or every user blocks | Queue is automatic; set concurrency when the default of 1 is wrong |
| Chatbot expects `[(user, bot), ...]` | Gradio 6 expects `{"role", "content"}` dicts |
| Share links last 72 hours | Share links expire after 1 week |
| Uploads default to 200MB | Set `max_file_size`; docs do not state a 200MB default |
