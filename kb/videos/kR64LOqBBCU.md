# AgentCraft: Putting the Orc in Orchestration — Ido Salomon

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `kR64LOqBBCU` · [watch](https://youtu.be/kR64LOqBBCU) · **date:** 2026-05-18 · **length:** 11:18 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Ido Salomon · **orgs:** ?
- **topics:** multi-agent, coding-agents, product-ux, pr-code-review · **tags:** orchestration, agent-ui, file-collision, review-bundles, campaign-mode, human-in-the-loop, collaboration, rts-metaphor

> Ido Salomon demos AgentCraft, an RTS-style orchestrator for many coding agents, arguing the human is the bottleneck and offering visibility, campaigns, review bundles and shared workspaces as fixes.

## Summary
The speaker argues that running 10 to 100 coding agents fails because the human operator is the bottleneck, not the agents. He presents AgentCraft, a free experimental orchestrator that shows live agent sessions (Cursor, Claude Code, Codex, OpenClaw) as units on a map. The map is a projection of the file system, so you can see which agent touches which file, build a lineage of changes, and show collision heat maps. He then describes moving the human out of the loop: agents generate their own missions (Quest), a broad campaign is decomposed by an agent in a container, and the human reviews plans and "review bundles" with diffs, rationale and screenshots or video. Shared workspaces let a teammate's agents be picked up and continued, and a soft chat lets humans and agents announce which files they are working on. The talk is mostly a product walkthrough with a call for feedback, so the reusable ideas are the visibility and review-surface patterns rather than measured results.

## Key ideas
- **The bottleneck in multi-agent work is the human operator, not spinning agents up.** — Launching 10, 20 or 100 agents is easy. Attention, planning and babysitting are what break down, so the orchestrator must reduce human attention cost. ([0:00](https://youtu.be/kR64LOqBBCU?t=0))
- **Managing many agents borrows skills from RTS games.** — Juggling dozens of units maps to real-time strategy play. He uses muscle memory, hotkeys to cycle to agents waiting on approval or answers, and fast visual scanning. ([1:03](https://youtu.be/kR64LOqBBCU?t=63))
- **Visibility comes from projecting agent activity onto the file system.** — Directories appear as map regions and files as runes. Each agent's touches, change lists and timing give full lineage. A heat map of overlapping activity can flag collisions before they happen. ([3:13](https://youtu.be/kR64LOqBBCU?t=193))
- **Remove the human from ideation with self-generated missions and campaigns.** — A Quest feature has agents pick their own tasks. A campaign takes a broad goal, runs in a container, decomposes and plans the work, and presents a plan for approval, so the human owns planning and review rather than babysitting. ([5:58](https://youtu.be/kR64LOqBBCU?t=358))
- **Review bundles are the new review surface.** — Each agent's output is grouped with its task list, rationale, and visual evidence such as screenshots and video, so reviewers do not have to reconstruct what happened from raw diffs. ([5:58](https://youtu.be/kR64LOqBBCU?t=358))
- **Cheap parallel attempts shift effort from planning to picking the best result.** — If an agent can attempt the same task 10 times, the human spends less time perfecting the plan and more time choosing among outputs. This is his stated reason for moving effort to review. ([7:28](https://youtu.be/kR64LOqBBCU?t=448))
- **Shared workspaces let humans hand work between their agents and teammates' agents.** — A designer's agent session can be picked up by an engineer's agents and continued. Soft coordination is a chat across humans and agents, where an agent that sees 'I'm also working on this' adjusts its next action and knows which files others are changing. ([7:28](https://youtu.be/kR64LOqBBCU?t=448))

## Techniques
- **Filesystem-projected agent map with collision heat map** — Map each agent's file reads and writes onto the directory tree, keep a per-file change list with agent and timestamp, and render overlap density as a heat map to flag or prevent collisions. *When:* Several agents edit one repo in parallel and you need to see who is touching what before merge conflicts happen.
- **Hotkey cycling to agents that need attention** — Surface agents waiting on plan approval or a question, and let the operator cycle between them with a fixed key so triage is fast and muscle-memory driven. *When:* Many agent sessions run at once and each one occasionally blocks on the human.
- **Campaign mode: broad goal in a container, plan first** — Give a high-level goal, let an agent decompose and plan inside an isolated container, present the plan for approval, then let it run unattended with no babysitting. *When:* Long multi-step tasks where the human should approve the plan and review the result, not watch each step.
- **Review bundles with rationale and visual evidence** — Package each agent run as one reviewable unit: diff, task list, why the changes were made, and screenshots or video of the result. *When:* Reviewing many agent-produced PRs or branches and wanting to cut review time.
- **Best-of-N parallel attempts with human selection** — Run the same task several times with different agents and pick the most fitting output, instead of over-investing in one upfront plan. *When:* Outputs are cheap to generate and easy to compare, and the planning cost is higher than the review cost.
- **Soft coordination via shared human and agent chat** — Agents post what they are starting, humans reply to claim the work, and agents read these signals and each agent's file-change intent on their next turn. *When:* Several humans and their agents work on one codebase and need to avoid duplicate work without hard locks.

## Numbers
- Example scale discussed: 10, 20 or 100 agents in parallel. This is illustrative, not a measured result. ([0:00](https://youtu.be/kR64LOqBBCU?t=0))
- Best-of-N example: an agent can attempt the same task 10 times, and the human picks the best. This is an illustrative argument, not a benchmark. ([7:28](https://youtu.be/kR64LOqBBCU?t=448))

## Hot takes
- The human operator, not the agents, is the bottleneck in multi-agent coding.
- Orchestrating agents is the same skill set as playing RTS games.
- Humans should spend their time on planning and review, and let agents spend their time on execution and retries.

## Tools mentioned
AgentCraft, MCPUI, MCP Apps, Cursor, Claude Code, Codex, OpenClaw, Git, Chrome

## Relevance to our work
- **prosharness** (2/3): Its campaign flow (plan, human approval, unattended run, review) and review bundles overlap with ProsHarness's plan, critique and approval loop, and its file-collision view bears on running parallel harness loops. → *Try a review bundle per ProsHarness run (diff, plan, rationale, test or screenshot evidence) as the surface for phone-driven approval, and check whether file-touch collision detection is needed for parallel loops.*
- **agentos** (1/3): Telemetry on which agent touches which file and when is a possible input for SkillForge's skill-mining signal, but the talk does not address skill mining. → *Consider logging per-file agent touch events as a candidate signal source for SkillForge's success and skill-worthiness scoring.*
