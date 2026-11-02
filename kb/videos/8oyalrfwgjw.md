# RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `8oyalrfwgjw` · [watch](https://youtu.be/8oyalrfwgjw) · **date:** 2026-07-18 · **length:** 17:27 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Shashi · **orgs:** Superagentic AI, MIT, Google, OpenAI, Anthropic, DSPy
- **topics:** context-engineering, coding-agents, agent-architecture · **tags:** RLM, recursive language models, large codebases, REPL, context management, llm_query, sub-calls, trajectory logging, budgets, Docker sandbox, Gemini, monorepo

> Shashi (Superagentic AI) explains Recursive Language Models (RLM) for large codebases: keep the repo in a REPL, let the model write code to slice it, and call sub-models in a loop. He demos his open-source RLM Code harness with Gemini.

## Summary
The talk argues that coding agents degrade on large monorepos because context grows too big. It contrasts the usual fixes (grep-style tool search, semantic search, summarizing or compressing context, memory products) with RLM, which keeps the whole repo outside the prompt as data in a programmable REPL. The model writes code to inspect and slice the repo, returns bounded observations to its context, and calls a sub-model (llm_query) when it needs a specialist answer, looping until it synthesizes a final answer. The speaker picks codebases as the test case because code is structured (directories, imports, configs, tests), not just prose. He stresses RLM is a pattern, not a package, and that his RLM Code harness is a reference implementation separate from the MIT paper and from DSPy's version. The live demo runs Gemini in a Docker sandbox with step and recursion-depth budgets, and shows traces that can be exported as JSONL. He ends with use cases (root-cause analysis, onboarding, unfamiliar repos) and says, from X posts he has seen, that some proprietary harnesses seem to use similar REPL-based context curation; this is unverified. No benchmarks or cost figures are given.

## Key ideas
- **Large-repo context problem** — Coding agents work well on small repos but degrade as context grows, and monorepos make it worse. Grep-style search, semantic search, summarization and memory tools are the usual workarounds. ([0:00](https://youtu.be/8oyalrfwgjw?t=0))
- **Externalize context into a programmable environment** — The core RLM thesis: don't load the repo into the prompt. Treat the repo as data in a separate REPL that the model queries with code, then feeds only the relevant pieces back into its main context window. ([1:28](https://youtu.be/8oyalrfwgjw?t=88))
- **Recursion through sub-calls** — When the model needs a specialist answer, it calls another model via llm_query on a slice. The loop runs REPL code, gets bounded observations, makes sub-calls as needed, and ends with a synthesized answer. ([3:57](https://youtu.be/8oyalrfwgjw?t=237))
- **Codebases are structured data** — The speaker picked codebases over books or dictionaries because a repo has directories, imports, dependencies, tests, and configs. The model has to reason over structure, not just text. ([5:31](https://youtu.be/8oyalrfwgjw?t=331))
- **RLM is a pattern, not a library** — Official RLM and rlm-minimal implementations exist, and DSPy has its own RLM module. The speaker says these are different implementations of one pattern, and RLM Code is one more reference harness. ([6:34](https://youtu.be/8oyalrfwgjw?t=394))
- **Budgets and traces are part of the harness** — The demo caps max steps, recursion depth and spend per run. It also records planning, code, observations, sub-calls and the final output, exportable as JSONL to any observability tool. ([12:58](https://youtu.be/8oyalrfwgjw?t=778))
- **Use cases and unverified industry signal** — He suggests RLM-style harnesses for root-cause analysis, onboarding and unfamiliar repos. He says, from posts he saw on X, that Codex writes REPL Python to curate context and that some Anthropic engineers said they used RLM ideas; he does not verify these. ([15:33](https://youtu.be/8oyalrfwgjw?t=933))

## Techniques
- **REPL-based context slicing (RLM loop)** — Put the repo or large corpus in a REPL as a variable. The model writes code to search, slice and summarize it, returns only bounded observations to the main context, and calls llm_query on sub-questions until it can answer. *When:* Codebases or document sets too large for one context window, such as root-cause analysis, onboarding, or questions about an unfamiliar monorepo.
- **Recursive sub-calls with a budget** — Give the model an llm_query tool that spawns a sub-model on a slice. Set max steps, max recursion depth, and spend per run so the loop stops. *When:* Any recursive agent run on paid models, to keep cost and runaway loops bounded.
- **Full trajectory capture as JSONL** — Log each run's planning, REPL code, observations, sub-calls, budget use and final output. Export as JSONL and import into an observability platform, then review in a run browser. *When:* Debugging or evaluating a custom harness, or comparing runs of the same task.
- **Sandboxed REPL execution** — Run the model-written REPL code inside a Docker container so it cannot touch the host. *When:* Any time an agent executes model-generated code over a repo.
- **Model-agnostic sub-calls** — Route the root loop and the sub-calls to different models, local or cloud, and plug in any observability layer. The speaker says it also fits frameworks like Pydantic AI or Google ADK. *When:* When you want to cut cost by sending cheap sub-queries to a smaller or local model.

## Hot takes
- Context management should move out of the prompt into a programmable execution environment, instead of relying on grep, semantic search or summarization alone.
- Codebases are a better test case for recursive LMs than prose, because their structure (directories, imports, configs, tests) has to be reasoned over.
- RLM is a pattern to implement your own way, not a single package; the official, DSPy and RLM Code versions are different implementations.
- Speaker's unverified claim: proprietary coding harnesses (Codex, managed agents) already use REPL-based context curation.

## Tools mentioned
RLM Code, DSPy, Gemini, Docker, Codex, Pydantic AI, Google ADK, JSONL trace export

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code runs, so per-run step and spend budgets plus trajectory logs are directly relevant to its checkpoint/resume and loop design. → *Add per-run max-step and spend caps plus a JSONL trajectory log (plan, commands, observations, sub-calls) to ProsHarness runs, then check whether a checkpoint can resume from it.*
- **general** (2/3): Context engineering is a recurring interest. The talk gives a concrete alternative to grep, summaries and compaction for large repos. → *Run a small test: answer 5 questions about one large repo with a REPL-slicing loop versus grep-plus-compaction, and compare accuracy and tokens.*
- **agentos** (1/3): MemoryMesh's hybrid retrieval (BM25 + pgvector) is a different approach from REPL-based context slicing, but the talk offers an alternative for very large knowledge buckets. → *Read the RLM paper and sketch one REPL-style retrieval path for a large MemoryMesh bucket to compare with BM25 + pgvector on a fixed question set.*
