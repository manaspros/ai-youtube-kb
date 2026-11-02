# The Base Model Is Dead — Varun Singh, Arcee AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `xbPriQWXtWM` · [watch](https://youtu.be/xbPriQWXtWM) · **date:** 2026-08-18 · **length:** 17:45 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Varun Singh · **orgs:** Arcee AI, OpenAI, DeepSeek, Xiaomi, Zyphra
- **topics:** training-finetuning-rl, models-research, data-engineering · **tags:** base-model, pretraining-data-mix, synthetic-data, rephrasing, mid-training, moe-load-balancing, rl-scaling, atomic-skills, reasoning-traces, agentic-priors

> Varun Singh (Arcee AI) argues base models have shifted from storing general web knowledge to priming RL for reasoning and agentic behavior, and explains the data-mix changes this requires.

## Summary
Varun Singh, pre-training lead at Arcee AI, argues that the base model is changing role rather than dying. Older base models were trained mostly on web text, with GPT-3's mix about 85% web text, and post-training only shaped chat behavior. After o1 and DeepSeek R1 made RL a major driver of capability, the base model became a prior for RL on reasoning and agentic tasks. He describes recent practice: web text falling to about 15% of one lab's mix, code and STEM rising, post-training-style SFT data pulled into pretraining, and web-scale synthetic rephrasing. He also covers MoE load-balancing problems caused by distribution shift, mid-training, and the view that SFT now mainly prepares atomic skills for RL. He admits the picture is unclear and frames the conclusion as a shift from world-knowledge priors to reasoning and agentic priors.

## Key ideas
- **RL has moved from a cherry on top to a main driver of capability** — After OpenAI o1 and DeepSeek R1 (Jan 2025), RL could dramatically improve performance, so the base model is now judged as a prior for the large RL phase. ([3:42](https://youtu.be/xbPriQWXtWM?t=222))
- **Web text share in pretraining mixes is shrinking while code and STEM grow** — Web text fell from about 85% of GPT-3's mix to about 15% in MAI Thinking One, which he says reflects growing value of code and STEM for real-world use cases. Code is now the dominant data subset in recipes. ([7:06](https://youtu.be/xbPriQWXtWM?t=426))
- **Post-training-style data is being pulled back into pretraining** — Nemotron 3 Ultra's mix includes SFT-prefixed chat QA data inside pretraining, so the model learns conversation shape and likely downstream task types from the start. ([8:31](https://youtu.be/xbPriQWXtWM?t=511))
- **Synthetic rephrasing upsamples information so the model sees it in several forms** — Trinity Large used large-scale rephrasing of seed items. He says the trend is that synthetic data yields more tokens, cleaner tokens, and tokens shaped like instruct or agentic tasks. ([9:35](https://youtu.be/xbPriQWXtWM?t=575))
- **Post-training data distribution shift can break MoE load balancing** — In MoEs, experts specialize and load balancing is hard. Post-training data differs from pretraining data, so MAI raised the load-balancing coefficient during SFT. He calls this a workaround and prefers stable routing from early on. ([10:36](https://youtu.be/xbPriQWXtWM?t=636))
- **Mid-training exposes the model to post-training distribution and longer context** — Mid-training is a stage that uses the distribution seen in RL and post-training, with longer context for agentic traces. He says pretraining could absorb these data too, instead of a separate stage. ([12:01](https://youtu.be/xbPriQWXtWM?t=721))
- **SFT now mainly prepares atomic skills for RL** — Supervised learning's job shifts to giving the base model the atomic skills RL must compose. The model can extrapolate during RL if the environment difficulty is sufficient. Xiaomi's lab reportedly splits compute roughly equally between pretraining and post-training. ([14:01](https://youtu.be/xbPriQWXtWM?t=841))
- **Novel data such as reasoning traces widens what RL can explore** — Some labs add data whose shape the model has not seen, such as reasoning traces, and warm the model up to test-time compute schemes during SFT or pretraining to improve exploration in RL. ([15:25](https://youtu.be/xbPriQWXtWM?t=925))
- **Think of the field as two paradigms rather than pretrain, mid-train, post-train, RL** — He argues the stage labels are muddy and that the two drivers are supervised next-token prediction and RL, with RL becoming more important. ([13:03](https://youtu.be/xbPriQWXtWM?t=783))

## Techniques
- **Rephrase-based synthetic upsampling** — Take a seed document or data item and generate several rephrasings that keep the same information, then upsample them in the pretraining mix so the model sees the content in multiple forms. *When:* Web-scale pretraining where you need more tokens or cleaner, higher-quality tokens. He cites Trinity Large, Kimi K2 and the Swallow Code and Math datasets.
- **Early injection of post-training-format data** — Include SFT-shaped chat or Q&A data in the pretraining mix rather than only in post-training, labeled by format. *When:* When you want the model to learn task and conversation shape from the start and avoid large distribution shifts later. Also relevant for MoE routing stability.
- **Mid-training on post-training and long-context traces** — Add a stage that exposes the model to the post-training or RL distribution and longer context, including agentic traces. *When:* Before RL, when the pretraining mix lacks agentic traces or long context.
- **Atomic-skill check before RL** — Assess whether the base model has the atomic skills RL needs to compose, and treat SFT as preparation for that composition. *When:* When planning an RL phase on top of a base model, especially where the environment is hard enough that the model must extrapolate.
- **Warm-up on test-time compute formats** — Include reasoning traces or test-time compute formats in SFT or pretraining so the model explores better during RL. *When:* When planning RL for reasoning models, and the model's default outputs do not look like the traces you want it to explore with.
- **Monitor MoE expert utilization under data shift** — Track load balancing and expert utilization when the data distribution changes between pretraining and post-training. *When:* Training MoE models where post-training data differs from pretraining data. He notes raising the coefficient late is a fix he would rather avoid.

## Numbers
- Web text, including Wikipedia, made up roughly 85% of GPT-3's training mix ([1:39](https://youtu.be/xbPriQWXtWM?t=99))
- In Llama 3, roughly 50% of tokens were general-knowledge web data ([2:40](https://youtu.be/xbPriQWXtWM?t=160))
- Web text fell to about 15% of MAI Thinking One's mix ([7:06](https://youtu.be/xbPriQWXtWM?t=426))
- Pretraining and post-training get roughly equal compute allocation in Xiaomi's final model, per an interview he cites ([14:01](https://youtu.be/xbPriQWXtWM?t=841))
- DeepSeek R1 was released in January 2025, following OpenAI o1 in 2024 ([3:42](https://youtu.be/xbPriQWXtWM?t=222))

## Hot takes
- The base model's job has shifted from storing general human knowledge to priming reasoning and agentic behavior for RL.
- Supervised learning now mainly prepares atomic skills for RL rather than being the bulk of training.
- Mid-training as a separate stage is a muddy label; the real split is next-token supervised learning versus RL.

## Tools mentioned
Claude Code

## Relevance to our work
- **general** (1/3): Rephrasing-based synthetic upsampling and seed-based augmentation could apply to our entity-resolution training data, but only if we fine-tune a model. The talk gives no evidence for this and it is a stretch. → *If we ever fine-tune a small model for entity resolution, test rephrasing-based augmentation of seed match pairs on the dev set before adopting it.*
