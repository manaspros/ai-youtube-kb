# Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ws9XcGGPBDk` · [watch](https://youtu.be/ws9XcGGPBDk) · **date:** 2026-10-13 · **length:** 25:08 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kim Maida · **orgs:** Keycard
- **topics:** security-guardrails, mcp-and-tools, governance-compliance · **tags:** lethal-trifecta, token-exchange, oauth, sts, mcp-gateway, intent-based-authorization, least-privilege, ephemeral-credentials, prompt-injection, on-call-agent, delegation-chain

> Kim Maida (Keycard) argues agents with private data, untrusted content and external comms form a "lethal trifecta" and shows how token exchange (OAuth 2 RFC 8693-style STS), task-scoped ephemeral tokens and mission-based authorization contain the blast radius without removing capabilities.

## Summary
The talk opens with a live-style demo of an on-call triage agent that leaks PII, uses static API keys, drops a production database and scales pods at $420/hour with no attribution. It names the "lethal trifecta" (private data access, exposure to untrusted content, external communication) credited to Simon Willison, and argues that removing any leg makes the agent much less useful. It then argues OAuth alone (broad grants), MCP gateways (route-level policy, standing credentials) and sandboxes (process-level bounds) each fail to give task-scoped access. The proposed fix is token exchange, an open standard from 2020 that extends OAuth 2: the user logs in, the agent's runtime exchanges the user's subject token at a security token service for a short-lived token per tool call, and the MCP server exchanges again for downstream resources, keeping the user in the delegation chain. Policy decides per request, and the speaker proposes intent-based authorization (a mission with goal and limits, approved by the user, checked by the gateway on each call) as a next step, though it is not yet a standard. The rerun demo shows PII access denied, the certificate renewal allowed, the database drop refused, and a restart blocked because the user lacked the role, while scaling passed after approval. The speaker is a Keycard GTM engineer, so the talk carries a vendor angle.

## Key ideas
- **The lethal trifecta: private data access + exposure to untrusted content + ability to communicate externally. Together they open the door for attackers.** — Speaker attributes the term to Simon Willison. The argument is that the same capabilities that make agents useful make them dangerous, so the fix is to control access rather than remove a capability. ([5:04](https://youtu.be/ws9XcGGPBDk?t=304))
- **Human-in-the-loop approval is not a complete control because it shifts access control to a consent-fatigued user.** — Speaker says forcing approvals pushes the security problem up the chain, and many agents run autonomously with no human at all, so approvals cannot be used everywhere. ([5:39](https://youtu.be/ws9XcGGPBDk?t=339))
- **OAuth, MCP gateways and sandboxes each bind access to something other than the task, so none gives task-scoped access alone.** — OAuth binds to a broad grant made before any task exists. A gateway binds to a route and holds standing credentials. A sandbox binds to a process, but useful work must reach outside it, which brings standing access back. ([6:46](https://youtu.be/ws9XcGGPBDk?t=406))
- **Token exchange (an existing standard extending OAuth 2) can issue a short-lived, per-tool-call token that keeps the user as subject and records the exchanging app.** — Flow: user logs in and consents to scopes; the agent runtime calls a security token service with its client or workload credentials plus the user's subject token; the STS checks policy and mints a token for that one tool call. Tokens should expire within minutes and never be stored. ([12:56](https://youtu.be/ws9XcGGPBDk?t=776))
- **Policy is a ceiling, so the speaker proposes intent-based authorization: the user approves a mission (goal, allowed actions, limits) and the gateway checks each tool call against it.** — Low-risk missions can be auto-approved. Higher-risk ones (e.g. scale a service once) are shown to the user. Speaker says IBA is not a finalized standard and Keycard's approach is one proposal. ([14:04](https://youtu.be/ws9XcGGPBDk?t=844))
- **In the rerun demo, the same agent behaviour was judged by policy: PII was denied, the cert renewal was allowed, the DB drop was refused, and a restart was blocked for a user without the role.** — Speaker notes the agent cannot take an action the human also cannot take, since the agent acts on the user's behalf. Scaling was approved and passed because the role allowed it. ([20:24](https://youtu.be/ws9XcGGPBDk?t=1224))

## Techniques
- **Per-tool-call token exchange through an STS** — Agent runtime sends the user's subject token and its own client credentials to a security token service, requesting access for one tool call. The MCP gateway proxies the call. Tokens are short-lived, never stored, and discarded after use. A second exchange is done for downstream resources. *When:* Agents that act on behalf of a user and touch several production systems, where static API keys or standing credentials are the risk.
- **Mission-scoped approval before tool use** — The agent proposes a mission with a goal and limits, the user approves it, and the STS issues a mission ID. Each tool call carries that ID and the gateway asks the STS whether the call fits the mission. *When:* Tasks where a broad grant would over-permission the agent, and where a human should see what the agent intends to do before it acts.
- **Keep all three trifecta legs and control access instead** — Do not remove private data, untrusted input or external communication. Constrain each with identity-bound, task-scoped, short-lived credentials and policy checks. *When:* When removing a capability would make the agent too weak to be useful.
- **Audit with attributed identity chains** — Each token keeps the user as subject and records the exchanging app, so logs show which user and which agent made each call. *When:* When an audit log cannot say who used an API key, which was the failure in the demo.

## Numbers
- Scaling from 4 to 40 pods in the naive demo incurred about $420 per hour. ([3:58](https://youtu.be/ws9XcGGPBDk?t=238))
- The token exchange standard is described as published in 2020, extending OAuth 2. ([8:59](https://youtu.be/ws9XcGGPBDk?t=539))
- Access tokens from token exchange should expire within minutes (speaker gives no exact figure). ([16:17](https://youtu.be/ws9XcGGPBDk?t=977))

## Hot takes
- Human-in-the-loop approval moves the access-control problem onto a consent-fatigued user.
- OAuth alone, MCP gateways alone and sandboxes alone do not provide task-scoped access control.
- Policies are ceilings, so intent (what the agent means to do) should be checked as well as policy.

## Tools mentioned
Keycard, OAuth 2 token exchange (RFC 8693 style), MCP servers, MCP gateway, Snowflake, Incident pager API, Google login

## Relevance to our work
- **agentos** (2/3): AgentOS L1 gateway and L2C Crucible sandboxing face the same trifecta problem, and the talk's per-call token exchange and mission model map onto the proxy's policy layer. → *Prototype a per-tool-call short-lived credential in the Govrix proxy, with a mission ID check, and log the user and agent identity chain.*
- **prosharness** (2/3): ProsHarness runs the Claude Code CLI with zero-token credential handling and phone-driven approvals, and the talk's mission approval and ephemeral token model apply directly. → *Consider scoping ProsHarness approvals to a mission (goal and allowed tools) approved once, instead of per-tool prompts, and check that no credential is stored by the harness.*
- **general** (1/3): Security framing for any agent with private data, untrusted input and external calls; useful background, not a concrete change. → *Read the token exchange standard (2020) and the Keycard IBA proposal before designing agent auth.*
