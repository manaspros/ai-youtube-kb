# Running a 80B AI Model on a 8GB GPU, FAST (oLLM Guide)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `5E3qTmQPmP8` · [watch](https://youtu.be/5E3qTmQPmP8) · **date:** 2026-09-02 · **length:** 9:40 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai (narrator, channel host) · **orgs:** Kai Explains, Hugging Face, Apple, NVIDIA
- **topics:** local-ai, inference-serving · **tags:** oLLM, layer offload, SSD offload, KV cache offload, Qwen3-Next, llama.cpp, long context, mixture of experts, 8GB VRAM, full precision

> Kai walks through oLLM, a Python library that streams Qwen3-Next 80B layers off SSD on an 8GB GPU, and argues it is only worth using for long-context offline passes, not interactive or agent work.

## Summary
The video explains oLLM (transcribed as "OLM"), a Python library on Hugging Face transformers and PyTorch that runs an 80B Qwen3-Next model on an 8GB GPU by loading one layer at a time from SSD and discarding it after use. The attention KV cache is also written to disk at full 16-bit precision, so peak VRAM stays under 7.5GB regardless of model size. The speaker's main point is that throughput is capped by storage bandwidth: a VRAM-to-NVMe bandwidth ratio of about 90 means decode runs around half a token per second, with the GPU mostly idle. The tool's real advantage is context length: on the same 8GB card, llama.cpp tops out around 32k tokens for an 8B 4-bit model while oLLM runs 100k with the cache on disk. The speaker recommends llama.cpp for interactive use and oLLM only for overnight reading of very large documents at full precision. He also flags that the project has had one commit in 2026 and that his SSD-wear question remains unresearched.

## Key ideas
- **Layer streaming makes a model far bigger than VRAM runnable at all** — oLLM loads transformer layers from SSD one at a time, runs each on the GPU, then discards it, so the full model never sits in memory. The speaker contrasts this with llama.cpp, which refuses to load a file that does not fit. ([1:22](https://youtu.be/5E3qTmQPmP8?t=82))
- **Attention cache goes to disk too, which bounds peak VRAM** — The KV cache is written to the drive at 16-bit as attention runs and read back when needed. Chunked large projection matmuls and flash attention keep peak VRAM under 7.5GB whatever the model size. ([1:22](https://youtu.be/5E3qTmQPmP8?t=82))
- **Storage bandwidth sets the token rate** — An RTX 3060 Ti reads VRAM at about 448 GB/s and a fast PCIe 4 NVMe drive at about 5 GB/s, a ratio of roughly 90. Each token has to walk the active layers off disk, and the GPU sits mostly idle during decode waiting for the next layer. ([2:42](https://youtu.be/5E3qTmQPmP8?t=162))
- **Mixture-of-experts sparsity is why the 80B model beats a 20B model on speed** — oLLM streams only the experts a token routes to, so the 80B Qwen3-Next moves fewer weights per token than the 20B GPT model, which keeps all experts on the GPU and runs slower here. ([1:22](https://youtu.be/5E3qTmQPmP8?t=82))
- **Slower SSDs make the tokens-per-second gap worse** — The speaker says a PCIe 3 drive at 3 GB/s instead of 5 GB/s cuts tokens per second by about 40%, and a SATA SSD is another 3 to 4 times slower. The README numbers assume a fast NVMe drive. ([4:06](https://youtu.be/5E3qTmQPmP8?t=246))
- **The real win is long context on small VRAM** — On 8GB with an 8B 4-bit model, llama.cpp is capped around 32k tokens and probably crashes at 64k. oLLM runs the same model at 100k tokens with the cache on disk, using 6.6GB VRAM and 69GB disk. ([5:26](https://youtu.be/5E3qTmQPmP8?t=326))
- **oLLM keeps 16-bit weights, so the benchmarked model is the one you run** — Most local models are quantized, which trades accuracy for size. oLLM runs full 16-bit weights and a full-precision cache on purpose, which the speaker calls the one place it makes no trade-off. ([6:43](https://youtu.be/5E3qTmQPmP8?t=403))
- **Maintenance and wear risks are real costs** — oLLM had one commit in 2026, and the last behavior-changing commit was on 29 Nov 2025, while llama.cpp shipped several tagged builds in 48 hours. A reply on SSD write endurance was 'need to research', and the speaker cites an August 2025 paper arguing SSD offload of MoE weights is energy-inefficient. ([5:26](https://youtu.be/5E3qTmQPmP8?t=326))

## Techniques
- **Layer-streaming offload from SSD** — Load one transformer layer from disk to GPU, run it, discard it, then load the next. Peak VRAM stays fixed regardless of model size. oLLM does this by default: point it at a Hugging Face model. The video shows no commands or config keys, and the speaker says the knob surface is small. *When:* The model is far larger than VRAM and you can tolerate very low tokens per second, such as overnight offline passes.
- **Disk-backed full-precision KV cache** — Write the attention cache to disk as it grows at 16-bit precision and read it back per step, instead of keeping it in VRAM or quantizing it. *When:* Long context (50k to 100k tokens) on a small GPU where you need the full-precision model output for accuracy.
- **Chunked projections plus flash attention to cap peak VRAM** — Split big MLP projection matrices into passes small enough to fit, and use flash attention so the full attention matrix is never materialized. *When:* Running large models or long sequences on a card with little VRAM, where peak memory matters more than speed.
- **Expert-selective streaming for MoE models** — Fetch only the experts each token routes to, so inactive experts never move from disk. *When:* Serving an MoE model that is too big for VRAM. It gives the speed edge over dense models of smaller size in this setup.
- **Predict throughput from storage bandwidth before running** — Divide the storage read rate by the weight bytes that must be moved per token to estimate tokens per second. The speaker does the ratio check with VRAM bandwidth (448 GB/s) against NVMe (about 5 GB/s), which gives roughly 90. *When:* Deciding whether an offload setup is usable, before spending time on benchmarks.
- **Pick the runtime by job shape (speaker's decision rule)** — Interactive chat: llama.cpp at 4-bit, context capped at 32k on 8GB. Model too big for VRAM: llama.cpp with memory mapping paging from NVMe, accepting 1 to 2 tokens per second. Full precision with 100k context on 8GB for offline reads: oLLM. *When:* Choosing a local inference tool for a specific workload on constrained hardware.

## Numbers
- Model file is 160 GB; the GPU has 8 GB of VRAM; the speaker reports about 0.5 tokens/s on a card that costs about $200 used. ([0:00](https://youtu.be/5E3qTmQPmP8?t=0))
- README table: 80B parameters, 160 GB weights, 50,000-token context, 7.5 GB VRAM, 180 GB disk; project has about 2,700 GitHub stars, MIT licensed. ([0:00](https://youtu.be/5E3qTmQPmP8?t=0))
- 8B model at 4-bit in llama.cpp is 4.9 GB, loads fully into VRAM, runs at 64 tokens/s; Qwen3-Next is about 20 times larger. ([0:00](https://youtu.be/5E3qTmQPmP8?t=0))
- RTX 3060 Ti VRAM bandwidth 448 GB/s vs PCIe 4 NVMe about 5 GB/s, ratio about 90; speaker cites a 129x gap versus llama.cpp. ([2:42](https://youtu.be/5E3qTmQPmP8?t=162))
- M2 Max with 64 GB unified memory on MLX at 4-bit: 42 tokens/s, about 80 times faster than oLLM on the 3060 Ti. ([4:06](https://youtu.be/5E3qTmQPmP8?t=246))
- PCIe 3 drive at 3 GB/s instead of 5 GB/s cuts tokens/s by about another 40%; SATA SSD is 3 to 4 times slower again. ([4:06](https://youtu.be/5E3qTmQPmP8?t=246))
- Qwen3-Next context window is 131,000 tokens; an 8B model at 50k context has a 52 GB full-precision cache. ([4:06](https://youtu.be/5E3qTmQPmP8?t=246))
- On 8GB VRAM, llama.cpp with an 8B 4-bit model tops out around 32k tokens and probably crashes at 64k; oLLM runs the same at 100k with 6.6 GB VRAM and 69 GB disk. ([5:26](https://youtu.be/5E3qTmQPmP8?t=326))
- llama.cpp had five tagged builds in a 48-hour window; oLLM had one commit in all of 2026, and the last behavior change was 29 Nov 2025. ([6:43](https://youtu.be/5E3qTmQPmP8?t=403))
- Unshipped roadmap from launch: 100k context on 12 GB and a better MoE cache algorithm. ([7:59](https://youtu.be/5E3qTmQPmP8?t=479))

## Hot takes
- Half a token per second is far too slow for an agent working unattended on a codebase; it is fine for reading a 50k-token filing and getting an answer by morning.
- For a local chat model, install llama.cpp, quantize to 4-bit and cap context at 32k on 8GB; oLLM is only worth it for full-precision, 100k-context offline work.
- oLLM is currently the only tool that runs 100k context at full precision on 8GB, and that niche is small but real.
- The project's main value is the idea (disk-backed cache, layer streaming) more than its throughput, and the work appears to have stopped.
- The speaker's view is that for two years VRAM was a hard wall, and oLLM turns that wall into a slow door.

## Tools mentioned
oLLM (OLM), Qwen3-Next 80B, llama.cpp, Hugging Face transformers, PyTorch, MLX, flash attention

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) plans pluggable KV-cache strategies including CPU offload and LMCache; this video gives a concrete case where disk-backed cache at 100k context works but decode is bounded by storage bandwidth (about 0.5 tokens/s), which is a useful reference for offload-tier benchmarks. → *Before choosing an InferCraft KV-cache offload tier, benchmark decode tokens/s against the storage tier's read bandwidth (the bandwidth-ratio check from 2:42), and use the 32k llama.cpp ceiling on 8GB as a baseline for context budgets.*
