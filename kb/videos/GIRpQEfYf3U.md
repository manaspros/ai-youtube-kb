# Any-to-Any: Building Native Multimodal Agents - Patrick Löber, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `GIRpQEfYf3U` · [watch](https://youtu.be/GIRpQEfYf3U) · **date:** 2026-06-18 · **length:** 16:21 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Patrick Löber · **orgs:** Google DeepMind, Google
- **topics:** voice-multimodal, agent-architecture, mcp-and-tools · **tags:** gemini, multimodal, native-image-generation, text-to-speech, function-calling, live-api, context-caching, file-api, notebooklm-clone, gemma, multimodal-embeddings, google-gen-ai-sdk

> Google DeepMind's Patrick Löber walks through building a NotebookLM-style agent: Gemini reasons, calls native image and speech generators via function calling, and uses multimodal input and a live audio model.

## Summary
The speaker, a Gemini API and AI Studio team member at Google DeepMind, explains that Gemini currently takes many input modalities but outputs text only. Image and speech output come from separate native generation models built on Gemini. He argues for an agent (a reasoning model that decides what to create) over a hard-coded pipeline. The demo ingests a PDF, a video and an MP3 about the "Attention Is All You Need" paper in one call, then gives Gemini two function declarations, one for image generation and one for speech, so it can decide where diagrams or audio summaries help. He gives token math for audio and video, suggests context caching for repeated queries, and says native generation inherits Gemini's world knowledge. He ends with the Live API, an audio-in, audio-out model that avoids a speech-to-text, LLM, text-to-speech cascade, and a multimodal embedding model. The talk is a vendor walkthrough with some concrete code shape, but few hard benchmarks. Several of its claims are the speaker's own and were not measured in the talk.

## Key ideas
- **Gemini is not yet one all-in-one multimodal model. It takes many input types but outputs only text, and image or speech output comes from separate native models built on Gemini.** — The speaker says the all-to-all slide shows a vision, not the current product. Gemini 3 is listed as text-only output, with specialized generators beside it. ([1:05](https://youtu.be/GIRpQEfYf3U?t=65))
- **Build an agent rather than a workflow. A reasoning model chooses what to create and loops until the assets are good enough, instead of following a hard-coded pipeline.** — The loop uses Gemini as the brain, with tool calls that invoke the generator models. Output is text, speech and infographics. ([3:28](https://youtu.be/GIRpQEfYf3U?t=208))
- **Mixed sources go into one generate-content call. Large files go through the File API, small ones can be sent inline, and the prompt asks for cross-source connections.** — The demo uploads a PDF, a video and an MP3 together and asks for a summary plus practical tips. The aim is that the model links information across the modalities. ([4:51](https://youtu.be/GIRpQEfYf3U?t=291))
- **Media token budgets and windowing matter. Audio and video are priced in tokens per minute, and you can restrict analysis to a time range.** — The speaker gives about 1,920 tokens per audio minute and roughly one hour of video within the context limit. He also mentions YouTube URLs as inputs and analysing only a time range such as minute 5 to 15. ([6:15](https://youtu.be/GIRpQEfYf3U?t=375))
- **Context caching makes repeated questions over the same long files cheap.** — The speaker says it cuts costs by about 90 percent for repeated queries on loaded files. It is built into the API. ([7:25](https://youtu.be/GIRpQEfYf3U?t=445))
- **Tool use is set up with function declarations, and the prompt tells the model when each tool applies.** — Each declaration has a name, a description and parameters. Here there is one string prompt parameter per generator. The agent prompt says which concepts need a diagram and which sections need an audio summary. ([10:26](https://youtu.be/GIRpQEfYf3U?t=626))
- **Native generation inherits the main model's world knowledge, so edits can use understanding, not only style.** — Examples include drawing errors on a map to get a corrected picture, and correcting math homework by drawing on the image. Audio output handles accents and tone, including an instructed Bavarian accent. ([11:38](https://youtu.be/GIRpQEfYf3U?t=698))
- **A single audio-in, audio-out live model replaces the cascaded speech pipeline.** — Gemini 3.1 Flash Live is presented as one architecture where audio goes in and audio comes out. The speaker says it gives more natural interaction. He did not show a live demo, only a recorded clip. ([14:10](https://youtu.be/GIRpQEfYf3U?t=850))

## Techniques
- **Agentic generation loop with function-declared generators** — Use a text reasoning model as the controller. Declare one function per generator (image, speech), each with a name, a description and a single prompt string. Tell the model in the system prompt when to call each one, then let it loop until the assets are judged good enough. *When:* When one request should produce several output modalities and the set of outputs should depend on the content, such as study guides, slides or podcasts.
- **Single-call multimodal synthesis** — Upload large PDFs, videos and audio through the File API. Send small files inline. Put all parts in one contents list with an instruction to analyse them together and link the material. *When:* When you need cross-source understanding, such as lecture slides plus a recording plus voice memos.
- **Timestamp-windowed media analysis** — Restrict audio or video analysis to a time range in the request, or pass a YouTube URL directly, instead of sending the full file. *When:* When the source is long and only part of it matters, which keeps token use and cost down.
- **Context caching for repeated queries** — Cache the large media context once and reuse it across follow-up questions. *When:* When many queries hit the same long files, such as a notebook or course corpus.
- **Scaffold with a Gemini API skill** — Attach the Gemini API skill to a coding agent and ask it to write the integration code, instead of writing the SDK calls by hand. *When:* When starting a new multimodal app and you want the agent to produce the SDK wiring.
- **Audio-to-audio live session for voice** — Stream audio to a native audio model and get audio back, with no separate speech-to-text and text-to-speech steps. *When:* When voice latency and natural-sounding turn-taking matter more than a custom ASR or TTS stack.

## Numbers
- About 1,920 tokens per minute of audio input ([6:15](https://youtu.be/GIRpQEfYf3U?t=375))
- A 1M-token context fits more than nine hours of audio, per the speaker. Using 1,000,000 tokens, the arithmetic gives about 8.7 hours, so the speaker's figure assumes 2^20 tokens. ([6:15](https://youtu.be/GIRpQEfYf3U?t=375))
- Roughly one hour of video fits in the context limit, with configuration options to go longer ([6:15](https://youtu.be/GIRpQEfYf3U?t=375))
- Context caching saves about 90 percent of cost on repeated queries over the same long files ([7:25](https://youtu.be/GIRpQEfYf3U?t=445))

## Hot takes
- Native image generation inherits Gemini's world knowledge, so it can edit maps and correct math homework, not just restyle images.
- A single audio-in, audio-out model is a better base for voice agents than a cascaded speech-to-text, LLM, text-to-speech pipeline.
- Multi-output apps should be agents that decide what to generate, not fixed pipelines.

## Tools mentioned
Google Gen AI SDK, Gemini API, Google AI Studio, Gemini 3 Flash, Gemini 3.5 Flash Image preview (Nano Banana 2), Gemini 2.5 text-to-speech, Gemini 3.1 Flash Live, File API, Gemma 4, Gemini API skill

## Relevance to our work
- **agentos** (1/3): AgentOS budgets and meters traffic through a proxy. Media inputs are priced in tokens per minute, so the budget pillar would need to count them. → *Check how the budget pillar counts audio and video inputs, using about 1,920 tokens per audio minute as a reference point, before adding media passthrough.*
- **general** (1/3): The agent-loop-with-function-declarations pattern applies to any task that produces several outputs, and it is a concrete alternative to a fixed pipeline. → *Prototype one multi-output task as a reasoning-model loop with a function declaration per generator, then compare step count and cost against a hard-coded pipeline on the same inputs.*
