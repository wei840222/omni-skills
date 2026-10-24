# Official Sources & API References

This document records the official developer documentation and API endpoint references for the MiniMax model ecosystem.

## Official Portals & Developer Documentation

- **MiniMax Developer Platform Docs**: [https://platform.minimax.cn/docs/guides/models-intro](https://platform.minimax.cn/docs/guides/models-intro)
  - Model capabilities, token limits, and integration guides for MiniMax text models (abab 6.5s, MiniMax-Text-01).
- **MiniMax Global Portal**: [https://www.minimax.io/](https://www.minimax.io/)
  - Product announcements, Hailuo AI video generation, and voice synthesis technology overview.

## API Interfaces & Protocol Compatibility

- **Chat Completions**:
  - Native Chat Completion API (`/v1/text/chatcompletion_v2`)
  - Anthropic-compatible protocol headers and OpenAI-compatible endpoint mapping (`/v1/chat/completions`).
- **Speech Generation (T2A)**:
  - Text-to-Audio v2 (`/v1/t2a_v2`): High-definition voice cloning and emotional timbre synthesis.
- **Video Generation**:
  - Hailuo Video API asynchronous polling endpoints (`/v1/video_generation`).
