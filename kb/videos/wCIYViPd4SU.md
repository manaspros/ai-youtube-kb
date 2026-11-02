# Tethered: Our Agents Are Us — Shu Fang, Two Sigma

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `wCIYViPd4SU` · [watch](https://youtu.be/wCIYViPd4SU) · **date:** 2026-09-18 · **length:** 21:10 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Shu Fang (introduced as Xu Feng in the transcript) · **orgs:** Two Sigma, Google (Web Grounding for Enterprise), Anthropic (Claude Code)
- **topics:** security-guardrails, enterprise-adoption, claude-code, observability · **tags:** agent identity, attribution header, web grounding, egress control, prompt injection, regulated industry, cloud agents, claude code, kubernetes namespaces, mcp cli

> Two Sigma explains how it runs cloud agents as each employee's own identity, using a propagated attribution header and enterprise-grounded web search to cut exfiltration risk.

## Summary
Xu Feng (credited as Shu Fang in the title) from Two Sigma describes how the firm moved cloud coding agents from local CLIs to remote runs under each employee's real identity. The naive shared "shadow agent" identity broke down on permission sync, licensing and blocked systems, so the firm reused per-user Kubernetes namespaces it already had in every region. The main risks he names are losing track of whether a human or an agent acted, and exfiltration or prompt injection through open web access. To handle attribution, every agent appends to an identity header, much like a trace ID, so the full action chain can be replayed. To handle web access, the native web search and fetch tools are denied and requests go through Google's enterprise web grounding inside the VPC, which trades freshness (about 6 to 24 hours) for removing external egress. He frames this as optimizing return over risk and says the firm lost no expected value while cutting risk. The firm now ships a managed fleet of cloud agents for every user. He also says he expects to move more token use to self-hosted open-weight models over time, for cost and to avoid volatility from model updates.

## Key ideas
- **Run agents under the user's own identity, not a separate machine or shadow identity.** — A separate agent identity was hard to keep in sync, doubled licensing, and was blocked by some systems such as Google Workspace. Running as the user avoids those constraints. ([2:13](https://youtu.be/wCIYViPd4SU?t=133))
- **Reuse existing per-user Kubernetes namespaces for remote agents.** — Every user already had namespaces in every region for automated jobs. A sidecar identity service mounts the user's identity into the pod, so the agent runs as that person. ([3:42](https://youtu.be/wCIYViPd4SU?t=222))
- **Two core risks: attribution and external exfiltration.** — Without a distinction, a human action and an agent action look the same and cannot be audited or blocked separately. Open web access also brings exfiltration, prompt injection and licensing risk. ([4:43](https://youtu.be/wCIYViPd4SU?t=283))
- **Frame the design as return over risk, not as a yes or no on agents.** — The goal is to keep most of the value of agents running as users while reducing the two main risks. ([6:42](https://youtu.be/wCIYViPd4SU?t=402))
- **Propagate an attribution header the way trace IDs are propagated.** — Every agent appends to the header. It is enforced through HTTP clients, MCP servers and skills. This lets the team replay the full chain of actions that led to a result, not only the first actor. ([8:10](https://youtu.be/wCIYViPd4SU?t=490))
- **Deny native web tools and route web access through enterprise grounding.** — Native web search and fetch are removed from the agent's tool set. Requests go through an MCP CLI and skills to Google's web index inside the VPC. Freshness lags by hours (about 24 hours in general, about 6 hours for frequently updated sites). ([9:38](https://youtu.be/wCIYViPd4SU?t=578))
- **Tagging gives observability; identity verification is not the only control.** — The speaker says the header adds a lot of observability over pure identity checks. The firm accepts index lag as the cost of removing egress. ([12:01](https://youtu.be/wCIYViPd4SU?t=721))
- **Enterprise infrastructure can make risky agent capabilities acceptable.** — He argues that a personal machine with full permissions is the worse default. Using enterprise controls can reduce the risk and still deliver the value. ([13:30](https://youtu.be/wCIYViPd4SU?t=810))

## Techniques
- **Run agents as the user identity in existing per-user namespaces** — Trigger a controller that starts a pod in the user's namespace. A sidecar identity service provides the user's identity to the containers, so the agent acts as that user. *When:* You already run per-user namespaces for automated jobs and want remote agents without a separate machine identity.
- **Propagate an attribution header like a trace ID** — Populate an agent-actor header at the first entry point. Enforce it with HTTP clients, MCP tools and skills so every downstream hop appends to it. Record it on spans as you would a trace ID. *When:* You need to tell human actions from agent actions and replay the chain of actions behind an outcome.
- **Deny native web tools and route through enterprise grounding** — Remove the harness's built-in web search and fetch tools from the tool list. Expose search and fetch through an MCP CLI and skills that call the grounded index inside the network boundary. *When:* External egress and prompt injection from web content are the main risks, and slightly stale results are acceptable.
- **Enforce tool behaviour with existing harness primitives** — Use the agent harness's configuration to block tools, and use skills and MCP to make the intended path the default. Do not rely on the model's choice alone. *When:* You want policy enforcement on agent behaviour without changing the model.

## Numbers
- Firm is about 25 years old and regulated. ([1:10](https://youtu.be/wCIYViPd4SU?t=70))
- Claude Code GA around June 2025, when the local-machine pattern was common. ([2:13](https://youtu.be/wCIYViPd4SU?t=133))
- Web grounding freshness: within 24 hours generally, within 6 hours for frequently updated sites (as the speaker last checked). ([10:38](https://youtu.be/wCIYViPd4SU?t=638))
- Every user has a managed cloud agent; the work described happened over 2025. ([14:28](https://youtu.be/wCIYViPd4SU?t=868))

## Hot takes
- Running agents under a person's real identity is acceptable in a regulated firm if attribution and egress are controlled.
- Stale enterprise search (hours old) is a good trade for removing external web egress.
- A personal machine with full agent permissions is a worse default than enterprise infrastructure with guardrails.
- Self-hosted open-weight models will win on cost and stability for many enterprise token workloads.

## Tools mentioned
Claude Code, Google Web Grounding for Enterprise, MCP CLI, Kubernetes, Brave Search (native web tool in Claude Code, per speaker)

## Relevance to our work
- **agentos** (2/3): The attribution header and replayable action chain map onto AgentOS's Merkle audit log and proxy. Its L1 proxy could record an originating-actor header, which is the speaker's core observability idea. → *Add an originating-actor header to requests through the Govrix proxy, carry it into the Merkle audit entries, and check that an agent-to-tool hop keeps the same actor ID.*
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI. The speaker's method of denying native web tools and routing through a controlled MCP path fits its approval and credential-safety goals. → *Test denying the native WebSearch and WebFetch tools in the Claude Code settings the harness generates, and route web lookups through one MCP tool that the harness controls and logs.*
