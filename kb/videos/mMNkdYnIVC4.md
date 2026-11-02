# Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `mMNkdYnIVC4` · [watch](https://youtu.be/mMNkdYnIVC4) · **date:** 2026-09-18 · **length:** 16:56 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** James Zou · **orgs:** Together AI, Stanford
- **topics:** agent-architecture, evals, multi-agent, training-finetuning-rl · **tags:** environment design, verifier, agent collaboration, competition leaderboard, kissing number, GPU kernels, benchmark shortcuts, DSGym, synthetic trajectories, small models, Einstein Arena

> James Zou (Together AI, Stanford) argues agents should be given designed environments with verifiers, incentives and shared infrastructure instead of fixed workflows, citing Einstein Arena results and the DSGym data-science benchmark.

## Summary
The speaker argues that the way to get more from capable agents is to design the environment they work in (infrastructure, incentives, guardrails, resources) rather than scripting workflows, since workflows cap creativity. The first example is Einstein Arena, an agent-native platform where any agent can join (humans must solve a proof-of-AI puzzle), pick curated open science problems that have deterministic verifiers, and post real-time scored solutions on a leaderboard with a discussion forum. Within weeks of its launch, agents reportedly beat the best known results on 11 problems, including a kissing-number bound in 11 dimensions (604 spheres), which the speaker says needed multiple agents building on each other's solutions. The same arena, with a compile-and-benchmark verifier, was used for GPU kernel optimization, with personas (profiling, memory, precision) and speedups of up to about 2x on production kernels that Together AI now uses. The second example is DSGym, a data-science environment with over 1,000 tasks, where the speaker shows many existing benchmarks can be solved 20-50% of the time without touching the data, so they built a shortcut-free set and found frontier models score under 50%. Execution-verified trajectories from DSGym were then used to fine-tune small open models that reach best-in-class open-source results on these tasks and can run on a laptop. The talk is short on methodology detail and the arena results are self-reported, but the verifier-first design and shortcut audit are concrete.

## Key ideas
- **Design environments, not workflows** — Specify where the agent works and what incentives, infrastructure, guardrails and resources it has, then let behaviour emerge. Scripted workflows limit the creativity of stronger agents. ([0:12](https://youtu.be/mMNkdYnIVC4?t=12))
- **Agent-native arena with verifiers** — Agents read a skill file and enter freely; humans must pass a puzzle to get in. Problems are chosen because a human research community cares about them and they have a deterministic verifier that scores each submission in real time. ([2:34](https://youtu.be/mMNkdYnIVC4?t=154))
- **Collaboration and competition in one loop** — A forum lets agents ask for help and share approaches, a leaderboard shows everyone's scores, and agents can download and refine each other's solutions. The speaker reports new best-known results on 11 problems within a few weeks of launch. ([4:01](https://youtu.be/mMNkdYnIVC4?t=241))
- **Lineage of refinement beats single-agent search** — The kissing-number result (604 spheres in 11 dimensions, beating 593) came from a traceable chain of agents refining each other's constructions. The speaker says no single agent could do it alone. ([6:47](https://youtu.be/mMNkdYnIVC4?t=407))
- **Same arena, different verifier, for kernel speedups** — Swapping the verifier for compile, benchmark and correctness testing turns the arena into a kernel optimizer. Agents with different personas (profiling, memory, precision) collaborate and compete. ([9:29](https://youtu.be/mMNkdYnIVC4?t=569))
- **Many benchmarks can be gamed without the data** — On several popular data-science benchmarks, 20-50% of tasks could be solved without looking at the underlying data. The speaker treats this as a major flaw and built DSGym tasks with that check in mind. ([11:50](https://youtu.be/mMNkdYnIVC4?t=710))
- **Execution-verified trajectories to train small models** — DSGym generates agent trajectories checked by actually executing the code, then fine-tunes small open models. The speaker says these reach best-in-class open-source results on the tasks and run locally. ([14:19](https://youtu.be/mMNkdYnIVC4?t=859))

## Techniques
- **Verifier-first problem curation** — Choose tasks that have a deterministic, automatic scorer (math constructions, compile+benchmark for kernels, held-out evals for data science) and a human community that already cares about them. Score every submission in real time and publish a leaderboard. *When:* When you want agents to iterate on open-ended problems without a human grading each attempt.
- **Agent-native onboarding** — Publish a skill file the agent can read to join and act. Gate human entry with a puzzle that only an agent is likely to solve, so the population stays agent-only. *When:* When the environment is meant for autonomous agents rather than humans in the loop.
- **Persona-differentiated agents** — Give agents different roles or priors (profiling focus, memory focus, precision/tensor focus) so they cover different parts of the search space and build on each other's work. *When:* For optimization problems with several distinct bottlenecks, such as GPU kernel tuning.
- **Shortcut audit before trusting a benchmark** — Run the agent with the underlying data withheld and count how many tasks it still solves through reasoning or leakage. Drop or fix tasks that pass without the data. *When:* Before using any internal or public data-science or analysis eval to make decisions.
- **Execution-verified trajectory generation** — Let agents attempt tasks in a unified execution layer (many parallel Docker containers), keep only trajectories whose code actually runs and passes, and use them as fine-tuning data for a small model. *When:* When you want a cheap, local model for a narrow agent task and have a verifiable task set.

## Numbers
- Agents reached new best-known solutions on 11 open problems within a few weeks of the arena launch (around March 2026, per speaker) ([4:01](https://youtu.be/mMNkdYnIVC4?t=241))
- Kissing number in 11 dimensions: about 440 (1980s), 582 (later), 592 (2022, mathematician), 593 (DeepMind, following year), 604 (agent collaboration within a few days) ([6:47](https://youtu.be/mMNkdYnIVC4?t=407))
- Production GPU kernels optimized by arena agents reach up to about 2x speedup over previous state of the art, and the kernels are already used in production at Together AI ([9:29](https://youtu.be/mMNkdYnIVC4?t=569))
- On popular data-science benchmarks, 20% to 50% of tasks can be solved without using the underlying data ([12:50](https://youtu.be/mMNkdYnIVC4?t=770))
- DSGym has over 1,000 tasks across dozens of scientific domains; frontier models score under 50% accuracy ([12:50](https://youtu.be/mMNkdYnIVC4?t=770))
- Small open models fine-tuned on DSGym execution-verified trajectories reach best-in-class open-source results on these tasks ([14:19](https://youtu.be/mMNkdYnIVC4?t=859))

## Hot takes
- Designing workflows and harnesses limits strong agents; designing the environment lets creativity and capability emerge.
- Many popular data-science benchmarks are largely solvable without the data, so their scores overstate agent skill.
- Agent collaboration, not a single stronger agent, is what produced the 604-sphere result.

## Tools mentioned
Docker

## Relevance to our work
- **general** (2/3): The shortcut audit (solve the task without the data) is a cheap check for any agent eval, and the entity-resolution rule baseline is at risk of the same problem. → *Run a shortcut audit on the entity-resolution dev set: measure how many pairs a trivial string or rule baseline gets right without the model, and flag tasks that are too easy.*
- **agentos** (1/3): Crucible and SkillForge could use the environment-plus-verifier pattern, and DSGym-style trajectories suit the local-model goal, but the talk gives no implementation detail. → *Read the DSGym paper for how execution-verified trajectories are filtered, then decide whether SkillForge telemetry can be filtered the same way for a small local model.*
- **prosharness** (1/3): The persona-based parallel agents for kernel work map onto ProsHarness subagent or critique loops, but the talk offers no evidence that personas beat a generalist. → *Try a plan-critique run with three subagents that have distinct priors (for example, profiling, memory and precision reviewers), and compare against one generalist run on the same task.*
