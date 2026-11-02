# Why Crush Is the Best‑Looking AI Coding CLI (RIP Claude Code?)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `kCcCxzCSf_w` · [watch](https://youtu.be/kCcCxzCSf_w) · **date:** 2025-11-02 · **length:** 4:53 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Presenter (Better Stack channel host, unnamed in transcript) · **orgs:** Charm, SST, Anthropic, OpenAI, Better Stack
- **topics:** coding-agents, claude-code, dev-tools · **tags:** crush, charm, opencode, claude-code, terminal-ui, coding-agent-cli, byok-api-keys, lsp, mcp, permissions, whisper, vite, react, crush.json, CRUSH.md

> A short hands-on look at Charm's Crush, a terminal AI coding CLI, compared against Claude Code and OpenCode on one React app prompt. It looks polished, but it trails on features and only supports API keys.

## Summary
The presenter tries Charm's Crush, a terminal coding agent that was renamed from OpenCode after a naming dispute. The tour covers the TUI: a permission modal for tool calls with an "allow for session" key, auto-generated session names, a sidebar with model, context percentage, price, modified files, LSPs and MCP servers, and a Ctrl+P command palette instead of slash commands. Crush only accepts API keys, so Claude Pro or Max subscriptions do not work, though local models, LSPs and MCP servers can be set up in crush.json. For a quality check, the same prompt (a Vite + React app that drag-and-drops an MP3 and transcribes it with OpenAI's Whisper API) was run in Crush, OpenCode and Claude Code, all on Claude Sonnet 4 in YOLO mode, each finishing in just under two minutes. The apps differed mainly in UX: Crush was drag-and-drop only with hard-to-read text, OpenCode supported click-to-select, and Claude Code needed a follow-up prompt for a server error but added a spinner and created a server.js so the API key stayed off the frontend. The presenter concludes Crush uses less memory and has good logging, but lacks hooks, plugins, subagents and built-in formatters, and leaves the question of whether it stands out open.

## Key ideas
- **Crush is Charm's terminal coding agent, originally named OpenCode. It was renamed after a split with the SST TypeScript OpenCode project, which the presenter already uses.** — Naming history explains why it was renamed; the two are separate projects now. ([0:00](https://youtu.be/kCcCxzCSf_w?t=0))
- **Crush's TUI is the main draw: tool calls go through a permission modal with an allow-for-session option, and the sidebar shows the session name, model, context-use percentage, price, modified files, LSPs and MCP servers.** — The modified-files sidebar is the feature the presenter liked most; the context and price readout is shown during a session. ([0:00](https://youtu.be/kCcCxzCSf_w?t=0))
- **Crush has no slash commands. The slash key is for file access and Ctrl+P opens a palette to switch sessions, switch models (large vs small), and change system or custom prompts from a commands folder.** — Keyboard-first UX is the main departure from Claude Code's slash-command model. ([1:21](https://youtu.be/kCcCxzCSf_w?t=81))
- **Crush only accepts provider API keys, so a Claude Pro or Max subscription does not work. Local models are supported, and LSPs and MCP servers are configured in crush.json.** — A real adoption blocker for subscription users, stated as a current limitation. ([1:21](https://youtu.be/kCcCxzCSf_w?t=81))
- **On one shared prompt, Crush, OpenCode and Claude Code (all Sonnet 4, YOLO mode) produced working apps in just under two minutes. Output quality differed mostly in UX and error handling.** — Single run per tool, so this is an anecdotal comparison. Crush was drag-and-drop only with hard-to-read text and did not show a progress checklist. OpenCode supported click-to-select. Claude Code hit a server error and needed a follow-up prompt, but added a spinner and hover effects. ([2:38](https://youtu.be/kCcCxzCSf_w?t=158))
- **Claude Code wrote a server.js so the API key stayed off the frontend. The Crush and OpenCode apps put the key directly in the frontend app file.** — The presenter calls the frontend key placement poor practice, a concrete security point for generated apps. ([4:07](https://youtu.be/kCcCxzCSf_w?t=247))
- **Crush uses less memory than Claude Code and OpenCode and has a useful log view, but it is behind on extensibility: no custom hooks, plugins, subagents or built-in formatters.** — The presenter's verdict is that Crush looks best but may not be enough to stand out among AI CLIs. ([4:07](https://youtu.be/kCcCxzCSf_w?t=247))

## Techniques
- **Same-prompt cross-CLI comparison** — Put the app spec in one prompt file (here a Vite + React template with a prompt file), then run that identical prompt in each CLI with the same model (Claude Sonnet 4) in YOLO mode. Compare time to finish and the output, including whether the app runs and whether the API key is server-side. *When:* Quick, cheap way to compare coding agents on one realistic build. A single run per tool is noisy, so repeat it before trusting it.
- **Permission modal: allow for session** — When Crush's permission modal asks to allow a tool such as bash, press F to allow that tool for the whole session instead of approving each call. *When:* Long agent runs where you trust a specific tool and want fewer prompts.
- **Init a project memory file** — Open Crush in a new project. It offers to initialize a CRUSH.md file. Press Enter or Y, then approve the follow-up permission modal for the write. *When:* Starting a new repo so the agent gets project context on its first run. This is Crush's counterpart to CLAUDE.md or AGENTS.md.
- **Keyboard navigation in Crush** — Ctrl+P opens the command palette (switch session, switch model between large and small, change system vs custom prompt; custom prompts live in a commands folder). Ctrl+F attaches an image, Ctrl+R followed by an index removes one, Tab moves focus from the prompt to the chat. In chat, use arrow keys or k/j to move, gg for top, G for bottom. There is no vim mode when typing a prompt. *When:* Daily driving the TUI, especially for Vim users browsing chat output.
- **Configure LSPs and MCP servers in crush.json** — Add LSP servers and MCP servers to a crush.json file, and point Crush at local models there too. The video does not show the exact schema. *When:* Adding language intelligence or tools to Crush beyond its defaults, or using a local model instead of a hosted API key.
- **Check where generated apps put API keys** — Review the generated code for keys in frontend files. Prefer a small server.js (or other backend) that holds the key and proxies the Whisper call, as Claude Code did in the test. *When:* Reviewing any agent-generated app that calls a paid API from the browser.

## Numbers
- Claude Code, OpenCode and Crush each finished the same app-building prompt in just under two minutes (single run each, Sonnet 4, YOLO mode). ([2:38](https://youtu.be/kCcCxzCSf_w?t=158))
- Crush uses less memory than Claude Code and OpenCode. No figures are given. ([4:07](https://youtu.be/kCcCxzCSf_w?t=247))
- Crush's sidebar shows the context-use percentage and the session price during a session. No values are given. ([0:00](https://youtu.be/kCcCxzCSf_w?t=0))

## Hot takes
- The title's 'RIP Claude Code?' framing is not supported by one five-minute, single-run test. Claude Code's server.js handling of the API key was the strongest result.
- Crush's TUI polish is the video's main point, but the presenter also says it is behind on extensibility and only accepts API keys, which is a real limitation for subscription users.
- The app outputs were judged on one shot by eye, with no repeated runs, no test suite and no error-rate data.

## Tools mentioned
Crush (Charm terminal coding agent), OpenCode (original project, later renamed to Crush), OpenCode (SST, TypeScript version), Claude Code, Claude Sonnet 4, OpenAI Whisper API, Vite, React, LSP servers, MCP servers, crush.json, CRUSH.md

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, so a competing CLI and its permission-prompt UX are a useful reference point. The API-key-in-frontend note also bears on zero-token credential handling. → *When reviewing ProsHarness approval and permission flows, compare them with Crush's allow-for-session modal, and add a check that generated apps keep API keys server-side.*
