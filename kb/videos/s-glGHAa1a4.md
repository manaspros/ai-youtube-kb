# An AI Future Without the Lock-In — Remy Guercio, Tailscale

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `s-glGHAa1a4` · [watch](https://youtu.be/s-glGHAa1a4) · **date:** 2026-10-11 · **length:** 19:38 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Remy Guercio · **orgs:** Tailscale
- **topics:** infra-cost-scaling, governance-compliance, mcp-and-tools · **tags:** AI gateway, vendor lock-in, ROI, token cost, MCP gateway, identity-aware access, Tailscale, Aperture, TSNet, WireGuard, agent observability, sandboxes, BYO interface

> Tailscale's Remy Guercio argues for "ROI maxing" over token maxing: keep choice at every AI layer through an identity-aware AI gateway (Aperture) to avoid lock-in. Mostly a product pitch.

## Summary
Remy Guercio, who works on Tailscale's AI gateway Aperture, reviews the last year of "token maxing" (large context windows, agentic coding, expensive usage, long sessions that never clear context) and calls the next phase "ROI maxing." He splits an internal AI deployment into four layers: LLMs, data connectors (MCP, CLI or APIs), the interface (chat, IDE, Slack, phone), and the sandbox where agents run. His argument is that companies should keep the ability to choose at each layer instead of consolidating on one vendor, which he presents as the wrong reaction to a spending panic. He says an AI gateway sitting between agents and all their endpoints gives control, cost visibility and per-identity access, and that Aperture gets caller identity from Tailscale's WireGuard-based mesh, including synced Entra/Okta groups. He also says a gateway's logs help diagnose what an agent did, even for an individual. Pass-through auth for third-party UIs and a sandbox orchestration layer are announced as coming soon, with no dates. The talk gives no benchmarks or prices, and most of it promotes one product, though the layered framing applies to any gateway.

## Key ideas
- **Last year was 'token maxing': huge context windows and agentic coding made expensive, unbounded usage normal.** — The speaker says the unlimited-AI-budget era is ending and that token use is expensive by default, which encourages wasted tokens. ([1:29](https://youtu.be/s-glGHAa1a4?t=89))
- **Long sessions that never clear context keep the prompt cache hot and burn tokens.** — From gateway data he reports sessions of hundreds or thousands of messages, with tens of millions of tokens where the cache stayed maxed out the whole time. ([2:27](https://youtu.be/s-glGHAa1a4?t=147))
- **Consolidating on one or two vendors is the common panic response to AI spend, and it is a bad one.** — He says he hears it from hundreds of folks over six months, since it creates lock-in and makes AI usage harder to expand across the company. ([3:47](https://youtu.be/s-glGHAa1a4?t=227))
- **Reframe the goal as ROI maxing: prove value and widen access, not just cut costs.** — Maximize choice so that different teams can use the right model, connector, interface and sandbox for their work. ([5:07](https://youtu.be/s-glGHAa1a4?t=307))
- **An internal AI deployment has four separable layers: LLMs, data connectors, interfaces and sandboxes.** — Data connectors can be MCP, but also CLI, APIs or just reading a file. The interface may be a chat UI, an IDE, Slack or a phone. Choice at each layer can differ by team, e.g. a marketing team working entirely in Slack. ([6:11](https://youtu.be/s-glGHAa1a4?t=371))
- **An AI gateway sits between agents or interfaces and every endpoint, so it can control and monitor them.** — Endpoints include LLM providers, MCP servers and plain APIs. The uses are security, cost, and understanding what an agent is doing. ([7:33](https://youtu.be/s-glGHAa1a4?t=453))
- **Identity-aware access removes per-tool key sprawl.** — Aperture is built on Tailscale, a WireGuard mesh where every connection carries the identity of a user or a tagged machine. Entra and Okta groups can be synced in. Users connect once and the gateway knows who they are and which models and budgets they get. ([9:57](https://youtu.be/s-glGHAa1a4?t=597))
- **The gateway also acts as an MCP gateway and re-exposes standard APIs as MCP servers, with per-group access.** — Admins choose the allowed MCP servers and set access by group, for example read-only versus write access to GitHub. Authentication happens at the gateway, so switching tools does not mean re-authenticating everywhere. ([12:39](https://youtu.be/s-glGHAa1a4?t=759))
- **Announced but not yet shipped: pass-through auth for third-party UIs and a sandbox orchestration layer.** — Pass-through auth is meant to keep user identity when a UI such as Open WebUI sits in front of the gateway. Sandbox orchestration would give one place to route environments. Neither has a date in the talk. ([15:16](https://youtu.be/s-glGHAa1a4?t=916))
- **Gateway logs help diagnose agents even for individuals.** — He describes people running agents like OpenClaw on a tailnet who need to find out what the agent did. Cheaper models often fail to stop themselves but are good at analyzing their own failures after the fact. ([17:58](https://youtu.be/s-glGHAa1a4?t=1078))

## Techniques
- **Decompose internal AI into four swappable layers** — Treat LLM provider, data connector (MCP, CLI, API or file read), interface (chat, IDE, Slack, voice) and sandbox as separate choices. Pick a component per layer per team instead of one stack for everyone. *When:* Planning an org-wide AI rollout where teams need different tools and where a single vendor's stack would limit spend or access.
- **Route all LLM, MCP and API traffic through one gateway** — Point every agent, IDE and custom app at one gateway endpoint. Store the upstream provider keys only at the gateway, and configure models, budgets and MCP servers there, not in each client. *When:* Several providers or agent tools are in use, or when key sprawl and per-tool re-authentication slow down trying new tools.
- **Per-identity budgets and model tiers** — Attach budgets to identities: unlimited or generous on a cheap model, a narrow budget on a frontier model. Scope access by group, for example GitHub read-only for one engineering sub-team and write access for another. *When:* Controlling spend on frontier models while keeping cheap models open to everyone.
- **Give each agent its own identity** — Tag a machine or service, such as a PR review bot, so each instance gets its own node identity. Use the human user's identity for personal sessions, and sync groups from the IdP. *When:* Auditing which agent or person made each call, and applying different permissions to bots and humans.
- **Diagnose agent runs by feeding gateway logs back to the model** — Export the agent's gateway logs and ask the model what went wrong. The speaker reports that models are weak at stopping a spiral but strong at post-hoc analysis. *When:* An agent spiraled, looped or did something unexpected and you need the cause.
- **Build custom interfaces on top of the gateway APIs** — Use the gateway's chat APIs to build Slack bots, voice interfaces or other custom UIs. Connectors stay configured in the gateway, not in each UI. *When:* A team wants agents to work in their own tools instead of a vendor chat UI.

## Numbers
- The speaker has spoken to hundreds of folks about AI spend over the last six months. ([3:47](https://youtu.be/s-glGHAa1a4?t=227))
- Some sessions run to hundreds or thousands of messages with the cache maxed out, adding up to tens of millions of tokens per session. ([2:27](https://youtu.be/s-glGHAa1a4?t=147))
- The talk gives no benchmarks, latencies, prices or adoption figures. ([11:21](https://youtu.be/s-glGHAa1a4?t=681))

## Hot takes
- Mostly a vendor pitch for Tailscale Aperture. The layered framing and gateway ideas apply to any gateway, but the identity-from-mesh claim is product-specific.
- Consolidating on one vendor under cost pressure is a bad response because it creates lock-in.
- Cheaper models are poor at stopping themselves but good at post-hoc analysis (anecdotal, from gateway usage, not measured).
- Features announced as coming soon (pass-through auth, sandbox orchestration) have no dates.

## Tools mentioned
Tailscale, Aperture (Tailscale AI gateway), WireGuard, TSNet, Entra, Okta, Anthropic API, OpenAI API, Vercel AI gateway, AWS Bedrock, Codex, Claude Code, Cursor, GLM 5.2, MCP, OpenClaw, Open WebUI

## Relevance to our work
- **agentos** (2/3): Govrix Scout (L1) is also an AI gateway with budgets, PII scanning, routing and an audit log, so the identity-per-caller and per-model budget-tier ideas map directly onto it. → *Check whether Govrix Scout's audit log and budget config key on caller identity (user, bot or group) and per-model tiers, the way Aperture does, and add those fields if they are missing.*
- **prosharness** (1/3): ProsHarness runs long Claude Code jobs and could tag each run with an identity and budget, but the talk is about enterprise gateways, not harness design.
