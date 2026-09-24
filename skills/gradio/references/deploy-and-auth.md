# Deploy and auth

## Share links

`share=True` opens a public proxy URL through Gradio's share servers. Current docs say share links expire after **1 week**, not 72 hours. The servers proxy the local process and do not store prediction data, but anyone with the URL can call the app.

Use a share link for a temporary demo. For anything that must stay up, host on Hugging Face Spaces or your own server. `share=False` is the default except in Colab, where a share link is created automatically.

A share link plus built-in auth still sends traffic through Gradio's proxy. Use your own tunnel or host when the payload is sensitive.

## Authentication

Built-in auth is a basic gate, not multi-factor, lockout, or rate limiting.

- Prefer `auth=callable` that checks credentials outside the source file.
- A tuple `auth=("user", "pass")` embeds a password in code. Keep that out of git.
- Auth wraps the whole app. Per-route checks need a FastAPI mount and `auth_dependency`.
- On Spaces, set `hf_oauth: true` in the README and read `gr.OAuthProfile` / `gr.OAuthToken` in the handler. Local OAuth tests require `huggingface-cli login`.

Read the inbound request by adding a `gr.Request` parameter when you need headers, client IP, or query params.

## Binding and reverse proxy

- Default `server_name` is loopback. Set `server_name="0.0.0.0"` only when other hosts must connect.
- Behind a subpath reverse proxy, set `root_path` (for example `/gradio`) or static assets and API routes 404.
- Environment variables from a laptop do not exist on Spaces. Put secrets in Space secrets or the Settings UI.

## Production path checklist

- No `share=True` on the long-lived process
- No plaintext auth tuple in the repo
- `max_file_size` set
- `root_path` set when the public URL is not the app root
- Model weights loaded once, not per request
