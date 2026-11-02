# Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `8txf05vVVl4` · [watch](https://youtu.be/8txf05vVVl4) · **date:** 2026-05-18 · **length:** 19:40 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sunil Pai · **orgs:** Cloudflare
- **topics:** mcp-and-tools, token-cost-efficiency, sandboxing-execution, agent-architecture · **tags:** code-mode, search-and-execute, mcp-token-cost, tool-calling, openapi, sandbox, v8-isolates, capability-security, generative-ui, agent-dx, cloudflare-workers

> Cloudflare's Sunil Pai on "Code Mode": have models write code against an API instead of making many tool calls, cutting a 2,600-endpoint API from ~1.2M tokens to ~1K, inside capability-restricted sandboxes.

## Summary
Pai argues that JSON tool calling breaks down at scale: many tools fill the context window and each step needs a slow round trip through the model. His team instead asks the model to write JavaScript that runs in a sandbox next to the API, so loops, state, sequencing and parallel calls happen in one execution. For Cloudflare's own API (about 2,600 endpoints), they expose only two tools, search and execute, both taking code as input; search runs over the OpenAPI spec and execute calls the typed functions, which he says cut the first-call cost from about 1.2M tokens to about 1,000. A live demo of the DDoS-blocking use case partly stalled on stage (JavaScript errors and pagination trouble), so it is an illustration, not evidence. He then describes an emergent example: a model given the raw state of a canvas app (an array of strokes) read it and played tic-tac-toe in place, without any game code, and he frames this as the model "inhabiting the state machine" rather than generating a new app. The sandbox design he recommends starts with zero capabilities, grants named APIs explicitly, blocks outbound fetches by default, and requires full observability; he uses V8 isolates for fast startup. He closes by saying agents are the new users of software and need developer experience (markdown docs, errors that say what to do next, search-based discovery) plus capability-based security.

## Key ideas
- **Tool calling via JSON breaks at scale** — With hundreds of tools filling the context, and each step needing a model round trip, multi-step tasks get slow and fragile. Pai's team asks the model to write code instead and runs that code against the environment. ([1:32](https://youtu.be/8txf05vVVl4?t=92))
- **Code gives you loops, state, sequencing and parallelism in one run** — Instead of many back-and-forth calls, one generated program does the whole job in a single execution. He also notes typed APIs let you type-check and get syntax errors, which models can read and fix. ([2:28](https://youtu.be/8txf05vVVl4?t=148))
- **Search and execute pair for huge API surfaces** — Rather than one tool per endpoint, expose two tools that both take code: search runs over the OpenAPI spec, and execute calls the typed functions. This is the core technique of the talk. ([3:29](https://youtu.be/8txf05vVVl4?t=209))
- **Unbounded tool count is a token-cost problem** — One tool per endpoint for Cloudflare's ~2,600 endpoints would be ~1.2M tokens in the first call. The per-task cost of a classic MCP approach is about eight round trips, versus one code run. ([4:55](https://youtu.be/8txf05vVVl4?t=295))
- **Non-programmers get custom software through generated code** — A user can ask for a behavior like renaming files by date and location, and the model writes and runs code against exposed systems. This replaces buying a generic app or waiting for a developer. ([8:52](https://youtu.be/8txf05vVVl4?t=532))
- **Let the agent inhabit the app's state rather than build a new app** — In Kenton's canvas example, the model was shown the raw stroke array instead of being asked for a tic-tac-toe program. It read the state and played in place. Pai presents this as anecdotal and emergent, not a benchmark, and says the model lost the game. ([10:17](https://youtu.be/8txf05vVVl4?t=617))
- **Sandboxes start with zero capabilities** — The sandbox can only execute code by default. Named APIs are granted explicitly, outbound fetches are blocked unless allowed, and full observability of every run is required. He uses V8 isolates for fast startup and says the default recommendation is no outgoing fetches, only APIs. ([12:33](https://youtu.be/8txf05vVVl4?t=753))

## Techniques
- **Search + execute two-tool facade** — Expose two tools that take code as a string. Search runs code over the API's OpenAPI spec to find endpoints. Execute runs code that calls typed functions for those endpoints. Token cost stays roughly flat as the API grows. *When:* The API or tool surface is too large to list as individual tools (thousands of endpoints), or each task chains many calls.
- **Code as the tool-call format** — Ask the model to generate a short JavaScript program that uses loops, await, pagination and parallel calls, then run it in the sandbox and return the result. Errors come back to the model so it can fix and retry. *When:* Multi-step tasks with dependencies, pagination or fan-out where JSON round trips are slow or costly.
- **Zero-capability sandbox with explicit grants** — Start the isolate with no network and no APIs. Expose only named functions. Block outbound fetch by default. Log every run for later inspection. *When:* Running model-written code on systems you care about, where you need to explain later why an action happened.
- **Agent-facing developer experience** — Write docs in Markdown, make errors say what to do next, and make the API discoverable through search. Pai treats agents as the new users of an API and says they need the same care as humans. *When:* Designing internal or public APIs that agents will call, or building a registry agents must search.
- **Operate on the app's raw state** — Give the model the app's underlying state (for example, a stroke array) and let it read and write that state directly, instead of generating new UI logic. *When:* The app's state is inspectable and structured, and you want flexible behavior without writing new features.

## Numbers
- Cloudflare API surface is about 2,600 endpoints ([3:29](https://youtu.be/8txf05vVVl4?t=209))
- One tool per endpoint would be about 1.2 to 1.5M tokens in the first call ([3:29](https://youtu.be/8txf05vVVl4?t=209))
- Search + execute reduced this to about 1,000 tokens (speaker's figure, which he calls a ~99.9% reduction) ([3:29](https://youtu.be/8txf05vVVl4?t=209))
- Classic per-call MCP approach would take about eight round trips per task (speaker's estimate) ([4:55](https://youtu.be/8txf05vVVl4?t=295))
- Live demo was rehearsed 10 times, but it stalled on stage with JS errors and pagination trouble; no measured result was shown ([6:27](https://youtu.be/8txf05vVVl4?t=387))

## Hot takes
- Give the model the API as code and let it write the calls, instead of exposing one tool per endpoint.
- A large MCP server's token cost can be cut by about 99% with a two-tool search and execute pair.
- The model should inhabit the app's state machine rather than generate a new app for each request.
- Agents are the next billion users of software, so developer experience for agents matters as much as for humans.
- Capability-based security should be the default: start a sandbox with no capabilities and grant them one by one.

## Tools mentioned
Cloudflare Workers, Cloudflare Dynamic Workers, V8 isolates, OpenAPI, PartyKit, Claude Opus, TLDraw-style canvas

## Relevance to our work
- **agentos** (2/3): Crucible is the opt-in sandboxed code execution layer. The zero-capability sandbox with explicit grants and no default outbound fetch maps onto it, and the search+execute pattern is a candidate for exposing large tool surfaces through the proxy. → *Prototype a Crucible-style search+execute tool pair over one large AgentOS tool surface, measure first-call token cost against one-tool-per-endpoint, and check whether exec-gate guardrails still apply to the executed code.*
- **prosharness** (1/3): The speaker frames a harness as a sandbox with explicitly granted capabilities and long-running stateful workflows, which overlaps with ProsHarness's Claude Code wrapper. He does not discuss checkpoint or resume. → *Consider whether ProsHarness should expose tools to the Claude Code run through explicit, zero-by-default grants rather than broad access.*
