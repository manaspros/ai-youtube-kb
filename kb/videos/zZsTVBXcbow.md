# How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zZsTVBXcbow` · [watch](https://youtu.be/zZsTVBXcbow) · **date:** 2026-05-18 · **length:** 20:37 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Raia Hadsell · **orgs:** Google DeepMind, UK Met Office, US National Hurricane Center
- **topics:** models-research, rag-retrieval · **tags:** embeddings, multimodal, matryoshka, weather-forecasting, graphcast, gencast, world-models, genie, veo, gemma-4, frontier-research

> Raia Hadsell (VP Research, Google DeepMind) surveys non-LLM frontier work: unified multimodal embeddings, neural weather models (GraphCast, GenCast, FGN), and Genie world models.

## Summary
Raia Hadsell, VP of Research at Google DeepMind, gives a 20-minute overview of DeepMind research that is not based on language models. She covers Gemini Embeddings 2, a unified multimodal embedding model, and explains why embeddings are the companion to generative models for retrieval and comparison. She then walks through the weather line of work, from GraphCast to GenCast to the cyclone-focused FGN, which the US National Hurricane Center has reportedly used. The talk ends with the Genie world-model series, which she presents as interactive, memory-consistent, promptable environments. The content is high-level and demo-driven, with few implementation details, and it is mostly a showcase of results rather than engineering method.

## Key ideas
- **Embedding models are the companion to generative AI** — Retrieval and comparison need learned representations, not only generation. She frames this with the 'Jennifer Aniston cell' analogy: one concept activates the same neurons across modalities. The aim is a network that gives robust, modality-independent concept representations, trained with contrastive losses. ([6:19](https://youtu.be/zZsTVBXcbow?t=379))
- **One vector across modalities removes stitching steps** — Gemini Embeddings 2 is described as omnimodal and derived from Gemini. A single vector can cover text up to 8K tokens, 128 seconds of video, 80 seconds of audio, and a full PDF. The claimed benefit is no per-modality pipeline and no information lost when combining signals. ([7:32](https://youtu.be/zZsTVBXcbow?t=452))
- **Matryoshka embeddings allow a cheap first pass and a richer second pass** — MRL trains one network so that it works at several embedding sizes. Retrieval can start at 256 dimensions and then expand to a larger vector for more expressive matching. The same model serves a unified semantic space. ([8:53](https://youtu.be/zZsTVBXcbow?t=533))
- **Learned weather models became tractable because of the data archive** — She says the team found that neural prediction of the atmosphere is tractable, given about 40 years of global weather data. GraphCast uses a spherical graph neural network and predicts up to 15 days ahead, autoregressively, over about 100 atmospheric variables. ([9:52](https://youtu.be/zZsTVBXcbow?t=592))
- **Probabilistic forecasting matters for tails in chaotic systems** — GenCast is probabilistic and mesh-based. She argues that weather is fundamentally chaotic and that the extremes (tails) are what matter, which is why a probabilistic model was chosen over a point forecast. ([12:33](https://youtu.be/zZsTVBXcbow?t=753))
- **Train the task output directly instead of bolting on a post-processor** — FGN predicts cyclones directly, with categorization, trajectory, wind speed and eye formation built into the network. Previously a detector was added after the weather forecast. Training for the target itself is presented as the reason for better results. ([13:33](https://youtu.be/zZsTVBXcbow?t=813))
- **World models from a scale-up path, with memory and live prompting** — The Genie line goes from Genie 1 (2D platformer, a few seconds) to Genie 2 (3D, not real-time) to Genie 3. Genie 3 is shown to keep spatial memory across a minute of movement and to change the world while the user is inside it. She treats this as a new interactive, adversarially promptable form of entertainment and education. ([14:34](https://youtu.be/zZsTVBXcbow?t=874))

## Techniques
- **Unified multimodal embedding** — Use one encoder that maps text, PDFs, audio and video into a single vector space, so retrieval does not need separate per-modality mapping steps. *When:* Retrieval over mixed-media corpora where cross-modal matching is needed and info loss from fusion is a concern.
- **Matryoshka (MRL) dimension scaling** — Train one embedding network so that prefixes of the vector are useful. Run a fast search at a small size (e.g. 256 dims), then use the larger size to refine. *When:* When retrieval latency or memory must be cut without retraining separate models for each size.
- **Probabilistic forecasting for tail events** — Model the output as a distribution rather than a single trajectory, so that rare extreme outcomes are represented. *When:* Chaotic or high-impact prediction tasks where the tails are the decision-relevant part.
- **Train for the end target, not a post-hoc detector** — Make the network output the high-level event (e.g. cyclone category, track, wind speed) directly and train on that objective, rather than running a separate detector on the forecast. *When:* When a downstream structured output can be defined and labelled, and error compounds through a post-processing step.
- **Memory consistency test for world models** — Move away from a start point for about a minute, return, and check whether the scene matches the start exactly. *When:* Evaluating whether an interactive generated environment keeps state over time.

## Numbers
- Gemini Embeddings 2 single-vector input limits: text up to 8,000 tokens, 128 seconds of video, 80 seconds of audio, full PDF ([7:32](https://youtu.be/zZsTVBXcbow?t=452))
- DeepMind group she leads: about 1,200 scientists and engineers across 10 labs ([2:20](https://youtu.be/zZsTVBXcbow?t=140))
- Weather training data: about 40 years of global weather data ([9:52](https://youtu.be/zZsTVBXcbow?t=592))
- GraphCast: 15-day global forecast, autoregressive, about 100 atmospheric variables ([11:19](https://youtu.be/zZsTVBXcbow?t=679))
- Hurricane Lee landfall prediction: accurate 9 days out for the GNN, versus 6 days for the best physics-based models ([11:19](https://youtu.be/zZsTVBXcbow?t=679))
- GenCast: more accurate than 1,300 gold-standard benchmarked forecasts 97% of the time ([12:33](https://youtu.be/zZsTVBXcbow?t=753))
- GenCast 15-day forecast takes 8 minutes on a single chip, versus a very large supercomputer for the earlier model ([12:33](https://youtu.be/zZsTVBXcbow?t=753))

## Hot takes
- Embeddings are a critical companion to generative AI, not an afterthought, and get less attention than language models.
- Weather forecasting is fundamentally chaotic, so probabilistic models are needed to capture the tails.
- Adversarially prompting a live world model could become a new form of gaming and entertainment, and useful for education.
- Going after root-node problems rather than leaf-node problems is how DeepMind chooses research.

## Tools mentioned
Gemini Embeddings 2, GraphCast, GenCast, FGN (Functional Generative Network), Genie 1, Genie 2, Genie 3, Veo 3, Gemma 4

## Relevance to our work
- **agentos** (1/3): MemoryMesh hybrid retrieval (BM25 + pgvector) could use a Matryoshka-style multi-size embedding scheme, but the talk gives no benchmarks for retrieval quality or latency and the model is closed. → *Check whether the embedding model used for MemoryMesh supports truncatable dimensions, and benchmark a 256-dim first-pass plus full-dim rerank against the current pgvector recall and latency.*
- **general** (1/3): Contrastive-embedding framing (Siamese and contrastive losses) and single-vector matching are close to entity-resolution candidate matching, but no ER-specific results are presented. → *When next reviewing entity-resolution candidate generation, test whether a unified embedding over name plus attribute text gives better candidate recall than current rules, using the MRL idea of a cheap first pass.*
