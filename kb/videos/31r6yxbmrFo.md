# Tiny AI Is About to Change Everything (IBM Granite 4.0)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `31r6yxbmrFo` · [watch](https://youtu.be/31r6yxbmrFo) · **date:** 2025-12-02 · **length:** 9:55 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andrus · **orgs:** Better Stack, IBM, Hugging Face
- **topics:** local-ai, models-research, inference-serving · **tags:** ibm-granite, granite-4, hybrid-architecture, mamba, small-models, transformers-js, browser-inference, offline, code-completion, quantization, tool-calling, hugging-face

> Better Stack walkthrough of IBM Granite 4.0 small models (hybrid Mamba-transformer, tiny browser-runnable variants), ending with an offline in-browser code-completion proof of concept.

## Summary
The host argues that small, efficient models are more interesting engineering progress than new giant benchmark-chasing releases. He presents IBM's Granite 4.0 family, which mixes transformer layers with Mamba layers to handle long context more cheaply, and says the models were trained with context windows in the hundreds of thousands of tokens. He cites Granite 4 small as roughly 32B total parameters with about 9B active via mixture-of-experts, and claims the 3B model beats older 8B Granite models. He demos the 350M Granite Nano running in the browser through transformers.js and Hugging Face, showing tool calling with output rendered as a React component, a stale 2023 knowledge cutoff, and a JSON-formatting run truncated by the demo's token limit. The main build is an offline code-completion page: the model downloads once into the local cache, then suggests the next lines on a 1-second throttle and accepts them on Tab, running on an M2 MacBook with the internet off. He uses the 1B model because the 350M was too unreliable, 4-bit quantization as IBM recommends, a 128-token limit, and temperature 1. He admits it is still a proof of concept with duplicated lines and missing closing brackets. No benchmarks are shown, and the tone is warm toward IBM.

## Key ideas
- **Granite 4.0 mixes transformer layers with Mamba layers, which the speaker presents as cheaper on long sequences than a pure transformer stack.** — Transformers get expensive as sequences grow; the hybrid is pitched as the reason the family can handle very long context (speaker says hundreds of thousands of tokens, no exact figure given). ([1:07](https://youtu.be/31r6yxbmrFo?t=67))
- **Granite 4 small is about 32B total parameters but only about 9B active per token via mixture-of-experts on the hybrid architecture.** — Speaker claims the 3B Granite model beats older 8B Granite models, framing it as more capacity for less compute. No benchmark table is shown. ([2:12](https://youtu.be/31r6yxbmrFo?t=132))
- **Small Granite models run entirely in the browser through transformers.js, using the 350M Granite Nano demo on Hugging Face.** — The demo supports tool calling, where tool results can be rendered as a styled React component; the speaker compares this to the MCP-UI idea. ([3:03](https://youtu.be/31r6yxbmrFo?t=183))
- **The browser demo exposes two limits: a stale knowledge cutoff (trained around 2023) and a token limit that truncated a JSON-formatting run.** — The truncation is fixable in your own agent by raising the max token setting, per the speaker. ([4:20](https://youtu.be/31r6yxbmrFo?t=260))
- **Offline code completion works by caching the model after the first load, then running inference locally with no network.** — Demo ran on an M2 MacBook with the internet off, suggesting the next line and then closing brackets on Tab accept. ([5:24](https://youtu.be/31r6yxbmrFo?t=324))
- **Model size matters for code completion: the 350M model was too unreliable, so the app uses the 1B model.** — The speaker found the Nano 350M too unreliable for this use case even though it worked in the chat demo. ([7:47](https://youtu.be/31r6yxbmrFo?t=467))
- **The PoC has clear quality gaps: it sometimes repeats the line just typed and sometimes omits the closing bracket.** — Speaker calls it very much a proof of concept, but says the idea of a local, offline completion assistant is compelling. ([6:49](https://youtu.be/31r6yxbmrFo?t=409))

## Techniques
- **Browser-only offline completion loop with transformers.js** — A simple HTML page with a code textarea; main.js loads the Granite 4 1B tokenizer and model through transformers.js, which caches them locally on first load so later sessions work offline. Load the model with 4-bit quantization (the level IBM recommends for this model version). *When:* Offline or privacy-sensitive coding assistance, travel without internet, or prototyping a local completion feature without a GPU server.
- **Completion prompt and generation settings** — Use a detailed system prompt that tells the model to output only the next suggested lines of code. Cap generation at 128 new tokens (raise for longer suggestions). Set temperature to 1, which the speaker found worked best. Strip non-code text artifacts from the raw response with helper functions before showing it. *When:* Inline code suggestions where a short, code-only continuation is wanted rather than chat-style prose.
- **Debounced suggestion UI with keyboard accept** — Throttle the inference call to fire about 1 second after the user stops typing. Show the suggestion, listen for keydown on Tab to append it to the code, and hide the suggestion when the user clicks outside the suggestion element. *When:* Building a responsive inline-completion UI where each model call is expensive and should not fire on every keystroke.
- **Raise the token budget in your own agent** — The browser demo cut off a long JSON output at its token limit. In your own agent code, raise the max-tokens setting to avoid truncation of structured output. *When:* Structured output (such as JSON conversion of many records) gets truncated mid-stream.

## Numbers
- Granite 4 small: about 32B total parameters, about 9B active per token (MoE on the hybrid architecture) ([2:12](https://youtu.be/31r6yxbmrFo?t=132))
- Speaker says the 3B Granite model beats older 8B Granite models on benchmarks (no table shown) ([2:12](https://youtu.be/31r6yxbmrFo?t=132))
- Context windows trained at hundreds of thousands of tokens (no exact figure) ([1:07](https://youtu.be/31r6yxbmrFo?t=67))
- Models: Granite Nano 350M (browser chat demo), Granite 4 1B (used in the completion app) ([3:03](https://youtu.be/31r6yxbmrFo?t=183))
- 4-bit quantization, recommended by IBM for this model version ([7:47](https://youtu.be/31r6yxbmrFo?t=467))
- Generation limit 128 tokens; temperature 1 worked best ([7:47](https://youtu.be/31r6yxbmrFo?t=467))
- Suggestion throttle: about 1 second after typing stops ([7:47](https://youtu.be/31r6yxbmrFo?t=467))

## Hot takes
- The title 'Tiny AI Is About to Change Everything' is hype; the substance is one author's browser demo and a small offline PoC.
- The speaker says IBM has 'risen like a phoenix' and praises the models warmly, but no benchmarks are shown to back the 3B-beats-8B claim.
- Cryptographic signing, documented training data and ISO 42001 alignment are stated as selling points without verification in the video.
- Speaker concedes the 350M model is too unreliable for code completion, which tempers the claim that small models are ready for everyday coding.

## Tools mentioned
IBM Granite 4.0, Granite 4 small, Granite 4 1B, Granite Nano 350M, transformers.js, Hugging Face, Mamba, React, MCP-UI, M2 MacBook (hardware used for the demo)

## Relevance to our work
- **agentos** (1/3): Hybrid Mamba-transformer long-context architecture is a non-transformer comparison point for InferCraft's KV-cache and serving work, though this talk gives no measurements. → *Include Granite 4.0 small (hybrid Mamba-transformer, about 9B active) as a long-context comparison point in InferCraft KV-cache benchmarks, measuring it against a pure-transformer model on the 5090.*
