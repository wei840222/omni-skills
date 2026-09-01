# Security & Privacy

**Default workflow is 100% offline:**
- Whisper runs locally on your machine
- Generated subtitle files stay local
- Burned-in videos stay local
- No network calls made

**Cloud APIs require explicit transfer approval:**
- Keep processing local unless the user explicitly selects AssemblyAI or Deepgram and approves sending the media to that provider.
- A configured API key enables authentication; it does not authorize a media upload.
- Use only the selected provider command after that approval.

**Privacy boundary:**
- The default workflow leaves media local.
- Basic local processing needs no internet connection.
- This skill does not persist user media or caption files externally.
