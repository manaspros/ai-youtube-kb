# Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `cVzf49yg0D8` · [watch](https://youtu.be/cVzf49yg0D8) · **date:** 2026-05-18 · **length:** 1:47:34 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Thor Schaeff, Philipp Schmid · **orgs:** Google DeepMind, Google AI Studio, Shopify, Waymo, LiveKit, Pipecat, Vision Agents, Fishjam, Vox Implant, Hey Addo, Context7, skills.sh
- **topics:** voice-multimodal, agent-architecture, mcp-and-tools, context-engineering · **tags:** gemini-interactions-api, gemini-live-api, server-side-state, implicit-caching, agent-skills, coding-agent, native-audio, ephemeral-tokens, context-window-compression, background-execution, google-search-grounding, system-instructions

> Google DeepMind hands-on workshop on building agents with the Gemini Interactions API (server-side state, background runs, skills) and the Live API (native-audio voice agents), with live demos that partly failed.

## Summary
Two Google DeepMind developer-experience speakers ran a 1h47m hands-on workshop. Part one introduced the Interactions API, which keeps conversation state on the server through a previous-interaction ID, supports background runs for long tasks, and works for both models and built-in agents such as Deep Research. The speakers then built a small coding agent step by step (read/write file tools, a bash tool, and a loop that runs until the model stops calling tools), using a Gemini skill installed into the coding agent as the main source of current API knowledge. Part two covered the Live API, a stateful WebSocket API with native-audio models, tool calling, and Google Search grounding, plus three ways to connect it (server proxy, ephemeral tokens, or a partner WebRTC layer). The live demos repeatedly failed, including grounding and tool calls. Q&A admitted that native-audio agents still lack per-step observability, so cascaded pipelines remain the safer choice for many business uses.

## Key ideas
- **Server-side state removes the client loop bookkeeping** — With the Interactions API you pass the previous interaction ID and send only the new input. The server holds the history, so the client does not resend or append turns. The speakers say this also simplifies agent loops. ([11:30](https://youtu.be/cVzf49yg0D8?t=690))
- **Long agent runs should be async, not held-open HTTP** — Agent calls can take minutes. The speaker says keeping connections open for more than about 10 seconds is poor practice. Background mode returns immediately, and the client polls or gets a webhook when the work is done. ([12:34](https://youtu.be/cVzf49yg0D8?t=754))
- **Server-held history helps cache hit rate** — Stripping whitespace or editing history on the client breaks implicit caching. Letting the server keep the context keeps the prefix stable. The speakers say startups using it see two to three times better cache rates. They also admit small prompt edits can still break the cache. ([13:42](https://youtu.be/cVzf49yg0D8?t=822))
- **Put what the model cannot know in the skill, and link to the rest** — The skill tells the agent which Gemini models exist, since the agent otherwise defaulted to an old model. Full API docs are not inlined. The skill links to Markdown docs that the agent fetches, so the skill does not need an update each time the API changes. ([23:40](https://youtu.be/cVzf49yg0D8?t=1420))
- **Tool loop: run until the model stops requesting tools** — The loop checks the interaction outputs for function calls, runs matching tools, sends the results back as a new interaction, and recurses. It stops when the model returns text. Thought signatures from reasoning models must be passed back in the same format. ([31:51](https://youtu.be/cVzf49yg0D8?t=1911))
- **A system instruction fixed a tool-calling failure** — The agent did not use its write-file tool until the speakers added a system instruction describing it as a coding agent with local file access. Explicit role and tool-use framing solved it. The speaker also says hallucinated weather answers are mostly a system-prompt problem. ([34:18](https://youtu.be/cVzf49yg0D8?t=2058))
- **Native-audio Live API has few observability hooks** — The model goes audio-token to audio-token rather than through a text pipeline, which gives low latency and natural barge-in. But transcripts and per-step rewrites are not exposed. The speaker says a cascaded pipeline is better for business use cases today. ([1:29:29](https://youtu.be/cVzf49yg0D8?t=5369))
- **Ephemeral tokens let the browser connect directly** — The server mints a short-lived token with the real API key and returns it to the client. The client opens the Live WebSocket itself, which avoids the extra hop through the server. Ephemeral tokens currently use the v1alpha API. ([1:14:03](https://youtu.be/cVzf49yg0D8?t=4443))

## Techniques
- **Chained interactions via previous ID** — Store the returned interaction ID and pass it as previous_interaction_id on each next call, so the server holds the history. Use interactions.get to walk back through the chain or branch from any earlier ID. *When:* Multi-turn agents where you want less client state handling and better cache hits. Be aware the free tier keeps interactions about one day and paid keeps them 55 days, and that context has no automatic compaction yet.
- **Async background runs with polling or webhooks** — Start the long agent task with background set to true, then poll for the result or subscribe to a webhook (the speaker says webhooks are coming). *When:* Agent or deep-research tasks that take minutes, where holding an HTTP connection is unreliable.
- **Skill that links to live docs** — Write a skill that covers only the model list, high-level behavior and gotchas, and points to a Markdown version of the docs that the agent fetches with web fetch or a file read. *When:* Packaging API knowledge for a coding agent when the API changes faster than the skill can be republished.
- **Tool loop with recursion** — Build tool definitions as JSON schemas, then for each output of type function call, execute the local function and send the result back. Recurse until there are no function calls. *When:* Any custom-tool agent on the Gemini API. Check that the model's tool names match your tool map to catch hallucinated tools.
- **Server-to-server Live proxy** — A backend (FastAPI in the example) holds the API key, opens the Live WebSocket to Gemini, and relays audio and video frames from the browser. *When:* When the API key must stay on the server. Accept the added hop latency.
- **Ephemeral token for direct browser connection** — The server calls the token endpoint with the real key and sends a short-lived token to the client. The client connects to the Live WebSocket directly with the token, and sends the setup message with model, tools and system instructions. *When:* Low-latency browser voice where you do not want the long-lived key on the client.
- **Context window compression for long Live sessions** — Enable the sliding-window context compression option so the session does not hit the time limit. Older context is dropped as the session goes on. *When:* Any Live session longer than the limits noted in the numbers section.
- **Voice persona through system instructions** — Set the accent and persona in the system instruction, for example asking for a friendly Irish accent on a fixed base voice. The model follows it because of its audio understanding. *When:* When the base voice list is too limited for the brand or persona.
- **Send a single image and then audio** — Send one image in real time, then stream audio. Do not stream frames that do not change. *When:* Voice coding or support assistants that look at one screen state at a time. The speaker estimates about 1,200 tokens per image.

## Numbers
- Cached input tokens are about 90% cheaper than uncached ones (speaker's figure for cache requests). ([13:42](https://youtu.be/cVzf49yg0D8?t=822))
- Startups using the Interactions API report two to three times better implicit cache hit rates. ([13:42](https://youtu.be/cVzf49yg0D8?t=822))
- Interaction storage: free tier keeps state about one day, paid tier keeps it 55 days. ([43:07](https://youtu.be/cVzf49yg0D8?t=2587))
- Without context compression, Live audio-only sessions are limited to about 15 minutes; audio-video sessions to about 2 minutes. ([1:25:28](https://youtu.be/cVzf49yg0D8?t=5128))
- Live API video input is capped at one frame per second. ([55:01](https://youtu.be/cVzf49yg0D8?t=3301))
- Gemini Live supports about 97 languages in preview, and handles code-switching such as Denglish. ([57:37](https://youtu.be/cVzf49yg0D8?t=3457))
- One image is about 1,200 tokens. ([1:38:28](https://youtu.be/cVzf49yg0D8?t=5908))
- The native voice set has about 30 voices. ([1:00:15](https://youtu.be/cVzf49yg0D8?t=3615))
- Speaker says keeping an HTTP connection open for more than about 10 seconds is poor practice. ([12:34](https://youtu.be/cVzf49yg0D8?t=754))

## Hot takes
- For many business voice use cases today, a cascaded STT-LLM-TTS pipeline is still the better bet because native audio gives little observability.
- Skills should hold model lists and gotchas, and link to docs instead of copying them, since agents can fetch Markdown on demand.
- Client-side context editing (stripping whitespace, trimming history) breaks implicit caching, so server-held state is the cheaper default.

## Tools mentioned
Gemini Interactions API, Gemini Live API, Google AI Studio, Gemini 3 Flash / 3.1 Flash Live, Lyria 3, Nano Banana, Google Search grounding, uv, FastAPI, Context7, skills.sh, Antigravity, NVIDIA Parakeet

## Relevance to our work
- **general** (2/3): Directly relevant to context engineering: what belongs in a skill versus fetched docs, system-instruction framing that fixes tool use, and how history handling affects cache hits. → *Audit CLAUDE.md and skill files for copied reference docs and move them to linked sources, and check that the stable prefix is not edited between turns.*
- **agentos** (1/3): The caching argument (server-held state gives better cache hits) is relevant to a cost-control layer in front of model calls, but it is a Gemini API point and not an AgentOS feature. → *Measure cache hit rate in the AgentOS proxy when a client resends full history versus sending a stable prefix, before adding any state-holding logic.*
- **prosharness** (1/3): The skill-links-to-live-docs pattern and the step-by-step agent loop touch ProsHarness skill design, but the talk does not cover checkpointing or plans. → *Read the skill section at 23:40 and check whether any ProsHarness skill file copies docs that could be linked instead.*
