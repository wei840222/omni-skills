# Caption Traps

- **Hallucinations on silence** → Use VAD pre-processing or trim silent sections
- **Wrong language detection** → Specify `--language` explicitly for mixed content
- **Timing drift in long videos** → Use word timestamps + manual spot-check
- **Character limit violations** → Set `--max_line_width 42` for Netflix compliance
- **Missing speaker IDs** → Enable diarization for multi-speaker content
- **Burn-in quality loss** → Use high bitrate output (`-b:v 8M`)