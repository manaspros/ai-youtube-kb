# A Genius With Amnesia - Victor Savkin, Nx

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jVjt-2g8NMY` · [watch](https://youtu.be/jVjt-2g8NMY) · **date:** 2026-07-18 · **length:** 20:00 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Victor Savkin · **orgs:** Nx, GitHub
- **topics:** coding-agents, memory, agent-architecture · **tags:** multi-repo, dependency-graph, session-replay, meta-harness, handoff, episodic-memory, CI-coordination, Polygraph, Nx

> Victor Savkin (Nx) argues coding agents are limited by seeing one repo and forgetting past sessions, and shows Polygraph, a meta-harness that builds a cross-repo dependency graph and replays captured sessions on other machines.

## Summary
Savkin frames the core problem of coding agents as two limits: they are bound to one repo (space) and they forget every session (time), so the human becomes the memory. He walks through a four-repo UI change that needed seven separate explanations to ship and to fix a later bug. He argues the fix is to give the agent a model of the whole organization's work: a graph of repos, packages, APIs and agent sessions. His product, Polygraph, is an agent-agnostic meta-harness that builds this graph from repo metadata without changing any repo, then starts multi-repo sessions, coordinates CI across the resulting PRs, and captures session traces. Those traces let a teammate resume the exact state on another machine with another agent, with the same SHAs and history. The demo shows a three-repo change made from one instruction, and repo selection driven by intent rather than by hand. The talk is part architecture argument and part product pitch, so the reusable ideas matter more than the tool.

## Key ideas
- **Agent limits are spatial and temporal: one repo at a time, and no memory between sessions.** — The human ends up as the memory. A four-repo change (UI library, two consumers, platform) took seven explanations, and a bug a week later needed the original change re-explained. The speaker's framing is that the agent sees one small fraction of the code and forgets everything. ([0:04](https://youtu.be/jVjt-2g8NMY?t=4))
- **Writes are repo-bound too, so downstream breakage goes undetected.** — The agent cannot validate consumers or update them in the same pass, even when it already has the information. Changing something across 20 repos means explaining it 20 times, which costs developer time and tokens. ([2:50](https://youtu.be/jVjt-2g8NMY?t=170))
- **Model the organization's work as a graph of repos and agent sessions.** — Repos depend on each other, and sessions relate to repos and to other sessions. The speaker says the agent should see this graph, not a single session. ([4:49](https://youtu.be/jVjt-2g8NMY?t=289))
- **Build the cross-repo graph from metadata, outside the repos.** — Extract what each repo, and each project in it, produces and consumes (packages, APIs), with no code changes in those repos. Feed that to the harness so the agent can work as if there is one codebase. ([6:21](https://youtu.be/jVjt-2g8NMY?t=381))
- **Treat multi-repo CI and PRs as one unit of work.** — When CI fails in one repo of a session, the system decides whether the consumer needs a patch or the producer is wrong. The session then groups the resulting PRs and their CI status. ([8:27](https://youtu.be/jVjt-2g8NMY?t=507))
- **Capture intent, repos, PRs and agent traces so any session can be restored.** — A collaborator resumes a session on their own machine, with a different agent, at the same repo SHAs and with the trace primed. The speaker uses this for PR review questions: resume the author's session instead of asking them. ([9:29](https://youtu.be/jVjt-2g8NMY?t=569))
- **Select repos from intent, and reuse prior sessions as a best-practice template.** — Instead of picking repos by hand, the agent finds the repos that depend on a library version, or finds past sessions by other engineers on similar work. This is offered as a way to keep cross-repo implementations consistent. ([16:04](https://youtu.be/jVjt-2g8NMY?t=964))

## Techniques
- **Out-of-band cross-repo dependency graph** — Crawl repo metadata (packages produced and consumed, APIs produced and consumed) for every repo a user can reach, without changing those repos. Store it as a graph that agents query to find related repos. *When:* Many repos with package or API coupling, where agents need to know consumers before editing a producer.
- **Multi-repo session as one unit of work** — One session holds the plan, the repos involved, the PRs, and CI for each. CI failures are triaged across repos to decide whether the consumer or the producer changes. *When:* A single change has to land in several repos together and must pass CI in each.
- **Session state replay for handoff** — Record the user's intent, repo list, exact SHAs, PRs and full agent trace. Rebuild the same checkout and agent setup on another machine, then prime the agent with the trace. The new agent can be a different one. *When:* Handing work to a teammate, reviewing a PR by continuing the author's session, or resuming work after a machine change.
- **Intent-based scope selection** — Give the agent a goal such as 'every repo that pins this library version' and let the graph pick the repos, instead of selecting them manually. *When:* Changes whose blast radius is unknown or spans many repos.
- **Agent-agnostic meta-harness** — Wrap existing CLI agents (Claude, Codex) rather than building an agent. The harness sets up repos, dependencies and agent connections, and the user works as if in one repo. *When:* Teams use more than one coding agent and need a common setup and state layer.

## Numbers
- The illustrative four-repo change needed seven separate explanations to the agent, including a later bug fix. ([0:04](https://youtu.be/jVjt-2g8NMY?t=4))
- A change across 20 repos means re-explaining it 20 times with the current workflow (illustrative). ([3:47](https://youtu.be/jVjt-2g8NMY?t=227))
- Speaker's own graph covers about 300 owned repos plus thousands of open-source dependencies. ([7:24](https://youtu.be/jVjt-2g8NMY?t=444))
- The live demo used a three-repo GitHub setup (back-end, front-end and one more). ([9:29](https://youtu.be/jVjt-2g8NMY?t=569))
- The speaker describes his usual PR review flow as resuming the author's session and asking the agent, instead of asking the person. ([17:08](https://youtu.be/jVjt-2g8NMY?t=1028))

## Hot takes
- An agent that sees one repo and forgets its past work is a genius with amnesia, and the human ends up as its memory.
- The right fix is to give agents a model of the whole organization's work (repos plus sessions), not a bigger context window for one session.
- Resuming a teammate's agent session on your machine is a better way to review a PR than asking the author questions.

## Tools mentioned
Polygraph, Nx, Claude Code, Codex, GitHub

## Relevance to our work
- **prosharness** (2/3): Resuming a run on another machine at the same SHAs with its trace primed is close to ProsHarness checkpoint/resume and the phone-approval flow. → *Compare the ProsHarness checkpoint format against this talk's replay model: does a checkpoint pin repo SHAs and the full agent trace so it can be resumed on another machine?*
- **agentos** (1/3): Session trace capture and provenance are relevant to MemoryMesh's cross-session memory, but the talk does not give benchmarks or a storage design. → *Check whether MemoryMesh provenance can record the repo SHA or workspace state each agent trace ran against, so a past session can be reconstructed later.*
- **general** (1/3): The framing of repeated re-explanation as a memory failure is a useful lens for context engineering, but it is mostly a product argument. → *Log how often a single change is re-explained across sessions in daily use, and use that as the baseline for any persistence work.*
