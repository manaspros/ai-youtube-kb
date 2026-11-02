# It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `xo68uCibfm8` · [watch](https://youtu.be/xo68uCibfm8) · **date:** 2026-09-18 · **length:** 20:48 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kevin Madura · **orgs:** AlixPartners
- **topics:** context-engineering, agent-architecture, multi-agent, data-engineering · **tags:** RLM, recursive-language-models, REPL, DSPy, subagents, long-context, context-rot, structured-outputs, dataframes, harness-optimization, Halo

> Kevin Madura (AlixPartners) explains recursive language models (RLMs): the context lives as a variable in a Python REPL, and the model writes code and delegates subcalls to sub-LMs, so only useful results return to the main context.

## Summary
The talk defines an RLM as a model that treats its input as a symbolic object inside a REPL, unlike a tool call that passes strings back and forth. The model can make subcalls to other LMs (often itself) from inside that environment, so it can decompose problems recursively and keep the full input out of its own context window. The speaker argues this avoids context rot, because the main model only sees the results that matter. He shows benchmark charts (OOLONG, BrowseComp) and a cited test on long chain-of-thought tasks, and says RLMs suit large or dense inputs, large outputs, and decomposable long-horizon work, but not small inputs or low-latency needs. He gives a dataframe cohort-analysis example where the model writes code against the data directly and decides when to call submit, bounded by a max-iteration setting. He points to PredictRLM (which uses DSPy signatures to type the main-to-sub-LM handoff), fastRLM, AXE, and the Halo project, which runs an RLM over agent traces to propose harness changes. He closes by arguing RLM-aware post-trained models would be a large step.

## Key ideas
- **An RLM treats the input as a variable in a symbolic environment (usually a Python REPL), not as a string returned by a tool call.** — The model writes code to slice, search and compute over the input, so the logic, execution and results stay tightly coupled. The speaker contrasts this with RAG, agents and CodeAct, where results come back as strings. ([0:12](https://youtu.be/xo68uCibfm8?t=12))
- **Recursion is the second key difference: the model can delegate subcalls to another LM, often itself, from inside the REPL.** — Sub-LMs can do the same thing, so problems decompose recursively. The model decides how to apply logic, or writes its own code to do it. ([0:12](https://youtu.be/xo68uCibfm8?t=12))
- **Keeping the full input out of the main context window is the main benefit, because performance degrades as context fills (context rot, the 'dumb zone').** — The input lives as a REPL variable. The main model only gets back the results that matter, so its context grows more slowly. ([5:46](https://youtu.be/xo68uCibfm8?t=346))
- **Use an RLM for large or dense inputs, large outputs, and decomposable long-horizon tasks. Skip it when the input fits in context or when latency matters.** — Examples given are a 30,000-token input with 12 numbers buried in it (regex-friendly, base models struggle) and whole-tax-code loophole search with subagents exploring sections. ([8:41](https://youtu.be/xo68uCibfm8?t=521))
- **Define a deterministic shell (inputs, outputs, intent) around the model and let it decide the middle, in the DSPy style.** — The speaker says this matters more as models improve. The guarantees sit on the I/O types, so the internal decomposition can change without breaking the pipeline. ([4:25](https://youtu.be/xo68uCibfm8?t=265))
- **Give the model a stopping rule: a max-iteration cap plus a submit call that returns typed outputs.** — The LM decides when it is done and calls submit. The cap (for example 10 or 100 iterations) bounds cost. ([14:15](https://youtu.be/xo68uCibfm8?t=855))
- **Structure the main-to-sub-LM handoff with typed schemas. PredictRLM does this with DSPy.** — The speaker expects this to help cheaper models, since sub-LM outputs are forced into the declared types. He has not tested this. ([16:38](https://youtu.be/xo68uCibfm8?t=998))
- **Halo applies an RLM to agent traces to recommend harness changes, rather than tuning a single workflow or prompt.** — Traces get long and complex, and the RLM can use their structure. The speaker ran a related experiment on a vulnerable OWASP web app with a very large codebase to produce a security report. ([18:37](https://youtu.be/xo68uCibfm8?t=1117))

## Techniques
- **REPL-held context with sub-LM delegation** — Store the full input as a Python variable. Let the main model write code to search, slice and compute over it, and call sub-LMs on the relevant chunks. Return only the sub-results to the main context. *When:* Input is too large or dense for one context window, or the task splits into independent pieces (log analysis, long contracts, invoice folders).
- **Typed I/O shell around an autonomous core** — Declare the input fields, output fields and an intent or guidance string (DSPy-style). Let the RLM choose the internal steps, and rely on the I/O types as the contract. *When:* You want reliable interfaces between pipeline stages but are happy for the model to choose how to get there.
- **Schema-enforced sub-LM handoff** — Give each sub-LM call an explicit output schema (PredictRLM uses DSPy to define it) so results come back in a parseable, known shape. *When:* Sub-calls go to cheaper models, or the main model needs predictable fields from many sub-calls.
- **Bounded self-terminating loop** — Set a max-iteration variable. The model explores, then calls submit with the typed final output when satisfied. *When:* Open-ended exploration where you need a cost ceiling but cannot predict how many steps are needed.
- **Dataframes in the REPL instead of JSON tool results** — Load the dataframes into the REPL and let the model run pandas-style code against them, iterating on the results directly. *When:* Tabular analysis such as cohort retention, where JSON round-trips would bloat context.
- **Trace-driven harness optimization (Halo)** — Run an RLM over agent execution traces and ask it to recommend changes to the harness, not to a single prompt or workflow. *When:* You have many long agent traces and want to improve the harness that runs the agent.

## Numbers
- On a long chain-of-thought benchmark, accuracy went from 2.6% to 45.4% with an RLM. The speaker cites this as Raymond's testing, not his own run. ([8:41](https://youtu.be/xo68uCibfm8?t=521))
- OOLONG and BrowseComp charts show the RLM at the top on performance. On cost, a GPT-5 BM25 tool-calling baseline is more expensive and performs worse than the RLM. No exact figures are stated in the talk. ([3:04](https://youtu.be/xo68uCibfm8?t=184))
- Example task: sum 12 numbers buried across about 30,000 tokens. Base models struggle with it, while code can do it easily. No RLM result is given. ([8:41](https://youtu.be/xo68uCibfm8?t=521))
- On the same tasks, Claude Code was described as 'totally bloated' in how it solved them. The speaker gives no figures and says the comparison is not fully fair. ([10:06](https://youtu.be/xo68uCibfm8?t=606))
- The max-iteration setting can be 10 or 100. The model decides when to call submit. ([14:15](https://youtu.be/xo68uCibfm8?t=855))
- The dataframe cohort-analysis example needed roughly 20 lines of code, with three dataframes fed in. ([12:54](https://youtu.be/xo68uCibfm8?t=774))
- A security-review experiment ran an agent over about 500,000 lines of code, using an intentionally vulnerable OWASP app. ([20:03](https://youtu.be/xo68uCibfm8?t=1203))

## Hot takes
- The approach is 'bitter lesson pilled': defer more and more to the model as models get better, rather than engineering the context yourself.
- Context engineering can largely be skipped by throwing the input at an RLM and letting it decide.
- Running a coding agent with 'claude -p' and hoping for a good result is not how production workloads should be run; a structured input/output pipeline is better.
- Post-trained, RLM-aware models would make things 'pretty crazy pretty quick'.

## Tools mentioned
DSPy, PredictRLM, fastRLM, AXE, Halo, Claude Code, GPT-5, Anthropic Workflows, pandas

## Relevance to our work
- **general** (2/3): Directly relevant to context engineering and subagent design. Typed sub-LM handoffs and a bounded submit loop are concrete patterns for multi-agent work. The numbers are cited, not verified. → *Look up the PredictRLM and DSPy signature approach for typed subagent handoffs, and try it on one existing multi-agent pipeline.*
- **agentos** (1/3): Long-context and context-rot ideas touch the MemoryMesh retrieval layer. The RLM REPL pattern is an alternative to chunk-and-retrieve, but the talk has no retrieval benchmarks. → *Run one long-document QA eval comparing MemoryMesh hybrid retrieval against an RLM-style REPL pass with a sub-LM. Do this before adding more retrieval tiers.*
- **prosharness** (1/3): The Halo idea of using traces to improve the harness matches ProsHarness's plan-critique-debate loop. The talk gives no results. → *Read the Halo project and consider a trace-review step that proposes harness changes from ProsHarness run logs.*
