# Scaling Compute on Context — Jack Morris, Engram

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `WiqDvX6isc4` · [watch](https://youtu.be/WiqDvX6isc4) · **date:** 2026-08-18 · **length:** 19:42 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Jack Morris · **orgs:** Engram
- **topics:** memory, training-finetuning-rl, models-research, context-engineering · **tags:** continual-learning, knowledge-injection, self-improvement, synthetic-data, context-compaction, on-policy-distillation, self-study, unsupervised-rl, data-wall, personalization

> Jack Morris (Engram) frames "scaling compute on context": with a fixed private dataset and a pretrained model, the only scaling axis left is compute, and he surveys why naive, compaction, distillation, synthetic-data and RL approaches all saturate.

## Summary
Jack Morris, a researcher at the startup Engram (the transcript spells it "Ngram"), argues that models cannot acquire private or post-cutoff knowledge because they are trained on public data, and that this is the core limit of the current paradigm. He frames the problem as taking a pretrained model and an unstructured dataset D and producing a model that truly knows D, which he calls scaling compute on context. He notes that with a fixed data budget and a pretrained starting point, compute is the only real axis left. He walks through approaches: naive next-token training (which reaches near-zero loss but collapses in generation), KV compaction for data that fits in context, on-policy distillation and self-study, synthetic continued pretraining, and unsupervised RL. His conclusion is that any fixed dataset eventually saturates, so the goal is self-improvement, where the model generates progressively harder training data for itself. The talk is conceptual and light on experiments, and it closes with a hiring pitch for the company.

## Key ideas
- **Models cannot acquire new or private knowledge after training because they are trained only on public data.** — Models know Wikipedia, Reddit, arXiv and GitHub but not a user's emails, a company's internal data, or events after their cutoff. He calls this the core problem of the current paradigm, not just an academic one. ([2:55](https://youtu.be/WiqDvX6isc4?t=175))
- **With a fixed data budget and a pretrained starting model, compute is the only scaling axis left.** — Data can't be created, and training from scratch on private data is impractical, so the question becomes how to scale compute over the same data set D. He notes that data access is not truly fixed (you can find more sources), but the idealised framing is compute-only. ([7:01](https://youtu.be/WiqDvX6isc4?t=421))
- **Naive next-token training on a private corpus memorises it but does not yield a usable model.** — Training until loss is about 0.0001 on 10K financial reports gives a model that knows the text, yet it collapses when generating and can only answer questions whose answers are directly encoded in the data. Training also has a bounded effect. ([10:52](https://youtu.be/WiqDvX6isc4?t=652))
- **Compaction and gradient-based 'make the model think the data is in context' are two different routes.** — KV compaction compresses data that fits in context into a small set of KV entries, but it only works for in-context data and misses what gradients provide. On-policy distillation trains the model to act as if the text were in context. ([12:16](https://youtu.be/WiqDvX6isc4?t=736))
- **Synthetic data and self-study are the most promising near-term routes, but each has costs.** — Self-study generates QA pairs conditioned on D. Synthetic continued pretraining overwrites some pretraining, is hard to scale, and forces a post-training step afterwards. Many teams start from post-trained models, which makes this harder. ([13:25](https://youtu.be/WiqDvX6isc4?t=805))
- **Every fixed-dataset method eventually saturates, creating a synthetic data wall.** — Once the model has learned all of the data (or all the synthetic data), further training gives no more gains. Unsupervised RL environments and distillation share this limit. Pretraining's scaling curve does not hold for them. ([15:41](https://youtu.be/WiqDvX6isc4?t=941))
- **The target is self-improvement: the model should generate harder training data for itself.** — He compares this to AlphaGo, which makes its own training questions harder as it improves. Engram's early runs plateaued in the same way, and he reports that more sophisticated, gradually harder curricula do better. The goal is a curve that keeps rising with compute. ([17:00](https://youtu.be/WiqDvX6isc4?t=1020))

## Techniques
- **Naive continued training on a private corpus** — Run next-token training on the raw documents until the loss is very low. *When:* Treat as the baseline to avoid. It memorises but does not generalise or answer unseen questions, so it is a bad fit for knowledge injection.
- **KV compaction of in-context data** — Compress a long context D into a small set of KV entries that stand in for it during inference, using a learned or greedy compaction method. *When:* Only when the whole dataset fits in the context window. It does not give the benefits of gradient updates, so it is not general.
- **On-policy distillation toward in-context behaviour** — Show the model text, then train it, on its own rollouts, to behave as if that text were in context, updating throughout training. *When:* When you want knowledge in the weights without raw text in the prompt. The hard part is choosing what data to distil, since raw documents do not work well.
- **Self-study (generated QA conditioned on the corpus)** — Generate question-answer pairs grounded in D, then train the model so it answers as if D were in context (Cartridges-style). *When:* When you need question-answering behaviour over a private corpus. He notes it has undesirable properties that he left for later slides.
- **Synthetic continued pretraining** — Craft synthetic documents conditioned on D, then continue pretraining on them as if it were a pretraining stage. *When:* When you want pretraining-style knowledge absorption. Costs include overwriting part of the base model's pretraining, scaling difficulty, and a required post-training step afterwards.
- **Unsupervised RL environments over the corpus** — Build RL environments that come from the data without labels and train with a GRPO-style loss. *When:* As an alternative to distillation. He argues it still saturates like the other fixed-dataset methods.
- **Gradually harder self-generated curriculum** — Loop: the model generates training data, trains on it, then generates harder data from its improved state, so difficulty grows over time. *When:* When fixed datasets plateau. He presents this as the direction to pursue for compute that keeps improving the model, though he gives no implementation detail.

## Numbers
- Naive next-token training on 10K financial reports reaches a loss of about 0.0001, yet the model collapses in generation. ([10:52](https://youtu.be/WiqDvX6isc4?t=652))
- The corpus in the example is 10K financial reports. ([10:52](https://youtu.be/WiqDvX6isc4?t=652))
- Models are pretrained with a cutoff and cannot answer about events after it, such as a sports result from the previous night. ([7:01](https://youtu.be/WiqDvX6isc4?t=421))
- The company's early training curves plateaued, with no gain from more data or training. ([17:00](https://youtu.be/WiqDvX6isc4?t=1020))

## Hot takes
- Scaling on public data is the driver of progress, but it cannot personalise a model; the missing piece is private knowledge.
- Next-token training on a corpus until loss is near zero produces a model that memorises but does not generalise.
- Any fixed-dataset method saturates, so there is a synthetic data wall that requires self-improvement to get past.
- Compaction misses what gradient updates give, so it does not generalise to knowledge injection.

## Tools mentioned
Cartridges (self-study paper, named on slide), On-policy distillation, GRPO (named as an RL loss example), KV cache compaction (named approach)

## Relevance to our work
- **agentos** (1/3): The talk's taxonomy of ways to get user-specific knowledge into a model is adjacent to MemoryMesh's tiered cross-session memory. It does not change current design. → *When designing MemoryMesh's cross-session tier, keep 'store and retrieve memory' separate from 'learn into weights' and note the saturation argument before any fine-tune-on-user-data idea.*
