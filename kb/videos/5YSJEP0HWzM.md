# Personalization in the Era of LLMs - Shivam Verma, Spotify

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `5YSJEP0HWzM` · [watch](https://youtu.be/5YSJEP0HWzM) · **date:** 2026-06-18 · **length:** 20:12 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Shivam Verma · **orgs:** Spotify
- **topics:** training-finetuning-rl, context-engineering, enterprise-adoption · **tags:** semantic-ids, recommender-systems, user-embeddings, soft-tokens, generative-recommendation, domain-adaptation, taste-profile, catastrophic-forgetting, open-weight-llms

> Spotify's AI Foundation tech lead explains how it personalizes recommendations with user embeddings, semantic IDs for catalog items, and soft user tokens fed into a fine-tuned open-weight LLM.

## Summary
Shivam Verma, tech lead of the user representations team at Spotify's AI Foundation org, describes how Spotify is moving from siloed multi-stage recommenders to a single generative recommender built on an LLM backbone. He covers three parts: user modeling (sequence-based user embeddings generated daily for over a billion users), catalog understanding (semantic IDs that compress item vectors into about four to six hierarchical tokens), and steerability (a user's editable text profile fed back into the model). The key technique is projecting a user's embedding into the LLM's input space as a soft token, so one shared model can personalize per user without training on every user's data. He says the next-episode recommendation work is in production with positive internal metrics, but gives no lift numbers. The Taste Profile product is live in a few markets. This is a practitioner overview with little method detail, and parts of it are company promotion.

## Key ideas
- **Spotify is moving from many per-product recommenders to one unified generative model** — Traditional recsys ran candidate generation (millions to a few hundred items) followed by one or more rankers, with each product team owning its own model. The direction is a single model with an LLM-like backbone that users can steer in natural language. ([5:56](https://youtu.be/5YSJEP0HWzM?t=356))
- **User embeddings are now a sequential model over interaction history, not a generic compressor** — The earlier approach was an autoencoder that compressed user features into a small vector. The newer approach uses a transformer where the user's interaction history sits in the prompt as context, together with the request context, query, product surface and candidate item. ([7:19](https://youtu.be/5YSJEP0HWzM?t=439))
- **Semantic IDs let an LLM generate catalog items one token at a time** — A roughly 1,000-dimensional item vector is quantized into about four to six hierarchical tokens. Related items share leading tokens (the speaker's example: two pop artists share their first two tokens), and the tail tokens encode finer niches. The LLM then autoregressively predicts the next track or episode. ([13:28](https://youtu.be/5YSJEP0HWzM?t=808))
- **Domain adaptation is continued pretraining or SFT on tokenized listening histories** — The open-weight LLM is trained on sequences where items appear as semantic IDs. The prompt holds a user's tokenized listening history plus the current item, converted from a Spotify URI to its semantic ID, and the target is the next item. ([14:41](https://youtu.be/5YSJEP0HWzM?t=881))
- **A soft user token gives per-user personalization without training on every user** — The user representation is projected into the LLM's embedding space and inserted into the prompt as a soft token. The token changes with each user, so one shared model can personalize its response. The speaker says this is needed because training data cannot cover 750M+ users. ([17:22](https://youtu.be/5YSJEP0HWzM?t=1042))
- **Fine-tuned LLMs bring world knowledge, explainability and steerability, with a forgetting cost** — Combining Spotify's interaction knowledge with open-weight LLM world knowledge gives steerability and explanations. The trade-off is catastrophic forgetting, which the speaker says has been manageable in practice. ([12:08](https://youtu.be/5YSJEP0HWzM?t=728))
- **An editable taste profile feeds user corrections back into the generative model** — The Taste Profile product shows users a text description of who they are. Users can chat to add or remove taste, and those edits flow back into the model. This is the steerability piece of the design. ([18:43](https://youtu.be/5YSJEP0HWzM?t=1123))

## Techniques
- **Semantic ID tokenization of item embeddings** — Quantize each item's embedding into about 4-6 hierarchical discrete tokens, so similar items share prefixes. Use those tokens as the vocabulary when training the LLM. *When:* When an LLM must autoregressively generate items from a large catalog and raw IDs or long vectors do not fit the token-prediction setup.
- **Soft user token injection** — Project a user representation vector into the LLM's input embedding space and insert it into the prompt as one soft token, recomputed for each user. *When:* When you want personalization inside a shared LLM without fine-tuning per user or training on every user's data.
- **Tokenized listening-history prompting for domain adaptation** — Format the user's history and the target item as semantic-ID tokens, then train the LLM to predict the next item. *When:* When adapting an open-weight LLM to a proprietary behavioural catalog for next-item recommendation.
- **Daily batch user-embedding generation** — Recompute user embeddings for the full active base every day as a large pipeline, then feed them to downstream models. *When:* When many downstream recommenders need a shared, up-to-date user representation at a scale of a billion users.
- **User-editable text profile as a steering signal** — Show users a text summary of their taste, let them edit it by chat or message, and feed the edits into the generative model. *When:* When you want users to control personalization directly and the model needs corrections without retraining.

## Numbers
- About 750 million monthly active users ([2:26](https://youtu.be/5YSJEP0HWzM?t=146))
- Catalog of over 100 million tracks, millions of podcasts, roughly 400,000 audiobooks, and growing video episodes ([2:26](https://youtu.be/5YSJEP0HWzM?t=146))
- Available in about 184 markets ([3:21](https://youtu.be/5YSJEP0HWzM?t=201))
- User embeddings generated every day for over a billion users, including inactive users ([7:19](https://youtu.be/5YSJEP0HWzM?t=439))
- Semantic IDs compress a roughly 1,000-dimensional item vector into about 4-6 tokens ([13:28](https://youtu.be/5YSJEP0HWzM?t=808))
- Discover Weekly has been around since about 2015 ([3:21](https://youtu.be/5YSJEP0HWzM?t=201))

## Hot takes
- The speaker says recommenders are moving away from siloed per-product models toward a single generative model with an LLM backbone.
- The speaker says that using an LLM for recommendations gives explainability and steerability almost for free, with catastrophic forgetting as the main cost.
- The speaker claims a soft user token can personalize a shared LLM better than the usual approach, and says the next-episode model is already in production.

## Tools mentioned
Llama, Qwen

## Relevance to our work
- **agentos** (1/3): The talk is about per-user state that is compressed into a vector and inserted into a shared model. That relates loosely to MemoryMesh's cross-session memory, but the domain is recommendation, not agent memory. → *Read the soft-token idea as a possible alternative to replaying full history in MemoryMesh: compare a learned per-user vector injected as one prompt token against raw retrieval for cross-session personalization.*
