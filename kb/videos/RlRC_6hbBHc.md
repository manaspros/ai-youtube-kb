# Xiaomi & DeepSeek Just Solved the Biggest Bottleneck in Your Local AI

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `RlRC_6hbBHc` · [watch](https://youtu.be/RlRC_6hbBHc) · **date:** 2026-10-02 · **length:** 14:26 · **format:** news · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai (Kai Explains host, not named in transcript) · **orgs:** DeepSeek, Xiaomi, Microsoft Research, Tsinghua University, Apple
- **topics:** inference-serving, token-cost-efficiency, local-ai, models-research · **tags:** KV cache, prefill, cache hit vs miss pricing, cross-layer KV sharing, YOCO, long context, recall, local inference, Apple M3 Ultra, agent cost

> Explainer on DeepSeek V4.1 Flash and Xiaomi HiSparse 2, two independent designs that split a model so the bottom half reads the prompt once; the real gain is cheaper reading (prefill), not memory, and recall is not yet proven.

## Summary
Kai argues that long agent sessions degrade because of the cost and latency of reading new input, not because models hold too few tokens. He compares DeepSeek V4.1 Flash (September 2026) and Xiaomi's HiSparse 2 (published 12 days later), which both use a cross-layer design in the style of YOCO (You Only Cache Once): the bottom half of the model reads the prompt and writes shared KV notes, and the top half borrows them. He says the widely reported "4x vs 4.5x" memory race compares each lab against its own previous model, so the numbers are not comparable. Both papers' headline gain is on reading, with memory savings largely coming from bookkeeping changes such as fewer note-keeping layers. He backs this with API cache-hit vs cache-miss pricing (about 50x apart), a developer's 11.59M-token app build that was 99.5% cache hits, and a local M3 Ultra prefill measurement of about 450 tokens/s. He closes with honest caveats: neither lab has a strong recall benchmark (Xiaomi's is under 60%), and user reports describe forgetting past about 400k tokens.

## Key ideas
- **Agents fail at long context because reading new input is expensive, not because models lack token capacity** — Kai frames the 2am coding-agent breakdown as hitting a reading wall. Both papers reportedly open by saying input-heavy agent workloads and long observations are the cost problem, and memory was never the main issue. ([0:00](https://youtu.be/RlRC_6hbBHc?t=0))
- **DeepSeek and Xiaomi independently converged on the same architecture 12 days apart** — DeepSeek V4.1 Flash (September) and Xiaomi HiSparse 2 both split the model so a bottom half reads the prompt and writes shared notes that the top half reuses. Kai links it to shared lineage: Xiaomi's last author helped build DeepSeek V2. ([1:23](https://youtu.be/RlRC_6hbBHc?t=83))
- **The 4x vs 4.5x memory comparison is not like-for-like** — DeepSeek's 4x compares against its own prior model at a different precision. Xiaomi's 4.5x compares against its own prior design on an 80B research model. Kai's point: the race framing is misleading; the 43 GB to 0.93 GB claim is a headline, not the research goal. ([2:45](https://youtu.be/RlRC_6hbBHc?t=165))
- **Cache hits are cheap, cache misses cost about 50x more, and the reading cliff hits quickly** — On DeepSeek's API a cache hit is about $0.003 per million tokens and a miss about $0.15. A Hacker News user reportedly hit the cliff around 60% of their context window and paid far more than expected. ([5:06](https://youtu.be/RlRC_6hbBHc?t=306))
- **Cutting the read path in half is the real win** — In a YOCO-style split, the bottom half reads the prompt once and the top half borrows its notes, so reading costs roughly half. DeepSeek activates about 16B parameters when writing a token and 8B when reading. Xiaomi's 5x fewer operations on a 1M-token prompt is the headline reading gain. ([6:23](https://youtu.be/RlRC_6hbBHc?t=383))
- **Only a few layers keep growing KV notes** — In V4.1 Flash (40 layers, bottom 20 read and top 20 write), only 4 layers keep notes that grow with the conversation; the rest borrow shared notes, giving about 890 bytes per token. HiSparse 2 has 49 layers and exits at layer 25 for prompts, so the top half need not be loaded for prefill, which helps local deployment. ([7:48](https://youtu.be/RlRC_6hbBHc?t=468))
- **Architectures that converge across rival labs tend to become defaults** — Kai compares this to grouped query attention. A LocalLLaMA user grafted the idea onto a smaller Qwen model within a day. Xiaomi says HiSparse 2 is the core of its next model, MIMO v3, and DeepSeek has shipped it in V4.1 Flash. ([10:12](https://youtu.be/RlRC_6hbBHc?t=612))
- **Measure prefill speed and time to first token, not just context size** — On a 512 GB M3 Ultra, V4.1 Flash reads about 450 tokens/s, flat across context size. Kai says that means about 4 minutes before the first word at 100k tokens, and a long wait at 1M. He argues reading speed is the number to ask for next. ([11:36](https://youtu.be/RlRC_6hbBHc?t=696))
- **Recall at long context is unproven** — DeepSeek's report has no standard recall test and says long-context retrieval is not fully characterized. Xiaomi's recall score improved over its old design but stayed under 60%. User reports describe forgetting past about 400k tokens. ([11:36](https://youtu.be/RlRC_6hbBHc?t=696))

## Techniques
- **Cross-layer KV sharing (YOCO-style split)** — Split the transformer: the bottom half processes the prompt and writes one shared KV set; the top half attends to that shared set instead of recomputing its own. Keep KV growing only in a few layers (DeepSeek: 4 of 40), and let the rest borrow. For local use, load only the bottom layers when the workload is prefill-only (Xiaomi exits at layer 25 of 49). *When:* Read-heavy workloads where prompts are much longer than outputs, such as agents whose tool outputs dominate the context. Also useful when KV memory is the constraint on a single GPU.
- **Split input-token cost into cache-hit and cache-miss** — Track cached-input and uncached-input tokens separately in cost accounting. Cache hits cost about $0.003/M and misses about $0.15/M on DeepSeek's API, so a blended average hides the cliff. Watch for the point where a session crosses from cached reads into fresh reads. *When:* Any agent or gateway that pays per token through an API with prompt caching.
- **Benchmark prefill tok/s and time-to-first-token at 100k and 1M** — Measure how long a 100k or 1M-token prompt takes before the first output token on your hardware, and check that prefill throughput stays flat across context sizes. Kai's example: 450 tok/s on an M3 Ultra. *When:* Choosing local hardware or a serving setup for long-context agents. Use reading speed alongside the advertised context window.
- **Run a recall test before trusting long context** — Kai's implicit advice: don't rely on advertised context length alone. Check retrieval of facts placed deep in a long context, and keep context below the point where you see forgetting (user reports around 400k for this model). This is anecdotal and not validated in the video. *When:* Before relying on a long context window for agents or RAG-free memory.
- **Trim large tool output before it enters context (inferred, not stated in video)** — The speaker's example is a 10-line fix next to 5,000 lines of test output, which is what drives reading cost. Summarizing or truncating large tool results before they go into context would reduce new reading. This is my inference from his framing, not advice he gives. *When:* Coding agents that run test suites or verbose builds.

## Numbers
- DeepSeek claims 1M tokens of memory in 0.93 GB (reported 43 GB down to 0.93 GB) ([1:23](https://youtu.be/RlRC_6hbBHc?t=83))
- Xiaomi HiSparse 2 shrinks memory 4.5x vs its own previous design, measured on an 80B research model ([2:45](https://youtu.be/RlRC_6hbBHc?t=165))
- API cache hit about $0.003 per million tokens vs cache miss about $0.15 per million (about 50x) ([5:06](https://youtu.be/RlRC_6hbBHc?t=306))
- Writing a token activates about 16B parameters; reading a token activates about 8B (half) ([6:23](https://youtu.be/RlRC_6hbBHc?t=383))
- Only 4 of 40 layers keep growing KV notes; about 890 bytes per token of storage ([7:48](https://youtu.be/RlRC_6hbBHc?t=468))
- HiSparse 2: 5x fewer operations to process a 1M-token prompt vs its old design ([7:48](https://youtu.be/RlRC_6hbBHc?t=468))
- Developer app build: 11.59M total input tokens, 99.5% cache hits, new tokens about 0.5% but about one fifth of the input bill ([10:12](https://youtu.be/RlRC_6hbBHc?t=612))
- Local prefill about 450 tokens/s on a 512 GB M3 Ultra, flat across context size ([11:36](https://youtu.be/RlRC_6hbBHc?t=696))
- Time to first token about 4 minutes at 100k tokens and 39 minutes at 1M (speaker's figures; 450 tok/s implies about 37 min at 1M, so the 39 min figure is slightly high) ([11:36](https://youtu.be/RlRC_6hbBHc?t=696))
- Xiaomi recall score improved over old design but remains under 60% on its benchmark ([11:36](https://youtu.be/RlRC_6hbBHc?t=696))
- User reports of V4.1 Flash forgetting content past about 400,000 tokens ([12:56](https://youtu.be/RlRC_6hbBHc?t=776))

## Hot takes
- The 4x vs 4.5x memory race is the wrong comparison; both numbers are against each lab's own prior model, so they cannot be ranked against each other.
- Memory was never the main problem; the headline gain is reading (prefill) cost, and the memory numbers are mostly a side effect of bookkeeping changes.
- Reading speed, not the advertised context window, is the number to ask about for long-context models.
- The open problem is recall: neither lab has a strong long-context retrieval result yet, and Xiaomi's recall is under 60%.
- Kai's agent-session story is anecdotal; his prediction that agents will 'just work' in six months is speculation.

## Tools mentioned
DeepSeek V4.1 Flash, HiSparse 2 (Xiaomi), MIMO v3 (Xiaomi's next model, per Luo Fuli), YOCO (You Only Cache Once, Microsoft Research and Tsinghua, May 2024), Grouped query attention (referenced), Qwen (smaller model grafted by a LocalLLaMA user), Apple M3 Ultra (512 GB, local benchmark), KV cache

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) is a vLLM-based single-RTX-5090 stack with pluggable KV strategies (H2O, CPU offload, LMCache). Cross-layer KV sharing and reading-speed metrics bear directly on that design and its benchmarks. → *Add prefill tok/s and time-to-first-token at 100k and 1M context to InferCraft benchmarks, then read the DeepSeek V4.1 Flash and HiSparse 2 papers to assess cross-layer KV sharing as a candidate KV strategy alongside H2O and CPU offload.*
- **prosharness** (1/3): Long Claude Code runs (checkpoint/resume) are the workload where context growth matters. The forgetting reports past about 400k are anecdotal, but they support tracking context size at checkpoints. → *Log context token count at each ProsHarness checkpoint so long-run degradation can be correlated with context size before any threshold is set.*
