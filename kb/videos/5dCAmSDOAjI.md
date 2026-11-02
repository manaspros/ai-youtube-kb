# The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `5dCAmSDOAjI` · [watch](https://youtu.be/5dCAmSDOAjI) · **date:** 2026-09-18 · **length:** 17:30 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Ahmed Ahres · **orgs:** Reactor, ByteDance, Alibaba, NVIDIA, Google DeepMind
- **topics:** voice-multimodal, inference-serving, product-ux, infra-cost-scaling · **tags:** real-time-video, world-models, streaming-inference, interactive-generation, video-to-video, gpu-routing, vendor-pitch

> Ahmed Ahres (Reactor) argues real-time interactive video and world models will change how content is made and consumed, then describes the infra gaps: streaming, session memory, and sub-100 ms global latency. Mostly a company pitch.

## Summary
Ahmed Ahres, head of go-to-market at Reactor (a Series A company building an API platform for real-time world models), argues that batch video generation is a "slot machine" because you get a file back and cannot change it. He claims real-time generation makes video programmable and gives creators instant feedback, using GPS and digital film as historical analogies. He sorts the market into three model types: infinite real-time interactive video, interactive world models that control a character from an image and text, and live interactive avatars. He lists use cases (live-stream voting, medical and cooking simulation, video-to-video editing, robotics training data, education) and names four models Reactor hosts. The infrastructure section is the most useful part: real-time serving needs pixel streaming, persistent live sessions with memory, and sub-100 ms latency via GPUs in the user's region. He closes with a promo code and admits in Q&A that evaluating real-time consistency and fidelity is unsolved and relies on human judgment. Treat the product claims as vendor claims.

## Key ideas
- **Batch video generation is passive: you prompt, get a file back, and cannot change it. Real-time generation makes video programmable, like software.** — The speaker frames instant feedback as the ultimate control for creators. He says real-time changes what the medium is, not just how fast it is made. ([1:31](https://youtu.be/5dCAmSDOAjI?t=91))
- **Past media shifts that were really about real-time feedback** — He compares GPS (which he says enabled Uber) and digital film with live preview (which he links to Instagram and TikTok). His point is that seeing the output while producing it is what unlocked new products. ([2:59](https://youtu.be/5dCAmSDOAjI?t=179))
- **Three model categories are emerging** — (1) infinite, interactive, real-time video models (Veo/Sora-like, but live and steerable, e.g. changing a scene mid-stream); (2) interactive world models that control a character from an image and text prompt; (3) live interactive avatars, which he says are still not solved. ([4:25](https://youtu.be/5dCAmSDOAjI?t=265))
- **Live-stream voting and interactive stories are the first consumer use cases** — Audiences type what happens next and vote on live-generated video. He also mentions medical-training and cooking simulations, and video-to-video editing done by prompting. ([9:16](https://youtu.be/5dCAmSDOAjI?t=556))
- **Real-time serving is a different problem from batch serving** — Batch means send a request and get a file. Real-time means streaming pixels to the client, keeping a live session running, and maintaining memory so the scene stays consistent when the camera turns away and back. ([11:40](https://youtu.be/5dCAmSDOAjI?t=700))
- **Latency target is sub-100 ms, which requires regional GPU routing** — Users in India or Japan should be routed to GPUs in or near their region. Without worldwide compute, he says, the experience stops being real-time and breaks the medium. ([13:08](https://youtu.be/5dCAmSDOAjI?t=788))
- **Evaluation for real-time world models is unsolved** — Fidelity is easy to judge because it is pixels. Consistency and real-time quality have no good automated metric today, so evaluation is human judgment ('look at it'). He says the research community has not solved this yet. ([16:16](https://youtu.be/5dCAmSDOAjI?t=976))

## Techniques
- **Stream frames over a live session instead of returning a file** — Keep a persistent session per user, stream pixels from server to client, and treat generation as a continuous job rather than a request/response call. The speaker gives no transport details. *When:* Interactive media where the user changes input while output is still being generated.
- **Regional GPU routing for a latency budget** — Route each user to the nearest GPU pool (for example India to India, Japan to Japan) so the round trip stays under about 100 ms. *When:* Any real-time interactive service where distance dominates latency and you run a global user base.
- **Session memory to keep generated worlds consistent** — Spend engineering effort on the context window so the model remembers earlier scene content when the viewpoint returns. He names this as a known weakness of current models and gives no method. *When:* Long-running generative sessions where revisiting earlier content must stay consistent.
- **Multi-GPU serving plus quantization for cost and speed** — Spread the model across multiple GPUs, optimize weights, and apply quantization. Trade-offs are set by priority (Q&A answer). *When:* Real-time inference where per-session compute cost must stay low enough to sell cheaply.
- **Human-in-the-loop evaluation for real-time output** — Judge consistency and quality by watching output. He says no automated real-time eval exists yet, so this is the current method. *When:* Generative output where no reliable automated metric exists yet.

## Numbers
- Target latency is sub-100 ms anywhere in the world, which requires GPUs near the user ([13:08](https://youtu.be/5dCAmSDOAjI?t=788))
- Integration is about 10 lines of code with an API key (the speaker says he simplified it) ([13:08](https://youtu.be/5dCAmSDOAjI?t=788))
- Promo code offers $75 of compute credits (vendor promotion, not a benchmark) ([13:08](https://youtu.be/5dCAmSDOAjI?t=788))
- Reactor hosts four models from ByteDance, Alibaba, and NVIDIA (two NVIDIA entries) ([10:36](https://youtu.be/5dCAmSDOAjI?t=636))
- Talk length is 17:30; no benchmark numbers, costs, or adoption stats were given ([0:12](https://youtu.be/5dCAmSDOAjI?t=12))

## Hot takes
- Batch AI video is a slot machine, and real-time generation changes the medium rather than just speeding it up [1:31]
- Ads will be generated live for each viewer from what they looked at, and pre-produced ads will go away [5:24]
- Real-time video evaluation is unsolved, and even large labs rely on human judgment (speaker's claim) [16:16]

## Tools mentioned
Reactor API (real-time world model platform, roughly 10 lines to integrate per the speaker), Helios (ByteDance, interactive video model), LingBot (Alibaba, world model), LongLive 2 (NVIDIA, multi-shot film model), StreamDiffusion (NVIDIA, video-to-video; transcript reads 'SoundCloud Streaming', likely a caption error), Veo, Sora, Genie 3 (mentioned as comparisons)

## Relevance to our work
- **agentos** (1/3): InferCraft serves models on one GPU with session scheduling. The talk's per-session streaming and latency framing (sub-100 ms, regional routing) is a loose design constraint, not a method. → *Low priority: when scoping InferCraft's scheduler for long-lived sessions, list the speaker's per-session memory and sub-100 ms latency targets as constraints to check against.*
