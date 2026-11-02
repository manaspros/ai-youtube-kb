# MCP = Mega Context Problem - Matt Carey

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YBYUvGOuotE` · [watch](https://youtu.be/YBYUvGOuotE) · **date:** 2026-05-18 · **length:** 22:42 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Matt Carey · **orgs:** Cloudflare
- **topics:** mcp-and-tools, sandboxing-execution, context-engineering · **tags:** mcp, code-mode, progressive-discovery, tool-search, context-window, sandbox, v8-isolates, typescript-sdk, openapi, programmatic-tool-calling, cloudflare-workers

> Cloudflare's Matt Carey argues that dumping every API endpoint into MCP tools blows up agent context, and that progressive discovery (tool search, CLIs, or code mode with typed SDKs run in isolates) is the way out.

## Summary
The speaker, who works on MCP and agents at Cloudflare, traces how tool calling moved from bundled per-agent tools to shared remote MCP servers. Exposing a whole API as naive MCP tools overflows the context window; Cloudflare's OpenAPI spec alone was about 2.3M tokens, which became roughly 1.1M tokens of tool definitions. Splitting the API across 16 product-specific MCP servers fixed the context problem but left coverage gaps and forced users to pick a server. He presents three alternatives: a CLI (needs shell access), tool search (keyword-match the request and load about 8 tool definitions), and code mode (generate a typed SDK from OpenAPI and let the model write code against it). Code mode stalled in clients because running model-written code is risky, so Cloudflare shows running generated code in an isolated V8 Worker with no secrets by default and programmable outbound-network rules. He argues that code is a more compact plan than many tool calls, predicts more clients will do programmatic tool calling and save generated scripts for recurring jobs, and expects MCP to become a native framework flag by year end. The talk is a vendor pitch for Cloudflare, but it carries concrete token numbers and a clear sandboxing model.

## Key ideas
- **Naive MCP (one tool per endpoint) explodes the context window. Cloudflare's OpenAPI spec was about 2.3M tokens, roughly 1.1M as tool definitions, which no model can take.** — Splitting into 16 product-specific MCP servers fixed size but left coverage gaps (one suite had 6 tools for about 30 endpoints) and made users choose a server. ([2:46](https://youtu.be/YBYUvGOuotE?t=166))
- **The problem is dumping tool definitions into context, not MCP itself. MCP is a protocol and can expose anything; the fix is to load capabilities progressively.** — The speaker says prompts, resources and skills should also not all be loaded at once. ([4:11](https://youtu.be/YBYUvGOuotE?t=251))
- **Three ways around it: a CLI the agent drives through shell, tool search that loads only relevant tools, or code mode where the agent writes code against a typed SDK.** — CLIs work but need shell access. Tool search keyword-matches the request and adds about K=8 tool definitions. Code mode generates types from OpenAPI and lets the model write code. ([5:40](https://youtu.be/YBYUvGOuotE?t=340))
- **Types are a compact way for an agent to reason about inputs and outputs. Generating a typed SDK from OpenAPI and letting the model write code against it is the main code-mode idea.** — The speaker says the OpenAPI spec should be the source of truth, and the model should improve as models get better. ([7:05](https://youtu.be/YBYUvGOuotE?t=425))
- **Clients did not adopt code mode because executing model-written code is scary. The answer is isolation: run the code in a fresh V8 isolate with no secrets and no network unless allowed.** — Node compatibility is off by default, so process.env is absent. Outbound access is a server-side flag, and finer rules can allow only specific domains. ([10:04](https://youtu.be/YBYUvGOuotE?t=604))
- **Code is a more compact plan than a sequence of tool calls, so the expected pattern is one code tool instead of many tools.** — He names Dynamic Workers (workerd), Deno and Pydantic Monty as other runtimes for untrusted code, and expects more primitives like them. ([15:08](https://youtu.be/YBYUvGOuotE?t=908))
- **Clients will need programmatic tool calling and will save generated scripts. A web-scraping job saved as a script can be rerun on a schedule, and the agent can repair and resave it when it breaks.** — He also says building MCP clients has been hard (stateful connections, resumability), so few well-used clients exist. ([18:06](https://youtu.be/YBYUvGOuotE?t=1086))
- **Stateless agent loops will not scale to many agents per person, so state needs to be something that can be turned on or off. APIs also need rate limiting, since code-writing agents can loop and hit them hard.** — He predicts MCP becomes a middleware flag in TypeScript full-stack frameworks by the end of the year, once the SDK is small enough. ([20:30](https://youtu.be/YBYUvGOuotE?t=1230))

## Techniques
- **Progressive tool discovery via tool search** — Keyword-match the user's request against the tool catalog and inject only the top K (about 8) tool definitions into context. The model can then load more when needed. Other tools stay out of context. *When:* When the total tool surface is too large to load at once, and the set of tools needed per request is small.
- **Code mode over a generated typed SDK** — Generate TypeScript types from the OpenAPI spec and show only those types to the model. The model writes code against the SDK, and the code is run as the single tool call. *When:* When an API has thousands of endpoints and you want the model to compose several calls in one plan.
- **Isolated execution of model-written code with programmable guardrails** — Load the generated code into a fresh V8 isolate (Worker) from a string. Keep Node compatibility off so there are no secrets or process.env. Control outbound network access with a server-side flag, or a function that allows only specific domains. *When:* When model-generated code needs to run for users, and you want the code to have no ambient secrets and only the network access you choose.
- **Save agent-generated code as mini-scripts** — Store code the model produced for a user action as a script. Run it on a schedule, such as a daily scraping job. When it breaks, the agent regenerates and resaves it. *When:* For recurring jobs where regenerating the same code each time wastes tokens and time.
- **Rate-limit APIs for agent callers** — Put rate limits on the API so that a loop of sandboxes calling it in parallel cannot overload it. *When:* When the API will be called by agent-written code running in loops or many parallel sandboxes.

## Numbers
- OpenAPI spec for the Cloudflare API is about 2.3M tokens, about 1.1M as naive tool definitions. ([2:46](https://youtu.be/YBYUvGOuotE?t=166))
- 16 product MCP servers covering about 2,500 endpoints (about 2,600 later). One suite had 6 tools for about 30 endpoints. ([4:11](https://youtu.be/YBYUvGOuotE?t=251))
- Tool search loads about K=8 tools, about 2,100 tokens, of which about 500 are used. ([7:05](https://youtu.be/YBYUvGOuotE?t=425))
- The Cloudflare MCP server exposes all of its API, which the speaker says is 2,000-plus endpoints. This conflicts with the 2,600 figure given at 4:11. ([14:16](https://youtu.be/YBYUvGOuotE?t=856))
- Vendor claim: the code-mode blog post shows an entire API given to agents in about 1,000 tokens. The number is not demonstrated in the talk. ([21:50](https://youtu.be/YBYUvGOuotE?t=1310))

## Hot takes
- MCP is not dead; the bad part is loading every tool into context. Progressive discovery is the fix.
- Code mode (typed SDK plus model-written code in an isolate) is likely to become the default pattern for APIs with thousands of endpoints.
- Every API should be exposed through MCP as a framework flag, and clients should do programmatic tool calling by default. This is a prediction, not a result.
- Vendor pitch for Cloudflare. The endpoint counts disagree (about 2,500 and 2,600 at 4:11 versus 2,000-plus at 14:16), and the 1,000-token figure is not shown on stage.

## Tools mentioned
MCP (Model Context Protocol), MCP SDK, OpenAPI, TypeScript, Cloudflare Workers, Dynamic Workers (workerd), V8 isolates, Wrangler, Cloudflare D1, Cloudflare Access, Claude Code, OpenClaw, Deno, Pydantic Monty, Next.js

## Relevance to our work
- **agentos** (2/3): Crucible is the sandboxed code-execution layer with exec-gate guardrails. The talk's isolate-with-no-secrets model and per-domain outbound rules map directly onto it. Code mode is also a way to expose many tools without bloating context. → *Prototype code mode for Crucible: generate a typed SDK from an OpenAPI spec, run model-written code in an isolate with secrets off, and compare its outbound-domain allowlist with the current exec-gate guardrails.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, which uses tool search. The talk's numbers (about 2,100 tokens loaded, about 500 used) and its idea of saving generated scripts for recurring runs apply to loops and schedules. → *Measure how many tokens ProsHarness spends on tool definitions per Claude Code run, and test saving generated scripts for scheduled loops instead of regenerating them.*
