# Queue and performance

## What the queue already does

Current Gradio creates a queue for every event listener. You do not need `demo.queue()` before `launch()` merely to stop one long call from blocking every other user.

Defaults:

- Each listener handles one request at a time (`concurrency_limit` defaults to 1).
- Extra requests wait until a slot frees.
- Change the app-wide default with `demo.queue(default_concurrency_limit=N)`.
- Raise one handler with `btn.click(fn, concurrency_limit=5)`.
- Share a scarce resource across handlers with the same `concurrency_id` (for example two GPU functions on one device).

```python
import gradio as gr

def generate(prompt):
    return prompt

with gr.Blocks() as demo:
    prompt = gr.Textbox()
    out = gr.Textbox()
    btn = gr.Button("Generate")
    btn.click(generate, inputs=prompt, outputs=out, concurrency_limit=1)

demo.queue(default_concurrency_limit=4)
demo.launch()
```

Set `concurrency_limit=1` (or a shared `concurrency_id`) on GPU-bound inference that cannot run in parallel. A generator that `yield`s streams output and holds its queue slot until it finishes.

## Batching and startup cost

- `batch=True` with `max_batch_size=N` groups concurrent calls. Use it when the model benefits from batched GPU throughput.
- Load large models in process scope, or initialize them once into `gr.State`, instead of reloading inside the request function.
- `cache_examples=True` precomputes example outputs at startup. Demos start slower and then serve those examples without rerunning the function.

## Recovery

| Symptom | First move |
| --- | --- |
| Second user waits forever on a GPU call | Lower `concurrency_limit` or share a `concurrency_id` across GPU handlers |
| Queue memory grows without bound | Cap the listener queue (`max_queue` on the event) and fail fast with a status message |
| Streaming response never releases the worker | Finish or cancel the generator; a `yield` loop holds the slot until return |
| Cold start on every request | Move model load to process scope |
