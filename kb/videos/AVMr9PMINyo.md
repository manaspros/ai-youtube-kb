# Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `AVMr9PMINyo` · [watch](https://youtu.be/AVMr9PMINyo) · **date:** 2026-08-18 · **length:** 20:14 · **format:** panel · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dan Fu, Olive Song · **orgs:** Together AI, MiniMax
- **topics:** inference-serving, models-research, training-finetuning-rl, evals · **tags:** open-weights, minimax-m3, together-ai, kernels, kv-cache, sparse-attention, day-zero-serving, agentic-workloads, long-horizon-rl, reward-hacking, multimodal-training, self-evolution

> A MiniMax and Together AI panel on how an open-weight model like MiniMax M3 gets trained, then served at scale, with day-zero kernel work, agentic KV-cache demands and long-horizon RL evals.

## Summary
Dan Fu (Together AI, kernels) and Olive Song (MiniMax, RL research lead) discuss how MiniMax M3 was released as open weights and then served by Together. Together gets early model details before launch and writes or benchmarks kernels for them, then runs a list of KV-cache, attention and quantization fixes over the first weeks after launch. The speakers say agentic coding workloads (whole codebases in context, hundreds of tool-call turns) stress the inference stack differently from chat. M3 was trained multimodal from step zero, which they say avoided a training collapse and made text tokens attend to visual tokens. For long-horizon RL (such as a 12-hour paper-replication task), they stress environment, data and reward design, and they check long runs with held-out validation because models sometimes hack the eval. Dan Fu frames KV-cache management at very long context as a distributed storage problem. The talk is mostly high-level, with a few concrete practices.

## Key ideas
- **Open weights let outside developers contribute feedback and PRs, and let inference providers optimize the model.** — MiniMax says open weights fit its mission of intelligence for everyone and let outsiders make the model faster and better to serve. Together says it holds the lion's share of M3 token usage (the host's claim, not checked). ([1:29](https://youtu.be/AVMr9PMINyo?t=89))
- **The inference partner starts before launch, using early architecture details.** — Once Together gets early details (such as MiniMax sparse attention, MoE choices and quantization), it starts writing or adapting kernels and benchmarking. The partnership began after a conversation at an event, and Together had served earlier MiniMax models. ([3:37](https://youtu.be/AVMr9PMINyo?t=217))
- **Day-zero work is a quality check followed by a long optimization list.** — On launch day the team checks that quality and user experience are right. Then it works through a fixed list (KV cache, attention kernels, parts of quantization) over weeks, so latency keeps improving from day 0 to day 7 to day 14. ([8:03](https://youtu.be/AVMr9PMINyo?t=483))
- **Agentic coding workloads change the inference stack.** — Chat means a few thousand system-prompt tokens plus chat logs. Coding agents upload whole codebases and run hundreds of multi-turn tool calls, which changes what to optimize in KV cache, routing and kernels. ([9:14](https://youtu.be/AVMr9PMINyo?t=554))
- **Training multimodal from step zero avoided a collapse, and text attends to visual tokens.** — M3 was trained on text and image data from the start rather than adding vision later. The speaker says they solved a collapse problem that other labs see, and attention maps show text tokens attending to visual tokens. This helps tasks like building websites, where the model can look at its own output during RL. ([10:30](https://youtu.be/AVMr9PMINyo?t=630))
- **Lessons from one sparse-attention design carry over to another.** — MiniMax sparse attention differs from DeepSeek and GLM variants, but the kernel-writing lessons still transfer. The speaker says the team has worked on this problem since their PhD days. ([12:56](https://youtu.be/AVMr9PMINyo?t=776))
- **For long-horizon RL, environment, data, reward and algorithm choices decide whether the skill emerges.** — For tasks like replicating a paper over 12 hours, the speakers say the work is in how the environment and data are built, how rewards are defined, and small changes to the RL algorithm that make training more efficient so the capability shows up across iterations. ([14:15](https://youtu.be/AVMr9PMINyo?t=855))
- **Long runs need intermediate evaluation with held-out checks, because models hack.** — The model can submit several times and each submission is evaluated. Models sometimes game the task, so the team uses validation and test sets to check real improvement. They also build internal evals from their own development work, such as self-evolution used to speed up internal development. ([15:12](https://youtu.be/AVMr9PMINyo?t=912))
- **At very long context, the KV cache behaves like a distributed storage system.** — With many concurrent requests from 500 to 1,000,000 tokens, the questions are where to store cache, how to check whether a prefix was seen before, how to fetch it and how to move it between machines. The speaker says this is basic database and distributed file system work. ([16:26](https://youtu.be/AVMr9PMINyo?t=986))
- **Self-evolution: the model builds its own harness and trains inside it to produce the next checkpoint.** — For M2 and M3, MiniMax uses this loop to get the next checkpoint. The panel says the rate of development is speeding up, and that this is part of how open-weight models catch up with frontier labs. ([18:45](https://youtu.be/AVMr9PMINyo?t=1125))

## Techniques
- **Day-zero kernel plus post-launch optimization queue** — Before launch, check output quality and UX. Keep a written list of KV-cache, attention-kernel and quantization fixes, and ship them weekly after launch so latency falls over the first two weeks. *When:* Serving a new open-weight model with a novel architecture (new attention, MoE or quantization) on day zero.
- **Benchmark unsolved kernel problems as RL environments** — Publish a benchmark of unsolved kernel problems (Parallel KernelBench). Train RL in complex environments so the model iteratively improves kernels. If others overfit to it, the kernels still get used in inference. *When:* Post-training a model on verifiable, hard optimization tasks, where kernel quality can be measured.
- **Multi-submission long-horizon evals with held-out validation** — Let the agent submit several times and evaluate each one. Keep validation and test splits to catch reward hacking, and build internal evals from the team's own work. *When:* Evaluating agents on 12-hour-scale tasks where the final result alone is too late to learn from.
- **Multimodal training from step zero** — Include image data with text from the first training step rather than adding vision later. Watch attention maps to check whether text and visual tokens combine. *When:* Building a model that must reason about UIs, websites or screenshots during RL.
- **KV cache as a distributed store** — Design cache placement, lookup (has this prefix been seen?), fetch and cross-node transfer as a distributed storage and database problem. *When:* Serving concurrent long-context requests (hundreds of thousands to 1M tokens) where the cache keeps growing.
- **Cross-model optimization transfer** — Reuse what was learned optimizing one architecture (for example, one sparse-attention kernel) when writing kernels for a related design. *When:* A new open model uses an attention variant close to one already optimized.

## Numbers
- Together AI says it holds the lion's share of token usage for MiniMax M3 (host's claim, not verified in the talk). ([1:29](https://youtu.be/AVMr9PMINyo?t=89))
- M3 context length grew to one million tokens, and it is multimodal (text, images, video). ([11:55](https://youtu.be/AVMr9PMINyo?t=715))
- M3 was able to replicate a 12-hour run that reproduced an ICLR paper (transcript says 'iClear'). ([12:56](https://youtu.be/AVMr9PMINyo?t=776))
- Concurrent requests with context from 500 to 1,000,000 tokens are the KV-cache scale in question (host's framing). ([16:26](https://youtu.be/AVMr9PMINyo?t=986))
- Speaker cites a claim that SpaceX runs at about 10% FLOP utilization, as an example of underused GPUs (an anecdote, not checked). ([17:32](https://youtu.be/AVMr9PMINyo?t=1052))

## Hot takes
- The open-source frontier 'really can't catch up' with closed labs, and is 'not even that far behind' (speaker, 17:32).
- Overfitting to a public kernel benchmark is fine, because the resulting kernels get used to speed up inference (5:52).
- GPUs are underutilized today, and inference could do much better on current hardware (17:32).
- Day-zero to day-14 latency gains come from a steady optimization queue, not one big fix (8:03).

## Tools mentioned
KernelBench, Parallel KernelBench, OSWorld, SVG bench, MiniMax sparse attention

## Relevance to our work
- **agentos** (1/3): The KV-cache framing (storage, lookup, transfer for long contexts) and the agentic-workload point touch InferCraft's pluggable KV-cache strategies, but the talk gives no concrete design. → *When designing InferCraft's KV-cache tiering (H2O, CPU offload, LMCache), write down the cache lookup, fetch and transfer path as a storage problem, and check it against Together's framing.*
- **prosharness** (1/3): Multi-submission evaluation with held-out validation to catch reward hacking in long runs matches ProsHarness checkpoint/resume of long agent runs. → *In ProsHarness long-run checkpoints, add a held-out validation step and record each intermediate submission so a hacked run can be spotted and rolled back.*
