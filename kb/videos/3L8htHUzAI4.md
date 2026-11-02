# Terax: One Developer Built an AI Terminal Better Than Warp

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `3L8htHUzAI4` · [watch](https://youtu.be/3L8htHUzAI4) · **date:** 2026-06-02 · **length:** 6:07 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed in transcript) · **orgs:** Better Stack, Warp, Vercel, Tauri, Ghostty
- **topics:** dev-tools, coding-agents, context-engineering · **tags:** terax, tauri, rust, ai-terminal, warp, cmux, neovim, helix, codemirror, xterm-js, vercel-ai-sdk, plan-mode, terax-md, agent-diffs, x-frame-options, nix

> Review of Terax, a small open-source AI terminal and code editor built with Tauri 2 and Rust, compared against Warp and CMUX; the reviewer keeps Warp and Neovim for daily work.

## Summary
Better Stack reviews Terax, an open-source terminal app built with Tauri 2 and Rust that bundles a multi-tab terminal, a CodeMirror 6 editor, a file preview sidebar, an embedded browser, and an AI agent. The reviewer says the app is about 7 MB, starts in under 300 ms, and avoids Electron's bundled Chromium. The agent can use any model through the Vercel AI SDK, including local ones, and proposes edits as diffs the user accepts or rejects. Its plan and build modes and an init subcommand that generates a TERAX.md project file mirror the CLAUDE.md or AGENTS.md pattern. The reviewer lists real gaps: Neovim crashed in his Nix and fish setup, the sidebar cannot be driven from the keyboard, zoom is missing, and non-localhost sites fail with X-Frame-Options. He positions Terax as a code-focused agentic terminal, whereas CMUX gives agents control over panes, tabs and the sidebar for multi-agent work. The video is a short, mostly balanced single-tool walkthrough, not a sponsored piece.

## Key ideas
- **Terax is an open-source AI-native terminal that combines a multi-tab terminal, code editor, file preview sidebar, and embedded browser in one small app.** — Speaker positions it against Warp: a single developer built it as a faster, lighter alternative with AI integrated for coding rather than added on. ([0:00](https://youtu.be/3L8htHUzAI4?t=0))
- **Tauri 2 instead of Electron is the reason the app is about 7 MB and starts in under 300 ms.** — Skipping the bundled Chromium saves roughly 200 MB. Rust owns PTY, filesystem and process management; React only renders the UI. ([0:47](https://youtu.be/3L8htHUzAI4?t=47))
- **The terminal and editor are built on established components rather than custom ones.** — Xterm.js with the WebGPU renderer (the same renderer VS Code uses) and CodeMirror 6 for editing. The author chose not to use libghostty for the terminal. ([0:47](https://youtu.be/3L8htHUzAI4?t=47))
- **The built-in agent works like a coding CLI with reviewable changes: it reads the codebase, answers questions about an open file, and proposes diffs.** — Model is selectable and API keys are stored in the native OS keyring. Context usage is shown and previous sessions can be resumed for follow-up questions. ([1:54](https://youtu.be/3L8htHUzAI4?t=114))
- **Plan and build modes plus an init subcommand make Terax's agent workflow similar to CLAUDE.md/AGENTS.md conventions.** — Plan mode is read-only planning, build mode returns to edits, and init scans the project and writes a TERAX.md file shown as a diff to accept or reject. ([2:50](https://youtu.be/3L8htHUzAI4?t=170))
- **A privacy page hides a tab from the AI agent, so the agent cannot read that content.** — The browser tab includes a list of common local ports, which allows running an app in one tab and editing its code in another. ([3:16](https://youtu.be/3L8htHUzAI4?t=196))
- **The reviewer lists concrete gaps: Neovim crashed in his Nix and fish setup, sidebar navigation needs the mouse, zoom is missing, and non-localhost sites hit X-Frame-Options errors.** — He says the app runs Helix fine, and that Neovim works in Warp on the same machine, so the crash may be specific to his environment. ([4:28](https://youtu.be/3L8htHUzAI4?t=268))
- **Terax and CMUX solve different problems. Terax's agent is scoped to code and files, while CMUX lets agents drive the terminal itself.** — CMUX agents can create panes and tabs, control and rename the sidebar, and spawn sub-agents, which suits multi-agent workflows. Terax agents only edit code. ([5:43](https://youtu.be/3L8htHUzAI4?t=343))

## Techniques
- **Lean desktop shell for a terminal-plus-agent app** — Put OS work (PTY, filesystem, process management) in a Rust backend and render the UI in React inside Tauri 2 instead of bundling Chromium through Electron. Terax reports about 7 MB and sub-300 ms startup. *When:* Building a desktop dev tool where startup time and footprint matter more than a full browser runtime.
- **Read-only plan mode, then build mode, for agent edits** — Terax's plan subcommand puts the agent in a planning mode that inspects code without changing it. Triggering plan again returns to build mode, which applies edits as diffs the user accepts or rejects. *When:* Before letting an agent touch a codebase, when you want the proposed plan and diff reviewed first.
- **Generate a project context file with init, then review it as a diff** — Run the init subcommand. The agent scans the whole project and writes a TERAX.md file, which appears as a diff. Accept or reject it, and request edits to the file the same way. *When:* Bootstrapping agent context for a repo that has no CLAUDE.md, AGENTS.md or equivalent.
- **Hide sensitive tabs from the agent with a privacy page** — Open a privacy page tab in Terax. The reviewer says this tab is hidden from the AI agent, so the agent cannot see its contents. *When:* When the terminal or a browser tab holds secrets or unrelated work the agent should not read.
- **Keep API keys in the OS keyring** — Terax stores OpenAI and Claude API keys in the native OS keyring instead of plaintext config. *When:* Any local agent tool that needs model API keys.

## Numbers
- App footprint is about 7 MB and startup takes under 300 ms. ([0:00](https://youtu.be/3L8htHUzAI4?t=0))
- Tauri 2 instead of Electron saves about 200 MB by avoiding a bundled Chromium. ([0:47](https://youtu.be/3L8htHUzAI4?t=47))
- Warp is reported at over 58,000 GitHub stars (speaker's figure, not verified). ([0:00](https://youtu.be/3L8htHUzAI4?t=0))

## Hot takes
- Title says 'Better than Warp', but the reviewer concludes he will keep using Warp and Neovim and says the app is not yet a 1.0.
- Reviewer says the app 'almost rivals Warp', a claim made without a feature-by-feature comparison.
- Reviewer says the project is nearly all JavaScript but feels as fast as a systems-language app, crediting the Rust Tauri core.

## Tools mentioned
Terax, Tauri 2, Rust, React, Electron (comparison), Xterm.js (WebGPU renderer), CodeMirror 6, Vercel AI SDK, Warp, CMUX, Helix, Neovim, Ghostty / libghostty, Nix, fish shell, OpenAI API, Claude API, VS Code (renderer reference)

## Relevance to our work
- **prosharness** (1/3): Terax's plan mode, init-generated project context file, and diff-based accept/reject for agent edits are small versions of ProsHarness plan and checkpoint ideas, though this is a terminal app and not a harness. → *Compare Terax's read-only plan mode to ProsHarness's plan stage, checking whether plan output is kept as a reviewable artifact before any edits.*
