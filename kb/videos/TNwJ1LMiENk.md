# Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `TNwJ1LMiENk` · [watch](https://youtu.be/TNwJ1LMiENk) · **date:** 2026-06-18 · **length:** 20:56 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kobie Crawford · **orgs:** Snorkel, UC Berkeley (RLM / Agentica), Prime Intellect, OpenEnv, Hugging Face, PyTorch
- **topics:** training-finetuning-rl, evals, mcp-and-tools · **tags:** GRPO, RL for tool use, FinQA, financial analysis, small models, behavior-targeted RL, single-table curriculum, rubric evals, OpenEnv, self-contained environment, text-to-SQL agent, Qwen3

> Snorkel shows a 4B model, RL-trained on single-table financial tool-use tasks for under $500, beating a 235B model. The gain came from fixing tool discipline, not reasoning.

## Summary
Kobie Crawford of Snorkel presents research with UC Berkeley's RLM/Agentica team on making a 4B-parameter model outperform a 235B model (Qwen3, transcribed as "QEN3") on financial-analysis tool use. The large model guessed a nonexistent table, never inspected the available tools, and then hallucinated an answer, so the authors treat this as a behavior problem rather than a reasoning problem. They trained the 4B model with GRPO on a self-contained FinQA environment, using a verified dataset built with domain experts in the loop. Single-table-only training beat mixing in multi-table questions and beat a curriculum. The tuned model learned to list tables, inspect schemas, run queries, and recover from column errors. Its pass@1 roughly doubled on both the single-table set and the harder multi-table FinQA reasoning set, and each run cost under $500. The speaker also argues for rubric-based evals, which split a response into sub-questions to locate the behavior to target, while RL still optimizes a single scalar reward. The talk is partly promotional for Snorkel's data offering, but it reports concrete before-and-after behavior and numbers.

## Key ideas
- **A bigger model was not the fix. A 4B model tuned for tool use beat a 235B model on the same financial tool-use questions.** — The goal was to get a smaller model to match a larger one on cost, speed, and on-prem deployability. RL was chosen because the target was changing behavior rather than adding knowledge. ([2:29](https://youtu.be/TNwJ1LMiENk?t=149))
- **The large model's failure was tool discipline, not reasoning.** — The 235B model queried a table that did not exist, never listed the available tools, retried once more without success, and then made up an answer. Its reasoning was strong but unused. ([6:14](https://youtu.be/TNwJ1LMiENk?t=374))
- **Data quality means expert-written tasks plus a verification pass.** — Domain experts (including PhD-level and industry practitioners) write the questions. A separate step checks that each task can be queried and has a verifiable answer before training. ([10:00](https://youtu.be/TNwJ1LMiENk?t=600))
- **The tuned 4B model's gain came from a fixed sequence of tool calls: list tables, inspect schema, query, then self-correct.** — After an error about a nonexistent revenue column, the model read the error and corrected the column name. The speaker says this discipline is what drives success on these questions. ([14:14](https://youtu.be/TNwJ1LMiENk?t=854))
- **Single-table-only training beat mixed and curriculum training, and the gain carried over to harder multi-table questions.** — In the ablation, single-table-only training gave the largest uplift. The multi-table benchmark also roughly doubled, so the speaker concludes that fixing one core failure mode generalizes. ([16:12](https://youtu.be/TNwJ1LMiENk?t=972))
- **Rubric evals help find which behavior to target, but RL still uses a single score.** — Breaking each response into yes/no sub-questions shows where it fails. Those findings decide which data to generate. The RL reward stays a single value, which GRPO expects. ([18:40](https://youtu.be/TNwJ1LMiENk?t=1120))

## Techniques
- **Behavior-targeted RL with GRPO on a tool environment** — Start from a small base model (4B). Build an environment that exposes the tools and the database, with no external dependencies. Train with GRPO on verifiable question-answer pairs. Run the RL framework from UC Berkeley's RLM group. *When:* When a model's failure is about how it uses tools rather than what it knows, and you need a cheap, self-hosted model.
- **Single-table-first training data** — Train only on single-table questions instead of a mixed or curriculum set. The speaker reports this gave the best results on both the easy and the harder multi-table sets. *When:* When the target skill is basic tool discipline, and harder multi-step cases are expected to generalize from it.
- **Verification pass on generated tasks** — After experts write tasks, check each one for queryability and a verifiable answer before using it for training. *When:* Before RL, whenever training data is written by people or generated and bad tasks would waste compute.
- **Rubric decomposition for diagnosis** — Break a response's correctness into a list of yes/no sub-questions (for example, did it list tables, did it recover from an error). Use the per-item results to decide what data to generate. Keep a single scalar reward for the RL update. *When:* When a final pass/fail score does not show why the model fails.
- **Publish the environment as a portable package** — Package the environment as self-contained so it runs anywhere, and publish it to shared hubs (OpenEnv, Prime Intellect, Hugging Face Spaces). *When:* When you want others to reuse an RL environment for tool-use training.

## Numbers
- Parameter counts compared: a 4B model versus a 235B model (Qwen3) on tool use for financial analysis. ([2:29](https://youtu.be/TNwJ1LMiENk?t=149))
- RL run took about 21 hours (as auto-captioned) and cost under $500 per run. ([11:22](https://youtu.be/TNwJ1LMiENk?t=682))
- Pass@1 roughly doubled on FinQA, and the 4B model outperformed the 235B model. ([14:14](https://youtu.be/TNwJ1LMiENk?t=854))
- Multi-table FinQA reasoning benchmark rose from 13.9 to 26.6 percentage points after training (transcribed as a 'percentage jump'). ([17:13](https://youtu.be/TNwJ1LMiENk?t=1033))
- Benchmark sizes: FinQA has 290 samples; FinQA reasoning (multi-table) has 79 samples. ([12:42](https://youtu.be/TNwJ1LMiENk?t=762))

## Hot takes
- Sometimes the answer is not a bigger model; the right behavior training on a smaller one can beat it.
- For this task, tool discipline mattered more than reasoning strength.
- Single-table-only training beat mixed and curriculum training.
- A useful RL run for under $500 is now practical for teams hosting their own models.

## Tools mentioned
GRPO, RLM framework (UC Berkeley), FinQA environment (Snorkel), OpenEnv, Prime Intellect, Harbor, GetTableNames / GetTableInfo tools, Qwen3

## Relevance to our work
- **agentos** (1/3): AgentOS plans RAGAS evals and failure-mode analysis for its own agents. The rubric breakdown of tool-use failure is a concrete method to try there. → *Add per-step rubric checks to the agent eval suite (for example, did the agent list tools before querying, and did it recover from an error) and report them next to the final pass/fail.*
- **prosharness** (1/3): ProsHarness runs Claude Code in long checkpointed runs. The talk's main finding is that agents skip tool discovery and invent answers, which a harness could check for. → *Add a check in the ProsHarness plan step that the agent inspects available tools and schema before issuing actions, and log cases where it does not.*
- **general** (1/3): Relevant to the recurring interest in small cheap models for pipelines: a 4B model can be made to beat a 235B model on one narrow task for about $500 of RL. → *Read the Snorkel/UC Berkeley write-up and the OpenEnv FinQA environment to see whether a small-model RL run is worth trying for a narrow agent task.*
