# Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `xs-ob87TTzg` · [watch](https://youtu.be/xs-ob87TTzg) · **date:** 2026-09-20 · **length:** 1:00:47 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ignacio Martinez · **orgs:** Oracle
- **topics:** memory, agent-architecture, context-engineering, skills-self-improvement · **tags:** agent-harness, agent-memory, files-vs-databases, context-rot, skill-promotion, toolbox-pattern, agent-loop, model-routing, oracle-database, oracle-agent-memory-package, hnsw, git-worktrees, continual-learning, semantic-layer

> Oracle workshop on agent harness design: a 30-minute framework for agent memory (files vs databases, memory types, context rot, skill promotion), then a hands-on notebook build, with heavy Oracle product promotion.

## Summary
Ignacio Martinez (Oracle) frames an AI agent as a frozen model plus a harness, and argues that the harness is where engineers can make non-deterministic model output reliable. He walks through the data layer under an agent: gateway/MCP, memory, semantic layer, retrieval and context. He argues that files and databases are both needed, with short-term state in files and promoted long-term facts in a structured store. The talk covers memory types (short-term, long-term, shared, episodic, procedural), context rot, and a "semantic layer" of tribal knowledge the model needs spelled out. For the agent loop he describes per-iteration context assembly and retrieving tools and skills only when needed, with a bounded retry budget. The continual-learning section covers context-space changes (skill promotion by distillation) as the cheapest route to behavior change. The second half is a Codespaces notebook workshop built around Oracle's converged database, Oracle Agent Memory Package and OCI GenAI, so treat vendor claims as unverified.

## Key ideas
- **An agent is a frozen model plus a harness; the model is rented and the harness is where engineers have control.** — He defines the harness as everything around the model needed to turn non-deterministic output into reliable, repeatable results. He says model weights almost never change for practitioners, so the harness is the lever. ([9:54](https://youtu.be/xs-ob87TTzg?t=594))
- **Files versus databases is a false choice; use both in a hybrid.** — Files match model instincts and are easy to append to, but they lack transactional consistency when many agents write at once, and they have no hybrid search or backups. Databases give ACID, replication and vector search. His suggested split: short-term state in files, and promote durable items such as user preferences into a structured store. ([20:48](https://youtu.be/xs-ob87TTzg?t=1248))
- **Parallel agents writing files need isolation, and he suggests git worktrees as the workaround.** — Each agent works in its own worktree and merges to main when done. This is presented as a workaround for missing transactional file writes, not a full fix. ([18:27](https://youtu.be/xs-ob87TTzg?t=1107))
- **Memory has types: short-term, long-term, shared, episodic and procedural.** — Short-term memory is ephemeral (e.g. a coding agent's to-do list). Episodic memory is past conversations. Procedural memory is workflows that worked and can be reused. Shared memory is what a sub-agent and its parent, or collaborating agents, exchange. ([26:00](https://youtu.be/xs-ob87TTzg?t=1560))
- **Context rot: more tokens in context means less attention per item, so keep the window small.** — He says the context window is only a form of short-term memory, and that attention degrades as it fills. He claims the attention matrix scales quadratically with length, which he uses to justify minimising context. He treats this as a reason to build memory outside the window. ([28:53](https://youtu.be/xs-ob87TTzg?t=1733))
- **The semantic layer is the agent's 'umwelt': the unstated institutional knowledge a model lacks.** — Colleagues share context that never gets said. An agent needs data modelling, query conventions and metadata made explicit. He frames this as the semantic layer that must be captured. ([34:25](https://youtu.be/xs-ob87TTzg?t=2065))
- **Assemble context on every agent-loop iteration and load tools and skills only when needed.** — The loop is observe, reason, act, and must be failure-resistant. Tools and skills are stored in an index (toolbox or skillbox pattern) and pulled in per iteration, then dropped if not relevant. ([37:09](https://youtu.be/xs-ob87TTzg?t=2229))
- **Continual learning can happen in context space, which is the cheapest of three routes; skills can be promoted through distillation.** — The three routes are weights, representations (embedding and reranking models) and context. A workflow that succeeded over hours can be stored, then distilled into a better skill.md. The old version is retired and the new one takes its place. ([38:39](https://youtu.be/xs-ob87TTzg?t=2319))
- **Bound the retry loop with a patience (hysteresis) budget tuned per model, and route by problem difficulty.** — For the model he used, he found 8 to 12 tool calls before giving up to be a reasonable cutoff. Hard problems go to a frontier model and easy ones to a small open model. He expects a mix of small specialist models behind a router. ([56:15](https://youtu.be/xs-ob87TTzg?t=3375))

## Techniques
- **Hybrid storage split** — Keep short-term and scratch state as files. When an item needs to persist (e.g. a user preference), promote it into a structured DB with transactions and vector search. *When:* Several agents read and write state concurrently, or durable facts must survive crashes and be searchable.
- **Per-agent git worktrees for file edits** — Each agent edits in its own worktree and merges to main when its task finishes. *When:* Many agents edit the same repo or file set and you lack transactional file writes.
- **Context card** — Compact a conversation into a structured object: topics to orient the model, a summary and current intent, facts/preferences/memories, open questions (episodic), and recent messages. Assemble it per call. *When:* Long-running sessions where raw history would cause context rot.
- **Toolbox / skillbox index with vector retrieval** — Store tool and skill descriptions in a vector index (HNSW). Retrieve only the relevant ones per iteration and place them in context, dropping them when no longer relevant. *When:* The number of tools or skills is too large to load upfront.
- **LLM-enhanced tool descriptions** — Rewrite each tool or skill description with an LLM so that similar tools from different sources separate better in vector search. *When:* Retrieval confuses tools with similar descriptions.
- **Patience (hysteresis) budget for agent loops** — Set a maximum number of tool calls per task, tuned to the model (he used 8 to 12). Stop, or escalate, when it is exhausted. *When:* Agent loops that can spin on hallucinated or failing tool results.
- **Skill promotion by distillation** — After a multi-hour workflow succeeds, store the trace, distill it into an improved skill.md, retire the old version and replace it. *When:* Repeated personal or team workflows where you want skills to improve with use.
- **Difficulty-based model routing** — A router sends hard problems to a frontier model and easy ones to a small open-weights model. *When:* Mixed-difficulty workloads where cost matters.

## Numbers
- Workshop has 19 to-dos; the intro was about 30 minutes and the hands-on part about 1.5 hours. ([48:16](https://youtu.be/xs-ob87TTzg?t=2896))
- Tool-call cutoff of 8 to 12 calls before giving up, for Grok 4.1 Fast Reasoning. One run found the answer in 2 calls, another took 16. ([56:15](https://youtu.be/xs-ob87TTzg?t=3375))
- Demo SQL question ran 16 steps, including a recovered error, before answering. ([49:49](https://youtu.be/xs-ob87TTzg?t=2989))
- Typical tool counts are said to stay under about 100 to 1,000, and tool-retrieval cost is claimed to be negligible at that scale. ([52:25](https://youtu.be/xs-ob87TTzg?t=3145))
- Hypothetical pricing example: a router vendor charging 10% of the tokens it saves. ([57:26](https://youtu.be/xs-ob87TTzg?t=3446))
- Attention cost is claimed to scale quadratically with context length (speaker's claim, not measured). ([28:53](https://youtu.be/xs-ob87TTzg?t=1733))

## Hot takes
- The model is the frozen part of the reasoning; engineers should focus on the harness.
- Files versus databases is a false choice; use both.
- The context window is just short-term memory and should be kept as small as possible.
- The future is a mixture of small, specialised models routed per problem type.
- Agent memory should make repeated problems easier for engineers too, not just for agents.

## Tools mentioned
Oracle Database (converged: JSON, relational, spatial, graph, vector), Oracle DBFS, Oracle Agent Memory Package (OAMP), LangChain Oracle DB integration, OCI Generative AI service, GitHub Codespaces, Grok 4.1 Fast Reasoning, HNSW vector indexes, git worktrees, Python 3.12 notebook

## Relevance to our work
- **agentos** (2/3): The talk's split of short-term files, long-term structured store, shared memory, and episodic versus procedural memory maps onto MemoryMesh's tiers. The file-to-DB promotion step is a concrete design option. → *Compare MemoryMesh's tiers against this taxonomy. Prototype a promotion step that moves durable facts from a scratch file store into pgvector, and check how it handles concurrent writers.*
- **agentos** (2/3): Skill promotion by distillation (promote a successful workflow, distill it, retire the old version) is a candidate answer to SkillForge's open question on skill-worthiness. The talk gives no success signal, so that gap remains. → *Sketch a SkillForge promotion loop: a trace that succeeded becomes a distilled candidate skill.md, and the old version is retired. Define the success signal yourself first.*
- **prosharness** (2/3): The bounded retry budget (8 to 12 tool calls, tuned per model) and per-iteration context assembly both map onto the harness loop and checkpoint/resume work around Claude Code. → *Add a per-task tool-call budget to the ProsHarness loop, record how many calls each task used before success or give-up, and pick the cutoff from that data.*
- **general** (2/3): The context-engineering points (context rot, loading tools and skills only when needed, rebuilding context each iteration) apply directly to coding-agent and subagent workflows. → *Measure context size per loop iteration in a coding-agent run, and move unused tool and skill definitions behind on-demand retrieval.*
- **general** (1/3): Difficulty-based routing (cheap model for easy items, frontier model for hard) is relevant to the cheap-model pipelines, but the talk gives no measured results. → *For a mixed-difficulty ER or extraction batch, try routing easy cases to Haiku and escalating failures to a stronger model, then measure cost and accuracy against the single-model baseline.*
