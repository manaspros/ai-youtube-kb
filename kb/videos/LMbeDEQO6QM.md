# Introducing WebMCP: Agents in the Browser — RL Nabors

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `LMbeDEQO6QM` · [watch](https://youtu.be/LMbeDEQO6QM) · **date:** 2026-06-18 · **length:** 23:08 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Rachel Lee Neighbors · **orgs:** Arize, Mozilla, W3C, Microsoft
- **topics:** mcp-and-tools, voice-multimodal, product-ux · **tags:** mcp, webmcp, mcp-apps, transports, stdio, streamable-http, browser-agents, csp, mcp-resources, web-speech-api, vite-single-file

> A practical tour of MCP over HTTP, MCP Apps for in-chat UI with CSP and sandbox gotchas, and WebMCP, which lets agents call tools exposed by a web page's own JavaScript.

## Summary
Rachel Lee Neighbors walks through hosting her webcomic archive as one server with three kinds of clients: humans in browsers, humans in agents, and agents in browsers. She compares stdio and HTTP transports: stdio runs as a local process the client spawns, while HTTP is a web service that suits serverless hosting and gives users a simpler remote-connector setup. She argues that MCP clients should implement resources, because agents will not reliably pull markdown docs through tools. She then covers MCP Apps, single-file HTML bundles rendered in a sandboxed iframe, and lists their gotchas: no local storage, no direct network access, links that need host permission, and a CSP that blocks external assets by default. Last, she introduces WebMCP, which registers page functions as agent tools either imperatively via navigator.modelContext.registerTool or declaratively via form attributes. She is clear that WebMCP is inspired by MCP rather than spec-compliant, and the spec is still in flux. The talk closes with browser built-in APIs such as Web Speech as zero-dependency capabilities.

## Key ideas
- **One server can serve three client types: humans in browsers, humans using agents, and agents driving browsers on a human's behalf.** — She hosts her comic archive as a single backend and exposes it to all three, instead of building separate integrations for each. ([4:52](https://youtu.be/LMbeDEQO6QM?t=292))
- **stdio and HTTP transports suit different deployments, and the choice changes the user experience.** — stdio is a local process spawned by the client and needs JSON config with command-line args. HTTP is a web service using POST that works with serverless/edge hosting and lets users add a remote connector by name and URL. ([6:14](https://youtu.be/LMbeDEQO6QM?t=374))
- **MCP resources are the right vehicle for bulk docs or transcripts, but no client she tested exposes them.** — Agents resist calling tools just to load markdown into context. Resources would let a harness pre-load context when the task changes, e.g. switching to a React mode. She asks harness builders to implement them, even minimally. ([9:54](https://youtu.be/LMbeDEQO6QM?t=594))
- **Tools can return interactive UI (MCP Apps), which fixes the chat box as the only interface.** — Chat is a weak landing page because users must already know what the system can do. An MCP app returns a single HTML bundle that renders inline, such as a comic reader with navigation and a text-mode toggle. ([11:59](https://youtu.be/LMbeDEQO6QM?t=719))
- **MCP Apps are sandboxed islands with real restrictions.** — Everything must be embedded in one HTML file, typically base64. There is no local storage, no direct network access (the app must ask the server via a tool call), and links need host permission. External fonts or CDN assets are blocked until CSP is configured, so a blank app usually means a CSP problem. ([14:37](https://youtu.be/LMbeDEQO6QM?t=877))
- **UI-only tools should be hidden from the model.** — Pagination tools like forward/backward should be app-visible only, so the model does not call them and dump raw JSON or text instead of using the UI. ([16:49](https://youtu.be/LMbeDEQO6QM?t=1009))
- **WebMCP lets a page expose its existing JavaScript functions as agent tools, without a server round trip.** — Declarative mode adds tool name and description attributes to forms. Imperative mode calls navigator.modelContext.registerTool with name, description, input schema, and an execute callback, so an agent can navigate or call APIs on the page. ([18:08](https://youtu.be/LMbeDEQO6QM?t=1088))
- **WebMCP is inspired by MCP, not a one-to-one spec implementation, and the standards work is still unsettled.** — She compares it to JavaScript vs Java. Its status is a community group proposal, with partial browser support. She demos it through a debugging extension, where the agent calls a next-page tool that reads the page's link rel=next. ([19:25](https://youtu.be/LMbeDEQO6QM?t=1165))
- **Browser built-in APIs are free capabilities for agents, such as Web Speech for text-to-speech.** — Her talking demo uses the browser's speech API, which needs no extra inference or dependency. She argues that canvas, WASM, CSS, audio, and animation APIs are already available for agent-facing experiences. ([22:01](https://youtu.be/LMbeDEQO6QM?t=1321))

## Techniques
- **Single server, multiple client surfaces** — Serve MCP over HTTP from the same backend that serves the website, reusing its data and navigation. Expose the same tools to chat clients, agents, and browser agents. *When:* You already have a website or API and want agents to reach the same content without a second integration.
- **Remote connector onboarding over HTTP** — Host the MCP server at a URL such as /mcp. Users add it as a named connector in client settings instead of editing a stdio JSON config. *When:* Non-technical users need to connect a server, or you want serverless hosting.
- **App-only tool visibility for UI navigation** — Mark pagination or view-state tools as app-visible only, so the model does not invoke them for text answers. *When:* An MCP App has tools that drive its own UI and should not be chosen by the model.
- **Bundle MCP App into one file with explicit CSP** — Build the UI as a single HTML file with Vite single-file, base64-embed assets, and declare any external origins (fonts, images) in the CSP config. *When:* Shipping an MCP App that needs fonts or a design system, or when blank renders appear.
- **WebMCP imperative registration with feature detection** — Check for navigator.modelContext. If present, call registerTool with name, description, input schema, and an execute callback that reuses existing page functions or DOM links. *When:* The page has workflows, API calls, or navigation that agents should be able to run directly in the browser.
- **Declarative WebMCP on existing forms** — Add tool name and tool description attributes to existing HTML forms. The form's JavaScript handler becomes the tool implementation. *When:* The site is form-heavy, such as dashboards or internal tools, and you want minimal change.

## Numbers
- Archive has 533 comics that a client would otherwise need to fetch transcripts for one by one ([9:54](https://youtu.be/LMbeDEQO6QM?t=594))
- Her earlier webcomics site had about 400,000 weekly readers (ad-supported, 2006-era, historical context) ([1:09](https://youtu.be/LMbeDEQO6QM?t=69))

## Hot takes
- Chat is the lowest common denominator of agent UX, roughly what the CLI was to software.
- Agents would rather not call MCP tools to load docs; MCP resources should be how context gets pre-primed.
- WebMCP is to MCP what JavaScript is to Java: borrowed name and ideas, not spec compliance.
- The browser is an infinite canvas, and agent-facing web experiences should use the APIs the browser already ships.

## Tools mentioned
MCP, MCP Apps, WebMCP, navigator.modelContext.registerTool, Vite single-file plugin, Web Speech API, MCP Inspector-style debugging extension

## Relevance to our work
- **prosharness** (1/3): The harness around Claude Code could load MCP resources at phase or mode switches instead of relying on tool calls to pull docs into context. → *Read the MCP resources spec and check whether the Claude Code CLI exposes resources; if it does not, consider a harness-side pre-prime step that reads resources on checkpoint resume.*
