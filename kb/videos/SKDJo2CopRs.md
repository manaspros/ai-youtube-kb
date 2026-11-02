# Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `SKDJo2CopRs` · [watch](https://youtu.be/SKDJo2CopRs) · **date:** 2026-06-18 · **length:** 24:51 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sunil Pai, Matt Carey · **orgs:** Cloudflare, Vercel, Daytona, Pi (coding agent), Open Claw
- **topics:** sandboxing-execution, agent-architecture, mcp-and-tools, infra-cost-scaling · **tags:** durable-objects, cloudflare-workers, dynamic-workers, code-mode, mcp, resumable-streaming, sandbox, generative-ui, agents-sdk, stateful-serverless

> Two Cloudflare engineers tour Durable Objects, dynamic workers and code mode as a stateful, sandboxed runtime for agents. Mostly product pitch, with a few reusable architecture ideas.

## Summary
The talk, titled "Why Eval++ Is the Next Great Compute Primitive", is a conversational product tour by two Cloudflare agent engineers. Their core pitch is that Durable Objects, which are addressable and persistent per ID, make a good home for agent state, connections and long-running loops. The Agents SDK on top of them gives resumable streaming and multi-tab or multi-device sync without a separate database or replication layer. Dynamic workers let an app run a code string at runtime in a fresh isolate, with no deploy step. The speakers present this as "eval++" and argue for a deny-by-default sandbox where code gets only explicit capabilities. They also describe "code mode", where the model writes code against an API instead of making tool calls, and claim a whole API surface fits in about 1,000 tokens. Much of the back half is announcements and sales material (plugins for a CMS, Next.js on Workers, a coming harness, pricing). Technical detail is thin, and the speakers say the deep dives are in their blog and other talks.

## Key ideas
- **Durable Objects as the agent compute unit** — A class instance per ID that starts once, stays addressable, persists state, hibernates when idle and can run in the background. The speakers call it stateful serverless. They say it suits agents because every client connection lands on the same instance. ([3:05](https://youtu.be/SKDJo2CopRs?t=185))
- **Resumability and multi-device sync come from the object model** — If a stream is running on the agent object, a reconnecting client gets the stream from the start and then keeps receiving bytes. Multi-tab and multi-device sync follow without custom replication or sticky sessions. The speakers use this to argue that shared AI chat should be multiplayer. ([13:18](https://youtu.be/SKDJo2CopRs?t=798))
- **MCP servers need stateful connections, and Durable Objects supply them** — Early MCP needed a stateful client-server connection, which was hard to run in the cloud. Durable Objects keep that connection, so the speakers say they hosted some of the first production MCP servers. ([5:44](https://youtu.be/SKDJo2CopRs?t=344))
- **Dynamic workers run code from a string at runtime** — Code that a user or an LLM produced can run in its own isolate without being deployed first. The speakers say you can start billions on demand. They describe it as an isolate, not a VM, with no full filesystem. ([6:57](https://youtu.be/SKDJo2CopRs?t=417))
- **Sandbox by starting from zero capabilities** — Instead of hardening a VM or container afterwards, the sandbox starts with only JavaScript running and no fetch. The host then grants explicit capabilities, such as fetch to one allowed domain, and no environment variables are exposed. ([8:26](https://youtu.be/SKDJo2CopRs?t=506))
- **Code mode: write code against the API instead of calling tools** — The model writes code that runs in a dynamic worker. The speakers claim this gives access to Cloudflare's roughly 2,600 API endpoints in about 1,000 tokens through one MCP server. They defer the explanation to a later talk. ([9:21](https://youtu.be/SKDJo2CopRs?t=561))
- **Generative UI: render generated code, not JSON specs** — The speakers ask why teams generate JSON that a renderer then turns into UI, when they could generate HTML or React. Their answer: the platform needs a safe place to run untrusted code. Client-side artifacts are fine, but server-side rendering needs isolation. ([12:28](https://youtu.be/SKDJo2CopRs?t=748))
- **Persistent agent loop reachable from many clients** — The speakers describe an agent loop like a Claude Code backend that lives on the server. Terminal, web, phone and iOS clients all attach to the same synced session. They say a coding harness on this runtime is coming soon. ([14:29](https://youtu.be/SKDJo2CopRs?t=869))
- **Virtual filesystem and bundler inside a worker** — The speakers describe a bundler that runs in a worker, pulls npm dependencies, strips types and JSX, and uses Cloudflare's cache. A filesystem sits on Durable Object SQLite, with R2 for large files. They say it works today. ([19:52](https://youtu.be/SKDJo2CopRs?t=1192))

## Techniques
- **One Durable Object per entity ID as the session or agent** — Make a class for each agent, session or room, and route every connection (WebSocket, MCP, HTTP) for that ID to the same instance. Keep state in the object and let it hibernate when idle. *When:* Per-user or per-session agent state, multiplayer or shared sessions, and long-lived MCP connections.
- **Resumable stream held by the agent object** — Keep the streaming output on the server-side agent object. A reconnecting client gets the stream from the start and then the live bytes, so there is no client-side replay logic. *When:* Chat or agent UIs where users refresh, switch tabs or switch devices during a long generation.
- **Deny-by-default capability sandbox for generated code** — Run generated code with no ambient network, no environment variables and no filesystem. Grant specific fetch targets or bindings one at a time. *When:* Executing LLM- or user-written code where the host wants least privilege by default.
- **Code mode for large API surfaces** — Give the model a code-execution interface over an API, not one tool definition per endpoint. The model writes a short program that runs in a sandbox and calls the API. *When:* APIs with thousands of endpoints, where tool definitions would use most of the context window. The speakers' token figure is a claim, not measured in the talk.
- **Scheduled work inside the agent class** — Register timed or recurring callables in the agent's constructor or startup, such as a weekly job that gathers context and drafts output. *When:* Background agent jobs that need no open client connection.
- **Plugins as isolated dynamic workers** — Load each third-party plugin into its own dynamic worker with its own capabilities, instead of running it in the host process. *When:* Extensible products where plugin code is not fully trusted, such as a CMS plugin system.

## Numbers
- Claimed latency in London for a Durable Object (about 15 ms), compared with a 60 FPS frame budget of about 16 ms ([3:05](https://youtu.be/SKDJo2CopRs?t=185))
- Claimed coverage of Cloudflare's roughly 2,600 API endpoints in about 1,000 tokens with code mode over MCP (not measured in the talk) ([9:21](https://youtu.be/SKDJo2CopRs?t=561))
- Dynamic workers can be spun up in very large numbers on demand (described as billions) ([6:57](https://youtu.be/SKDJo2CopRs?t=417))
- Paid plan described as about $5 per month, with a free tier they say is not a marketing expense ([22:52](https://youtu.be/SKDJo2CopRs?t=1372))

## Hot takes
- AI should be a multiplayer game, and shared chat sessions are a missing product feature.
- Dynamic isolates are better sandboxes for generated code than VMs or containers.
- Dynamic workers are an eval++ primitive that opens a branch of the tech tree unexplored for about 30 years.
- Code mode beats per-endpoint tool calls for large APIs.
- Generating HTML or React and rendering it on the server beats generating JSON for UI.

## Tools mentioned
Cloudflare Durable Objects, Cloudflare Workers, Cloudflare Dynamic Workers, Cloudflare Agents SDK, Vercel AI SDK, MCP, Cloudflare Sandbox SDK, Daytona, SQLite, R2, Zig (via Wasm), Next.js on Workers, Pi coding agent

## Relevance to our work
- **agentos** (2/3): Crucible is the opt-in sandboxed code execution layer, and the talk's deny-by-default capability model (no ambient fetch, explicit per-host grants, no env vars) is a concrete design to compare against. → *Compare Crucible's exec sandbox with the deny-by-default capability model (no fetch, no env, explicit host grants). Read the Cloudflare dynamic workers and sandbox posts the speakers point to before deciding.*
- **prosharness** (2/3): ProsHarness needs checkpoint/resume of long runs and phone-driven approvals. The per-ID addressable, hibernating object model with resumable streams maps directly onto that. → *Sketch whether a ProsHarness run could live in a per-run addressable store, so a terminal and a phone attach to the same run. Read the Agents SDK resumable-stream description at 13:18 first.*
- **general** (1/3): Recurring interest in context engineering. Code mode is a claim about shrinking the context cost of large API surfaces. → *Read the code-mode write-up the speakers reference (Cloudflare blog) and note the token-accounting method.*
