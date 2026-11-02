# Vercel Built a Terminal Emulator and It's Only 12KB

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `MxACQUVS5mE` · [watch](https://youtu.be/MxACQUVS5mE) · **date:** 2026-06-02 · **length:** 5:56 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Vercel, Better Stack, Coda (GhosttyWeb), Hetzner, Ghostty
- **topics:** dev-tools, sandboxing-execution · **tags:** web-terminal, terminal-emulator, dom-rendering, xterm-js, webassembly, zig, libghostty, websocket, pty, react, accessibility

> Better Stack walks through Vercel's Wterm, a web terminal that renders to the DOM instead of a canvas, with a 12KB Zig/WASM core and an optional libghostty renderer; it covers WebSocket wiring and the rough edges.

## Summary
A Better Stack presenter demos Wterm, a web terminal emulator from Vercel that renders terminal output as ordinary DOM HTML rather than to a canvas like xterm.js. Because the output is HTML, text selection, browser find and screen readers work without extra work, and the Zig core re-renders only the rows that changed. The core compiles to a roughly 12KB WASM binary, and an optional WtermGhostty package swaps in libghostty for better terminal compatibility and colors at about 400KB. The demo installs Wterm into a React app, shows that the client does nothing until it is connected to a backend, and then builds a Node WebSocket server that spawns a pseudo-terminal on a Hetzner Ubuntu box, with the client using Wterm's WebSocket transport (auto-reconnect, resize handling). The presenter reports that the libghostty renderer had glitches with Neovim and OpenCode and needed a WASM import under Bun, and points to GhosttyWeb (libghostty as a drop-in xterm.js replacement, still canvas-based) as an alternative. The video is a short overview, not a full build guide, so exact package names and setup commands are mostly not shown.

## Key ideas
- **Wterm renders terminal output to the DOM rather than a canvas, so selection, browser find and screen readers work without re-implementing them.** — Xterm.js, the default for web terminals (Codespaces, Portainer, VS Code, Cursor), draws to a canvas, which forces selection and find to be rebuilt from scratch. ([0:00](https://youtu.be/MxACQUVS5mE?t=0))
- **The Zig core is small (about 12KB WASM) and only re-renders the HTML rows that changed rather than the whole terminal each frame.** — The core diffs output and patches only the changed part of the DOM. Wterm also has bindings for React and Vue and supports theming. ([1:01](https://youtu.be/MxACQUVS5mE?t=61))
- **A browser terminal is only a front end; something on a real machine has to run a pseudo-terminal and relay keystrokes and output.** — Keystrokes go over a WebSocket to a server, which feeds them to a pty of matching dimensions and sends the full output back. Without this the demo terminal accepts input but shows nothing. ([2:02](https://youtu.be/MxACQUVS5mE?t=122))
- **The client side needs resize handling and a column/row size that matches the server-side pty, plus automatic reconnects.** — The Wterm WebSocket transport handles reconnects and sends keystrokes. The server returns the whole output stream rather than only changed rows; the DOM diffing happens on the client. ([3:19](https://youtu.be/MxACQUVS5mE?t=199))
- **The default Zig renderer produced unreadable characters on selection; the libghostty-backed renderer fixed readability and colors but is much larger.** — Ghostty renders colors slightly better and handles emoji and OpenCode output. The presenter's advice is to use the Zig core if size matters. ([4:23](https://youtu.be/MxACQUVS5mE?t=263))
- **The presenter found the libghostty path rough in practice: rendering glitches with Neovim and OpenCode, and a Bun build issue.** — Bun would not copy non-JS files from node_modules, so the WASM file had to be imported manually. The DOM approach still gives accessibility and native browser features for free, which xterm.js has struggled to match. ([5:33](https://youtu.be/MxACQUVS5mE?t=333))
- **Xterm.js remains the safe default because of its ecosystem and maturity; GhosttyWeb is an alternative that keeps the xterm.js API but uses libghostty (still canvas-based).** — The presenter frames Wterm as a different trade-off (DOM rendering) rather than a clear replacement. The video does not benchmark either option. ([5:33](https://youtu.be/MxACQUVS5mE?t=333))

## Techniques
- **DOM-rendered web terminal** — Install Wterm for React, import the component and its CSS, and render it in the app. The output is plain HTML, so browser find, text selection and screen readers work without extra code. The video uses this with the default Zig core. *When:* When a browser terminal needs native find, selection and accessibility, and you want to avoid re-implementing them on a canvas.
- **WebSocket pty bridge** — Run a Node server with a WebSocket endpoint (the video uses /api/terminal) that spawns a pseudo-terminal named to match the TERM type and the client's cols/rows. Forward each keystroke from the client into the pty and send the output back. On the client, use Wterm's WebSocket transport for auto-reconnect, and forward browser resize events so the pty dimensions match. *When:* To give a browser terminal a real shell on a local or remote machine. Keep the pty dimensions identical on client and server, or the output wraps incorrectly.
- **Swap in the libghostty renderer** — Use the WtermGhostty package, which replaces the Zig core call with libghostty. In React, load the Ghostty core and pass it as a prop to the component. In the video, the Bun frontend also needed the WASM file imported explicitly because Bun does not copy non-JS files from node_modules. *When:* When you need better colors, emoji and terminal-app compatibility and can accept a roughly 400KB bundle plus some rendering risk with full-screen TUIs like Neovim.
- **Browser demo fallback without a backend** — The video says Wterm can run a bash-style fake filesystem in the browser with no backend, and can render Markdown as terminal output. It did not show the commands or config. *When:* For a static demo or a sandbox-free preview of a terminal UI.

## Numbers
- Wterm Zig core compiles to a roughly 12KB WASM binary. ([0:00](https://youtu.be/MxACQUVS5mE?t=0))
- The libghostty-based build is about 400KB, versus 12KB for the Zig core. ([4:23](https://youtu.be/MxACQUVS5mE?t=263))
- Xterm.js has been around for more than 10 years and is the default for web terminals. ([4:23](https://youtu.be/MxACQUVS5mE?t=263))

## Hot takes
- The 12KB headline describes only the Zig core, which lacks full terminal compatibility; the libghostty build is about 400KB and the presenter found it had rendering issues with Neovim and OpenCode.
- The presenter calls DOM rendering a real advantage for accessibility and native browser features, while noting that xterm.js has the bigger ecosystem and is the safer default.
- The video is an overview with no benchmarks, so claims about DOM-rendering performance are unverified.

## Tools mentioned
Wterm (Vercel), WtermGhostty, libghostty, Ghostty, GhosttyWeb (Coda), xterm.js, Zig, WebAssembly, React, Vue, Node.js, Bun, WebSocket, Hetzner, Ubuntu, Vim, Neovim, OpenCode, GitHub Codespaces, Portainer, VS Code, Cursor

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, so a browser console for a remote run could use a pty bridge like this one. The talk does not cover checkpoints, approvals or credentials. → *If ProsHarness ever needs a browser view of a remote Claude Code session, evaluate Wterm's DOM rendering and WebSocket pty pattern against xterm.js, and keep credentials out of the terminal channel.*
