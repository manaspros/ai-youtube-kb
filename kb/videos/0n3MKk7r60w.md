# Scaling GitHub for your Agents — Sam Morrow, GitHub

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `0n3MKk7r60w` · [watch](https://youtu.be/0n3MKk7r60w) · **date:** 2026-05-18 · **length:** 20:35 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Sam Morrow · **orgs:** GitHub, Anthropic, OpenAI, Cloudflare, LangChain, VS Code, Invariant Labs
- **topics:** mcp-and-tools, context-engineering, security-guardrails · **tags:** MCP, GitHub MCP server, tool count, tool sets, dynamic tool discovery, token reduction, OAuth 2.1, PKCE, step-up auth, scope filtering, stateless server, prompt injection, tool descriptions, evals, Redis

> GitHub's MCP server lead on scaling a remote MCP server: why too many tools hurt agents, how defaults and tool-set grouping work, token-trimmed outputs, scope-based auth, and a stateless design.

## Summary
Sam Morrow (GitHub, leads development of GitHub's MCP server) reviews a year of running a large public MCP server. The server grew past 100 tools, and agents got worse at using GitHub and burned context. Grouping tools into sets and dynamic tool discovery helped, but almost all users kept the defaults, so he argues that client-side gaps and spec gaps are being papered over with server modes. The team cut the default load by about 49%, trimmed output tokens, moved multi-call logic server-side, and tuned tool descriptions by evaluating them against each other. On security he covers long-lived plain-text tokens, OAuth 2.1 with PKCE (rejecting dynamic client registration), scope-filtered tool lists with step-up OAuth, and prompt-injection exfiltration risk that is not yet solved. The server runs stateless, building a fresh server instance per request, with Redis for session data. He closes by predicting thousands of tools will become normal and encourages people to build new clients and wrap read-only tools in CLIs to test them.

## Key ideas
- **More tools make agents worse, not better. Once the server passed 100 tools, agents got confused and forgetful, and context windows filled faster.** — The problem is the tool definitions loaded into context up front, so the fix is to reduce what is in context, not only to add features. ([2:16](https://youtu.be/0n3MKk7r60w?t=136))
- **Configuration features did not fix the problem because users keep defaults.** — Tool sets and dynamic tool selection were built, but most users never edited the JSON. He suggests some of these modes paper over gaps in client implementations and the MCP spec. Grouping proposals were rejected in the spec several times. ([3:36](https://youtu.be/0n3MKk7r60w?t=216))
- **A read-only mode maps to a hint annotation, but no client filters servers on that hint.** — About 17% of users use read-only mode. It is an easy win for enterprise use, and some gateways now support this kind of filtering. ([4:37](https://youtu.be/0n3MKk7r60w?t=277))
- **Shrink the default surface: focus tools on common cases, group CRUD tools, and land near 40 tools by default.** — This cut the initial load by about 49% at first, with further reduction from grouping. Users can expand or contract from that default. ([4:37](https://youtu.be/0n3MKk7r60w?t=277))
- **Tailor tool output to what the agent needs. Trimming the pull request list output removed more than 75% of its tokens.** — Output size is treated as a tuning target, not only input size. The token cost of GitHub's server is a moving target that changes with each release. ([5:51](https://youtu.be/0n3MKk7r60w?t=351))
- **Move multi-step logic into the server. Encoding agent intent in the tool surface cut tool failures, and success is now above 95%.** — Doing several API calls on the server saves round trips, context, and time. Some errors remain because agents hallucinate permissions and repo access. ([7:16](https://youtu.be/0n3MKk7r60w?t=436))
- **Evaluate tool descriptions against each other, not one at a time. The goal is to get each tool called at the right moments and not at the wrong ones.** — Micro-tuning one description can make the agent call that tool too often. The team wrote up its eval approach in a blog post. ([7:16](https://youtu.be/0n3MKk7r60w?t=436))
- **Long-lived plain-text tokens are a security problem. Remote HTTP with OAuth 2.1 and PKCE is the safer default, but dynamic client registration was rejected.** — Unbounded app growth, rate-limit bucketing, and no reliable app identity made DCR a bad fit. Client ID metadata is the direction he is pushing for. ([8:41](https://youtu.be/0n3MKk7r60w?t=521))
- **Prompt injection exfiltration applies to almost any agent setup, not just MCP. Utility and safety conflict, and no one has solved it.** — He points to the lethal trifecta framing and says the fix is still open. Users have very different risk profiles, from air-gapped Enterprise Server to full-token agents. ([10:09](https://youtu.be/0n3MKk7r60w?t=609))
- **Filter the tool list by the caller's token scopes. Step-up OAuth lets a call ask for more scope interactively rather than fail.** — Tools that need user identity are removed for server tokens. This cuts failures and wasted context together. ([12:37](https://youtu.be/0n3MKk7r60w?t=757))
- **Run the server stateless. A new SDK server instance is built on every request with only the allowed tools, and sessions are used only to identify the client.** — No session affinity is needed. Redis holds session storage. The server handles about 7 million tool calls per week. ([13:59](https://youtu.be/0n3MKk7r60w?t=839))

## Techniques
- **Per-request server construction with policy-filtered tools** — Create a new server instance for each request. Add only the tools the caller's config and policy allow. Keep state in an external store such as Redis, and use sessions only for client identification. *When:* Running a remote MCP server at scale where config, policy, and token scope change which tools a caller may use, and where session affinity is undesirable.
- **Scope-filtered tool listing with step-up auth** — Read the token's scopes and return only matching tools. If a call needs more scope, return a scope challenge so the user can grant it interactively, and then continue the call instead of failing. *When:* A tool surface spans permission levels and users may start with a narrow token but later need more access.
- **Tool-set grouping with defaults tuned from usage data** — Group related tools into sets. Choose the default set from observed usage, collapse CRUD operations, and let users expand or contract from there. *When:* The server has many tools and the default config is what most users will actually run.
- **Output-token tailoring per tool** — Review each list or read tool's output and return only the fields the agent uses. Measure token count before and after. *When:* Tools return large JSON payloads that fill the context window.
- **Server-side composition to encode intent** — Combine several API calls into one tool that handles the sequence and checks permissions, so the agent makes one call with fewer round trips. *When:* Agents need several calls to complete a common task, or fail because they guess the wrong permission or repo.
- **Cross-tool eval for description tuning** — Write tasks, run the agent with the full tool set, and check whether each tool is called at the right times and not when a sibling tool should be used. Adjust descriptions as a group. *When:* Adding or changing tools that overlap in purpose.
- **Wrap read-only tools in a CLI to test agent use** — Take a server's read-only tools, expose them through a CLI with good help text, and see how an agent uses them before building a full integration. *When:* Early exploration of whether an agent can use a set of tools well.

## Numbers
- Open-sourced the local MCP server in April 2025, now about one year old; it was the most-starred repo on GitHub for that week. ([1:15](https://youtu.be/0n3MKk7r60w?t=75))
- The server passed 100 tools at one point, which the speaker calls too many. ([2:16](https://youtu.be/0n3MKk7r60w?t=136))
- About 17% of users use the read-only mode. ([4:37](https://youtu.be/0n3MKk7r60w?t=277))
- Focusing tools on common cases cut the initial context load by about 49%. The default config now exposes about 40 tools. ([4:37](https://youtu.be/0n3MKk7r60w?t=277))
- Tailoring the pull request list output cut its output tokens by more than 75%. ([5:51](https://youtu.be/0n3MKk7r60w?t=351))
- Tool success rate is roughly above 95%. ([5:51](https://youtu.be/0n3MKk7r60w?t=351))
- About 7 million tool calls per week, later stated as nearly 8 million. ([13:59](https://youtu.be/0n3MKk7r60w?t=839))
- The standard IO server has over 11 million Docker downloads; the repo has about 30,000 stars, about 4,000 forks, 126 contributors, and over 2,300 issues and PRs. ([19:19](https://youtu.be/0n3MKk7r60w?t=1159))
- Over seven new issues or PRs a day, every day, for more than a year. ([19:19](https://youtu.be/0n3MKk7r60w?t=1159))

## Hot takes
- More tools do not make better agents; they get confused and forgetful.
- Most configuration modes paper over gaps in client implementations and the MCP spec.
- Thousands of tools will be normal soon, and many fewer-tools decisions will be reversed.
- Users should not need to know what MCP is; they should state what they want and the tool selection should happen automatically.
- Long-lived plain-text access tokens for MCP are a constant menace.

## Tools mentioned
GitHub MCP server, Claude Code, VS Code, Redis, Cloudflare code mode, Anthropic tool search, Pi

## Relevance to our work
- **general** (2/3): The talk is a practitioner account of tool count, tool-description evals, and output trimming, which matches the context-engineering and eval interests. → *Read the GitHub blog post on evaluating tool descriptions against each other, and use its method on one overlapping tool set.*
- **agentos** (1/3): AgentOS's L1 proxy already does budgets and PII scans. The talk's tool-list pruning and output trimming are MCP-specific, so the match is only indirect. → *Read the tool-set and scope-filtering sections of the talk, then decide whether the L1 proxy should trim large tool outputs in traffic it already sees. Not a priority now.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and MCP tools load into its context. The advice to keep the default tool set small and test descriptions as a group applies only if ProsHarness loads MCP servers. → *Check how many MCP tools a ProsHarness run loads at checkpoint time. If the count is high, try a smaller default set and compare the number of wrong tool calls.*
