# NanoClaw: The Lightweight, Secure AI Assistant OpenClaw Should Have Been

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `AQ5uiLyr8bQ` · [watch](https://youtu.be/AQ5uiLyr8bQ) · **date:** 2026-03-02 · **length:** 4:49 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Cisco, Vercel, Docker, Apple, Tailscale, Unsplash, WhatsApp
- **topics:** sandboxing-execution, agent-architecture, claude-code · **tags:** nanoclaw, openclaw, personal-assistant, whatsapp, claude-agent-sdk, containers, self-modifying-agent, security, setup-walkthrough

> Better Stack walkthrough of NanoClaw, a ~500-line personal AI assistant on the Claude Agent SDK with WhatsApp, containers and self-extension by asking the agent; a short overview with a single feature-add demo.

## Summary
The speaker presents NanoClaw as a minimal personal AI assistant of roughly 500 lines, built on the Claude Agent SDK, with WhatsApp as the default channel and container isolation (Docker on Linux, Apple containers on Mac). He contrasts it with OpenClaw, which he says has about 15 channels, more than 45 dependencies and many skills, and runs without a sandbox. He walks through prerequisites (a Claude subscription so the SDK does not burn API tokens, Node above 20, Docker, and a hardened non-root VPS if relevant), then the setup, which is driven by a Claude Code slash command that connects WhatsApp via QR code. The main idea is that the agent is extended by asking it: when it lacked image sending, he asked it to add the feature, reviewed a plan, approved it, restarted the service, and then got a random Unsplash image over WhatsApp. He argues the small codebase gives a smaller attack surface, citing a Cisco figure that 26% of agent skills have vulnerabilities, though he does not show evidence for it. The video is short and light on architecture or config detail, and the speaker admits the setup is rougher than OpenClaw's.

## Key ideas
- **NanoClaw is a deliberately tiny personal assistant (about 500 lines) built on the Claude Agent SDK, versus OpenClaw's many channels, dependencies and skills.** — Default channel is WhatsApp only, web browsing uses Vercel's agent-browser, and there is no configuration file. The claimed advantage is that the code is small enough for an agent or a human to read and change. ([0:00](https://youtu.be/AQ5uiLyr8bQ?t=0))
- **Features are added by asking the agent to build them, not by configuring a feature set.** — The agent replies with a plan of what it will change, the user approves, and the agent edits its own code. Each user's fork therefore diverges toward their own needs instead of carrying unused features. ([2:44](https://youtu.be/AQ5uiLyr8bQ?t=164))
- **The Claude subscription is effectively required because the SDK only supports Claude models by default.** — Using a subscription avoids API-billed token burn during setup and operation. Sonnet is the default model and can be changed. ([1:24](https://youtu.be/AQ5uiLyr8bQ?t=84))
- **Security case rests on smaller surface area and container isolation rather than on any audited claim.** — Containers have a 5-minute timeout, and the speaker says OpenClaw runs unsandboxed with direct host access. He cites a Cisco report that 26% of agent skills have vulnerabilities, but does not show the source in the video. ([3:54](https://youtu.be/AQ5uiLyr8bQ?t=234))
- **Setup is mostly standard server hygiene plus one Claude Code slash command.** — On Linux you need Docker. On a VPS, use a non-root user, disable public SSH and reach the box over Tailscale or an equivalent. You need Node above 20, and the slash command performs the setup and WhatsApp QR pairing. Expect some NPM commands and a few service restarts. ([1:24](https://youtu.be/AQ5uiLyr8bQ?t=84))
- **Demo of self-extension: the agent lacked image sending, and it was added on request.** — After the change and a service restart, the agent fetched random images from Unsplash over several days. This is the only concrete demonstration in the video. ([2:44](https://youtu.be/AQ5uiLyr8bQ?t=164))
- **The speaker admits the setup is rougher and has no dashboard or identity files, and says he was initially unconvinced.** — The trade-off he describes is less out-of-the-box polish for a codebase that grows to match the owner. ([3:00](https://youtu.be/AQ5uiLyr8bQ?t=180))

## Techniques
- **Self-extending assistant via chat-driven code change** — Ask the running agent (via WhatsApp or Claude Code) whether it can do a capability. If it says no, ask it to add the feature. Review the plan it returns, approve it, then restart the service so the change takes effect. The speaker did this for image sending: it added a send-image tool. *When:* When you want a small personal agent whose codebase stays tailored to a single user, and when the feature set is small enough that each addition can be reviewed.
- **Hardened VPS install for a personal agent** — Create and use a non-root user for the install. Disable public SSH access and reach the host only over Tailscale or an equivalent private network. Install Docker and Node.js above 20. Install Claude Code, then run its setup slash command, which pairs WhatsApp by QR code. *When:* When running the assistant on a remote VPS rather than a local machine. The video describes these steps only at a high level; the exact slash command name is not spoken in the transcript.
- **Use a Claude subscription for an SDK-based agent** — Because NanoClaw uses the Claude Agent SDK, which supports only Claude models by default, the speaker runs it under a Claude subscription to avoid API token billing. Sonnet is the default model and can be swapped. *When:* When you want a cheap always-on personal agent on Claude and accept Claude-only models by default.

## Numbers
- NanoClaw is about 500 lines of code. ([0:00](https://youtu.be/AQ5uiLyr8bQ?t=0))
- OpenClaw supports around 15 channels, has more than 45 dependencies and many skills, at time of recording. ([0:00](https://youtu.be/AQ5uiLyr8bQ?t=0))
- Node.js above version 20 is required. ([1:24](https://youtu.be/AQ5uiLyr8bQ?t=84))
- Default model is Sonnet. ([1:24](https://youtu.be/AQ5uiLyr8bQ?t=84))
- Containers have a 5-minute timeout. ([3:54](https://youtu.be/AQ5uiLyr8bQ?t=234))
- A Cisco report (as cited by the speaker, not shown) says 26% of agent skills have vulnerabilities. ([3:54](https://youtu.be/AQ5uiLyr8bQ?t=234))

## Hot takes
- The speaker frames OpenClaw's feature breadth as wasted code; the claim that a bare-bones codebase is inherently more secure is asserted, not demonstrated.
- A Cisco figure (26% of agent skills vulnerable) is cited with no link or context, and the video does not show it.
- Title says NanoClaw is what OpenClaw should have been; the body is a light overview with one feature demo, no architecture or config walkthrough.
- Speaker concedes setup is rougher and lacks OpenClaw's dashboard and identity files, which weakens the 'easier to set up' implication in the framing.
- Auto-captions render the product names as 'Manoclaw' and 'clawed agent SDK'; the notes use NanoClaw and Claude Agent SDK.

## Tools mentioned
NanoClaw, OpenClaw, Claude Agent SDK, Claude Code, Claude Sonnet (default model), Docker, Apple containers, Node.js (above v20), WhatsApp, Tailscale, Vercel agent-browser, Unsplash (image tool demo), Memubot and Nanobot (named as similar assistants)

## Relevance to our work
- **agentos** (1/3): NanoClaw is a small self-hosted agent that isolates execution in containers with a 5-minute timeout. Only loosely related to AgentOS's Crucible sandbox and exec-gate design. → *Read NanoClaw's container lifecycle (per-session container, 5-minute timeout) as a reference point when deciding Crucible's celld timeout and isolation defaults.*
- **prosharness** (1/3): NanoClaw wraps the Claude Agent SDK and is set up through a Claude Code slash command, which overlaps with ProsHarness's wrapping of the Claude Code CLI. The video shows no checkpoint or resume design. → *Compare how NanoClaw drives Claude through the Agent SDK with ProsHarness's CLI wrapper, to see whether the SDK offers session resume that ProsHarness's checkpoint design could use.*
