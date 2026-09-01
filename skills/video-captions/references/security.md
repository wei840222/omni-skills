# Security & Privacy

**Default workflow is 100% offline:**
- Whisper runs locally on your machine
- Generated subtitle files stay local
- Burned-in videos stay local
- No network calls made

**Cloud APIs are OPTIONAL and OPT-IN:**
- Only used if you set `ASSEMBLYAI_API_KEY` or `DEEPGRAM_API_KEY`
- Only triggered when you explicitly use cloud engine commands
- By keeping these keys unset, all audio processing remains entirely local on your machine

**This skill does NOT:**
- Upload anything by default
- Require internet connection for basic use
- Store data externally
