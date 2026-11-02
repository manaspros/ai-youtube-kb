# INK: The React Library POWERING AI Terminal Tools (For Now...)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `qSZwx5_EmSA` · [watch](https://youtu.be/qSZwx5_EmSA) · **date:** 2025-11-02 · **length:** 4:24 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Anthropic, Google, OpenAI, OpenCode
- **topics:** dev-tools, coding-agents · **tags:** ink, react, terminal-ui, typescript, opentui, bubble-tea, memory-footprint, cli, yoga-layout

> Quick Ink (React for terminals) counter tutorial that measures its memory cost against Bubble Tea and points to OpenTUI as a leaner TypeScript alternative.

## Summary
The video introduces Ink, a TypeScript library that renders React components in the terminal, and says it powers several AI coding CLIs (Qwen Code, Gemini CLI, Claude Code). The host builds a small counter app to show that web React skills transfer: a bordered Box layout, useInput-style key handling for K/J increment and decrement, and Ctrl+C to exit. He notes Ink's ecosystem (devtools, spinner packages) and that a coding LLM could build similar apps. The main point is cost: the same counter uses about 50 MB in dev mode and 32 MB bundled, versus 13 MB in dev and under 4 MB as a built binary in Go's Bubble Tea. He attributes this to the bundled JS runtime, React, and the WASM build of Yoga used for flexbox layout, and says Ink is hard-coded to 32 fps, which he links to OpenAI moving Codex CLI to Rust. He then points to OpenTUI (Zig core with TypeScript bindings via Bun FFI, from the OpenCode team) as a promising TypeScript option: his OpenTUI version of the app used less memory than Ink but more than Bubble Tea. The video ends with a sponsor segment for Better Stack.

## Key ideas
- **Ink brings React to the terminal, and it powers several AI coding CLIs** — The host names Qwen Code, Gemini CLI and Claude Code as Ink-based tools (his claims; the video does not verify them). ([0:00](https://youtu.be/qSZwx5_EmSA?t=0))
- **Web React skills transfer directly to terminal apps** — A counter app is built with hooks, a bordered column Box, a Fragment wrapper, and dimmed instruction text. Keys K and J change the count, and the process only exits on Ctrl+C. ([0:00](https://youtu.be/qSZwx5_EmSA?t=0))
- **Ink has a usable ecosystem and is easy to scaffold with an LLM** — He points to React DevTools support, rendering to stdout, and extra packages such as a spinner. He notes it is not new, so an LLM could generate a similar app. ([1:26](https://youtu.be/qSZwx5_EmSA?t=86))
- **The memory cost of Ink is large for a trivial app** — The counter uses about 50 MB in dev mode and 32 MB bundled. The same app in Go with Bubble Tea uses 13 MB in dev and under 4 MB as a built executable. ([1:26](https://youtu.be/qSZwx5_EmSA?t=86))
- **Ink's footprint comes from its runtime stack, which he links to frame rate and a Rust migration** — He cites the bundled JS core runtime, React code and the WASM build of Yoga for flexbox layout. He says Ink is hard-coded to 32 fps and that OpenAI's Codex CLI moved from Ink to Rust for this reason (speculation). ([2:41](https://youtu.be/qSZwx5_EmSA?t=161))
- **OpenTUI is a TypeScript-facing alternative with a native core** — OpenTUI, from the OpenCode team, is built in Zig with TypeScript on top and calls the Zig code through Bun's FFI. His OpenTUI version of the same React-style app used less memory than Ink but more than Bubble Tea. ([2:41](https://youtu.be/qSZwx5_EmSA?t=161))
- **OpenCode is already moving its Bubble Tea UI to OpenTUI** — The host says OpenTUI is already being used to replace the Bubble Tea side of OpenCode. He hopes Anthropic and Google will consider it for future CLI tools. ([2:41](https://youtu.be/qSZwx5_EmSA?t=161))

## Techniques
- **Ink counter component pattern** — Wrap the text in a Box with borderStyle round and flexDirection column. Handle keys with the useInput hook: K increments, J decrements, and Ctrl+C is the only exit. Show the count in its own Box, add a second Box below with dimmed instructions, and wrap the whole tree in a Fragment. Use ordinary React state and hooks for the counter. The exact package install and scaffold commands are not shown. *When:* Building a small interactive terminal UI when the team already knows React. Use it only if the memory footprint is acceptable for the tool.
- **Measure the runtime footprint before choosing a TUI framework** — Compare the same app in three forms: dev mode, a bundled JS build, and a compiled executable. Record memory for each (the host reports about 50 MB dev, 32 MB bundled for Ink, against 13 MB dev and under 4 MB built for Bubble Tea). The method used is not described. *When:* Before committing to a terminal UI framework for a long-running or frequently launched CLI, where startup and resident memory matter.
- **Keep the TUI process alive until an explicit exit key** — Use useInput to listen for keypresses and exit only when Ctrl+C is pressed, so the terminal app does not close on other input. *When:* Interactive terminal tools that should stay open while the user works.

## Numbers
- Ink counter app memory: about 50 MB in dev mode, 32 MB as a bundled build ([1:26](https://youtu.be/qSZwx5_EmSA?t=86))
- Bubble Tea (Go) counter app memory: 13 MB in dev mode, under 4 MB as a built executable ([1:26](https://youtu.be/qSZwx5_EmSA?t=86))
- Ink is hard-coded to render at 32 frames per second (speaker's statement) ([2:41](https://youtu.be/qSZwx5_EmSA?t=161))
- The speaker's OpenTUI version of the app uses less memory than Ink and more than Bubble Tea. No exact figure is given. ([2:41](https://youtu.be/qSZwx5_EmSA?t=161))

## Hot takes
- React in a terminal is not automatically a performance problem, but Ink's memory overhead for a trivial counter (about 32 MB bundled) is hard to justify for a CLI.
- The Codex CLI move from Ink to Rust is linked to Ink's 32 fps cap, which is speculation.
- OpenTUI (Zig core with TypeScript bindings) is the TypeScript terminal library to watch, and the host wants Anthropic and Google to adopt it.
- Memory numbers come from one counter app, single runs, with no methodology given. Treat them as a rough indicator.
- Sponsored segment for Better Stack at the end (about 4:06). Quality is capped at 2 for this reason.

## Tools mentioned
Ink, React, TypeScript, Yoga (WASM build, flexbox layout), Bubble Tea (Go), OpenTUI (Zig and TypeScript), Bun FFI, SolidJS implementation of OpenTUI, OpenTUI core, OpenCode, Qwen Code, Gemini CLI, Claude Code, OpenAI Codex CLI, React DevTools, Ink spinner package

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and the host says Claude Code's terminal UI is built on Ink (his claim). A TUI framework choice would matter only if ProsHarness adds its own interface. → *If ProsHarness gets a terminal UI, measure resident memory of dev vs built output for the candidate framework before choosing one (Ink used about 32 MB for a counter app in this video).*
- **general** (1/3): Shows how TUI framework choice affects memory footprint for coding-agent CLIs, a general dev-tools decision. → *Read OpenTUI's README for its current status before committing to a TypeScript terminal UI stack.*
