# Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `hCMrEfPG2Yg` · [watch](https://youtu.be/hCMrEfPG2Yg) · **date:** 2026-06-18 · **length:** 16:58 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ruben Casas · **orgs:** Postman, Anthropic, Vercel, OpenAI, Netflix
- **topics:** product-ux, mcp-and-tools, sandboxing-execution · **tags:** generative-ui, mcp-apps, declarative-ui, static-components, sandboxed-iframe, json-render, ag-ui, human-agent-collaboration, postman, front-end-generation

> Ruben Casas (Postman) maps generative UI from static components to declarative JSON to runtime-generated HTML/JS, argues MCP apps are the right sandboxed delivery layer, and says collaborative canvases are the next step.

## Summary
Casas traces how agent-generated UI has moved from copy-pasting ChatGPT code in 2022 to models that produce high-fidelity front-end code in late 2025. He separates two questions: where the UI runs (third-party app, super app, or chat everywhere) and what the model actually generates. He lays out three levels: static components filled with agent-supplied props, declarative UI where the agent emits a JSON or YAML descriptor that a renderer maps onto a design system, and generative components where the model writes HTML, CSS and JavaScript at runtime. He argues declarative generation is the practical balance today for consistency and cost, while runtime generation needs a sandbox boundary, which MCP apps provide along with auth, tool calling and message passing. He shows a weather-agent experiment that returns a joke and its UI in one tool call. He closes by arguing the next step is a shared human-agent canvas rather than just rendered output, and that we are still in the "radio era" of this medium. The talk is a conceptual taxonomy with one demo and no benchmarks.

## Key ideas
- **Two separate design questions: where the UI runs, and what the model generates** — Third-party UI in a super app versus chat embedded everywhere is one axis. Whether the model fills static props, emits a descriptor, or writes raw HTML/CSS/JS is a different axis. Most discussion conflates them. ([4:05](https://youtu.be/hCMrEfPG2Yg?t=245))
- **Static components: agent supplies props, developers own the components** — The agent makes a tool call with parameters and data. The client maps the result onto developer-built components, as in AG-UI client tools that map to React components and Goose's auto visualizer. The agent produces data only, so the layout stays fixed. ([6:25](https://youtu.be/hCMrEfPG2Yg?t=385))
- **Declarative UI: the agent emits a descriptor, and a renderer builds the UI from the design system** — The agent outputs JSON, YAML or a Python descriptor that maps to predefined components. A translation engine turns it into UI. The speaker calls this the right balance today because it keeps design-system consistency, predictability, lower token cost and speed. Netflix's server-driven UI is an earlier version of the same idea. ([7:50](https://youtu.be/hCMrEfPG2Yg?t=470))
- **Generative components: the model writes HTML, CSS and JavaScript on demand, which needs a trust boundary** — Runtime generation skips the component library. The speaker's weather demo returned a joke and the matching HTML, CSS and JS in one tool call with no components. Treating LLM output as trusted code is the failure mode, so this level needs distribution, containment and a sandbox. ([10:43](https://youtu.be/hCMrEfPG2Yg?t=643))
- **MCP apps are the delivery layer for generated UI** — They are sandboxed by default in a double iframe and already provide auth, tool calling and message passing between UI and agent. He notes Anthropic chose MCP apps for its own first-party Visualizer rather than building its own rendering path. ([11:55](https://youtu.be/hCMrEfPG2Yg?t=715))
- **Future is a shared artifact, not one-way output** — He points to the Excalidraw MCP app (transcribed as ScallyDraw) as a shared canvas where the human can edit directly and the agent can edit too. He expects collaboration and personalization to matter more than fixed visualizations. ([14:45](https://youtu.be/hCMrEfPG2Yg?t=885))
- **Radio-era analogy: we lack imagination for the medium yet** — Early TV was radio with cameras. The speaker argues we are still making the equivalent of that and cannot yet picture what agent-driven interfaces will look like. He describes this as speculation. ([13:20](https://youtu.be/hCMrEfPG2Yg?t=800))

## Techniques
- **Declarative generative UI with a component catalog** — Expose the design system as a fixed set of components. Have the agent emit a JSON or YAML descriptor that references them. A rendering engine validates and maps the descriptor onto the components. Examples named: Vercel's json-render and FastMCP-style Python descriptors. *When:* You need design-system consistency, predictable output, lower token cost and faster rendering, and cannot accept fully free-form UI.
- **Static client-tool to component mapping** — Register a client tool in the agent UI SDK (AG-UI named) that maps to a React component. The agent's tool call props fill the component's props. *When:* A small, fixed set of visualizations covers the use case and the agent only supplies data.
- **Runtime generated HTML/CSS/JS in a sandboxed MCP app** — Have the agent or a second model call return a full HTML, CSS and JS bundle in one tool call. Render it inside an MCP app iframe so it can call tools and pass messages back to the agent under the host's sandbox. *When:* One-off, highly personalized UI where no design system constraint applies and the output is untrusted and must be contained.
- **Use MCP apps as the default delivery for generated UI** — Ship any generated UI as an MCP app to inherit sandboxing, authentication, tool calling and UI-to-agent messaging rather than building a custom renderer. *When:* Any time UI is produced on the fly by an agent or coding model, including first-party UI.

## Numbers
- Late-2025 models (GPT-5.2 and Opus 4.5) were described as very good at high-fidelity, fast UI generation and long-horizon tasks. No benchmark scores given. ([1:10](https://youtu.be/hCMrEfPG2Yg?t=70))
- The speaker says the shift from ChatGPT's release to now happened within about three years. ([2:35](https://youtu.be/hCMrEfPG2Yg?t=155))
- Weather demo: one tool call returned a joke plus generated HTML, CSS and JS with no component library. No latency or cost figures given. ([10:43](https://youtu.be/hCMrEfPG2Yg?t=643))

## Hot takes
- Declarative generative UI, not free-form generated code, is the right balance today.
- MCP apps are the best delivery mechanism for generative UI, and more so when the UI is generated on the fly.
- We are still in the radio era of agent interfaces, so the obvious Jarvis-style floating windows are probably not the answer.
- Chat in every SaaS homepage is not the final UI, but it is acceptable for now.
- Future generative UI is a shared human-agent canvas, not one-way visualization.

## Tools mentioned
MCP apps, AG-UI, Goose (auto visualizer), json-render (Vercel), FastMCP, Excalidraw MCP app (transcribed as ScallyDraw), Claude Visualizer, GPT-5.2, Claude Opus 4.5, React

## Relevance to our work
- **agentos** (1/3): AgentOS is a proxy and infra layer, not a UI product. Its sandboxing pillar (Crucible) is the containment layer that generated HTML/JS would need, which the talk stresses. → *If AgentOS ever renders agent-generated UI, read the MCP apps sandbox model first and check whether Crucible's celld sandbox can host an untrusted iframe bundle.*
- **prosharness** (1/3): Phone-driven approvals are a UI surface. The static-versus-declarative split maps directly to whether approval cards are fixed templates or agent-described. → *For ProsHarness phone approvals, prototype a fixed approval-card component fed by a small JSON descriptor from the agent, rather than free-form generated HTML.*
