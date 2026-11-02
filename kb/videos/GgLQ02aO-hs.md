# The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `GgLQ02aO-hs` · [watch](https://youtu.be/GgLQ02aO-hs) · **date:** 2026-08-18 · **length:** 17:11 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Maxime Rivest, Isaac Miller · **orgs:** DSPy, Shopify, MIT, UC Berkeley
- **topics:** evals, agent-architecture, data-engineering · **tags:** dspy, prompt-optimization, signatures, specs-code-evals, qualitative-learning, recursive-language-models, gepa, cost-reduction, structured-extraction

> DSPy maintainers argue AI programs should be functions with fixed typed contracts, with the model, prompts and harness swappable underneath and optimized against evals.

## Summary
Maxime Rivest and Isaac Miller present DSPy as a way to make AI programs behave like functions: a named task with typed inputs and outputs, reusable and composable, with the implementation hidden behind the contract. They say a task is only fully specified when three things are written down: instructions (what should happen), code constraints (what must always hold, enforced in code rather than prompt text), and examples or evals (what good looks like). Once specified, an optimizer can search over prompts, few-shot examples, and harnesses without changing the interface. They claim enterprise users get cheaper implementations (Shopify is cited at 550x cheaper after moving to a cheap model with the same evals) and that new research techniques such as Recursive Language Models can be tried with a one-line change. They preview DSPy.Flex, a module that learns a harness per function, and qualitative learning, a research direction that turns production feedback (traces, user actions, analytics) into evals the system can climb. The talk is given by the DSPy maintainers, so the project framing is promotional; the concrete points are the spec/constraint/eval split and the cost claim with a named case.

## Key ideas
- **Treat a repeated AI task as a function with a fixed input/output signature** — The contract (named inputs, outputs, natural-language instruction) stays stable, so the model, the reasoning strategy and the internals can change without touching callers. Packaged modules can be shared and used as black boxes. ([1:16](https://youtu.be/GgLQ02aO-hs?t=76))
- **A task needs three specs: instructions, constraints, and examples** — Instructions say what should happen. Code constraints say what must always hold (checked in code, not left to the model). Examples or evals say what good looks like, including long-tail successful behaviour that is hard to state in words. Only with all three can an optimizer work. ([7:50](https://youtu.be/GgLQ02aO-hs?t=470))
- **Enforce hard requirements in code around the LLM call** — Example: run a cheap predictor first, fall back to chain-of-thought if extraction fails, and raise to a human if a value is negative. The speaker wants these guards to hold even if the model improves. ([6:50](https://youtu.be/GgLQ02aO-hs?t=410))
- **Cheaper implementations come from keeping the interface and evals fixed** — Because the contract and evals stay constant, a team can swap an expensive model for a cheap one and keep iterating on the internals. The speaker cites Shopify at 550x cheaper. ([9:51](https://youtu.be/GgLQ02aO-hs?t=591))
- **New techniques should plug in without changing the signature** — Recursive Language Models are offered as a one-line change for long-context tasks. The speaker stresses that no technique is guaranteed to help; the user must check it against their own problem. ([10:53](https://youtu.be/GgLQ02aO-hs?t=653))
- **Optimization has moved from few-shot examples to prompts to harnesses** — The speaker describes DSPy's history: first few-shot examples, then instructions, then harnesses, and now evals that evolve over time. DSPy.Flex is a module that learns a harness for one function. ([11:57](https://youtu.be/GgLQ02aO-hs?t=717))
- **Qualitative learning tries to build evals from real-world feedback** — Evals are hard because defining good loses detail and a dataset is only a proxy for reality. The idea is that a model reads textual feedback from traces, user actions and analytics, and turns it into a measure to climb. The speaker calls it an open research question. ([13:03](https://youtu.be/GgLQ02aO-hs?t=783))
- **Judge any new technique by a data-driven check on your own problem** — Define the business problem, then hold prompts, models and code accountable to it. The speaker says this lets a team benefit from techniques invented across the community. ([15:12](https://youtu.be/GgLQ02aO-hs?t=912))

## Techniques
- **Typed signature with natural-language instruction** — Declare inputs and outputs with types and a short instruction, and keep the instruction separate from the model and strategy wrapped around it. *When:* Any repeated LLM task that callers depend on, such as invoice field extraction or text rewriting in a keyboard shortcut.
- **Three-part task spec (instructions, code constraints, examples)** — Write the instruction in language, enforce invariants in code (rerun with reasoning on failure, raise on invalid values), and supply examples or an eval metric for the optimizer. *When:* When a task has hard rules that must never be broken, or when stating the goal in words loses detail.
- **Predict-then-reason fallback in code** — Run a vanilla predictor first. If the output is missing or invalid, rerun the same signature with chain-of-thought. *When:* When most inputs are easy and cheap calls should be the default, with reasoning used only as a fallback.
- **Optimizer over a fixed metric** — Keep the metric and dataset constant and let the optimizer search prompts, few-shot examples or instructions. *When:* When you have an eval set and want to compare cheaper models or prompts without rewriting the pipeline.
- **Learn a harness per function (DSPy.Flex, announced)** — A module that learns its own harness for one function, judged by the same metric. *When:* Future work per the speaker; relevant when one function needs a different strategy than the rest of the program.

## Numbers
- Shopify moved to a cheaper model while keeping the same evals: about 550x cheaper implementation (speaker's figure, not verified in talk) ([9:51](https://youtu.be/GgLQ02aO-hs?t=591))
- DSPy has been focused on specs, code and evals since 2022 ([15:12](https://youtu.be/GgLQ02aO-hs?t=912))
- Three enterprise case studies are referenced and linked after the talk; none are detailed on stage ([9:51](https://youtu.be/GgLQ02aO-hs?t=591))

## Hot takes
- Intelligence is not all-knowing: even AGI will not know your business context, so last-mile learning from your own feedback is still needed.
- Hard requirements belong in code around the model, not in prompts, and should hold even as models improve.
- Evals are a proxy for reality; the goal is to build evals automatically from production feedback.

## Tools mentioned
DSPy, GEPA (transcript says JEPA; caption error, prompt optimizer from Berkeley), Recursive Language Models (RLM), MultiModule GRPO, BetterTogether, DSPy.Flex (announced for DSPy 4)

## Relevance to our work
- **general** (2/3): Entity-resolution matching is a classification task with a fixed metric (F0.5). Fixing the signature and eval set and optimizing the prompt could show whether a cheap Haiku-class model can match the current pipeline. This is a test of the speaker's cheap-model claim, which is not proven here. → *On the ER matcher, keep the dev eval set and F0.5 metric fixed, write the match decision as a typed signature, and run a prompt optimizer to see whether a Haiku-class model reaches the current F0.5 (0.961 on the rule matcher is the baseline to beat).*
- **agentos** (1/3): AgentOS is a proxy with pluggable pillars and an eval layer (RAGAS). DSPy's typed-signature and optimizer approach could inform how modules are swapped, but the talk is about app-level programs, not infra. → *Skim DSPy's optimizer docs and compare its metric-driven search with the RAGAS eval layer in MemoryMesh; decide whether any AgentOS module needs a typed contract.*
- **prosharness** (1/3): ProsHarness runs plan, critique and debate steps around Claude Code. The talk's point that hard invariants should be checked in code, not left to the model, applies to its checkpoint and gate logic. → *Review ProsHarness's checkpoint and critique gates and move any invariant that currently lives only in a prompt into code checks.*
