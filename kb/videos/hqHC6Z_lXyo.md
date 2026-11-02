# 20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `hqHC6Z_lXyo` · [watch](https://youtu.be/hqHC6Z_lXyo) · **date:** 2026-06-18 · **length:** 19:36 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Bertrand Charpentier · **orgs:** Pruna
- **topics:** evals, models-research, inference-serving · **tags:** model-selection, leaderboards, pareto-front, image-generation, eval-methodology, statistical-significance, clip-score, efficiency, compression, denoiser-step-reduction, video-generation

> Public leaderboards and manual or metric-based checks mislead model choice; the speaker argues for task-specific, many-sample evals plus Pareto fronts of quality vs latency and cost, where smaller fast models often win.

## Summary
The speaker (Bertrand Charpentier of Pruna) asks what state-of-the-art means for a model, and says the two usual answers, public leaderboards and internal evals, both lead teams to a large foundation model by default. He shows that image-editing leaderboards (Design Arena, LM Arena, Artificial Analysis) disagree on the top model and on ELO ranges, and that per-task rankings differ from the aggregate ones. He argues that leaderboards rest on a few thousand samples and that the top model still loses many battles, so teams should evaluate on samples that match their final conditions. He shows that manual inspection is biased by personal taste and by the few prompts chosen, and that metrics such as CLIP score are unstable across datasets, while a task-specific text-rendering metric gave consistent, well-separated rankings. He then makes the cost case: one leaderboard's 26K battles took about 20 days of compute, about $5K and roughly 556 kWh, against 7 hours and $265 for a fast model. He recommends Pareto plots of quality against latency or price, which show several co-equal state-of-the-art models, and closes with compression methods (per-module quantization, pruning, fewer denoising steps via distillation or caching) and a pitch for Pruna's endpoints. The Q&A adds detail on those compression methods.

## Key ideas
- **Public leaderboards are a weak basis for choosing a model** — Image-editing leaderboards disagree on the top model and on relative ranks, and ELO scales differ between boards (one cited range 1,100 to 1,300 on one board, another on a different scale). Use several boards and treat models within noise as equivalent. ([2:31](https://youtu.be/hqHC6Z_lXyo?t=151))
- **Use case beats aggregate rankings** — Per-task leaderboards (object removal, background change, text editing) show different winners, and no single model dominates all of them. Filter public boards to the task you will actually run. ([3:57](https://youtu.be/hqHC6Z_lXyo?t=237))
- **Leaderboards are statistically thin for your conditions** — Each board is built on a few thousand samples, far fewer than production traffic. Even the top model loses at least around 40% of battles, so picking the top-ranked model can pick the wrong one for your slice. Evaluate on samples close to the final setup. ([5:25](https://youtu.be/hqHC6Z_lXyo?t=325))
- **Manual inspection is biased twice over** — A live audience split its preference across the same three images, and the vote changed when the prompt changed. Personal taste and the few samples you look at both skew the result, so get many raters on many prompts. ([7:43](https://youtu.be/hqHC6Z_lXyo?t=463))
- **Automated metrics need validation before use** — CLIP score rankings changed across datasets, and the score gaps between models were tiny on a 0 to 1 or 0 to 100 scale. Understand what the metric measures, use several, and prefer task-specific metrics such as text rendering, which gave consistent rankings with clear gaps. ([10:10](https://youtu.be/hqHC6Z_lXyo?t=610))
- **Quality mostly tracks compute, so measure efficiency too** — A large-model eval of 26K battles took about 20 days of compute, $5K and about 556 kWh (the speaker's estimate: about 400 marathons of energy). A fast model ran the same eval in 7 hours for $265. Quality gains often do not justify the compute cost. ([12:06](https://youtu.be/hqHC6Z_lXyo?t=726))
- **Multiple state-of-the-art models exist on a Pareto front** — Plot quality (ELO) against latency or price and draw the Pareto front. Several models sit on it at similar quality, with up to about 20x speed differences. Repeat the plot with a task-specific quality metric for your use case. ([14:33](https://youtu.be/hqHC6Z_lXyo?t=873))
- **Smaller performance models can replace the default foundation model** — The speaker's conclusion is that careful evaluation finds many small, fast, task-tuned models rather than one general large one. Compression methods that make this possible include per-module quantization, pruning, and cutting denoiser steps (from 20 to 50 down via distillation or caching, roughly 4x to 20x fewer computations). ([16:04](https://youtu.be/hqHC6Z_lXyo?t=964))

## Techniques
- **Pareto front selection** — Plot each candidate on quality (ELO or task metric) against latency or price. Keep the non-dominated models, and pick by the cost or speed you need among them. *When:* Choosing among models or deployment configs when quality gaps are small or within noise.
- **Consensus across leaderboards and per-task boards** — Check several public leaderboards and per-task splits. Look for models that rank well everywhere, and treat tied or near-tied models as equivalent. *When:* Shortlisting models from public rankings before any internal testing.
- **Large-sample, condition-matched human evaluation** — Run many raters on many prompts under the final input and output conditions. Track win rate and not only the rank. *When:* Judging generative output where taste matters, and where single-person spot checks are too noisy.
- **Metric validation before use** — Test whether a metric's ranking is stable across datasets and whether its gaps are larger than noise. Add task-specific metrics where the generic one is flat. *When:* Before trusting any automated score to decide between models.
- **Compression for latency (quantization, pruning, step reduction)** — Quantize each module with its own setting, prune components that matter little, and reduce the diffusion denoiser steps through distillation or step caching. Re-check quality on the target task after each change. *When:* Serving image or video generation models where latency or cost dominates and the quality loss is measurable.

## Numbers
- Image-editing leaderboards (Design Arena, LM Arena, Artificial Analysis) give different top models and different relative ranks; one model moves from rank 10 on Artificial Analysis to rank 5 on Arena. ([2:31](https://youtu.be/hqHC6Z_lXyo?t=151))
- ELO ranges differ across leaderboards (one cited range 1,100 to 1,300). ([2:31](https://youtu.be/hqHC6Z_lXyo?t=151))
- Public leaderboards are built on a few thousand samples each; the speaker says Pruna serves millions of runs per day. ([5:25](https://youtu.be/hqHC6Z_lXyo?t=325))
- No model in the image-editing leaderboards reaches near 100% win rate; most models lose at least about 40% of battles. ([6:44](https://youtu.be/hqHC6Z_lXyo?t=404))
- Large-model eval: 26K battles, about 62 seconds per image, about 20 days of compute, about $5K, about 556 kWh (speaker's estimate: about 400 marathons of energy). ([12:06](https://youtu.be/hqHC6Z_lXyo?t=726))
- Fast model eval: under 1 second per image, 7 hours total for the same 26K evals, $265, about 4 marathons of energy. ([13:07](https://youtu.be/hqHC6Z_lXyo?t=787))
- Top models on the quality plot sit between about 1,100 and 1,200 ELO, with up to about 20x speed difference between Pareto points. ([14:33](https://youtu.be/hqHC6Z_lXyo?t=873))
- Denoiser steps: typical image or video generation uses 20 to 50 steps; distillation or caching can cut computation about 4x to 20x, depending on aggressiveness (speaker's figures). ([17:54](https://youtu.be/hqHC6Z_lXyo?t=1074))
- Pruna's endpoints for image and video models run in about 1 to 5 seconds (speaker's claim). ([16:04](https://youtu.be/hqHC6Z_lXyo?t=964))

## Hot takes
- Benchmarking is not dead, but it has to be run carefully: done properly, it finds many small performance models rather than one large foundation model.
- A single public leaderboard rank, or one manual comparison, is not enough to call a model state of the art.
- There is no single state-of-the-art model; there is a Pareto front of models that trade quality against speed and cost.
- Quality gaps of about 100 ELO points between the top models can be worth less than a 20x speed or cost difference.
- Picking the top-ranked model by default is often the lazy choice, and it can be wrong for your specific slice.

## Tools mentioned
Design Arena, LM Arena (now Arena), Artificial Analysis, CLIP score, Pruna open-source compression package

## Relevance to our work
- **general** (2/3): The core method (condition-matched evals with many samples, multiple metrics, and Pareto selection on quality against cost) applies to any model choice, including Haiku pipelines and entity-resolution evaluation. → *For the entity-resolution work, check that model or prompt rankings hold across several slices of our own data (for example per country) with enough samples before picking one, and plot F-score against cost per candidate.*
- **agentos** (1/3): Model choice for strategy routing and InferCraft serving could use quality-versus-cost Pareto selection, but the talk covers image and video models only. → *When adding model-routing options to Govrix Scout, plot candidate models on quality against latency and cost and pick from the Pareto front rather than the single top score.*
