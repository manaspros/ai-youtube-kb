# Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `fLUtUkqYHnQ` · [watch](https://youtu.be/fLUtUkqYHnQ) · **date:** 2026-05-18 · **length:** 20:13 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Maxime Labonne · **orgs:** Liquid AI
- **topics:** training-finetuning-rl, inference-serving, models-research, local-ai · **tags:** small-models, edge-models, doom-looping, preference-alignment, DPO, RLVR, repetition-penalty, on-device, short-convolution, embedding-layer, pretraining-scaling, tool-use, LFM2, Liquid AI

> Liquid AI's Maxime Labonne on training 350M to 24B edge models: small models have their own constraints, narrow targeting and doom-loop fixes via DPO and RL.

## Summary
Maxime Labonne (head of post-training at Liquid AI) argues that small edge models are not just shrunk versions of big ones. He frames them around three constraints: memory-bound, task-specific, and latency-sensitive. On architecture, he says Liquid's LFM2 uses a gated short-convolution block chosen by on-device profiling on CPU and GPU, not theory, because it was faster and used less memory than attention alternatives. On training, he reports pretraining a 350M model on 28T tokens and still seeing gains, which he says is beyond Chinchilla-style compute-optimal scaling. The talk then covers "doom looping" (repeated text that never stops) in small reasoning models, which he says SFT does not fix but DPO on on-policy data and RL with verifiable rewards plus a repetition penalty largely do. He ends by arguing small models should be paired with tools (for example web search and a Python environment for long context), since reasoning matters more than memory for them.

## Key ideas
- **Small models have three constraints (memory-bound, task-specific, latency-sensitive) and need their own design, not scaled-down big-model recipes.** — Low knowledge capacity means they should be narrow and good at a few things like summarization, extraction and tool use. The speaker says the stages are the same as for big models, but how you run them differs. ([1:04](https://youtu.be/fLUtUkqYHnQ?t=64))
- **For tiny models, the embedding layer can take a large share of parameters, so the effective reasoning size is much smaller than the headline count.** — He says Gemma 3 270M is about 63% embedding parameters and Qwen 3.5 0.8B about 29%, since big teacher vocabularies were distilled into the student. Liquid's LFM2 keeps the embedding share small so more parameters do the work. ([2:20](https://youtu.be/fLUtUkqYHnQ?t=140))
- **Architecture was chosen by profiling on the target hardware rather than on theory.** — Liquid profiled on an AMD Ryzen Max Plus CPU, a Samsung Galaxy S25 Ultra, and GPU. The gated short-convolution block beat sliding-window attention, Gated DeltaNet, gated linear attention and GQA on speed and memory at the sizes they tested. ([4:36](https://youtu.be/fLUtUkqYHnQ?t=276))
- **Pretraining still helps at very small scale, well past compute-optimal token counts.** — LFM 2.5 350M was pretrained on 28T tokens. The speaker says this is more than Chinchilla would suggest and that the model still improved, so he thinks it was under-trained by the newer scaling laws he cites. ([5:37](https://youtu.be/fLUtUkqYHnQ?t=337))
- **Target a few capabilities (here data extraction and tool use) rather than being average across everything.** — The speaker says that if a small model is not best at code or math, it does not matter much for its intended users. Narrow SFT and RL data help more than broad mixes. ([6:56](https://youtu.be/fLUtUkqYHnQ?t=416))
- **Doom looping is a major small-model failure mode, and it is fixed in preference alignment and RL, not SFT.** — After mid-training the doom-loop ratio on LFM 2.5 1.2B Thinking was about 15-16%, and SFT barely changed it. DPO reduced it a lot and RL made it almost non-existent. ([13:20](https://youtu.be/fLUtUkqYHnQ?t=800))
- **Small models should be paired with tools and environments to cover their weaknesses in knowledge and long context.** — Hallucination from low knowledge capacity can be cut by giving the model web search. Long-context weakness can be worked around with a recursive language model environment where the model uses Python. He argues reasoning, not knowledge, is the key capability for tool use. ([14:40](https://youtu.be/fLUtUkqYHnQ?t=880))

## Techniques
- **On-policy DPO pairs for doom-loop suppression** — Sample 1M prompts. For each, draw five temperature-sampled rollouts from the policy being trained, plus one temperature-0 rollout that is expected to loop. An LLM jury scores all six. Highest score is chosen, lowest is rejected, so looping outputs become negatives. *When:* When training a small reasoning model that loops on hard prompts and you want general preference gains as well as loop removal.
- **Repetition penalty inside RLVR** — Use verifiable rewards (for example extracting a final answer, which gives zero reward if missing) and add a small n-gram repetition penalty. Keep temperature sampling so rollouts are diverse. *When:* When RL is already in the pipeline and you want loops reduced as a side effect, without a separate fix stage.
- **Fix training stage by diagnosis** — Watch RL reward curves. If RL does not learn, suspect missing cold-start SFT data for that task. Add similar SFT samples, then restart from the SFT stage and rerun the later stages. *When:* When RL on a narrow task stalls on a small model.
- **Profile architecture on target hardware** — Implement candidate operators on the actual phone/CPU/GPU targets and measure latency and memory before choosing a block design, instead of relying on FLOP counts. *When:* When designing or choosing an architecture for on-device latency constraints.
- **Tool and environment offload for small models** — Give the model web search for knowledge questions and a Python/recursive-LM environment for long contexts, and train it for reliable tool use. *When:* When the model is too small to hold the knowledge or context a task needs but has good reasoning.

## Numbers
- Model family sizes released by Liquid, from 350M to 24B parameters, across text, vision and audio. ([0:00](https://youtu.be/fLUtUkqYHnQ?t=0))
- Gemma 3 270M: embedding layer is about 63% of total parameters. ([2:20](https://youtu.be/fLUtUkqYHnQ?t=140))
- Qwen 3.5 0.8B: embedding layer is about 29% of total parameters. ([3:15](https://youtu.be/fLUtUkqYHnQ?t=195))
- LFM2 embedding layer is much smaller than competitors'. The auto-caption says about 90%, which contradicts the point being made, so it is likely about 10%. Treat as unverified. ([3:15](https://youtu.be/fLUtUkqYHnQ?t=195))
- LFM 2.5 350M was pretrained on 28 trillion tokens, above Chinchilla compute-optimal, and still improved. ([5:37](https://youtu.be/fLUtUkqYHnQ?t=337))
- Doom-loop ratio on LFM 2.5 1.2B Thinking after mid-training across hard benchmarks: about 15-16%. After SFT it barely moved. ([13:20](https://youtu.be/fLUtUkqYHnQ?t=800))
- Doom-loop ratio after RL on LFM 2.5 1.2B Thinking is described as almost non-existent. DPO reduced it significantly, but no exact figure is given. ([14:40](https://youtu.be/fLUtUkqYHnQ?t=880))
- Qwen 3.5 0.8B in reasoning mode: over 50% doom loops on the speaker's tests. ([14:40](https://youtu.be/fLUtUkqYHnQ?t=880))
- Preference-data generation uses about 1 million prompts, with 5 temperature rollouts and 1 temperature-0 rollout per prompt. ([10:32](https://youtu.be/fLUtUkqYHnQ?t=632))

## Hot takes
- Small models are not just scaled-down versions of big models and need their own training recipe.
- SFT is not the right stage to fix doom loops; preference alignment and RL are.
- Pretraining a 350M model on 28T tokens is still worth it, even though it is far past Chinchilla's compute-optimal point.
- Competitor Qwen 3.5 0.8B in reasoning mode loops over half the time, which he says shows a shrunk big-model recipe does not work for edge models.
- Small models do not need large knowledge; they need reasoning to use tools well.

## Tools mentioned
Hugging Face, Python

## Relevance to our work
- **general** (2/3): Practical evidence that small-model failures (looping, weak long context) are fixed in post-training and by tools, plus a measured loop ratio per training stage. Relevant to the recurring interest in cheap-model (Haiku) pipelines and eval methods. → *Measure loop rate per stage when fine-tuning or choosing a cheap model for a pipeline, and read the Liquid LFM2 technical report for the DPO and RLVR details.*
- **agentos** (1/3): InferCraft targets small local models on one RTX 5090. The talk is on training small models rather than serving them, but its doom-loop measurement and tool-pairing advice are relevant to a small local tier. → *Add a doom-loop metric (share of outputs with a repeated n-gram block over a length threshold) to the L2B eval harness for any small local reasoning model.*
- **prosharness** (1/3): ProsHarness runs long Claude Code loops. A repetition detector like the one described could catch stuck agent turns before they burn tokens. → *Add a repeated-block detector in the loop runner that flags a turn repeating the same long n-gram and triggers checkpoint-and-stop.*
