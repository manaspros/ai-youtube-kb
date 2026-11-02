# Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `KGFyOtl5ktI` · [watch](https://youtu.be/KGFyOtl5ktI) · **date:** 2026-10-09 · **length:** 16:39 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Jake Broekhuizen · **orgs:** LangChain
- **topics:** agent-architecture, memory, evals, context-engineering · **tags:** agent memory, procedural memory, semantic memory, episodic memory, trace-to-memory flywheel, human-in-the-loop, sleep-time compute, progressive disclosure, context hub, observability

> Jake Broekhuizen (LangChain) argues agent memory is a read-write loop: capture traces, filter them into signal, and promote only the durable parts into long-term context, with human review for procedural memory.

## Summary
Jake Broekhuizen of LangChain's labs team describes giving agents memory that learns from their own runs. He uses a financial-services budgeting agent whose tone kept slipping into directive advice, and fixing it by hand did not scale. He separates evidence (traces and logs) from memory, which is durable context the agent reads on later runs. He frames memory with cognitive-science buckets (semantic, episodic, procedural) and separates working memory from long-term memory. The loop is capture, analyze, update: traces are filtered so only a small subset becomes memory updates. He presents LangSmith Context Hub as one implementation. He warns that updates may not reach long-running agents because of runtime state and caching. He recommends human review and evals before procedural changes go live. The talk is a practitioner walkthrough with one concrete case and no benchmarks.

## Key ideas
- **A trace only becomes memory when its lesson is converted into durable context the agent reads on future runs. Observability alone tells you what happened and does not change behavior.** — Memory is defined as durable context that guides future runs. Traces, transcripts and logs are evidence until they are filtered and written back as context. ([3:41](https://youtu.be/KGFyOtl5ktI?t=221))
- **Memory is grouped into three cognitive-science buckets: semantic (facts and preferences), episodic (past examples and patterns), and procedural (instructions, skills and rules).** — The speaker says procedural memory is where most of the visible behavior gains come from. In his tone example the fix was a new rule, not a new fact. ([5:11](https://youtu.be/KGFyOtl5ktI?t=311))
- **Working memory (per-run scratch, tool results, retrieved files) is separate from long-term memory (a store the agent loads from). Each run reads long-term into working memory, then writes signal back.** — Harnesses inject long-term memory in different ways: into the prompt, through retrieval tools, from a store directly, through files, or by changing runtime state. ([6:15](https://youtu.be/KGFyOtl5ktI?t=375))
- **The core loop is memory informs the run, the run produces evidence, a filter extracts signal, and the signal updates memory. The abstract form is capture, analyze, update.** — The speaker calls the loop a flywheel. The analyze step runs in the background to extract signal from traces based on what matters to the team. ([9:39](https://youtu.be/KGFyOtl5ktI?t=579))
- **Most trace data should stay as referenceable history. Only a small subset should change memory, and some data should become offline eval datasets.** — Turning all evidence into long-term memory makes the agent struggle and makes future reasoning harder, so the filter step is the key design decision. ([12:11](https://youtu.be/KGFyOtl5ktI?t=731))
- **Memory updates may never reach a long-running agent. Caching and runtime state can keep the agent from re-reading the updated store, so behavior does not change.** — The speaker says he spent a long time on this gotcha before realizing that the hot path and caching were hiding his updates. He recommends deciding what can be cached. ([13:38](https://youtu.be/KGFyOtl5ktI?t=818))
- **Decide which memory can self-update and which needs human review. Procedural memory, which drives most behavior (he estimates about 75%), should be surfaced for review before it reaches the hot-reload path.** — He cites self-updating agents such as OpenClaw and HermesAgent as examples of this pattern. Protecting important behavior with evals is the third principle. ([13:38](https://youtu.be/KGFyOtl5ktI?t=818))
- **LangSmith Context Hub is one implementation. Capture comes from observability, analysis is a background agent that promotes signal to a remote store, and agents pull the updated context on their next run.** — The speaker presents this as one approach and says he does not claim it is the only one. ([10:44](https://youtu.be/KGFyOtl5ktI?t=644))

## Techniques
- **Trace-to-memory capture, analyze, update loop** — Capture every run's trajectory (tool calls, subagent calls, retrieved context). Run a background analysis step over traces that looks for patterns on criteria you define, such as failed tool calls, user corrections, or tone drift. Promote only the useful signal into the durable store that the agent loads on its next run. Keep the rest as history. *When:* Use when agents repeat mistakes that observability already shows, and manual prompt or skill fixes do not scale.
- **Classify memory into semantic, episodic and procedural buckets** — Assign each lesson to a bucket. Facts and preferences go to semantic memory. Past examples and learned patterns go to episodic memory. Instructions, skills and rules go to procedural memory. Treat procedural changes with the most care, since they drive most behavior. *When:* Use when designing memory schemas or deciding where a new learning should be stored.
- **Gate procedural memory updates with human review and evals** — Surface proposed changes to procedural memory (instructions, policies, tone rules) for review. Only commit them after evals show no regressions, then push them into the hot-reload path. *When:* Use for regulated or customer-facing agents, or any self-updating agent where a bad rule would change behavior broadly.
- **Check the hot path for memory staleness** — Confirm that a memory update written during a long run is re-read on later runs. Review which parts of the runtime state or prompt are cached, and make sure the cache is invalidated or the store is re-read when memory changes. *When:* Use for long-running background agents where an update made early in a run is never picked up later.

## Numbers
- The speaker estimates procedural memory (instructions, policies, tone guidelines) drives about 75% of an agent's behavior. ([14:57](https://youtu.be/KGFyOtl5ktI?t=897))
- The financial-services example is a budgeting and spending agent whose tone slipped from advisory into directive. The fix is manual and does not scale. No quantitative results are given. ([1:11](https://youtu.be/KGFyOtl5ktI?t=71))

## Hot takes
- Most trace data should stay as history and only a small subset should change memory.
- Procedural memory changes should go through human review and evals before they reach the hot path.
- Observability alone does not make an agent better; the trace has to become durable context.

## Tools mentioned
LangSmith, LangSmith Context Hub, LangChain, OpenClaw, HermesAgent

## Relevance to our work
- **agentos** (2/3): AgentOS L2A MemoryMesh already has tiered cross-session memory and conflict resolution. The trace-to-memory filter and the procedural-versus-semantic split map directly onto that design. → *Add a filter stage between trace capture and memory writes in MemoryMesh, and label each memory entry as semantic, episodic or procedural so only the signal is promoted.*
- **prosharness** (2/3): ProsHarness checkpoints long agent runs and loops over them. The talk's caching and staleness gotcha for long-running agents applies to checkpoint and resume state. → *Verify that memory or context updates made mid-run are re-read after checkpoint resume, not served from cached runtime state.*
