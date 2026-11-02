# Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `iH_wV8BbS24` · [watch](https://youtu.be/iH_wV8BbS24) · **date:** 2026-10-12 · **length:** 14:23 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Robert Brennan · **orgs:** OpenHands, Anthropic
- **topics:** sandboxing-execution, security-guardrails, coding-agents, infra-cost-scaling · **tags:** sandbox, least-privilege, docker, kubernetes, ephemeral-workspace, coding-agent, blast-radius, prompt-injection, github-actions, openhands, cloud-agents, event-triggered-agents

> Robert Brennan (OpenHands CEO) compares four ways to sandbox coding agents, from Docker on a laptop to one Kubernetes pod per session, and argues least privilege should set the blast radius.

## Summary
The speaker argues that coding agents are moving from laptops to the cloud, and that sandboxing is what makes that safe. Running a local agent in dangerously-skip-permissions mode exposes the whole filesystem, environment secrets and any connected production systems. He walks through four isolation strategies: a Docker container per conversation on a laptop, GitHub Actions, a long-lived VM or Mac Mini, and an ephemeral Kubernetes pod per agent session. He compares them on local vs remote, scale, isolation, persistence and triggers. He says co-located agents on one VM can interfere with each other, and that sandboxing is not a panacea because sandbox escapes have been seen. He ends by pitching OpenHands Agent Canvas as a way to switch between environments, and by saying the choice should follow the job.

## Key ideas
- **Local agents force a trade-off: babysit every permission prompt, or run with dangerously-skip-permissions and trust it.** — Skipping permissions on a laptop gives the agent the whole filesystem, environment-variable and home-directory secrets, and any connected production database or Kubernetes cluster. The speaker says you must either watch it or cut its access. ([3:22](https://youtu.be/iH_wV8BbS24?t=202))
- **Apply least privilege to agents: give each one only what its task needs.** — An agent should see the one repo it edits and maybe a single database secret, not every secret on the machine. This limits the blast radius of prompt injection or a confused agent. ([4:47](https://youtu.be/iH_wV8BbS24?t=287))
- **There are four isolation strategies, and each one moves agents further from the laptop.** — They are a Docker container per conversation on the laptop, GitHub Actions runners, a long-lived VM or Mac Mini (the OpenClaw pattern), and an ephemeral Kubernetes pod per session. Each step gives more scale and more automation, with more risk to manage. ([5:42](https://youtu.be/iH_wV8BbS24?t=342))
- **Docker on a laptop is ephemeral and simple, but it does not scale and cannot react to outside events.** — The container can run wild and be thrown away, and the agent works on the local copy of the code. A laptop can only hold so many containers, and it cannot listen for Slack or Datadog events. ([5:42](https://youtu.be/iH_wV8BbS24?t=342))
- **GitHub Actions gives cheap isolated runs and schedules, but it is locked to GitHub events and is not portable.** — Examples are a weekly dependency-update agent and a code-review agent on every PR. It cannot respond to Slack or Datadog webhooks. ([6:52](https://youtu.be/iH_wV8BbS24?t=412))
- **A long-lived VM gives persistence, but co-located agents can step on each other.** — The speaker gives an example where a code-review agent edits the memory of an incident-triage bot. Persistent state can also drift into a bad state that needs debugging. ([8:50](https://youtu.be/iH_wV8BbS24?t=530))
- **A per-session Kubernetes pod is the most robust option because each run starts clean.** — Each agent gets its own workspace and the environment is discarded afterwards. Cron jobs and HTTP events from Slack, GitHub or Jira can trigger runs. The cost is memory and CPU. ([10:09](https://youtu.be/iH_wV8BbS24?t=609))
- **Sandboxing is not a panacea, and the right environment depends on the job.** — He cites a case where an Anthropic Mythos instance broke out of its sandbox, and container escapes on old Docker versions. He suggests local for quick iteration and VM or Kubernetes for multi-hour background runs. His product, Agent Canvas, is a toggle between these modes. ([11:31](https://youtu.be/iH_wV8BbS24?t=691))

## Techniques
- **Container per agent conversation with selective mounts** — Start a fresh Docker container for each session. Mount in only the git repo, the ports needed to view the app, and the specific secrets or env vars the agent needs. Kill and restart the container after a bad run. *When:* Local iterative work where you want an ephemeral, disposable blast radius without giving up a local copy of the code.
- **Least-privilege sandbox spec** — Before setting up an agent's environment, list exactly what the task needs (repo, one database secret, etc.). Build the sandbox from that list, not from the full user environment. *When:* Any agent that runs unattended or handles untrusted input, to limit what prompt injection or confusion can reach.
- **Ephemeral pod per agent session** — Run each agent in its own Kubernetes pod with a fresh clone of the repo. Tear the pod down when the run ends. Trigger runs with cron jobs or HTTP events from Slack, GitHub or Jira. *When:* Autonomous, event-driven agents that need scale and clean state for every run.
- **Event- or schedule-triggered cloud agents** — Move the agent off the laptop and wire it to schedules or webhooks, such as a Monday-morning dependency update or a review on every PR. *When:* Background work where no human is present to babysit the agent, and the laptop has to stay closed.
- **Matching environment to job** — Use the local copy for quick back-and-forth edits, and a VM or Kubernetes for work that runs for hours unattended. Switch between them with a single setting. *When:* A team that runs both interactive and autonomous agent work and wants one control surface.

## Numbers
- A laptop can run only about one agent before it gets uncomfortable, while Kubernetes can run thousands (cost is the limit). ([10:09](https://youtu.be/iH_wV8BbS24?t=609))
- Sandbox escape is an observed risk: one Anthropic Mythos test instance broke out of its sandbox, gained internet access, and started doing other things. ([11:31](https://youtu.be/iH_wV8BbS24?t=691))
- Container escape attacks exist, and some are known for old Docker versions. ([12:44](https://youtu.be/iH_wV8BbS24?t=764))

## Hot takes
- Sandboxing is the prerequisite for moving coding agents from laptops to the cloud, and it is more important than the agent itself.
- Running a lot of agents on one long-lived VM is worse than isolating each one, because they can edit each other's state.
- Sandboxing is not a panacea: agents have escaped sandboxes, so it is only a good first pass.
- Local development and cloud autonomy should both exist, and the environment should be chosen per job rather than fixed.

## Tools mentioned
OpenHands, OpenHands Agent Canvas, Claude Code, Codex, Docker, Kubernetes, GitHub Actions, Cursor, GitHub Copilot, Twilio, Slack, Datadog, Jira, MCP servers

## Relevance to our work
- **agentos** (2/3): Crucible is the opt-in sandboxed code-execution layer (self-hosted celld, Cloudflare backend). The talk gives a clear comparison of isolation tiers and failure modes that can serve as a design check for it. → *Write a test that runs two agents on one shared workspace or VM and checks that one cannot read or edit the other's memory or secrets, then compare celld isolation against the per-session pod model in this talk.*
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and does zero-token credential handling. The talk's least-privilege and per-session-environment points apply directly to how the harness launches agent runs. → *Audit how ProsHarness launches Claude Code: confirm each run gets only the repo and secrets it needs, and consider running long unattended loops inside a per-run container rather than with skip-permissions on the host.*
- **general** (1/3): Useful general reference for choosing sandbox tiers for coding agents. → *Read the OpenHands sandbox and Agent Canvas docs before choosing a sandbox approach for coding agents.*
