# Visual Studio Code Architecture and Extensions

Visual Studio Code (commonly referred to as VS Code) is a source-code editor developed by Microsoft for Windows, Linux, and macOS.

## Key Architecture Concepts
- **Electron:** VS Code is built using the Electron framework, which allows it to run Node.js applications on the desktop.
- **Language Server Protocol (LSP):** Standardizes the communication between development tools and language smartness providers (Language Servers). This allows VS Code to support features like IntelliSense and refactoring across many languages.
- **Extension Host:** VS Code runs extensions in a separate process called the Extension Host. This ensures that extensions cannot crash the main editor process or slow down the UI.
- **Debug Adapter Protocol (DAP):** Similar to LSP, DAP standardizes how the editor communicates with debuggers.

## Remote Development
The Remote Development extension pack allows you to open any folder in a container, on a remote machine, or in the Windows Subsystem for Linux (WSL) and take advantage of VS Code's full feature set.
- The UI runs locally, while the workspace, files, and extensions run remotely.
- `devcontainer.json` defines how a development container should be built and started.

## Sources

- Wikipedia: Visual Studio Code — `https://en.wikipedia.org/wiki/Visual_Studio_Code`
- VS Code Settings — `https://code.visualstudio.com/docs/getstarted/settings`
- VS Code Debugging — `https://code.visualstudio.com/docs/editor/debugging`
- VS Code Remote Development — `https://code.visualstudio.com/docs/remote/remote-overview`
