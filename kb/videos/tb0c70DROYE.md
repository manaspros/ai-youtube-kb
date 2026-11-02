# AI Agent Protocols Explained: MCP, A2A, ACP and More

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `tb0c70DROYE` · [watch](https://youtu.be/tb0c70DROYE) · **date:** 2025-11-02 · **length:** 12:40 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus (Better Stack) · **orgs:** Better Stack, Anthropic, Google, IBM, ByteDance
- **topics:** mcp-and-tools, multi-agent, agent-architecture · **tags:** agent-protocols, mcp, a2a, acp, anp, agent-cards, json-rpc-2.0, goose, ollama, puppeteer, local-llm

> Better Stack walks through MCP, A2A, ACP and ANP: what each protocol does, where it fits, and short local demos of MCP (Goose), A2A (two agents on Ollama) and ACP (story writer). Practical orientation, no benchmarks.

## Summary
The video surveys agent communication protocols and treats MCP and A2A as the two to learn first. MCP connects an LLM client to tool servers, and the demo wires a browser MCP server and a VS Code MCP server into Goose. A2A lets agents discover each other through a JSON agent card and talk over HTTP with JSON-RPC 2.0; the demo builds a summarizer agent and an ideator agent on a local Llama 3.1 model, chained by a client. ACP (IBM) is presented as a simpler, plain-HTTP alternative, shown with a multi-agent story-writing server running a local Qwen 2.5 model. ANP is described as a peer-to-peer design with decentralized identities, but without a demo because it has little adoption. The closing argument is that the protocol landscape is experimental and many of these projects will merge or fade.

## Key ideas
- **MCP exists because an LLM alone cannot take actions; it gives agents a standard way to discover tools, read their parameters and call them.** — Developed by Anthropic and released November 2024 (per the speaker). Messages use JSON-RPC 2.0. MCP is described as the most widely adopted agent protocol. ([0:00](https://youtu.be/tb0c70DROYE?t=0))
- **In MCP the server exposes tools and instructions, while the client runs the LLM and decides when to call them. Result quality depends on both sides.** — The speaker says output quality depends on how well the client is implemented and how well it uses the server. mcpservers.org is cited as a directory of thousands of servers. ([1:11](https://youtu.be/tb0c70DROYE?t=71))
- **Multiple MCP servers compose inside one task without explicit orchestration code.** — In the demo, the agent first drives a browser MCP server (Puppeteer underneath) to read Hacker News, then calls a VS Code MCP server to open the resulting markdown file. The LLM picks the order itself. ([2:30](https://youtu.be/tb0c70DROYE?t=150))
- **A2A is a peer-to-peer agent standard where each agent publishes a discoverable agent card.** — The card is a JSON file at a known location listing name, capabilities, methods, auth details and connection info. Agents then talk over HTTPS with JSON-RPC 2.0 and exchange text, files, structured data or multimodal content. ([3:38](https://youtu.be/tb0c70DROYE?t=218))
- **A2A demo: a summarizer and an ideator run as separate agents, chained by a client, all on a local model.** — Both agents use the same local Llama 3.1 model through Ollama. The summarizer returns three bullets and the ideator returns five article ideas from that summary. Each agent is launched as its own standalone Express app. ([4:44](https://youtu.be/tb0c70DROYE?t=284))
- **ACP's pitch is accessibility: anything that can send an HTTP request, such as curl, Postman or a browser, can call an agent.** — One ACP server can expose several named agents, each with a name and description. The speaker says ACP is not much different from A2A, but is a good choice when you want something simple and REST-compatible. ([7:02](https://youtu.be/tb0c70DROYE?t=422))
- **ANP targets an open agent mesh where agents need no pre-shared credentials or central registry, using decentralized identities (DIDs).** — The speaker's hotel-booking example: an assistant agent finds a hotel agent, negotiates a secure channel and books, with no scraping or custom API. The speaker says adoption is limited and no easy demo exists. ([9:25](https://youtu.be/tb0c70DROYE?t=565))
- **Beyond the main protocols, the field is experimental, and the speaker recommends learning only MCP and A2A for now.** — Other names mentioned include AITP, ACONP, ACOMP, Coral, Agora, agents.json and WAP push. The speaker expects some to merge and others to disappear, and points to the paper 'A Survey of AI Agent Protocols' for a fuller list. ([10:40](https://youtu.be/tb0c70DROYE?t=640))

## Techniques
- **Add an MCP server to Goose as a command-line extension** — Run `goose configure`, open the add-extension menu, choose a command-line extension, give it a name, and enter the command exactly as the MCP server's schema lists it. Other settings can stay at defaults. Demo servers: a browser MCP server (ByteDance, Puppeteer-based) and a VS Code MCP server. *When:* Wiring any stdio MCP server into a CLI agent. Check the server's documented command first.
- **Chain MCP servers in one agent task** — Register several MCP servers with the client. Give a single natural-language goal that spans them, for example: scrape the top 10 of the first 100 Hacker News items, write them to a markdown file, then open it in VS Code. The LLM decides which server to call and in what order. *When:* Multi-step tasks that cross tool boundaries, such as browse, extract, then edit local files.
- **Build a standalone A2A agent (summarizer / ideator pattern)** — 1) `mkdir a2a-duo`, `npm init`, install the A2A SDK, node-fetch and uuid. 2) Set `"type": "module"` in package.json. 3) Per agent file: define an agent card (name, description, what it does), write an executor function that takes a prompt and calls the local model (Llama 3.1 via Ollama), create a request handler from the A2A SDK with the card and executor, and launch it as a standalone Express app. 4) Write a client that fetches a source text (a random Wikipedia article), sends it to agent 1, forwards the output to agent 2, and prints the chain. 5) Start both agents, then the client. *When:* When you need two independently running agents to pass work to each other over HTTP, possibly from different frameworks.
- **Serve several ACP agents from one server and call them over HTTP** — Clone the ACP repo and open the examples folder. In the OpenAI story-writer demo, replace the OpenAI client with a local Ollama endpoint (Qwen 2.5 in the demo). The server defines three agents: outline generator, story writer and an orchestrator that calls the first two. Invoke the orchestrator from an ACP client, or call it with plain HTTP tools. *When:* Trying a quick, REST-style agent endpoint without installing a protocol-specific SDK on the caller side.

## Numbers
- MCP released November 2024 (speaker's date); the speaker says it is the most widely adopted agent protocol. ([0:00](https://youtu.be/tb0c70DROYE?t=0))
- mcpservers.org lists thousands of MCP servers across use cases. ([1:11](https://youtu.be/tb0c70DROYE?t=71))
- Demo task: scan the first 100 Hacker News articles, keep the top 10 by rating. ([2:30](https://youtu.be/tb0c70DROYE?t=150))
- A2A demo output: summarizer returns 3 bullet points; ideator returns 5 article ideas. ([5:44](https://youtu.be/tb0c70DROYE?t=344))
- ACP demo server defines 3 agents (outline generator, story writer, orchestrator) on one server. ([7:02](https://youtu.be/tb0c70DROYE?t=422))
- The video gives no benchmarks, latency, cost or adoption figures; the 'widely adopted' claims are qualitative. ([10:40](https://youtu.be/tb0c70DROYE?t=640))

## Hot takes
- ACP is not much different from A2A in practice; it is mainly worth choosing when you want something simple and REST-compatible.
- ANP's peer-to-peer, DID-based design is attractive in concept, but it has not seen widespread adoption and has no easy demo.
- The protocol space is a 'wild west'; many of these projects will merge or fade. Only MCP and A2A are worth learning first.
- Quality of MCP results depends on the client implementation as much as on the server.

## Tools mentioned
MCP (Model Context Protocol, Anthropic), JSON-RPC 2.0, A2A (Agent2Agent, Google) and its SDK, ACP (Agent Communication Protocol, IBM), ANP (Agent Network Protocol), AITP, ACONP / ACOMP, Coral, Agora, agents.json, WAP push, Goose, Cursor, Claude Desktop, Puppeteer, VS Code MCP server, browser MCP server (ByteDance), Ollama, Llama 3.1, Qwen 2.5, Express, node-fetch, uuid, npm, curl, Postman, mcpservers.org

## Relevance to our work
- **agentos** (1/3): The L1 proxy sits on the tool-call path, and MCP is the dominant tool-connection protocol in the talk. The video does not cover proxy or security design. → *Check whether MCP JSON-RPC tool-call traffic would pass through the L1 proxy and the budget/PII scanner, or bypass it. Decide whether that matters before adding MCP support.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, which reaches tools through MCP servers. The video shows only the basic CLI extension configuration pattern. → *Confirm that ProsHarness passes MCP server configuration through to the Claude Code CLI unchanged, so its checkpoint/resume and approval flows do not hide tool calls.*
