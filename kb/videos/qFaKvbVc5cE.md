# Teaching Agents to Search with NVIDIA Data Designer — Dhruv Nathawani, NVIDIA

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `qFaKvbVc5cE` · [watch](https://youtu.be/qFaKvbVc5cE) · **date:** 2026-10-12 · **length:** 55:30 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dhruv Nathawani · **orgs:** NVIDIA
- **topics:** training-finetuning-rl, data-engineering, rag-retrieval, evals · **tags:** synthetic-data, data-designer, seed-data, wikidata, agentic-search, tavily, mcp, distillation, llm-as-judge, evaluation, personas, nemotron, sft, structured-output

> NVIDIA workshop on NVIDIA Data Designer: build column-by-column synthetic data pipelines, seed them with Wikidata random walks and Tavily search traces, and use them to teach a model web search (BrowseComp 0 to about 30%).

## Summary
Dhruv Nathawani (NVIDIA, Nemotron team) walks through Data Designer, an open-source framework for building synthetic data as a column-by-column DAG. Columns can be optional seed data, sampler columns for diversity, LLM text/structured/code/image columns, and validators. He argues that naive prompt loops collapse in diversity and give no correlations or validation. The workshop has three notebooks: basic generation with a judge, agentic data via MCP with Tavily search, and a search-training pipeline. The search pipeline starts from random 4-to-8-hop walks over the Wikidata graph, turns them into hard search questions, and has a teacher model (gpt-oss-120b) produce search trajectories and golden answers. Roughly 50,000 seeds were filtered to 7,000 SFT records, which moved BrowseComp from about 0 to about 30 percent. The talk spends its second half on evaluation: a string matcher, an LLM judge, human audit of the judge, and live search for stale ground truth. It closes with best practices and NVIDIA's persona dataset and other open tools. Much of the content is a tool pitch, and the pace was rushed by the one-hour slot.

## Key ideas
- **Naive prompt loops fail for synthetic data** — Repeatedly prompting an LLM for a product review or question set starts repeating after 10 to 20 tries and misses feature correlations, multimodality, steering, and validation. Data Designer fixes this by generating column by column, with diversity from sampler columns and templated seeds. ([5:42](https://youtu.be/qFaKvbVc5cE?t=342))
- **Data Designer is a DAG of columns, run in preview then batch** — Columns can be an optional seed (CSV, JSONL, Parquet, or company data), sampler columns (for example difficulty with weights and sub-samplers), LLM text/structured/code/image columns, and LLM-as-judge columns. Preview generates three records for inspection, then batch mode generates the full set. Structured output that fails parsing is dropped. ([7:09](https://youtu.be/qFaKvbVc5cE?t=429))
- **Random walks over Wikidata make hard, grounded search seeds** — Random walks of about 4 to 8 hops over the Wikidata graph give entity chains. The speaker picked this range because shorter walks are trivial and longer ones drift off topic. The chain then becomes a multi-hop riddle that needs search to answer. ([25:19](https://youtu.be/qFaKvbVc5cE?t=1519))
- **Questions must be unanswerable from weights, or the agent cheats** — If the answer is recallable from training data, the agent answers directly and skips the tool calls. Questions are therefore chosen so the answer is hard to find without search, and the training target is the search behaviour itself. ([23:58](https://youtu.be/qFaKvbVc5cE?t=1438))
- **Overproduce, then filter hard** — The search pipeline went from 50,000 seeds to 7,000 high-quality end-to-end SFT records. Quality is the main lever in the speaker's view. Diversity is one axis of quality, and the funnel applies LLM-judge scores and simple heuristics such as question word count. ([39:19](https://youtu.be/qFaKvbVc5cE?t=2359))
- **Ground truth goes stale, so verification needs layers** — A verifier accepted 'U.S.' as the owner of U.S. Steel, but the company had been sold to a Japanese owner. A string matcher kept only about 24 percent, which the speaker calls too low. Evaluation needs a union of layers: a deterministic checker, an LLM judge audited by humans, and live search for current facts. ([35:40](https://youtu.be/qFaKvbVc5cE?t=2140))
- **Use the cheapest correct column type, and version the pipeline as code** — Samplers should be Python, not LLM calls, and LLMs should be used only where text is actually generated. Because the pipeline is code, it can be versioned, shared, and forked. Looking at a few samples is the speaker's main quality check. ([46:03](https://youtu.be/qFaKvbVc5cE?t=2763))

## Techniques
- **Column-by-column DAG for synthetic data** — Declare seed, sampler, LLM text/structured, and judge columns in a graph. Use Jinja-style templates to insert seed values into each prompt so every call is unique. Run preview on 3 records, iterate on prompts, then run batch. *When:* Any time you need a large, diverse, correlated, validated dataset that someone else can reproduce.
- **Seeded random walks over a knowledge graph** — Sample an entity from Wikidata and walk 4 to 8 hops along property edges. Pass the chain into the question-generation prompt as the seed path. *When:* You need multi-hop questions that a model cannot answer from memory and that stay on topic.
- **Teacher trajectories with a tool, then SFT on the trajectories** — Give a teacher LLM a search tool through MCP, with usage guidelines (a call budget and a JSON answer format with URLs and justification) and an in-context example. Keep the full tool-call trace as the training target. *When:* Teaching a smaller model when and how to call a search or other tool.
- **Overproduce and filter funnel** — Generate far more candidates than needed, score each with a judge and cheap heuristics, then keep the top fraction. The speaker's example keeps 66 percent at one stage and 7,000 out of 50,000 overall. *When:* Synthetic data quality varies a lot across samples and filtering is cheaper than generation errors.
- **Layered verification of synthetic labels** — Combine a deterministic matcher, an LLM judge, a human audit of a sample of judge verdicts, and live retrieval to check whether facts are still true. Treat a clean check of 100 items as evidence only for those 100 issues. *When:* Labels depend on facts that can change, or when the judge model's own reliability is unknown.
- **Skip the golden answer and use a reward function (RL path)** — Generate only the prompts, then score rollouts with an RL reward function (NVIDIA Nemo Gym) during training. *When:* Doing RL on tool-use tasks where you do not want to pay for teacher answers.
- **Persona seeds from census marginals** — Fit a probabilistic graphical model to census demographics, sample personas from it, and use them as seeds so generated records follow real demographic distributions and avoid individual user data. *When:* Generating records such as health or tax data that must match real population distributions and privacy constraints.

## Numbers
- Data Designer has been used to create 6.5 trillion tokens of training data (speaker's figure, growing daily) ([4:44](https://youtu.be/qFaKvbVc5cE?t=284))
- Tavily gives 1,000 free credits on signup, per the speaker ([1:40](https://youtu.be/qFaKvbVc5cE?t=100))
- Search pipeline: 50,000 seeds filtered to 7,000 high-quality end-to-end SFT records ([39:19](https://youtu.be/qFaKvbVc5cE?t=2359))
- After SFT on that data, BrowseComp moved from about 0 to about 30 percent ([39:19](https://youtu.be/qFaKvbVc5cE?t=2359))
- A keep rate of 66 percent is shown at one filter stage ([40:44](https://youtu.be/qFaKvbVc5cE?t=2444))
- A deterministic string-match checker keeps about 24 percent of the data, which the speaker says is low and partly due to the matcher ([42:13](https://youtu.be/qFaKvbVc5cE?t=2533))
- BIRD SQL benchmark moved from 26 percent to 41 percent with the agentic SQL data (speaker's Q&A answer). The speaker notes the SOTA of about 70 is agentic, while their SQL dataset is not ([29:28](https://youtu.be/qFaKvbVc5cE?t=1768))
- Hop length heuristic: 4 to 8 hops over Wikidata ([25:19](https://youtu.be/qFaKvbVc5cE?t=1519))
- Nemotron Personas USA has about one million personas ([48:47](https://youtu.be/qFaKvbVc5cE?t=2927))
- Example: exactly seven U.S. people under 18 report more than $10 million in tax return income, which an LLM would not produce by default ([50:19](https://youtu.be/qFaKvbVc5cE?t=3019))

## Hot takes
- "Internet data is not the data you want for your transformer" (Karpathy, quoted by the speaker)
- Diversity before volume. The speaker cites the Kimi K2 paper: ten strategies at one epoch beat one strategy at ten epochs.
- Evaluating synthetic data is an open research problem, and an LLM judge alone is not enough.
- Synthetic distillation can beat the teacher when the pipeline adds diversity and filtering (StructEval, Nemotron versus gpt-oss).

## Tools mentioned
NVIDIA Data Designer, Nemo Curator, Nemo Gym, Nemo Anonymizer, Nemo Safe Synthesizer, Tavily, MCP, vLLM, gpt-oss-120b, Wikidata, Hugging Face

## Relevance to our work
- **general** (2/3): Relevant to our entity-resolution and cheap-model pipelines: keep samplers and matchers in code, use an LLM only where it generates or judges, overproduce then filter, and audit judge verdicts with humans. → *Apply the cheapest-correct-column rule to the ER and Haiku pipelines: move any LLM-based sampling or string matching to code, then check the LLM judge against a human-labelled sample before trusting it.*
- **agentos** (1/3): MemoryMesh's RAGAS-style evals rely on LLM judges, and the talk shows judge verdicts need a human-audited sample before trusting them. → *Add a small human-audit pass (about 50 items, double-labelled) on MemoryMesh RAGAS judge scores before using them to rank retrieval changes.*
