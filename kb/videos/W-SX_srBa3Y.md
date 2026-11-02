# Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `W-SX_srBa3Y` · [watch](https://youtu.be/W-SX_srBa3Y) · **date:** 2026-06-18 · **length:** 16:17 · **format:** demo · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Michael Richman · **orgs:** Bitly, Anthropic
- **topics:** coding-agents, multi-agent, agent-architecture · **tags:** fomat, agent-supervision, push-notifications, session-management, remote-agent-control, mobile, claude-code, multi-agent-choreography, blocked-agents, control-plane

> Bitly engineer Michael Richman presents Command & Control, his tool for monitoring and answering coding agents from a phone, web or watch, and frames the idle-agent problem as FOMAT.

## Summary
Michael Richman, who leads engineering teams at Bitly, argues that coding agents spend a lot of time blocked waiting for a human, and calls this fear of missing agent time (FOMAT). He presents Command & Control, his own tool for running and supervising coding agents outside the terminal or IDE. Each agent platform gets a small daemon that reports lifecycle state (running, blocked, done) to a control plane, which aggregates sessions across machines and agent frameworks and serves a mobile, web or watch UI. The demo shows starting a session from a phone, replying to a session that is waiting, getting a push notification on completion, and resuming the same conversation in the CLI. Session management adds notification subscriptions, an "On My Radar" tier, a last-24-hours bucket, and an overview dashboard that summarizes each session from its last few messages. It is a product walkthrough of one tool with little implementation detail, so the evidence is anecdotal; the broader claim is that flow is shifting toward choreographing parallel agents and that time away from them is when good ideas come.

## Key ideas
- **Idle agent time is a real cost: an agent can stop after about two minutes to ask a question and then sit blocked until the developer returns.** — Speaker frames this as fear of missing agent time. Agents are not as autonomous as hyped, and the wait window grows as tasks run for hours or days. ([0:00](https://youtu.be/W-SX_srBa3Y?t=0))
- **Developers cannot track more than two or three concurrent agent sessions, so they cannot tell which one is blocked or off track.** — Across terminal tabs and several agent CLIs, the speaker loses track past four or five sessions. This motivates a single view with a needs-attention signal. ([4:10](https://youtu.be/W-SX_srBa3Y?t=250))
- **Command & Control gives one interface for many agent platforms and machines.** — It is built to be coding-tool agnostic (Claude Code, Codex, Gemini, Cursor, GitHub Copilot, OpenCode named). Sessions on a Mac and on a cloud VM appear in the same UI. ([11:44](https://youtu.be/W-SX_srBa3Y?t=704))
- **Architecture: a daemon per agent platform watches lifecycle and reports to a control plane, and the UI reads from that control plane.** — The control plane detects blocked state, aggregates all agents regardless of host or framework, and drives notifications. The daemon layer is described as open source. ([11:44](https://youtu.be/W-SX_srBa3Y?t=704))
- **Session triage uses tiers: push-notify sessions, an On My Radar watch list, a recent (last 24 hours) bucket, and everything else.** — Push is reserved for sessions the user subscribes to, so quieter tracking does not generate a notification per message. The list holds thousands of sessions. ([9:24](https://youtu.be/W-SX_srBa3Y?t=564))
- **An overview dashboard gives a stand-up summary of recent sessions from their last several messages.** — This lets the user triage many sessions without opening each one. ([10:20](https://youtu.be/W-SX_srBa3Y?t=620))
- **Sessions resume identically across surfaces: a prompt sent from the phone shows up in the terminal session with full history.** — The demo starts a Claude Code session from the app, then continues the same conversation in the CLI. The speaker often starts sessions from bed. ([6:59](https://youtu.be/W-SX_srBa3Y?t=419))
- **The new flow is agent choreography: moving between parallel agents, unblocking one and redirecting another.** — Speaker argues the cognitive load of many sessions is high, and that breaks away from agents are where best ideas come from, so systems should let you reach agents from anywhere. ([13:14](https://youtu.be/W-SX_srBa3Y?t=794))

## Techniques
- **Per-platform lifecycle daemon feeding a control plane** — Run a small daemon beside each agent CLI that watches session state (running, blocked on input, done). The daemon reports changes to a central control plane that aggregates all sessions. The UI reads only from the control plane and sends replies back through its API. *When:* You run several agent platforms or several machines and need one view plus a reliable blocked-on-human signal.
- **Tiered notification and watch lists** — Subscribe push notifications only to the few sessions you care about, put others on a quieter On My Radar list, and bucket the rest into recent (last 24h) and older. *When:* Many concurrent sessions where some need alerts but most only need occasional checks.
- **Overview summaries from the last few messages** — For each session, generate a short status from its last several messages and show these as a stand-up style overview. *When:* Triaging a large number of sessions quickly, to see which are finished, stuck or off track.
- **Start remotely, resume locally on the same session** — Launch or reply to a session from a phone or web UI, then resume that same session in the terminal so the full conversation history is present on both surfaces. *When:* You need to kick off or unblock agent work while away from the dev machine.

## Numbers
- An agent stalled after about two minutes waiting on a question, and sat blocked for the entire gap the developer was away. ([0:00](https://youtu.be/W-SX_srBa3Y?t=0))
- Typical coding tasks today run about 5 to 45 minutes; the speaker expects waits to grow as tasks run for five hours or five days. ([1:15](https://youtu.be/W-SX_srBa3Y?t=75))
- The speaker can keep track of only two or three concurrent sessions; at four or five they lose track. ([4:10](https://youtu.be/W-SX_srBa3Y?t=250))
- The session list holds thousands of sessions, grouped into push, On My Radar, a last-24-hours bucket, and the rest. ([9:24](https://youtu.be/W-SX_srBa3Y?t=564))
- Overview summaries are built from the last several messages of each session. ([10:20](https://youtu.be/W-SX_srBa3Y?t=620))

## Hot takes
- Agents are far from maximally autonomous; in practice they need babysitting and the need for input is unpredictable.
- Managing many concurrent agent sessions carries high cognitive load, and breaks away from agents are where the best ideas come from.
- The new flow state is agent choreography across parallel sessions rather than solo focus on one task.
- Product walkthrough of the speaker's own tool with thin architecture and no measured results; quality capped near 2 for that reason.

## Tools mentioned
Command & Control (Cmd+Ctrl, speaker's own tool), Claude Code (captioned as Cloud Code), Codex / Codex CLI, Gemini (CLI), Cursor (IDE), GitHub Copilot, OpenCode, Anthropic remote control and teleportation (Claude Code features, mentioned), Bitly MCP server (co-written by speaker, mentioned), Agent Craft (gaming-based agent tool, mentioned as seen earlier that morning)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and plans phone-driven approvals and checkpoint/resume. This talk shows the same pattern: detect a blocked session, push a notification, answer from a phone, and resume in the CLI with full history. → *Prototype a blocked-on-human state for ProsHarness runs, detected when the CLI stops on a question, that triggers a push notification and a reply path back into the same session. Compare it against the approval flow already planned.*
- **agentos** (1/3): AgentOS observability (L4: Prometheus, OTel) tracks load and latency, but the talk points to idle, blocked-waiting time as a distinct and costly state that current metrics would not show. → *Add a blocked-on-human event or span type to the OTel traces so time spent waiting on human input is measured per agent session.*
