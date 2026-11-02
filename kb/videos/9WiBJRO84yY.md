# Building on the Codex Harness — Dominik Kundel, OpenAI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `9WiBJRO84yY` · [watch](https://youtu.be/9WiBJRO84yY) · **date:** 2026-10-10 · **length:** 18:08 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dominik Kundel · **orgs:** OpenAI
- **topics:** coding-agents, agent-architecture, mcp-and-tools, context-engineering · **tags:** codex, app-server, json-rpc, agent-harness, dynamic-tools, deferred-tools, developer-instructions, codex-exec, python-sdk, ollama, lm-studio, stdio, websocket, acp, claude-code-plugin

> OpenAI's Dominik Kundel shows how to build your own client on the open-source Codex app server, the JSON-RPC protocol that wraps the Codex harness, and gives three rules for customizing it safely.

## Summary
The speaker (OpenAI, developer experience for Codex) explains the Codex app server, a JSON-RPC-style protocol that wraps the Codex agent harness. The same server powers the Codex desktop app, IDE extensions, several third-party clients, and a Codex plugin inside Claude Code. He says the harness and server are open source under Apache 2, and can point at any Responses-API-compatible model provider, including local LM Studio or Ollama. He shows a live inspector of the event stream between the Codex app and the server, then demos a custom client that runs the agent inside a Doom renderer, with game state exposed as dynamic tools. For integration he recommends either the Python SDK or simply asking Codex to implement the protocol from the docs. He contrasts the app server with the non-interactive codex exec, which suits CI scripts but not many parallel threads or eval harnesses. He closes with three rules: ship a pinned copy of the harness, expose custom functions as deferred tools, and add developer instructions instead of replacing the base system prompt.

## Key ideas
- **The app server is the protocol that wraps the Codex harness, similar in concept to Agent Client Protocol (ACP). It is open source (Apache 2), so you can fork it and point it at any Responses-API-compatible provider.** — Clients send messages to the server to act and receive events back. Local LM Studio and Ollama have convenience settings. ([1:14](https://youtu.be/9WiBJRO84yY?t=74))
- **One app server powers many clients: the Codex app, IDE extensions, third-party editors and tools, and a Codex plugin inside Claude Code.** — This is the same harness behind every surface, so a custom client gets the same agent behaviour. ([2:40](https://youtu.be/9WiBJRO84yY?t=160))
- **The protocol exposes almost everything the first-party app uses, so a custom client can match it.** — Over 120 client messages cover initialization, thread changes, setting goals, listing plugins, file search and file system access. Sign-in with ChatGPT lets end users run on their own subscription limits. ([5:29](https://youtu.be/9WiBJRO84yY?t=329))
- **Customize the agent with two levers: developer instructions and dynamic tools.** — Developer instructions are appended to Codex's system prompt, so the model-tuned base prompt is kept. Dynamic tools are functions you define, or MCP tools, and they can be marked deferred so they are found through tool search instead of filling the context window. ([6:38](https://youtu.be/9WiBJRO84yY?t=398))
- **Per-thread configuration overrides let one client run threads with different models, providers, or sandbox rules, such as network access or writable files.** — This gives fine control over each agent run from the client side. ([7:57](https://youtu.be/9WiBJRO84yY?t=477))
- **The protocol changes between versions, so generate TypeScript bindings or a JSON schema for the exact version you target and ship that binary with your app.** — Windows ships both a Linux and a native binary, so WSL mode uses the Linux one. Transport can be stdio or WebSocket. ([9:12](https://youtu.be/9WiBJRO84yY?t=552))
- **Codex exec is for scripts and CI. The app server is for interactive clients and for running many threads at once, such as eval harnesses, without writing your own parallelism around exec calls.** — The speaker lists running your own eval harness and using slash goal as cases where the app server is the better fit. ([15:35](https://youtu.be/9WiBJRO84yY?t=935))
- **Three rules for building on the harness: ship your own pinned version, expose new functions as deferred tools, and start by appending developer instructions rather than writing a new system prompt.** — He argues that a hand-written system prompt loses the prompt tuning done per model, and that deferred tools keep the context clean without confusing the agent. ([16:35](https://youtu.be/9WiBJRO84yY?t=995))

## Techniques
- **Append developer instructions instead of replacing the system prompt** — Customize the harness by adding instructions on top of the built-in system prompt, which the app server supports directly, rather than writing your own base prompt. *When:* Any time you need to adapt the agent to your product. It keeps the per-model prompt tuning the vendor did.
- **Deferred dynamic tools with tool search** — Define custom functions (or MCP tools) and mark them deferred so the agent finds them through a tool-search tool, not in the system prompt. *When:* When you expose many tools, such as app controls or game state, and do not want them to crowd the context window.
- **Pin and bundle the harness binary** — Ship the specific Codex binary with your app and generate TypeScript bindings or JSON schema from that exact version. Build against that schema. *When:* When the protocol changes between versions and users might run a different installed CLI.
- **Per-thread config overrides** — Set model, model provider, and sandbox permissions (network, writable files) for each thread from the client. *When:* When different threads or tenants need different models or safety boundaries from one client.
- **Integrate by delegating to the coding agent** — Point Codex at the app server docs and ask it to write the client. Or use the Python SDK, which handles lifecycle and ChatGPT sign-in. *When:* When building a client quickly. The speaker reports a Windows-native client built largely in one shot.
- **Choose exec or app server by parallelism and interactivity** — Use codex exec for one-shot scripted tasks, such as auto-fixing a PR in CI. Use the app server for interactive UIs, many concurrent threads, or eval harnesses. *When:* When deciding how to drive the agent from code.

## Numbers
- Over 120 client messages in the app server protocol, covering initialization, threads, goals, plugins, file search and file system access. ([5:29](https://youtu.be/9WiBJRO84yY?t=329))
- Windows ships two binaries of the harness (Linux-compiled and Windows-native), so the right one runs in WSL or native mode. ([9:12](https://youtu.be/9WiBJRO84yY?t=552))
- The harness and app server are Apache 2 licensed. ([1:14](https://youtu.be/9WiBJRO84yY?t=74))

## Hot takes
- Ship your own pinned copy of the harness instead of relying on the user's installed CLI.
- Do not write your own base system prompt. Append developer instructions to the vendor's prompt.
- Mark custom tools as deferred so they do not pollute the context window.

## Tools mentioned
Codex app server, Codex CLI, Codex exec, Codex desktop app, Python SDK (Codex), Agent Client Protocol (ACP), LM Studio, Ollama, Electron, Cloudflare Doom WASM renderer, T3 Code, Claude Code Codex plugin

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI. The talk argues that a structured, versioned protocol gives thread-level control, parallel runs and per-thread config, which the speaker contrasts with scripted one-shot exec calls. The developer-instructions and deferred-tool advice also applies to harness design. → *Check whether Claude Code exposes an equivalent structured control interface (its own JSON protocol or SDK) that ProsHarness could drive instead of wrapping the terminal, and whether it supports appending instructions rather than replacing the system prompt.*
- **agentos** (1/3): AgentOS is an OpenAI-compatible proxy with pluggable pillars. The app server's per-thread config and deferred-tool design is a reference point for how an agent platform could expose its tools to agents. → *Read the Codex app-server docs in the open-source repo to compare its per-thread config and deferred tool search with how AgentOS exposes its pillars to agents.*
