# Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ewtOo0scUh0` · [watch](https://youtu.be/ewtOo0scUh0) · **date:** 2026-08-18 · **length:** 19:12 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Mahesh Sathiamoorthy · **orgs:** Bespoke Labs, Google DeepMind, OpenThoughts, Stanford, UC Berkeley, University of Washington, Intuit, Credit Karma, Thinking Machines, Terminal-Bench
- **topics:** training-finetuning-rl, data-engineering, sandboxing-execution · **tags:** post-training, data curation, synthetic data, reasoning traces, RL environments, SFT vs RL, teacher model selection, scaling laws, sandboxes, checkpoint and rollback, prompt optimization, enterprise fine-tuning, structured tags, hallucinated numbers

> Bespoke Labs on curating data and RL environments for post-training: OpenThoughts and OpenThoughts-Agent recipes, counterintuitive sampling and teacher findings, and a tag-based SFT fix for numeric hallucinations.

## Summary
Mahesh Sathiamoorthy (Bespoke Labs) argues that data and RL environments are the bottleneck for post-training agents, not compute or models. He describes the OpenThoughts reasoning-data effort, built by ablating each stage of a curation pipeline (question sourcing and filtering, teacher answer generation, answer filtering) and showing performance scales with dataset size. Counterintuitive findings include sampling many answers per question beating more unique questions, and stronger models not always being the best teachers. The same recipe was applied to OpenThoughts-Agent, where he says SFT delivered most of the gains and RL added the last few points. A deployed enterprise case with Intuit/Credit Karma used tags in training data to stop a model from hallucinating numbers like 0% APR, improving compliance, latency and throughput. He ends by sketching a stack of environment quality tracking, sandboxed rollouts with checkpoint and rollback, and SFT/RL on top, plus LLM-reflection prompt optimization. Much of the talk is about Bespoke's own tools and work, so treat the performance claims as the speaker's reported results without independent detail.

## Key ideas
- **Data, including RL environments, is the bottleneck for post-training, not compute or models** — Post-training infrastructure is well defined through providers, but enterprises and frontier labs lack high-quality data and RL environments. He treats environments as data in a different shape. ([4:21](https://youtu.be/ewtOo0scUh0?t=261))
- **Curation works as an ablation-driven recipe that scales with data size** — The OpenThoughts pipeline runs stage by stage (source choice, question filtering with LLM judges for quality and hardness, teacher answers, answer filtering), keeping what each ablation shows helps. The paper reports that metrics keep improving as the dataset grows. ([7:03](https://youtu.be/ewtOo0scUh0?t=423))
- **Sample several answers per question instead of more unique questions** — He calls this counterintuitive: answering one question 16 times beats answering many questions once. His guess is that the varied reasoning traces help fine-tuning. ([10:48](https://youtu.be/ewtOo0scUh0?t=648))
- **Stronger models are not always the best teachers** — This held for reasoning data and for agent trajectories, where he says some Qwen models beat Claude models as teachers. Synthetic question rewriting and task augmentation did not help much. ([10:48](https://youtu.be/ewtOo0scUh0?t=648))
- **SFT gives most of the agent gains and RL adds the last few points** — In building OpenThoughts-Agent, SFT did most of the work. RL is compute-heavy and helped only at the end, and he notes SFT often suffices in enterprise settings. ([13:16](https://youtu.be/ewtOo0scUh0?t=796))
- **Structural tags stop a fine-tuned model from hallucinating numbers** — A fine-tuned model in the Intuit/Credit Karma case invented values such as 0% APR because the data was imbalanced. Adding tags to the prompt-response pairs made the model learn the form instead of the specific figures, which raised compliance, latency and throughput. ([14:42](https://youtu.be/ewtOo0scUh0?t=882))
- **Serious post-training needs a stack of environment quality tracking, sandboxed rollouts and training methods** — The layers are: build environments, measure quality and track versions; sandboxes that run long-horizon rollouts with snapshot and rollback; then SFT and RL on top. He says this is converging with the stack Ross described. ([16:52](https://youtu.be/ewtOo0scUh0?t=1012))
- **LLM reflection can optimize system prompts and harnesses** — He cites a prompt-optimization method that uses an LLM to reflect on failures and rewrite prompts, and says it also works for harnesses. The transcript writes the name as JEPA; this is most likely GEPA, an LLM reflection optimizer, but the speaker did not name it clearly. ([18:07](https://youtu.be/ewtOo0scUh0?t=1087))

## Techniques
- **Stage-wise ablation of a data curation pipeline** — Build the pipeline as sources, then question filter, then teacher answers, then answer filter. Ablate each stage on a fixed eval and keep only what moves the metric before moving to the next stage. *When:* Building SFT or reasoning datasets from many sources where you cannot tell in advance which choices matter.
- **Multi-sample answers per question** — For each training question, generate many teacher answers (he used 16) and keep them all as separate traces rather than sampling many questions once. *When:* When you have a limited question budget and want diverse reasoning traces for fine-tuning.
- **Teacher model selection by measurement** — Test several teacher models on the same questions and pick by downstream student performance, not by teacher size or reputation. *When:* Choosing the model that generates training traces for a smaller student.
- **Structural tags in fine-tuning data** — Wrap the parts of each response that need to be exact (form, or the rule being followed) in tags so the model learns the structure and does not memorize specific values from an imbalanced dataset. *When:* Fine-tuning for compliance-style outputs where a model hallucinates specific numbers or terms from skewed examples.
- **Reflection-based prompt optimization** — Have an LLM read failed runs and reflect on them to propose revised system prompts or harness text, then keep the revisions that score better on a task set. *When:* Improving prompts or harness instructions when you have a reliable eval signal and want to avoid hand-tuning.

## Numbers
- Sampling 16 answers per question was used in the reasoning curation recipe, and was found to beat answering more distinct questions once ([10:48](https://youtu.be/ewtOo0scUh0?t=648))
- Credit Karma/Intuit example: fine-tuning on tagged data improved compliance, latency and throughput, with an example of hallucinated 0% APR. No figures given ([14:42](https://youtu.be/ewtOo0scUh0?t=882))
- Scaling-law curves are shown for both OpenThoughts (reasoning) and OpenThoughts-Agent, with metrics rising as dataset size grows. The talk gives no numeric values ([7:03](https://youtu.be/ewtOo0scUh0?t=423))
- Talk length 19:12 ([0:00](https://youtu.be/ewtOo0scUh0?t=0))

## Hot takes
- Stronger models are not always the best teachers; some Qwen models beat Claude models as teachers for agent trajectories.
- Answering one question 16 times beats answering 16 different questions once.
- For agents, SFT delivers most of the gain and RL is only worth it for the last few points, especially in enterprises.
- Prompt and harness optimization by LLM reflection is a practical lever alongside post-training.

## Tools mentioned
Curator, Bespoke Stratos, OpenThoughts, Terminal-Bench, Tinker, Fireworks

## Relevance to our work
- **agentos** (1/3): SkillForge and EvolveCraft mine agent telemetry into reusable skills and self-improvement, and this talk covers curating agent trajectories into training data. The link is weak because AgentOS has no training pipeline yet. → *Read the OpenThoughts curation paper's stage ablation method before designing how SkillForge turns agent trajectories into training data.*
- **prosharness** (1/3): The reflection-based prompt and harness optimization idea could apply to Claude Code harness prompts, but the talk gives no numbers for it. → *Try a small reflection loop on one ProsHarness planning prompt, scored on a fixed set of past tasks, before changing anything else.*
