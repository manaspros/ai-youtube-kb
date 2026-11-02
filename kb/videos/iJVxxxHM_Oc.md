# Where RL Will Take Search — Maximilian-David Rumpf, SID.ai

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `iJVxxxHM_Oc` · [watch](https://youtu.be/iJVxxxHM_Oc) · **date:** 2026-09-18 · **length:** 9:36 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Maximilian-David Rumpf · **orgs:** SID.ai
- **topics:** rag-retrieval, training-finetuning-rl, multi-agent, context-engineering · **tags:** agentic search, reinforcement learning, search sub-agent, reranker, BM25, vector search, context pollution, latency and cost, verifiable rewards, hiring pitch

> Founder of SID.ai argues search should move from fixed retrieval pipelines to one RL-trained model, reporting about 20x faster and 100x cheaper than frontier-model search agents.

## Summary
The speaker, CEO of SID.ai, says agentic search gives better results (about twice as likely to find the right document) but costs 100 to 1,000 times a classical query and takes minutes. Agents spend 30% to 50% of their tokens searching, usually at the start of a task. Classical search is a chain of locally optimized models (query rewrite, search, reranker) with decisions fixed at design time, so unexpected questions fall into a long tail of failures. The proposed fix is one model trained with reinforcement learning that controls the whole search loop: it searches, reads, refines filters and iterates, with compute scaled to question difficulty. Search suits RL because a right-document reward is easy to verify and rollouts are cheap. The talk claims that search quality rises predictably with compute, and that the trained sub-agent is about 20x faster (around 5 seconds versus 2 minutes) and about 100x cheaper than a frontier model. Running search in a sub-agent also keeps bad results out of the main agent's context. The talk is short, gives few method details, and ends with a pitch for the company.

## Key ideas
- **Agentic search is much better but far too costly and slow** — Agents find the right document about twice as often, but cost 100 to 1,000 times a classical query and take minutes per question. ([0:08](https://youtu.be/iJVxxxHM_Oc?t=8))
- **Agents burn a large share of their tokens on search** — Searching takes 30% to 50% of agent tokens, usually at the start of a task, to find the context the agent then works from. The speaker proposes moving that search into a sub-agent. ([1:06](https://youtu.be/iJVxxxHM_Oc?t=66))
- **Fixed search pipelines fail in the long tail** — A chain of locally optimized models (rewrite, search, rerank) bakes all decisions in at design time. A reranker can see that results are bad but cannot act on it, so unexpected questions fail, and designers patch them with edge cases. ([2:35](https://youtu.be/iJVxxxHM_Oc?t=155))
- **Learned end-to-end designs beat human-designed pipelines** — The speaker traces a pattern from hand-written rules to small specialized models to one learned model (vision, chess, AlphaZero), and expects search to follow the same path toward a single model that makes every decision. ([4:01](https://youtu.be/iJVxxxHM_Oc?t=241))
- **One RL model can run the whole search loop** — The model queries the database, reads results, sets metadata filters, refines and searches again, then returns a ranked list. It can spend more compute on hard questions. ([4:01](https://youtu.be/iJVxxxHM_Oc?t=241))
- **Search is a good RL target because it is verifiable and cheap to roll out** — Reward is easy to check (did it find the correct document), and the environment can be run thousands of times per second in training. Models can also be specialized, since much of a general language model is unneeded for search. ([5:11](https://youtu.be/iJVxxxHM_Oc?t=311))
- **The trained model discovers its own search strategies** — Rewards are not hand-scripted. The speaker says search quality grows predictably with training compute, latency and other rewards can be mixed in, and they have not yet seen a ceiling. ([6:15](https://youtu.be/iJVxxxHM_Oc?t=375))
- **Sub-agent search keeps the main agent's context clean** — In a normal agent trace, bad results pollute the context window. A search sub-agent returns only good results, so the main agent is more likely to be correct and spends fewer tokens. ([7:36](https://youtu.be/iJVxxxHM_Oc?t=456))

## Techniques
- **Search as a delegated RL-trained sub-agent** — The main agent hands a query to a sub-agent that runs all searching, reading and iteration, then returns only the ranked results. The main context never sees the failed attempts. *When:* Agent tasks where search takes a large share of tokens or where bad retrieval results pollute the context window.
- **Verifiable retrieval reward for RL** — Score each rollout by whether it retrieved the known correct document, and run many rollouts per training step against the search environment. *When:* Any retrieval task with a labeled correct document or answer that can be checked automatically.
- **Mixed reward with latency** — Add latency (and other cost-related signals) to the retrieval-quality reward so the model learns to be fast as well as accurate. *When:* Latency or cost budgets matter, not just recall.
- **Learned loop in place of a fixed pipeline** — Replace the chain of query rewrite, search and rerank with one model that picks the next action (search, read, filter, stop) at run time. *When:* Long-tail or varied questions where edge-case rules keep breaking a fixed pipeline.
- **Parallel sub-agent searches** — Run several search actions in parallel within one sub-agent run to cut wall-clock time. *When:* The sub-agent is too slow for the use case, as in the speaker's 5-second target.

## Numbers
- Agentic search is about twice as likely to find the right document as classical search, but costs about 100 to 1,000 times a classical query and takes minutes. ([0:08](https://youtu.be/iJVxxxHM_Oc?t=8))
- Agents spend 30% to 50% of their tokens on searching. ([1:06](https://youtu.be/iJVxxxHM_Oc?t=66))
- The trained sub-agent is about 20x faster: roughly 2 minutes down to about 5 seconds on average. ([6:15](https://youtu.be/iJVxxxHM_Oc?t=375))
- The trained sub-agent is about 100x cheaper than a frontier model on this task. ([6:15](https://youtu.be/iJVxxxHM_Oc?t=375))
- RL rollouts for search run thousands of times per second during training. ([5:11](https://youtu.be/iJVxxxHM_Oc?t=311))

## Hot takes
- Search is verifiable, which makes it one of the best targets for reinforcement learning.
- Pipelines of chained, locally optimized models accumulate a long tail of failures that edge-case rules cannot fix.
- The most valuable information is not on the internet; it is in private databases, such as a bank's internal systems.

## Tools mentioned
BM25, PageRank, vector search, rerankers

## Relevance to our work
- **agentos** (1/3): MemoryMesh does hybrid BM25 plus pgvector retrieval with fixed logic. The talk's trained search loop could be a comparison point, but the talk gives no method details to build on. → *Benchmark a single-agent search loop (search, read, refine filters, stop) against MemoryMesh's fixed BM25 plus pgvector retrieval on one knowledge bucket, counting tokens and latency per question.*
- **prosharness** (1/3): ProsHarness runs long Claude Code sessions. Isolating search or research in a sub-agent that returns only results could keep the main run's context clean. → *Try running the research or lookup step of one long ProsHarness task as a subagent whose only output is a short ranked list, and compare context size and task success with the current run.*
- **general** (1/3): Matches the recurring interests in context engineering and subagents: the talk argues that filtering what enters the main context improves accuracy and cost. → *Read the talk's claims on sub-agent context isolation alongside existing context-engineering notes, and check whether the claims hold on one of our own agent traces.*
