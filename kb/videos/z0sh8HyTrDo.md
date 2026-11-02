# Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `z0sh8HyTrDo` · [watch](https://youtu.be/z0sh8HyTrDo) · **date:** 2026-08-18 · **length:** 13:42 · **format:** talk · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Ramana Siddanth Emani · **orgs:** Auditoria AI
- **topics:** software-factory, multi-agent, coding-agents, governance-compliance · **tags:** harness-engineering, developer-velocity, git-worktrees, parallel-subagents, human-in-the-loop, sox-compliance, finance-agents, goals-and-loops, self-improving-harness, dreaming, minimal-ux

> Auditoria AI speaker says human attention bottlenecks agent work: use parallel worktree subagents, skills, one-pane UX, goals and loops, and self-improving harnesses, keeping humans at intake and sign-off.

## Summary
The speaker, a data scientist at Auditoria AI (finance agents), argues that production agent failures come from slow developer loops, not from models or frameworks that change every few months. He proposes four primitives: subagents running in parallel git worktrees, organizational skills as encoded recipes, MCP connections to client systems, and goals plus loops. He walks through a nine-step bug-ticket-to-stage pipeline where a human is needed only at intake (step 1) and final validation on stage (step 9). He suggests a single "one pane of glass" UI that aggregates cluster status, logs, Jira, GitHub PRs and an agent session. For finance, he argues accountability and SOX sign-off keep humans in the loop, so human attention becomes the bottleneck. In the last section he describes having the agent review its own loop each day to remove bottlenecks, and a background "dreaming" process that compacts customer session patterns into improvement data. The talk offers no measured results, and most numbers are the speaker's own claims or verbal estimates.

## Key ideas
- **Production agent failures are a developer-velocity problem, not a model problem** — Models and frameworks change every few months or years, so swapping them does not fix production bugs fast. The speaker says the answer is to speed up the developer loop itself by automating it. ([1:12](https://youtu.be/z0sh8HyTrDo?t=72))
- **Four primitives: subagents in worktrees, skills, MCP connections, goals and loops** — Each subagent gets its own git worktree as an isolated folder so parallel agents do not collide. Skills hold organizational workflows, and MCP lets agents reach client data in any system. ([2:43](https://youtu.be/z0sh8HyTrDo?t=163))
- **Human attention, not compute, becomes the limit once agents run in parallel** — With many worktrees running, the orchestrator's attention is the constraint. The speaker says tasks should not be queued by hand; the agents should handle the queue. ([3:47](https://youtu.be/z0sh8HyTrDo?t=227))
- **Map each QA bug ticket to its own worktree and pipeline** — Each ticket runs a root-cause analysis, pulls traces and logs, does TDD, runs local end-to-end tests, opens a PR, merges, and deploys through dev and stage. The speaker proposes a human at only the first and last steps. ([5:52](https://youtu.be/z0sh8HyTrDo?t=352))
- **Accountability in regulated finance limits how far humans can be removed** — Under SOX, a human auditor and controller sign off on work, and agent-reviews-agent does not give clear accountability when production breaks. The speaker therefore keeps a human as verifier. ([8:26](https://youtu.be/z0sh8HyTrDo?t=506))
- **Let the agent analyze and remove its own loop bottlenecks each day** — After each batch of tickets, the agent lists bottlenecks in its own process and removes them over time. The speaker says after about a month a one-sentence request can drive the full bug-fix cycle. ([9:31](https://youtu.be/z0sh8HyTrDo?t=571))
- **Combine goals and loops, run from a phone, and add background dreaming** — A goal such as fixing a data discrepancy can run as a loop that the user monitors from a phone. A background process collects patterns from customer sessions and compacts them into data points the system can learn from. ([11:00](https://youtu.be/z0sh8HyTrDo?t=660))

## Techniques
- **Worktree-per-task parallel subagents** — Give each independent task (for example each Jira ticket) its own git worktree. Let an agent in that worktree spawn its own subagents, and keep worktrees parallel so agents do not fight over files. *When:* Many independent bug or feature tasks at once, where work must not collide on the same checkout.
- **Ticket-to-stage pipeline with two human gates** — The agent handles requirements, RCA, trace and log pulls, TDD fix, local end-to-end tests, PR creation, and deploys to dev and stage. A human reviews intake at the start and validates on stage at the end. The speaker says the middle steps need no human. *When:* High-volume bug fixing where the team trusts the agent for middle steps but must keep sign-off, such as regulated finance.
- **Encode organizational procedure as skills** — Write each team workflow as a reusable skill so agents follow the correct process for each production bug, not an improvised one. *When:* Repeated workflows where consistency and audit of the procedure matter.
- **Single-pane minimal UX for orchestration** — One widget or dashboard shows cluster services and pods, system logs, Jira tickets, GitHub PRs, and an agent session, so the orchestrator does not switch windows. *When:* An orchestrator is juggling many agents and tools and losing time to context switching.
- **Daily self-retrospective on the agent's own loop** — After each batch of tickets, ask the agent to list the bottlenecks in its own workflow and fix them, repeating daily. *When:* A stable, repeating dev workflow where the harness itself can be iteratively improved.
- **Goals plus loops, monitored from a phone** — Set a goal (for example, resolve a data discrepancy in a report), run it as a loop, and check progress from a phone rather than staying at a laptop. *When:* Long-running fixes that need little steering and periodic check-ins.
- **Background dreaming for pattern compaction** — Run a background job that gathers customers' repeated session patterns and failure types and compacts them into data points that the system can use for upgrades. *When:* Many customers hitting the same problem patterns in production, so shared improvement data helps everyone.

## Numbers
- New model releases arrive about every 3.5 months, and new chips about once a year (speaker's general estimate, not measured) ([1:12](https://youtu.be/z0sh8HyTrDo?t=72))
- On a 48 GB MacBook, the speaker says about 50 active worktrees, meaning 50 active subagents, can run at once (speaker's claim, no benchmark shown) ([3:47](https://youtu.be/z0sh8HyTrDo?t=227))
- The ticket-to-stage pipeline has nine steps, with a human needed only at steps 1 and 9 ([5:52](https://youtu.be/z0sh8HyTrDo?t=352))
- A graph shows the number of neck rotations per shipped change dropping sharply, but no values are given in the transcript ([7:25](https://youtu.be/z0sh8HyTrDo?t=445))
- Example cadence: one loop run over a day or two solves about five to six bug tickets ([9:31](https://youtu.be/z0sh8HyTrDo?t=571))

## Hot takes
- Model and framework swaps are not what fixes production bugs; the developer loop's velocity is the real lever.
- Humans should be verifiers, not the throughput ceiling, since human attention is limited.
- In regulated finance, 'the agent did it' is not an acceptable accountability answer, so a human sign-off must stay in the loop.
- Agents can upgrade their own harness by analyzing and removing their bottlenecks, which eventually lets one sentence drive a full bug fix.

## Tools mentioned
Claude Code, git worktrees, Kubernetes, Docker, Jira, GitHub, MCP

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code with checkpoint/resume, loops/schedules and phone-driven approvals. The talk's worktree-per-task subagents and goal-plus-loop-from-phone pattern overlap directly with that design. → *Prototype a ProsHarness run that gives each ticket its own git worktree with subagents, and check whether the phone approval flow can cover both the intake gate and the stage-validation gate described in the talk.*
- **general** (2/3): Parallel worktree subagents, human-gate placement, and self-retrospectives on the agent's own loop are relevant to context engineering and multi-agent work. The evidence is anecdotal, though. → *Run one week of parallel worktree subagents on independent tasks and log how often a human gate is actually needed, compared with a single-session baseline.*
- **agentos** (1/3): The 'dreaming' idea of compacting repeated session patterns into reusable data points is loosely related to SkillForge's telemetry-to-skill mining. The talk gives no method, so it is only a prompt for our own design. → *Note the background pattern-compaction idea as a candidate input for SkillForge's open skill-worthiness question. Design the method ourselves, since the talk offers none.*
