# If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `O84lhGc1OOI` · [watch](https://youtu.be/O84lhGc1OOI) · **date:** 2026-09-18 · **length:** 17:55 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Benjamin Clavié · **orgs:** Mixedbread, Hugging Face, Snowflake, Google
- **topics:** rag-retrieval, multi-agent, evals, context-engineering · **tags:** knowledge-agents, agentic-search, bm25, hybrid-search, multimodal-retrieval, browsecomp-plus, matqa, subagents, oracle-gap, tool-design

> Benjamin Clavié (Mixedbread) argues agents should be designed as knowledge workers, not coding agents, and uses BrowseComp-Plus and MatQA results to show that tooling and search orchestration drive accuracy.

## Summary
Clavié argues that agent design has been shaped by coding, which is an unusually easy form of knowledge work: code has durable identifiers, a narrow grep-able surface, and narrow tickets. Real knowledge work (legal, medical, financial) has implicit meaning, the same term can mean different things, and tasks are open-ended. He frames tooling as the thing that makes a task cheap enough to scale, not just possible. On BrowseComp-Plus, a badly tuned BM25 scores about 60%, optimized lexical search reaches 70-80%, and a hybrid harness reaches about 90% (90.2%) with about 20% fewer tool calls. On MatQA (PDF enterprise tasks), a multimodal search tool beats OCR-text search, but his agent still trails the human score (88.9 vs 99.4). A manager agent that splits the query into aspects and dispatches searcher subagents that return memos adds about 3.5 points, and by his account it cuts the oracle gap by about 40%. He closes by saying tools should be co-designed with the agent, that models should know several retrieval primitives (grep, BM25, semantic search) rather than defaulting to grep, and that context is finite, so search has to be orchestrated.

## Key ideas
- **Design agents as knowledge workers, not coding agents.** — Knowledge work takes information as its main input and produces a judgment or decision. Most white-collar workflows fit this; coding is only one part of it. ([0:08](https://youtu.be/O84lhGc1OOI?t=8))
- **Coding is an easy special case for agents.** — Code has durable identifiers, a narrow grep-able surface, and narrow tickets. Legal and medical knowledge has implicit meaning and open-ended tasks, so grep alone does not cover it. ([3:55](https://youtu.be/O84lhGc1OOI?t=235))
- **Context-dependent meaning is the hard part of non-code knowledge.** — The same term (e.g. '30 days') can be a deadline, a grace period, or a retention rule, depending on the domain. Conditions are not predefined in the task and the agent has to find them. ([5:08](https://youtu.be/O84lhGc1OOI?t=308))
- **Tooling decides what is scalable, not just what is possible.** — A tool such as a library catalog or search engine changes a task from weeks to minutes, so people actually do the work. He frames tool and organizational changes as one loop. ([6:28](https://youtu.be/O84lhGc1OOI?t=388))
- **Tune the baseline before rejecting a method.** — On BrowseComp-Plus, a poorly tuned BM25 gives about 60% and an optimized one 70-80%. Claims that BM25 is weak often compare against an untuned version. ([9:06](https://youtu.be/O84lhGc1OOI?t=546))
- **Hybrid search reduces tool calls as well as raising accuracy.** — The hybrid harness reaches about 90% with about 20% fewer tool calls, which means fewer tokens and less cost. ([10:07](https://youtu.be/O84lhGc1OOI?t=607))
- **Multimodal retrieval over PDFs beats OCR text, but a single agent still leaves a gap.** — On MatQA, a multimodal search tool gives a large jump, but the agent scores 88.9 against 99.4 for the human. Tables and layout are part of the problem. ([12:50](https://youtu.be/O84lhGc1OOI?t=770))
- **Split the search: a manager agent dispatches searcher subagents.** — The manager breaks the question into aspects and writes queries for each. Searchers work independently and return short memos, which the manager uses to answer. This adds about 3.5 points and narrows the oracle gap. ([14:16](https://youtu.be/O84lhGc1OOI?t=856))
- **Co-design tools with the model and train it on several retrieval primitives.** — Agents default to grep because it is common in training data, but PDFs need semantic search. Tools exist to overcome performance ceilings, and the model has to know when to use each primitive. ([15:38](https://youtu.be/O84lhGc1OOI?t=938))
- **Context is finite, so orchestrate the search.** — Even a 100M-token window is costly and still not enough for a large legal corpus, so the task has to be broken down and organized across agents. ([16:54](https://youtu.be/O84lhGc1OOI?t=1014))

## Techniques
- **Manager-plus-searcher subagents for open-ended retrieval** — A top-level agent splits the question into aspects, writes a query for each, and runs separate searcher agents. Each searcher returns a short memo, and the manager writes the answer from the memos. *When:* Open-ended research over thousands of documents, where a single agent's context or query breadth is the bottleneck.
- **Optimize the lexical baseline before comparing** — Tune BM25 (parameters, tokenization, normalization) and report optimized versus unoptimized numbers, not one default run. *When:* Before deciding that keyword search is too weak, or before picking a baseline for an agent-search benchmark.
- **Hybrid search harness** — Combine lexical search (BM25) with semantic search in one tool harness, so the agent gets both signals. *When:* Retrieval tasks where exact terms and meaning both matter, and tool-call count drives cost.
- **Multimodal PDF search instead of OCR text** — Index PDF pages visually with a vision-capable model so tables and layout survive retrieval. *When:* Enterprise document collections where OCR loses tables or structure.
- **Teach the agent its retrieval primitives** — Make the model aware of several tools (grep, BM25, semantic search) and train or prompt it to choose between them, instead of letting it default to grep. *When:* Agents that search heterogeneous corpora, such as PDFs mixed with code-like text.

## Numbers
- BrowseComp-Plus: badly tuned BM25 about 60% accuracy; optimized lexical search 70-80%; hybrid harness about 90% (90.2%), with about 20% fewer tool calls. ([9:06](https://youtu.be/O84lhGc1OOI?t=546))
- BrowseComp-Plus: the speaker says the hybrid result costs about 5% of the unoptimized baseline's spend. The wording is ambiguous. ([10:07](https://youtu.be/O84lhGc1OOI?t=607))
- BrowseComp-Plus corpus size is said as 200,000 documents at 9:06 and 100,000 at 10:07. The auto-captions disagree, so treat it as unverified. ([9:06](https://youtu.be/O84lhGc1OOI?t=546))
- MatQA: the agent scores 88.9 against 99.4 for the human, an gap of about 10 points. A human given unlimited BM25 searches still cannot match the target, so the tool is the limit. ([12:50](https://youtu.be/O84lhGc1OOI?t=770))
- Searcher-subagent architecture adds 3.5 accuracy points and cuts the oracle gap from about 10 points to about 6 (a stated 40% reduction in mistakes). ([14:16](https://youtu.be/O84lhGc1OOI?t=856))
- Context window: even 100M tokens is described as a small fraction of one state's legal code. ([16:54](https://youtu.be/O84lhGc1OOI?t=1014))

## Hot takes
- Grep working for coding does not mean agents can do legal or medical research, because the knowledge task is not narrow.
- BM25 is not weak in general. Most people who call it weak are comparing against an untuned version.
- Tools exist to overcome ceilings, so a tool should only be added when measured performance hits a ceiling.
- Long context will not solve knowledge work. Orchestrated search is required even with 100M-token windows.

## Tools mentioned
BM25, Gemini, Claude Code, Codex, Mixedbread search tool

## Relevance to our work
- **agentos** (2/3): MemoryMesh already has hybrid retrieval (BM25 + pgvector), and the talk gives tuned-baseline and tool-call-count evidence for that choice. → *Benchmark MemoryMesh with a tuned BM25 baseline against the current hybrid path, and log tool calls per query as a cost metric.*
- **prosharness** (1/3): The manager-plus-searcher-subagent split is a planner/worker pattern, similar to ProsHarness plan and debate steps. → *Read the talk's subagent memo pattern and check whether a research-style plan step should return a memo to a manager instead of full context.*
- **general** (1/3): Its advice on tuned baselines, multi-primitive retrieval and orchestration applies to recurring interests in context engineering and subagents. → *Skim the talk's slides or paper for the MatQA and BrowseComp-Plus setups before choosing a retrieval baseline for the next eval.*
