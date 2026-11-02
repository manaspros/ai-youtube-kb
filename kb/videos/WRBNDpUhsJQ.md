# Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `WRBNDpUhsJQ` · [watch](https://youtu.be/WRBNDpUhsJQ) · **date:** 2026-06-18 · **length:** 15:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Adrian Bertagnoli · **orgs:** Callosum, ARIA (UK), Cerebras, Stamanova
- **topics:** multi-agent, token-cost-efficiency, inference-serving · **tags:** heterogeneous-intelligence, recursive-language-models, multi-agent, model-routing, heterogeneous-hardware, cost-latency, video-web-arena, oolong, context-rot, subagents

> Adrian Bertagnoli (Callosum) argues AI is moving from homogeneous scaling to heterogeneous multi-agent systems mixing models, workflows and chips, and shows a recursive-LM variant that routes sub-contexts to different models and hardware for big cost and speed gains.

## Summary
The speaker frames the next paradigm as heterogeneous intelligence: different model architectures, sizes and chips working together, instead of scaling one model on identical chips. He says this is already happening in mild form (mixture of experts, multi-agent systems, prefill/decode disaggregation) and claims a formal, mathematical argument that heterogeneous systems beat homogeneous ones under reasonable constraints. The main technique is "heterogeneous recursion": build on recursive language models, which treat long context as an environment searched programmatically, and send each sub-context to a different model or chip. He reports a Cerebras-based version that is about 7x cheaper and 5x faster than GPT-5/5.2 on the OOLONG benchmark, with a Stamanova-based version reaching 12x cheaper and 3x faster. For visual web navigation, a mix of open and closed video-action models beats GPT-5.2 and Gemini 2.5 on VideoWebArena, with cheap models handling subtasks such as zooming. The talk is partly a company pitch (hiring, a UK grant), but it includes concrete benchmark numbers. The numbers come from the speaker's own system and are not independently verified in the talk.

## Key ideas
- **Scaling is moving from homogeneous (one model on identical chips) to heterogeneous (mixed models, workflows and hardware).** — Mixture-of-experts, multi-agent systems and prefill/decode disaggregation are already mild forms of heterogeneity. The next stages are different models on different chips, then co-evolution of hardware, software and models. ([0:59](https://youtu.be/WRBNDpUhsJQ?t=59))
- **Real problems decompose into sub-problems that need different kinds of intelligence, so one model type is inefficient.** — The speaker says the heterogeneity benefit is formalised and proved mathematically, using a production-function model that spans domains such as neuroscience, economics and ecology. He claims heterogeneous systems win under any reasonable constraints. This is the speaker's claim, not checked in the talk. ([3:34](https://youtu.be/WRBNDpUhsJQ?t=214))
- **Recursive language models treat long context as an environment, not as prompt text.** — The context is stored in a file, and an agent searches it with a Python REPL (keywords, regex). It extracts sub-contexts and passes each to a new recursive agent. Information-dense tasks degrade much earlier on long prompts than needle-in-a-haystack tasks. ([6:44](https://youtu.be/WRBNDpUhsJQ?t=404))
- **Heterogeneous recursion maps each recursive sub-call to a different model or chip.** — Instead of one model on one chip, each sub-context is routed to the model and hardware best suited to it. The speaker claims this matches frontier-model quality at much lower cost and latency. ([8:03](https://youtu.be/WRBNDpUhsJQ?t=483))
- **Decompose visual web tasks into reasoning steps and route each step to the cheapest adequate model.** — Zooming and other simple visual subtasks go to small models. Heavier reasoning goes to large models. The speaker says this beats single frontier models on the Pareto frontier with no quality downside. ([10:50](https://youtu.be/WRBNDpUhsJQ?t=650))
- **Routing is now automated: a layer detects task complexity and predicts the best model and hardware.** — The team started with hand-made mappings of simple subtasks to simple models. They later built an automation layer that predicts the best model and hardware per task. ([13:15](https://youtu.be/WRBNDpUhsJQ?t=795))

## Techniques
- **Heterogeneous recursion** — Use a recursive LM pattern: store context as a file, let a coding agent search it programmatically (regex, keyword search, sub-context extraction), and send each sub-context to a recursive agent. Map each recursive call to a different model and chip. *When:* Very long contexts with information-dense queries, where one model's context rot or cost is the bottleneck.
- **Subtask offloading to small models** — Split an agent workflow into visual, textual and control subtasks. Send simple steps such as zooming or cropping to cheap, small models and keep frontier models for hard reasoning. *When:* Multi-step agent tasks where most steps are simple and only a few need frontier reasoning.
- **Automated model and hardware routing** — Build a layer that estimates task complexity and predicts the best model and hardware for each step, replacing hand-written rules. *When:* When the set of task types and models grows past what hand-written mapping rules can cover.
- **Hardware-matched inference for sub-calls** — Run the cheap, fast sub-calls on fast-inference hardware (the speaker names Cerebras) and slower-but-cheaper models on other chips. *When:* When latency or cost per sub-call dominates total run time.

## Numbers
- Recursive LM degradation: information-dense (linear/quadratic) tasks degrade at around 60% to 30% of the context window, while constant-information tasks hold up. ([6:44](https://youtu.be/WRBNDpUhsJQ?t=404))
- OOLONG benchmark: GPT-5/5.2 takes about 2,000 seconds and about $3.75 per task. The Cerebras-based system is 7x cheaper and 5x faster. ([9:19](https://youtu.be/WRBNDpUhsJQ?t=559))
- Stamanova-based variant: 12x cheaper and 3x faster than the GPT-5 baseline, at some cost in latency. ([9:19](https://youtu.be/WRBNDpUhsJQ?t=559))
- VideoWebArena: beats GPT-5.2 by 18% and Gemini 2.5 by 25% using a mixed set of open and closed video-action models. ([9:19](https://youtu.be/WRBNDpUhsJQ?t=559))
- Qwen3-VL-8B plus Kimi K2.5 is 1.3x faster than Kimi alone and 18x cheaper than GPT-5.2 alone. Qwen3 plus GPT is 3x faster and 3.7x cheaper. ([10:50](https://youtu.be/WRBNDpUhsJQ?t=650))
- Offloaded subtasks such as zooming run 11x faster and 43x cheaper than using a frontier model. ([12:13](https://youtu.be/WRBNDpUhsJQ?t=733))
- A UK ARIA grant of about 3 million for a heterogeneous co-located cluster. ([13:15](https://youtu.be/WRBNDpUhsJQ?t=795))

## Hot takes
- Homogeneous scaling (one model on identical chips) is becoming less relevant, and heterogeneity is the next paradigm for AI infrastructure.
- Heterogeneous systems beat homogeneous ones under any reasonable constraints; the speaker says this is proven mathematically.
- The talk's own pitch: 'This is the worst our infrastructure will ever be.'

## Tools mentioned
Python REPL, Cerebras, Kimi K2.5, GPT-5.2, Gemini 2.5, Qwen3-VL-8B-Instruct, Stamanova

## Relevance to our work
- **agentos** (2/3): InferCraft already covers KV-cache and scheduling on one GPU. Routing sub-tasks to different models and hardware, plus a complexity-based router, fits the same layer. → *Prototype a complexity-based router in the L1 proxy that sends sub-calls to a cheap model or a larger one, and measure cost and latency on a long-context task.*
- **prosharness** (2/3): Sub-agent routing with a cheap model for simple steps and a frontier model for hard ones matches the harness's multi-agent and plan/critique design. Recursive sub-context handling also fits long agent runs. → *Read the recursive language models paper (MIT, Oct 2025) and test whether routing ProsHarness sub-agents to cheaper models keeps plan quality.*
