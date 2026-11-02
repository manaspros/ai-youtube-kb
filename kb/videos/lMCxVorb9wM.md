# You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `lMCxVorb9wM` · [watch](https://youtu.be/lMCxVorb9wM) · **date:** 2026-08-18 · **length:** 12:50 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ravi Madabhushi · **orgs:** Scalekit, Freshworks, ref.tools, Google, Salesforce, Databricks, HubSpot, Notion, Gmail
- **topics:** security-guardrails, mcp-and-tools, governance-compliance · **tags:** agent-identity, oauth, least-privilege, delegation, actor-vs-principal, mcp-authorization, audit-trail, just-in-time-access, spiffe, write-amplification

> Ravi Madabhushi (Scalekit) argues agents break the human and service-account identity model: they need a distinct identity bound to a principal, fine-grained time-bound scopes, and full action audit, beyond OAuth.

## Summary
The speaker starts with a latency spike every 15 minutes at his identity platform, traced to last-seen timestamp writes that agent traffic made about 60 times more frequent. Batching those writes to one-second granularity fixed it, but it exposed a bigger question: auth assumptions built for humans may not hold for agents. He says today's two identity slots (a human using an API key or session, and a service account or M2M client) both assume the actor is the principal and that a deterministic program with fixed permissions is acting. Agents break that because the program is not written by a human, its behavior is probabilistic, and OAuth on-behalf-of is often unsupported. He describes MCP servers that expose every tool a user or app can reach and rely on the agent to choose, with runtime checks as the only guard. His prescription is an agent identity bound to its principal, least-privilege scopes at attribute, context, and time level, just-in-time elevation, and an audit trail of who acted, for whom, who authorized it, and for how long. The talk is short and mostly a thesis, with light references to his company's customers.

## Key ideas
- **A latency spike every 15 minutes traced to per-user last-seen writes that agent traffic made about 60x more frequent** — Agents hitting the APIs drove the timestamp update rate far above what the human-built system assumed, adding pressure to the DB write path. Fix: batch these updates to a one-second interval. The speaker says the assumption that broke was how often each row's timestamp gets updated. ([0:00](https://youtu.be/lMCxVorb9wM?t=0))
- **Current identity models assume the authenticating party is the acting party** — Human auth (password, API key, session) and service or M2M accounts both bind permissions at registration time. This worked because programs are deterministic and code can be reviewed, so the actor and the principal are effectively the same. ([2:47](https://youtu.be/lMCxVorb9wM?t=167))
- **Agents break the determinism assumption that OAuth and code review rely on** — An agent is not a program a human wrote line by line, so its behavior is probabilistic. You cannot be certain it will not do the same thing tomorrow. The speaker contrasts this with Google's security review, which inspects code for deterministic programs. ([5:34](https://youtu.be/lMCxVorb9wM?t=334))
- **Delegation is often missing, so you cannot tell whether an agent or the user acted** — Many systems do not support OAuth on-behalf-of. Teams either give the agent its own client identity that acts for many users, or let the agent act as the user. The speaker calls both lanes wrong, since the agent needs per-user permissions. ([6:52](https://youtu.be/lMCxVorb9wM?t=412))
- **MCP servers should filter tools by the authorizing user's context, not expose everything** — Most MCP servers surface every tool the user or app can reach and let the agent pick. Runtime checks still leave the agent looking at the full surface, which invites wrong tool choices. ([8:13](https://youtu.be/lMCxVorb9wM?t=493))
- **OAuth scopes are too coarse for agents, so least privilege needs attribute, context, and time-bound scopes** — The Gmail example is 'can this client send emails on your behalf'. Wanted instead: which hours the agent can act, which senders it can read, which recipients it can email, and just-in-time elevation. Agents should be least-privileged by default. ([9:36](https://youtu.be/lMCxVorb9wM?t=576))
- **Full action visibility is required: actor, principal, authorizer, grant time, scope, and duration** — For every action, you should be able to say which agent took it, on whose behalf, who authorized it, when, with what scope, and for how long. Without that, the speaker says you are 'praying' the agent behaves. ([11:55](https://youtu.be/lMCxVorb9wM?t=715))

## Techniques
- **Coalesce high-frequency timestamp writes** — Batch per-row last-seen or activity updates to a coarse interval (the speaker uses one second) instead of writing on every request. *When:* Non-critical metadata updates that agent traffic makes far more frequent than human traffic, where they add pressure to the write path.
- **Bind agent identity to principal** — Give each agent its own identity and record the user it acts for on every call, so actor and principal are separate fields. Avoid both a shared client identity and the agent acting as the user. *When:* Agents acting on behalf of multiple users, where per-user permissions must hold.
- **Context-filtered MCP tool surface** — Use the authorizing user's grant to decide which tools an MCP server lists to the agent, so the agent only sees tools it may call. Keep runtime checks as a second layer. *When:* MCP servers used by agents with differing permissions across users or tasks.
- **Least-privilege, time-bound, just-in-time grants** — Scope credentials by attribute (such as recipients or senders), context (such as hours), and time. Let agents request elevated scope at runtime and expire grants. *When:* Agents with write or destructive capabilities, such as email, CRM, or production databases.
- **Full-provenance action audit** — Log actor, principal, authorizer, grant timestamp, granted scope, and expiry for every agent action. *When:* Any production agent that touches third-party data or can change state.

## Numbers
- Latency spiked every 15 minutes because of last-seen timestamp updates ([0:00](https://youtu.be/lMCxVorb9wM?t=0))
- Last-seen update rate rose about 60x as agent traffic hit the APIs over roughly the last 12 months ([0:00](https://youtu.be/lMCxVorb9wM?t=0))
- Speaker has about 10 years of identity work, including building an identity platform at Freshworks used by millions of daily users ([1:22](https://youtu.be/lMCxVorb9wM?t=82))
- Talk runs about 12 minutes 50 seconds ([0:00](https://youtu.be/lMCxVorb9wM?t=0))

## Hot takes
- Runtime checks inside an application do not fix agent authorization, because the agent still sees the full tool surface and will pick the wrong tool.
- Code review and security review of deterministic programs do not carry over to agents, since the agent's behavior is probabilistic.
- Broad OAuth scopes that were acceptable for human-written apps are not acceptable for agents.
- Praying the agent behaves is not a strategy, so deterministic authorization controls are needed.

## Tools mentioned
OAuth, SPIFFE, MCP, Gmail API, Salesforce API, Databricks, HubSpot, Notion

## Relevance to our work
- **agentos** (2/3): AgentOS is a gateway where all agent traffic passes, so per-agent identity, principal binding, and scoped grants fit at the proxy. The talk's audit fields (actor, principal, authorizer, grant, expiry) would extend the Merkle audit log. → *Add actor, principal, authorizer, grant time, and expiry fields to the Govrix Scout audit record, and check whether the proxy can filter tools per principal before forwarding MCP tool lists.*
- **prosharness** (2/3): ProsHarness runs Claude Code under checkpoint and approval flows, and zero-token credential handling is already a goal. Scoped, expiring credentials per run would limit what a rogue run can do. → *Issue each harness run a short-lived credential scoped to its plan step, and log the run as actor with the approving user as principal and authorizer.*
- **general** (1/3): Useful background on agent authorization and least privilege, but mostly a thesis without implementation detail. → *Skim the talk's authorization framing when designing any agent that holds third-party credentials.*
