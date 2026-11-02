# Apple Won the AI Race

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Ba3xunEk8Y8` · [watch](https://youtu.be/Ba3xunEk8Y8) · **date:** 2026-10-02 · **length:** 7:20 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Apple, Google, Anthropic, OpenAI, xAI, Cursor, Better Stack
- **topics:** models-research, local-ai, product-ux · **tags:** apple-intelligence, siri, on-device-ai, distillation, mixture-of-experts, private-cloud-compute, platform-strategy, ai-race

> Better Stack argues Apple can win the AI race through distribution, device data and an on-device model that is good enough, not frontier model quality. Mostly speculative commentary with few verifiable facts.

## Summary
The Better Stack host argues that Apple, despite lagging on models, is well placed to win the AI race because no frontier lab keeps a lead for long and the competition is shifting to the surrounding stack. He says Apple's new Siri uses five Apple models (two on-device, three in Private Cloud Compute) that were distilled and trained with help from Google's Gemini rather than served by Google, citing a rumored roughly $1B per year deal and an Apple executive's statement that Google is not the foundation of the system. He claims on-device mixture-of-experts models have improved sharply, with techniques that stream expert weights from SSD and cache hot experts in memory, and that Apple's control of model and silicon lets it exploit this. The rest of the case is distribution (about 2.5B active devices and ecosystem lock-in), device interaction data as a training source, and privacy or security as a justification for locking out third-party accessories, with Apple's history of entering late and still winning some markets as precedent. The video gives no benchmarks or primary sources for most claims, and several are unsourced.

## Key ideas
- **No frontier lab holds a model lead for long, so the durable edge is the surrounding stack (harness, tools, integration, user base).** — Speaker says the top model rotates among Anthropic, Google, OpenAI and xAI within weeks or months, so the winner is whoever wins on everything around the model. ([0:00](https://youtu.be/Ba3xunEk8Y8?t=0))
- **Apple's new Siri uses five Apple models: two on-device and three in Private Cloud Compute. Gemini was used for distillation and training, not inference.** — Speaker says a Google deal rumored at about $1B per year was used to distill the models. Apple's wording is that the models were built in collaboration with Google. Senior VP Craig Federighi is quoted as saying Google Search or similar is not the foundation of the system and Google's assistant is not used. ([0:00](https://youtu.be/Ba3xunEk8Y8?t=0))
- **On-device mixture-of-experts models have improved by orders of magnitude, and Apple's model-to-silicon control lets it exploit that.** — Speaker credits MoE work that streams expert weights directly from SSD and caches frequently used experts in memory, and says Apple's ownership of the full stack plus its privacy stance makes local models a strong fit. ([2:33](https://youtu.be/Ba3xunEk8Y8?t=153))
- **Open-weight models (DeepSeek, Kimi, MiniMax) trail closed models closely at a fraction of the cost, and know-how spreads as researchers move between labs.** — Speaker argues that distillation and researcher mobility make capability leads short-lived. He also says labs that complain about distillation were themselves caught pirating, with no source given. ([2:33](https://youtu.be/Ba3xunEk8Y8?t=153))
- **Distribution means Apple's models only need to be good enough, because switching cost across its ecosystem is very high.** — Speaker cites about 2.5 billion active devices and lock-in via AirPods, Apple Watch, Photos and Password Manager. He argues competitors would need an astronomical improvement to overcome switching friction. ([3:59](https://youtu.be/Ba3xunEk8Y8?t=239))
- **Device interaction data is a training advantage, comparable to the usage data behind coding-agent leaders.** — Speaker says millions of real users interacting with software could make models better. He cites a report, not verified in the video, that 40-50% of Anthropic revenue came from Cursor, and argues that usage data contributed heavily to Anthropic's software-engineering dominance. ([3:59](https://youtu.be/Ba3xunEk8Y8?t=239))
- **Apple uses privacy and security to justify locking third parties out of its ecosystem, and the speaker doubts the privacy claim is the real reason.** — Speaker uses AirPods as the example: third-party earbuds cannot connect to iPhone the same way. He argues the protocol could be designed better and that the privacy justification works in Apple's favor either way. ([5:04](https://youtu.be/Ba3xunEk8Y8?t=304))
- **Apple's track record is mixed: late entries like iPod, iPhone, iPad, Apple Watch, AirPods and Apple Silicon led their markets, while Maps, HomePod, Vision Pro and a cancelled car did not.** — Speaker treats Apple's late-entry pattern as a basis for expecting a late but winning AI product, while noting that in past categories Alexa (speakers) and Google (Maps) had clear leaders. ([5:04](https://youtu.be/Ba3xunEk8Y8?t=304))

## Techniques
- **Distill a frontier model into smaller deployable models** — Use a larger model as a teacher to distill and train the smaller models you ship, while serving them on infrastructure you control (speaker's description of Apple's Gemini-based distillation). The video gives no implementation details, such as data, loss or evaluation. *When:* When you need small on-device or private-cloud models without serving a third-party model at runtime. The speaker notes this is legally contested depending on the terms.
- **Run large MoE models locally by streaming experts from SSD and caching hot experts in RAM** — Keep frequently used expert weights cached in memory and page the rest in from SSD on demand, as the speaker describes for several named MoE projects. The video gives no memory or latency numbers. *When:* When running a large mixture-of-experts model on a low-memory local machine, where total weights exceed RAM but only a few experts are active per token.

## Numbers
- Google-Apple deal rumored at about $1B per year (unverified rumor) ([0:00](https://youtu.be/Ba3xunEk8Y8?t=0))
- Apple announced five models: two on-device (AFM3 Core, AFM3 Core Advanced) and three in Private Cloud Compute ([0:00](https://youtu.be/Ba3xunEk8Y8?t=0))
- Lead at the frontier lasts only a few weeks or months before others match it ([0:00](https://youtu.be/Ba3xunEk8Y8?t=0))
- Grok 4.6 is about one point behind Fable on benchmarks (no benchmark named or shown) ([2:33](https://youtu.be/Ba3xunEk8Y8?t=153))
- OpenAI Sol Ultra was released a few weeks after Anthropic's Fable ([2:33](https://youtu.be/Ba3xunEk8Y8?t=153))
- About 2.5 billion active devices worldwide ([3:59](https://youtu.be/Ba3xunEk8Y8?t=239))
- Reported (unverified) that 40-50% of Anthropic revenue came from Cursor at one point ([3:59](https://youtu.be/Ba3xunEk8Y8?t=239))

## Hot takes
- Apple's ecosystem lock-in is an excuse: privacy and security are used to block third parties, and the protocol could simply be designed better (AirPods example).
- Distribution, device data and integration matter more than frontier model quality, so a good-enough model can win.
- Labs that complain about distillation were themselves caught pirating, with no source given.
- No single lab has maintained an LLM lead, which is stated as a general fact with only anecdotal examples.
- Apple's late-entry pattern predicts an AI win, which rests on a selected list of Apple successes and failures.

## Tools mentioned
Apple Intelligence, Siri, Apple Foundation Models (AFM3 variants, names partly garbled in captions: AFM3 Core, AFM3 Core Advanced, AFM3 Cloud Pro, and one cloud variant), Private Cloud Compute, Google Gemini, Anthropic Fable (described as the public version of Mythos), Mythos (described as too dangerous for public release), OpenAI Sol Ultra (as captioned), Grok 4.6 (xAI), DeepSeek, Kimi, MiniMax, Cursor, AirPods, Apple Watch, Apple Photos, Apple Password Manager, Vision Pro, Apple Silicon, Three MoE on-device projects named in captions as Turbo Fieldfare, Calibri and Free Token (names likely garbled, not identified)

## Relevance to our work
- **agentos** (1/3): Touches on on-device MoE inference with SSD expert streaming and hot-expert caching, adjacent to InferCraft's CPU-offload and KV-cache strategy work. No numbers or implementation shown. → *Look up the MoE expert-streaming projects the speaker names (names garbled in captions) and compare their offload design against InferCraft's CPU-offload tier before sizing it.*
