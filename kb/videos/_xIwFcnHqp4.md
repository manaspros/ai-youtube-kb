# Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_xIwFcnHqp4` · [watch](https://youtu.be/_xIwFcnHqp4) · **date:** 2026-06-18 · **length:** 16:06 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Marlene Mhangami, Liam Hampton · **orgs:** GitHub, Microsoft, Anthropic, Shopify, Excalidraw, Figma
- **topics:** mcp-and-tools, coding-agents, product-ux · **tags:** MCP Apps, VS Code, GitHub Copilot, interactive UI, iframe sandbox, flame graph, pprof, Go profiling, tool visibility, MCP server scaffolding

> Marlene Mhangami and Liam Hampton (GitHub) show how MCP Apps let a tool return an interactive HTML UI rendered in a sandboxed iframe inside VS Code chat, with a live Go flame-graph demo.

## Summary
The talk explains MCP as an open protocol for giving LLM apps context, then argues that text-only tool output forced chat tools into ASCII art and emoji. MCP Apps fix this: a tool result carries a reference to an HTML UI resource, the host (VS Code) fetches it and renders it in a sandboxed iframe, and the app can call back to the server for fresh data. The speakers list use cases such as data exploration and in-chat checkout, and name Shopify, Excalidraw and Figma as builders. Liam then scaffolds MCP app projects by adapting an Anthropic MCP skill run through Copilot CLI. His demo wraps a Go pprof profiler in an MCP server, profiles a bubble sort and Fibonacci program for five seconds, and renders the result as an interactive flame graph in chat. He justifies the iframe as containment, so the app cannot touch VS Code settings or external APIs. The talk is short and mostly a live demo with light product promotion, and it gives no benchmarks.

## Key ideas
- **Text-only tool output pushed chat tools into ASCII art and emoji; MCP Apps let a tool return a live UI component instead.** — Tool results can point to an HTML UI resource, so users can click, drag and edit inside the chat rather than retyping questions. ([3:19](https://youtu.be/_xIwFcnHqp4?t=199))
- **MCP Apps run as a fixed flow: the LLM calls the tool, the server returns data plus a UI resource reference, and the host renders it.** — The host (VS Code) fetches the HTML the server generated and shows it in a sandboxed iframe. The app then calls back to the server, so fresh data can update the UI. ([5:19](https://youtu.be/_xIwFcnHqp4?t=319))
- **An MCP app has three parts: the tool, the bundled HTML resource, and the link between them that the host recognises.** — The UI can be written in React, Vue, Svelte or vanilla JS. The host and server must agree on the link so that data and UI arrive together. ([10:00](https://youtu.be/_xIwFcnHqp4?t=600))
- **The iframe is a deliberate containment boundary.** — The speaker's analogy is a hamster in a cage. The app should not reach VS Code settings, APIs or anything external, so it stays inside the chat window. ([14:19](https://youtu.be/_xIwFcnHqp4?t=859))
- **Scaffolding MCP apps can be automated with a skill.** — Liam adapted an Anthropic MCP skill and ran it through Copilot CLI to generate several starter apps, including a flame graph, a markdown viewer and a colour picker. ([10:00](https://youtu.be/_xIwFcnHqp4?t=600))
- **Wrap a local profiler in an MCP server and render the output as an interactive view, which removes the back-and-forth of asking a model to interpret raw data.** — The server runs Go pprof for five seconds, returns JSON, and the React flame graph shows where time is spent. The speaker says this replaces repeatedly asking the model whether the results are good. ([12:00](https://youtu.be/_xIwFcnHqp4?t=720))
- **Control who can invoke each tool.** — Tool visibility settings decide whether the model alone, the model and the app, or only the app can call a tool. ([10:57](https://youtu.be/_xIwFcnHqp4?t=657))

## Techniques
- **MCP App tool-plus-resource pattern** — Register a tool whose result includes a UI resource reference. The server serves a bundled HTML app, the host renders it in a sandboxed iframe, and the app calls back to the server for updates. *When:* When a chat tool's output is better as an interactive view, such as charts, diagrams, data exploration or multi-step selection.
- **Skill-driven MCP app scaffolding** — Use an MCP skill (borrowed from the MCP repo and edited) inside a coding agent such as Copilot CLI to generate the server, the tool definitions and the UI bundle in one pass. *When:* When starting a new MCP app and wanting a consistent project layout instead of hand-written boilerplate.
- **Tool visibility scoping** — Set each tool so that only the model, the model plus the app, or only the app can invoke it. *When:* When some tools should be user-driven UI actions rather than model-callable, to limit what the agent can trigger.
- **Profiler-to-flame-graph bridge** — An MCP server runs a local profiler (Go pprof, 5-second window), returns structured JSON, and a React component renders the flame graph in the chat iframe. *When:* When a developer wants performance hotspots visible in chat without copy-pasting raw profile output.
- **Install MCP servers from curated lists only** — Pick servers from VS Code's extensions list (search for MCP) or GitHub's list rather than random internet sources. *When:* Before installing any third-party MCP server, to reduce the risk of malicious code.

## Numbers
- The live demo profiles the Go program for a 5-second window using Go pprof. ([12:00](https://youtu.be/_xIwFcnHqp4?t=720))

## Hot takes
- Emoji- and ASCII-art-heavy READMEs were overcompensation for tools that could only return text.
- Use only MCP servers from VS Code's curated list, because random servers from the internet can contain malicious code.

## Tools mentioned
VS Code, GitHub Copilot, Copilot CLI, MCP, Go pprof, React, Excalidraw, Figma

## Relevance to our work
- **prosharness** (1/3): Shows an iframe-sandboxed MCP app pattern that could in principle host ProsHarness checkpoint or approval views in-chat, but this is not a current need. → *Read the MCP Apps spec on the sandboxed-iframe and tool-visibility model before deciding whether approval or checkpoint views belong in an MCP app.*
