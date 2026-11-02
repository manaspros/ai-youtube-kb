# Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `65X0pQ6Lmbg` · [watch](https://youtu.be/65X0pQ6Lmbg) · **date:** 2026-07-18 · **length:** 13:05 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Allen Pike · **orgs:** Forestwalk Labs, Thinking Machines
- **topics:** voice-multimodal, infra-cost-scaling, product-ux · **tags:** voice-agents, latency, prompt-caching, visual-output, model-tiering, realtime, turn-taking, generative-ui

> Allen Pike (Forestwalk Labs) on why voice input with visual output beats voice-to-voice for AI now, and the latency tactics (fast small model, eager short inference turns, stable prompt prefixes) that make it feel responsive.

## Summary
Allen Pike argues that voice is a good input for AI but visual output is the better response channel, since current voice-in, voice-out systems feel slow and dumb. He describes a voice agent Forestwalk Labs runs inside its team calls, which acted on a request (filing a Linear issue) in about a second. The core problem is latency: full voice conversation needs roughly 200 ms, while a visual response that appears within about one second still feels seamless to the user. He reports that a small GPT-5 Mini had P95 latencies of 5 to 10 seconds, so he prefers a Haiku-class model with a latency-focused inference platform. The responding model should hand heavy work to a larger model asynchronously and interleave the results. Three practices make the loop work: a fast model with a short context, inference every one or two seconds while the user is still speaking, and a stable prompt prefix so provider prefix caching cuts cost and time. The talk is short, practitioner-level, and gives a few concrete numbers, with few specifics on architecture details.

## Key ideas
- **Voice in, visuals out is the practical pattern now** — Voice is a high-bandwidth input, but voice output is hard to get right. Visual output has a larger latency budget and can carry rich HTML, controls and illustrations, so the speaker favors it as the response channel. ([0:00](https://youtu.be/65X0pQ6Lmbg?t=0))
- **Current voice interfaces feel slow and dumb** — Most people's experience with voice assistants is poor. The speaker's view is that the problem is model speed and capability, not that speaking is a bad input. ([2:36](https://youtu.be/65X0pQ6Lmbg?t=156))
- **Latency budgets set the design** — About 100 ms feels instant, about 1 s is the limit before users lose their train of thought, and full voice-to-voice conversation needs about 200 ms or less. Visual output within about a second is within the attention span and feels seamless. ([5:41](https://youtu.be/65X0pQ6Lmbg?t=341))
- **Use a fast small model, with an async handoff for heavy work** — The real-time responder must be Haiku-class or a small open model on a latency-focused platform. Heavy reasoning goes to a larger model that runs asynchronously, and its results are interleaved back into the live session. ([8:31](https://youtu.be/65X0pQ6Lmbg?t=511))
- **Send inference eagerly while the user is still talking** — Waiting for silence wastes most of the latency budget. Sending inference every one or two seconds during speech lets the agent act on partial, mid-sentence changes. ([9:59](https://youtu.be/65X0pQ6Lmbg?t=599))
- **Keep the prompt prefix stable to use prefix caching** — If the first ~90% of each request is identical, providers can serve it from cache, which the speaker says can be up to 90% cheaper and faster. Only the final ~10% should change, and output tokens should be kept low. He applies the same rule to long-running and frequently running agents. ([11:20](https://youtu.be/65X0pQ6Lmbg?t=680))

## Techniques
- **Two-tier model split (fast responder plus async thinker)** — A Haiku-class or small open model handles the live turn with a short context. It hands off heavier work as an async message to a larger model, then weaves the result into the live conversation when it arrives. *When:* Real-time voice or chat UIs where some requests need deep reasoning but the user must not wait on the reasoning.
- **Eager short-interval inference** — Instead of waiting for end-of-speech silence, run inference every one or two seconds while the user is speaking, and let the model update its action as the utterance changes. *When:* Voice turn-taking where silence detection adds seconds of latency and users revise mid-sentence.
- **Prefix-stable context layout for caching** — Keep the first ~90% of the prompt identical across requests (system prompt, tool definitions, stable context) and append the variable part at the end. Minimise output tokens. *When:* Any frequently running or long-running agent that calls a provider with prefix caching.
- **Visual response envelope** — Answer with on-screen visuals, such as generated HTML, interactive controls or illustrations, instead of spoken audio, since the visual only needs to appear within about a second. *When:* Products where the user can look at a screen and audio output would miss the ~200 ms conversational budget.

## Numbers
- Human-perceived instant response is about 100 ms; the limit before users lose their train of thought is about 1000 ms ([5:41](https://youtu.be/65X0pQ6Lmbg?t=341))
- Full voice-in, voice-out conversation needs about 200 ms latency or less ([5:41](https://youtu.be/65X0pQ6Lmbg?t=341))
- GPT-5 Mini P95 latencies of about 5000 to 10000 ms in the speaker's production use, despite being cheaper than the larger model ([8:31](https://youtu.be/65X0pQ6Lmbg?t=511))
- Inference should run every 1 to 2 seconds while the user is speaking ([9:59](https://youtu.be/65X0pQ6Lmbg?t=599))
- Prefix caching can make inference up to 90% cheaper and faster when the start of the context is unchanged ([11:20](https://youtu.be/65X0pQ6Lmbg?t=680))
- Thinking Machines demoed a model doing continuous inference in 200 ms time slices (a few weeks before the talk) ([7:04](https://youtu.be/65X0pQ6Lmbg?t=424))

## Hot takes
- Voice as an AI input is controversial, but speaking is the most natural high-bandwidth channel, and the fix is latency rather than dropping voice.
- Most voice assistant experiences today are both slow and dumb, and that combination is why people are down on voice input.
- Voice-to-voice with novel architectures is not needed yet: voice in with visual out already lands inside the attention span.
- Small cheap models are not enough for real-time voice; P95 latency is the deciding metric, and in the speaker's testing Haiku-class models beat a smaller GPT-5 variant.

## Tools mentioned
Linear, Slack, GPT-5 Mini, Haiku

## Relevance to our work
- **general** (2/3): The two-tier pattern (small fast model in the loop, larger model async for heavy work) and the prefix-caching rule both apply to cheap-model pipelines. The talk's latency numbers are anecdotal. → *Prototype a two-tier entity-resolution or extraction step: a Haiku-class model answers quick triage calls on the hot path and queues hard cases to a larger model, then measure P95 and cache hit rate.*
- **agentos** (1/3): InferCraft serves models, and the talk's point that stable prompt prefixes drive provider caching applies to the proxy and memory layers. The talk gives no measurements for self-hosted vLLM. → *In the L1 proxy or L2A context assembly, check that the system prompt, tool schemas and retrieved memory are ordered stable-first so cached prefix hits are maximised; log cache hit rate per request.*
- **prosharness** (1/3): ProsHarness runs long Claude Code sessions and resumes them from checkpoints. Keeping the prefix stable across resumes would help caching, but the talk does not discuss checkpoint or resume architecture. → *Check whether checkpoint resume re-sends a changing preamble (timestamps, plan state) at the start of the prompt; move volatile content to the end so the cached prefix survives resumes.*
