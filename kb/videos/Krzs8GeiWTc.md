# Generative UI... in Python? — Jeremiah Lowin, Prefect

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Krzs8GeiWTc` · [watch](https://youtu.be/Krzs8GeiWTc) · **date:** 2026-09-18 · **length:** 17:38 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jeremiah Lowin · **orgs:** Prefect
- **topics:** mcp-and-tools, product-ux, vibe-coding-app-building · **tags:** MCP Apps, FastMCP, Prefab, generative UI, Python DSL, reactive UI, file upload, token efficiency

> Jeremiah Lowin (Prefect) on Prefab, a Python DSL for composing MCP App UIs; the talk argues scoping UIs to pre-built components makes Python-only front ends viable and that streaming compact Python beats streaming JSON.

## Summary
Lowin introduces MCP Apps, where a tool result is rendered as an interactive UI for the user instead of going back through the agent's context. He argues that FastMCP's mostly-Python users do not need fully custom branded front ends, only tables, forms, and charts, so a scoped UI framework is practical. Prefab is a Python context-manager DSL that builds a declarative UI tree, serializes it to JSON, and renders it with a React app hosted as the MCP app. He shows three escalating uses: returning a component from a tool, adding client-side reactive bindings with no JavaScript, and building a full FastMCP app with back-end tool callbacks. He also demos file upload that bypasses the agent, and streaming generative UI. The talk is a product walkthrough, but it includes one concrete finding: the Python form of a UI is about 70% smaller than its JSON form, so the system now streams Python and executes it server-side.

## Key ideas
- **MCP Apps let a tool result render as a full interactive UI sent straight to the user, not back through the agent's context window.** — Normally the user never talks to the MCP server directly. With MCP Apps, the tool sends HTML/CSS/JS UI to the user, who then interacts with it, and the agent is bypassed for those interactions. ([1:29](https://youtu.be/Krzs8GeiWTc?t=89))
- **Scope the UI problem to composing known components, not building a frontend from scratch.** — Lowin's users are mostly enterprise Python engineers who need tables, forms, and charts for sharing and collecting information. Limiting the target to world-class components is what makes a Python-built UI viable. ([3:49](https://youtu.be/Krzs8GeiWTc?t=229))
- **Prefab's architecture is Python DSL, then a serializable JSON protocol, then a React renderer.** — The JSON middle layer was the design goal, since it lets agents generate or edit UIs. The Python syntax came out of that as a side effect. ([7:27](https://youtu.be/Krzs8GeiWTc?t=447))
- **Scale from one-line tool changes to full apps with back-end callbacks.** — Level 1: a tool returns a component instead of a dict, and FastMCP detects this and serves it as an MCP app. Level 2: reactive variables link components with no JavaScript. Level 3: an app class with app.ui for the base view and app.tools as back-end methods the UI can call. ([10:43](https://youtu.be/Krzs8GeiWTc?t=643))
- **File upload through an MCP app avoids the agent copy-paste problem.** — Uploading via an MCP tool forces the agent to re-emit the file's contents token by token. An app-based drag-and-drop upload sends the bytes straight to the server. ([14:13](https://youtu.be/Krzs8GeiWTc?t=853))
- **Streaming Python is more token-efficient than streaming JSON.** — The team first planned to stream JSON, then found the Python form was about 70% smaller. They now stream Python, which runs in a sandbox on the server and is converted to JSON there before rendering. ([15:36](https://youtu.be/Krzs8GeiWTc?t=936))

## Techniques
- **Return a UI component from a tool** — In a FastMCP tool, return a Prefab component (e.g., a data table) instead of a dict. The framework detects this and serves an MCP app with the HTML, JS, and CSS. Compose multiple components in a grid with context managers. *When:* When a tool's result is better viewed and used by the human than read by the agent, such as a directory, table, or chart.
- **Reactive bindings for client-side interactivity** — Use Rx reactive variables and reference them across components that share the attribute. These compile to JavaScript automatically, so the controls update each other with no hand-written JS. *When:* When controls on the same screen need to update each other without a server round trip.
- **App class with app.ui and app.tools** — Write a class with one or more app.ui functions that return the base UI, and zero or more app.tools that the UI calls as back-end methods, such as a button that saves form data. *When:* When the interaction is a multi-step application with server state, not a one-shot view.
- **Agent-bypass upload via MCP app** — Ask the agent to open the app's upload component, then drag the file in. The browser sends the file directly to the server, so the agent never sees the content. *When:* When large files must reach an MCP server and passing them through the agent's context would be slow and costly.
- **Stream generative UI as code** — Expose a tool that accepts UI definitions and stream the agent's output as Python. Execute it in a sandbox on the server, convert the result to JSON, and render it. Shipping a skill teaches the agent the DSL. *When:* When an agent should generate UIs on the fly and token count or latency matters.

## Numbers
- Python UI representation is about 70% smaller than the equivalent JSON representation, which led to switching the streaming format from JSON to Python. ([15:36](https://youtu.be/Krzs8GeiWTc?t=936))
- Prefab ships roughly 130 to 140 components. ([13:08](https://youtu.be/Krzs8GeiWTc?t=788))
- MCP Apps was introduced in January of 2026; an agent-interaction extension was expected in the July MCP release. ([1:29](https://youtu.be/Krzs8GeiWTc?t=89))

## Hot takes
- Pure JSON is not the best wire format for generative UI; compact Python executed server-side can beat it on tokens and latency.
- Enterprise Python developers do not need consumer-grade branded UIs, so a constrained component DSL is the right scope for MCP apps.
- Uploading files through an agent is the world's most expensive copy-paste operation.

## Tools mentioned
Prefab, FastMCP, MCP Apps, React, shadcn/ui, Goose

## Relevance to our work
- **general** (2/3): The 70% token saving from streaming Python over JSON is a concrete context-engineering result for any agent that generates structured output. The MCP Apps interaction pattern also applies to agent-built tools. → *Measure token cost of generating a structured output as JSON versus a compact code DSL on one of our own agent tasks before choosing a schema format.*
- **agentos** (1/3): AgentOS exposes MCP-style tools behind an L1 proxy. MCP Apps with a Python DSL is a possible way to surface its budget, audit, or memory UIs to users. The talk does not address the proxy or the storage layers. → *Read prefab.prefect.io docs to judge whether a small AgentOS admin view (budgets, audit log tables) is cheaper as a Prefab MCP app than as a separate web UI.*
- **prosharness** (1/3): ProsHarness has phone-driven approvals and checkpoint status, which are forms and tables. Prefab can render these as MCP apps, but the talk does not cover approval flows or credential handling, which are the hard parts. → *Try a one-tool Prefab card for ProsHarness checkpoint status in a FastMCP server to see if an approval UI works in one Claude Code client.*
