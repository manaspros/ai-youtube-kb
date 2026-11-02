# Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `btxG75rNJC4` · [watch](https://youtu.be/btxG75rNJC4) · **date:** 2026-09-20 · **length:** 18:06 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Asaf Gardin, Yuval Belfer · **orgs:** AI21 Labs, vLLM, Hugging Face
- **topics:** inference-serving, observability, training-finetuning-rl · **tags:** vllm, mamba, ssm, hybrid-architecture, logprobs, silent-failures, debugging, kv-cache, state-cache, grpo, rl-rollouts, integer-overflow, scheduler, prefill-decode, reproduction

> Two AI21 engineers walk through two silent vLLM bugs for hybrid Mamba models, one a scheduler ordering error and one a 32-bit index overflow, and the debugging method that found them.

## Summary
The speakers from AI21 Labs describe two bugs in vLLM serving their hybrid Mamba-plus-attention model, both found during RL training and production use. Neither crashed or logged an error; the output was just confidently wrong, which they treat as an engineering problem rather than a model-quality one. The first bug produced gibberish roughly once in 1,000 requests, only under vLLM and only under sustained load. They reproduced it faster by lowering GPU memory utilization and running temperature-zero requests, then compared vLLM's logprobs against a prefill-only pass in vanilla Hugging Face Transformers. Bisecting kernels and threading the request ID into the forward context showed the scheduler was sending some requests to decode before prefill, so Mamba read stale state. The second bug caused logprob spikes every 12 RL steps between rollout and the training step; raising rollouts per prompt made it reproduce at step one, but the memory-utilization change that hid it was a misleading lever. The real cause was an unsigned 32-bit index in the Mamba kernels that wrapped silently past about four billion, fixed by moving to a 64-bit type. Their closing point is that stateful inference systems fail quietly, so you need logprob comparison against a baseline and a willingness to read the engine code.

## Key ideas
- **Silent wrong output is the hardest class of inference bug** — No crash, no warning, high confidence in bad text. The speakers treat this as an engineering problem to hunt down, not something a research team can tune away. ([0:17](https://youtu.be/btxG75rNJC4?t=17))
- **Bug 1 looked like rare gibberish that only appeared under vLLM and only at scale** — Roughly one in a thousand requests returned gibberish, late in a run, and only in vLLM. Few requests never triggered it, so it needed a real workload to appear. ([1:17](https://youtu.be/btxG75rNJC4?t=77))
- **Shrink the feedback loop by changing the conditions, not just the volume** — They lowered GPU memory utilization from 90% to 20%, ran many concurrent requests, and used temperature 0 so the failing request (around #854) reproduced deterministically. ([4:04](https://youtu.be/btxG75rNJC4?t=244))
- **Use a vanilla reference implementation as a logprob oracle** — They took vLLM's generated tokens and logprobs, ran a prefill-only forward pass over the full sequence in Hugging Face Transformers, applied softmax, and measured per-token divergence. The Transformers Mamba kernels were simpler and had not been through vLLM's optimizations. ([5:17](https://youtu.be/btxG75rNJC4?t=317))
- **Bisect by forcing computation through one kernel path** — Routing everything through the prefill kernel made the gibberish disappear, which pointed at the decode path. Their first guess was the decode kernels; the real cause was upstream of them. ([7:49](https://youtu.be/btxG75rNJC4?t=469))
- **Root cause: scheduler ran decode before prefill for some requests** — Inside the forward pass, tensors have no request identity. Adding the request ID to a forward-context object and breaking on it showed some requests ran decode first. Mamba reads its state before writing it, so it consumed state left by earlier requests. Attention overwrites its KV cache before reading, so it was tolerant of the same ordering. ([8:45](https://youtu.be/btxG75rNJC4?t=525))
- **Bug 2: logprob spikes every 12 RL steps between rollout and the training step** — With identical weights and inputs, the rollout and training-side logprobs should match. They did not, at a fixed cadence. ([11:26](https://youtu.be/btxG75rNJC4?t=686))
- **Turn up the knob that changes timing to pull the failure forward** — Increasing rollouts per prompt from the default 8 up to 128 moved the spike from step 12 to step 1, which gave them a fast repro loop. ([12:39](https://youtu.be/btxG75rNJC4?t=759))
- **A lever that hides a bug is not the cause** — Lowering memory utilization also made the spike vanish, which was misleading. The actual cause was an unsigned 32-bit index in the Mamba kernels that silently wrapped past about 4 billion. The fix was changing that type to a 64-bit size type. ([13:48](https://youtu.be/btxG75rNJC4?t=828))
- **Shared lessons across both bugs** — Both were silent, both showed up under memory pressure, both were found through logprob forensics, and both lived in the Mamba state cache. The speaker's summary: stateful inference systems do not fail loudly. ([15:10](https://youtu.be/btxG75rNJC4?t=910))

## Techniques
- **Logprob comparison against a reference forward pass** — Generate with the production engine at temperature 0 and keep the per-token logprobs. Re-run the full prompt plus generation through a simple reference model (prefill only), apply softmax, and compute per-token divergence between the two distributions. Keep a script for this. *When:* Any time a serving stack might silently corrupt output, or to validate a kernel, quantization, or scheduler change before shipping it.
- **Reproduce under pressure with determinism** — Lower GPU memory utilization to force small caches and preemption, raise concurrency, and use temperature 0. Then find the smallest failing request ID. *When:* When a bug appears only after many requests and is not reproducible by hand.
- **Thread identity through the forward context** — Attach the request ID to a context object that travels with the batch down to the kernel call sites. Use a conditional breakpoint on that ID to inspect its metadata, such as scheduler decisions and state offsets. *When:* When batched tensors lose the link to the request they came from and you need to see what happened to one specific request.
- **Bisect by forcing one code path** — Route all work through a single kernel path (for example, prefill only) and see whether the symptom goes away. Use the result to narrow the suspect set. *When:* When a bug could sit in one of several kernels or phases of the forward pass.
- **Check whether a fix is causal and watch for overflow** — If a knob changes the failure, verify it causes the failure rather than hiding it. Look for 32-bit indices in kernels that could overflow at large cache offsets, and widen them to 64-bit. *When:* When a symptom appears only at high memory use or large offsets, or when a parameter change seems to make a bug go away.

## Numbers
- Gibberish appeared in about 1 in 1,000 requests in vLLM only, with late onset ([1:17](https://youtu.be/btxG75rNJC4?t=77))
- GPU memory utilization was lowered from 90% to 20% to reproduce; the failing request was around #854 ([4:04](https://youtu.be/btxG75rNJC4?t=244))
- Default RL engine uses 8 rollouts per prompt; the spike happened every 12 steps ([11:26](https://youtu.be/btxG75rNJC4?t=686))
- Raising rollouts per prompt through 16, 32, 64 and 128 moved the spike earlier; at 128 it appeared on step 1 ([12:39](https://youtu.be/btxG75rNJC4?t=759))
- The overflow was an unsigned 32-bit index that wrapped past roughly 4 billion offsets; the fix was a 64-bit size type ([13:48](https://youtu.be/btxG75rNJC4?t=828))

## Hot takes
- Stateful inference systems do not fail loudly; they lie to you confidently.
- Models and LLMs may explain how the code works, but you only really understand a complex engine like vLLM after reading and debugging its code yourself.
- Attention is tolerant of stale KV data because it overwrites before reading, while Mamba's state is read first, so the same scheduling bug is harmless in one and corrupting in the other.

## Tools mentioned
vLLM, Hugging Face Transformers, NVIDIA compute-sanitizer, FSDP, Jamba (hybrid Mamba plus attention model)

## Relevance to our work
- **agentos** (3/3): InfraCraft (L2B) runs vLLM with pluggable KV-cache and state strategies on one RTX 5090, so this talk maps directly onto silent corruption risks in that stack. The logprob oracle and memory-pressure sweep are cheap ways to validate it. → *Add a logprob-divergence check to the InferCraft test suite: run vLLM at temperature 0 under low gpu_memory_utilization and high concurrency, then compare per-token logprobs against a prefill-only HF Transformers reference on the same sequences.*
- **general** (2/3): The logprob-oracle method and the rule to look for what changes the failure shape apply to any serving or eval pipeline. → *Keep a reusable logprob-comparison script against a reference implementation for any self-hosted model used in an agent pipeline, and run it on a load sweep before trusting a new serving change.*
