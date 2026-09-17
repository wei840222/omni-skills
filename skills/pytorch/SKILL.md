---
name: pytorch
description: Ensure correct PyTorch implementation for training loops, evaluation
  modes, gradient controls, and model persistence. Use when an agent is writing or
  debugging PyTorch code to ensure correct device matching and clean memory management.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🔥", "requires": {"bins": ["python3"]}}'
---
## Train vs Eval Mode
- `model.train()` enables dropout, BatchNorm updates — default after init
- `model.eval()` disables dropout, uses running stats — MUST call for inference
- Mode is sticky — train/eval persists until explicitly changed
- `model.eval()` keeps gradients enabled — must also use `torch.inference_mode()` to prevent tracking

## Gradient Control
- `torch.inference_mode()` for inference — preferred over `torch.no_grad()`, enables further optimizations and reduces memory
- `loss.backward()` accumulates gradients — call `optimizer.zero_grad()` before backward
- `zero_grad()` placement matters — before forward pass, not after backward
- `.detach()` halts gradient flow — prevents memory leak in logging

## Device Management
- Model AND data must be on same device — `model.to(device)` and `tensor.to(device)`
- `.cuda()` vs `.to('cuda')` — both work, `.to(device)` more flexible
- CUDA tensors must be moved to CPU before numpy conversion — `.cpu().numpy()` required
- `torch.device('cuda' if torch.cuda.is_available() else 'cpu')` — portable code

## DataLoader
- `num_workers > 0` uses multiprocessing — Windows needs `if __name__ == '__main__':`
- `pin_memory=True` with CUDA — faster transfer to GPU
- Workers maintain independent state — random seeds differ per worker, explicitly set them in `worker_init_fn`
- Large `num_workers` can cause memory issues — start with 2-4, increase if CPU-bound

## Saving and Loading
- `torch.save(model.state_dict(), path)` — recommended, saves only weights
- Loading: create model first, then `model.load_state_dict(torch.load(path))`
- `map_location` for cross-device — `torch.load(path, map_location='cpu')` if saved on GPU
- Saving whole model pickles code path — explicitly save `state_dict` to maintain compatibility if code changes

## In-place Operations
- In-place ops end with `_` — `tensor.add_(1)` vs `tensor.add(1)`
- In-place on leaf variable breaks autograd — error about modified leaf
- In-place on intermediate can corrupt gradient — always use out-of-place operations in computation graph
- `tensor.data` bypasses autograd — legacy, prefer `.detach()` for safety

## Memory Management
- Accumulated tensors leak memory — `.detach()` logged metrics
- `torch.cuda.empty_cache()` releases cached memory — must address root cause leaks separately
- Delete references and call `gc.collect()` — before empty_cache if needed
- `with torch.inference_mode():` prevents graph storage — crucial for validation loop

## Common Mistakes
- BatchNorm with `batch_size=1` fails in train mode — use eval mode or `track_running_stats=False`
- Loss function reduction default is 'mean' — may want 'sum' for gradient accumulation
- `cross_entropy` expects logits — ensure softmax is applied internally by the loss function
- `.item()` to get Python scalar — `.numpy()` or `[0]` deprecated/error

## PyTorch 2.x Optimization
- Use `torch.compile(model)` to JIT compile models and significantly speed up training/inference
- Use `torch.autocast(device_type='cuda')` for Automatic Mixed Precision (AMP) to save memory and increase speed
- Prefer `DistributedDataParallel` (DDP) over `DataParallel` even on single-node multi-GPU setups
