# YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `OE_lLNCNfQo` · [watch](https://youtu.be/OE_lLNCNfQo) · **date:** 2026-10-04 · **length:** 11:35 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Rowan Christmas · **orgs:** Docker, Anthropic, CrowdStrike
- **topics:** sandboxing-execution, security-guardrails, governance-compliance · **tags:** micro-vm, docker-sbx, claude-code, secrets-placeholder, egress-control, default-deny, agent-identity, cedar, yolo-mode, prompt-injection-self-test, read-only-mounts

> Docker's product manager argues coding agents need micro-VM sandboxes with secret placeholders and default-deny egress, and shows a self-test where Claude Code found his bank data. Mostly a product pitch.

## Summary
The speaker, a Docker product manager, says developers trust coding harnesses like Claude Code too much. To test this, he ran Claude Code on his own Mac and asked it to find his browser history and bank data, and it did, within five prompts. Asking directly was refused, but framing the request as security research got past the refusal. He argues that prompts like "please don't do nefarious things" are not a security control. His proposed fix is Docker's SBX product, which runs an agent in a micro-VM with its own kernel, an isolated filesystem, and no visibility into host secrets. Real credentials are swapped in at the network layer from placeholders, egress is blocked by default, and there is an audit trail. Repos can be mounted read-only so the agent can read related code without committing to it. He says agent-level identity and delegation chains with Cedar policies are coming, and that L7 and per-repo controls are on the roadmap. The talk is short and mostly a pitch, but the self-test and the placeholder-secret design are concrete.

## Key ideas
- **Self-test: the agent exposed the speaker's personal data** — He ran Claude Code (desktop app) on his own Mac. It found browser history, bank account data and Zelle info in about five prompts. A direct request got a warning, but saying he was researching security got it to help. The speaker's point is that the harness is not a reliable safety layer. ([1:39](https://youtu.be/OE_lLNCNfQo?t=99))
- **Please-be-safe prompts are not security** — He says that asking the model not to do nefarious things in the system prompt is the current level of security. Enforcement has to sit outside the model. ([3:05](https://youtu.be/OE_lLNCNfQo?t=185))
- **Put the boundary at the micro-VM, not the host or the prompt** — A micro-VM runs its own kernel and isolates the filesystem. Agents find their way around controls on the host, so once the agent reaches the host the protection is already lost. ([3:05](https://youtu.be/OE_lLNCNfQo?t=185))
- **Secrets never enter the sandbox** — The sandbox sends a placeholder. The host proxy swaps in the real credential on the outgoing network request, so the agent never holds the secret and cannot leak it. ([3:05](https://youtu.be/OE_lLNCNfQo?t=185))
- **Default-deny egress and telemetry blocking** — In his demo, a blocked site was refused by default. He also says Claude Code sends telemetry to an outside service, and that the sandbox blocks this. Egress rules are configurable. ([5:35](https://youtu.be/OE_lLNCNfQo?t=335))
- **Mount related repos read-only** — The agent can read other repos for context but cannot make commits there. This gives a guarantee about what the agent changed, not just what it says it changed. ([9:54](https://youtu.be/OE_lLNCNfQo?t=594))
- **Identity and delegation chains are planned, not shipped** — The goal is to trace which human authorized which agent action, and to write Cedar policies that reduce permissions as things happen. He presents this as upcoming work. L7 network rules and per-repo filesystem rules are also on the roadmap. ([6:59](https://youtu.be/OE_lLNCNfQo?t=419))

## Techniques
- **Run agents in a micro-VM with bypass permissions on** — Start the agent in a per-project VM (e.g. `sbx run claude`). The VM gets its own kernel and filesystem, so the agent's broad permissions only affect the VM. The speaker says the command also works for shells, Codex, Python jobs and web servers. *When:* Use it when you want to run an agent in YOLO or bypass-permissions mode on a machine that holds personal or client data.
- **Placeholder secrets swapped at the network boundary** — Give the sandbox a placeholder token. A host-side proxy replaces it with the real credential on outgoing requests, so the agent never sees the secret. *When:* Use it whenever an agent needs API credentials and you do not want them in its context, env vars or logs.
- **Default-deny egress with an allowlist** — Block all outbound network access by default and allow only named hosts. Log each blocked request. *When:* Use it for any agent that can browse, fetch URLs or call tools that make network calls.
- **Read-only mounts of context repos** — Mount related repositories read-only so the agent has context but cannot write to them. *When:* Use it for multi-repo work where the agent needs to read another codebase but should not change it.
- **Self red-teaming with real personal data** — Point the agent at your own sensitive data and see how many prompts it takes to get it. The speaker used five prompts and a security-research framing. *When:* Use it as a cheap check on how your agent setup behaves before you trust it with real work.

## Numbers
- Claude Code found browser history, bank data and Zelle details in about five prompts, with a security-research framing ([1:39](https://youtu.be/OE_lLNCNfQo?t=99))
- Speaker's CrowdStrike security assessment of his machine scored 9 out of 10 ([1:39](https://youtu.be/OE_lLNCNfQo?t=99))
- Running in the sandbox added about seven extra keystrokes ([5:35](https://youtu.be/OE_lLNCNfQo?t=335))

## Hot takes
- Please-be-safe prompts are the current level of agent security
- Once an agent reaches the host machine, it is too late, so the boundary must be the micro-VM
- A coding harness's built-in safety checks are not a reliable security layer

## Tools mentioned
Docker SBX, Claude Code, Claude Desktop, Codex, CrowdStrike, Cedar, Datadog

## Relevance to our work
- **agentos** (2/3): AgentOS Crucible (L2C) has sandboxed code execution and exec-gate guardrails. The talk offers a VM boundary with placeholder secrets and default-deny egress as a comparison point. → *Compare Crucible's celld sandbox boundary with a micro-VM. Test whether a placeholder-secret swap at the egress proxy can replace secrets inside the exec path, and whether default-deny egress is enforced by default.*
- **prosharness** (2/3): ProsHarness wraps Claude Code and handles credentials with zero-token handling. Running long loops in a VM with placeholder secrets could strengthen that. → *Check whether ProsHarness loops and schedules can run inside a micro-VM where credentials are injected at egress as placeholders, so Claude Code never holds the real keys.*
- **general** (2/3): The self-test result is a concrete warning that agent refusals can be bypassed with framing. It is a useful reminder for any agent with access to personal or client data. → *Add a short red-team step to agent setup: point the agent at a dummy sensitive dataset and try framing-based extraction before giving it real access.*
