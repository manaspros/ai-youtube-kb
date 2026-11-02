# From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-561cZmir5Q` · [watch](https://youtu.be/-561cZmir5Q) · **date:** 2026-08-18 · **length:** 16:57 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Akram Baharlouei · **orgs:** Altos Labs, Human Cell Atlas
- **topics:** models-research, data-engineering, evals · **tags:** single-cell, foundation-models, scRNA-seq, scGPT, Geneformer, PrimeFlow, flow-matching, transformers, benchmarking, biology, data-quality, partial-reprogramming

> Altos Labs engineer on why single-cell foundation models (scGPT, Geneformer, PrimeFlow) struggle with noisy data, and why distribution-matching and data quality matter more than scale.

## Summary
Akram Baharlouei, an ML engineer at Altos Labs who describes herself as coming from outside biology, gives an engineering view of foundation models for single-cell biology. She motivates the field with Yamanaka factors and partial reprogramming, and with the slow, failure-heavy drug pipeline. She explains why single-cell RNA-seq is the modality most used for training, since the others are harder to measure or lower throughput. She argues the data is inherently noisy: identical cells do not read the same, measurements are snapshots of bursty processes, and labs and machines add technical variation. She describes transformer models that treat cells as sentences and genes as tokens, and says compressing cells into a latent vector loses information, so simple linear models sometimes match them. She reports that NeurIPS benchmarks she co-authored found these expensive models underperform compared with language and imaging transformers. She presents flow matching (PrimeFlow) as better at capturing the distribution of cell populations than autoencoders that predict the mean. Her conclusion is that data quality and realistic measurement matter as much as scale.

## Key ideas
- **Single-cell modelling is a route to cell rejuvenation and drug development, with partial reprogramming aiming to change cell age without changing cell type.** — Yamanaka's four transcription factors (2006) reprogrammed old skin cells toward a young state. The speaker says a first reprogramming medicine (OSK) is set to be tested in humans in 2026. ([1:08](https://youtu.be/-561cZmir5Q?t=68))
- **Drug development is slow and mostly fails, so cell-level models should help across the whole pipeline, not just early R&D.** — Acceptance rates are around 5% or lower and the pipeline can take up to 10 years and billions of dollars. She argues that speeding up only R&D saves little if later stages stay slow. ([3:57](https://youtu.be/-561cZmir5Q?t=237))
- **RNA sequencing is the modality used for most foundation-model training because it is easier to measure and scale.** — Protein measurement is hard and low throughput, and imaging gives shape and spatial position. The RNA data is a cell-by-gene matrix with about 20,000 genes. ([6:29](https://youtu.be/-561cZmir5Q?t=389))
- **Single-cell data is inherently noisy and heterogeneous, which limits what scale alone can buy.** — Identical cells give different readings. Each measurement is a snapshot of bursty biological processes, and labs and machines add technical variation. ([8:56](https://youtu.be/-561cZmir5Q?t=536))
- **Transformer models such as scGPT and Geneformer treat cells as sentences and genes as tokens, trained by masked-count prediction.** — Bidirectional attention models gene-gene relationships. Downstream tasks include cell-type prediction and perturbation response. ([10:15](https://youtu.be/-561cZmir5Q?t=615))
- **Compressing a cell into a latent vector discards information, so simple linear baselines sometimes match or beat the big models.** — The speaker treats this as a warning to check cheap baselines before assuming a large model is needed. ([11:37](https://youtu.be/-561cZmir5Q?t=697))
- **Flow matching learns the distribution of cell states, which captures population spread better than mean-predicting autoencoders.** — PrimeFlow starts from Gaussian noise and is shown matching ground-truth distributions. Autoencoder baselines mainly predict the mean. The comparison is scored with MMD. ([14:00](https://youtu.be/-561cZmir5Q?t=840))
- **Data quality and measurement realism matter as much as scale, and generalising to unseen data will need both.** — She says the field should improve how cells are measured so the data better reflects real organisms, not just add more of the same data. ([15:16](https://youtu.be/-561cZmir5Q?t=916))

## Techniques
- **Cell-as-sentence masked modelling** — Represent each cell as a sequence of genes with their expression counts, mask some counts, and train a bidirectional transformer to predict them. *When:* Pretraining on single-cell RNA-seq for downstream tasks like cell-type prediction or perturbation response.
- **Flow-matching distribution learning** — Learn a transport from Gaussian noise to the data distribution instead of compressing each sample into a latent vector and decoding a mean. *When:* When the output must reproduce population spread or multimodal variation, not a single average prediction.
- **Simple-baseline check before scaling** — Benchmark a linear or other simple model on the same task before accepting a large foundation model. *When:* Deciding whether an expensive model earns its training and serving cost.
- **Distributional scoring with MMD** — Compare predicted and ground-truth distributions with Maximum Mean Discrepancy rather than point error. *When:* Evaluating generative or distribution-predicting models on noisy measurements.

## Numbers
- Yamanaka's four transcription factors reprogrammed old skin cells to a young embryonic-stem-like state (2006); Nobel Prize in 2012. ([1:08](https://youtu.be/-561cZmir5Q?t=68))
- Drug development acceptance rate is around 5% or less. ([3:57](https://youtu.be/-561cZmir5Q?t=237))
- Drug development pipeline can take up to 10 years and cost billions. ([5:08](https://youtu.be/-561cZmir5Q?t=308))
- Single-cell RNA-seq datasets reach tens of millions of cells, with mentions of up to 500 million and a 1-billion-cell project. ([7:53](https://youtu.be/-561cZmir5Q?t=473))
- Gene expression profile per cell covers about 20,000 genes. ([6:29](https://youtu.be/-561cZmir5Q?t=389))

## Hot takes
- Expensive single-cell foundation models often do not beat simple linear baselines.
- Scaling single-cell data alone will not fix the field; measurement quality matters as much.
- Flow matching fits single-cell data better than autoregressive or autoencoder approaches that predict the mean.

## Tools mentioned
scGPT, Geneformer, PrimeFlow, MMD

## Relevance to our work
- **agentos** (1/3): The talk's lesson that a big learned model can lose to simple baselines applies to evaluating any learned component, such as the MemoryMesh or SkillForge evals, but the domain is not AgentOS. → *When adding a learned model to an AgentOS eval, always report a simple baseline next to it, and check whether the model beats it.*
