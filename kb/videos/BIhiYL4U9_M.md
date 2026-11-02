# From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `BIhiYL4U9_M` · [watch](https://youtu.be/BIhiYL4U9_M) · **date:** 2026-10-10 · **length:** 18:20 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Anders Swanson · **orgs:** Oracle
- **topics:** memory, rag-retrieval, context-engineering, security-guardrails · **tags:** agent memory, hybrid retrieval, memory governance, feedback loop, poison memory, episodic memory, procedural memory, multi-model database, Oracle AI Database, context cards

> Oracle's Anders Swanson argues agent memory should be a governed, typed database layer with redaction, hybrid retrieval, scoped access, and feedback loops, not files or bigger context windows.

## Summary
Anders Swanson, a developer advocate for Oracle AI Database, argues that context windows and scratchpad files are not memory, because useful work from one agent session is discarded and the next agent repeats it. He describes a memory loop: distill a session into a structured fact, redact and scope it, embed it, store it with a link back to the source transcript slice, retrieve it later through hybrid search, and record feedback on whether it helped. He splits memory into episodic, semantic, procedural and working state, and lists the storage fields he expects, including vector and full-text indexes, graph links, temporal validity and audit events. The talk covers failure modes he has seen with customers: stale facts, bad scope, poisoned memory, conflicting memories, over-recall, leakage and silent drift as the store grows. He concludes that feedback is what closes the loop, and that memory quality has to be measured. The talk is a vendor pitch for Oracle's multi-model database and its Python SDK, and it gives no benchmarks.

## Key ideas
- **Context windows and scratchpad files are not memory** — Work done in one session is thrown away, so the next agent rereads the same files and reruns the same queries. Bigger windows and compaction lose the useful signal. Files and grep do not scale to multi-tenant recall, and a file-based memory layer ends up as a home-built database. ([0:12](https://youtu.be/BIhiYL4U9_M?t=12))
- **Memory is a loop: form, recall, evolve, evaluate, govern** — Memories should be distilled facts, not raw transcript dumps. Recall should use hybrid search. The store needs consolidation, conflict resolution, temporal validity and feedback, plus governance on what gets written and who can read it. ([3:07](https://youtu.be/BIhiYL4U9_M?t=187))
- **Memory is typed: episodic, semantic, procedural, working state** — Episodic memory holds past events or transcript slices. Semantic holds facts, preferences and entities. Procedural holds reusable how-to rules, such as a build routine. Working state is short-term, time-limited, and can be promoted to another type. Each type can use different search methods. ([6:02](https://youtu.be/BIhiYL4U9_M?t=362))
- **Redact before embedding, then enrich, scope and link back to the transcript** — Strip PII and secrets first, so they never reach embeddings or enrichment. Then attach scope (agent, workflow, team, user, org), embed the content, and save an episode, which is the transcript slice that produced the memory, for provenance. ([8:01](https://youtu.be/BIhiYL4U9_M?t=481))
- **Hybrid retrieval fuses weighted search branches into a context card** — Run vector, lexical, entity or graph, and temporal or feedback branches in parallel. Weight each branch, merge the scores, threshold and rerank, then return the top K as a context card. Each result keeps its provenance, such as strong on vector and weaker on lexical. ([10:22](https://youtu.be/BIhiYL4U9_M?t=622))
- **Scope and staleness must be checked on both write and read** — Stale facts happen when the project changes, such as moving from npm to another build system. Bad scope can leak one user's memories to another. He says the system should expect stale facts rather than let them drift in quietly. ([11:49](https://youtu.be/BIhiYL4U9_M?t=709))
- **Feedback is what closes the memory loop** — Record whether each memory was helpful, stale, irrelevant or harmful. Demote harmful memories and promote useful ones. Memory quality has to be measured against correct retrieval and downstream usefulness. ([14:45](https://youtu.be/BIhiYL4U9_M?t=885))

## Techniques
- **Typed memory schema with per-type lookup** — Store memories as typed objects: episodic, semantic, procedural and working state. Give each object an ID, text, JSON tags, an embedding, a vector index, a full-text index, graph edges, temporal validity (valid-to, last used) and audit events (who created it, what it was used for). Pick the search method per type, such as exact ID match for facts. *When:* When one flat memory store is returning weak matches or mixing task types.
- **Write pipeline: redact, enrich, scope, embed, episode-link** — Run redaction first. Enrich the record with metadata, then apply scope (agent, workflow, team, org). Create the embedding and save an episode (transcript slice) linked to the memory. Apply organization policies at this step. Keep the memory record small: distilled content, metadata and embedding, with the transcript kept as a linked episode. *When:* Any time an agent runtime writes to a shared or multi-tenant memory store.
- **Weighted hybrid retrieval with fused scores and provenance** — Run separate query branches (vector similarity, full-text, entity or relational lookup, graph traversal, recency and feedback signals). Apply a tunable weight to each branch, merge into one score, threshold, rerank, and return top K as a context card that records which branches matched and how strongly. *When:* When pure embedding similarity misses exact facts or returns lexically close but off-task results.
- **Governance on write and on read** — Scope every memory to agent, workflow, team or user. Check scope when writing and again when reading. Add admin review and the ability to suppress stale or poisoned records. Treat content from untrusted sources as a possible durable prompt-injection vector. *When:* Multi-tenant deployments, or any agent that reads documents or web content it does not control.
- **Feedback signals that rank and promote or demote memories** — After the agent uses a retrieved memory, log an outcome: helpful, rejected, stale, irrelevant or harmful. Use the signals to adjust ranking, promote useful memories and suppress harmful ones. *When:* As soon as memories are retrieved in production, so quality can be measured instead of guessed.
- **Expose memory as a runtime function** — Let the agent runtime call read, write, feedback and admin endpoints through hooks, MCP servers or skills. The memory layer then talks to the storage database behind those endpoints. *When:* When the agent harness (Claude Code, Codex or similar) needs to query and update memory mid-session.

## Numbers
- No benchmarks or measured results are given. The only scale claim is qualitative: a memory system that works at about 1,000 records can degrade silently by 50,000 to a million records. ([14:45](https://youtu.be/BIhiYL4U9_M?t=885))
- Talk length is 18:20. ([0:00](https://youtu.be/BIhiYL4U9_M?t=0))

## Hot takes
- If you keep building memory on top of files, you are building your own database.
- Expect stale facts; don't let them drift in quietly.
- Redaction must run before embeddings and enrichment, not after.
- Without feedback signals, a memory layer falls over.

## Tools mentioned
Oracle AI Database, Oracle Python SDK for agent memory (speaker's; referenced, not shown), Claude Code, Codex, MCP, hooks, skills

## Relevance to our work
- **agentos** (2/3): L2A MemoryMesh already has hybrid retrieval (BM25 + pgvector), tiered memory, conflict resolution and provenance. The talk adds redact-before-embed ordering, episode links, per-memory audit events and helpful/stale/harmful feedback that feeds ranking, none of which the profile mentions. → *Compare MemoryMesh's write path against the talk's order (redact, scope, embed, episode link) and add a feedback-outcome field (helpful, stale, irrelevant, harmful) plus per-memory audit events to the schema.*
- **prosharness** (1/3): Checkpoint/resume covers long single runs. The talk's cross-session procedural memory overlaps only loosely with that, and it does not address checkpoint state. → *Read only if ProsHarness later stores reusable procedural memory across runs; no change needed now.*
