# Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jebp4V0vh30` · [watch](https://youtu.be/jebp4V0vh30) · **date:** 2026-09-18 · **length:** 20:43 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Carlos Sanchez · **orgs:** Adobe, Cerebras, Google, Cloudflare, Promptfoo, AWS Bedrock
- **topics:** evals, inference-serving, rag-retrieval, product-ux · **tags:** personalization, edge-delivery, promptfoo, cerebras, latency, grounded-generation, persona-bucketing, adobe-experience-manager, demo

> Adobe's Carlos Sanchez demos "agentic sites" that personalize page blocks in real time from browsing intent, grounded on the existing site, with provider choice driven by latency and accuracy evals.

## Summary
Carlos Sanchez from Adobe (Experience Manager) demos a system that rebuilds parts of a website in real time from what a visitor is doing on it. Signals such as pages visited and time per page are bucketed into intent or persona groups and fed to an LLM. The LLM then selects or rewrites blocks like hero cards, product lists, blog feeds and navigation. Only sections are generated, and the generation is grounded on the site's own content so brand guidelines hold. The backend runs continuous Promptfoo evals across models and providers, scoring accuracy and speed, because the right choice depends on the site. Speed is treated as a product constraint, with a target of roughly 1 to 2 seconds per page. The speaker reports Cerebras-hosted Gemma 4 at about 1.1 s average versus 4.6 s for another provider on a 15-prompt set, and a live demo with about 2,200 to 2,300 tokens per second. He notes that small models are enough for layout decisions. He also covers pre-generated "For You" pages with prefetch, a tool that builds a demo agentic site from a URL in under an hour, and a speculative vision of intent-driven pages delivered by voice to a TV. The talk is mostly a live demo, with some vendor promotion.

## Key ideas
- **Personalize by intent, in real time** — Browsing signals (pages visited, time per page, visitor bucket such as 'exploring') are sent to an LLM that rebuilds parts of the page for the current visitor. The goal is more engagement or conversion. ([1:09](https://youtu.be/jebp4V0vh30?t=69))
- **Regenerate blocks, not whole sites** — Only specific blocks or sections change. The LLM's context is a corpus built from the existing site, so output stays grounded and on brand, which marketers require. He says hallucinated full-site generation is not acceptable to them. ([2:33](https://youtu.be/jebp4V0vh30?t=153))
- **Model and provider choice is site-specific** — Accuracy and speed vary by site size, vertical and commerce type. The speaker runs prompts continuously across many models and providers with Promptfoo rather than picking one model once. ([4:56](https://youtu.be/jebp4V0vh30?t=296))
- **Latency is a hard product budget** — Page generation should stay under about 1 to 2 seconds, because faster pages convert better. Fast-but-good-enough beats slightly better but slow. ([6:15](https://youtu.be/jebp4V0vh30?t=375))
- **A small model is enough for layout decisions** — Choosing blocks and ordering a page is light text work. He argues you do not need a large LLM for this, which makes speed and cost easier to reach. ([7:15](https://youtu.be/jebp4V0vh30?t=435))
- **Pre-generate where latency is not critical** — A 'For You' page can be generated ahead of time from accumulated signals and prefetched when the visitor navigates. This trades cost (repeated LLM calls on each update) against speed. ([8:44](https://youtu.be/jebp4V0vh30?t=524))
- **Marketers set strategy in natural language** — Marketing teams define personas, groups and goals in plain language. Analytics then close the loop by feeding results back into the personalization. ([3:56](https://youtu.be/jebp4V0vh30?t=236))

## Techniques
- **Multi-provider eval matrix for accuracy and latency** — Keep a prompt set per site (the demo used 15 prompts). Run it across many models and providers with Promptfoo. Record accuracy and average generation latency for each, then pick the fastest model that is good enough. *When:* When a model choice is driven by a workload with a tight latency budget and the right answer varies by domain.
- **Grounded block-level generation** — Build a retrieval corpus from the whole existing site. Ask the LLM to choose or assemble existing blocks and copy only from that corpus. Limit it to sections, never the full page. *When:* When brand or compliance rules forbid invented content, but per-visitor variation is still wanted.
- **Signal bucketing into personas or intents** — Group visitors by browsing signals into a small set of intent classes (for example exploring, buying). Generate once per class, not once per visitor, to cut LLM calls. *When:* When per-visitor generation is too costly or slow, but segment-level personalization is enough.
- **Pre-generate and prefetch** — Generate personalized pages (for example a recommendations page) in the background as signals arrive. Prefetch when the visitor is likely to navigate there. Re-generate as signals change. *When:* When the page is not needed instantly and you can predict the next navigation.
- **Fast inference provider for the hot path** — Send the latency-critical generation step to a high-throughput inference provider (the demo used Cerebras). Keep other providers as fallbacks and for less time-sensitive jobs. *When:* When time-to-first-page is the metric and a smaller model is acceptable.

## Numbers
- Average page generation latency of about 1.1 s on Cerebras-hosted Gemma 4 (announced the week before), vs 4.6 s on another provider, across a 15-prompt eval set ([6:15](https://youtu.be/jebp4V0vh30?t=375))
- Target: site generation under about 1 to 2 seconds per page; speaker cites that faster sites convert better ([6:15](https://youtu.be/jebp4V0vh30?t=375))
- Live demo: LLM step about 1 s; throughput about 2,200 to 2,300 tokens per second on Cerebras Gemma 4. Total page time was shown as '164 seconds' in captions, which is probably 1.64 s ([15:11](https://youtu.be/jebp4V0vh30?t=911))
- A demo agentic site can be built from any URL in less than an hour (the 'Of One Labs' tool) ([16:40](https://youtu.be/jebp4V0vh30?t=1000))

## Hot takes
- The web may not be the main interface; personalized generated answers could be delivered by voice to a TV without a phone or PC.
- Most page-personalization decisions do not need a large LLM; a fast small model is enough.
- Costs and latency for LLM-generated pages will keep falling, so this will be practical soon.

## Tools mentioned
Adobe Experience Manager, Edge Delivery Services, Cerebras, Gemma 4, Promptfoo, AWS Bedrock, Cloudflare, Google Cloud

## Relevance to our work
- **agentos** (1/3): The talk compares providers on latency and accuracy for one workload. This is relevant to InferCraft and the routing side of Govrix Scout, but the content is about marketing sites, not infrastructure. → *Run a small Promptfoo-style matrix of accuracy and p95 latency across providers for one AgentOS routing workload before setting strategy-routing defaults.*
- **general** (1/3): The point that small, fast models suffice for simple structured decisions supports cheap-model (Haiku) pipelines, but the talk gives no evidence beyond the demo. → *Test whether a Haiku-class model meets accuracy for one simple structured classification step in the entity-resolution pipeline before using a larger model.*
