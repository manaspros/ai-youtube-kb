# Multiplayer agentic engineering — Arjun Singh, Superconductor

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `OL7kfezynJM` · [watch](https://youtu.be/OL7kfezynJM) · **date:** 2026-08-18 · **length:** 18:44 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Arjun Singh · **orgs:** Superconductor, Gradescope
- **topics:** software-factory, coding-agents, sandboxing-execution · **tags:** multiplayer agents, team collaboration, cloud sandbox, model-agnostic, meeting bot, codebase benchmark, network egress allowlist, scoped credentials, Superconductor

> Arjun Singh (Superconductor) on making agent work multiplayer: one shared session across Slack, desktop, mobile and GitHub, cloud sandboxes, and benchmarking agents on your own codebase.

## Summary
Arjun Singh, co-founder of Superconductor (formerly of Gradescope), describes how his team works with coding agents as a group rather than on individual laptops. He lists five lessons and adds a sixth: stay model and harness agnostic, make one agent session reachable from every interface, make agent work visible to the whole team, turn external signals like meetings, tickets and calls into reviewable code, run agents in isolated cloud sandboxes with scoped access, and benchmark agents on your own repo. He reports that about 99.9% of their PRs are agent-generated, all human-reviewed, and that Codex became their cheaper default after their own benchmark. Much of the talk promotes his product, and the benchmark charts are shown on screen but not quantified in the transcript, so the cost and quality comparisons cannot be checked from the talk alone.

## Key ideas
- **Stay model and harness agnostic** — The best model or harness can change weekly, and open-weight models such as GLM 5.2 are much cheaper. Speaker also argues token sellers' incentives are not aligned with the team's. Switching defaults should not disrupt the team's workflow. ([1:09](https://youtu.be/OL7kfezynJM?t=69))
- **One agent session across every human interface** — Slack bots from Claude, Codex and Superconductor still trap work in one surface. The goal is the same session, with the same context, reachable from Slack, desktop, mobile and GitHub, so people can start in one place and finish in another. ([3:30](https://youtu.be/OL7kfezynJM?t=210))
- **Make agent work visible and collaborative** — The session shows everyone involved and who is notified, which matters when non-technical people trigger work. Team members can ask the agent in-thread why it made a choice, and the agent can attach screenshots or videos as artifacts visible from any surface. ([3:30](https://youtu.be/OL7kfezynJM?t=210))
- **Turn external signals into code the team can evaluate** — Customer calls, Slack threads, Sentry errors and emails already exist in many systems. A meeting bot that joins Meet, Zoom or Teams listens, links to existing work when it finds it, and creates tickets and prototypes. Speaker says this yields dozens of prototypes and a few shippable PRs per customer call with little manual work. ([6:17](https://youtu.be/OL7kfezynJM?t=377))
- **Add acceptance criteria so agents know when they are done** — A bot-created ticket led the team to add acceptance-criteria fields to the ticket form. The idea came from a meeting, not from an engineer, and was then made concrete with a screenshot and a live preview. ([7:44](https://youtu.be/OL7kfezynJM?t=464))
- **Run agents in isolated cloud sandboxes, not on laptops** — Cloud sandboxes remove laptop-lid anxiety and keep agents away from whatever is on a developer's machine. Speaker's main argument is least privilege: an agent that finds a production token on a laptop while believing it is on staging can delete production data. ([10:06](https://youtu.be/OL7kfezynJM?t=606))
- **Use a configurable network sandbox that asks before granting access** — Agents get an allowlist of reachable hosts. When they try a blocked host, the user is prompted and can grant access per ticket or per project, for example to read a new vendor's docs. This also blocks code or secret exfiltration. It lets non-technical staff trigger real changes safely. ([11:07](https://youtu.be/OL7kfezynJM?t=667))
- **Benchmark agents on your own codebase** — Pick PRs that represent good engineering work, run each agent and harness on the same task, and compare quality against cost and time. Speaker says public benchmarks like SWE-bench are Python-only and may not predict results on a Ruby on Rails codebase. ([13:35](https://youtu.be/OL7kfezynJM?t=815))

## Techniques
- **Cloud sandbox per project** — Run the project's agents in an isolated cloud environment instead of on a laptop. Use an environment-setup assistant, or ask Claude Code or Codex to make the project run inside the sandbox. *When:* When work must continue after the laptop closes, or when agents should see only the access they need.
- **Same session across interfaces** — Keep one agent session that can be continued from Slack, desktop, mobile or GitHub, so context is never copied between tools. *When:* When a task starts with one person or surface and must be finished by another, such as a non-technical requester and an engineer.
- **Artifacts as proof of work** — Have the agent attach screenshots or videos of what it built to the session so reviewers can see results without opening a separate tool. *When:* For UI or visual changes, and for reviews by people who do not read code.
- **Meeting bot as an idea-to-ticket intake** — Invite a bot to a meeting on Meet, Zoom or Teams. It listens, links to existing work, creates tickets and starts prototypes. *When:* During customer calls, onboarding calls and team meetings, when ideas come up faster than people can file them.
- **Acceptance-criteria fields in the ticket form** — Add explicit criteria fields to the ticket so the agent checks its own output against stated conditions before reporting done. *When:* When an agent is asked to ship a change and needs a clear definition of done.
- **Network egress allowlist with grant prompts** — Define which hosts an agent can reach. When it tries a blocked host, prompt the human to grant access for one ticket or the whole project. *When:* When agents need documentation or vendor access but must not send code or secrets to unknown places.
- **Scoped credentials instead of ambient access** — Do not let agents find broad tokens on a developer's machine. Give each sandbox only the credentials its task needs. *When:* Always, but especially when an agent might be wrong about which environment it is in, such as staging versus production.
- **Codebase-specific agent benchmark** — Select strong PRs from the repo, run each candidate agent or harness on the same task, and plot quality against cost and time. *When:* When choosing default harnesses or models, or deciding how to route tasks for a specific codebase.
- **Switch defaults on evidence** — Keep several harnesses and models available, and move the default when a benchmark or vibe check shows a change. The speaker says switching took no meaningful disruption. *When:* When a new model or harness appears, or when cost or quality shifts.

## Numbers
- Small team used about 10.5 billion tokens in the past month ([15:31](https://youtu.be/OL7kfezynJM?t=931))
- About 3,300 Claude Code runs in the past month ([15:31](https://youtu.be/OL7kfezynJM?t=931))
- Those Claude Code runs were quoted at about $10,000 in token usage. The speaker jokes that they did not actually spend that much, so the real cost is unclear. ([16:29](https://youtu.be/OL7kfezynJM?t=989))
- Codex ran about 4x as many sessions as Claude Code and was cheaper overall ([16:29](https://youtu.be/OL7kfezynJM?t=989))
- About 99.9% of PRs are heavily agent-generated, and all are human-reviewed ([15:31](https://youtu.be/OL7kfezynJM?t=931))
- Benchmark charts (quality vs cost, quality vs time) were shown on screen but no values were stated in the transcript. Speaker says Anthropic agents got steadily better but not faster, and Codex and Cursor were fast and good. ([14:38](https://youtu.be/OL7kfezynJM?t=878))
- Meeting bot was left running for a four-hour Google Meet at the expo ([6:17](https://youtu.be/OL7kfezynJM?t=377))

## Hot takes
- Public benchmarks like SWE-bench may have little to do with your codebase. Benchmark on your own PRs.
- Token vendors want to sell you more tokens. Stay model-agnostic so you control spend.
- Running agents in YOLO mode on a laptop with broad credentials is a real risk. Put agents in sandboxes with scoped access.
- Non-technical staff can safely ship real changes if they work through a sandboxed, permissioned agent.

## Tools mentioned
Claude Code, Codex, Cursor, Slack, GitHub, Linear, Sentry, Notion, Google Meet, Zoom, Microsoft Teams, GLM 5.2, Fable (model, per speaker), MiniMax and Kimi K2 (mentioned, not evaluated), SWE-bench, Terminal-Bench, Ruby on Rails

## Relevance to our work
- **agentos** (2/3): Model-agnostic routing and per-codebase quality/cost/time measurements apply to AgentOS's strategy routing in Govrix Scout. The talk gives a concrete benchmark method. → *Add a repo-level benchmark (curated merged PRs, run each candidate model, record quality, cost and time) as an input to Govrix Scout strategy routing, and compare against the public-benchmark routing currently assumed.*
- **prosharness** (2/3): ProsHarness wraps Claude Code and already handles checkpointing and zero-token credentials. The talk's egress allowlist with grant prompts and its per-run scoped credentials are directly comparable. → *Compare ProsHarness's credential handling with the talk's scoped-credential and egress-allowlist approach, and consider a per-ticket allowlist prompt for unattended plan runs.*
- **general** (2/3): Recurring interests include evals for agents and multi-agent workflows. The talk gives a practitioner method for evaluating agents on real repo tasks and for keeping several agents running in parallel. → *Build a small eval set of 10 to 20 merged PRs from one real repo, then run two or three agent configurations against it and record quality, cost and time.*
