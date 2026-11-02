# I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `4kYl2_mqmnQ` · [watch](https://youtu.be/4kYl2_mqmnQ) · **date:** 2026-07-18 · **length:** 9:11 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kyle Jaejun Lee · **orgs:** KRAFTON
- **topics:** multi-agent, claude-code, context-engineering, coding-agents · **tags:** agent fleet, orchestration hierarchy, file-based state, context reset vs compaction, review gateway, human approval gate, git sync, tmux, discord router, kubernetes underlay, multi-machine, claude code

> A KRAFTON engineer runs AI coding agents across three machines, organizes them as a hierarchy, keeps state in files, and lists the five failures and four open problems that followed.

## Summary
Kyle Jaejun Lee describes running a daily fleet of AI coding agents on a MacBook and two headless Linux boxes. He found that he had become the scheduler, memory and reviewer for six contexts, so he built a hierarchy (CEO, VP, manager, worker) where each agent has scoped context and an approval boundary. Agent state lives in files on disk, not in the model's context window, so he resets the context and reloads handoff files instead of compacting. A review gateway blocks each plan until he approves it, and then a hook starts the work. Scaling to three machines brought five failures: agents doing work themselves, cramped tmux panes, out-of-memory swap, git credentials bound to the wrong workspaces, and laptop sleep killing jobs. The fixes were a boot command that restores state from files, git-based context sync with per-machine directories, one main gateway on an always-on box, and Discord as a single router. He closes with four unsolved problems and a plan to declare what each agent needs and let Kubernetes handle compute, secrets and tools underneath his own orchestration layer.

## Key ideas
- **The human becomes the bottleneck: one person acting as scheduler, memory and reviewer for six live contexts does not scale.** — He says at six contexts he was no longer running agents, he was the scheduler, the memory and the reviewer. His fix was to model the agents as an organization so each layer sees only its slice. ([0:00](https://youtu.be/4kYl2_mqmnQ?t=0))
- **Organize agents as a hierarchy with scoped context per layer.** — CEO, VP, manager and worker are real entity types in his system, each with its own scoped context and approval boundary. Context flows down, results flow up, and he reviews only what reaches the top. ([1:22](https://youtu.be/4kYl2_mqmnQ?t=82))
- **Keep agent state in files on disk, not in the model's window.** — Each entity has a workspace with its mission, current status and a handoff folder. Shared rules, machine-bound state and work products are kept apart, so the state survives context wipes and machine crashes. ([1:22](https://youtu.be/4kYl2_mqmnQ?t=82))
- **Reset and reload instead of compacting.** — He says compaction is slow, he cannot choose what survives, and dropped content is gone. He clears the context, then the agent reads its own handoff and history files and continues. ([2:38](https://youtu.be/4kYl2_mqmnQ?t=158))
- **A review gateway blocks each plan until a human approves it.** — Any layer that wants to act submits a plan and waits. A hook starts the work on approval. He says he never has to walk into the work windows anymore, and that an infra team of agents built this gateway. ([2:38](https://youtu.be/4kYl2_mqmnQ?t=158))
- **Multi-machine scaling exposed five concrete failures.** — Orchestrators did the work themselves instead of delegating, so he forced dispatch through a CLI harness with skills. Panes got too small to read, memory ran out under Claude Code and MCP processes, git credentials bound to the wrong workspaces, and a laptop losing power killed in-flight jobs. ([4:05](https://youtu.be/4kYl2_mqmnQ?t=245))
- **Sync context across machines through git, and keep shared state behind pull requests.** — Machines commit and push context files, then poke each other over SSH to pull. Shared directories conflicted, so machine-specific state moved to per-machine directories and shared state changes only through PRs. ([5:23](https://youtu.be/4kYl2_mqmnQ?t=323))
- **Centralize control and remove any single machine that can sleep.** — Every machine sends review requests to one main gateway on an always-on Linux box. Discord, with one bot per machine, became the single router, so his phone is the remote control for the whole fleet. ([6:44](https://youtu.be/4kYl2_mqmnQ?t=404))
- **Declare what an agent needs, not where it runs, and stack Kubernetes underneath.** — He lists four open problems: cross-machine consistency, local-only tools such as MCP servers and the browser, secure credential handoff, and resource management. He plans to reuse Kubernetes for compute, secrets and tools, and build only the task orchestration, review flow and context management on top. ([7:57](https://youtu.be/4kYl2_mqmnQ?t=477))

## Techniques
- **Agent org hierarchy with scoped context** — Model orchestrators as layers (CEO, VP, manager, worker), each with its own context slice and approval boundary. Push tasks down, roll results up, and only review the top. *When:* When one human cannot hold the state of many concurrent agents and a flat pile of sessions drifts out of alignment.
- **File-backed agent state with handoff folders** — Store mission, status and handoff artifacts for each agent in a workspace on disk. On resume, the agent reads its own handoff and history files instead of relying on the window. *When:* For long-running agent work that must survive context resets, compaction loss, or machine crashes.
- **Clear-and-reload instead of compaction** — Wipe the context completely and rebuild it from the agent's own written handoff and history files, rather than asking the model to summarize the history. *When:* When the context window fills during long runs and summary-based compaction loses content you cannot choose.
- **Blocking review gateway with approval hook** — An agent submits its plan to a gateway and blocks. A human approves in one web inbox, and a hook then starts the work automatically. *When:* When plans drift down a delegation chain and you want one control point before any action runs.
- **Force delegation through a CLI harness** — Expose the dispatch path as CLI commands wrapped in skills, so the orchestrator can only delegate rather than do the task itself. *When:* When an orchestrator keeps doing worker tasks directly instead of dispatching them.
- **Git-based context sync with per-machine partitions** — Commit and push context files between machines and trigger pulls over SSH. Keep machine-specific state in per-machine directories and change shared state only through pull requests. *When:* When several machines must share agent context without silently diverging.
- **Single always-on control plane and chat router** — Send every machine's review requests to one gateway on an always-on host. Use one chat bot per machine so the phone can drive the whole fleet. *When:* When laptops sleep and no single machine should be the place where approvals or control live.
- **Boot command that restores the fleet from state files** — One command brings all agents back up after a crash or reboot, because all their state is already on disk. *When:* When machines can lose power or restart and in-flight jobs must resume without manual rebuilding.

## Numbers
- Three machines (MacBook, Linux A for long-running coding, Linux B for short-lived side projects), all under one control plane. ([0:00](https://youtu.be/4kYl2_mqmnQ?t=0))
- Four to six live agent contexts in front of him before the design broke down, which he calls one human in three roles. ([1:22](https://youtu.be/4kYl2_mqmnQ?t=82))
- Five named failures in the multi-machine move: orchestrator doing work itself, crowded panes, out-of-memory swap, git credential collisions, and laptop power loss. ([4:05](https://youtu.be/4kYl2_mqmnQ?t=245))
- Four unsolved problems: cross-machine consistency, local-only tools, secure credential handoff, resource management. ([7:57](https://youtu.be/4kYl2_mqmnQ?t=477))
- No benchmarks, latencies or cost figures are given. The talk is an experience report, and its numbers are counts only. ([0:00](https://youtu.be/4kYl2_mqmnQ?t=0))

## Hot takes
- Compacting a long agent context is worse than resetting and reloading from files written by the agent, because you cannot control what survives compaction.
- An agent's state should live in files, not in the model, so a crash or context wipe does not lose the work.
- Infrastructure for agents should be built by agents: his review gateway was built by an agent team inside the fleet.
- The controller must never sit on a machine that can sleep, so the approval point should be an always-on box.
- Do not rebuild compute, secrets and tool placement for agents; stack Kubernetes underneath and build only the orchestration layer.

## Tools mentioned
Claude Code, tmux, tmux capture-pane, SSH, Git, Discord, MCP servers, Kubernetes, Linux, macOS

## Relevance to our work
- **prosharness** (3/3): ProsHarness wraps Claude Code for checkpoint/resume and phone-driven approvals. The talk covers the same ground: file-based state with reset-and-reload instead of compaction, a blocking approval gate, a boot command that resumes work after a crash, and Discord as a phone router. → *Test ProsHarness resume by clearing the context and restarting from only the handoff and history files, as described at 2:38, and check whether the checkpoint files alone are enough to continue.*
- **agentos** (1/3): Speaker's per-machine placement and declare-needs-not-location idea touches AgentOS's self-hosted infra, but the talk gives no infra code or measurements. → *Skim the 'declare what an agent needs, let the scheduler place it' section (7:57) before designing multi-machine placement for AgentOS.*
