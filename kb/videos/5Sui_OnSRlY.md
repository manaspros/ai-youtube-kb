# The Missing Primitive for Agent Swarms — Lou Bichard, Ona

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `5Sui_OnSRlY` · [watch](https://youtu.be/5Sui_OnSRlY) · **date:** 2026-06-18 · **length:** 18:37 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Lou Bichard · **orgs:** Ona, Stripe, Ramp, OpenAI, GitHub, Linear
- **topics:** multi-agent, software-factory, sandboxing-execution, agent-architecture · **tags:** swarms, sub-agents, coordination, software factory, background agents, fleets, harness engineering, VM isolation, state machines, durable execution, CLI gates, ACP, Symphony, context rot

> Ona's field CTO argues that runtimes, orchestration and triggers are largely solved for coding-agent swarms, and that agent coordination is the missing primitive. He proposes state-machine workflows packaged as a CLI that runs locally and in CI.

## Summary
Lou Bichard (field CTO at Ona, formerly Owner in the auto-captions) defines a software factory as gradually moving the human out of the SDLC loop, rather than one engineer running many parallel agents. He lays out three scaling patterns (swarm fan-out and fan-in, fleets across many repos, and event triggers) and cites Stripe's Minions and Ramp's Inspect as large-company examples. He argues that the runtime (VMs preferred over containers), orchestration and triggers are mostly solved, but agent coordination is not, since GitHub PRs and Linear tickets are human tools misused for agents. He says agents skip micro-steps and lose context, so SDLC stages need to be broken into gated micro-steps. His proposed fix is workflows as state machines or graphs, packaged as a CLI that the local agent calls to check whether it can advance a step. The talk is short and mostly conceptual, with a brief sub-agent demo, and it ends with a public two-week build of a software factory.

## Key ideas
- **Software factory means slowly moving the human out of the SDLC loop, not running many agents in parallel as one IC.** — The speaker's own definition: work flows from development into production automatically, with the human on the loop. He says the parallel-agents-per-engineer framing is not his definition. ([1:03](https://youtu.be/5Sui_OnSRlY?t=63))
- **Three scaling patterns for coding agents: swarm, fleet and events.** — Swarm fans one intent out to several agents and funnels results into one PR or task. Fleet fans agents out across many repos in an org. Events (webhooks, PR raised, ticket created) trigger agents. ([2:17](https://youtu.be/5Sui_OnSRlY?t=137))
- **Runtime, orchestration and triggers are mostly solved. Agent coordination is the missing piece.** — Coordination means agents handing off tasks to each other and collaborating. He says this is the gap that blocks a full software factory. ([5:59](https://youtu.be/5Sui_OnSRlY?t=359))
- **He argues dev tasks should run inside a VM, not a container.** — He says containers are not a bulletproof isolation boundary. Pods are bursty and show noisy-neighbor compute contention, while a VM gives full isolation. ([5:59](https://youtu.be/5Sui_OnSRlY?t=359))
- **Sub-agents come in two forms with different isolation and scale.** — In the demo, a parent agent in a VM spawns sub-agents that either run as processes inside that VM or as new VMs. The parent gives each child a small context and one task, and children message results back. Managing these sub-agents in the UX is an open problem. ([7:17](https://youtu.be/5Sui_OnSRlY?t=437))
- **Agents do not respect coarse SDLC stages, so the SDLC must be broken into micro-steps.** — A stage like plan contains many micro-steps. Agents lose context as the window fills (context rot), skip steps, and skip tests to please the user. Context is the hardest part of building a software factory. ([10:20](https://youtu.be/5Sui_OnSRlY?t=620))
- **GitHub and Linear are poor coordination layers for agents.** — Using PRs for agent handoffs becomes noisy, and humans cannot tell where to step in. Symphony built on Linear has the same problem of reusing human tools in odd ways. ([11:46](https://youtu.be/5Sui_OnSRlY?t=706))
- **Proposed fix: state-machine workflows with gates, packaged as a CLI.** — Workflows would be state machines (drawing on durable execution) with compliance gates. The local agent would call a CLI to ask whether it has finished a step and may proceed. The same CLI would run in CI. He is unsure whether to release his spec as an implementation or as a standard. ([12:58](https://youtu.be/5Sui_OnSRlY?t=778))

## Techniques
- **Parent-child sub-agents with scoped context** — A controlling parent agent splits a large spec into tasks. Each sub-agent gets a small slice of context and one task, and reports back by message passing. The parent governs and collapses the results at the end. *When:* Implementing a large detailed spec, where one agent's context would rot before it finishes.
- **Two-tier sub-agent placement** — Run lightweight sub-agents as processes inside one VM, and use separate VMs for scale-out or stronger isolation. *When:* Choose process-level for cheap parallel sub-steps and VM-level when isolation or horizontal scale matters.
- **Fleet fan-out with prompts and scripts as a workflow** — Define a change as prompts and scripts, then trigger agents on a schedule or event to run it across many repos, each in its own environment. *When:* Org-wide mechanical changes such as CVE remediation, raising test coverage, or enforcing a standard.
- **Harness engineering loop** — Let the agent run, find where it gets lost, then encode the fix back into the repo as AGENTS.md, skills, or unit tests that give it feedback. *When:* After each recurring failure, so the repo steers future agent runs.
- **Gated micro-step workflow (state machine)** — Split each SDLC stage into micro-steps. Each step has a deterministic completion gate, and the workflow advances only when the gate passes, so the agent cannot skip steps such as tests. *When:* Agents keep skipping steps or stages, and you need deterministic progress and compliance checks.
- **CLI-packaged workflow gate** — Expose the workflow as a local CLI that a running coding agent calls to check whether a step is complete and whether it can proceed. The same CLI runs in CI. *When:* You want one workflow definition to run both locally and in CI.

## Numbers
- Stripe's Minions drive thousands of pull requests with coding agents on top of existing infrastructure (as cited by the speaker, not measured here). ([3:20](https://youtu.be/5Sui_OnSRlY?t=200))
- Demo: a parent VM agent spawned three sub-agents, each in its own VM, and each showed seven sub-items. The speaker says VM count is limited only by spend and cloud scale. ([7:17](https://youtu.be/5Sui_OnSRlY?t=437))
- The speaker's public build of a software factory runs over two weeks, starting the following week. ([14:16](https://youtu.be/5Sui_OnSRlY?t=856))

## Hot takes
- Coordination, not runtime or triggers, is the missing primitive for agent swarms.
- GitHub is a poor coordination layer for agents.
- Dev tasks should run in VMs, not containers, for agent isolation.
- Context management is the hardest part of building a software factory.
- Harness engineering is context engineering extended to everything in the repo that gives agents feedback.

## Tools mentioned
Ona dev environments, GitHub, Linear, Symphony, ACP, ACPX, Fabro, n8n-style graph workflows, backgroundagents.com

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has checkpoint and resume plus plan-critique-debate stages, and this talk's gated micro-step workflow and CLI gate fit that design directly. → *Prototype a ProsHarness command that the running Claude Code agent calls to ask whether a plan or checkpoint stage is complete before advancing, then check whether the same command can run in CI.*
- **agentos** (1/3): Crucible runs opt-in sandboxed code execution, and the talk argues VMs beat containers for agent dev tasks, which bears on that backend choice. → *Check whether Crucible's celld backend gives VM-grade isolation for coding-agent tasks, or whether containers are the default that the talk warns about.*
