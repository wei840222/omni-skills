### 1. Launch News.app with Deterministic Paths
- Prefer opening News by absolute app path: `open /System/Applications/News.app`.
- Always use absolute app paths like `open /System/Applications/News.app` as some locales may not support app names.

### 2. Treat Apple News Links as the Primary Read Interface
- For direct article reads, prefer `https://apple.news/...` links and open them in News.app.
- Validate URL shape before launch and reject malformed links.

### 3. Use Search Fallbacks Explicitly
- If user asks for topic search and no direct Apple News link is available, use a user-owned Shortcut workflow when configured.
- If no search shortcut is configured, ask for one target source or one reference link before proceeding.

### 4. Preview Actions Before Opening
- Show which URL or shortcut will run before execution.
- For query text that may contain sensitive terms, require explicit confirmation before launch.

### 5. Confirm High-Impact Opens
- Always require confirmation before opening multiple links in one step.
- For more than one link, show count and require a second explicit confirmation.

### 6. Verify Launch Result State
- After launch, confirm expected state: app opened, target link opened, or shortcut completed.
- If expected state is not reached, stop and switch to a safer fallback path.

### 7. Keep Data Exposure Minimal
- Use only links and fields needed for the requested read task.
- Only send data to explicitly declared third-party APIs.
