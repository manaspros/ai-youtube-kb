# Google Shrunk 31GB of AI Memory Down to 4GB (TurboQuant)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `dfMeOTLSar8` · [watch](https://youtu.be/dfMeOTLSar8) · **date:** 2026-08-02 · **length:** 8:11 · **format:** news · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kai Explains host (not named in transcript) · **orgs:** Google, Meta, Qdrant, Micron, Western Digital, LangChain, LlamaIndex
- **topics:** rag-retrieval, inference-serving, token-cost-efficiency, local-ai · **tags:** vector-quantization, turboquant, turbovec, vector-index, embeddings, kv-cache, lloyd-max, qjl, simd, filtered-search, jevons-paradox

> Explains TurboQuant, Google's training-free vector compression (31GB to about 4GB for 10M vectors), the independent TurboVec build, and KV-cache gains. Google published math only, not a supported product.

## Summary
The video explains TurboQuant, a Google research method that compresses vector indexes (not models) by randomly rotating every vector with one shared matrix, then rounding each coordinate with boundaries precomputed from theory. Because it never looks at the data, it needs no codebook training and works on drifting data, and a 1,500-dimension float32 vector drops from about 6KB to 384 bytes at 4 bits. A 1-bit QJL residual step corrects error, and the speaker claims the result is within about 2.7x of the Shannon limit. Google only published the paper; independent developer Ryan Kodry built TurboVec, a Rust library with Python bindings that supports online inserts and filtered search, and his viral benchmark shows a 10M-vector index going from 31GB to about 4GB. The same rotation applied to the KV cache is described as roughly 6x smaller at 3 bits, with 4-bit attention up to 8x faster on a data-center GPU. The speaker says the rotation trick now ships in Qdrant, cautions that production tooling is still community-driven, and advises trying it only at millions of vectors or with long-context serving.

## Key ideas
- **The headline compresses the vector index, not the model, and vector indexes are a large cost in RAG and semantic search.** — Raw float32 storage for 10M embeddings of 1,500+ dimensions is about 31GB, held in memory for every query. ([0:00](https://youtu.be/dfMeOTLSar8?t=0))
- **TurboQuant is data-oblivious: it needs no training pass or codebook.** — Classic product quantization runs k-means on your vectors first and must be rerun when data drifts. TurboQuant uses the same quantizer for any dataset. ([1:20](https://youtu.be/dfMeOTLSar8?t=80))
- **A single shared random rotation makes every coordinate follow a known bell curve, so quantizer boundaries can be computed in advance.** — Vectors are stripped of length, multiplied by one random rotation matrix, then each coordinate is rounded with Lloyd-Max boundaries computed once from theory, then bit-packed. ([2:35](https://youtu.be/dfMeOTLSar8?t=155))
- **Two stages: rotate-and-round uses most bits, and a 1-bit QJL residual pass corrects leftover error almost for free.** — The speaker says the combined distortion lands within about 2.7x of the Shannon limit for a given size. ([3:58](https://youtu.be/dfMeOTLSar8?t=238))
- **Google published only the paper. An independent developer, Ryan Kodry, built TurboVec, a Rust library with Python bindings.** — TurboVec supports online inserts without retraining or rebuilding as the collection grows, and it plugs into LangChain and LlamaIndex. ([3:58](https://youtu.be/dfMeOTLSar8?t=238))
- **The speed and filtering claims depend on hand-written SIMD kernels and one developer's benchmark.** — Separate ARM and Intel SIMD builds are described, with the ARM build claimed to beat Meta's FAISS FastScan by 10-19%. Filtering runs inside the kernel using an allowed-ID list, so filtered search stays exact. ([3:58](https://youtu.be/dfMeOTLSar8?t=238))
- **The same rotation trick shrinks the KV cache for long-context serving.** — The speaker describes roughly 6x compression at 3 bits with little quality loss, about 6x more long chats per GPU, and about half the attention cost on long context. ([5:19](https://youtu.be/dfMeOTLSar8?t=319))
- **Caveat: this is a paper and an algorithm, not a supported product. The rotation trick now ships as a checkbox in Qdrant.** — Hardening production tooling is left to the community. The speaker's rule of thumb: little benefit below a few hundred thousand vectors, and worth trying at millions of vectors or with hourly-billed long-context serving. ([6:43](https://youtu.be/dfMeOTLSar8?t=403))

## Techniques
- **Data-oblivious rotate-and-round quantization** — Strip each vector's norm, multiply every vector by the same random rotation matrix, then round each coordinate into 2^b buckets (2 bits = 4 buckets, 4 bits = 16) using Lloyd-Max boundaries precomputed from the known post-rotation distribution. Bit-pack the results. No training pass is needed. Reported result: 1,500-dim float32 vector goes from about 6KB to 384 bytes (16:1). No commands or config shown. *When:* Vector index memory is a bottleneck (millions of embeddings), the corpus drifts or grows continuously, and you cannot afford k-means codebook training or index rebuilds.
- **1-bit residual sign correction (QJL)** — After the main rotate-and-round quantization, spend one leftover bit per coordinate on a sign-based sketch of the residual error to correct the estimate with little extra cost. *When:* You want the extra accuracy from a single bit when the main quantizer leaves residual error and the bit budget is tight.
- **Filtered search inside the distance kernel** — Pass the query along with the list of allowed IDs (for example, from a permission check) into the search kernel, so only candidate vectors are scored. The speaker says this keeps hybrid search exact and makes selective filters faster, not slower. *When:* Retrieval must respect per-user or per-tenant permissions, or runs as hybrid search with selective metadata filters.
- **Same rotation applied to the KV cache** — Apply the rotate-and-quantize method to attention keys (and values) at 3 or 4 bits to shrink the KV cache for long conversations. The speaker reports about 6x memory reduction and up to 8x faster 4-bit attention versus uncompressed keys on a data-center GPU. *When:* Serving long-context chats (around 100k tokens) on rented or fixed GPUs, where KV-cache memory limits concurrency and cost.
- **Adoption rule of thumb** — Stay on the existing index below a few hundred thousand vectors. Test the compressed index at millions of vectors or when long-context serving costs are high. The speaker says it costs nothing to try. *When:* Deciding whether to spend engineering time on vector compression for a retrieval stack.

## Numbers
- 10M embeddings of 1,500+ dimensions as float32 take about 31GB in memory ([0:00](https://youtu.be/dfMeOTLSar8?t=0))
- A single 1,500-dim float32 vector is about 6KB ([1:20](https://youtu.be/dfMeOTLSar8?t=80))
- Compressed vector goes from about 6KB to 384 bytes, a 16:1 reduction at 4 bits ([2:35](https://youtu.be/dfMeOTLSar8?t=155))
- Distortion within about 2.7x of the Shannon limit ([3:58](https://youtu.be/dfMeOTLSar8?t=238))
- TurboVec index of 10M vectors goes from 31GB to about 4GB (developer benchmark) ([3:58](https://youtu.be/dfMeOTLSar8?t=238))
- On ARM, TurboVec beats FAISS FastScan by 10-19% (developer benchmark, ARM only) ([3:58](https://youtu.be/dfMeOTLSar8?t=238))
- KV cache compressed about 6x, down to 3 bits, with almost no quality loss ([5:19](https://youtu.be/dfMeOTLSar8?t=319))
- 4-bit attention is up to 8x faster than uncompressed keys on a top data-center GPU, roughly halving long-context cost ([5:19](https://youtu.be/dfMeOTLSar8?t=319))
- About 6x more long (100k-token) chats fit on the same GPU ([5:19](https://youtu.be/dfMeOTLSar8?t=319))
- Micron and Western Digital each slid a few percent in one trading session ([5:19](https://youtu.be/dfMeOTLSar8?t=319))

## Hot takes
- Headlines credit Google with the tool, but Google only published the math. An independent developer built the usable library.
- The 31GB-to-4GB number comes from one developer's benchmark on a single 10M-vector setup. It is not an independent or general result.
- The 'byte for byte identical whether it runs on your vectors or mine' data-oblivious framing is strong. The speaker's claim that the memory-stock selloff is backwards, citing Jevons paradox, is opinion.
- The speaker calls the paper's math 'cheating' and says it is nearly the physical compression limit, which is a strong claim the video does not back with independent measurements.

## Tools mentioned
TurboQuant (Google research, published as a paper; no official product), TurboVec (Rust library with Python bindings, by Ryan Kodry; version not stated), FAISS FastScan (Meta; named in the transcript as 'face fast scan'), Qdrant (vector database; now ships the rotation trick, per the speaker), LangChain, LlamaIndex, Lloyd-Max quantizer, QJL (1-bit residual method), Product quantization (background concept, not used)

## Relevance to our work
- **agentos** (2/3): MemoryMesh uses BM25 plus pgvector hybrid retrieval, and InferCraft has pluggable KV-cache strategies. A data-oblivious rotate-and-quantize index and a 3-4 bit KV-cache option are both direct candidates for those components. → *Benchmark a TurboVec-style (or Qdrant TurboQuant) compressed index against the current pgvector setup at 1M+ vectors, measuring recall, latency and memory. Evaluate 3-4 bit rotation-based KV-cache compression as a new InferCraft strategy alongside H2O and LMCache.*
