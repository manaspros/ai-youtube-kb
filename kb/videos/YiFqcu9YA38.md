# Dashboards Are Dead — Sarah Simionescu, Composio

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YiFqcu9YA38` · [watch](https://youtu.be/YiFqcu9YA38) · **date:** 2026-10-04 · **length:** 10:42 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Sarah Simionescu · **orgs:** Composio, Anthropic, Datadog, Sentry, GitHub, PostHog, Metabase, Atlassian
- **topics:** mcp-and-tools, context-engineering, product-ux · **tags:** MCP, tool discovery, agent-native interfaces, dashboards, context window, cross-app workflows, Composio, vendor pitch

> Composio's Sarah Simionescu argues agents should replace dashboards, and that MCP servers need task-scoped tool discovery to work. Vendor pitch with a mock-up demo.

## Summary
Sarah Simionescu of Composio argues dashboards are becoming obsolete because they are translation layers between users and per-tool query languages that agents can now handle directly. She traces the path from 2023 "sparkle button" LLM query writers to MCP, then says raw MCP servers fail for three reasons: agents do not learn across conversations, large tool catalogs flood the context window, and each server sees only its own app. Composio's answer is a search step where the agent states its task and gets back relevant tools plus an ordered usage plan, along with a remote workbench that keeps bulky query results out of context. The Slack-to-draft-PR demo is explicitly a mock-up, and her comparison against native MCP servers is described as unreleased with no figures shown. The talk is a product pitch from a vendor with a booth, so the evidence is anecdotal.

## Key ideas
- **Dashboards are translation devices: every tool has its own query language (Datadog syntax, JQL, Slack modifiers, mismatched SQL dialects), and users really want the answer.** — Her 2022 example is a single bug report that needed five tools and five UIs. ([1:10](https://youtu.be/YiFqcu9YA38?t=70))
- **The 2023 sparkle button put LLM query generation inside dashboards, but it only handled simple questions.** — She jokes that it works only if the question needs no more than two database joins. ([2:40](https://youtu.be/YiFqcu9YA38?t=160))
- **MCP gives agents a standard channel into apps, but the service decides how well agents can use it, and naive MCP servers are messy.** — Anthropic announced MCP in November 2024. She argues the protocol alone is not the end of the story. ([2:40](https://youtu.be/YiFqcu9YA38?t=160))
- **Three failures of wired-up MCP servers: agents have no memory across conversations (skills are a band-aid), more tools and context make agents worse, and each app is isolated.** — Her team's GitHub toolkit alone has over 200 tools, and the model drowns, picks the wrong one, or misorders dependencies. ([3:53](https://youtu.be/YiFqcu9YA38?t=233))
- **Task-first discovery: the agent states what it wants to do, and the search returns the right tools plus a plan for using them, including prerequisite lookups.** — Example: for Slack, the agent must find the channel ID before it can query messages. ([5:18](https://youtu.be/YiFqcu9YA38?t=318))
- **Her mock-up takes a pasted Slack link to a root cause and draft PR in under five minutes by pulling Datadog, Sentry and code in parallel. This is a mock-up, not a live run.** — She says no workflow or skill had to be built for it. ([5:18](https://youtu.be/YiFqcu9YA38?t=318))
- **Large results should stay out of the model context: the agent saves query output and inspects the schema and samples before generating a query in a remote workbench.** — In the PostHog and Metabase example, user IDs are stored and never loaded into context. ([8:06](https://youtu.be/YiFqcu9YA38?t=486))
- **Design for agents as a new user: no eyes, a goal and a tool set, and it judges the product on whether the job got done.** — She closes by saying the next era belongs to products that are easy for agents to use. ([9:27](https://youtu.be/YiFqcu9YA38?t=567))

## Techniques
- **Task-first tool discovery** — Have the agent declare its sub-tasks up front (for example, fetch Slack messages, search Sentry issues, search Datadog logs). The search endpoint returns the tools for each sub-task plus an ordered plan with prerequisite steps, such as resolving a Slack channel ID before querying messages. The agent then loads only those tools instead of the whole catalog. *When:* Cross-app tasks where the full tool catalog would overflow the context window (she cites a 200+ tool GitHub toolkit).
- **Parallel fetch after planning** — Once the plan identifies independent data sources, query them concurrently (she names Datadog and Sentry, plus scanning the codebase), then correlate the results to find the root cause. *When:* Incident or bug triage that spans observability tools and the codebase.
- **Keep bulky results out of context** — Store raw query output in a saved variable or workspace and pass only references or filtered subsets to the model. Use a remote code workbench to filter or aggregate the data programmatically rather than loading it into the conversation. *When:* Queries that return large sets of IDs or rows, where the agent only needs a subset or an aggregate.
- **Schema-first exploration before querying** — List the database schema, sample a few rows, and only then generate the SQL. In her demo this is done through Metabase before a regex-based SQL query is written in the workbench. *When:* Working with an unfamiliar database or BI tool.
- **Bug-report prompt to an agent with connected tools** — Paste the Slack message link and ask the agent to use the named observability tool, find the root cause, and create a draft PR. She uses a closing instruction along the lines of 'make no mistakes'. The talk does not give the exact prompt beyond this. *When:* Triaging a user-reported bug where the evidence sits across chat, logs, error tracking and code.

## Numbers
- A single 2022 bug-report workflow needed five tools and five UIs. ([1:10](https://youtu.be/YiFqcu9YA38?t=70))
- The 'sparkle button' LLM query generation handled only questions needing no more than about two database joins (her joke). ([2:40](https://youtu.be/YiFqcu9YA38?t=160))
- Her team's GitHub toolkit alone has over 200 tools. ([3:53](https://youtu.be/YiFqcu9YA38?t=233))
- Mock-up: Slack link to root cause and draft PR in under five minutes. ([5:18](https://youtu.be/YiFqcu9YA38?t=318))
- Composio vs each app's native MCP on the same tasks and model: 'early unreleased results' showing a clear difference, with no figures shown. ([5:18](https://youtu.be/YiFqcu9YA38?t=318))
- Cross-source analysis (PostHog users to Metabase toolkits) completed in 'less than a few minutes'. ([8:06](https://youtu.be/YiFqcu9YA38?t=486))

## Hot takes
- Vendor pitch: Composio sells the agent-facing layer the talk recommends, and the talk ends with a booth plug at 8:06. Quality is capped at 2 for that reason.
- The headline 'dashboards are dead' is rhetoric. The demo is labelled a mock-up, and the Composio-vs-native comparison is unreleased with no numbers, so the performance claim cannot be checked.
- The diagnosis (context bloat from many tool definitions, no cross-session memory, apps isolated from each other) is more credible than the fix. The talk does not show how task search ranks tools or how the workbench is sandboxed.
- Framing 'agents judge you on exactly one thing' is persuasive, not evidence.

## Tools mentioned
Composio (MCP, CLI, native tools, Composio Search, Composio Remote Workbench), Claude, MCP (Model Context Protocol, announced by Anthropic Nov 2024), Datadog, Sentry, Slack, GitHub, Jira (JQL), VS Code, PostHog, Metabase, SQL, skills

## Relevance to our work
- **agentos** (1/3):  → *Measure on a multi-app task whether a flat tool list or a task-scoped tool subset gives fewer wrong-tool calls and fewer tool-definition tokens, using the proxy as the measurement point.*
- **prosharness** (1/3): Long Claude Code runs suffer from the same context bloat, and keeping bulky results out of context fits the harness's checkpointing design. → *Check whether long ProsHarness runs write bulky tool output to files and pass paths, instead of pasting it into the context window.*
