# NVIDIA NemoClaw First Look: Secure AI or Just Over-Engineered?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `5v0RJkqjU8c` · [watch](https://youtu.be/5v0RJkqjU8c) · **date:** 2026-04-02 · **length:** 8:10 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andrus · **orgs:** NVIDIA, Better Stack
- **topics:** sandboxing-execution, security-guardrails, agent-architecture · **tags:** nemoclaw, openclaw, nvidia-openshell, nemotron, nvidia-brev, sandbox, egress-policy, human-in-the-loop-approval, telegram-bot, agent-gateway, cron

> Better Stack's hands-on first look at NVIDIA's NemoClaw, an OpenClaw agent wrapped in the OpenShell sandbox; the setup is fragile and per-request approvals make autonomous tasks tedious.

## Summary
The host reports on NVIDIA's NemoClaw, an open-source stack that moves the OpenClaw agent into NVIDIA OpenShell, a sandbox where a declarative policy governs file access, network requests and inference calls, and blocked actions wait for manual approval in a terminal TUI. He deploys it on NVIDIA Brev, notes that the default install script failed to install OpenShell (manual download from NVIDIA's GitHub worked as a fallback), and walks through the setup prompts: agent name, NVIDIA API key, inference model (he picks Nemotron), and a Telegram bot token. Starting the agent, the gateway and the Telegram bridge were fragile, with stale gateway processes, a Telegram 255 error and replies taking up to about two minutes. A test task (a cron job sending Hacker News articles every three minutes) needed a manual approval for every outbound request plus repeated prompts to retry, and took about 30 minutes of babysitting to work. His verdict is that the security layer is too strict for autonomous operation and the stack feels unstable and hard to use, though it is very new. This is one developer's single-session observation, not a benchmark.

## Key ideas
- **NemoClaw is NVIDIA's open-source stack that runs the OpenClaw agent inside the NVIDIA OpenShell sandbox, positioned as a secure enterprise-grade wrapper for autonomous agents.** — The speaker frames it as a safety sandbox that monitors each action in real time, since base OpenClaw lacks security oversight for sensitive workflows. The claim is NVIDIA's; the video tests it. ([0:00](https://youtu.be/5v0RJkqjU8c?t=0))
- **The architecture is a blueprint (a Python orchestrator script) managing the agent lifecycle, with a declarative policy governing every file access, network request and inference call.** — Unauthorized network destinations or restricted filesystem paths are blocked and flagged for manual approval in the terminal. The speaker describes this as a managed infrastructure layer beneath the agent. ([1:11](https://youtu.be/5v0RJkqjU8c?t=71))
- **The default install script failed for the speaker, so the install needed a manual workaround.** — The default script failed to install OpenShell. The fallback was to download OpenShell manually from NVIDIA's GitHub repository. ([2:20](https://youtu.be/5v0RJkqjU8c?t=140))
- **Egress approval is the central friction point: each outbound request from a scheduled task needs a human to approve it in the OpenShell manager, and the agent often has to be told to retry.** — A cron job polling Hacker News every three minutes required back-and-forth approvals per request. The speaker says this kneecaps autonomy because the security layer is too strict, and that complex workflows would need constant babysitting. ([5:29](https://youtu.be/5v0RJkqjU8c?t=329))
- **The stack was fragile to operate: the gateway needed manual kills, the Telegram bridge was unstable, and inference was slow.** — Stale gateway processes had to be killed before a new one could start. Telegram sometimes returned error 255. Replies took up to about two minutes, which the speaker attributes possibly to the Nemotron model choice. ([4:25](https://youtu.be/5v0RJkqjU8c?t=265))
- **The speaker's verdict is that NemoClaw is too new and unstable for production, and its policy controls are too limited.** — NVIDIA's policy commands are limited and do not give a sophisticated way to write custom rules. He thinks it may become production-ready later but says it currently feels unstable and hard to use. ([6:24](https://youtu.be/5v0RJkqjU8c?t=384))

## Techniques
- **Deploy NemoClaw on a Brev GPU instance** — From NVIDIA's NemoClaw page click Try Now to reach Brev, which ships with NVIDIA drivers, CUDA and Docker preinstalled; new accounts get $2 of free credits. Connect with `brev shell`, then run NVIDIA's NemoClaw install script. If it fails to install OpenShell, download OpenShell manually from NVIDIA's GitHub repository. *When:* First-time evaluation of NemoClaw on rented GPU hardware without local setup.
- **Answer the NemoClaw installer prompts** — Agent name (default 'My Assistant', or any name). NVIDIA API key (the speaker warns the key must be set up for this purpose or NemoClaw may not work properly). Inference model selection (he chose Nemotron, which NVIDIA recommends). Telegram bot token is added after install to connect the agent to Telegram. *When:* Running the installer for the first time.
- **Start the agent and approve pending egress requests** — Run `nemoclaw start` and wait for all green check marks. Open the OpenShell manager, a TUI that lists pending network requests; press A to approve each one, then return to the overview. *When:* Bringing the agent up, and whenever it stalls on a blocked outbound call.
- **Recover a stuck Telegram gateway** — Connect to the agent and launch the gateway. If a new gateway will not start, kill the previous gateway process manually. For Telegram error 255, exit the OpenClaw shell, kill leftover Telegram bridge processes in the deployment container, then re-enter the Telegram bot token through the OpenClaw `configure` wizard. *When:* Telegram chat with the agent fails to start or returns error 255.
- **Watch OpenClaw logs during autonomous tasks** — For scheduled work, the speaker monitored OpenClaw logs while the agent retried requests, prompting it again after each approval until the cron job produced output. *When:* Debugging a multi-step or scheduled task under the NemoClaw policy layer.

## Numbers
- Brev gives new accounts $2 of free credits, enough for a first test deployment. ([2:20](https://youtu.be/5v0RJkqjU8c?t=140))
- Installation takes a few minutes. ([3:22](https://youtu.be/5v0RJkqjU8c?t=202))
- Telegram replies sometimes took up to about two minutes with Nemotron. ([4:25](https://youtu.be/5v0RJkqjU8c?t=265))
- Test cron job polled Hacker News every three minutes; each outbound request needed manual approval. ([5:29](https://youtu.be/5v0RJkqjU8c?t=329))
- About half an hour of babysitting to reach a working state for the test task. ([6:24](https://youtu.be/5v0RJkqjU8c?t=384))
- Video length 8:10, single-run hands-on test with no benchmarks. ([0:00](https://youtu.be/5v0RJkqjU8c?t=0))

## Hot takes
- Per-request manual approval of outbound network calls makes the NemoClaw security layer too strict for autonomous operation.
- NemoClaw feels very unstable and very hard to use at this stage.
- NVIDIA's claim that OpenClaw is 'the next ChatGPT' is hype; the speaker tests whether NemoClaw's security story holds up.
- NVIDIA's policy commands are too limited for custom, tailored security rules.

## Tools mentioned
NemoClaw (NVIDIA, install script plus `nemoclaw start`), NVIDIA OpenShell (sandbox; OpenShell manager TUI for approving requests), OpenClaw (agent; `configure` wizard), Nemotron (NVIDIA inference model), NVIDIA Brev (cloud GPU platform; `brev shell`), Docker, CUDA, Telegram (bot token bridge)

## Relevance to our work
- **agentos** (2/3): Crucible has an exec-gate guardrail and Govrix Scout enforces budgets and policy at a proxy. NemoClaw shows the same pattern (declarative policy at a layer beneath the agent) and the cost of per-request human approval when it is too strict. → *Measure how many approval prompts a typical scheduled agent task would trigger under Crucible's exec-gate, and design allow-policies for routine egress so autonomy does not stall on per-call approval.*
- **prosharness** (2/3): ProsHarness plans phone-driven approvals and loops. NemoClaw's experience (a cron task blocked on approvals for each request) is a direct cautionary case for the approval UX. → *Design ProsHarness approvals as batched or pre-declared allowlists (approve a host or action class once with an expiry) rather than per-request prompts, so scheduled runs do not stall.*
