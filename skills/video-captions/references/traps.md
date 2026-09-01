# Caption Traps

- **Hallucinations on silence** → Use VAD pre-processing or trim silent sections
- **Wrong language detection** → Specify `--language` explicitly for mixed content
- **Timing drift in long videos** → Use word timestamps + manual spot-check
- **Character limit violations** → For OpenAI Whisper, use `--word_timestamps True --max_line_width 42`; then validate the delivered caption file against the target platform requirements
- **Missing speaker IDs** → Enable diarization for multi-speaker content
- **Burn-in quality loss** → Use high bitrate output (`-b:v 8M`)
