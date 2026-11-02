# How to use Reasoning Models Correctly?

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `w42_sbxa08w` · [watch](https://youtu.be/w42_sbxa08w) · **date:** 2025-11-02 · **length:** 8:10 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS narrator (unnamed) · **orgs:** OpenAI, Google, DeepSeek, Anthropic
- **topics:** context-engineering, models-research, multi-agent · **tags:** reasoning-models, prompt-engineering, chain-of-thought, few-shot, delimiters, developer-messages, planner-workhorse, openai-docs

> Walkthrough of OpenAI's Reasoning Best Practices doc: keep prompts direct, skip chain-of-thought instructions, use delimiters, go zero-shot first, and use reasoning models as planners with cheaper models executing.

## Summary
The AI LABS video reads through OpenAI's "Reasoning Best Practices" documentation and adds one example prompt credited to a third party (Alvaro Sintas, via X). The core advice is to keep prompts short and direct, and to stop asking reasoning models to "think step by step", since they already reason internally. Inputs should be separated with delimiters such as markdown headers, XML tags or section titles, typically ordered as context, examples, then instructions. Start with zero-shot prompts and add few-shot examples only for edge cases, keeping the examples consistent with the instructions. Constraints should be explicit, along with the goal they serve. Over the API, the developer message replaces the system message, and markdown formatting is suppressed unless a formatting re-enable line is included. The video also covers when to use reasoning models (ambiguous tasks, needle-in-a-haystack extraction, multi-step planning, visual reasoning) and presents OpenAI's planner/workhorse pattern: a reasoning model plans and validates, and non-reasoning models execute. Most of the material restates vendor guidance, with little independent testing.

## Key ideas
- **Keep prompts simple and direct; drop extra words and fluff.** — The narrator presents this as the first OpenAI tip, saying many people over-complicate prompts. ([0:00](https://youtu.be/w42_sbxa08w?t=0))
- **Do not add chain-of-thought instructions to reasoning models.** — Telling a reasoning model to think step by step or explain its reasoning is unnecessary because it already reasons internally. ([0:00](https://youtu.be/w42_sbxa08w?t=0))
- **Use delimiters to separate context, examples and instructions.** — Markdown, XML tags or section titles help the model parse structured input, which the narrator links to more accurate output. ([1:27](https://youtu.be/w42_sbxa08w?t=87))
- **Try zero-shot first and add few-shot examples only when needed.** — Reasoning models often predict the desired output without examples. Add examples for edge cases or when output misses, and keep them aligned with the instructions. ([1:27](https://youtu.be/w42_sbxa08w?t=87))
- **State constraints explicitly and include the goal they serve.** — Illustrated with a $500 budget: the model should be told what the budget is for so its iterative reasoning stays focused. ([2:51](https://youtu.be/w42_sbxa08w?t=171))
- **Over the API, the developer message replaces the system message and suppresses markdown by default.** — To get markdown or code blocks back, the developer message needs a formatting re-enable string on its first line. The narrator quotes it as 'string formatting re-enabled'; check the doc for the exact wording. ([2:51](https://youtu.be/w42_sbxa08w?t=171))
- **Planner/workhorse pattern for agent systems.** — In OpenAI's customer-service example, o1 turns policy documents into structured routines, GPT-4o mini and GPT-4o execute the steps, and o3-mini validates the results. Reasoning models plan and check; cheaper non-reasoning models execute. ([4:16](https://youtu.be/w42_sbxa08w?t=256))
- **Reasoning models fit ambiguous tasks, large unstructured data and multi-step planning.** — The narrator lists four uses: asking for clarification on ambiguous prompts, pulling specific facts from large unstructured data, planning multi-step agent work, and delegating subtasks to models sized to their compute needs. Visual reasoning on architectural drawings is also cited. ([5:36](https://youtu.be/w42_sbxa08w?t=336))

## Techniques
- **Section the prompt into Context / Examples / Instructions** — Wrap each part in a delimiter (markdown headers, XML tags such as <context>, <examples>, <instructions>, or titled sections). Put background in context, style or format samples in examples, and the task with its limits in instructions. *When:* Any prompt to a reasoning model that combines background material, examples and a task.
- **Drop chain-of-thought scaffolding** — Remove phrases such as 'think step by step' or 'explain your reasoning' from prompts sent to reasoning models. *When:* When migrating prompts written for non-reasoning models to o-series or other reasoning models.
- **Zero-shot first, then few-shot** — Send the instructions with no examples. If the output misses or edge cases fail, add examples that closely match the wording and constraints of the instructions. *When:* Default for reasoning models; add examples only after a zero-shot failure.
- **Explicit constraints plus goal** — Write each limit as a concrete condition (for example, a $500 budget) and add one sentence on what the constraint is for. *When:* Tasks with budgets, quotas, audience or tone requirements.
- **Re-enable markdown in developer message (API)** — Put the formatting re-enable string on the first line of the developer message. The narrator says the string is 'string formatting re-enabled'; confirm the exact wording in OpenAI's Reasoning Best Practices doc before relying on it. *When:* When calling reasoning models through the API and you need markdown or code blocks in the output.
- **Planner/workhorse agent split** — Use a reasoning model to turn inputs into a structured plan or routine, dispatch each step to cheaper non-reasoning models, then send results back to a reasoning model for validation. *When:* Multi-step agent workflows where planning is hard and execution steps are simple and high-volume.

## Numbers
- Illustrative budget of $500 used as a constraint example; no benchmarks, latencies or prices are given. ([2:51](https://youtu.be/w42_sbxa08w?t=171))

## Hot takes
- The speaker says Claude is 'much, much better' than GPT models at coding, with no evidence offered.
- Most of the video restates OpenAI's own documentation. The planner/workhorse example comes from OpenAI and is not independently tested.
- The prompt template is credited to a third party via X and is presented as a boilerplate, not measured against any baseline.
- Model names (o1, o3-mini, GPT-4o, GPT-4o mini) are those the video cites; check current OpenAI docs for the lineup in use.
- Quality is capped at 2 because the content is thin: a doc read-through with one unverified example and no measurements.

## Tools mentioned
OpenAI Reasoning Best Practices documentation, o1, o3-mini, GPT-4o, GPT-4o mini, Claude, Gemini, DeepSeek

## Relevance to our work
- **agentos** (1/3): Planner/workhorse split is a routing idea for the AgentOS strategy router, but the video offers no measured results and no routing design. → *Prototype a planner/executor route in AgentOS L1 strategy routing: a reasoning model drafts and validates the plan, cheaper models run the steps, and cost per step is logged.*
- **prosharness** (1/3): ProsHarness's plan step could use the delimiter and no-chain-of-thought advice before the Codex critique pass. → *Restructure the ProsHarness plan prompt into context / examples / instructions sections with delimiters and no 'think step by step', then compare plan quality against the current prompt.*
