# User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Jx4ZFEAq6bY` · [watch](https://youtu.be/Jx4ZFEAq6bY) · **date:** 2026-07-18 · **length:** 15:37 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Sonam Pankaj · **orgs:** StarlightSearch
- **topics:** memory, rag-retrieval, skills-self-improvement, evals · **tags:** utility-score, retrieval-reranking, outcome-feedback, agent-memory, skill-consolidation, runtime-learning, cold-start, human-in-the-loop-feedback

> StarlightSearch's CEO argues agent memory should learn from outcomes: utility-weighted retrieval, reasoning-style memories, and consolidation into skills. Product-pitchy, with self-reported benchmarks.

## Summary
The talk argues that agents fail because retrieval is static and outcome signals (eval results, human failure reports) never reach the retrieval layer, so the same mistakes repeat. The speaker says the fix is a runtime memory layer that ranks memories by a "utility score": embedding similarity weighted by how often that memory helped or hurt past runs. Memories are stored as reasoning and procedures (for example, check the settlement before issuing a refund), not as static user facts. Once enough memories accumulate (around 10 by the speaker's account), they are consolidated into skills so the agent loads updated guidance and stale prompt lines get dropped. A live SQL product-search demo shows a failed search, a human correction, and a later run that takes a different tool trajectory after the memory is re-ranked. The speaker lists limits: cold start (pure semantic search until reviews accumulate), utility drift, noisy review labels, and a lambda re-ranking hyperparameter. The benchmark numbers are the speaker's own, and the talk gives little implementation detail.

## Key ideas
- **Retrieval is the missing learning loop** — The speaker says most pipeline failures trace to retrieval and context stuffing. Observability captures traces and evals give pass/fail, but neither reaches the agent's retrieval, so improvement needs a manual engineer loop. ([1:26](https://youtu.be/Jx4ZFEAq6bY?t=86))
- **Evals and traces are not wired into the agent** — Observability stores every tool call and exception, and evals judge the final output. The gap is a layer that converts those traces and verdicts into guidance the agent reads on future runs. ([2:51](https://youtu.be/Jx4ZFEAq6bY?t=171))
- **Existing agent memory stores facts, not outcomes** — The speaker says current memory products keep user preferences, profiles and chat history, and rank by embedding similarity. None of them use past task outcomes to rank. ([3:50](https://youtu.be/Jx4ZFEAq6bY?t=230))
- **Utility score re-ranks memories by past usefulness** — Retrieval score is semantic similarity to the current task, weighted by how much that memory helped or hurt earlier executions. Outcome becomes a first-class re-ranking signal. ([5:15](https://youtu.be/Jx4ZFEAq6bY?t=315))
- **Store memories as procedures with reasoning** — Instead of 'user prefers dark theme', a memory encodes a rule like 'check the settlement before refunding so the customer is not paid twice'. The speaker says this is what cuts context stuffing. ([6:16](https://youtu.be/Jx4ZFEAq6bY?t=376))
- **Consolidate memories into skills after enough reviews** — After roughly 10 memories, the system bakes the accumulated reasoning into a skill file. The agent reloads the skill each run, so stale system-prompt items (such as a dropped database column) can be removed without editing the prompt. ([7:17](https://youtu.be/Jx4ZFEAq6bY?t=437))
- **Known limits: cold start, drift, noisy labels, lambda** — Cold start means pure semantic search until enough reviews exist, and the speaker says they cannot fix this. Utility drift, noisy review labels, and the lambda re-ranking weight were mitigated by design, according to the speaker. ([9:35](https://youtu.be/Jx4ZFEAq6bY?t=575))
- **Demo: one human correction changes the next trajectory** — A 'gaming mouse' search returned nothing. The presenter marked it as a failure and supplied the right answer (a wireless mouse exists). On the next run the trajectory changed: the agent still called the search tool, but it now used the fed-back feedback, and the memory's utility score moved. ([12:26](https://youtu.be/Jx4ZFEAq6bY?t=746))

## Techniques
- **Utility-weighted memory retrieval** — Store each memory with the outcomes of runs where it was used. Rank candidates by semantic similarity to the current task multiplied or weighted by historical usefulness, with a lambda weight controlling how much outcome counts. Update scores as new reviews arrive. *When:* Agents that handle repeated task types and have a measurable success or failure signal per run.
- **Human failure report as a memory write** — When a run is marked as failed, the reviewer supplies the correct answer or fix. That correction is stored as a memory tied to the failed query, so the next similar query gets it at retrieval time. *When:* Early-stage agents where a small set of reviewers can label failures, and the failure cases repeat.
- **Memory as procedure, not fact** — Write memories as conditional rules or checks (when X, verify Y first) instead of static user attributes. Retrieve by task similarity so the rule shows up at the right step. *When:* Customer-support or transactional agents where a skipped check causes real harm (for example, double refunds).
- **Consolidate memories into skills** — When a cluster of memories for one domain reaches a threshold (speaker says about 10, or about 5 reviews), summarize them into a skill file that the agent loads on every run. Delete system-prompt lines that the consolidated skill makes obsolete. *When:* When the agent's prompt is accumulating stale instructions, or rules change often and should not require prompt edits.
- **Runtime learning vs compile-time optimization** — Update memory and retrieval during execution, with no retraining or prompt recompilation. The speaker contrasts this with DSPy-style compile-time tuning, which bakes lessons into the prompt. *When:* Production agents where outcomes arrive continuously and redeploying prompts for each fix is too slow.

## Numbers
- 73% of pipeline failures attributed to retrieval non-generation and context stuffing (speaker's figure, citing a post by Ram Sriharsha) ([1:26](https://youtu.be/Jx4ZFEAq6bY?t=86))
- Policy-following benchmark (transcribed 'on towel bench', likely tau-bench): 66% baseline, 76% with the memory system without skills, 80% with skills ([10:50](https://youtu.be/Jx4ZFEAq6bY?t=650))
- Humanity's Last Exam (transcribed 'human last exam'), agentic setting: RAG 47.5, baseline 35.7, another memory system 58.2, their system 61.3 (the speaker's wording on which number is which is ambiguous) ([8:23](https://youtu.be/Jx4ZFEAq6bY?t=503))
- Skill consolidation threshold: about 10 memories (7:17) or about 5 reviews (13:47) ([7:17](https://youtu.be/Jx4ZFEAq6bY?t=437))
- Other benchmarks mentioned without numbers: BigCodeBench and LongMemEval ('long tv') ([8:23](https://youtu.be/Jx4ZFEAq6bY?t=503))

## Hot takes
- Most agent memory systems optimize for making wrong answers faster and cheaper, not for making retrieval learn.
- Current agent memory is built for chat personalization, not for self-improving production systems.
- Memory should store reasoning and checks, not static facts.

## Tools mentioned
Reflect (StarlightSearch's memory system), Mem0 (transcribed as 'memzero'), DSPy, ReAct, Pinecone (cited in a post, not used)

## Relevance to our work
- **agentos** (2/3): MemoryMesh already has tiered cross-session memory, provenance, and hybrid BM25+pgvector retrieval. Adding an outcome-based usefulness weight to re-ranking is a direct, testable extension. → *Add a per-memory usefulness score to MemoryMesh's re-rank step, updated from run outcomes behind a flag, with lambda as a config value. Compare retrieval against a fixed eval set with and without it.*
- **prosharness** (1/3): ProsHarness has skill ranking and checkpoint/resume. A per-skill success record would make its ranking outcome-aware, the same idea as the utility score, but the talk gives no mechanism for it. → *Log pass/fail per skill invocation in ProsHarness and test whether ranking by past success beats the current ranking on a small set of runs.*
