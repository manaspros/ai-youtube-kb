# The Best Local AI Hardware (APPLE M5 MAX vs NVIDIA DGX SPARK)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `4kuS_1y-nqc` · [watch](https://youtu.be/4kuS_1y-nqc) · **date:** 2026-08-02 · **length:** 8:10 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Kai Explains host (name not spoken in transcript) · **orgs:** NVIDIA, Apple
- **topics:** local-ai, inference-serving · **tags:** unified-memory, memory-bandwidth, vram, local-llm-hardware, decode-throughput, dgx-spark, mac-studio, rtx-5090, cuda, buying-guide

> Compares Apple Mac Studio, NVIDIA RTX 5090 and DGX Spark for local LLMs through memory capacity, bandwidth and compute. Main takeaway: decode speed follows memory bandwidth, so size the model first, then pick hardware.

## Summary
The host argues that single-stream local LLM speed is set mostly by memory bandwidth, because each generated token reads the whole model, while memory capacity decides whether the model runs at all. He compares an RTX 5090 (about 32GB at roughly 1.8 TB/s), a high-memory Mac Studio with M3 Ultra (up to 512GB unified at about 800 GB/s) and the DGX Spark (128GB unified at about 270 GB/s). The Spark loses to the Mac on chat speed but keeps the full CUDA stack, which matters for training, fine-tuning and parallel requests. His buying rule is to size the model in GB first: models that fit in 24-32GB suit a 5090 or 4090, larger models suit a high-memory Mac Studio, and some users should run a small model locally and keep a cloud key for the rest. The video is a mental model and spec-sheet comparison with no measured benchmarks, and the Spark bandwidth figure is attributed to unnamed reviews. Not a sponsored segment.

## Key ideas
- **Each generated token reads the entire model from memory, so the model's size and memory traffic dominate local inference.** — Uses a librarian analogy: every word requires consulting the whole library. Speaker says this is mechanically what generating a token is. ([0:00](https://youtu.be/4kuS_1y-nqc?t=0))
- **Rule zero: the model has to fit in fast memory. Spilling to system RAM is far slower.** — Speaker estimates spilling out of VRAM or unified memory into system RAM is about 10x slower, and says nothing else matters if the model does not fit. ([1:25](https://youtu.be/4kuS_1y-nqc?t=85))
- **Memory bandwidth sets interactive chat speed, not compute.** — For one response at a time, compute is usually not the bottleneck. He calls bandwidth the hidden boss and says words per second lives there. ([1:25](https://youtu.be/4kuS_1y-nqc?t=85))
- **No consumer box maxes out capacity, bandwidth and compute together.** — RTX 5090 gives about 32GB at roughly 1.8 TB/s, so 70B-class models do not fit. Mac Studio M3 Ultra goes to 512GB unified at about 800 GB/s, so it loads far bigger models but runs them slower. ([2:45](https://youtu.be/4kuS_1y-nqc?t=165))
- **NVIDIA DGX Spark has a large memory pool but slower decode than the Mac Studio.** — 128GB unified memory, with bandwidth around 270 GB/s, about a third of the Mac's. Speaker frames this as the Spark losing the one job it was built for. ([4:08](https://youtu.be/4kuS_1y-nqc?t=248))
- **The Spark still wins where compute and the software stack matter.** — It has real compute and the full CUDA stack. Training, fine-tuning, or serving many requests at once favour it over raw chat speed. ([4:08](https://youtu.be/4kuS_1y-nqc?t=248))
- **Unified memory is a capacity win, not a speed win.** — Even about 800 GB/s starts to crawl on very large models. Words appear at reading pace, not thinking pace. ([5:35](https://youtu.be/4kuS_1y-nqc?t=335))
- **Buying rule: size the model in GB first, then pick the tier.** — Models that fit in 24-32GB suit an RTX 5090 or last-gen 4090, which is the fastest answer for the money with the best software support. Bigger models point to a high-memory Mac Studio. ([5:35](https://youtu.be/4kuS_1y-nqc?t=335))
- **Hybrid setup: run a small fast model locally and keep a cloud key for models too big for the desk.** — Framed as renting the cathedral and owning the reading room. Speaker suggests this for private everyday work with rare heavy requests. ([7:00](https://youtu.be/4kuS_1y-nqc?t=420))

## Techniques
- **Fit-first sizing before hardware choice** — Estimate the model's memory footprint in GB and compare it with VRAM (NVIDIA card) or unified memory (Mac). If it does not fit, expect a large slowdown from spilling to system RAM. The video gives no footprint formula. *When:* Before buying hardware or choosing which open-weight model to run locally.
- **Bandwidth-bound decode estimate (derived)** — Not stated by the speaker. Derived from his premise that each token reads the whole model: the throughput ceiling scales with memory bandwidth divided by the model's in-memory size. Use it to compare hardware on the same model, then measure. *When:* Comparing candidate machines for one model when no benchmark exists yet.
- **Local hardware decision tree** — (1) Model fits in 24-32GB: buy an RTX 5090, or a 4090 to spend less. (2) Need models above 32GB: buy a Mac Studio with large unified memory and accept slower generation. (3) Need the CUDA stack for training, fine-tuning or many concurrent requests in a small box: DGX Spark, accepting slow chat. (4) Otherwise: hybrid setup. *When:* Planning a local LLM machine purchase or deciding between owned and rented inference.
- **Hybrid local and cloud split** — Run a small, fast model on owned hardware for private everyday work. Keep one cloud API key for the occasional request that needs a model too big for local memory. *When:* Privacy-sensitive daily work with occasional heavy tasks, or a limited hardware budget.

## Numbers
- DGX Spark costs around $4,000 (the opening 'four grand' figure). ([0:00](https://youtu.be/4kuS_1y-nqc?t=0))
- Spilling a model from fast memory to system RAM is about 10x slower (speaker's 'easy' estimate). ([1:25](https://youtu.be/4kuS_1y-nqc?t=85))
- RTX 5090: about 32GB of memory at roughly 1.8 TB/s bandwidth. ([2:45](https://youtu.be/4kuS_1y-nqc?t=165))
- Mac Studio M3 Ultra: up to 512GB unified memory at about 800 GB/s bandwidth. ([2:45](https://youtu.be/4kuS_1y-nqc?t=165))
- DGX Spark: 128GB unified memory at about 270 GB/s bandwidth, roughly a third of the Mac's. ([4:08](https://youtu.be/4kuS_1y-nqc?t=248))
- Models that fit in 32GB on a 5090-class card reach 'a straight 50-90' (unit not spelled out; context suggests tokens per second). Speaker does not name a source. ([4:08](https://youtu.be/4kuS_1y-nqc?t=248))
- Mac Studio-class machines are priced around $5,000 (speaker's figure). ([5:35](https://youtu.be/4kuS_1y-nqc?t=335))

## Hot takes
- Read the memory bandwidth number on the spec sheet; it is the whole game for local chat speed.
- NVIDIA's big-memory DGX Spark generates tokens slower than the Mac Studio it was built to beat.
- Apple's unified memory is a capacity win, not a speed win, and should not be sold as both.
- Run a small model locally and rent the big one from the cloud rather than buying a box for the largest models.
- The DGX Spark is the narrow pick, only for developers who need the real CUDA stack in a small package.

## Tools mentioned
NVIDIA GeForce RTX 5090, NVIDIA GeForce RTX 4090, NVIDIA DGX Spark, Apple Mac Studio, Apple M3 Ultra, CUDA

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on one RTX 5090. The video's 32GB ceiling and bandwidth-bound decode apply directly to which models that card can host and what throughput to expect. → *Before benchmarking InferCraft on the 5090, record model footprint in GB and measured tokens/s, then compare against bandwidth divided by model size to check the baseline.*
