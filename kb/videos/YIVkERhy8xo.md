# We're the bottleneck, but we don't have to be — Ido Salomon, AgentCraft

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YIVkERhy8xo` · [watch](https://youtu.be/YIVkERhy8xo) · **date:** 2026-10-04 · **length:** 14:50 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Ido Salomon · **orgs:** AgentCraft, MCP Steering Committee
- **topics:** multi-agent, product-ux, coding-agents, software-factory · **tags:** agent-supervision, orchestrator, RTS-UI, attention-queue, review-kit, parallel-runs, shared-workspace, collaboration, low-floor-ux, loops, local-containers, heat-map, MCP Apps

> Ido Salomon (AgentCraft) argues that humans are the bottleneck in agent work and demos a game-style orchestrator with attention-jumping, a map view, review kits, shared rooms, and a simpler "loopers" mode for non-engineers.

## Summary
The speaker says agents are capable but supervising many of them at once is exhausting, so the human is the real limit. He presents AgentCraft, a game-inspired orchestrator that wraps Claude Code, Codex, OpenCode and similar agents. He builds the talk as a ladder: visibility first (a side panel of agent status and a map that projects the file system and shows which agent touched which file), then autonomy (orchestrators that break a goal into tasks and run them in isolated local containers, plus background loops), then a review kit that shows changes with visual evidence and can compare parallel attempts. Next comes collaboration, with local rooms that others join through a tunnel, shared views of humans and agents, and forking work without being tied to Git. He ends with a lower-floor idea, a simpler mobile-game-style view for people who find the granular tools daunting. The talk is a product demo with a call for feedback, and it contains no measured results.

## Key ideas
- **The human supervisor, not the model, is the bottleneck when many agents run at once.** — Steering, reviewing and babysitting each agent is what burns people out at scale, so the goal is to raise the ceiling of what one person can supervise. ([0:08](https://youtu.be/YIVkERhy8xo?t=8))
- **Visibility comes first: show each agent's task, last action and current action in one place.** — A side panel lets the user see at a glance which agent needs attention. A map view projects the file system and marks which agent is working on which file, with heat maps built from those links. ([2:46](https://youtu.be/YIVkERhy8xo?t=166))
- **Borrow RTS-game attention controls: one key jumps to the nearest agent that needs input.** — The user can move from one blocked agent to the next to answer questions or approve plans without scanning every session. ([4:04](https://youtu.be/YIVkERhy8xo?t=244))
- **Autonomy means giving a broad goal to an orchestrator that splits it into tasks and runs them in isolated local containers, with loops that create work in the background.** — Loops can scan sources such as GitHub or social feeds and turn findings into feature work with no upfront prompting. The speaker frames this as the start of software factories. ([5:29](https://youtu.be/YIVkERhy8xo?t=329))
- **Reviewing many agent outputs needs a review kit, not a stream of raw diffs.** — The kit gathers all changes, offers a per-file view or visual evidence such as videos and screenshots, and can run several instances in parallel so the user picks the best result. ([6:52](https://youtu.be/YIVkERhy8xo?t=412))
- **Collaboration means shared rooms that people and agents join, with a common notice board of who is doing what.** — Rooms run locally and can be exposed through a tunnel. A designer can produce work that an engineer picks up, forks and continues, so the team is not tied to Git as the only shared workspace. ([8:19](https://youtu.be/YIVkERhy8xo?t=499))
- **Lowering the floor matters as much as raising the ceiling: non-engineers have adopted the tool, and a simpler mode is being tested.** — Early users include children and people with no coding background. The proposed loopers mode is a simple prompt-result loop with project bookmarks and optional detail. The speaker calls it a very early draft. ([11:03](https://youtu.be/YIVkERhy8xo?t=663))

## Techniques
- **Attention queue with jump-to-next** — Track each agent's state (running, blocked on a question, waiting for plan approval, done) and bind one key to jump to the most urgent item that needs a human. *When:* Many agents run in parallel and the human cannot watch all of them.
- **Spatial projection of agent activity** — Lay the project file tree out as a map, place markers where each agent touches files or directories, and aggregate the touches into a heat map. *When:* You need to see where agents are working across a large codebase without reading logs.
- **Review kit for parallel agent output** — Collect the full change set per run, provide a per-file view plus visual evidence (screenshots or video), and run N attempts in parallel so the reviewer compares and picks the best. *When:* Several agent runs produce changes that need quick human approval.
- **Orchestrator with isolated local containers and background loops** — Give one high-level goal to an orchestrator that decomposes it into tasks, runs each in its own local container, and schedules loops that scan sources for new work. *When:* Work can run unattended and each task needs isolation from the others.
- **Shared room with cross-agent notice board** — Host a local room, expose it through a tunnel when needed, and show each person and agent's current activity on a shared board so people can fork or hand off each other's work. *When:* A team, including non-engineers such as designers, needs to work on the same agent-driven project.
- **Progressive disclosure for low-floor use** — Default to a simple prompt-then-result view and let users open the file, tool and status detail only when they want it, with customizable layout. *When:* The target users are not developers and the granular views are overwhelming.

## Numbers
- Illustrative only: a user could 'spin up 25 cloud code agents' in the thought experiment. ([0:08](https://youtu.be/YIVkERhy8xo?t=8))
- Anecdotal workload: 'I would say 20, but even five things to review at the same time' is described as hard to manage. ([6:52](https://youtu.be/YIVkERhy8xo?t=412))
- Stated target audience for the lower-floor idea: 'around 90% of the people in the world'. This is a goal, not a measured result. ([11:03](https://youtu.be/YIVkERhy8xo?t=663))

## Hot takes
- The human, not the model, is the bottleneck in agentic work.
- Real-time strategy and city-builder games are a good model for supervising agent fleets.
- Visual evidence (video or screenshots) of agent changes is better for review than reading diffs.
- Shared agent workspaces should not be tied to Git as the only collaboration layer.
- Agent tooling should be designed for non-engineers too, including children and people with no coding background.

## Tools mentioned
AgentCraft, Claude Code, Codex, OpenCode, OpenClaw, Git, Telegram, MCP Apps (MCPUI)

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has phone-driven approvals and checkpointed long runs. The talk's needs-attention queue and review kit for parallel attempts map directly onto those flows. → *Add a needs-attention queue to ProsHarness that lists runs blocked on a question or plan approval, ordered by urgency, with a single key to jump to the next one. Feed it from the existing phone-approval events.*
- **agentos** (1/3): AgentOS has L4 observability and agent telemetry. A per-agent activity view could use that data, but the talk shows no measurements. → *Prototype a per-agent activity panel on AgentOS telemetry that shows which files or tools each agent touched, using the L4 OTel data.*
- **general** (1/3): The parallel-run review kit (diff, per-file view, visual evidence, pick the best) is a reusable pattern for reviewing subagent outputs in any multi-agent setup. → *Read the talk's review-kit section and sketch a review bundle for parallel subagent runs: changed-file list, evidence attachments, and a side-by-side pick.*
