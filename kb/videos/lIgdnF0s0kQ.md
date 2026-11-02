# Why LLM Recommenders Will Be AI's Biggest Consumer App — Devansh Tandon, Meta

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `lIgdnF0s0kQ` · [watch](https://youtu.be/lIgdnF0s0kQ) · **date:** 2026-09-27 · **length:** 18:01 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Devansh Tandon · **orgs:** Meta, Google, YouTube, DeepMind, Instagram, Spotify, DoorDash
- **topics:** models-research, product-ux, infra-cost-scaling · **tags:** recommender-systems, semantic-ids, scaling-laws, generative-retrieval, llm-recommender, token-economics, consumer-ai, chain-of-thought-ranking

> Devansh Tandon (Meta) argues recommenders scale like LLMs, lays out four recommender S-curves, gives a three-step recipe for LLM recommenders built on semantic IDs, and claims feeds are far more token-efficient than chat apps.

## Summary
The speaker argues that recommendation models follow the same power-law scaling behaviour as LLMs and that the field is early on that curve. He describes a flywheel where inference tokens drive engagement, which drives monetization and pays for the next training run. He splits the industry into four paradigms: traditional feature-engineered models, LLM-inspired end-to-end models, LLM-native models built on a base model, and agentic loops that plan, retrieve, rank and critique. His recipe has three steps: tokenize content into semantic IDs, adapt an LLM to read both English and those IDs, then post-train for ranking with chain-of-thought and optionally fine-tune per surface. He presents steerable, explainable recommenders as a new consumer product surface. He ends by arguing that content feeds are structurally cheaper per hour of engagement than AI chat apps, because they output pointers to existing content rather than generating tokens. Most numbers are his own or come from Meta earnings remarks, and several are unverified.

## Key ideas
- **Recommenders show the same power-law scaling as LLMs** — Loss falls log-linearly with model size, data and compute. The speaker says recsys models are among the largest production ML models and that offline gains (NE, AUC) translate into engagement and revenue. He cites HSTU (2024) and a follow-up as evidence. ([0:08](https://youtu.be/lIgdnF0s0kQ?t=8))
- **Tokens in, engagement out flywheel** — Train, then run inference (tokens in), which improves recommendations, which drives engagement and time spent, which becomes monetization that pays for the next training run. Each step up the scaling curve is one turn of this loop. He uses it as a lens to evaluate any consumer app. ([5:00](https://youtu.be/lIgdnF0s0kQ?t=300))
- **Four recommender S-curves run in parallel** — (1) Traditional two-tower and sparse rankers, where agents will increasingly do feature engineering. (2) LLM-inspired end-to-end models (HSTU), where most leading systems sit today. (3) LLM-native models that adapt a base LLM for recommendation (Tiger, Plum). (4) Agentic loops where an LLM plans, retrieves, ranks, critiques and refines. ([6:23](https://youtu.be/lIgdnF0s0kQ?t=383))
- **Three-step recipe: tokenize, bilingualize, steer** — First create a domain token language by tokenizing the content corpus. Then adapt an LLM so it understands English and that language. Then prompt it with user information so it decodes recommendations straight from the corpus. The model is a five-layer stack: semantic IDs, base model, pre-training, post-training, light surface fine-tuning. ([7:23](https://youtu.be/lIgdnF0s0kQ?t=443))
- **Semantic IDs give stable tokens and compression** — A semantic ID replaces a shifting hash ID with a stable code, and similar items share prefixes. It also compresses content: the speaker says a three-minute video of about 10,000 tokens can be reduced to about 10 semantic tokens, so long user histories fit in a context window. ([9:56](https://youtu.be/lIgdnF0s0kQ?t=596))
- **Post-training for reranking with visible reasoning** — The model reranks about 30 candidate videos down to 5 and writes a chain of thought that names the user's interests and creator affinities. Because the model reads both English and recommendation tokens, its decisions can be inspected. ([11:18](https://youtu.be/lIgdnF0s0kQ?t=678))
- **Steerable recommenders as a new product surface** — Users can see what the model thinks their interests are, then add or remove interests in natural language. The example is adding a FIFA World Cup interest and getting personalized clips. The speaker expects more control, explanations and interactive playlists or feeds. ([12:18](https://youtu.be/lIgdnF0s0kQ?t=738))
- **Feeds are structurally more token-efficient than chat** — Feeds run roughly 1-10B active parameters and output semantic-ID pointers to creator-uploaded content. Chat apps run 10-100B active parameters and generate every output token, often a few thousand per turn. The speaker says feeds are up to 100x cheaper per hour of engagement. ([15:10](https://youtu.be/lIgdnF0s0kQ?t=910))

## Techniques
- **Semantic ID tokenization of content** — Map each content item to a short sequence of codes (about 10 tokens for a video) that share prefixes for similar items. Use these codes in place of hash IDs in models and as the vocabulary the LLM learns. *When:* When item IDs churn or hash embeddings only memorize, or when user histories are too long to fit in context at raw token cost.
- **Bilingual LLM pre-training on semantic IDs** — Train on prompts that pair semantic-ID sequences with English descriptions, and on masked-sequence prediction over watch histories, so the model links the two vocabularies. *When:* When adapting a base LLM to a domain with its own item vocabulary and you need it to reason over that vocabulary in natural language.
- **Post-training LLM rerankers with chain of thought** — Give the model user context plus a candidate set (about 30 items) and train it to output the top few with reasoning about interests and affinities. *When:* When you need an explainable ranker, or a ranker that can be steered by natural-language instructions.
- **Shared base model with thin per-surface fine-tuning** — Put most compute into one shared model (semantic IDs, pre-training, post-training), then do light fine-tuning for each product surface. *When:* When many surfaces share one content corpus and you want to avoid training a model from scratch for each.
- **Agentic recommendation loop** — Let an LLM plan, call retrieval and ranking models, critique the candidate list, then refine and call the models again before returning results. *When:* Speculative: the speaker describes it as active research, not production practice.

## Numbers
- Instagram Reels watch time up 30% year over year in a quarter, per Meta earnings remarks the speaker cites; the gains are attributed partly to a simpler ranking architecture and to doubling the length of user interaction sequences used for training. ([3:57](https://youtu.be/lIgdnF0s0kQ?t=237))
- A three-minute Instagram Reel is about 10,000 raw tokens; semantic IDs compress it to about 10 tokens. ([9:56](https://youtu.be/lIgdnF0s0kQ?t=596))
- Content-feed models run about 1-10B active parameters; AI chat apps serve about 10-100B active parameters. ([15:10](https://youtu.be/lIgdnF0s0kQ?t=910))
- Content feeds are up to 100x or more cheaper than AI chat apps per hour of consumer engagement (speaker's estimate, not independently verified). ([15:10](https://youtu.be/lIgdnF0s0kQ?t=910))
- A chat turn outputs a few thousand tokens, all generated at inference time, whereas a feed outputs semantic-ID pointers to existing content. ([15:10](https://youtu.be/lIgdnF0s0kQ?t=910))
- Four of the top 10 apps by daily active users are content feeds. ([16:33](https://youtu.be/lIgdnF0s0kQ?t=993))
- Reranker example: about 30 candidate videos are reranked to a top 5. ([11:18](https://youtu.be/lIgdnF0s0kQ?t=678))

## Hot takes
- LLM recommenders will be one of the biggest consumer AI applications.
- Feeds are up to 100x cheaper per engagement hour than AI chat apps, so they are the more token-efficient consumer AI product.
- Agentic recommendation loops (plan, retrieve, rank, critique) will be the next S-curve, in parallel to coding-agent harnesses.

## Tools mentioned
Semantic IDs, HSTU, Tiger, Plum, Gemini, Claude Code, Codex

## Relevance to our work
- **agentos** (1/3): The token-cost argument (pointers versus generated tokens) and semantic-ID compression of long histories touch the L2A MemoryMesh context-budget question, but the talk gives no retrieval or memory design. → *Read the Tiger and Plum papers the speaker cites for how semantic-ID compression is handled before deciding whether MemoryMesh should compress long user histories.*
- **prosharness** (1/3): The plan, retrieve, rank, critique loop mirrors ProsHarness's plan, then critique, then debate flow, but the talk does not give a verification method. → *Compare the speaker's agentic loop (plan, retrieve, rank, critique, refine) against the ProsHarness plan, critique and debate stages and note where a critique step gates the next call.*
- **general** (1/3): Useful as a case study of semantic-ID tokenization, which may apply to entity resolution where stable item codes replace shifting IDs, but the talk does not cover entity resolution. → *Skim the speaker's semantic-ID and generative-retrieval papers and check whether stable learned codes beat hashed keys for entity-resolution candidates.*
