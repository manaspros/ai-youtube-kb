# A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `adfw3xJBx1o` · [watch](https://youtu.be/adfw3xJBx1o) · **date:** 2026-10-21 · **length:** 15:30 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Felippe Felisola Caso, Francesco Galletta · **orgs:** Monzo
- **topics:** enterprise-adoption, mcp-and-tools, coding-agents, sandboxing-execution · **tags:** monzo, agent-chip, slack-bot, mcp-gateway, sandbox, egress-control, incident-response, on-call, data-quality, proactive-agents, human-in-the-loop, provider-agnostic, linear, github, building-blocks

> Monzo's engineers describe Agent Chip, an in-house coding agent that began as a viral Slack emoji trigger and grew into a sandboxed, MCP-gated platform building block.

## Summary
Felippe Felisola Caso and Francesco Galletta of Monzo describe Agent Chip, the bank's internal coding agent, which started as a Slack feature where reacting to a message with an emoji sent it as a prompt. It grew into an always-available teammate that answers questions, reviews code, takes Linear tickets, and works in incident channels. The speakers credit Monzo's existing platform capabilities (alerting, monitoring, third-party integrations, staging, queuing, deployment, database abstractions) as the real reason it shipped fast. Their first building block was an MCP gateway in front of internal services and knowledge sources, which gives deterministic control over what agents can see and centralizes authn/authz. Agent Chip runs as remote agents inside an isolated namespace of sandbox pods, where the agent image defines its tools, a proxy controls egress, and the agent itself is the innermost, least-trusted layer. Non-specialists use it to draft changes that are tested in staging before an engineer reviews and deploys them. The talk is a company showcase: it gives architecture and outcomes but few implementation details or independent measurements.

## Key ideas
- **Monzo's scale is the context: 3,000+ backend services, about 13,000 data warehouse models, and many ML predictors maintained by engineering teams.** — Explains why an internal coding agent is worth building: the surface area for changes is very large in a regulated bank. ([0:08](https://youtu.be/adfw3xJBx1o?t=8))
- **Agent Chip went viral from a small UX trick: reacting to a Slack message with an emoji sends that message to the agent as a prompt. It then became an always-available Slack teammate.** — Works as a coworker that answers questions, explains architecture, does code review (approves with a short comment), and takes assigned Linear tickets. ([1:32](https://youtu.be/adfw3xJBx1o?t=92))
- **The speakers argue the value comes from the platform under the agent, not the model. Monzo already had alerting, monitoring, third-party integrations, staging, queues, easy deploys and database abstractions.** — They describe their 'LLMs' as lots of little multipliers rather than one model. ([4:18](https://youtu.be/adfw3xJBx1o?t=258))
- **Monzo started with an MCP gateway for local coding agents before remote agents existed. It exposes internal services and knowledge sources through one server, so the team chooses what agents can reach.** — The gateway also handles authentication and authorization for many different agents, which the speakers say matters more as agents get more context. ([4:18](https://youtu.be/adfw3xJBx1o?t=258))
- **The orchestration system runs remote agents in sandboxes and is kept separate from production. The gateway box is deterministic; the agent box is where non-determinism lives.** — The speakers frame the design as containing non-determinism inside layers, so agents can run loose while production stays controlled. ([5:37](https://youtu.be/adfw3xJBx1o?t=337))
- **Agents run in an isolated namespace of pods. The agent image defines the exact CLIs, environment and auth; a proxy allows only chosen egress (for example specific repositories).** — Every outbound connection is a deliberate grant, so the blast radius of a misbehaving agent is limited by design. ([6:49](https://youtu.be/adfw3xJBx1o?t=409))
- **In incident mode the agent joins the incident channel, pulls logs, traces, service code via MCP and tests hypotheses. The team deliberately keeps its chatter low and lets humans control how far it goes.** — Other uses include 'ask channels' for squad-to-squad questions (drafts answers, can close the ticket itself or ask for context), and on-call triage of data quality alerts. ([10:04](https://youtu.be/adfw3xJBx1o?t=604))
- **A proactive variant watches backend changes and predicts their impact on data before the next batch run, so some data failures are prevented rather than investigated.** — Reactive on-call investigates failures after they happen; the proactive version works on the change itself. ([11:09](https://youtu.be/adfw3xJBx1o?t=669))
- **Non-specialists (product, business users) can get a tested draft change from the agent in staging, and only then does an engineer review and deploy it, so review rigor stays the same.** — Speakers say this widens who can contribute without lowering the bar for shipping. ([12:07](https://youtu.be/adfw3xJBx1o?t=727))
- **The agent is provider-agnostic: the model in the agent box can be swapped, and models are chosen per task.** — They say they are not tied to any one provider and can keep Agent Chip valuable even if they stopped developing it today. ([13:28](https://youtu.be/adfw3xJBx1o?t=808))

## Techniques
- **Gateway-first MCP layer for internal tools** — Put internal services and knowledge sources behind a single MCP server you build. Choose which tools and data are exposed (deterministic), and handle authn/authz for each agent there rather than in each tool. *When:* Several agents (local IDE agents, remote agents, chat bots) need the same internal systems, and access must be controlled and audited.
- **Isolated sandbox namespace for remote agents** — Run each agent in its own pod inside an isolated namespace. The agent image declares the exact CLIs, environment and credentials it may use. Put a proxy in front of all outbound traffic and allow only the destinations you choose (e.g. specific repos). Keep the orchestrator outside and have it read results from the sandbox. *When:* Agents must run code with broad freedom but production and regulated data must stay under control, such as in a bank.
- **Separate orchestrator from execution** — A separate orchestration system triggers agents, gives them strict tools and permissions, and collects their output. The agent itself has no direct path to production systems. *When:* You want to add triggers (Slack, tickets, alerts) and reuse the same agent runtime across them.
- **Emoji-reaction prompt trigger in chat** — Let a reaction emoji on any chat message send that message as a prompt to the agent. The agent then replies in the thread. *When:* You want a very low-friction entry point that adoption can spread through (the speakers say it went viral).
- **Low-signal incident mode** — When an incident is detected, the agent joins the incident channel and investigates (logs, traces, linked code via MCP), posting only key findings. Humans decide how much of the investigation it should run. *When:* Incidents where noisy agent output would slow humans down.
- **Proactive impact checks on backend changes** — Monitor incoming backend changes and predict their effect on downstream data before the next batch job runs, rather than only investigating failed runs. *When:* Batch data pipelines where failures are costly and the upstream change is visible in advance.

## Numbers
- Over 3,000 backend services maintained by engineering teams ([0:08](https://youtu.be/adfw3xJBx1o?t=8))
- About 13,000 data warehouse models ([0:08](https://youtu.be/adfw3xJBx1o?t=8))
- Agent Chip is involved in more than 10% of all merged PRs across tech (data, ML, backend, app) ([2:48](https://youtu.be/adfw3xJBx1o?t=168))
- More than 1,800 agent tasks run per day ([2:48](https://youtu.be/adfw3xJBx1o?t=168))

## Hot takes
- Company showcase with little implementation detail: no model names, prompts, eval method, cost, or failure data are given.
- The '10% of merged PRs' and '1,800 tasks per day' figures are unverified and not defined (what counts as an agent-involved PR?).
- The speakers say the value is the platform, not the LLM, which is a useful point, but it is also an argument that most of the success is not transferable without a similar platform.
- Their 'high signal' incident design (limit chatter, humans set scope) is a more practical lesson than the viral Slack story.

## Tools mentioned
Agent Chip (Monzo's in-house coding agent), Slack, GitHub, Linear, MCP (internal MCP gateway server)

## Relevance to our work
- **agentos** (2/3): Single MCP gateway in front of internal tools with central authn/authz for many agents mirrors the AgentOS proxy-with-pillars idea, applied to tools rather than model traffic. → *Compare Monzo's MCP gateway (central exposure choice plus per-agent auth) with AgentOS's proxy design and decide whether tool access should be a fourth pillar next to budgets and PII scanning.*
- **prosharness** (1/3): Human-controlled, low-signal agent behavior and approval gates fit ProsHarness's phone-driven approvals loosely; no harness or checkpoint details are given. → *Consider a ProsHarness rule where an agent in an incident-like run posts only findings and asks for approval before widening its scope.*
