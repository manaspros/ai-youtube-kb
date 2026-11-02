# How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Tt2kX2sgQio` · [watch](https://youtu.be/Tt2kX2sgQio) · **date:** 2026-08-18 · **length:** 22:30 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vinoo Ganesh · **orgs:** Kepler, Anthropic, Palantir, Citadel, Bloomberg, FactSet, SEC, OCC
- **topics:** governance-compliance, data-engineering, enterprise-adoption, agent-architecture · **tags:** verifiable-ai, provenance, deterministic-substrate, financial-services, derivation-chains, finance-llm, numerical-accuracy, citations, audit-trail, model-vs-tool-split

> Kepler's CEO argues finance AI needs a deterministic substrate: the model points to sources and decides what to compute, while code extracts, checks and calculates numbers, with replayable derivation chains.

## Summary
Vinoo Ganesh, CEO of Kepler, argues that AI can draft financial work product but cannot verify it on its own, because models are probabilistic and finance needs numbers that can be traced and reproduced. He says citations are only an after-the-fact audit, and that real verification means a deterministic, numerically checkable path from source to output. His three principles are atomic provenance (the model writes a reference to a number, never the number itself, and unverifiable numbers are stripped), scope determinism (the model decides what to compute, while code does the extraction and arithmetic), and derivation chains (every derived metric records its inputs and transformations so it can be replayed). He says verification is defined by each firm's own rules rather than a single ground truth, so the same data can rightly yield opposite trades. He claims a fine-tuned extraction model reached 94% accuracy, which he says is not enough when the other 6% is wrong. The talk is partly a pitch for Kepler, and most of its concrete content is architecture rather than benchmarks.

## Key ideas
- **A citation is only an after-the-fact audit; verification means a deterministic, repeatable check that a number is right.** — He separates showing sources (citations) from proving a pulled figure matches its filing, and says the second is what finance needs. ([6:18](https://youtu.be/Tt2kX2sgQio?t=378))
- **Finance verification is path-dependent, not ground truth.** — Two desks can hold the same data and reach opposite trades. Verification therefore means output that follows the firm's own codified rules and sources, not one correct answer. ([7:45](https://youtu.be/Tt2kX2sgQio?t=465))
- **AI cannot be the verifier on its own; it needs a deterministic substrate around it.** — He says the model should be treated like a portfolio manager who uses trusted tools, working inside grounding and risk thresholds. Humans should not copy numbers from PDFs into models either. ([8:44](https://youtu.be/Tt2kX2sgQio?t=524))
- **Atomic provenance: the model writes a reference to a number, never the number.** — A separate system (a database-style ledger) writes the figure. A deterministic check strips any number it cannot verify independently, and the cycle repeats at least a couple of times. He explicitly rejects cross-checking between different LLM vendors. ([10:07](https://youtu.be/Tt2kX2sgQio?t=607))
- **Scope determinism: the model decides what to compute, and code does the computing.** — Nearly all of the pipeline is non-deterministic in his view, so the platform splits it and gives the model tools for the deterministic parts. A model should not spend a multi-billion-parameter pass on 1+1 when a CPU can do it. ([11:26](https://youtu.be/Tt2kX2sgQio?t=686))
- **Derivation chains make derived metrics replayable.** — Ratios like gross margin or EBITDA adjustments are not in filings and are defined differently by each firm. The system records what went into each number and what each number fed into, so an analyst-style trail can be replayed and rewound. ([13:59](https://youtu.be/Tt2kX2sgQio?t=839))
- **The system needs an explicit allow-list of what it may produce and what it may never produce.** — Extraction from structured filings is allowed for code paths, while the model is kept out of raw extraction. He says this makes consolidating statements in seconds with every figure tied to a source possible. ([13:59](https://youtu.be/Tt2kX2sgQio?t=839))
- **Customers want an AI analyst that returns analysts' time, not an AI portfolio manager.** — The most-wanted use is automating repeatable work such as listening to earnings calls or building a first-pass model from many 8-Ks and 10-Ks. ([21:38](https://youtu.be/Tt2kX2sgQio?t=1298))

## Techniques
- **Atomic provenance ledger** — The LLM emits only a pointer to the source of each number. A deterministic extractor reads the value into a persistent store, then a check confirms the value independently. Anything that fails is dropped. Repeat the cycle a couple of times. Do not use multiple LLMs to vote on the value. *When:* Any numeric or factual output where one wrong value is costly, such as financial statements, legal citations or dosages.
- **Model decides, code computes** — Split each step into what the model may decide (which fields to fetch, which formula applies) and what code must do (fetch, parse, calculate). Keep an explicit allow-list of what the model may output and what it must never output. *When:* Agent pipelines that produce quantitative results, where math or extraction errors would otherwise come from the model.
- **Derivation chains for derived metrics** — For each computed metric, persist its inputs, the formula or transformation applied, and the outputs that depend on it. The chain can then be replayed or traced back to source documents. Encode firm-specific definitions (recurring vs non-recurring, enterprise-value method) as code, not prompt text. *When:* Derived figures that have no single source record and where different teams define them differently.
- **Deterministic sanity gate on model output** — Before a number reaches a user, check that it is traceable to a stored source record. Strip any value that is not traceable. This is a deterministic gate, not an LLM judge. *When:* Final output stage of any agent that writes figures into reports or models.

## Numbers
- A fine-tuned extraction model reached 94% accuracy, which the speaker says beat foundation models on extraction. He argues a 6% error rate is still unacceptable for verified work product. ([10:07](https://youtu.be/Tt2kX2sgQio?t=607))
- Kepler is the only company Anthropic has written a case study about in financial services, according to the speaker. ([1:03](https://youtu.be/Tt2kX2sgQio?t=63))
- Analysts in the case study are described as earning roughly $600K-$700K a year, which he uses to frame the value of analyst time. ([21:38](https://youtu.be/Tt2kX2sgQio?t=1298))
- The speaker says there is a club of people who have consumed over a billion tokens. He presents this as a bad incentive. ([16:38](https://youtu.be/Tt2kX2sgQio?t=998))
- The speaker says citations get a system about 50% of the way to verifiability. He does not give a measured figure. ([18:01](https://youtu.be/Tt2kX2sgQio?t=1081))

## Hot takes
- Evals cannot make a non-deterministic LLM deterministic, so eval-based trust is not verification.
- AI has turned a writing problem into a reading problem, so the scarce skill is verifying output.
- Intelligence is commoditized; a model should not do arithmetic that a CPU can do.
- Token maxing is the wrong goal and is being rewarded for the wrong reasons.
- Bloomberg and FactSet exist to shift culpability onto a vendor, and that is a barrier to AI adoption in finance.

## Tools mentioned
Claude, XBRL, ChatGPT, GLM 5.2, Opus 4.8

## Relevance to our work
- **agentos** (2/3): The model-decides, code-computes split and the provenance check on outputs map to MemoryMesh's provenance and conflict-resolution work, and to the audit log in Govrix Scout. → *Prototype a MemoryMesh provenance check: store a source pointer with each stored fact, and at read time drop any generated claim whose pointer does not resolve to a stored record. Measure how many claims are dropped on a fixed set of documents.*
- **prosharness** (2/3): Derivation chains and the deterministic gate fit ProsHarness's checkpoint/resume and plan-critique loop. Each checkpoint could record the inputs and transformations that produced it, so a resumed run can be replayed and audited. → *Add a derivation record to each ProsHarness checkpoint (inputs, tool calls, outputs, hash) and a replay check on resume that fails if a recorded output no longer matches.*
