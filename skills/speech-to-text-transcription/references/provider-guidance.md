# Provider guidance

Read this reference when selecting a cloud provider, checking a request example, or confirming a provider-specific limit. Prefer the provider's current documentation over any remembered endpoint or model name.

## OpenAI Audio API

- [OpenAI file transcription guide](https://developers.openai.com/api/docs/guides/speech-to-text) — `/v1/audio/transcriptions`, supported formats, 25 MB upload limit, `gpt-transcribe`, and speaker diarization with `gpt-4o-transcribe-diarize`.

## AssemblyAI

- [AssemblyAI prerecorded-audio quickstart](https://www.assemblyai.com/docs/pre-recorded-audio/getting-started/transcribe-an-audio-file) — local-file handling, `speaker_labels`, SDK flow, and HTTP submission/polling behavior.

## Deepgram

- [Deepgram prerecorded-audio guide](https://developers.deepgram.com/docs/pre-recorded-audio) — authenticated local and remote transcription requests and current `nova-3` examples.

## Local Whisper

- [OpenAI Whisper repository](https://github.com/openai/whisper) — installation requirements, `ffmpeg` dependency, supported CLI usage, and model trade-offs.
