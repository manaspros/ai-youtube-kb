# Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XEd_SRVHBgU` · [watch](https://youtu.be/XEd_SRVHBgU) · **date:** 2026-08-18 · **length:** 20:51 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Sara Hooker · **orgs:** Adaption, Google DeepMind, Stanford
- **topics:** training-finetuning-rl, models-research, evals · **tags:** autoscientist, automated-model-training, data-model-co-optimization, small-models, distillation, pre-training-scaling, compute-access, post-training, open-source-safety

> Sara Hooker (Adaption) argues frontier AI should be open to more builders, and pitches Autoscientist, an automated training loop that co-optimizes data and model while saying pre-training scale is no longer the main lever.

## Summary
Sara Hooker opens with a history of who does discovery, from independent gentleman scientists to the narrow PhD-to-frontier-lab path she says AI research now requires. She argues that compute cost and a handful of frontier labs limit who can shape the frontier, and that labs ship one model to everyone even though problems differ in difficulty. She presents Autoscientist, a beta product that automates model training from data through alignment and searches across architectures and sizes. Her main technical claim is that data must be co-optimized with the model, since automated agents that treat data as just another choice did not get good returns. She argues pre-training scale is no longer the most lucrative axis, that small models are catching up to large ones, and that returns now come from post-training and a wider action space. In Q&A she gives her view on open source and safety (risk is real, but the framing should be control and ownership), says architecture sets the size ceiling, and says distillation helps. Much of the talk is opinion and product pitch, but the co-optimization and stopping-rule points are concrete.

## Key ideas
- **Ship one model to everyone wastes compute** — Speaker argues that spending the same compute on easy and hard problems is inefficient, and that the frontier has narrowed to a few labs with a few kinds of training experience. ([3:47](https://youtu.be/XEd_SRVHBgU?t=227))
- **Autoscientist automates the whole training loop** — Her product searches across data, alignment, model architectures, and dense and MoE designs. She claims it beats research staff because the search base is broader than any one team's experience. This is a product claim, not independently shown. ([4:50](https://youtu.be/XEd_SRVHBgU?t=290))
- **Data must be co-optimized with the model** — She says the approach only worked after data quality was controlled as part of the same search. Auto-research projects that let an agent decide whether to create data did not get the same returns. ([6:08](https://youtu.be/XEd_SRVHBgU?t=368))
- **Automated search can change many hyperparameters at once** — Humans are cautious and change one thing at a time. The automated search changes many at once, which lets it explore the space more widely and makes training more predictable, she says. ([7:11](https://youtu.be/XEd_SRVHBgU?t=431))
- **Pre-training scale is no longer the best lever** — She says pre-training size is not the most lucrative axis now. Inference and post-training compute can be distributed and give more return per FLOP, and small models under 13B are increasingly beating larger ones on leaderboards. ([10:44](https://youtu.be/XEd_SRVHBgU?t=644))
- **Returns now come from a broader action space** — Her view is that the best gains now come from recipe, algorithm and research choices, which lowers the barrier to entry compared with pure scale. ([11:45](https://youtu.be/XEd_SRVHBgU?t=705))
- **Frontier training know-how is secret and apprentice-based** — She estimates fewer than about 5,000 people can train frontier models at scale. Automating that tacit knowledge speeds up experiment cycles, and cheaper experiments change what people choose to ask. ([12:56](https://youtu.be/XEd_SRVHBgU?t=776))
- **Architecture sets the size ceiling; distillation and post-training matter more** — In Q&A she says no frontier lab is likely to make pre-training 4x larger again, so future gains come from post-training, data quality and distillation, not size alone. ([18:39](https://youtu.be/XEd_SRVHBgU?t=1119))

## Techniques
- **Co-optimize data curation with the model in the same search** — Treat data selection and quality as part of the search space that is tuned alongside training choices, rather than letting an agent freely create data as a separate step. *When:* When building automated training or fine-tuning loops, where data quality limits the gains you can get from model search.
- **Win-rate threshold as the stop condition for a training search** — Set a target win rate (she uses above 60%) and stop the genetic search loop once it is reached or the budget runs out. *When:* When running automated search over training recipes with a fixed compute budget and a pairwise win-rate metric.
- **Wide architecture and size search instead of team familiarity** — Test many model architectures, sizes, dense and mixture-of-experts variants, so the search is not limited to the model types your team already knows. *When:* When choosing a base model for a domain and your team's experience would narrow the options too early.
- **Adaptive test-time compute per task (planned)** — She says the next step is to make test-time compute depend on the task, not fixed per request. She gives no implementation detail. *When:* Only as a direction to watch; she describes it as future work.

## Numbers
- Modern computer science has existed for about 77 years, roughly two generations of researchers. ([0:08](https://youtu.be/XEd_SRVHBgU?t=8))
- Autoscientist was released a few weeks before the talk; its beta was announced about four weeks before the talk. ([4:50](https://youtu.be/XEd_SRVHBgU?t=290))
- Autoscientist search stopped once win rates were above 60%, which the speaker describes as a budget stop. ([6:08](https://youtu.be/XEd_SRVHBgU?t=368))
- Adaption covers 242 languages from day one. ([8:35](https://youtu.be/XEd_SRVHBgU?t=515))
- Fewer than about 5,000 people in the world can train frontier models at scale (her estimate). ([12:56](https://youtu.be/XEd_SRVHBgU?t=776))
- Small models under 13B are increasingly outperforming larger ones on the Open LLM leaderboard over time (shown as a trend, not a precise figure). ([11:45](https://youtu.be/XEd_SRVHBgU?t=705))
- GPUs for the beta are offered for free. ([19:44](https://youtu.be/XEd_SRVHBgU?t=1184))

## Hot takes
- Pre-training scale is no longer the most lucrative axis for performance.
- Auto-research agents that treat data as just another agent choice will not get the returns that co-optimized data and model give.
- Frontier model size is near its ceiling for the current architecture; only a new architecture changes that.
- The person with the best idea has a better chance of winning now than the person with the most GPUs.

## Tools mentioned
Autoscientist (Adaption, beta)

## Relevance to our work
- **agentos** (1/3): Her point that the balance between parametric and non-parametric storage is central to continual learning touches MemoryMesh's tiered memory design. Her talk gives no design detail, so the link is thin. → *Read Adaption's Autoscientist or continual-learning material before deciding how to split memory tiers between parametric and non-parametric stores.*
- **general** (1/3): Small models beating larger ones and distillation matter for cheap-model pipelines, but the evidence is an opinion plus a leaderboard trend, not measured results. → *Compare a small model with distillation against the current Haiku pipeline on one task and measure cost and quality before drawing conclusions.*
