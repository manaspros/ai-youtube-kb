# Gateways are All You Need — Karan Sampath, Anthropic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `CD6R4Wf3jnY` · [watch](https://youtu.be/CD6R4Wf3jnY) · **date:** 2026-05-18 · **length:** 17:48 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Karan Sampath · **orgs:** Anthropic
- **topics:** mcp-and-tools, security-guardrails, governance-compliance, infra-cost-scaling · **tags:** MCP gateway, enterprise MCP, access control, observability, root of trust, pluggable credentials, agent harness separation, MCP registry, Claude managed agents

> Anthropic forward-deployed engineer Karan Sampath argues enterprises should put one gateway in front of all MCP servers for auth, access control, observability and credentials, so teams build only business logic.

## Summary
The speaker, a forward-deployed engineer at Anthropic, says enterprises struggle with MCP on three fronts: observability (who uses which tool, which tools fail), access control (who can call or change which servers), and security (verifying servers and letting untrusted clients reach private data). He argues a public registry is useful but not enough for an enterprise, because auth, access control, observability and credential management are missing. His core recommendation is for security teams to bless one platform as the root of trust, with a gateway sitting between any MCP client and the MCP servers behind it. The gateway handles auth, roles, routing, secure tunnels, an internal sub-registry and a CLI, so a team that builds a server only writes its business logic and an agent can scaffold the rest. He lists follow-on benefits: a new client surface plugs in once, connections are more secured, teams iterate without repeated security reviews, enterprise standards get encoded, credentials are swappable, and scale is handled in one place. He ends by saying the agent harness should be separated from the data layer so the in-house vs hosted agent choice stays reversible. The talk has no benchmarks; the scale figures are illustrative.

## Key ideas
- **Enterprises get stuck with a handful of MCP tools because observability, access control and security are missing.** — Registries help discovery but do not cover auth, role-based access, observability or credential management. Teams can build MCP servers quickly, but security teams cannot see or approve them, so deployment stalls. ([1:07](https://youtu.be/CD6R4Wf3jnY?t=67))
- **The key move is to bless one platform as the root of trust.** — Security teams should allow decentralized MCP building by standardising on one platform. The speaker says this is the one slide to remember. Each MCP server then has knock-on value for all agents in the company. ([5:12](https://youtu.be/CD6R4Wf3jnY?t=312))
- **A gateway is a middle layer between any MCP client and many MCP servers.** — Clients see only the gateway. Servers trust only the gateway. The gateway covers auth, roles, routing, a secure tunnel, an internal sub-registry and a CLI for creating servers. ([7:33](https://youtu.be/CD6R4Wf3jnY?t=453))
- **Teams that build servers should only write business logic.** — Example: a legal team writes a contract-review server by encoding its own red-line and escalation rules. It does not handle who can access it, how often, or scaling. An agent can use the gateway CLI to scaffold a new server. ([8:27](https://youtu.be/CD6R4Wf3jnY?t=507))
- **Once a gateway exists, several benefits come almost free.** — New surfaces (claude.ai, Claude Code and others) plug in once. Connections are encrypted with a root of trust over data sent out. Teams iterate without new security reviews. Standard primitives encode company procedures. Credentials are swappable (user, team, service account). Scaling is handled in one place. ([11:27](https://youtu.be/CD6R4Wf3jnY?t=687))
- **Keep the agent harness separate from where the data and MCP servers live.** — Agents should not be tightly coupled to data structure. Whether an agent runs in-house or hosted becomes a choice the gateway does not depend on. The speaker points to a recent release connecting a gateway to managed agents and the Claude Agent SDK. ([14:53](https://youtu.be/CD6R4Wf3jnY?t=893))
- **Summary: invest in shared infra, build root of trust, separate harness from data.** — Do not roll your own MCP gateway. Let teams build their own MCP servers on top of it. Gateways make the root of trust explicit. Observability should also cover how each tool is defined, so the load-bearing tools can be improved. ([16:13](https://youtu.be/CD6R4Wf3jnY?t=973))

## Techniques
- **Single gateway in front of all MCP servers** — Clients connect only to the gateway. Each MCP server treats the gateway as its only trusted endpoint. The gateway handles auth, role-based access, routing, encrypted tunnels and a sub-registry of internal servers. *When:* An enterprise has many teams building MCP servers, and security needs one place to verify and control access.
- **Gateway CLI as a scaffold for new MCP servers** — A gateway CLI generates a new server already wired to auth, access control, observability and deployment. A coding agent can run it, so the team only writes tool logic. *When:* Teams should build their own MCP servers without waiting on a central platform team.
- **Encode enterprise standards as gateway policy** — The gateway enforces which primitives, tools and patterns are allowed or forbidden, so each new server follows company rules without a manual review. *When:* Agents must meet company operating procedures and security rules.
- **Pluggable credentials at the gateway** — The gateway swaps credential types (per user, per team, service account) for each server, so servers do not each need to support every auth method. *When:* Different servers or use cases need different kinds of user or service identity.
- **Observability on tool definitions, not only call counts** — Track which tools are used most, and how each tool is defined, so the load-bearing tools can be found and revised as the protocol changes. *When:* The MCP spec and tool definitions change quickly and need ongoing tuning for many agents.
- **Separate agent harness from data layer** — Put the data and MCP servers behind the gateway, and let agents (in-house or hosted) connect to the gateway as clients. Changing or swapping an agent then does not change the gateway. *When:* Enterprises run many agent types and expect the agent choice to change over time.

## Numbers
- The official MCP registry lists over thousands of servers, and growth was rapid over the prior year. ([1:07](https://youtu.be/CD6R4Wf3jnY?t=67))
- Illustrative example: 40 separate MCP servers, each configured for only some clients, versus one gateway that all clients share. This is a hypothetical, not a measurement. ([11:27](https://youtu.be/CD6R4Wf3jnY?t=687))
- Illustrative scale target: from tens to hundreds of thousands of agents on one gateway. This is a goal the speaker describes, not a benchmark. ([14:53](https://youtu.be/CD6R4Wf3jnY?t=893))

## Hot takes
- Enterprises should not roll their own MCP gateway. They should adopt common infra.
- A registry is not enough for enterprises. Auth, access control, observability and credentials are the gap.
- Every good MCP server helps all the agents in a company, so a central gateway multiplies its value.
- Security teams should bless one platform and let teams build MCP servers themselves, so legal teams can build their own servers without going back to engineering.

## Tools mentioned
MCP, Claude Code, Claude Agent SDK, claude.ai, Claude managed agents

## Relevance to our work
- **agentos** (2/3):  → *Compare Govrix Scout's scope with the talk's five gateway components. Note which are missing for MCP traffic (RBAC per server, per-tool metrics, a scaffold CLI). Add the missing ones to the L1 backlog.*
- **prosharness** (1/3): ProsHarness wraps Claude Code and handles credentials and approvals itself. The talk's point about pluggable credentials and keeping the harness separate from data is a light, indirect fit. → *Low priority: note whether ProsHarness credential handling should delegate to a gateway for MCP calls instead of living in the harness.*
