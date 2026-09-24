# Blocks, State, and events

## Interface vs Blocks

- `gr.Interface(fn, inputs, outputs)` fits a single function and a fixed layout.
- `gr.Blocks` is the path for multiple steps, conditional UI, or custom layout. It exposes `.click()`, `.change()`, and `.submit()`.
- Mixing an Interface inside Blocks creates two state models. Pick one pattern per app.

## State

`gr.State()` is per browser session. A refresh starts a new session and resets it.

```python
import gradio as gr

def increment(count):
    return count + 1, count + 1

with gr.Blocks() as demo:
    count = gr.State(0)
    btn = gr.Button("Click")
    output = gr.Number(label="Count")
    btn.click(increment, inputs=count, outputs=[count, output])

demo.launch()
```

- Pass State as an input and include it in `outputs` on every handler that mutates it. Omitting the output drops the update.
- Keep values JSON-serializable. Dicts and lists round-trip; a custom class without a serializer does not.
- A module-level counter or cache is shared across users. Use it only for read-only process data such as a loaded model.

## Events and updates

- Return `gr.update(value=x, visible=True)` to change component properties. A bare return updates the value only.
- Chain dependent work with `.then()`. Separate `.click()` handlers on the same control race.
- `every=5` polls every 5 seconds and holds connections. Use it for a small status panel, not a heavy inference loop.
- `trigger_mode="once"` collapses rapid repeat clicks. The default accepts duplicate submissions.

## Components that fail quietly

- `gr.Dropdown` with `allow_custom_value=False` needs a default or optional handling when the user submits an empty value.
- `gr.Image(type="pil")` returns a PIL image, `type="numpy"` an array, and `type="filepath"` a path. Match the function signature to the type.
- `visible=False` still runs the component's functions. Use `gr.update(interactive=False)` to disable input while keeping the component mounted.

## Chatbot history (Gradio 6)

Gradio 6 removed the tuple format. History is a list of message dicts:

```python
history.append({"role": "user", "content": user_text})
history.append({"role": "assistant", "content": reply})
return history
```

Gradio 5 accepted `type="tuples"` and `[(user, bot), ...]`. A Gradio 6 app that still returns tuples does not render. Pin the installed major version before copying an older snippet.
