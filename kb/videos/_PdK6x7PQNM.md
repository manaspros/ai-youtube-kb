# Data Quality Is the Compute Multiplier — Ari Morcos, DatologyAI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_PdK6x7PQNM` · [watch](https://youtu.be/_PdK6x7PQNM) · **date:** 2026-08-18 · **length:** 19:05 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Ari Morcos · **orgs:** Datology AI, Thomson Reuters, RCAI, Meta, Google, OpenAI, NeurIPS
- **topics:** data-engineering, training-finetuning-rl, models-research · **tags:** data-curation, pretraining-data, synthetic-data, rephrasing, mid-training, decontamination, scaling-laws, cross-lingual-transfer, compute-efficiency, domain-adaptation

> Ari Morcos (Datology AI) argues data quality is an under-used compute multiplier, showing curated-data gains in VLMs, multilingual and legal models, and a small-budget frontier-scale run.

## Summary
Ari Morcos, CEO of Datology AI, argues that with compute getting scarce and token use rising, the best lever is better training data. He frames data quality as a compute multiplier: a better data curve gives the same performance for far less compute, or better performance for the same compute. His core idea is to maximise the information each token and batch gives the model, and he says the right data depends on the target task, not on one universal dataset. He describes Datology's four steps (clean, curate, create, compose), with rephrasing of high-quality documents as the synthetic-data step. He shows results in VLMs (about 14 points gained from curation alone and about 45x less training compute to match a strong Qwen model), multilingual models (8% multilingual data, about 8x less compute than Qwen3), and a Thomson Reuters legal mid-training run. The talk ends with a customer's 17T-token open model trained for under $20M total, and the claim that domain models can be built for high six to seven figures. Most of the evidence is vendor-reported, with no methods detail, so treat the numbers as claims.

## Key ideas
- **Data quality is a compute multiplier** — Better data makes the learning curve steeper, so the same compute gives much better performance, or the same performance costs far less compute. The speaker says the x-axis can be data, compute, time or dollars. ([1:28](https://youtu.be/_PdK6x7PQNM?t=88))
- **Maximise signal per token and per batch** — The aim is to maximise the marginal information gain per data point. There is no single golden dataset; the best mix depends on the output tasks the model must do (e.g., legal data for a legal model). Diversity and mixing also matter, since narrow data makes models brittle to rephrasing. ([2:53](https://youtu.be/_PdK6x7PQNM?t=173))
- **Four-stage data pipeline: clean, curate, create, compose** — Clean uses heuristic filters and benchmark decontamination against downstream benchmarks. Curate uses quality classifiers, topic taxonomies, semantic redundancy removal, quality-based up/downsampling and task-distribution matching. Create uses synthetic rephrasing to expand data. Compose mixes and sequences data across at least three training phases. ([3:56](https://youtu.be/_PdK6x7PQNM?t=236))
- **Rephrase only the high-quality documents** — Rephrasing is framed as a fancy form of augmentation. Choosing which documents to rephrase matters a lot; a random pick gives poor results. Because the source facts stay in the document, the speaker says there is no model collapse and the rephrasing model needs only a simpler transform task. ([12:14](https://youtu.be/_PdK6x7PQNM?t=734))
- **Repeating high-quality data beats showing low-quality data** — The speaker says repeating high-quality data is almost always better than showing new low-quality data, up to some threshold. This is a token-scarcity argument. ([17:17](https://youtu.be/_PdK6x7PQNM?t=1037))
- **Domain mid-training keeps general skills when most data is representative** — In the Thomson Reuters case, 100B tokens of mid-training (under 1% of pretraining budget) raised LegalBench by about 5 points with no catastrophic forgetting. The majority of the mix matched the pretraining distribution, with only some domain data. Post-training gains then roughly tripled on the mid-trained model. ([14:37](https://youtu.be/_PdK6x7PQNM?t=877))
- **Cross-lingual transfer from English curation** — Curating only the English data improved non-English accuracy. The size of the transfer tracked how similar each language is to English. The effect also runs the other way, but is smaller. ([10:50](https://youtu.be/_PdK6x7PQNM?t=650))
- **Simulate token scarcity to predict large-run scaling** — The speaker says a model trained on the right data with simulated token scarcity follows a predictable scaling line. This lets a team de-risk a run with 50 to 100 times less compute before scaling up. The 17T-token Trinity Large run landed on the line of the two smaller models despite 50x more training compute. ([10:50](https://youtu.be/_PdK6x7PQNM?t=650))

## Techniques
- **Four-C data pipeline (clean, curate, create, compose)** — Heuristic filters and n-gram decontamination against downstream benchmarks first; then quality classifiers, topic taxonomy balancing, semantic redundancy removal, quality-weighted up/downsampling, and task-distribution matching; then synthetic rephrasing; then mixing and sequencing into at least three phases. *When:* When pretraining or continued training a model and compute is the bottleneck, or when building a domain model from mixed sources.
- **Selective synthetic rephrasing into many formats** — Pick the highest-quality source documents first, then rephrase each into many templates (e.g., true/false questions) so the facts all come from the source document. *When:* When you have a small, high-value proprietary corpus and need more diverse training data without generating new facts.
- **Domain mid-training with a representative mix** — Continue pretraining an open model on a mix that is mostly general pretraining-like data plus some domain data, then run post-training on the mid-trained model. *When:* When adapting a model to a specialised domain and general capability must not drop.
- **Small-run scaling check under token scarcity** — Train small models on curated data with the token budget constrained to match the target run, fit the scaling line, and predict the large run before committing compute. *When:* Before a costly large training run, to check whether the expected gains will appear.
- **Repeat high-quality data under token limits** — When new tokens are scarce, repeat the best data up to a threshold rather than adding low-quality data. *When:* When the token pool is limited and quality is uneven.

## Numbers
- Reasoning models use about 8x as many tokens as non-reasoning models, projected to grow about 5x again in the next year. ([0:12](https://youtu.be/_PdK6x7PQNM?t=12))
- H100 prices rose about 40% above their end-of-last-year lows. ([0:12](https://youtu.be/_PdK6x7PQNM?t=12))
- VLM trained on curated data (about 25B tokens, MAmmoTH mix) reaches about 14 absolute percentage points above its input dataset, with no post-training, and beats the public VLM Pareto frontier. ([6:52](https://youtu.be/_PdK6x7PQNM?t=412))
- VLM result roughly matches a Qwen 3.5 4B-class model with about 45x less training compute. ([6:52](https://youtu.be/_PdK6x7PQNM?t=412))
- Curated VLMs reach about 35x fewer FLOPs per correct answer than a Qwen 3.5-class model on the inference-efficiency plot. ([8:15](https://youtu.be/_PdK6x7PQNM?t=495))
- Multilingual model uses only 8% multilingual tokens (most languages at most about 6B tokens) and is slightly better than Qwen 3 with roughly 8x less compute. ([9:39](https://youtu.be/_PdK6x7PQNM?t=579))
- Trinity Large (17T tokens, hyper-sparse MoE) scaling was predicted from smaller runs despite 50x more training compute. ([10:50](https://youtu.be/_PdK6x7PQNM?t=650))
- Legal mid-training: 100B tokens (under 1% of pretraining budget) raised LegalBench about 5 points with no catastrophic forgetting. ([14:37](https://youtu.be/_PdK6x7PQNM?t=877))
- Post-training gain almost tripled on the mid-trained model versus the default instruction-tuned model (the speaker later says 2 to 3x). ([14:37](https://youtu.be/_PdK6x7PQNM?t=877))
- A fully open US-made model trained on 17T curated public tokens reached a competitive level with the open frontier for under $20M total cost, including R&D and salaries. ([17:17](https://youtu.be/_PdK6x7PQNM?t=1037))
- Speaker says a narrow domain model can be trained for high six figures to about $1M. ([17:17](https://youtu.be/_PdK6x7PQNM?t=1037))

## Hot takes
- Data quality is the single most under-leveraged compute multiplier.
- Frontier API access may be limited for outside users because inference capacity is short, not as a business choice.
- Customizing a model does not need hundreds of millions of dollars; a narrow domain model can be built for high six figures to about $1M.
- Repeating high-quality data is almost always better than adding low-quality data, up to a threshold.
- Post-training and pretraining should be treated as one connected pipeline, not three independent handoffs.

## Relevance to our work
- **general** (1/3): Relevant only to the recurring interest in data quality with LLMs; the reusable idea is 'rephrase only high-quality sources' for training or eval data. → *If you build LLM-generated eval or fine-tuning sets, test whether filtering source documents for quality before rephrasing beats random selection; the speaker's paper 'Beyond Neural Scaling Laws' is the cited starting point.*
