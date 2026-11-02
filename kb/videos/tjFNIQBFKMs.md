# China Is Coming for Your Local AI Box (XIAOMI AI Cube)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `tjFNIQBFKMs` · [watch](https://youtu.be/tjFNIQBFKMs) · **date:** 2026-09-02 · **length:** 14:06 · **format:** news · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Ankit · **orgs:** Xiaomi, Alibaba, Apple, NVIDIA, AMD, TSMC, BYD, DeepSeek
- **topics:** local-ai, inference-serving, models-research · **tags:** local-ai, unified-memory, memory-bandwidth, decode-vs-prefill, tokens-per-second, dgx-spark, strix-halo, mac-studio, rtx-5090, xiaomi-ai-cube, mixture-of-experts, quantization, hardware-buying, memory-prices, serving-software

> Kai Explains on why local AI boxes are judged by memory bandwidth, not headline TFLOPS or tok/s, and how to read this week's Xiaomi, Alibaba and Apple announcements. Verdict: buy only for a specific model you need now.

## Summary
The speaker admits his own failed home-AI build: a fast-looking CPU that ran a large model at only 3-4 tokens per second. He explains that a local AI box is one shared memory pool, and that generation speed is set mostly by memory bandwidth (the "door"), while compute mainly affects prompt reading. Using DGX Spark, RTX 5090, Strix Halo and Mac figures, he shows how a headline petaflop or a single tok/s number hides the metric that matters. He then breaks down Xiaomi's AI Cube claims (demo versus slide versus unverified) and Alibaba's 27B-at-30-tok/s CPU result, whose setup details were left out of the headline. The video closes with a buying checklist, a note that memory prices are inflating sealed-box value, and a clear rule: buy for a model you need today, wait for a serving backend to merge support for new chips.

## Key ideas
- **A local AI box is one shared memory pool. Model capacity decides which models fit, but generation speed is set by memory bandwidth, because every generated word reads the active weights from memory.** — The speaker uses a warehouse-and-door analogy. Bandwidth sets how fast tokens are written. The processor mainly controls how fast the prompt is read. ([1:16](https://youtu.be/tjFNIQBFKMs?t=76))
- **Headline compute (petaflops) is misleading for local inference. Bandwidth is the figure that predicts generation speed.** — DGX Spark advertises 1 petaflop but reviewers measured under 3 tok/s on a 70B model. Spark bandwidth is 273 GB/s versus 1792 GB/s on an RTX 5090. He says generation speed tracks bandwidth almost one to one. ([2:33](https://youtu.be/tjFNIQBFKMs?t=153))
- **Benchmark prefill (prompt reading) and decode (generation) separately, because the two halves favour different hardware.** — On a 30B coding model, prompt reading was 564 tok/s on a Mac Mini, 342 on Strix Halo and 2107 on Spark. Generation was 56 and 73 for two machines. Spark dominates prefill but barely leads on generation. ([3:53](https://youtu.be/tjFNIQBFKMs?t=233))
- **Separate what was demoed, what was claimed on a slide, and what is independently verified. Xiaomi's AI Cube numbers are mostly claims.** — On stage, the Cube ran a 120B model alongside a 3B one. Claimed: 1.22 TB/s bandwidth and 330 tok/s, with the bandwidth figure tied to the O100 chip. No outside reviewer has tested it, and there is no price or date. The chips are not expected commercially until 2027. The fast demo ran the small model. ([5:12](https://youtu.be/tjFNIQBFKMs?t=312))
- **Single-number claims can be technically true and still mislead. Alibaba's '27B at 30 tok/s with no GPU' needed 64 cores, 4-bit weights, one request at a time, and an unstated memory amount.** — The speaker lists the omitted conditions and says the chip cannot be bought anyway. ([6:35](https://youtu.be/tjFNIQBFKMs?t=395))
- **Serving software can change throughput a lot on identical hardware. One YouTuber reportedly got 10x throughput on the same box and model by fixing the serving stack.** — This supports the checklist point that a chip without mature runtime support is of little use. ([8:01](https://youtu.be/tjFNIQBFKMs?t=481))
- **A 16-node Spark cluster (about 2 TB, about $75k) still generates only about 20 tok/s. The owner moved generation to Mac Studios and kept the Sparks for prompt reading.** — This is a practical split-role setup: a prefill-heavy node and a bandwidth-heavy node, reported as an anecdote rather than a formal benchmark. ([9:16](https://youtu.be/tjFNIQBFKMs?t=556))
- **Sealed boxes look cheap now because of a memory shortage. Retail DDR5 kits have risen sharply in price, so the bundled memory is a hedge that the shortage will eventually reach the box price too.** — A 128GB DDR5 kit that once bottomed near $300 is listed above $3000. The speaker says Nvidia has already raised Spark prices and cited memory supply. ([10:28](https://youtu.be/tjFNIQBFKMs?t=628))
- **Buying rule: buy for one large open-weight model needed today that fits nowhere else. Don't buy for a large dense model, and don't buy if the model fits in 32GB, since a gaming GPU is about 6x faster for less money.** — A $2000 128GB box is said to run a 120B model at 30+ tok/s. A large dense model runs at about 3 tok/s on these boxes. The signal to watch is a serving backend merging support for the chip. ([11:34](https://youtu.be/tjFNIQBFKMs?t=694))

## Techniques
- **Bandwidth-first sizing for local decode** — Estimate generation speed from memory bandwidth divided by the bytes of active weights read per token, not from TFLOPS. Check the measured bandwidth rather than the theoretical sum. Use mixture-of-experts models, where only a few experts are active per token, to lower the bytes read per token. Use quantization to shrink weights. *When:* When choosing hardware or a model size for local inference, or when a vendor number does not match measured speed.
- **Split prefill and decode benchmarks** — Time prompt processing (tok/s on the prompt) and answer generation (tok/s on output) as separate metrics for the same model on each machine. Judge hardware by the metric your workload stresses. *When:* When comparing boxes for coding agents, which send long prompts and read long outputs, or when setting up mixed-hardware pipelines.
- **Buying checklist for local AI hardware** — Before buying, confirm: total memory; measured bandwidth; which models fit and at what quantization; prefill speed; decode speed; which runtimes support the chip; actual stock price; whether memory can be upgraded later; and the maturity of the serving software. *When:* When evaluating an announced or sealed AI box, or any new accelerator.
- **Read claims by their conditions** — For each vendor number, list the hidden conditions: batch size, quantization, core count, model size, memory used, and whether the figure is measured or a slide claim. Treat unverified claims as unverified until an outside reviewer or a serving backend has run them. *When:* When reading keynote coverage or launch-day benchmarks.
- **Split generation and prefill across heterogeneous nodes** — Run prompt reading on a high-compute node (e.g. DGX Spark) and token generation on a high-bandwidth node (e.g. Mac Studio). This is the speaker's anecdotal setup, described without configuration detail. *When:* When one machine is strong at prefill but weak at decode, and the workload has long prompts with short-to-medium answers.

## Numbers
- DGX Spark advertises 1 petaflop; a 70B model measured under 3 tok/s on it. ([2:33](https://youtu.be/tjFNIQBFKMs?t=153))
- Memory bandwidth: DGX Spark 273 GB/s vs RTX 5090 1792 GB/s. ([2:33](https://youtu.be/tjFNIQBFKMs?t=153))
- Prefill on a 30B coding model: Mac Mini 564 tok/s, Strix Halo 342 tok/s, DGX Spark 2107 tok/s. ([3:53](https://youtu.be/tjFNIQBFKMs?t=233))
- Generation on the same model: 56 tok/s and 73 tok/s for two machines (the third value is cut off in the transcript). ([3:53](https://youtu.be/tjFNIQBFKMs?t=233))
- Xiaomi AI Cube claims: 1.22 TB/s bandwidth and 330 tok/s (an analyst's slide reading gives 295 tok/s). The fast demo ran a small model, and the bandwidth figure is estimated at about 3-4 GB of memory. ([5:12](https://youtu.be/tjFNIQBFKMs?t=312))
- Alibaba: 27B model at 30 tok/s on CPU, using 64 cores, 4-bit weights and one request at a time. ([6:35](https://youtu.be/tjFNIQBFKMs?t=395))
- A 128GB Strix Halo machine costs roughly half of a DGX Spark. Apple's new Mac Studio supports up to 512GB at over 1 TB/s. ([8:01](https://youtu.be/tjFNIQBFKMs?t=481))
- 16-node Spark cluster: about 2 TB of memory, about $75,000, about 20 tok/s generation. ([9:16](https://youtu.be/tjFNIQBFKMs?t=556))
- A 2.4T-parameter model ran on one Spark at 11 seconds per token by keeping most weights on disk. ([9:16](https://youtu.be/tjFNIQBFKMs?t=556))
- A 128GB DDR5 kit that bottomed near $300 is now listed above $3000. Three companies control about 90% of memory supply. TSMC has over 70% of contract chip-making revenue. ([10:28](https://youtu.be/tjFNIQBFKMs?t=628))
- A $2000 box with 128GB runs a 120B model at 30+ tok/s. A gaming GPU is about 6x faster for models that fit in 32GB. ([11:34](https://youtu.be/tjFNIQBFKMs?t=694))
- One YouTuber got 10x throughput on the same box and model by fixing the serving software. ([8:01](https://youtu.be/tjFNIQBFKMs?t=481))

## Hot takes
- Compute (petaflops) is a poor predictor of local decode speed. Memory bandwidth and the active weights per token are what matter.
- Vendor and keynote numbers for Xiaomi's AI Cube are unverified. The fast demo used the small model, and the headline figures are slide claims.
- Alibaba's '27B at 30 tok/s with no GPU' headline omits 64 cores, 4-bit quantization, batch size 1 and the memory amount, so it is not a practical consumer result.
- Sealed AI boxes look like value now only because of a DRAM price spike. The same shortage can hit their prices too.
- For large dense models, these boxes are not usable for real work (about 3 tok/s). A gaming GPU is the better buy for models under 32GB.
- The real signal for a new accelerator is a serving backend merging support for it, not a keynote.

## Tools mentioned
DGX Spark (NVIDIA), RTX 5090, AMD Strix Halo, Mac Mini, Apple Mac Studio, Xiaomi AI Cube, Xiaomi O100 accelerator, Xiaomi D100 chip, CUDA, DeepSeek coding harness, Qwen, Kimi, GLM, TSMC, DDR5

## Relevance to our work
- **agentos** (2/3): AgentOS InferCraft runs vLLM on one RTX 5090 with KV-cache and quantization strategies. The bandwidth-bound decode model and the prefill/decode split are directly relevant to its capacity planning and benchmarks, but the video does not discuss vLLM or KV-cache offload. → *Add a bandwidth-based decode estimate (tok/s is roughly memory bandwidth divided by active weight bytes per token) to InferCraft's capacity notes, and benchmark prefill and decode tok/s separately for the 5090 setup, checking the numbers against the estimate.*
