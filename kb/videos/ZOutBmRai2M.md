# Docker Just Fixed 90% of AI Coding By Releasing This

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `ZOutBmRai2M` · [watch](https://youtu.be/ZOutBmRai2M) · **date:** 2026-01-02 · **length:** 9:57 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** unnamed AI LABS host · **orgs:** Docker, Anthropic, Cloudflare, GitHub, Notion
- **topics:** mcp-and-tools, token-cost-efficiency, sandboxing-execution · **tags:** docker, mcp, mcp-gateway, mcp-catalog, dynamic-tool-selection, code-mode, context-bloat, sandbox, volumes, claude-code, github-mcp, notion-mcp

> Docker's MCP toolkit walkthrough: one gateway in front of a vetted catalog, on-demand tool loading, and "code mode" where the agent chains MCP calls in a sandbox, keeping bulky results out of context.

## Summary
The host argues that MCP setups with hundreds of servers and thousands of tools bloat agent context, and that Docker's MCP Toolkit addresses this in three ways. A curated MCP catalog and gateway let a client connect to one endpoint and choose which servers to trust. Dynamic tool selection (mcp find, add, remove) loads only the tool definitions a session needs, so a GitHub server's roughly 40 other tools stay out of context. Code mode exposes a single JavaScript-capable tool that calls other MCP tools inside a Docker sandbox, with volumes holding intermediate data so the model sees only summaries. The demo has Claude Code merge six repo searches into one tool, then redirect its output to a text file so only descriptions reach the model, followed by a GitHub-to-Notion tool. The video names commands but shows no config, benchmarks or token measurements, and the title's "fixed 90% of AI coding" claim is not backed by anything in the video. Treat it as a product tour of a useful pattern set rather than evidence of savings.

## Key ideas
- **Context bloat is the core MCP problem now: hundreds of servers and thousands of tools, most unused in any one session.** — Cloudflare raised this first and Anthropic published a related post; the host frames the two costs as tool definitions in context and raw intermediate tool results. ([0:00](https://youtu.be/ZOutBmRai2M?t=0))
- **Docker's catalog and gateway solve trust and connection management: the client connects to one Docker endpoint that manages the catalog servers.** — The catalog lists verified servers; the client sees a single MCP connection and the gateway handles which servers are attached. ([1:02](https://youtu.be/ZOutBmRai2M?t=62))
- **Dynamic tool selection loads only the tools a session needs, using find/add/remove meta-tools.** — Example: keep only the GitHub search-repos tool out of about 40 others. Find searches the catalog by name or description, and the gateway injects definitions on demand. ([2:05](https://youtu.be/ZOutBmRai2M?t=125))
- **Raw tool results are the second token sink; a few search calls can fill the window.** — The GitHub search returned links, stars, descriptions and dates for every hit, while the user wanted only descriptions. The host estimates about 20 tool calls can fill the context. ([3:09](https://youtu.be/ZOutBmRai2M?t=189))
- **Code mode: the agent writes JavaScript that calls MCP tools inside a sandbox, and the model only sees one code-mode tool.** — Three claimed benefits: sandboxing contains untested agent-written code; only one tool definition is sent per request; volumes persist data between calls so it never reaches the model. ([4:24](https://youtu.be/ZOutBmRai2M?t=264))
- **Volume-backed state keeps large data out of context; the model gets status and summaries only.** — Example: download a 5GB dataset to a volume, have the model report success, then process the first 10,000 rows from the volume and return only the summary. ([5:51](https://youtu.be/ZOutBmRai2M?t=351))
- **Practical pattern from the demo: merge repeated tool calls into one generated tool, then write its output to a file and return only the needed fields.** — Claude Code combined six keyword searches into one multi-search tool (29 unique repos), run via the mcp exec tool. Results were then written to a repo text file so the model only received descriptions. The host says reusable saving of such tools is still manual. ([7:37](https://youtu.be/ZOutBmRai2M?t=457))

## Techniques
- **Single MCP gateway front door** — Install or update Docker, enable the Docker MCP toolkit (it may sit under beta features), then connect the MCP client (Claude Code in the demo) to the Docker MCP endpoint and add servers from the catalog. Features are on by default once connected. *When:* When you run many MCP servers and want vetted sources and one connection point instead of configuring each server in the client.
- **On-demand tool discovery with find/add/remove** — Ask the agent to find an MCP server by name or description using mcp find, then add it or remove it with the matching commands. The gateway loads only the tool definitions it needs. The video shows no config files. *When:* In sessions where you use 2-3 tools out of dozens, so unused definitions do not consume context on every request.
- **Code mode: chain MCP calls in a sandboxed script** — Have the agent write JavaScript that calls the MCP tools it needs, package it as a reusable tool, and invoke it through the mcp exec tool. Run it in the Docker sandbox so untested code cannot affect the host. *When:* For multi-step or batch tool use, such as repeated searches or pipelines, where intermediate results would otherwise flood the context.
- **Write bulky tool output to a file and return only the fields needed** — Tell the agent to write all raw results to a file in the repo, and return only the fields the model needs (the demo used descriptions). Later lookups read the file. *When:* Whenever a tool returns large payloads like search results or datasets. This works without Docker, using any tool that can write files.
- **Volume-backed state between tool calls** — Store intermediate data such as downloads or processed rows in a persistent volume. Return to the model only status messages, final results, summaries or errors. *When:* Data pipelines where the raw data is too large for context but the model needs to decide the next step.
- **Merge repeated tool calls into one generated tool** — After noticing the agent making many similar calls (e.g. the same search with different keywords), ask Claude Code to write one tool that runs all the queries and returns combined output. *When:* Repetitive research or lookup workflows that run the same tool with varied inputs.

## Numbers
- Users reportedly run hundreds of MCP servers with thousands of tools. ([0:00](https://youtu.be/ZOutBmRai2M?t=0))
- The GitHub MCP server exposes about 40 tools; the user needed one (search repos). ([2:05](https://youtu.be/ZOutBmRai2M?t=125))
- About 20 tool calls can fill the context window with raw MCP results (host estimate, not measured). ([3:09](https://youtu.be/ZOutBmRai2M?t=189))
- Six keyword searches produced 29 unique repos in one multi-search tool run. ([7:37](https://youtu.be/ZOutBmRai2M?t=457))
- Example data pipeline: 5GB dataset kept on a volume; only the first 10,000 rows processed for the summary. ([5:51](https://youtu.be/ZOutBmRai2M?t=351))
- The video gives no benchmark, token count or cost measurement for any savings claim. ([9:03](https://youtu.be/ZOutBmRai2M?t=543))

## Hot takes
- The title's claim that Docker fixed 90% of AI coding is not supported by anything shown in the video.
- Code mode puts agent-written, untested code in the path; the safety case depends entirely on the sandbox, and the video does not test it.
- The trust problem is addressed by a curated catalog run by Docker, which means trusting Docker's vetting; the video does not explain the verification process.
- Vendor walkthrough: the presenter is demoing a Docker product, and the video contains no comparison with alternative approaches.
- Minor inconsistency: the host cites about 40 other GitHub tools at 2:05 and 47 at 5:51.

## Tools mentioned
Docker MCP Toolkit, Docker MCP Catalog, Docker MCP Gateway, Docker MCP find/add/remove tools, mcp exec tool, Docker containers and volumes (sandbox), Claude Code, GitHub MCP server, Notion MCP server, Cloudflare code mode (referenced), Anthropic MCP token post (referenced)

## Relevance to our work
- **agentos** (2/3): AgentOS's L1 proxy and L2C sandboxed execution are the same layer that Docker's gateway and code mode occupy; the on-demand tool loading and large-result-to-volume pattern map directly onto that design. → *Compare Docker's find/add/remove plus code-mode approach with AgentOS's proxy and Crucible sandbox. Prototype whether the proxy can cap tool-result size and write oversized results to storage, returning only summaries to the model.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, so unused MCP tool definitions and large tool outputs add to every run's context, which matters for checkpoint and resume of long runs. → *Test whether ProsHarness can scope MCP servers per run so unused tool definitions stay out of the session, and whether tool outputs over a size limit can be written to a file instead.*
