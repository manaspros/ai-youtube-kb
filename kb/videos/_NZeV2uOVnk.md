# Mac Studio vs DGX Spark: Which Is Better for Local AI?

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `_NZeV2uOVnk` · [watch](https://youtu.be/_NZeV2uOVnk) · **date:** 2026-10-02 · **length:** 16:48 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai Explains host (unnamed in transcript) · **orgs:** Apple, NVIDIA, Lambda, RunPod, Ollama, LMSYS, Computer Base
- **topics:** local-ai, inference-serving, infra-cost-scaling · **tags:** mac-studio, dgx-spark, prefill-vs-decode, memory-bandwidth, unified-memory, concurrency, continuous-batching, disaggregated-inference, kv-cache, local-llm-hardware, buying-guide

> Kai Explains compares a Mac Studio (M3 Ultra, with M5 Ultra prices and specs) and an NVIDIA DGX Spark for local LLM inference, and argues the answer depends on whether the workload is decode-bound, prefill-bound, or CUDA-shaped.

## Summary
The host ran the same large model on a Mac Studio and a DGX Spark and found decode tokens per second roughly tied at 4K to 32K context, while setup took about 4 hours on the Mac and 96 hours on the Spark. He splits local inference into prefill (compute-bound, favors the Spark) and decode (memory-bandwidth-bound, favors the Mac), and explains why bandwidth divided by model size sets the decode ceiling. He covers concurrency for agent workloads, usable memory after macOS reserves its share, and the CUDA ecosystem advantage. He tests splitting prefill and decode across both machines, which gave about 2.8x over either alone but ran the Spark side on CPU on the stock build. Benchmarks are from an M3 Ultra, not the M5 Ultra, and he flags every place the generation gap could change the answer. He closes with a buying rule: under 128 GB of models pick the Mac, CUDA-shaped work (fine-tuning, diffusion, research repos, many agents) picks the Spark, and uncertain buyers should rent for a month first.

## Key ideas
- **Setup time is the most important number: the Mac Studio served inference about 4 hours after unboxing, the DGX Spark took about 96 hours.** — Decode tok/s was roughly tied on the same model at 4K, 8K and 32K context, so the setup gap and ongoing software friction decided the experience. ([0:00](https://youtu.be/_NZeV2uOVnk?t=0))
- **Local inference is two workloads with different bottlenecks: prefill scales with compute, decode scales with memory bandwidth.** — Prefill is parallel matrix work over the whole prompt. Decode reads all weights for every generated token, so it is limited by how fast weights move from memory. ([2:24](https://youtu.be/_NZeV2uOVnk?t=144))
- **Decode speed is roughly memory bandwidth divided by model size, so software tuning does not change the ceiling much.** — Spark at 273 GB/s with a ~40 GB 4-bit 70B model lands around 2.7 to 5 tok/s across several testers. M3 Ultra at 819 GB/s wins decode clearly, and the M5 Ultra is stated at 1.2 TB/s. ([3:39](https://youtu.be/_NZeV2uOVnk?t=219))
- **The Spark wins prefill clearly, and that matters for long prompts over about 32K context.** — On one box with GPT-OSS 120B, prefill was about 45x faster than decode in throughput terms. Head-to-head, Spark prefill was 730 vs 317 tok/s at 4K and 643 vs 476 at 32K, with the gap narrowing as context grows. ([4:45](https://youtu.be/_NZeV2uOVnk?t=285))
- **For agents, the workload is several concurrent streams, not one stream, so continuous batching and KV cache budget per instance decide usable context.** — vLLM and TensorRT-LLM with continuous batching favor the Spark for multi-agent use. Splitting one memory pool across many instances shrinks the KV budget per agent. ([9:47](https://youtu.be/_NZeV2uOVnk?t=587))
- **Advertised figures and memory capacity both need discounting before buying.** — NVIDIA's 1 petaflop is FP4 with sparsity, with about 480 TFLOPS measured. macOS reserves about 12 GB, so a 96 GB Mac Studio has roughly 84 GB usable. The M5 Ultra memory tiers jump from 96 GB to 256 GB with no 128 GB option. ([7:07](https://youtu.be/_NZeV2uOVnk?t=427))
- **Splitting prefill and decode across both machines with layer-wise KV streaming gave about 2.8x over either alone, but the stock build leaves the Spark GPU unused.** — On Llama 3.1 8B with an 8K prompt, Spark alone took 4.34 s, M3 Ultra 6.42 s, and the pair 2.32 s. The Spark side ran on CPU, so the speedup is treated as a demo, not a default. ([13:37](https://youtu.be/_NZeV2uOVnk?t=817))
- **The Spark's ecosystem advantage is real: CUDA, cuDNN, NCCL, TensorRT-LLM, vLLM and SGLang, plus day-one support for new CUDA kernels, while the Mac often never gets them.** — Fine-tuning and diffusion are described as minutes instead of hours, and hours instead of days. The Spark includes 4 TB NVMe, where Apple charges about $1,500 extra for matching storage. ([11:04](https://youtu.be/_NZeV2uOVnk?t=664))
- **Decision rule: pick the Mac for models under 128 GB, the Spark for CUDA-shaped work, the 256 GB Mac for one address space, and rent in the cloud when the workload is unclear.** — Two dates may shift this: Apple's 512 GB tier in late October and LPDDR6 on a future Spark in 2027 to 2028. The host frames the choice as which failure mode to live with, slow prefill or self-inflicted setup debugging. ([13:37](https://youtu.be/_NZeV2uOVnk?t=817))

## Techniques
- **Benchmark prefill and decode separately** — Measure prompt-processing tok/s and generation tok/s as two numbers, at several context lengths (he used 4K, 8K, 32K). Do not report a single tok/s figure. Use llama.cpp for GGUF models; he cited GPT-OSS 120B in llama.cpp with MXFP4 as the example. No exact flags were shown. *When:* Comparing any two local inference machines, or choosing hardware for long-prompt agent work where prefill dominates latency.
- **Estimate decode ceiling from bandwidth** — Decode tok/s is roughly memory bandwidth (GB/s) divided by bytes read per token, approximately the model's weight size. Example: about 40 GB of 4-bit 70B weights on 273 GB/s gives about 2.7 to 5 tok/s in practice. *When:* Before buying hardware or choosing a quantization or model size for interactive decode speed.
- **Size memory as usable, not nominal** — Subtract the OS reservation (he cites about 12 GB on macOS) from unified memory, then budget model weights plus KV cache for each concurrent instance. Check whether the next memory tier is reachable. *When:* Sizing a single box for a model plus several agents with separate contexts.
- **Test concurrency, not just one stream** — Run several simultaneous generation streams on the same server and measure aggregate throughput and per-agent context. He pointed to vLLM and TensorRT-LLM continuous batching as the mechanism. *When:* Serving multiple agents from one local box, where single-stream tok/s is not the workload.
- **Disaggregated prefill and decode across two machines** — Run prompt prefill on the machine with more compute and decode on the machine with more memory bandwidth. Stream the KV cache layer by layer so transfer overlaps compute. He measured about 2.8x over either machine alone on Llama 3.1 8B with 8K prompt, but this needed a build that runs the accelerator side on GPU, not CPU. *When:* Two heterogeneous boxes on a fast link, where the software stack supports KV transfer. Verify the GPU is actually used on both sides before trusting the result.
- **Rent before buying** — Rent a comparable configuration by the month on a GPU cloud (he named Lambda and RunPod) to measure your own workload before buying hardware. *When:* Workload shape is unclear, or the next hardware generation is close enough that a purchase may age badly.

## Numbers
- Same-model decode tok/s on both machines at 4K, 8K, 32K context: 27.1 vs 29.2, 27.3 vs 28.6, 26.9 vs 26.7 (a tie). ([0:00](https://youtu.be/_NZeV2uOVnk?t=0))
- Time to first served inference: Mac Studio about 4 hours, DGX Spark about 96 hours. ([0:00](https://youtu.be/_NZeV2uOVnk?t=0))
- Memory bandwidth: DGX Spark 273 GB/s; M3 Ultra 819 GB/s; M5 Ultra 1.2 TB/s (stated, not measured). ([3:39](https://youtu.be/_NZeV2uOVnk?t=219))
- Llama 3.1 70B at 4-bit (~40 GB weights): roughly 2.7 to 5 tok/s on Spark across cited testers. ([3:39](https://youtu.be/_NZeV2uOVnk?t=219))
- GPT-OSS 120B on Spark (llama.cpp, MXFP4): prefill 1723 tok/s, decode 38.55 tok/s, about 45x throughput gap within one machine. ([4:45](https://youtu.be/_NZeV2uOVnk?t=285))
- Prefill at 4K context: Spark 730 tok/s vs M3 Ultra 317 tok/s. At 32K: 643 vs 476. ([5:54](https://youtu.be/_NZeV2uOVnk?t=354))
- Apple claims M5 Ultra prefill up to 4x faster than M3 (Apple's July testing, unverified externally). M3 Ultra took 227 s for a 15,777-token prompt on 4-bit DeepSeek V3. ([5:54](https://youtu.be/_NZeV2uOVnk?t=354))
- NVIDIA advertises 1 petaflop FP4 with sparsity; measured performance is closer to 480 TFLOPS. ([7:07](https://youtu.be/_NZeV2uOVnk?t=427))
- Prices: M5 Ultra 96 GB base $5,499; 256 GB $9,499; NVIDIA two-Spark bundle $9,449 (128 GB each); Apple 512 GB tier ships late October. ([7:07](https://youtu.be/_NZeV2uOVnk?t=427))
- macOS reserves about 12 GB, so a 96 GB Mac Studio has about 84 GB usable. ([8:28](https://youtu.be/_NZeV2uOVnk?t=508))
- Two-node Spark cuts time per output token on Llama 3.3 70B from 269 ms to 133 ms (NVIDIA's numbers). ([8:28](https://youtu.be/_NZeV2uOVnk?t=508))
- Llama 3.1 8B, 8K prompt: Spark alone 4.34 s, M3 Ultra alone 6.42 s, combined split 2.32 s (about 2.8x). ([13:37](https://youtu.be/_NZeV2uOVnk?t=817))
- DGX Spark storage 4 TB NVMe standard; Apple charges an extra $1,500 for comparable storage. ([11:04](https://youtu.be/_NZeV2uOVnk?t=664))
- Forum report from an NVIDIA developer thread: 3-minute model load, 1 to 3 minute responses, about 15 tok/s, crashes every few hours (single user, anecdotal). ([11:04](https://youtu.be/_NZeV2uOVnk?t=664))
- Another forum user spent over a week and about $18,000 on four GB10 boxes without a working pipeline (anecdotal). ([12:18](https://youtu.be/_NZeV2uOVnk?t=738))

## Hot takes
- A 96 GB Mac Studio is closer to two RTX 5090s of usable memory than three, once macOS overhead is subtracted.
- DGX Spark's advertised petaflop is a sparse FP4 peak. Measured throughput is about half that.
- The 2-Spark clustering speedup is a demo, not a default, because the stock Linux build runs the Spark side on CPU.
- Setup friction (about 96 hours to serve on the Spark) matters more than tokens per second for most buyers.
- Most local AI hardware reviews only show tok/s and miss the prefill vs decode split and concurrency.
- Buy the Mac for under 128 GB of models; buy the Spark only for CUDA-shaped work such as fine-tuning, diffusion and research repos.

## Tools mentioned
Mac Studio (M3 Ultra, 819 GB/s; M5 Ultra for specs and pricing, 1.2 TB/s), NVIDIA DGX Spark (GB10, 128 GB LPDDR5X, 273 GB/s), llama.cpp, MXFP4, Ollama, vLLM, TensorRT-LLM, SGLang, CUDA, cuDNN, NCCL, Triton, Lambda, RunPod, Qwen 3.5 (397B, as transcribed), Llama 3.1 70B 4-bit, Llama 3.1 8B, GPT-OSS 120B, DeepSeek V3 4-bit, macOS, Metal

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on one RTX 5090 and targets KV cache strategies and scheduling. The video's prefill vs decode split, continuous batching under concurrent agents, and KV budget per instance apply directly, though it is a hardware comparison and the numbers are for other machines. → *Extend InferCraft benchmarks to report prompt-processing tok/s and decode tok/s separately at 4K, 8K and 32K context, and add an aggregate-throughput test with N concurrent agent streams that records the usable KV budget per stream.*
