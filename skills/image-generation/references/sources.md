# Official Sources & Image Model References

This document records the official documentation and model provider specifications for modern generative image workflows.

## Primary Image Providers & Frameworks

- **Black Forest Labs (FLUX.1)**:
  - Official Portal: [https://blackforestlabs.ai/](https://blackforestlabs.ai/)
  - Models: FLUX.1 [schnell] (distilled, 1-4 steps), FLUX.1 [dev] (guidance-distilled, non-commercial), and FLUX.1 [pro] (API).
- **OpenAI Images API (DALL-E)**:
  - Documentation: [https://platform.openai.com/docs/guides/images](https://platform.openai.com/docs/guides/images)
  - Features: Text-to-image generation with DALL-E 3 (`1024x1024`, `1024x1792`, `1792x1024`), image editing (inpainting/masking), and automatic prompt enhancement.
- **Google Cloud Vertex AI (Imagen)**:
  - Documentation: [https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/overview)
  - Capabilities: Enterprise image generation, subject-consistent multi-turn editing, and digital watermarking (SynthID).
- **Stability AI & Open-Weight Ecosystem**:
  - Stability AI: [https://stability.ai/](https://stability.ai/) (Stable Diffusion 3.5, SDXL).
  - Hugging Face Diffusers: [https://huggingface.co/docs/diffusers/index](https://huggingface.co/docs/diffusers/index) (Standard inference pipeline library for local weights and LoRA adapters).
