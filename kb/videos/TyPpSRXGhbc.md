# Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `TyPpSRXGhbc` · [watch](https://youtu.be/TyPpSRXGhbc) · **date:** 2026-10-10 · **length:** 17:16 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Charles Dickens · **orgs:** Snorkel AI, UC Berkeley Sky Computing Lab
- **topics:** training-finetuning-rl, evals, data-engineering · **tags:** small-models, GRPO, binary-reward, LLM-as-judge, synthetic-data, finance, FinQA, curriculum, tool-use, BFCL, Qwen3, RLLM

> Snorkel AI and UC Berkeley Sky lab trained a 4B Qwen3 agent with RL for under $500 that beats its 235B variant on finance QA; simple binary rewards and single-table curricula won.

## Summary
Charles Dickens (Snorkel AI) describes building FinQA, an expert-validated financial question-answering benchmark built from SEC 10-K tables, and training a 4B Qwen3 model with RL (GRPO, RLLM framework) that reaches about 60% pass rate versus 51% for the 235B variant. The data pipeline has three stages: table and schema extraction from EDGAR filings, QA generation with lineage metadata, and three-layer verification (programmatic checks, independent agent review, expert manual review). He names three recurring failure modes in frontier models: schema hallucination, context flooding from poorly planned queries, and repeating failed strategies instead of adapting. Training uses a ReAct-style agent with table tools, a binary correctness reward from a GPT-5 nano judge, and about 1,000 concurrent environments on eight H100s, costing about $460 in total. Ablations show that training on single-table data gives the most lift, that gains transfer to multi-table questions and to BFCL tool calling, and that a binary reward beat a weighted expert rubric. He closes with three evaluation axes for agents (environment complexity, autonomy horizon, output complexity) and a pitch for Snorkel's open benchmark grants.

## Key ideas
- **Specialization can beat raw scale for enterprise agents when the training data matches the target domain and task distribution.** — A 4B model trained on domain-representative data outperforms a 235B generalist on FinQA at a small fraction of the cost. The speaker says the goal is parity with frontier models, not general reasoning. ([0:08](https://youtu.be/TyPpSRXGhbc?t=8))
- **Synthetic benchmark data needs three verification layers.** — Programmatic checks use lineage and table/column metadata to catch hallucinated names, then independent agent reviews run, then expert humans check realism and answer correctness. ([5:18](https://youtu.be/TyPpSRXGhbc?t=318))
- **Frontier models show three repeated failure modes on this environment.** — Schema hallucination (assuming tables or columns exist), context flooding (e.g. SELECT * with poorly planned queries), and poor recovery (the 235B model repeats the same failed strategy instead of adapting to the error message). ([6:42](https://youtu.be/TyPpSRXGhbc?t=402))
- **Simple binary reward beat a carefully engineered rubric.** — A weighted, expert-designed rubric scoring intermediate steps (table access, query completeness) did worse than a single binary correctness reward from an LLM judge, which the speaker says became the basis of an enterprise agent blueprint. ([13:28](https://youtu.be/TyPpSRXGhbc?t=808))
- **The bottleneck was tool-use discipline, not reasoning depth.** — Training only on simple single-table questions lifted multi-table accuracy with no multi-table training data. A single-to-multi curriculum was not needed to get that lift, and the speaker suggests the model learned reliable tool use that composes. ([11:54](https://youtu.be/TyPpSRXGhbc?t=714))
- **Specialist RL did not erode general tool calling.** — On BFCL, overall accuracy rose slightly, with small gains on multi-turn and memory categories, so the fine-tune kept broader tool-use competence. ([11:54](https://youtu.be/TyPpSRXGhbc?t=714))
- **Evaluate agents on three axes.** — Environment complexity (how realistic and dynamic the environment is), autonomy horizon (whether tests match the task lengths people actually run and whether agents judge safely alone or as co-pilots), and output complexity (beyond text artifacts, which he says is underexplored). ([14:53](https://youtu.be/TyPpSRXGhbc?t=893))

## Techniques
- **Multi-stage synthetic eval and training data pipeline** — Extract schema from real documents (10-K tables from EDGAR), generate one QA pair per table with lineage metadata and a domain-expert question taxonomy, then verify in three layers: programmatic metadata checks, independent agent review, and expert manual review. *When:* Building domain benchmarks or RL training sets where no labelled data exists and hallucinated table or column names are a risk.
- **Company-level data split to prevent leakage** — Split the data so no company (entity) appears in more than one of train, validation and held-out benchmark. *When:* Benchmarks where the same entity can show up in many items and inflate held-out scores.
- **Binary reward with reference-based LLM judge** — Reward 1 only for a correct final answer, scored by a cheap judge model (GPT-5 nano) against a reference answer, rather than rubric points for intermediate steps. *When:* RL on tasks with single verifiable final answers, where judge cost matters and rubric weights are hard to tune.
- **Single-table-first data mixture** — Train on simple single-table questions only. The ablation found this beat a mixed set and a single-to-multi curriculum. *When:* When a small model must learn tool use cheaply and the harder compositional tasks are expected to transfer.
- **Decorator-based RL wrapper for existing agents** — The RLLM framework wraps an existing agent with a decorator, with near-zero code changes, a CLI-first workflow, and pluggable RL algorithms and training backends. *When:* Adding RL training to an agent that already runs, without rewriting its loop.
- **Large concurrent rollout generation** — Run about 1,000 environment instances concurrently to generate trajectories for GRPO, on eight H100s. *When:* Keeping RL rollout cost low by parallelising environment episodes.

## Numbers
- Qwen3 4B RL-trained agent reaches about 60% pass rate versus 51% for the 235B variant on the 290-sample held-out FinQA benchmark (transcript says 'pass at run'; likely pass@1) ([2:34](https://youtu.be/TyPpSRXGhbc?t=154))
- Base 4B model accuracy more than doubled after RL training ([10:30](https://youtu.be/TyPpSRXGhbc?t=630))
- Total training cost under $500: about $420 compute on eight H100s and about $40 judge API ([9:00](https://youtu.be/TyPpSRXGhbc?t=540))
- About 1,000 concurrent environments used to generate trajectories ([9:00](https://youtu.be/TyPpSRXGhbc?t=540))
- About 6,900 SQL tables extracted from 10-K filings; split into about 4,000 train, 500 val, 290 held-out benchmark ([5:18](https://youtu.be/TyPpSRXGhbc?t=318))
- Multi-table FinQA dataset: about 1,000 train, 120 val, 80 benchmark; tables span 2 to 5 ([14:00](https://youtu.be/TyPpSRXGhbc?t=840))
- BFCL overall accuracy slightly improved after specialist RL, with minor gains on multi-turn and memory ([11:54](https://youtu.be/TyPpSRXGhbc?t=714))

## Hot takes
- You wouldn't call Terence Tao for a tax audit: specialised workflows don't need generalists.
- Simpler reward beat the expert rubric: a single binary signal gave more lift than weighted intermediate-step scoring.
- The reasoning bottleneck was never depth; it was tool-use reliability.

## Tools mentioned
RLLM, GRPO, Qwen3 4B and 235B, GPT-5 nano (judge), FinQA benchmark, BFCL, EDGAR, H100

## Relevance to our work
- **general** (2/3): Small-model specialisation with cheap LLM-judge binary rewards (about $460 total) is a concrete cost benchmark for cheap-model pipelines, and the verification layering applies to data-quality and entity-resolution labelling with LLMs. → *For the entity-resolution labelling work, try a binary LLM-judge with a cheap model against reference answers and compare it with a weighted rubric before investing in rubric design.*
- **agentos** (1/3): Evals and benchmark-building for agents are a recurring interest, and AgentOS has RAGAS evals. The three-layer verification and company-level split are reusable ideas, but no RL training is planned. → *When building an eval set for AgentOS MemoryMesh, split by entity so no entity crosses train/val/benchmark, and add a metadata-based programmatic check before any LLM review.*
- **prosharness** (1/3): The failure mode of repeating a failed strategy instead of reading the error is relevant to long checkpointed agent runs, but the talk gives no harness-level method. → *Add an error-aware check to the ProsHarness retry path: if the same tool call fails twice with the same error, force a re-plan step and log it.*
