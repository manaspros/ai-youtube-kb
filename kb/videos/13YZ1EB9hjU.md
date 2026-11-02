# Stop Renting Intelligence: The Train-to-Deploy Loop for Specialized AI — Fireworks AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `13YZ1EB9hjU` · [watch](https://youtu.be/13YZ1EB9hjU) · **date:** 2026-10-12 · **length:** 19:18 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Jatish Sri (Jet) · **orgs:** Fireworks AI, Cursor, Vercel, GenSpark, Qwen, Weights & Biases
- **topics:** training-finetuning-rl, inference-serving, product-ux · **tags:** fine-tuning, RFT, SFT, DPO, open-source models, train-deploy loop, hot-loading, speculative decoding, FireAttention, numerical fidelity, evaluator functions, hyperparameters, vendor talk

> Fireworks AI talk on the train-to-deploy loop: moving from closed models to open-source models by fine-tuning (SFT, RFT, DPO) on the same platform used for hosting, with hot-loading and a training agent. Mostly a product pitch, with a few usable workflow ideas.

## Summary
Jatish Sri (Jet) from Fireworks AI argues that open-source models are production-ready, and that the gap versus closed models is closed through customization and training rather than serving alone. He describes Fireworks' inference stack (FireAttention custom CUDA kernels, speculative decoding, disaggregation, quantization) and claims customer results such as Cursor's Composer 2 at 13x faster inference, Vercel at 40x latency improvement, and GenSpark at 12% quality gain from RFT. The core product idea is a continuous loop: train, deploy with one click, monitor, collect feedback, and retrain from the last checkpoint. Three training surfaces are presented: a training agent (UI, supervised fine-tuning only, with planning and approval steps), managed training (API or UI, with W&B export), and a training API for custom loops and loss functions. Hot-loading swaps new checkpoint weights into a live endpoint without downtime, and the speaker says training and inference on one platform avoid numerical mismatch from moving between platforms. The talk is light on evidence: the benchmarks are customer claims with no methodology, and the demo was mostly UI walkthrough.

## Key ideas
- **Open-source models are now production-ready, and the quality gap with closed models is closed by customization and training, not by serving alone.** — Speaker lists three premises: open models are production-ready (GLM 5.2 cited for coding), differentiation comes from how you train and improve them, and the AI stack is shifting from serve-once to a continuous train-serve loop. ([1:25](https://youtu.be/13YZ1EB9hjU?t=85))
- **Use the same platform for training and inference to avoid numerical mismatch.** — Speaker says training on one platform and hosting on another can degrade quality because numerics differ. Training and serving together are presented as the fix, with no numerical differences after training. ([16:58](https://youtu.be/13YZ1EB9hjU?t=1018))
- **Hot-loading lets a new checkpoint replace live weights without downtime.** — Built for Cursor and then offered generally. A deployment keeps its endpoint and swaps in new weights after a retrain, so the loop closes without a redeploy. ([12:56](https://youtu.be/13YZ1EB9hjU?t=776))
- **Quality, not latency, is the real bottleneck when moving from closed to open models.** — Speaker says customers reach the serving stage only after they are happy with quality. Fireworks answers that gap with training products, and the GenSpark case used RFT with dataset cleaning and evaluator functions. ([7:06](https://youtu.be/13YZ1EB9hjU?t=426))
- **Three training surfaces for three audiences: an agent, managed training, and a raw training API.** — Training agent (UI, plans SFT and picks model and hyperparameters, but no RFT yet), managed training (UI or API, pick hyperparameters and data then click go), and a training API where ML engineers write their own loop and loss. ([7:06](https://youtu.be/13YZ1EB9hjU?t=426))
- **Evaluator functions are the hard part of RFT, and the vendor helps write them.** — Speaker says RFT is now very popular, and that defining a good evaluator function is the hard part. Fireworks helped GenSpark define one, clean data, and tune hyperparameters. ([9:20](https://youtu.be/13YZ1EB9hjU?t=560))
- **Speculative decoding draft models can be trained on the platform from your own dataset.** — Customers upload data the same way as for fine-tuning. A well-trained draft model raises throughput and lowers latency for the main model. ([5:43](https://youtu.be/13YZ1EB9hjU?t=343))

## Techniques
- **Continuous train-deploy-monitor-retrain loop** — Deploy a fine-tuned checkpoint, monitor token volume, cache hit rate and speculator behaviour, gather feedback, then retrain from the current checkpoint and hot-load the result. *When:* When user feedback keeps changing the target and a model must be kept current without rebuilding infrastructure.
- **RFT with a vendor-built evaluator function** — Clean the dataset, write an evaluator function that scores outputs, then run reinforcement fine-tuning against it, tuning hyperparameters for that run. *When:* When a task has a checkable success criterion and you are replacing a closed model that was good enough on it.
- **Training agent with plan approval gate** — Give the agent a dataset (train and eval splits) and a task description. It proposes an SFT plan with base model and hyperparameters, you approve, and it runs and reports metrics with recommended next steps. *When:* For a quick first pass at SFT when the team lacks deep hyperparameter experience. The speaker notes it does not support RFT yet.
- **Draft model training for speculative decoding** — Upload a dataset to train a draft model for the target model, then serve both together. *When:* When latency or throughput targets are not met by the base model alone and the workload's token distribution is stable.
- **Clone-and-compare training runs** — Clone a finished run, change its dataset, hyperparameters or config, and rerun for side-by-side comparison. *When:* When tuning hyperparameters on a fixed dataset.

## Numbers
- About 30 trillion tokens served per day in production, rising by at least 5 trillion/day after the GLM 5.2 release. ([2:39](https://youtu.be/13YZ1EB9hjU?t=159))
- Over 10,000 customer companies and about 200K requests per second. ([2:39](https://youtu.be/13YZ1EB9hjU?t=159))
- Cursor's Composer 2 model is trained and hosted on the platform with 13x faster inference. ([3:52](https://youtu.be/13YZ1EB9hjU?t=232))
- Vercel reports a 40x latency improvement after fine-tuning and hosting on the platform. ([3:52](https://youtu.be/13YZ1EB9hjU?t=232))
- GenSpark saw a 12% quality improvement from its RFT job. ([4:34](https://youtu.be/13YZ1EB9hjU?t=274))
- Company raised about $327M and has about 200 staff. ([4:34](https://youtu.be/13YZ1EB9hjU?t=274))
- Example SFT run picked Qwen3 8B as the base model; the agent reports accuracy and F1 at the end of the run. ([14:54](https://youtu.be/13YZ1EB9hjU?t=894))

## Hot takes
- Open-source models for the most part are production-ready, and what separates them from closed models is post-training work, not the base weights.
- Training and inference should happen on the same platform, because numerical differences between platforms can hurt quality after hosting.

## Tools mentioned
Fireworks AI platform, FireAttention, Weights & Biases, Qwen3 8B

## Relevance to our work
- **agentos** (1/3): AgentOS InferCraft already covers serving with vLLM, KV-cache strategies and speculative decoding on one GPU. The talk's train-serve loop and draft-model training are a different concern and only loosely related to that. → *Read the Fireworks docs on draft-model training to see whether speculative decoding gains depend on the workload, then compare with EAGLE-3 in InferCraft.*
- **general** (1/3): Useful as a reference for the cheap-model and open-model pipeline idea: fine-tune a small model with RFT and an evaluator function, then host it. Claims are vendor-supplied and unverified. → *Treat the 12% GenSpark RFT figure as a claim, and check whether an evaluator-function RFT setup is worth trying on one of our Haiku-style pipelines.*
