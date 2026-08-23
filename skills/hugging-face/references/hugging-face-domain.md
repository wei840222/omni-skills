# Hugging Face Domain Knowledge

## APIs

- **Hugging Face Hub API**: `https://huggingface.co/docs/hub/api`
  - REST API to interact with the Hub, download models, datasets, and search/filter.
  - Endpoints: `https://huggingface.co/api/models`, `https://huggingface.co/api/datasets`, `https://huggingface.co/api/spaces`.
- **Hugging Face Inference API**: `https://huggingface.co/docs/api-inference/index`
  - Serverless API to run thousands of models via HTTP.
  - Endpoint pattern: `https://api-inference.huggingface.co/models/{model_id}`.

## Libraries

- **transformers**: Download and train state-of-the-art pretrained models.
- **datasets**: Access and share datasets for audio, computer vision, and NLP tasks.
- **diffusers**: State-of-the-art diffusion models for image and audio generation.
- **huggingface_hub**: Python library to interact with the Hugging Face Hub (download files, upload files, manage repositories).

## Access Types

- **Public**: Open to download and use.
- **Gated**: Requires user to accept terms or be granted access before downloading (e.g. Llama 2).

## Source URL for verification
- https://huggingface.co/docs/hub/api
- https://huggingface.co/docs/api-inference/index
- https://huggingface.co/docs/huggingface_hub/index
