# Agent Memory Is Solved. Agent Learning Isn't. — Karthik Ranganathan, Yugabyte

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `9_oy4owGtPI` · [watch](https://youtu.be/9_oy4owGtPI) · **date:** 2026-10-06 · **length:** 20:36 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Karthik Ranganathan · **orgs:** Yugabyte
- **topics:** memory, multi-agent, context-engineering, observability · **tags:** agent-memory, shared-context, promotion-gate, provenance, resumability, data-pack, mcp, rag-tuning, token-cost, vendor-pitch

> Yugabyte's CEO argues agent memory is solved but cross-agent learning is not, and demos Mako, a private-to-shared context store where humans promote memories and provenance is traceable.

## Summary
The speaker, a Yugabyte co-founder, says per-agent memory works but learning across a group of agents is unsolved. He says handoffs through output files (MD, PDF) lose the reasoning and dead ends, so the receiving agent re-derives everything and burns tokens. He lists five misconceptions: more memory is not learning, shared files are not shared knowledge, RAG over everything is not quality, fine-tuning cannot persist lessons, and bigger context windows make context rot worse. He describes their failed attempts (a distributed RAG pipeline, per-agent Postgres, a headless backend with no human in the loop) and the tuning that followed. The product pitch is Mako, which stores private memories, promotes selected pieces to a shared space under human supervision, and records provenance and traces. A recorded, sped-up demo shows cross-session resumability and cross-IDE sharing via MCP tool calls. Most claims are vendor-side and the metrics are only partly specified, so treat the numbers as self-reported.

## Key ideas
- **Per-agent memory is solved, but learning across a group of agents is not, and single-agent memory infrastructure is not the same as what shared learning needs.** — The speaker frames the gap as an infrastructure problem: memory is extracted from a single agent's conversations and reused by that agent, while learning requires sharing across agents. ([0:08](https://youtu.be/9_oy4owGtPI?t=8))
- **Passing only the output of an agent to another agent loses the reasoning, the dead ends and the failed attempts, so the receiver re-derives the work at token cost.** — He compares it to a new team member who needs the project history; without it they re-argue settled decisions. ([2:33](https://youtu.be/9_oy4owGtPI?t=153))
- **Five misconceptions: more memory is not learning, shared files are not shared knowledge, RAG over everything is not quality, fine-tuning does not persist lessons, and a bigger context window makes things worse.** — He calls each one an architecture gap rather than a feature gap. Context rot is the stated reason larger windows fail. ([3:59](https://youtu.be/9_oy4owGtPI?t=239))
- **Shared context needs three properties: agents work on the same context, contributions are supervised (promoted) rather than open, and every fact can be traced to a source, person or conversation.** — He compares contribution to code review: not everyone can write to the shared context, and promotion is what makes it durable. ([4:55](https://youtu.be/9_oy4owGtPI?t=295))
- **Their own earlier designs failed (a shared knowledge base with a distributed RAG pipeline, per-agent tiny Postgres, a headless backend with no UI), and tuning the RAG stack one variable at a time improved results.** — Without a human in the loop they could not see what went wrong. Per-variable tuning from traces raised the reported scores and cut the context from about 7,000 chunks to about 1,000. ([6:24](https://youtu.be/9_oy4owGtPI?t=384))
- **Each memory is private by default and is promoted to a shared space one piece at a time, so access is fine-grained rather than whole-store.** — In the demo, a memory was invisible to another client until it was promoted, and then it became retrievable. A maintainer can still open a whole data pack. ([14:34](https://youtu.be/9_oy4owGtPI?t=874))
- **Human promotion decisions can serve as labeled examples of good memory for future self-improving orchestration, and decision traces down to tool calls can show whether the memory actually saved tokens.** — He says the trace lets a team check cost savings instead of assuming them. He presents training on promotions as a future direction, not something shipped. ([15:56](https://youtu.be/9_oy4owGtPI?t=956))
- **Shared incident memory stops many agents from repeatedly calling a service that is down, because the first agent to hit the failure records it for the rest.** — This is a proposed use case with no measured result in the talk. ([17:24](https://youtu.be/9_oy4owGtPI?t=1044))

## Techniques
- **Private-to-shared promotion gate** — Agents write memories to a private scope. A human or a supervised step promotes selected items into a shared scope, so only reviewed items become shared context. *When:* When several agents or people share context and unreviewed memory would add noise or cost.
- **Provenance on every memory** — Store the source (data source, person or conversation) for each extracted fact so it can be traced back before it is trusted or promoted. *When:* When shared context must be audited or when a wrong fact needs to be traced to its origin.
- **Scoped data packs with a skill-driven MCP interface** — Group memories into named packs. Expose create and add operations over MCP, and use a skill to tell the agent when to write, so calls are not made on every turn. *When:* When the same memory must be read from different IDE or chat clients under one account.
- **Cross-session resumability via shared memory** — Start a session, kill it, and start a new one. The new session first searches the stored conversation and then continues, so no project or memory toggle is needed. *When:* When work on a topic spans days or devices and re-deriving prior reasoning costs tokens.
- **One-variable-at-a-time RAG tuning with traces** — Change a single retrieval variable, re-run with tracing, and keep only changes that improve the metric. Track context chunk count as well as precision. *When:* When a RAG pipeline built from best-of-breed components performs poorly and the cause is unknown.
- **Trace-based token accounting** — Inspect stored conversation traces down to the tool call to measure whether a retrieval avoided repeated token spend. *When:* When a team wants evidence that shared memory reduces cost rather than assuming it.

## Numbers
- Initial RAG faithfulness was 14% on an MD benchmark and 20% on a PDF benchmark. Context precision started at 57%. ([6:24](https://youtu.be/9_oy4owGtPI?t=384))
- Scores rose to 65, 74 and then 82 after one-variable-at-a-time tuning. The speaker does not say which metric each value refers to. ([6:24](https://youtu.be/9_oy4owGtPI?t=384))
- Context chunks dropped from over 7,000 to about 1,000 (about one-seventh of the context size), with higher precision and lower token spend. ([6:24](https://youtu.be/9_oy4owGtPI?t=384))
- The speaker says the token savings from resumed sessions are large but gives no measured figure. The demo only shows the mechanism. ([11:49](https://youtu.be/9_oy4owGtPI?t=709))

## Hot takes
- Agent memory is solved, but agent learning is not.
- Shared state is not shared knowledge.
- A bigger context window is the surest way to the quickest, most expensive failure.
- Fine-tuning cannot save and persist lessons that agents learn.
- Running RAG over every transcript adds garbage and burns more tokens for worse results.

## Tools mentioned
Mako (Yugabyte agent-native persistence layer), YugabyteDB, Claude Desktop, Claude Design, Codex, ChatGPT, MCP, Postgres

## Relevance to our work
- **agentos** (2/3): MemoryMesh already has tiered cross-session memory with provenance and conflict resolution. The talk's private-to-shared promotion gate and per-memory traceability map onto that design, and the trace-based token check matches the benchmark-first thesis. → *Add a private-to-shared promotion step to MemoryMesh that requires a human or rule-based approval and stores the source reference, then measure chunk count and token use before and after promotion on a fixed task set.*
- **prosharness** (1/3): Resumability across sessions is related to ProsHarness checkpoint/resume. The talk's approach is memory search over a shared store, not a checkpoint, so the overlap is partial. → *Compare ProsHarness checkpoint/resume with a memory-search resume on the same long run and check which needs fewer tokens to restart.*
- **general** (1/3): Stated general principle: shared agent context should be a reviewed, provenance-tagged layer rather than a raw RAG dump. The talk offers no independent evidence. → *Read the RAG tuning steps in the talk and check whether our own retrieval changes were tested one variable at a time with traces.*
