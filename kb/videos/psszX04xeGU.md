# MCP vs REST vs A2A How AI Agents Actually Talk

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `psszX04xeGU` · [watch](https://youtu.be/psszX04xeGU) · **date:** 2026-08-02 · **length:** 8:29 · **format:** other · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Google, Microsoft, OpenAI, Linux Foundation
- **topics:** mcp-and-tools, agent-architecture, multi-agent · **tags:** mcp, a2a, rest, agent-protocols, agent-interop, json-rpc, agent-cards, explainer

> Explainer arguing REST, MCP and A2A are stacked layers, not rivals: REST links programs, MCP links an agent to tools, A2A links agents to agents. Advice: learn MCP first and add A2A only for multiple independent agents.

## Summary
The host argues that REST, MCP and A2A are not competing choices but layers that stack: REST connects programs to programs, MCP connects an agent to its tools, and A2A connects an agent to other agents. He frames the problem as M models times N tools, where every pairing needs a hand-written translator, and presents MCP as a shared tool-description standard that turns that into M plus N. He notes MCP runs on JSON-RPC 2.0 over stdio locally or HTTP remotely, and that many MCP servers are thin wrappers around existing REST APIs. A2A is presented as agent discovery through published agent cards and delegation to specialist agents. He is skeptical of A2A hype, citing 2025 criticism that it had stalled, and says many teams do not need multi-agent systems yet. His practical rule is to keep REST underneath, use MCP for tools, and reach for A2A only when independent agents from different vendors must coordinate. The video has no code, benchmarks or measured results, so it is conceptual rather than evidence-backed.

## Key ideas
- **REST vs MCP vs A2A is a false choice; they are layers.** — The host says the three protocols run on the same plumbing and stack. REST is the base transport, MCP sits on tools, and A2A sits on agent coordination. The apparent rivalry comes from all three becoming popular in the same 18-month window. ([0:00](https://youtu.be/psszX04xeGU?t=0))
- **Without a standard, each tool needs a custom translator, which scales as M times N.** — Each new tool needs its own glue code for each model or agent. The host calls this the M-times-N problem and uses 10 tools as the example of the pain. ([1:28](https://youtu.be/psszX04xeGU?t=88))
- **MCP turns M-times-N into M-plus-N by standardizing tool descriptions.** — A tool exposed once over MCP can be used by any MCP-capable agent. MCP uses JSON-RPC 2.0, runs over stdio for local tools or HTTP for remote ones, and is often a thin layer over the REST API behind the tool. ([2:56](https://youtu.be/psszX04xeGU?t=176))
- **A2A adds discovery and delegation between agents.** — Each A2A agent publishes an agent card at a well-known address describing its identity, skills, endpoint and auth requirements. A calling agent reads the card, finds a specialist and hands off work. Google launched A2A on April 9, 2025. ([4:20](https://youtu.be/psszX04xeGU?t=260))
- **A2A had a hype cycle and a doubt cycle, and the host advises waiting before adopting it.** — By September 2025 critics said A2A had stalled and that most systems were one agent plus tools, which made multi-agent coordination unnecessary. The host says the picture looked healthier in 2026 but still does not treat A2A as essential. ([5:37](https://youtu.be/psszX04xeGU?t=337))
- **The one-sentence rule: REST connects programs to programs, MCP connects an agent to tools, and A2A connects agents to agents.** — The host's practical order is REST underneath everything, MCP for most people, and A2A only once there are several real agents that must hand work to each other. He says Anthropic and Google both donated their protocols to neutral foundations, so readers should check the standard itself rather than the press release. ([6:56](https://youtu.be/psszX04xeGU?t=416))

## Techniques
- **Map each integration to one protocol layer** — Use REST for program-to-program calls, MCP for an agent calling tools, and A2A for one agent delegating to another agent. Treat them as stacked layers, not alternatives. *When:* When designing or reviewing any link between an AI system and a backend, to decide which protocol belongs there.
- **Expose each tool once as an MCP server** — Describe each tool (name, purpose, arguments, result) in MCP's shared format using JSON-RPC 2.0. Run it over stdio for a local process or HTTP for a remote service, so any MCP-capable agent can call it without custom glue. *When:* When more than one agent or model needs the same tools, or when the number of tool integrations is growing.
- **Wrap an existing REST API with a thin MCP server** — Keep the existing REST service as the system of record. Build a small MCP server in front of it whose tool handlers make the REST calls, rather than rewriting the service. *When:* When exposing an internal service to agents without changing how the service itself is built.
- **Publish an agent card for discovery and delegation** — Serve a card at a well-known address listing the agent's identity, skills, endpoint and how to authenticate. The caller fetches the card, checks the skills, and delegates the task to that agent. *When:* When several independent agents, possibly from different vendors, need to find and hand work to each other.
- **Adopt multi-agent protocols only when the pain is specific** — Start with one agent plus tools using MCP. Add an agent-to-agent layer only after you have multiple independent agents that must coordinate and you can name the coordination failure. *When:* When deciding whether a project needs A2A or any multi-agent protocol at all.

## Numbers
- Three protocols were all rising in the same 18 months. ([0:00](https://youtu.be/psszX04xeGU?t=0))
- Example of M-times-N glue: 10 tools need 10 custom translators, and each new model needs all of them rewritten. ([1:28](https://youtu.be/psszX04xeGU?t=88))
- MCP launched from Anthropic in November 2024. ([1:28](https://youtu.be/psszX04xeGU?t=88))
- Within about a year of launch, MCP reached tens of thousands of servers and tens of millions of downloads a month, with OpenAI, Microsoft and Google adopting it. ([2:56](https://youtu.be/psszX04xeGU?t=176))
- Anthropic handed MCP to a Linux Foundation fund in December 2025. ([4:20](https://youtu.be/psszX04xeGU?t=260))
- A2A launched from Google on April 9, 2025. ([4:20](https://youtu.be/psszX04xeGU?t=260))
- Google donated A2A to the Linux Foundation in June 2025. Since then it has drawn 150+ member organizations. ([5:37](https://youtu.be/psszX04xeGU?t=337))

## Hot takes
- The 'REST vs MCP vs A2A' framing is quietly wrong because the three are stacked layers, not competitors.
- About 90% of people should stop at MCP. A2A is only needed once multiple independent agents must coordinate.
- Anthropic and Google donating their protocols to neutral foundations is positioning, so read the standard rather than the press release.
- The claim that A2A looked healthier in 2026 is asserted without specifics. The video is conceptual with no benchmarks, code or sources.

## Tools mentioned
REST, MCP (Model Context Protocol), A2A (Agent2Agent), JSON-RPC 2.0, HTTP, stdio

## Relevance to our work
- **agentos** (2/3): AgentOS puts a proxy in front of agents and exposes pillars such as the Crucible sandbox and MemoryMesh retrieval, so tool-facing interfaces matter. The video's layering (REST underneath, MCP for tools, A2A deferred) maps onto that design. → *Decide whether the Crucible and MemoryMesh tool surfaces should be exposed as MCP servers wrapping their existing REST APIs. Document that A2A is deferred until AgentOS hosts multiple independent agents.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and has phone-driven approvals. An MCP interface could expose checkpoints or approvals to other agents, but the video does not add a concrete pattern beyond that. → *Low priority. If ProsHarness exposes checkpoint or approval controls to other agents, use an MCP server over a thin REST layer and skip A2A unless multiple vendor agents need to coordinate.*
