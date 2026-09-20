# Image Edit Sources

## Inpainting / generative fill
- OpenAI image editing overview — mask-based edits and prompt-guided fill via https://platform.openai.com/docs/guides/images
- Stability AI inpainting concepts — latent fill and mask workflows via https://stability.ai/stable-image
- Black Forest Labs Flux fill / edit family — generative fill model notes via https://blackforestlabs.ai/

## Background removal / segmentation
- remove.bg API docs — automated background removal via https://www.remove.bg/api
- Meta Segment Anything — interactive segmentation for precise masks via https://ai.meta.com/sam/
- Photoroom API — product/cutout background workflows via https://www.photoroom.com/api

## Upscaling / restoration
- Real-ESRGAN project — practical image super-resolution via https://github.com/xinntao/Real-ESRGAN
- GFPGAN project — face restoration priors via https://github.com/TencentARC/GFPGAN
- CodeFormer project — robust face restoration via https://github.com/sczhou/CodeFormer
- Topaz Labs Gigapixel — commercial upscaling reference via https://www.topazlabs.com/gigapixel

## Outpainting / relight / style
- ClipDrop tools — background, relight, and cleanup utilities via https://clipdrop.co/
- IC-Light project — illumination-conditioned relighting via https://github.com/lllyasviel/IC-Light
- ControlNet overview — conditioned img2img / structure-preserving edits via https://github.com/lllyasviel/ControlNet

## Quality practice
- Non-destructive edit pipeline: keep originals, edit copies, upscale last
- Prefer iterative small masks over one-shot large canvas expansion
