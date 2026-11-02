# MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `sAOBXCDiDOs` · [watch](https://youtu.be/sAOBXCDiDOs) · **date:** 2026-07-18 · **length:** 28:54 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Pietro Zullo · **orgs:** Manufact, Anthropic, OpenAI, Cursor, Remotion, Granola, Linear
- **topics:** mcp-and-tools, product-ux, security-guardrails · **tags:** MCP Apps, MCP-UI, sandboxed iframe widgets, set state, model context sync, split output, structured content, tool input streaming, client capability detection, MCP app stores, submission review, dynamic discovery, MCP registry, display modes, React widgets, distribution

> Pietro Zullo (Manufact) explains MCP Apps: tools that return sandboxed UI widgets, the primitives behind them, and how the new client app stores distribute MCP servers.

## Summary
The speaker, co-founder of Manufact (maker of open-source MCP SDKs, an inspector, and a hosted MCP cloud), explains MCP Apps. An MCP tool can return a UI widget rendered in a sandboxed iframe inside the chat, so the host shows a rich interface instead of plain JSON. The widget and the host communicate in both directions. He walks through the primitives: a set-state call that keeps the model aware of what the UI shows, sending follow-up messages, calling other tools from the widget, streaming partial tool arguments into the UI as tokens arrive, and splitting tool output so the user sees full data while the model sees only what you choose. He then covers display modes, theme sync, and returning different output when a client does not support widgets. On the SDK side, widgets are React components in a resources folder that get compiled into HTML and linked to tools. The second half covers distribution: ChatGPT, Claude and Cursor now accept self-serve MCP app submissions, which involve compliance checks, tool annotation review, auth declaration and test prompts. He claims Claude already searches the MCP registry for connectors when no tool fits a task. Much of the talk is vendor promotion, but the primitives are concrete and checkable.

## Key ideas
- **An MCP tool can return a UI widget instead of JSON, rendered in a sandboxed iframe with two-way messaging to the host.** — The tool result carries a UI resource declared at init. The model fills the tool arguments, and the widget renders from them. The widget can send messages back to the host, so the chat becomes an interactive surface. ([5:18](https://youtu.be/sAOBXCDiDOs?t=318))
- **Split the tool output: one part for the user's UI, another for the model.** — A tool can return structured data that only the widget shows, plus a text output that the model sees. Private fields can stay out of model context while the user still sees the full card. Pattern: show full data in the UI and give the model a short text summary, or nothing. ([13:55](https://youtu.be/sAOBXCDiDOs?t=835))
- **The set-state primitive keeps the model in sync with what the widget shows.** — Without it, the model cannot introspect the UI. Widget state changes (for example a selection) are pushed to the model, so the next user message is answered with that context. ([8:52](https://youtu.be/sAOBXCDiDOs?t=532))
- **Tool arguments can stream into the widget while the model is still generating them.** — Partial tool input tokens update the UI incrementally. The speaker's demos include a diagram syntax rendered as it streams and a Remotion video rendered live during generation. ([10:23](https://youtu.be/sAOBXCDiDOs?t=623))
- **Return UI only to clients that can render it, and fall back to a different output otherwise.** — The server reads client metadata during connection. If the widget is not shown, data that was meant for the widget may need to go to the model as text instead. ([18:35](https://youtu.be/sAOBXCDiDOs?t=1115))
- **Dynamic discovery through the MCP registry is the main distribution claim; he says only Claude does it today.** — When a task has no matching tool, Claude searches the registry for a connector. The speaker says ChatGPT is expected to follow. Store presence is therefore a discovery channel, not just a listing. ([24:59](https://youtu.be/sAOBXCDiDOs?t=1499))
- **Store submission is a checklist: compliance scan, tool annotations, declared auth, and test prompts.** — The client scans the remote MCP server's tools and auth, and reviewers test with supplied prompts, partly manually. Acceptance is partly automatic. The speaker's company runs these checks beforehand and generates screenshots and test cases. ([23:49](https://youtu.be/sAOBXCDiDOs?t=1429))
- **Clients differ on follow-up messages: Claude puts them in the input box for the user to send, while ChatGPT sends them and starts streaming at once.** — Designers of widget actions have to account for this per-client behavior, which the speaker says applies to many MCP features. ([10:23](https://youtu.be/sAOBXCDiDOs?t=623))

## Techniques
- **Widget-returning tool** — Register a React component file in the server's resources folder. The SDK compiles it to HTML and CSS and links it to the tool, which returns it as a UI resource populated with tool arguments. *When:* When a tool's output is easier to read as a card, table, chart or diagram than as text.
- **Split structured output (UI vs model)** — Return structuredContent for the widget and a separate text output for the model, or no model output at all. *When:* When the tool returns private or bulky data that the model should not see or does not need.
- **Set-state to sync UI to model** — Call the set-state primitive from the widget on each meaningful state change, so the model's view of the UI stays current. *When:* When users interact with a widget and the next model turn depends on what they selected or changed.
- **Stream tool input into the UI** — Consume partial tool-argument streams and re-render the widget incrementally as tokens arrive. *When:* For generated artifacts such as diagrams, SVG or video code where live preview improves the experience.
- **Widget actions that call tools** — Bind a button in the widget to another tool call to fetch more data from the same server. *When:* When the user should drill into data without typing a new prompt.
- **Client-aware output** — Read the connected client's metadata and choose between a UI response and a text-only response. *When:* When the server must support hosts with and without widget rendering.
- **Pre-submission checks for stores** — Verify tool annotations, argument schemas and auth declarations against the store's checks, then prepare test prompts and screenshots before submitting. *When:* Before submitting an MCP server or app to ChatGPT, Claude or Cursor directories.

## Numbers
- MCP launched in 2024; MCP-UI proposal appeared around May 2025; MCP apps as a concept date to about end of 2025. ([1:03](https://youtu.be/sAOBXCDiDOs?t=63))
- Manufact's SDKs have over 8 million downloads and about 10K GitHub stars (speaker's own figures). ([2:28](https://youtu.be/sAOBXCDiDOs?t=148))
- ChatGPT and Claude opened app/connector stores around end of 2025; MCP-UI became the official MCP extension MCP Apps in January 2026. ([3:56](https://youtu.be/sAOBXCDiDOs?t=236))
- Speaker says the chat platforms have more than 1 billion active users who will express intent in chat (unverified claim). ([24:59](https://youtu.be/sAOBXCDiDOs?t=1499))

## Hot takes
- AI apps are the new browsers and MCP servers are the new websites, so dashboards should move into the chat as MCP apps.
- Being in the MCP app stores is becoming the most basic buying signal: he says he checks whether a product has an MCP server before buying.
- Claude is the only client doing dynamic registry discovery today, and that will make store listings a major organic channel.

## Tools mentioned
MCP, MCP Apps, MCP-UI, MCP SDK, MCP Inspector, React, Remotion, Excalidraw, Granola MCP, Linear MCP, Postgres MCP, Claude Code, Claude Cowork, Codex, Cursor, ChatGPT Apps SDK, VS Code, Mermaid

## Relevance to our work
- **agentos** (1/3): AgentOS's proxy and PII scan layer could use the split-output pattern to keep private tool data out of model context, but the talk does not cover proxies or policy enforcement. → *Consider whether AgentOS tool responses that carry PII can be routed to a UI-only channel while the model gets a redacted text summary.*
