# You Need To Know This Before Installing OpenClaw

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `M3P0hQMQtq0` · [watch](https://youtu.be/M3P0hQMQtq0) · **date:** 2026-03-02 · **length:** 7:32 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** AI LABS, Cisco, Anthropic, OpenAI, Google Cloud, OpenRouter, Ollama, Discord, WhatsApp
- **topics:** security-guardrails, token-cost-efficiency, sandboxing-execution, skills-self-improvement · **tags:** openclaw, agent-cost, context-growth, heartbeat, prompt-injection, skill-supply-chain, plain-text-credentials, docker-sandbox, budget-alerts, ollama, cisco-skill-scanner

> AI LABS tests the self-hosted agent OpenClaw and finds it costly (token-heavy context, heartbeats), slow as context grows, and risky (plain-text credentials, malicious community skills, prompt injection); it closes with mitigation advice.

## Summary
The AI LABS team installed OpenClaw, a self-hosted AI assistant, and reports a rough setup: WhatsApp kept dropping on 408 errors, so they used Discord instead. Their main cost finding is that OpenClaw resends the full conversation, memory, skills and heartbeat traffic with every query, so a daily cron job was estimated near $128 per month and an hourly email-summary job burned API credits fast. Response time also grew with context, from about 2 to 12 seconds on a fresh session to about 119 seconds once context had built up. On security, they say credentials and sessions sit in plain JSON files, the agent can run shell commands and read files, and Cisco's open-source skill scanner found nine findings (two critical, five high) in one community skill that exfiltrated data. They note OpenClaw's security policy treats prompt injection as out of scope. Their advice is to set API budgets and alerts, lengthen heartbeat intervals, clear sessions, install only necessary and scanned skills, run the agent in Docker or a VM with a separate account, and revoke tokens for unused channels. The video is short, anecdotal from one setup, and ends with pitches for the channel's paid community and super thanks.

## Key ideas
- **OpenClaw's real cost is tokens, not the free software: it resends conversation, memory, skills and channel context on every query, so per-query cost grows with the session.** — Simple daily cron job estimated around $128 per month; an hourly email-summary automation burned through OpenAI credits quickly. Switching to smaller models did not lower cost much, which they read as a usage-pattern problem rather than a model-price problem. ([1:18](https://youtu.be/M3P0hQMQtq0?t=78))
- **Heartbeats and periodic tasks keep spending tokens even when idle.** — The agent sends server heartbeats and runs periodic tasks, so API usage rises even without user chat. Community suggestions: heartbeat interval over two hours and clearing sessions before sleep. ([2:46](https://youtu.be/M3P0hQMQtq0?t=166))
- **Latency grows with context length.** — Their logs showed response time rising from about 2-12 seconds on a fresh session to about 119 seconds after context built up; tool calls add more overhead. ([2:46](https://youtu.be/M3P0hQMQtq0?t=166))
- **Credentials and sessions are stored in plain JSON files readable by anyone with system access.** — Combined with the agent's ability to run shell commands, read files and execute scripts, this is presented as the core security risk, even on a local install. ([4:14](https://youtu.be/M3P0hQMQtq0?t=254))
- **Community skills can be malicious; Cisco's open-source skill scanner found nine findings, two critical and five high, in one skill.** — The skill was described as functionally malware: it instructed the bot to send data via curl to an external server controlled by the skill author. Skills are hosted on a public skill hub (named Claw Hub in the video). ([4:14](https://youtu.be/M3P0hQMQtq0?t=254))
- **Prompt injection is out of scope in OpenClaw's security policy, so the team relies on model-provider guardrails.** — Their OpenAI-backed setup refused to reveal credentials even when told the user was the server owner, but they note clever injections can override this. ([5:41](https://youtu.be/M3P0hQMQtq0?t=341))
- **Isolation and least privilege are the main mitigations: a separate account without sensitive data, Docker or a VM, and revoking unused access.** — Resetting a channel token (for example Discord) revokes the agent's access to that channel. ([5:41](https://youtu.be/M3P0hQMQtq0?t=341))

## Techniques
- **Hard budget and alerts on the model API key** — Set spend budgets and alerts in the provider console (they name OpenAI and Google Cloud) for whatever key the agent uses, so runaway automations get caught early. *When:* Any always-on agent or scheduled job that calls a paid model API.
- **Reduce idle token burn** — Raise the heartbeat interval above two hours and clear the session before the agent sleeps, so old conversation is not resent with every query. *When:* Long-running personal agents with heartbeats or cron-style tasks, where context keeps growing.
- **Vet community skills before install** — Run the open-source Cisco skill scanner on any third-party skill before installing it, install only skills verified by the community, and block skills that touch passwords or sensitive systems unless needed. *When:* Adding skills or plugins from a public registry to an agent that can run shell commands.
- **Sandbox the agent** — Run it in a Docker container (isolated, restricted from other system resources) or in a VM that contains only the agent setup; give it a separate account with no sensitive data. *When:* Any agent that can execute commands or read local files.
- **Least-privilege channel tokens** — Remove access to unused integrations, and reset the bot token (e.g. Discord) to revoke the agent's access when you stop using a channel. *When:* Agents connected to chat channels or other services you no longer use.
- **Prefer providers with built-in guardrails, with caution** — Choose hosted models from providers with their own guardrails (they cite OpenAI and Anthropic) over unguarded setups, and do not treat this as a complete defense against injection. *When:* Choosing a model backend for an agent that handles credentials or untrusted content.

## Numbers
- Simple daily cron job estimated at around $128 per month in OpenClaw token costs ([1:18](https://youtu.be/M3P0hQMQtq0?t=78))
- Response time grows from about 2-12 seconds on a fresh session to about 119 seconds with built-up context (from their logs) ([2:46](https://youtu.be/M3P0hQMQtq0?t=166))
- Cisco's scanner found nine security findings (two critical, five high) in a single community skill ([4:14](https://youtu.be/M3P0hQMQtq0?t=254))
- OpenClaw was rebranded from Claudebot to Maltbot to OpenClaw within about three days ([0:00](https://youtu.be/M3P0hQMQtq0?t=0))

## Hot takes
- OpenClaw is described as a security nightmare; the cost problem is in how the product uses context, not the model choice (single-setup observation).
- Models from OpenAI and Anthropic are recommended partly because their built-in guardrails refuse credential leaks, but the video admits clever injections can override them.
- Quality is capped by thin evidence: one anecdotal test setup, a single cited malicious skill, and repeated pitches for the channel's paid community and super thanks.

## Tools mentioned
OpenClaw, Claude (former Claudebot name), OpenAI API, Anthropic models, OpenRouter, Ollama, Docker, Cisco open-source skill scanner, Discord, WhatsApp

## Relevance to our work
- **agentos** (2/3): Govrix already has PII and prompt-injection scanning, and the video's scanner-gated skills and cost alerts map to AgentOS budgets and exec-gate guardrails. → *Add a pre-install scan gate for community skills in the SkillForge/registry path, and check whether Govrix budget alerts fire on context-growth spikes, not only on total spend.*
- **prosharness** (2/3): ProsHarness has zero-token credential handling, and the video shows plain-JSON credential storage and unscoped channel tokens as the main risk. → *Audit where ProsHarness stores API keys and channel tokens, move them out of plain files, and make revoking a single integration one step.*
