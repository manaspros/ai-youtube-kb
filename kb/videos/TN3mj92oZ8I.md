# Building Self-Improving Agent Software Factories — Suraj Gupta, Warp

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `TN3mj92oZ8I` · [watch](https://youtu.be/TN3mj92oZ8I) · **date:** 2026-10-04 · **length:** 12:52 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Suraj Gupta · **orgs:** Warp
- **topics:** software-factory, skills-self-improvement, memory, token-cost-efficiency · **tags:** self-improving agents, outer loop, triage agent, GitHub PR review of skills, versioned memory store, provenance, model routing, best-of-k, cost control, Warp Oz

> Warp's Suraj Gupta on making agent software factories self-improve through outer-loop skill edits gated by PR review, agent-scoped versioned memory, and rule-based model routing for cost.

## Summary
Suraj Gupta, who leads harness development at Warp, argues that software factories (automated pipelines that take work from triage to production) should also get better over time, not just the agents inside them. He covers three levers: skills, persistent memory, and model routing. For skills, an outer-loop agent watches an inner-loop triage agent, gathers feedback such as thumbs up or down, comments and employee replies, and then edits the skill and opens a pull request so a human reviews each change. For memory, a per-agent fact store is filled by an outer-loop agent with root-cause facts from past runs. Each memory links to its source run and can be versioned, edited or deleted by a human, and the agent reports which memories it used on a run. For routing, he says running every simple task (triage, simple CI fixes) on Opus is too expensive, so Warp offers auto models and lets teams write rules that map task classes to specific models. He admits rule-writing is still more art than science. Warp's next step is customer-facing evals that compare models on each team's own task classes, and the current method is a best-of-k run across several models per prompt. The talk is short and product-tinged, with one example per lever and no measured cost or latency data.

## Key ideas
- **Three concrete levers make a factory self-improve: skills, persistent memory, and model routing.** — The talk frames self-improvement around procedural memory (skills), cross-run fact memory, and choosing the right model per task, which together make the factory cheaper and faster over time. ([1:37](https://youtu.be/TN3mj92oZ8I?t=97))
- **An outer-loop agent can edit an inner-loop agent's skill from feedback, with a PR as the gate.** — The inner agent applies the skill (e.g. issue triage). The outer agent reviews its decisions and feedback signals (thumbs up or down, user comments, employee comments), synthesizes changes, and opens a PR. Git gives a history of how the skill changed, and human review stops the outer loop from making the agent worse. ([3:04](https://youtu.be/TN3mj92oZ8I?t=184))
- **Agent-scoped persistent memory stops agents from re-deriving the same root cause.** — An outer-loop agent extracts facts, learnings and outcomes from runs into a fact store attached to the agent. Memories can be versioned, traced to their source run, and edited or deleted by humans. Warp says memory works across harnesses, including its own, Codex and Claude Code. ([5:57](https://youtu.be/TN3mj92oZ8I?t=357))
- **Running every simple task on the top model is a cost problem that routing must solve.** — Triage and simple CI fixes on Opus are called prohibitively expensive at factory scale. Warp offers auto models that route for Pareto efficiency, and lets teams define rules that map task classes to specific models. ([8:49](https://youtu.be/TN3mj92oZ8I?t=529))
- **Model routing rules are more art than science today, so the next step is task-specific evals.** — Rules are hand-written now. The planned change is customer-facing evals where a team picks what it cares about and tests whether a cheaper model such as Haiku or GLM beats Opus on its own class of issues, instead of relying on public benchmarks. ([10:20](https://youtu.be/TN3mj92oZ8I?t=620))
- **Best-of-k runs across models reveal which task classes a cheaper model can handle.** — For each prompt, Warp runs several agents on different models and records the winners per task class. The example given is that UI tasks do well on GLM, so they do not need Opus. ([11:53](https://youtu.be/TN3mj92oZ8I?t=713))

## Techniques
- **Outer-loop skill improvement with PR gate** — Run an observer agent over the inner agent's decisions and feedback signals (reactions, comments, maintainer replies). It edits the skill file and opens a PR, so every change is versioned in git and reviewed by a human before it applies. *When:* A recurring agent workflow (e.g. issue triage) whose skill goes stale as humans give feedback and the codebase changes.
- **Agent-scoped fact memory with provenance** — An outer-loop agent extracts facts and outcomes from each run into a store attached to one agent. Each memory links to its source run. Humans can version, edit or delete memories, and the agent reports which memories it used on a later run. *When:* An agent repeatedly does root-cause analysis or context gathering on similar issues and wastes tokens rediscovering the same facts.
- **Rule-based model routing by task class** — Write config rules that map classes of work (e.g. database migrations, runbooks and API docs) to specific models, instead of pinning all agents to one model. *When:* A factory runs many agents with mixed difficulty and the top model's cost is too high for simple tasks.
- **Best-of-k model sampling to learn routing** — For each prompt, run agents on a set of models in parallel. Record which model wins for each task class, then use those results to write the routing rules. *When:* You want routing decisions based on your own workflows instead of public benchmarks, and can afford extra parallel runs while you learn.

## Numbers
- Warp's agentic development environment has about 1 million active users. ([0:12](https://youtu.be/TN3mj92oZ8I?t=12))
- A Sentry triage agent reused 5 stored memories on a later run to speed up root-cause analysis (a single example, no timing or token data given). ([7:23](https://youtu.be/TN3mj92oZ8I?t=443))
- No benchmark, cost or latency figures are given. The talk is a 12:52 demo of Warp's approach. ([0:00](https://youtu.be/TN3mj92oZ8I?t=0))

## Hot takes
- Outer-loop agents should not write skill changes directly. Every change should land as a reviewed git PR, because an unreviewed self-edit can make the inner agent worse.
- Running triage and simple CI-fix agents on Opus is a cost trap that many organizations have already been burned by.
- Model routing is still more art than science. Teams need evals on their own task classes rather than public benchmarks.

## Tools mentioned
Warp, Oz (Warp cloud agent platform), Sentry, GitHub, Codex, Claude Code, Opus, Haiku, GLM, Qwen

## Relevance to our work
- **agentos** (2/3): MemoryMesh already has tiered cross-session memory with provenance, and Govrix Scout has strategy routing. This talk describes the same two things with a human review and edit loop, plus routing rules set per task class. → *Add a review step to MemoryMesh: each memory links to its source run, humans can version or delete it, and each run records which memories it used. Then test whether task-class routing rules in Scout can be learned from best-of-k runs.*
- **prosharness** (2/3): ProsHarness already has skill ranking and checkpoint/resume. An outer loop that reads run feedback and proposes skill edits as PRs fits its design. → *Prototype a ProsHarness job that reads finished-run logs and feedback, drafts an edit to the relevant skill, and opens a git PR for review before the skill changes.*
