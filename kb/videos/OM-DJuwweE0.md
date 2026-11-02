# How Big Models Fit on Small GPUs (DeepSpeed)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `OM-DJuwweE0` · [watch](https://youtu.be/OM-DJuwweE0) · **date:** 2026-02-02 · **length:** 4:24 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Microsoft, Hugging Face, Google, NVIDIA, Apple, Better Stack
- **topics:** training-finetuning-rl, local-ai · **tags:** deepspeed, zero, zero-infinity, gpu-memory, vram, cpu-offload, nvme-offload, pytorch, hugging-face, accelerate, google-colab, config-json, tutorial

> Better Stack's short tutorial on using Microsoft's DeepSpeed ZeRO stages to fit training workloads into limited GPU memory, run on Colab from a Mac.

## Summary
The presenter explains that large-model training usually fails on GPU memory (optimizer states, gradients, parameters), not on speed, and that DeepSpeed's ZeRO shards these across devices to reduce per-GPU usage. Because the presenter's machine is a Mac M4 Pro with no NVIDIA GPU, the demo runs on Google Colab, installing PyTorch, Hugging Face and DeepSpeed and running DSReport to check the CUDA and compiler setup. The walkthrough starts from a ZeRO stage 2 config.json taken from the official docs, with advice to change one thing at a time and to treat setup failures as usually CUDA mismatches. The run finishes on a small imported dataset, and the presenter notes the loss barely moved. The video then walks through ZeRO stages 1 to 3 and ZeRO-Infinity offload to CPU or NVMe, framing offload as trading speed for the ability to fit the model at all. It closes by mentioning DeepSpeed's pipeline, tensor and mixture-of-experts support and its Hugging Face and Accelerate integration, and says throughput claims should be tested on your own setup.

## Key ideas
- **Big-model training fails on VRAM, not speed** — The presenter says optimizer states, gradients and parameters are what blow up GPU memory, and DeepSpeed's ZeRO works by not storing a full copy of all of that on every GPU. ([0:00](https://youtu.be/OM-DJuwweE0?t=0))
- **Start from a ZeRO stage 2 config and change one thing at a time** — The config.json is described as the core of the setup. Start from the official HF and DeepSpeed docs config, avoid adding random settings, and treat failures at the environment step as usually CUDA version mismatches rather than a model problem. ([0:59](https://youtu.be/OM-DJuwweE0?t=59))
- **ZeRO stages each remove one more kind of per-GPU state** — Stage 1 shards optimizer states, stage 2 also shards gradients, and stage 3 also shards parameters, which the presenter calls the biggest memory win. ZeRO-Infinity can offload to CPU or NVMe when the model still does not fit, at a cost in speed. ([1:58](https://youtu.be/OM-DJuwweE0?t=118))
- **DeepSpeed covers more than memory** — The presenter lists pipeline and tensor parallelism and built-in mixture-of-experts support as additional options once memory is no longer the only limit. ([3:04](https://youtu.be/OM-DJuwweE0?t=184))
- **Integration path is through Hugging Face and Accelerate** — DeepSpeed plugs into Hugging Face and Accelerate so you do not have to build the training loop from scratch, and Accelerate is suggested as the route to multi-GPU later. ([3:04](https://youtu.be/OM-DJuwweE0?t=184))
- **Benchmarks are setup-dependent and were not reproduced here** — The presenter could not show an optimized speedup on the Mac/Colab setup with a basic model, and says the throughput wins seen in other DeepSpeed projects are the reason to try it, not this run. ([3:04](https://youtu.be/OM-DJuwweE0?t=184))

## Techniques
- **Run the DeepSpeed environment check before training** — Install PyTorch, Hugging Face libraries and DeepSpeed, then run DSReport to sanity-check CUDA and the compiler setup. If this step fails, stop and fix the CUDA mismatch before touching the model or config. *When:* First setup on any new machine or Colab runtime, before any training run.
- **Begin with a ZeRO stage 2 config.json copied from the official docs** — Take the config from the Hugging Face or DeepSpeed docs, set ZeRO stage 2 (shards optimizer states and gradients, parameters stay replicated), and reuse the docs' Python script with minimal changes. The transcript does not show the individual config keys. *When:* When you need a first working config that fits more model than a plain PyTorch run, and you want a known-good baseline.
- **Change one config knob per run** — Keep the working baseline and alter a single setting at a time, rather than adding multiple configs at once. Record peak GPU memory after each run. *When:* Tuning DeepSpeed settings after the baseline runs, to see which change moved memory or speed.
- **Escalate ZeRO stage only when memory still fails** — Move from stage 1 (optimizer states) to stage 2 (plus gradients) to stage 3 (plus parameters). If the model still does not fit, enable ZeRO-Infinity offload to CPU or NVMe, and watch CPU RAM while offload is on. *When:* The model OOMs at the current stage, accepting slower steps in exchange for fitting the model.
- **Use a hosted GPU runtime when the local machine has no NVIDIA GPU** — The presenter ran the whole workflow on Google Colab from a Mac, using a small imported dataset so the run finishes in minutes. *When:* Prototyping DeepSpeed on a Mac or other machine without CUDA hardware, where the goal is to get the workflow running rather than to benchmark.
- **Scale to multiple GPUs through Accelerate** — Keep the Hugging Face and DeepSpeed setup and let Accelerate handle multi-GPU launch later, instead of rewriting distributed code. *When:* Moving from a single-GPU run to multi-GPU training.

## Numbers
- No benchmark numbers were quoted. Peak GPU memory was printed on screen after the run but not stated, and the training loss barely changed on the small dataset. ([1:58](https://youtu.be/OM-DJuwweE0?t=118))
- Run length is 4:24 with a small imported dataset, and the presenter notes that a run takes a few minutes. ([1:58](https://youtu.be/OM-DJuwweE0?t=118))
- Throughput gains from DeepSpeed are cited only as results from other projects, with no figures given. ([3:04](https://youtu.be/OM-DJuwweE0?t=184))

## Hot takes
- DeepSpeed is described as an 'I refuse to be out of memory today' button, which is hype beyond what the short demo shows.
- Most DeepSpeed setup failures are CUDA mismatches, not model problems (presenter's experience).
- Benchmarks depend heavily on setup, so large published speedup numbers should not be trusted without testing on your own hardware.
- The config.json is 'the whole game', and the advice is to avoid random config additions.

## Tools mentioned
DeepSpeed, PyTorch, Hugging Face (transformers), Accelerate, Google Colab, CUDA, DSReport (DeepSpeed environment check), ZeRO / ZeRO-Infinity (DeepSpeed features)

## Relevance to our work
- **agentos** (1/3): AgentOS L2B (InferCraft) is inference on one RTX 5090 with CPU-offload KV strategies. This video is about training-time memory sharding and ZeRO offload, which is a different problem, though the offload ladder is a conceptual parallel to the KV offload tiers. → *Read the ZeRO-Infinity offload description next to InferCraft's CPU-offload KV strategy notes to compare the speed-for-capacity trade-off, but do not adopt DeepSpeed training tooling for AgentOS.*
