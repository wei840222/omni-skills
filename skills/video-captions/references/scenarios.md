# Common Scenarios

### YouTube Video
1. Transcribe: `whisper video.mp4 --output_format vtt`
2. Upload .vtt to YouTube Studio
3. Review auto-sync suggestions

### TikTok/Instagram Reel
1. Transcribe with word timestamps
2. Apply bold animated style
3. Burn-in: `ffmpeg -i video.mp4 -vf "subtitles=video.ass" -c:a copy output.mp4`
4. Export at platform resolution

### Netflix/Professional
1. Use Whisper large-v3 for best local accuracy
2. Export TTML format
3. Verify: 42 chars/line, 2 lines max, timing gaps
4. Include translator credit as last subtitle

### Podcast/Interview
1. Enable speaker diarization
2. Format as dialogue: `[SPEAKER]: text`
3. SDH option: include `[music]`, `[laughter]` descriptions

### Foreign Film Translation
1. Transcribe in original language
2. Translate: `--task translate` for English
3. Or use external translation + timing sync
