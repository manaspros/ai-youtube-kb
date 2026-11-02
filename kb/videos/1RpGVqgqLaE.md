# Anthropic Have FINALLY Solved the MCP Context Nightmare

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `1RpGVqgqLaE` · [watch](https://youtu.be/1RpGVqgqLaE) · **date:** 2026-02-02 · **length:** 4:11 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Cloudflare, Redis, Cursor, Better Stack
- **topics:** mcp-and-tools, token-cost-efficiency, context-engineering, claude-code · **tags:** mcp, tool-search, context-window, progressive-disclosure, token-efficiency, programmatic-tool-calling, cloudflare, mcporter, agent-skills

> Claude Code's MCP tool search loads only the 3-5 most relevant tools on demand instead of preloading every schema, cutting context use. A short explainer that compares it with Cloudflare's code-orchestration approach.

## Summary
A short Better Stack explainer on Anthropic's MCP tool search in Claude Code. The core problem is that every tool from every connected MCP server is preloaded into the context window, which the speaker says can consume tens of thousands of tokens before the first prompt. The cited example is 167 tools from four servers, over 60,000 tokens, almost half of a 200k Opus window. The fix described is a search approach: when preloaded MCP tools exceed about 10% of the context, Claude discovers tools from a natural-language query and loads only the 3-5 most relevant full schemas, similar to how Agent Skills use progressive disclosure. The video contrasts this with the programmatic approach, where the model writes code to orchestrate tools, as Cloudflare does with generated TypeScript definitions run in a sandbox. The speaker reports that the Claude Code team tried programmatic calling and found search better, which he finds hard to believe. He closes by suggesting that converting MCP servers to CLI commands, for example with mcporter, may be more context-efficient. The video offers no measurements of its own and shows no configuration.

## Key ideas
- **Preloading all MCP tool schemas (names, descriptions, full JSON schema with parameter types and constraints) costs tokens before the user writes anything, and the cost scales with the number of connected servers.** — The speaker names this as MCP's biggest problem, alongside naming collisions and command injection. He presents it as the main thing the new feature fixes. ([0:00](https://youtu.be/1RpGVqgqLaE?t=0))
- **Claude Code's tool search claims up to a 95% context reduction by searching for a tool before using it, not loading all tools up front.** — The 95% figure is stated in the intro and is not sourced or measured in the video. ([0:00](https://youtu.be/1RpGVqgqLaE?t=0))
- **Concrete cost example: 167 tools from four servers used over 60,000 tokens before any prompt, nearly half of a 200k Opus context window.** — The speaker notes this excludes skills and plugins, and that more context can reduce model performance even in 1M-token models such as Gemini. ([1:11](https://youtu.be/1RpGVqgqLaE?t=71))
- **The trigger is a threshold: if preloaded MCP tools exceed about 10% of the context window (about 20k tokens of 200k), tool search activates. Below it, tools load normally.** — When active, Claude discovers tools from a natural-language description of the task and fully loads only 3-5 of the most relevant ones. The speaker says this was the most requested feature on the Claude Code GitHub repo. ([1:11](https://youtu.be/1RpGVqgqLaE?t=71))
- **The search approach mirrors Agent Skills progressive disclosure: only names and short descriptions sit in context until a match is needed.** — The speaker says Anthropic and Cursor both report benefits from this approach for MCP tools. He does not give the source of those reports. ([2:36](https://youtu.be/1RpGVqgqLaE?t=156))
- **The programmatic alternative has the model orchestrate tools in code rather than through individual tool-call round trips, which matters when calls depend on each other's output.** — Claude can write a Python script to chain calls and return only the result. Cloudflare goes further: the model writes TypeScript definitions for the tools and runs the code in a sandbox, usually a Worker. ([2:36](https://youtu.be/1RpGVqgqLaE?t=156))
- **The speaker reports that the Claude Code team tried the programmatic approach and found search worked better. He finds this hard to believe, given how good Claude is at writing code, and gives no evidence either way.** — This is the main point where the video's claims are unverified and the speaker's skepticism is untested. ([2:36](https://youtu.be/1RpGVqgqLaE?t=156))
- **Speaker's own suggestion: convert MCP servers into CLI commands (he mentions mcporter) so the model runs a specific command rather than holding tool schemas in context.** — Presented as opinion. The video does not test it. ([3:45](https://youtu.be/1RpGVqgqLaE?t=225))

## Techniques
- **Threshold-gated tool search** — Measure the tokens taken by preloaded MCP tool schemas. If they exceed about 10% of the context window (about 20k of 200k), stop preloading. Expose a search over tool names and descriptions, then load full schemas only for the top 3-5 matches for the current request. Below the threshold, keep preloading as usual. *When:* When many MCP servers are connected and tool definitions take a large share of the context before the first user prompt, for example in long-running agent sessions with little room left for work.
- **Programmatic tool orchestration** — Give the model typed definitions of the available tools (Cloudflare uses TypeScript) and have it write code that chains the calls, with loops and conditionals, instead of making one tool call per round trip. Run the code in a sandbox such as a Worker or a container, then return only the final result to the model. *When:* When a multi-step tool chain depends on intermediate results, so one round trip per call wastes tokens. The video says the Claude Code team found this less effective than search, so compare the two on your own workload.
- **Wrap MCP servers as CLI commands** — Convert each MCP server's tools into CLI subcommands (the speaker suggests mcporter) and have the agent invoke the specific command through the shell. Only the command the agent actually runs enters context. *When:* As a speculative alternative when a tool set is large and mostly stable. The speaker gives no benchmark, so measure it before committing.

## Numbers
- Claimed context reduction of up to 95% from tool search. ([0:00](https://youtu.be/1RpGVqgqLaE?t=0))
- 167 tools from four MCP servers used over 60,000 tokens before any prompt, almost half of a 200k Opus window. ([1:11](https://youtu.be/1RpGVqgqLaE?t=71))
- Tool search activates when preloaded MCP tools exceed about 10% of the context window (about 20k tokens of 200k). ([1:11](https://youtu.be/1RpGVqgqLaE?t=71))
- Tool search loads 3-5 of the most relevant tools in full. ([1:11](https://youtu.be/1RpGVqgqLaE?t=71))

## Hot takes
- The title's 'FINALLY Solved' overstates a four-minute walkthrough. The 95% reduction figure is unsourced, and the video shows no measurements or configuration.
- The speaker calls it hard to believe that the Claude Code team found search beat programmatic tool calling, and offers no evidence for or against.
- Converting MCP servers to CLI commands is presented as opinion and is not tested.
- Quality is capped at 2 because the title is hype and the substance is thin. The video is a useful pointer to the context-cost problem, not a reproducible method.

## Tools mentioned
Claude Code, Claude Opus, MCP (Model Context Protocol), Cloudflare Workers, Cloudflare (programmatic tool calling), Cursor, Agent Skills, mcporter, Python, TypeScript, Better Stack MCP server, Gemini (1M-token window, mentioned only), Headless Chromium agent browser CLI (name garbled in captions, not named in the video), GitHub, Docker, Notion MCP servers (mentioned only)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code for long checkpointed runs. Tool schemas loaded at the start of every run eat the context budget that those runs need. → *Measure how many tokens connected MCP tool schemas take at the start of a ProsHarness run, and use per-run server selection or tool search if they exceed about 10% of the window.*
- **agentos** (1/3):  → *Note the tool-schema token cost as a metric for the L1 proxy budget work, and check whether any MCP-style tool listing passes through it.*
