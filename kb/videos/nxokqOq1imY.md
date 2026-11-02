# Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `nxokqOq1imY` · [watch](https://youtu.be/nxokqOq1imY) · **date:** 2026-09-18 · **length:** 24:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ameya Bhatawdekar · **orgs:** Braintrust
- **topics:** evals, observability, agent-architecture · **tags:** evals, pass-at-k, pass-hat-k, reliability, eval-flywheel, production-traces, failure-clustering, agent-architecture, workflow-graphs, react-loop, sre-agent-example

> Braintrust field CTO argues each agent architecture generation (single call, chain, ReAct loop, graph, product system) needs different evals, and that production traces should keep feeding the eval set.

## Summary
The speaker, Ameya Bhatawdekar (field CTO at Braintrust, auto-captioned as "Amir Bhattavdekar"), argues that AI systems are being re-platformed with each model generation, and that evals must change with the architecture. He walks through five stages: a single model call, a multi-step RAG chain, a ReAct-style loop, workflow graphs, and finally a product system with memory, sandboxes, and MCP/skills. Each stage adds failure surfaces that the previous eval style does not see. The loop era brought in run-to-run variance, so he recommends running each eval k times and reporting pass@k (capability) next to pass^k (reliability). He closes with a production flywheel: harvest traces, cluster failures (Braintrust's Topics feature), and turn new failure modes into eval cases. The talk is conceptual and vendor-framed, with almost no benchmark numbers.

## Key ideas
- **Architecture follows model updates, and evals have to follow the architecture.** — Old systems were built around model limits (for example weak tool calling). New models unlock capability only after re-architecture, and each new surface needs new evals. Evals are the durable asset that describes how the system should work. ([2:38](https://youtu.be/nxokqOq1imY?t=158))
- **Each architecture generation fails in different places, so the eval unit changes.** — A single call needs a golden set scored on the final answer. A RAG chain needs per-step evals (parser, retrieval, context use, synthesis). Graphs need node-level evals plus tests for branching and retry logic. ([6:16](https://youtu.be/nxokqOq1imY?t=376))
- **Loop agents need distribution-level evals, not single-run pass/fail.** — The same input can take different trajectories and still reach the right answer. Run each eval k times and look at the outcome distribution. ([14:22](https://youtu.be/nxokqOq1imY?t=862))
- **Use pass@k for capability and pass^k for reliability.** — pass@k asks whether the agent succeeds at least once in k runs, which measures what it can do. pass^k asks how many of k runs succeed, which measures how dependable it is. A high pass@k with a low pass^k means the system works sometimes. ([14:22](https://youtu.be/nxokqOq1imY?t=862))
- **Product-style agents have more failure surfaces than loop-level evals cover.** — Memory (within and across sessions), code-execution sandboxes, and MCP or skill directories add new failure points. Evals from the earlier generation give only partial coverage. ([15:43](https://youtu.be/nxokqOq1imY?t=943))
- **Static evals go stale unless production data feeds back into them.** — Many teams describe a production-to-eval flywheel but do not run it. Harvest failures from production, including ones you already expected and ones you did not, and turn them into eval cases. ([18:37](https://youtu.be/nxokqOq1imY?t=1117))
- **Cluster production data to find failure modes nobody anticipated.** — Braintrust's Topics runs cluster analysis across production traces to surface new failure categories. Teams can then add guardrails or evals for those categories, not just more examples of known failures. ([19:57](https://youtu.be/nxokqOq1imY?t=1197))

## Techniques
- **Architecture-matched eval suites** — Match the eval design to the architecture: final-answer golden sets for a single call, per-step evals for chains, node/branch/retry evals for graphs, and k-run distribution evals for loops. *When:* When you change the agent architecture or adopt a new model generation that changes how the system is built.
- **k-run pass@k and pass^k reporting** — Run each eval case k times. Report pass@k as a capability measure and pass^k as a reliability measure. *When:* For non-deterministic agent loops, where a single run gives a misleading signal.
- **Production failure clustering to harvest evals** — Cluster production traces by failure type. Review the clusters, then add new eval cases and guardrails for failure modes that existing evals miss. *When:* After shipping, or whenever the failure set is changing faster than your eval set.
- **Node-level and branch-level evals for graph workflows** — Test each node's contract, branch selection, and retry loops separately, in addition to end-to-end runs. *When:* When the agent is built as a workflow graph or state machine with hand-written branches.

## Numbers
- The talk gives no benchmark, cost, or latency figures. Its only concrete timing is a model release cadence of roughly every few months. ([1:11](https://youtu.be/nxokqOq1imY?t=71))
- A single-prompt-plus-golden-set eval style was common about three years before the talk. ([4:55](https://youtu.be/nxokqOq1imY?t=295))
- The ReAct loop became popular in late 2023 to early 2024. ([7:31](https://youtu.be/nxokqOq1imY?t=451))
- Workflow graphs were popular in late 2024 to early 2025. ([11:40](https://youtu.be/nxokqOq1imY?t=700))
- Tool calling and long-horizon planning improved noticeably in mid-to-late 2025, which made the ReAct loop viable again. ([13:08](https://youtu.be/nxokqOq1imY?t=788))

## Hot takes
- Architecture follows model updates, and evals have to follow the architecture.
- Most teams that describe an eval flywheel do not actually run it, so their evals are static.
- Reporting only pass@k hides unreliability. Pass^k is the number to watch for loop-based agents.

## Tools mentioned
Braintrust, Braintrust Topics

## Relevance to our work
- **agentos** (2/3): AgentOS has RAGAS evals and load tests but no distribution-level metric for agent runs. The pass@k vs pass^k split applies to the agent-facing layers (Crucible, SkillForge, EvolveCraft). → *Add a k-run mode to the agent eval harness that reports pass@k and pass^k per case, starting with the MemoryMesh or Crucible task suite.*
- **prosharness** (2/3): ProsHarness runs long Claude Code loops with checkpoint and resume. Reliability over repeated runs matters more than a single success, and the talk gives the metric for it. → *Run one checkpointed ProsHarness workflow k times on the same spec and record pass^k before trusting loops or schedules.*
- **general** (2/3): Gives a clear framing for how eval design should follow architecture changes, which applies across the recurring interest in agent evals and context engineering. → *Read Braintrust's Topics docs or the talk's flywheel section for the cluster-to-eval workflow, then compare it with the current eval plan.*
