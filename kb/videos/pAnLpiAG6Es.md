# MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `pAnLpiAG6Es` · [watch](https://youtu.be/pAnLpiAG6Es) · **date:** 2026-10-04 · **length:** 18:44 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jan Čurn · **orgs:** Apify, Anthropic, Cloudflare, Cursor
- **topics:** mcp-and-tools, context-engineering, coding-agents · **tags:** MCP, progressive tool discovery, code mode, CLI vs MCP, context bloat, MCPC, connector evals, async tasks, Apify

> Apify's CEO argues MCP's problems come from agent harnesses, not the protocol. He covers progressive tool discovery, code mode, and CLIs, then pitches MCPC, a CLI wrapper for MCP.

## Summary
Jan Čurn (Apify) responds to the wave of "MCP is dead" posts by saying the main complaint, context bloat, comes from how agent harnesses load tools, since the MCP spec says nothing about harness design. He walks through three fixes in order: sub-agents (which still pay tokens and leak sensitive results into context), progressive tool discovery (load tool schemas only when needed), and Cloudflare-style code mode (let the model call tools by writing code). He argues CLIs already work this way by default: agents know the shell, load help text on demand, and run commands as code. The weak spot he names is that CLIs are opaque to enterprise instrumentation and have no standard credential injection, so he suggests MCP for remote access and CLI for local use. He then demos MCPC, Apify's open-source CLI client for MCP, which handles sessions, keychain credentials, grep-style tool search, async tasks, and JSON output for piping through jq. A rough connector eval he built shows MCPC and plain CLI are close on time and tokens, while raw MCP is faster but uses more tokens. About half the talk is a product pitch, and the evals are described as early.

## Key ideas
- **Context bloat from MCP is a harness problem, not a protocol problem** — Naive clients load every tool from every server into context up front. The speaker's example is 10 servers with about 100 tools, which he says can use roughly a third of the context before any work starts. The MCP spec leaves harness design to implementers. ([2:41](https://youtu.be/pAnLpiAG6Es?t=161))
- **Sub-agents move the context problem but do not remove it** — Delegating to sub-agents keeps the main window clean, but the tokens still get paid. Sensitive values returned by tools still end up in some context, so context is a poor place to pass secrets or large data. ([4:12](https://youtu.be/pAnLpiAG6Es?t=252))
- **Progressive tool discovery** — Expose a search tool that finds tools by need and adds only the matched schemas to context. Anthropic's Tool Search Tool and Cursor are cited as examples. Most tasks need only one or two tools. ([4:12](https://youtu.be/pAnLpiAG6Es?t=252))
- **Code mode: models write code against tools** — Cloudflare's approach turns MCP tools into code the model navigates and calls. The speaker argues models are better at code than at tool calling, which he calls a synthetic construct. He says Cloudflare's version is tied to its platform, so adoption is low. ([5:39](https://youtu.be/pAnLpiAG6Es?t=339))
- **CLIs already load progressively and run as code** — Agents do not load a full CLI's manual. They call a tool only when needed, rely on help output and training knowledge of common commands, and run commands as code by default in a shell sandbox. ([7:04](https://youtu.be/pAnLpiAG6Es?t=424))
- **CLIs are opaque to enterprise control, so use MCP for remote access** — A CLI has no standard transport or credential injection, so an organization cannot easily instrument it. The speaker's split is MCP for remote access and CLI for local access. Then the agent needs only one tool, bash, with the MCP features behind it. ([8:31](https://youtu.be/pAnLpiAG6Es?t=511))
- **MCPC: a CLI over MCP with JSON output and persistent sessions** — Every command has a --json flag, so output can be piped through jq. Sessions persist across runs, credentials go to the OS keychain, and grep-style search finds tools across servers. A --task flag runs a tool call asynchronously so the agent can detach and poll later. ([9:59](https://youtu.be/pAnLpiAG6Es?t=599))
- **Connector evals compare the connectors themselves, not the agents** — The speaker built a harness that runs the same tasks through different connectors and records time and token cost. In his early results MCPC and CLI are close, and raw MCP is faster but uses more tokens. He calls the results early. ([17:02](https://youtu.be/pAnLpiAG6Es?t=1022))

## Techniques
- **Progressive tool discovery** — Give the agent a search or grep tool over the tool catalogue, and load full schemas only for matched tools into context. *When:* Many tools across several MCP servers, where most tasks need only a few.
- **Code mode for tool calls** — Expose tools as callable code or a typed API. The model writes a short script that calls tools, filters or joins results, and returns only the needed output. *When:* Multi-step tool sequences, or results too large to pass through the model's context.
- **Keep large or sensitive tool output out of context** — Have the tool write results to a file or pipe them through jq or another filter in the sandbox, so the model sees only the needed fields. *When:* Tool results are large, or they contain passwords or other secrets.
- **Wrap MCP in a CLI and give the agent bash** — Expose each MCP server as CLI commands with JSON output, persistent sessions, and credentials in the OS keychain. The agent calls one bash tool. *When:* The agent already has a shell, and you need authenticated remote MCP access without schema bloat.
- **Async tool invocation with detach and poll** — Start a long tool call as a background task, do other work, then check progress and fetch the result later. *When:* Long-running remote tool calls such as web research or crawls.
- **Connector evals** — Run identical tasks through each connector option (raw MCP, CLI, wrapper) and record time and token cost, instead of comparing agents. *When:* Choosing how an agent should reach tools, or checking a claim that one interface is better.

## Numbers
- About 10,000 to 15,000 MCP servers exist (speaker's estimate). ([0:13](https://youtu.be/pAnLpiAG6Es?t=13))
- Naive loading of 10 MCP servers exposes about 100 tools up front, which the speaker says can use roughly one third of the context before any question is asked. ([2:41](https://youtu.be/pAnLpiAG6Es?t=161))
- Connector evals run on Claude Code with Sonnet 5 (per the speaker): MCPC and CLI perform similarly on time and token cost, raw MCP finishes faster but uses more tokens. No exact figures are given in the talk. ([17:02](https://youtu.be/pAnLpiAG6Es?t=1022))
- In the live grep demo, the filesystem server had 3 tools matching 'find' and the Apify server had 4. ([14:31](https://youtu.be/pAnLpiAG6Es?t=871))

## Hot takes
- The 'MCP is dead' posts are really complaints about bad harnesses, not the protocol.
- Models are better at writing and calling code than at tool calling, which is a synthetic construct.
- Stop saying CLI beats MCP. MCP plus CLI is the best combination.
- Many MCP servers could have been deterministic CLIs.

## Tools mentioned
MCP, MCPC, Claude Code, Claude Tool Search Tool, Cloudflare code mode, Bash, jq, Terminal Bench

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code, so how it loads tool definitions sets the per-run context cost. Its checkpoint and resume design also fits the talk's async-task and session-persistence ideas. → *Measure how many tokens tool definitions use at harness start. Then try deferred or searchable tool loading, and try async invocation for long background runs in ProsHarness.*
- **agentos** (1/3): The AgentOS proxy sits between agents and tools, so it could see tool-definition overhead per request. The talk does not cover proxy design directly. → *Add a metric for tokens spent on tool definitions per request at the proxy layer, as a baseline before choosing a discovery strategy.*
- **general** (1/3): The talk's main lesson is that tool-context cost should be measured, not assumed. → *In any agent eval, record tokens spent on tool definitions separately from task tokens.*
