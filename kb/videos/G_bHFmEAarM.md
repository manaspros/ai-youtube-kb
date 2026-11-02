# Build & deploy AI-powered apps — Paige Bailey, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `G_bHFmEAarM` · [watch](https://youtu.be/G_bHFmEAarM) · **date:** 2026-05-18 · **length:** 1:03:20 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Paige Bailey · **orgs:** Google DeepMind, Google, Augment Code
- **topics:** models-research, vibe-coding-app-building, product-ux · **tags:** gemini, ai-studio, code-execution, url-context, grounding, video-input, thinking-levels, genie-3, veo, lyria, gemma-4, gemini-live, firebase-build, robotics, demo

> Paige Bailey (Google DeepMind) gives a demo-heavy tour of Gemini models, AI Studio tools (grounding, URL context, code execution), Build for prompt-to-app, Genie 3, Veo 3.1 Lite, Gemma 4 and Gemini Live.

## Summary
This is a live demo session, mostly product walkthroughs rather than slides, from Google DeepMind developer relations. Paige Bailey runs AI Studio demos covering Gemini 3.1 Pro, 3.1 Flash, and 3.1 Flash-Lite, with tools switched on or off in the UI. Key demos include YouTube-URL video analysis, code execution for bounding boxes, URL context with inline citations, and a "Build" flow that turns a prompt into a deployed app with a database and Google login. She also shows Genie 3 world generation, Veo 3.1 Lite video, Lyria 3 music, Gemma 4 (open, Apache 2.0), and Gemini Live voice/screen interaction. The session ends with an open-source Raspberry Pi robot (Puppr) where Gemini builds the plan and on-device models run the actions. Almost all numbers are token or cost anecdotes from the demos, with no benchmarks. The useful parts are the practical tool-usage patterns, such as clipping video by time, letting code execution do exact work, and tuning thinking levels per task.

## Key ideas
- **Models only know data up to their training cutoff; post-cutoff facts need a tool such as search grounding, URL context, or retrieval.** — The speaker frames this as the reason to turn on grounding or retrieval for anything recent. She demos grounding with Google Search and says internal documents can be queried through Vertex retrieval. ([7:47](https://youtu.be/G_bHFmEAarM?t=467))
- **A YouTube URL can be passed straight into Gemini for video inference, with start and end times to limit the span.** — No download step is needed. Default sampling is about 1 frame per second, and she says five minutes of video comes to roughly 27,600 tokens. The UI also shows a 'Get Code' export for the same call. ([8:51](https://youtu.be/G_bHFmEAarM?t=531))
- **Enabling code execution gives the model a sandboxed Python environment with data science libraries pre-installed, so it can compute exact answers.** — She asks a small model to draw bounding boxes on a Lego photo. The model writes Python to do it, and runs in a sandbox so the local machine is not affected. The speaker says the small model got it right on the first try. ([13:21](https://youtu.be/G_bHFmEAarM?t=801))
- **URL context is a light form of retrieval: paste a list of URLs into the prompt and the model answers with inline citations to them.** — She calls it a poor man's retrieval, with no vector database needed. Her example compares two blog posts published after the model's cutoff. ([16:48](https://youtu.be/G_bHFmEAarM?t=1008))
- **Build turns a natural-language app spec into a deployed app with a database, Google login and secret API keys.** — Her spec for a bookshelf cataloguer covers photo upload, search grounding for book details, login, and persistence. Gemini 3.1 Pro plans the app while it builds, and the generated app can be shared by link or deployed to Cloud Run. ([24:55](https://youtu.be/G_bHFmEAarM?t=1495))
- **Genie 3 generates each frame from scratch with no physics engine, yet its responses to player actions look physics-consistent.** — The speaker says it is a composition of several models rather than a single model. The output is pixels only, so turning it into game assets needs extra steps. ([30:07](https://youtu.be/G_bHFmEAarM?t=1807))
- **For vague generation tasks, have the model expand the prompt first and then generate from the expanded version.** — She uses high thinking to rewrite a one-line request for an SVG of a photo before generation. She says the first pass was reasonable but not exact. ([39:21](https://youtu.be/G_bHFmEAarM?t=2361))
- **For robots, let the large model build the plan and let on-device models carry out the physical actions, not the live voice model.** — Gemini Live is used for reasoning and conversation, and local models handle things like picking up specific objects. The speaker presents this as the orchestration pattern for the Puppr robot. ([1:00:09](https://youtu.be/G_bHFmEAarM?t=3609))

## Techniques
- **Clip video by time and frame rate** — Pass a YouTube URL or media file to Gemini and set start/end offsets and the sampling rate, so token use stays bounded. *When:* Analysing a long public video where only a segment matters, or where cost must be controlled.
- **Let code execution do the exact work** — Turn on the sandboxed code-execution tool and ask the model to write Python for counting, boxes, masks or measurements, rather than reasoning about pixels in prose. *When:* Tasks with a checkable exact answer, such as counting objects or drawing boxes on an image, and when you want the output to be runnable code.
- **URL context as lightweight grounding** — Give the model a list of URLs with URL context enabled, so it answers from those pages and cites them inline. *When:* Answering questions about specific docs or posts, especially recent ones past the training cutoff, without standing up a vector store.
- **Per-task thinking level** — Use minimal or low thinking for fast routine responses, and high only for planning or multi-step reasoning. *When:* Balancing latency and cost across steps in one pipeline; she says she usually runs minimal or low for speed.
- **Prompt expansion before generation** — Ask the model to rewrite a short user prompt into a detailed one, then generate from that rewrite. *When:* Image-to-SVG or other generation tasks where a one-line prompt gives weak output.
- **Plan with a big model, act with a local model** — The cloud model produces a plan; smaller on-device models execute the physical or local actions. *When:* Embodied or latency-sensitive agents where the live model should not control low-level actions directly.
- **Compare mode for model choice** — Run two models side by side on the same prompt, tools and file, and compare output and cost per run. *When:* Choosing the cheapest model that still gets a tool-assisted task right.
- **Export UI experiments to code** — Use the Get Code option to turn a prototype run in the UI into SDK code (Python, TypeScript, Java) with the right model and media handling. *When:* Moving from a playground experiment to a working API call.
- **System instructions for voice output style** — Set language, accent, tone or dialect in system instructions for a realtime voice model, and tune media resolution and compression for video input. *When:* Building a multilingual or branded realtime voice or screen-aware assistant.

## Numbers
- Five minutes of YouTube video at default 1 fps is about 27,600 tokens. ([8:51](https://youtu.be/G_bHFmEAarM?t=531))
- A ~1,000-token Lego image with a bounding-box task on Gemini 3.1 Flash-Lite cost well under a fraction of a penny; Gemini 3 Flash got the same answer slower at slightly higher cost, still under a penny. ([14:27](https://youtu.be/G_bHFmEAarM?t=867))
- Augment Code moved its agent system to default to Gemini 3.1 Pro for performance and cost reasons (speaker-reported). ([2:30](https://youtu.be/G_bHFmEAarM?t=150))
- Veo 3.1 Lite output defaults to 720p (not 4K); it supports 16:9 and 9:16 and 4, 6 or 8 second durations, and is a paid-tier model needing an API key. ([47:57](https://youtu.be/G_bHFmEAarM?t=2877))
- Gemma 4 is open-weights under Apache 2.0, is free to try via the AI Studio API, and its smallest versions run on mobile devices. ([50:30](https://youtu.be/G_bHFmEAarM?t=3030))
- Genie 3 is not an API yet; it is available through an Ultra subscription in a limited set of countries. ([36:23](https://youtu.be/G_bHFmEAarM?t=2183))

## Hot takes
- Small, cheap models with tools such as code execution can match larger models on tool-assisted tasks, so the speaker recommends trying small models first.
- Genie 3 output is pixels only, so it is not a route to 3D game assets without extra work.
- A live voice model with screen and video input is much cheaper than stitching speech-to-text, an LLM and text-to-speech together yourself (speaker's claim).

## Tools mentioned
Google AI Studio, Gemini API, Gemini Live, Gemini 3.1 Pro, Gemini 3.1 Flash, Gemini 3.1 Flash-Lite, Google Search grounding, URL context, code execution, Build (AI Studio app builder), Firebase / Firestore, Cloud Run, Genie 3, Veo 3.1 Lite, Lyria 3, Nano Banana 2, Gemma 4, Vertex AI retrieval, Puppr (Raspberry Pi robot), OpenClaw

## Relevance to our work
- **agentos** (1/3): Managed sandboxed code execution with pre-installed data libraries is a reference point for the L2C Crucible sandbox design. → *Compare the Gemini code-execution sandbox (no local impact, pre-installed libraries) against Crucible's exec-gate design when writing up the sandbox threat model. Reference only.*
- **prosharness** (1/3): The plan-with-a-large-model, act-with-a-small-model split and per-step thinking levels map onto ProsHarness's plan and critique steps. → *When configuring ProsHarness planning versus execution steps, check whether the planning step can use higher thinking effort and cheaper steps can use lower effort, as the speaker suggests.*
- **general** (1/3): Cheap-model pipelines with tools (code execution, URL context, compare mode) are a pattern for the Haiku-based work the user cares about. → *Run the same tool-assisted task on a small model and a larger one, as the compare-mode demo does, and record cost and accuracy.*
