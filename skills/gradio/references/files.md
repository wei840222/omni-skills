# Files

## Uploads

Uploaded files arrive as temp paths or bytes and are not a durable store. Copy anything the app must keep before the request ends.

- `gr.File(type="filepath")` returns a string path.
- `gr.File(type="binary")` returns bytes.
- A function written for one type fails silently on the other. Match the parameter to the component type.

Set a size cap when the app is reachable by anyone else. Official docs show `max_file_size` on `launch()` as either `"5mb"` or `5 * gr.FileSize.MB`. There is no documented universal 200MB default; set the cap explicitly.

```python
demo.launch(max_file_size="20mb")
```

## Downloads and serving

Return a file path the component can serve, not an ad-hoc byte blob, when the user should download a file. `gr.File` sets the download headers.

Gradio only serves files that are:

- in the app's current working directory
- in the Gradio cache (`GRADIO_TEMP_DIR` overrides the cache location)
- listed in `launch(allowed_paths=[...])`

`blocked_paths` overrides both the defaults and `allowed_paths`. If a prediction returns a path outside those roots, the file is blocked.

Do not return arbitrary user input from a function wired to `gr.File` or `gr.Image`. `lambda s: s` from text to file lets a caller pull any allowed path into the cache.

## Persistence

Copy into an app-owned directory, then return that new path:

```python
import shutil
from pathlib import Path

def keep(upload_path: str) -> str:
    dest = Path("uploads") / Path(upload_path).name
    dest.parent.mkdir(exist_ok=True)
    shutil.copy(upload_path, dest)
    return str(dest)
```

Add `uploads` to `allowed_paths` if it sits outside the working directory and the cache.
