# Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `VaS2h-dY1-4` · [watch](https://youtu.be/VaS2h-dY1-4) · **date:** 2026-06-18 · **length:** 19:00 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Onur Solmaz · **orgs:** OpenClaw, TextCortex, Zed
- **topics:** multi-agent, mcp-and-tools, sandboxing-execution, pr-code-review · **tags:** ACP, acpx, OpenClaw, Codex, Claude Code, Discord, Slack, Kubernetes, Helm, Go operator, PR triage, workflow engine, disposable agents, per-task pods, agent interoperability, Ralph loop

> An OpenClaw maintainer shows acpx, a CLI and workflow engine over the Agent Client Protocol (ACP), used to automate PR triage and to run disposable per-task agents on Kubernetes.

## Summary
Onur Solmaz, a founding engineer at TextCortex and an OpenClaw maintainer, describes how he moved from driving Codex through Discord to a general ACP tool called acpx. ACP standardizes how a client talks to a coding agent, while MCP gives tools to the model. OpenClaw faces a flood of PRs (300 to 500 open per day, by his account), so he automates the mechanical PR work: checking intent, judging the implementation, resolving conflicts, and getting CI green before a human looks. The workflow mixes scripted steps with agent loops, and the agents return JSON so the workflow can branch. He allows agent review loops only for shallow fixes and sends fundamental refactors to a human. For enterprise use, he argues each task should get its own disposable agent, which needs Kubernetes, a harness, and state sync; his day-job open-source Go operator does this with a full pod per agent. The talk is a practitioner account with little measured data, and it includes some self-promotion of his project.

## Key ideas
- **ACP and MCP solve different problems** — MCP gives tools to the model. ACP (Agent Client Protocol) standardizes how a client talks to an agent, so one client integration can serve many agents. He chose ACP because Zed had built adapters for Codex and Claude Code when he needed them, and Google had none yet. ([5:09](https://youtu.be/VaS2h-dY1-4?t=309))
- **acpx started as a CLI to call any agent from the command line** — He began with a CLI to call agents from the shell for OpenClaw's own features. It grew into a broader ACP tool, and he built it by driving Codex through a Discord channel bound to an ACP session. ([6:36](https://youtu.be/VaS2h-dY1-4?t=396))
- **The bottleneck is absorbing stakeholder demand, not writing code** — Tens of thousands of people want features, and PRs arrive in volume. The hard problem is balancing them without accumulating AI slop. He treats each discarded or flagged PR as feedback data to categorize. ([6:36](https://youtu.be/VaS2h-dY1-4?t=396))
- **Automate the mechanical PR steps before a human sees the PR** — Intent check, implementation judgment, conflict resolution, review feedback, and CI are handled by a workflow first. He says the human should see only what is left. He also has the agent explain the PR, since AI-written descriptions often hide what the change does. ([8:11](https://youtu.be/VaS2h-dY1-4?t=491))
- **Mix scripted steps with agent steps and require structured output** — The workflow reproduces the bug in code, then has an agent judge the refactor and run a review loop. He makes agents emit JSON so the workflow engine can branch on the result. He describes this as standard operating procedures for agents. ([10:41](https://youtu.be/VaS2h-dY1-4?t=641))
- **Agent loops are acceptable only for shallow fixes** — Repeated agent review and refactor loops (he calls them Ralph loops) are fine for superficial bugs. They become slop when the agent is asked to redesign. Fundamental refactors are routed to a human. ([10:41](https://youtu.be/VaS2h-dY1-4?t=641))
- **Give each task its own disposable agent with its own full machine** — Chat platforms like Slack give one bot per app, and each new agent needs a manually created app manifest, so multi-agent provisioning is not supported. His answer is a Kubernetes operator that starts a full pod per agent with a harness and state sync. He calls this wasteful but a better abstraction than a sandboxed web agent. ([13:09](https://youtu.be/VaS2h-dY1-4?t=789))
- **Use the chat channel as the control surface for parallel agents** — He runs 1 to 5 agents at once, each bound to a Discord channel. Those channels are also how he handles side projects on the go. For the enterprise version, the same pattern is a Slack message that dispatches a debugging agent after a production release. ([3:48](https://youtu.be/VaS2h-dY1-4?t=228))

## Techniques
- **ACP as the client-side adapter layer** — Write one client integration against ACP, then plug in different coding agents (Codex, Claude Code) through their ACP adapters. Avoid building a separate plugin per editor or agent. *When:* You need one interface to many coding agents, for example across chat, IDE, and CLI surfaces.
- **Channel-bound agent sessions** — Bind one chat channel to one agent session over ACP. Run each parallel task in its own channel so the agent's context stays separate. *When:* You want to run several coding tasks in parallel from a phone or chat app.
- **Hybrid PR-triage workflow with JSON handoffs** — Chain deterministic code steps (reproduce bug, check CI) with agent judgment steps (intent, implementation quality, review). Have each agent step return structured JSON so the workflow engine can route on it. *When:* A repo gets a high volume of PRs, many of them AI-written, and you want the mechanical checks done before human review.
- **Shallow-fix loop with a human escalation gate** — Let the agent loop run superficial refactors and small bug fixes. Require a human decision for any refactor that changes design. *When:* You run agent review loops and want to avoid design drift.
- **Feedback bin for PR outcomes** — Classify each discarded or flagged AI-generated PR and store the reason as a data point about what users actually need. *When:* You need to decide which requests to absorb from a large stakeholder base.
- **Per-task disposable agent pods via a Kubernetes operator** — Create a Helm-deployed Go operator that starts a full pod per agent, with the harness inside and state synced (he suggests rsync-style or Dropbox-style sync). Expose a web UI for the agent. *When:* Many agents need to run concurrently for separate tasks with full machine access, and each task should be isolated.

## Numbers
- Over 60 KPRs total; 300 to 500 PRs open per day on average (transcript garbled; likely a PR count, unverified) ([6:36](https://youtu.be/VaS2h-dY1-4?t=396))
- Tens of thousands of stakeholders want features added to OpenClaw ([6:36](https://youtu.be/VaS2h-dY1-4?t=396))
- 1 to 5 agents run in parallel per person, each in its own Discord channel ([3:48](https://youtu.be/VaS2h-dY1-4?t=228))

## Hot takes
- Running an agent in a loop does not automatically create slop, as long as it only fixes shallow bugs and is not asked to design.
- Personal and work agents will diverge because work agents consume far more inference, so enterprise agents are where the money is.
- Chat platforms need standard multi-agent provisioning (many bots from one app manifest) before multi-agent setups in Slack or Teams can work well.
- One full machine per agent is wasteful but a better abstraction than a sandboxed web agent, because a full computer makes agents more capable.

## Tools mentioned
acpx, ACP (Agent Client Protocol), Codex, Claude Code, Zed, Discord, Slack, MS Teams, Kubernetes, Helm, Go operator, rsync, Firecracker (mentioned as used by Open Hands)

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs plan, critique, and debate loops around Claude Code. The talk's JSON-returning agent steps, which the workflow branches on, and its chat-channel control surface map onto those loops and the phone approvals. → *Make the critique step in the plan-critique loop return a JSON verdict that the harness branches on, instead of free text, and test whether it reduces misrouted loops.*
- **agentos** (1/3): The per-task pod versus sandbox trade-off touches the Crucible sandboxing layer, but the talk gives no isolation benchmarks. → *Compare a full-pod-per-agent model with Crucible's celld sandbox boundary, looking at cost and startup time, before deciding whether Crucible needs a heavier mode.*
- **general** (1/3): The talk offers a practical view of PR-triage automation, but there is no measured result. → *Read the acpx repo's workflow-engine code to see how it structures agent steps and JSON handoffs.*
