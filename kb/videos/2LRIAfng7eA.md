# Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `2LRIAfng7eA` · [watch](https://youtu.be/2LRIAfng7eA) · **date:** 2026-09-27 · **length:** 19:40 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Yves Raimond, Jacqueline Wood · **orgs:** Spotify
- **topics:** training-finetuning-rl, evals, product-ux · **tags:** semantic-ids, generative-recommendation, LLM-as-judge, domain-grounding, catastrophic-forgetting, constrained-decoding, beam-search, Cranfield-evaluation, Qwen, LoRA, personalization, Spotify

> Spotify's engineers explain turning recommendations into a steerable LLM: semantic-ID tokens, a four-stage NEO training recipe, and LLM judges grounded in behavioral data.

## Summary
Yves Raimond and Jacqueline Wood of Spotify describe moving from ranking-based recommendations to "generative personalization," where users steer and query the system in natural language. They say one model, the "large-taste model," handles recommendation, reasoning, explanation and generation, and that about one in four US premium subscribers use it daily. Jacqueline then explains the training method: content embeddings are quantized into discrete semantic-ID tokens that are added to an open-weight LLM's vocabulary, and a four-stage recipe (semantic foundation, frozen-backbone domain grounding, multi-task capability induction, optional RL post-training) is used. Their ablations show the frozen backbone preserves language ability that continued pretraining destroys, and that beam search beats top-piece sampling for accuracy. The second half covers evaluation: offline engagement metrics cannot judge explanation quality, so they ground LLM judges in user profiles and behavioral signals, reporting 75% alignment with humans and a 0.87 agreement with human rankings for Cranfield-style pools. Most numbers are Spotify-internal and the talk gives few implementation details beyond the linked papers.

## Key ideas
- **Recommendation is shifting from guessing (ranked lists) to reasoning, and from black-box ranking to steerable, language-controlled personalization.** — Users can steer the DJ mid-session, write prompted playlists, and edit a natural-language taste profile. The system is built to explain and generate experiences, not only rank. ([2:25](https://youtu.be/2LRIAfng7eA?t=145))
- **One unified model (the 'large-taste model') covers prediction, reasoning, steering and generation across Spotify surfaces.** — The speaker says it understands every historical interaction with every item, and that about one in four US premium subscribers use it daily. Deploying it on existing surfaces (autoplay, podcast discovery, DJ messages) produced gains. ([6:23](https://youtu.be/2LRIAfng7eA?t=383))
- **Catalog items become semantic-ID tokens that are added to an open-weight LLM's vocabulary.** — Existing content embeddings (e.g. podcast episode embeddings) are quantized into discrete tokens. The LLM is then fine-tuned so it reads both natural language and these catalog tokens, so one prompt can mix listening history with text. ([7:42](https://youtu.be/2LRIAfng7eA?t=462))
- **The NEO training recipe freezes the backbone at the grounding stage so the new tokens are learned without erasing language ability.** — Stage 2 trains only the semantic-ID embeddings with a bidirectional text-to-ID and ID-to-text mapping. Stage 3 unfreezes everything for multi-task instruction tuning (full fine-tuning or LoRA). Stage 4 is optional RL post-training. ([10:01](https://youtu.be/2LRIAfng7eA?t=601))
- **Continued pretraining on catalog data erases the base model's natural-language and world knowledge, while frozen-backbone grounding keeps it.** — Task performance barely changes with continued pretraining, but natural-language and world-knowledge ability drops to essentially zero. The effect was checked on Qwen and LLaMA, so the speaker attributes it to the training paradigm rather than one backbone. ([13:17](https://youtu.be/2LRIAfng7eA?t=797))
- **Multi-task training matched or beat single-task models, and helped cold-start content such as audiobooks.** — Podcast recommendation data helped the newer audiobook recommendation task, which is the speaker's example of cross-task transfer for cold-start items. ([11:58](https://youtu.be/2LRIAfng7eA?t=718))
- **Offline engagement metrics cannot judge whether a generated recommendation or explanation makes sense, so LLM judges must be grounded in data.** — Grounding means passing a textual user profile built from listening history, or similar queries and their past user interactions, to the judge. Overall alignment rose 5%, and on ambiguous queries it rose 91%. ([15:45](https://youtu.be/2LRIAfng7eA?t=945))
- **Grounded LLM judges can replace expensive human ranking stages when building relevance collections.** — Candidate pools from several sources are ranked by the grounded judge instead of only by humans. The speaker reports 0.87 agreement with human system rankings. ([18:12](https://youtu.be/2LRIAfng7eA?t=1092))

## Techniques
- **Semantic-ID tokenization and vocabulary extension** — Quantize existing item embeddings into discrete tokens, add them as special tokens to an open-weight LLM's vocabulary, then fine-tune on both text and ID tokens. *When:* When an LLM must reason over a large catalog of items with IDs and natural language in the same prompt.
- **Frozen-backbone domain grounding** — Freeze all original LLM weights and train only the new ID embeddings with a bidirectional text-to-ID and ID-to-text objective. *When:* When adding new tokens to a pretrained LLM and you need to keep its core language and world knowledge.
- **Staged training: grounding, then multi-task instruction tuning, then optional RL** — Stage 2 aligns the new embeddings. Stage 3 unfreezes the model for multi-task instruction tuning with full fine-tuning or LoRA over several recommendation tasks. Stage 4 adds post-training such as RL. *When:* When one model must serve several tasks (retrieval, next-item recommendation, explanation) and the base model must stay general.
- **Beam search over constrained decoding for ID generation** — Decode semantic IDs with beam search. Constrained decoding can be turned on to restrict output to a subset, such as new content only. Top-piece sampling was clearly less accurate. *When:* When generated IDs must be valid catalog items and accuracy matters more than a small latency cost.
- **Grounding LLM judges with user profiles and behavioral signals** — Give the judge a text summary of the user's history, or the past interactions of similar queries, so it can judge fit with the user's intent instead of only the item. *When:* When offline engagement metrics miss recommendation quality or explanation accuracy, especially for ambiguous queries.
- **LLM judges for Cranfield-style relevance pools** — Build a candidate pool from several sources and have a grounded LLM judge rank it, replacing most human ranking work. Validate the judge against human rankings (agreement reported as 0.87). *When:* When labeled relevance sets are needed at scale and human ranking is too expensive.

## Numbers
- About 760 million monthly active users in about 184 markets ([0:08](https://youtu.be/2LRIAfng7eA?t=8))
- Catalog of more than 100 million music tracks, plus video, podcasts and audiobooks ([1:17](https://youtu.be/2LRIAfng7eA?t=77))
- About 10 billion playlists ([2:25](https://youtu.be/2LRIAfng7eA?t=145))
- About one in four US premium subscribers interact with the large-taste model daily ([6:23](https://youtu.be/2LRIAfng7eA?t=383))
- Valid semantic IDs generated 98% of the time without constrained decoding ([13:17](https://youtu.be/2LRIAfng7eA?t=797))
- Continued pretraining drops the backbone's natural-language and world-knowledge ability to essentially zero ([13:17](https://youtu.be/2LRIAfng7eA?t=797))
- Grounded LLM judge alignment with human preferences: 75% (textual user profile grounding) ([16:46](https://youtu.be/2LRIAfng7eA?t=1006))
- Behavioral-signal grounding raised judge alignment by 5% overall and by 91% on ambiguous queries ([16:46](https://youtu.be/2LRIAfng7eA?t=1006))
- Grounded LLM judge agreement with human system rankings: 0.87 ([18:12](https://youtu.be/2LRIAfng7eA?t=1092))

## Hot takes
- Generative personalization (steerable, language-based experiences) is the next phase, replacing ranked-list recommendation.
- Offline engagement metrics are not sufficient for generative or explanatory recommendations; LLM judges need grounding in user data to be trusted.
- Freezing the backbone while adding new tokens beats continued pretraining, which wipes out general language ability.

## Tools mentioned
Qwen, LLaMA, LoRA, NEO (Spotify's training paradigm, linked paper), Discover Weekly, Spotify DJ

## Relevance to our work
- **general** (2/3): Concrete, reusable evaluation practice: grounding LLM judges in per-user context, and the ablation method for freezing the backbone while adding new tokens. Relevant to the team's recurring interest in evals for agents. → *Read the linked NEO paper and the Spotify grounded-judge paper for the exact judge prompts and the alignment-measurement setup.*
- **agentos** (1/3): The grounded LLM-judge method (user profile and similar-query behavioral signals) could sharpen the RAGAS-style evals planned for the MemoryMesh layer, though the talk is about recommendation, not retrieval QA. → *Add a grounded-judge variant to the MemoryMesh RAGAS evals: give the judge a per-user memory summary and check whether its agreement with human labels improves on ambiguous queries.*
