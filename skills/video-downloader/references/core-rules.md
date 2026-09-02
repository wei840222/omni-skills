# Core Rules

## 1. Confirm Rights and Target First
- Ask for the exact URL and intended use when unclear.
- If the request implies unauthorized copying, refuse and suggest legal alternatives.

## 2. Inspect Metadata Before Downloading
- Run metadata check first to confirm title, duration, and available formats.
- If metadata fetch fails, stop and report the exact error and halt execution immediately to allow user correction.

## 3. Match Quality to User Intent
- Use `best` when user says "highest quality".
- Use capped quality (`1080p`, `720p`, etc.) for smaller files or device limits.
- Use audio-only mode only when they explicitly want audio extraction.

## 4. Use Deterministic Output Names
- Save files as `%(title)s [%(id)s].%(ext)s` to reduce collisions.
- Keep downloads in a user-approved directory and limit all writes exclusively to it.

## 5. Prefer the Local Wrapper Script
- Use `python3 download_video.py "<url>" ...` for consistent behavior.
- Fall back to raw `yt-dlp` commands only if the user asks for custom flags not covered by the script.

## 6. Verify Output Before Declaring Success
- Confirm file exists, extension matches request, and size is non-zero.
- For audio-only downloads, confirm output is `.mp3`.
