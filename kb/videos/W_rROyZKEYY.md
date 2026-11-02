# This Could Change Local AI Forever

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `W_rROyZKEYY` · [watch](https://youtu.be/W_rROyZKEYY) · **date:** 2026-08-02 · **length:** 8:09 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kai Explains host (name not stated in transcript) · **orgs:** PrismML
- **topics:** local-ai, inference-serving, models-research · **tags:** Bonsai 27B, ternary quantization, 1-bit quantization, FP16 group scaling, on-device LLM, KV cache, speculative decoding, open-weight models, RTX 5090, M5 Max, tool calling, quantization benchmarks

> Prism ML's Bonsai 27B compresses a 27B model to 5.9 GB (ternary) or 3.9 GB (1-bit); the speaker says the 1-bit build is a headline and the ternary build is the usable one, with agentic quality falling notably.

## Summary
The video examines Prism ML's Bonsai 27B, released July 14 and built on Qwen 3.6 27B under Apache 2.0, in two variants: a 5.9 GB ternary build (about 1.71 effective bits per weight) and a 3.9 GB 1-bit build (about 1.125 effective bits). The speaker explains the method as low-bit weights with a shared FP16 scale per group of 64 or 128 weights, applied uniformly across the whole network, including embeddings and the output head, rather than leaving the hardest layers at higher precision. The main caveat is memory: file size is not working memory, and KV cache, activations and buffers decide whether a real conversation fits on a 12 GB phone. Reported retention versus full precision is 95% (ternary) and 90% (1-bit) on averages, but the drops are sharper on agentic and tool-calling tasks (80 to 74 to 66) and instruction following (78.4 to 71.8 to 65.8). All benchmarks come from PrismML's own launch post, which the speaker flags as non-independent. The speaker concludes that the ternary build is the more useful variant for agent work, that hybrid local-plus-cloud setups are where it is practical, and that launch speed numbers may not hold in existing GGUF runtimes.

## Key ideas
- **Compression is applied uniformly across the whole network, not partially** — The speaker says PrismML compressed embeddings, attention, MLPs and the LM head alike, with no layers kept at higher precision. The upside is the headline size; the risk is that the weakest-compressed part sets the ceiling. Partial-quantization projects can shrink file size while leaving the hardest layers at FP16. ([2:51](https://youtu.be/W_rROyZKEYY?t=171))
- **Ternary and 1-bit weights use shared group scales to keep dynamic range** — Ternary stores each weight as -1, 0 or +1; 1-bit stores -1 or +1 with no zero. Each group of about 64 or 128 weights shares one FP16 multiplier, giving 1.71 effective bits (5.9 GB) for ternary and 1.125 bits (3.9 GB) for 1-bit. The speaker notes the zero value lets the network silence a connection, which 1-bit loses. ([1:26](https://youtu.be/W_rROyZKEYY?t=86))
- **File size is not working memory: KV cache and activations decide real context length** — A model that fits on disk may not run a real conversation. KV cache grows with every prior token, and activations, kernels and buffers also take memory. On a 12 GB iPhone the speaker estimates the 1-bit build gives only about 4,000 tokens of useful context before memory pressure hurts speed or crashes the app. ([3:54](https://youtu.be/W_rROyZKEYY?t=234))
- **Averages hide the losses that matter for agents** — Overall retention is 95% (ternary) and 90% (1-bit), and math and coding hold up reasonably. Agentic and tool-calling scores fall from 80 to 74 to 66, instruction following from 78.4 to 71.8 to 65.8, and vision from 72.6 to 65.2 to 59.6. The speaker argues these are the categories that decide whether an agent works. ([5:09](https://youtu.be/W_rROyZKEYY?t=309))
- **Benchmarks come from the vendor's launch post and are not independent** — The speaker explicitly says the numbers are PrismML's own and need outside replication and real GGUF runtime tests before they guide buying decisions. ([5:09](https://youtu.be/W_rROyZKEYY?t=309))
- **The ternary build is the practical variant; the 1-bit build is mainly a headline** — Ternary keeps more instruction-following and tool-use quality, the dimensions the speaker says decide whether a local model is useful. The 1-bit build loses about 14 points on agentic tasks. ([6:21](https://youtu.be/W_rROyZKEYY?t=381))
- **Local-plus-cloud hybrid is where this becomes practical** — Keep private filtering, routing and quick actions on-device; send hard reasoning and long context to a cloud model. This cuts API calls and gives an offline mode when connectivity drops. ([6:21](https://youtu.be/W_rROyZKEYY?t=381))
- **Launch speed numbers may not transfer to existing runtimes** — PrismML reports up to 163 tok/s for 1-bit on an RTX 5090 and 87 on an M5 Max. The speaker says current GGUF toolchains are tuned for Q4, Q5 and Q8, and the kernels needed for ternary and 1-bit are newer and less tested. ([6:21](https://youtu.be/W_rROyZKEYY?t=381))

## Techniques
- **Group-scaled low-bit weight quantization** — Split weights into groups of about 64 or 128. Store each weight at 1 or 2 levels (ternary -1/0/+1, or 1-bit -1/+1). Store one high-precision (FP16) scale per group to restore dynamic range. Apply this to every layer, including embeddings and the LM head, rather than leaving some layers at higher precision. *When:* When a model must fit a phone or small-memory device and you can accept a measured quality loss. Evaluate per capability before adopting, since the loss is uneven.
- **On-device memory budgeting beyond file size** — Budget = weights + KV cache at the target context length + activations + kernel/buffer overhead, compared with the memory the OS allows the app (for example about half of a 12 GB phone). Check the context you actually need, not just whether the file loads. *When:* Before choosing a local model for a phone or laptop, and when a demo fits on disk but may not run long conversations.
- **Capability-split regression check before swapping a local model** — Run the candidate and the current model on separate suites: math, coding, instruction following, tool calling, and vision if relevant. Weight tool calling and instruction following most for agent work. Compare against your current quantization (for example Q4 or Q8), not only against full precision. *When:* When deciding whether a more aggressive quantization can replace the local model used in an agent or pipeline.
- **Local-first routing with cloud escalation** — Run a small local model for private filtering, routing and simple actions. Escalate hard reasoning or long-context requests to a cloud model. The local model decides what to escalate. *When:* When data must stay on-device, when offline operation matters, or when routine steps are driving API cost and latency.
- **Validate speed in your own runtime** — Measure tokens per second and time-to-first-token in the exact runtime and kernels you will use, instead of using launch-post figures. Check that the runtime actually uses the fast path for the chosen quantization. *When:* Before treating a vendor speed claim as a planning number, especially for new quantization formats.

## Numbers
- A 27B model at 16 bits needs about 54 GB; a standard 4-bit quantization needs about 18 GB ([0:00](https://youtu.be/W_rROyZKEYY?t=0))
- Bonsai 27B ternary build is 5.9 GB at 1.71 effective bits per weight; 1-bit build is 3.9 GB at 1.125 effective bits ([1:26](https://youtu.be/W_rROyZKEYY?t=86))
- Both variants advertise a 262,000-token context window ([2:51](https://youtu.be/W_rROyZKEYY?t=171))
- An iPhone with 12 GB RAM gives roughly 6 GB to an app; the 5.9 GB ternary build barely fits before generating a token ([2:51](https://youtu.be/W_rROyZKEYY?t=171))
- On a 12 GB phone the 1-bit build gives roughly 4,000 tokens of useful context before memory pressure (speaker estimate) ([3:54](https://youtu.be/W_rROyZKEYY?t=234))
- Retention vs full precision: 95% ternary, 90% 1-bit (averages, vendor-reported) ([3:54](https://youtu.be/W_rROyZKEYY?t=234))
- Math: 95.3 full precision, 93.4 ternary, 91.7 1-bit ([3:54](https://youtu.be/W_rROyZKEYY?t=234))
- Coding: 88.7 full precision, 86.0 ternary, 81.9 1-bit ([3:54](https://youtu.be/W_rROyZKEYY?t=234))
- Agentic and tool calling: 80 full precision, 74 ternary, 66 1-bit (1-bit loses about 14 points) ([5:09](https://youtu.be/W_rROyZKEYY?t=309))
- Instruction following: 78.4 full precision, 71.8 ternary, 65.8 1-bit ([5:09](https://youtu.be/W_rROyZKEYY?t=309))
- Vision: 72.6 full precision, 65.2 ternary, 59.6 1-bit (vision tower is 4-bit) ([5:09](https://youtu.be/W_rROyZKEYY?t=309))
- Launch-post speed: 1-bit up to 163 tok/s on RTX 5090 and 87 tok/s on M5 Max; ternary 134 and 58 ([6:21](https://youtu.be/W_rROyZKEYY?t=381))

## Hot takes
- "The 1-bit build is a headline. The ternary build is a tool." The speaker's bottom line on which variant matters for real work.
- A 27B model at 3.9 GB is a different approximation of the same model, not the same model in a smaller box.
- The title overstates the result: the compression is real, but the agentic-quality drop and the vendor-only benchmarks mean it is not an automatic migration from Q4/Q8 setups.
- Phone demos show that the model fits on disk, which is the easy part; the question is whether a real conversation fits beside it.

## Tools mentioned
Bonsai 27B (PrismML), Qwen 3.6 27B (base model), GGUF runtimes, Q4 / Q5 / Q8 quantizations, speculative decoding, RTX 5090, Apple M5 Max, iPhone (12 GB RAM reference device)

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) already serves quantized models with vLLM on one RTX 5090 and compares quantization strategies (NVFP4). Bonsai is another low-bit point on that curve, and its claimed speed on the same GPU is directly comparable. Its agentic and instruction-following drops are the numbers that would matter for AgentOS tool use. → *Add Bonsai 27B (ternary and 1-bit) to InferCraft's quantization comparison, scored on tool-calling and instruction-following evals rather than only math and coding, and measured in the real vLLM or GGUF runtime, before any adoption decision.*
- **prosharness** (1/3): ProsHarness is a harness around the Claude Code CLI and already has an interest in cheap-model pipelines. The local-filter-then-escalate pattern could apply to its routing steps, but the video does not address the Claude Code path. → *Consider whether a small local model could take the cheap filter and routing steps ProsHarness now sends to a hosted model, and test it on an eval before changing anything.*
