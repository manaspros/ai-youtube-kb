# Your Voice Agent is Just a Walkie Talkie — Neil Zeghidour, Gradium

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `a8EcVumh71E` · [watch](https://youtu.be/a8EcVumh71E) · **date:** 2026-09-18 · **length:** 19:14 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Neil Zeghidour · **orgs:** Gradium, Kyutai, OpenAI, Thinking Machines, Anthropic, Apple
- **topics:** voice-multimodal, agent-architecture, models-research · **tags:** voice agents, speech-to-speech, full duplex, half duplex, turn-taking, backchanneling, neural codec, audio tokenizer, multi-stream, Moshi, MoshiRAG, hybrid architecture, cascaded pipeline, latency, GPT Realtime

> Gradium's CEO traces voice agents from Siri to speech-to-speech models, explains why full-duplex needs multi-stream audio, and argues for a small full-duplex front end delegating to a background text LLM.

## Summary
Neil Zeghidour, CEO of Gradium (a Paris model company that grew out of the Kyutai research lab), walks through three generations of voice interfaces: closed-ended NLU pipelines like Siri, open-ended LLM voice modes with high latency and no real actions, and today's voice agents that call tools. He argues that speech-to-speech models gain naturalness and latency but lose intelligence, because adding audio to a text model's fixed capacity costs reasoning ability. He explains that current realtime models are half-duplex (turn-taking), that full duplex needs a multi-stream architecture, and that raw audio must be compressed by neural codecs before an LLM can process it. He proposes splitting the system into a small, natural, full-duplex front model and a large background text model that handles thinking and tools, citing cost and freedom to swap back-ends. The last few minutes are mostly product and hiring pitch for Gradium's models.

## Key ideas
- **Voice has moved through three generations: closed-ended NLU pipelines (Siri), open-ended LLM voice modes with no real actions, and now voice agents that take actions with tools.** — Siri-era systems ran a fixed chain of transcript, intent classification and app action. LLM voice modes replaced that logic and became open-ended, but could not check stocks or weather. Today's agents keep natural speech while calling tools, tracking state and taking payment in a drive-through demo. ([1:00](https://youtu.be/a8EcVumh71E?t=60))
- **Speech-to-speech models trade intelligence for naturalness.** — Cascaded STT-LLM-TTS systems inherit the strength of the best text models. Speech-to-speech models keep tone and emotion but lag in reasoning and tool reliability. The speaker's explanation is that a model's fixed capacity is shared between text and audio. ([6:40](https://youtu.be/a8EcVumh71E?t=400))
- **Raw audio cannot go into an LLM directly, so audio must be compressed into tokens first.** — A roughly 3-second sentence at 24 kHz becomes about 72,000 time steps. Attention cost grows with the square of sequence length, so a 10,000x longer sequence costs about 100 million times more. A neural codec (audio tokenizer) encodes audio into dense discrete tokens and decodes them back, letting an LLM train on audio tokens much as it would on text. ([10:56](https://youtu.be/a8EcVumh71E?t=656))
- **Current realtime speech models are half duplex: they either speak or listen.** — Turn-taking breaks on backchanneling ("mm-hm") and interruptions. Human phone calls have up to about 20% of time with both people speaking. Half-duplex models cannot handle that overlap, and that limitation cannot be fixed by lower latency alone. ([8:09](https://youtu.be/a8EcVumh71E?t=489))
- **Full duplex comes from modeling two parallel token streams, one for each speaker.** — Instead of one sequence where user and model alternate, a multi-stream transformer models both sides at once, so each can be active or silent independently. The speaker says Moshi (August 2024) was the first full-duplex model. He claims this design stays robust in noisy, overlapping speech. ([12:08](https://youtu.be/a8EcVumh71E?t=728))
- **Two architectural paths: scale one speech-to-speech model, or split naturalness from intelligence.** — Path one (which he thinks OpenAI follows) is a frontier text LLM post-trained on audio: one model, easy to deploy, but costly to build. Path two, MoshiRAG, uses a small on-device full-duplex model that handles conversation and asynchronously delegates hard queries to a background text LLM. He notes this approach is also used in Thinking Machines' interaction models. ([14:51](https://youtu.be/a8EcVumh71E?t=891))
- **The split design is motivated by cost and by the freedom to choose the back-end model.** — Running chit-chat through a large speech-to-speech model is expensive. A separate back-end lets a product swap in newer text models. He says OpenAI's advanced voice mode ran on GPT-4o for a long time because the speech model was costly to update. ([17:35](https://youtu.be/a8EcVumh71E?t=1055))

## Techniques
- **Audio tokenizer (neural codec) before the LLM** — Encode waveform into a compact sequence of discrete audio tokens, train an LLM to predict audio tokens from past tokens, and decode back to audio. This cuts sequence length by orders of magnitude versus raw samples. *When:* Whenever you need a language model to handle speech directly rather than through a transcript-and-TTS cascade.
- **Multi-stream full-duplex modeling** — Use one transformer that models two parallel token streams, one per speaker, so both can talk, listen, or overlap at the same time instead of alternating turns. *When:* When the product needs interruptions, backchanneling, or overlapping speech to feel natural (e.g. noisy or chaotic calls).
- **Split front-end / background-LLM voice architecture (MoshiRAG)** — A small, natural, possibly on-device full-duplex speech model handles the conversation and learns when it does not know something. It hands the query asynchronously to a large background text LLM, which returns text for the voice layer to speak. *When:* When you want speech naturalness and low latency without losing the reasoning and tool quality of the best text models, or want to swap the back-end model freely.

## Numbers
- Kyutai released Moshi, the first full-duplex speech-to-speech model, in 2024 (announced live in August 2024 per the talk). ([0:08](https://youtu.be/a8EcVumh71E?t=8))
- Sample sentence of about 8 words (around 3 seconds) at 24 kHz equals roughly 72,000 raw audio time steps. ([10:56](https://youtu.be/a8EcVumh71E?t=656))
- A 10,000x longer sequence costs about 100 million times more under quadratic attention. ([10:56](https://youtu.be/a8EcVumh71E?t=656))
- In a typical phone conversation, up to about 20% of the time both people are speaking at once. ([9:37](https://youtu.be/a8EcVumh71E?t=577))
- OpenAI's advanced voice mode was powered by GPT-4o for a long time, despite several newer text-model generations, because speech-to-speech is expensive to update. ([17:35](https://youtu.be/a8EcVumh71E?t=1055))

## Hot takes
- Speech-to-speech models will stay less intelligent than cascaded text-based voice agents unless scaling closes the gap.
- A hybrid front-end/back-end split beats end-to-end speech models on both cost and optionality, even though the field has been betting on end-to-end systems.
- Current realtime APIs (half duplex) cannot be fixed by lower latency alone, because turn-taking is a structural limit.

## Tools mentioned
Moshi, Hibiki, GPT Realtime, OpenAI advanced voice mode, Siri, Claude Sonnet 5

## Relevance to our work
- **agentos** (1/3): The split front-end / background-LLM pattern is a routing idea that could apply to the L1 proxy's strategy routing, but the talk is about audio, which AgentOS does not handle. → *Read the MoshiRAG paper and note whether a small-model-delegates-to-large-model split could fit the L1 strategy-routing design.*
- **prosharness** (1/3): Asynchronous delegation from a fast front model to a slower background reasoner is close to ProsHarness's plan, critique and delegate loop, though the talk does not cover harnesses. → *Consider whether ProsHarness's background worker design could use a fast front agent that delegates asynchronously while staying responsive.*
- **general** (1/3): Cheap-model front ends with a larger model behind them fit the Haiku pipeline interest, but the talk gives no cost numbers for text pipelines. → *Look for a cost-vs-quality comparison of small-front / large-back-end routing for text agents.*
