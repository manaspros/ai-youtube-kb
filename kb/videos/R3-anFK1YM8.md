# Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `R3-anFK1YM8` · [watch](https://youtu.be/R3-anFK1YM8) · **date:** 2026-08-18 · **length:** 13:04 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Stefania Druga · **orgs:** Sakana AI
- **topics:** memory, context-engineering, evals, local-ai · **tags:** long-horizon agents, context rot, recall policy, decision ledger, vector RAG, oracle ablation, local models, Apple M3 Ultra, XBench, DeepSeek V4 Flash, Qwen 4-bit, sovereign AI

> Sakana AI researcher on memory harnesses for long-horizon research agents running on local models; a ranked decision-ledger recall policy beat both no memory and plain vector RAG, at lower cost.

## Summary
Stefania Druga (Sakana AI) argues that long-horizon agent tasks suffer from context rot, where the model contradicts itself, redoes work, or drifts from the question. She frames memory as a write-manage-read control loop around the model, not just a database. Her research agents start with zero durable memory, so all memory comes from the harness: an always-shown core, a recall block, and an archival store across sessions. She compares a ladder of recall modes (no memory, vector RAG, a decisions ledger with prioritisation, and an oracle that supplies ground-truth memory) with the model held fixed. When the whole task fits in context, memory added cost but no capability. On an XBench-style task where the answer lay about 376 steps outside the window, ranked recall beat no memory, and the ranked ledger beat simply gating whether to use memory. Ablations with wrong or recent steps still favoured the ranked policy, and it held across two models and more than one benchmark. Her advice is to treat the recall policy as a first-class metric and to test it over repeated runs and sessions. She notes that local models run serially here, which makes evals slow.

## Key ideas
- **Long-horizon agents fail through context rot: contradictions, repeated work, and drift from the original question.** — She says this matters more as tasks get longer while model releases become less frequent, so context management becomes a priority. ([0:08](https://youtu.be/R3-anFK1YM8?t=8))
- **Treat memory as a write-manage-read control loop around the model, not as a database.** — The store is only one part. The harness decides what gets written, managed, and read back on every turn. ([3:55](https://youtu.be/R3-anFK1YM8?t=235))
- **Memory does not help when the task already fits in context.** — On a literature-review task with a retracted headline claim, memory gave the same performance as no memory and only added cost. ([5:18](https://youtu.be/R3-anFK1YM8?t=318))
- **Memory pays off when the relevant information falls outside the context window.** — On the XBench-style question, the answer was at about step 124 while the question came at step 500, so recall was required. ([6:18](https://youtu.be/R3-anFK1YM8?t=378))
- **A ranked decision-ledger recall policy beat both no memory and gating on whether to use memory.** — The oracle does not reach the maximum because supplying the right memory does not force the model to use it. ([7:43](https://youtu.be/R3-anFK1YM8?t=463))
- **The ranked policy held up under ablations, across models, and across benchmarks, and it also cost less.** — Wrong-step and most-recent-step conditions were worse than the ranked policy. The speaker says bad memory is expensive because it wastes tokens and misleads the agent. ([9:06](https://youtu.be/R3-anFK1YM8?t=546))
- **Make the recall policy a first-class metric and evaluate it across runs and sessions.** — Questions to answer include which memory types to store, how to rank them, and which ones survive repeated runs over multiple sessions. ([10:02](https://youtu.be/R3-anFK1YM8?t=602))

## Techniques
- **Write-manage-read memory loop** — Design memory as a control loop around a fixed model. Define what gets written, how it is managed, and how it is read on each turn, separate from the storage backend. *When:* Building a harness for agents with no durable memory, such as short-lived research agents on long tasks.
- **Ranked decision-ledger recall** — Log the decisions made on each turn, rank them by priority, and recall the top items into a recall block shown to the agent. Compare against vector RAG and no-memory baselines. *When:* Long tasks where the relevant context has scrolled out of the window and plain similarity search pulls in the wrong things.
- **Recall-mode ladder with an oracle** — Hold the model fixed and vary only the recall mode, going from no memory to vector RAG to a ledger. Add an oracle that supplies ground-truth memory to set an upper bound. Run multiple cells and seeds per question. *When:* Measuring whether a memory change helps, and separating retrieval quality from whether the model uses what it was given.
- **Ablate with wrong and recent memory** — Feed the agent deliberately wrong or most-recent steps as memory and check that the chosen policy still wins. This tests whether the gain comes from structure and not from luck. *When:* Validating that a recall policy is more than a benchmark artefact.
- **Local, controlled eval pipeline** — Run quantised open models on a single workstation so every trace, compute step and eval result stays under your control. Accept serial execution, since batch querying was not available for the model used. *When:* You need full data and trace control, or sovereignty over the stack, and can accept slower evals.

## Numbers
- Ran over 68 questions on the XBench-style long-horizon benchmark, each with multiple cells and seeds. ([7:43](https://youtu.be/R3-anFK1YM8?t=463))
- Answer at about step 124 while the question was asked at step 500, so it was outside the context window. ([6:18](https://youtu.be/R3-anFK1YM8?t=378))
- Test machine is an M3 Ultra with 96 GB of memory and a 28-core CPU, running a 4-bit quantised Qwen model and DeepSeek V4 Flash. ([2:31](https://youtu.be/R3-anFK1YM8?t=151))
- A retracted headline claim of 742,000 promising materials was used as a needle-in-a-haystack case. ([5:18](https://youtu.be/R3-anFK1YM8?t=318))
- Over 30 runnable memory cookbooks are in the open-source repository she cites. ([10:02](https://youtu.be/R3-anFK1YM8?t=602))

## Hot takes
- Bad memory is more expensive than no memory, because it burns tokens and sends the agent the wrong way.
- Recall policy should be treated as a first-class metric, not an implementation detail.
- When the task fits in context, adding a memory harness adds cost and no capability.

## Tools mentioned
DeepSeek V4 Flash, Qwen (4-bit quantised), XBench, vector RAG, Spyder V2 benchmark

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans tiered cross-session memory and RAGAS evals. The ranked-ledger versus vector-RAG versus no-memory comparison with an oracle upper bound is a concrete eval design that its memory layer lacks. → *Add a recall-mode ablation to MemoryMesh evals (no memory, vector RAG, ranked decision ledger, oracle) on a long-context task, measuring correctness and token cost per answer across repeated seeds.*
- **prosharness** (2/3): ProsHarness does checkpoint/resume of long Claude Code runs. Carrying decisions from earlier checkpoints into later sessions with a ranked recall policy is directly relevant, and the write-manage-read framing fits its harness design. → *Prototype a decisions ledger written at each checkpoint, with ranked recall into the next resumed session, and compare resume quality and token cost against a plain-summary baseline.*
- **general** (1/3): Useful general framing for the context-engineering interest: memory as a control loop, and when memory helps versus when it only adds cost. → *Read the cited memory cookbook repository and note which recall policies the cookbooks implement.*
