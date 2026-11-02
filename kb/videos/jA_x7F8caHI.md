# No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jA_x7F8caHI` · [watch](https://youtu.be/jA_x7F8caHI) · **date:** 2026-09-18 · **length:** 21:37 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Kay Malcolm · **orgs:** Oracle, Southern Company, OpenAI
- **topics:** memory, agent-architecture, multi-agent, enterprise-adoption · **tags:** agent memory, agent harness, shared context, team handoff, episodic memory, procedural memory, Oracle AI Database, memory broker, vendor pitch

> Oracle's Kay Malcolm argues that agent harnesses need shared, database-backed memory, using a five-type memory taxonomy and a team memory broker; mostly a product pitch for Oracle AI Database.

## Summary
The speaker, an Oracle outbound database product manager, says AI made individual developers faster but not her distributed team, because Git records code and not the agent context or intent behind it. A Netherlands engineer's Codex context did not reach the US team overnight, and repos diverged. She frames an enterprise agent as a model plus tools, context window, memory, retrieval and guardrails, with memory as the part that carries context across the harness. She lists five memory types (short-term, long-term, episodic, procedural, semantic) and argues that storing them across separate relational, JSON, graph and vector databases forces the agent to reconcile sources and burn tokens. Her proposed fix is one Oracle AI Database holding all these data types, plus a shared memory broker called Poly that tracks context per fork, branch and commit so teammates' agents can pick it up. The talk makes vendor claims (single-store support, scale, Oracle Agent Memory SDK) without benchmarks or failure cases, and the rest is a pitch for Oracle's LiveLabs, developer hub and always-free cloud tier.

## Key ideas
- **AI made individuals faster but not the team; the bottleneck moved to handoff and coordination** — Code checked in from one timezone arrived without the Codex session context, so the other timezone got code but not the reasoning. Git records code, not human or agent intent, so repos diverged and testing and validation still slowed the team. ([1:13](https://youtu.be/jA_x7F8caHI?t=73))
- **An enterprise agent is more than the model: tools, context window, memory, retrieval and guardrails make up the harness** — She uses an analogy: the model is the brain in a jar, the harness is the body, and memory is the central nervous system that carries context to the rest of the body. ([4:45](https://youtu.be/jA_x7F8caHI?t=285))
- **Agent memory splits into five types with different shapes** — Short-term is the session. Long-term persists across sessions. Episodic is what happened last time. Procedural is the tools and steps taken. Semantic is the facts. Each type needs a different kind of storage. ([6:57](https://youtu.be/jA_x7F8caHI?t=417))
- **Spreading memory across several specialised databases makes the agent reconcile them** — Relational, JSON, graph and vector stores cannot talk to each other. The agent has to work out which store is the source of truth, which is often wrong and costs tokens. ([12:23](https://youtu.be/jA_x7F8caHI?t=743))
- **Her vendor claim: one Oracle AI Database can hold all the memory data types** — She says relational, JSON, graph, vector and spatial data can live in the same table and partition, and maps each memory type to a model. The talk gives no benchmark or evidence for this. ([15:36](https://youtu.be/jA_x7F8caHI?t=936))
- **A shared memory broker keeps team agent context tied to repo state** — Her team's broker, Poly, keeps context for each fork, branch and commit, so one developer's agent context can be used by teammates' agents. Developers stay in control of the process. ([16:57](https://youtu.be/jA_x7F8caHI?t=1017))
- **Owning the harness means owning the memory; built-in chat memory fails at team scale** — She quotes Harrison Chase as saying that if you do not own your harness you do not own your memory. She calls built-in chat memory file-system-like and says it works for one user but breaks when the team grows. Her Oracle Agent Memory SDK can use a chosen LLM or a local model in a private container. ([18:22](https://youtu.be/jA_x7F8caHI?t=1102))

## Techniques
- **Five-type agent memory taxonomy** — Classify each piece of agent memory as short-term, long-term, episodic, procedural or semantic, then pick a store whose shape fits that type. *When:* Designing memory for an agent that must persist across sessions or steps.
- **Shared memory broker tied to repo state** — Capture agent context (decisions, steps taken, conversation state) and tag it with fork, branch and commit, so a teammate's agent can retrieve the context that goes with a given code change. *When:* Several developers or agents work on the same repo across timezones and need to hand off reasoning, not just code.
- **Keeping context alongside commits** — Store the agent session context next to the code change instead of relying on Git history alone, so the reasoning behind a commit is recoverable. *When:* Teams where code is generated by agents and reviewers need to know why a change was made.
- **Single-store consolidation for agent memory** — Keep relational, JSON, graph and vector memory in one database so the agent does not have to pick a source of truth across stores. *When:* The agent's queries span several data models. The talk gives no evidence that this beats a multi-store design.
- **Private local model for memory extraction** — Run the memory-extraction model in a private container instead of a hosted LLM, so conversation data stays inside the environment. *When:* Data cannot leave the environment or the team wants LLM choice.

## Numbers
- Team split across EMEA and US timezones; a Netherlands check-in at 4 a.m. reached the US team without its Codex context ([2:37](https://youtu.be/jA_x7F8caHI?t=157))
- Five memory types in the taxonomy (short-term, long-term, episodic, procedural, semantic); no benchmarks or latency or cost figures given ([6:57](https://youtu.be/jA_x7F8caHI?t=417))
- Speaker claims 40 million users for LiveLabs content built about six years earlier (self-reported, unverified) ([19:49](https://youtu.be/jA_x7F8caHI?t=1189))
- OCI Always Free promo: 3,000 emails per month and 200 GB storage, plus a free Oracle database and compute ([21:10](https://youtu.be/jA_x7F8caHI?t=1270))

## Hot takes
- If you don't own your harness, you don't own your memory.
- Git records code, not human intent.
- Built-in chat memory is file-system-like and works for one user but not at team scale.
- Agent memory belongs in one database, not spread across relational, JSON, graph and vector stores.

## Tools mentioned
Oracle AI Database 26AI, Oracle Agent Memory SDK, Codex, Claude, Git, Neo4j, Redis, OCI Always Free

## Relevance to our work
- **agentos** (2/3): The five-type memory taxonomy maps directly onto MemoryMesh's tiered cross-session memory, and the talk raises the question of whether memory needs several stores or one. → *Map MemoryMesh's tiers to the five memory types (short-term, long-term, episodic, procedural, semantic) and check which of these fit Postgres/pgvector and which would need Neo4j or another store.*
- **prosharness** (2/3): ProsHarness checkpoints long Claude Code runs. The talk's point that procedural and episodic memory need to survive a session and be shared with teammates applies directly. → *Store the steps taken and decisions made in a Claude Code run as procedural and episodic memory, keyed by branch and commit, so a resumed or teammate session can load them.*
- **general** (1/3): The team-handoff problem (code moves without intent) is general, but the talk gives no evidence beyond the speaker's anecdote. → *Read the Git-intent argument as a prompt to test whether recording agent decision logs with commits helps review; do not adopt Oracle's stack on the strength of this talk.*
