# Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards — Filip Makraduli

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `c1hGBoWw20A` · [watch](https://youtu.be/c1hGBoWw20A) · **date:** 2026-09-20 · **length:** 17:18 · **format:** talk · **quality:** 4/5 · **depth:** deep
- **speakers:** Filip Makraduli · **orgs:** Superlinked, Hugging Face
- **topics:** inference-serving, models-research · **tags:** RMSNorm, weight folding, deferred normalization, flash norm, CUDA streams, race condition, kernel fusion, torch.compile, quantization, Llama, Hugging Face, self-hosted inference

> Filip Makraduli on "flash norm": algebraic rewrites of RMSNorm (weight folding, deferred division) that speed up transformer decoding, plus a CUDA stream race that corrupted long generations.

## Summary
The speaker co-authored a paper with Niels Graf on restructuring RMSNorm so it costs less in wall-clock time, even though its arithmetic is tiny. The main idea is that GPUs are slow at the overhead around math (launching work, moving memory, waiting on sync), and RMSNorm is called many times per decode step. Three algebraic moves address this: weightless normalization with the gain folded offline into the next matrix (weight folding), deferring the scalar division until after the matmul so vector and matrix units can run in parallel, and dropping a redundant pre-norm when two norms are scale-invariant. Applying the parallel version needs custom CUDA kernel work, and the speaker's first attempt had an implicit stream join that let post-scale reads hit an unfinished buffer. Short unit tests and perplexity looked fine, and only long generations exposed repetition and one-step lag. The fix was explicit event markers on both streams before the join. The talk ends with a pitch for deploying custom Hugging Face checkpoints on a self-hosted cluster (Superlinked's inference engine), with smarter queuing for small models. No benchmark numbers for the speedup are given beyond "some improvement" on Llama models.

## Key ideas
- **GPUs are not slow at math but at everything around it; RMSNorm does little arithmetic yet costs a lot of wall-clock time.** — In one decode step RMSNorm can be launched about 33 times (model-dependent). The overhead is in starting work, moving memory, and waiting, not in the math itself. ([1:43](https://youtu.be/c1hGBoWw20A?t=103))
- **Weight folding moves the norm gain into the next matrix offline.** — Using weightless normalization, the gain is multiplied into the following weight matrix once, ahead of time, so the runtime does not need that extra step or memory pass. ([4:33](https://youtu.be/c1hGBoWw20A?t=273))
- **Deferred normalization splits the scalar division off the matmul so the two can run in parallel.** — Normally the code computes, waits, then computes again. Moving the division after the matmul lets the vector unit compute the RMS while the matrix unit runs the matmul. ([4:33](https://youtu.be/c1hGBoWw20A?t=273))
- **A redundant pre-norm can be dropped when two norms in a row are scale-invariant.** — The speaker says one of two RMSNorm layers can be removed without changing results, and that newer architectures such as Gemma 4 can hit this case. ([5:56](https://youtu.be/c1hGBoWw20A?t=356))
- **Weight folding is easy to apply to any model, but the parallel-stream version needs kernel work.** — The transformer-tricks repo applies weight folding (proposition 1) to a model with a simple script. The deferred-normalization path needs custom CUDA kernels. ([5:56](https://youtu.be/c1hGBoWw20A?t=356))
- **An implicit stream join caused a race condition that short tests did not catch.** — The post-scale step read an old buffer value because one stream had not finished its matmul. Unit tests and perplexity looked similar. Only long generations showed repetition and a one-step lag in the output. ([9:12](https://youtu.be/c1hGBoWw20A?t=552))
- **Make every cross-stream join explicit: mark the end of each stream's work and wait on both before reading.** — The fix records an end marker on the matmul stream and on the RMS stream, then waits for both before the post-scale step. This removed the bug and restored correct output. ([9:12](https://youtu.be/c1hGBoWw20A?t=552))
- **Weight folding alone still helps and works with standard tooling.** — The speaker says the simple weight-folding version shows some gain, works with torch.compile because the result is a new checkpoint, and works with quantized models. ([11:52](https://youtu.be/c1hGBoWw20A?t=712))

## Techniques
- **Weight folding of norm gain into the next linear layer** — Compute W' = gain * W offline and use a weightless normalization at runtime. The result is a plain checkpoint that loads in normal tooling. *When:* Any transformer with RMSNorm followed by a linear layer where you can rewrite the checkpoint once. The speaker reports it works with torch.compile and quantized models.
- **Deferred scalar division for overlap** — Move the RMS scalar division after the matmul, so the vector unit computes the RMS while the matrix unit runs the matmul. *When:* Decode-time kernels where norm and matmul are serialized and the GPU is idle during the norm. Needs custom CUDA kernels rather than Python.
- **Explicit CUDA stream join with event markers** — Record an event at the end of each parallel stream's work, then have the joining stream wait on every event before it reads the shared buffer. Do not rely on implicit ordering. *When:* Any time two CUDA streams write to buffers that a later op reads. Implicit joins can pass short tests and fail on long runs.
- **Long-generation regression check for kernel changes** — After a kernel or stream change, generate long outputs and look for repetition or one-step lag, not just perplexity or short unit tests. *When:* Before trusting any custom kernel or concurrency change in an inference path.
- **Deploy custom Hugging Face checkpoints on a self-hosted cluster** — Push a modified HF checkpoint to a self-hosted inference cluster with an API for model config, and use a queue that lets several small models share one GPU. *When:* Testing research variants of open-weight models without renting a closed endpoint, where you need to own the inference stack.

## Numbers
- RMSNorm can be launched about 33 times in one decode step (model-dependent). ([1:43](https://youtu.be/c1hGBoWw20A?t=103))
- Weight folding alone shows some improvement on Llama models; no speedup figure is given in the talk. ([11:52](https://youtu.be/c1hGBoWw20A?t=712))
- The paper's core change is described as two lines of algebra. ([0:16](https://youtu.be/c1hGBoWw20A?t=16))

## Hot takes
- GPUs are bad at everything around the math, not the math itself.
- Perplexity and short unit tests can pass while a concurrency race silently corrupts long generations.

## Tools mentioned
Hugging Face, CUDA streams, torch.compile, transformer-tricks repo

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on one RTX 5090 and already uses quantization. This talk covers kernel-level norm rewrites and a concurrency bug that short tests missed, both relevant to the inference pillar. → *If InferCraft ever adds a custom kernel or multi-stream path, add a long-generation regression check (repetition and one-step lag) to its tests, since perplexity missed the race here. Then read the transformer-tricks repo to see whether weight folding applies to the Llama-family checkpoints InferCraft serves.*
- **general** (1/3): The stream-join bug is a general lesson: validate concurrent or async code on long, realistic runs, not just short unit tests and aggregate metrics. → *Note the lesson for any eval or test plan: include long-horizon output checks, not only aggregate scores.*
