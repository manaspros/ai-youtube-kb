# Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `DCZZ3AJKzuc` · [watch](https://youtu.be/DCZZ3AJKzuc) · **date:** 2026-05-18 · **length:** 8:12 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Luke Harries · **orgs:** ElevenLabs, Revolut, PostHog, GOV.UK
- **topics:** voice-multimodal, agent-architecture, mcp-and-tools · **tags:** voice-agents, text-to-speech, speech-to-text, turn-taking, sdk-wrapper, elevenlabs, product-preview, chat-to-voice

> ElevenLabs' Luke Harries argues chat agents should add voice, and previews VoiceEngine, a wrapper that adds STT, TTS and turn-taking to an existing chat agent without a rebuild.

## Summary
Luke Harries (Head of Growth, ElevenLabs) argues that 2025 was the year of chat agents and that voice is the natural next interface because it is faster, more accessible and works across channels such as phone lines and Zoom calls. He observes that most voice stacks look alike: a voice engine (speech-to-text, text-to-speech, turn-taking) plus an agent layer (LLMs, RAG, tool calling, integrations). Many customers had already built the agent layer and did not want to rebuild it, so ElevenLabs is previewing VoiceEngine, a separately packaged voice engine that wraps an existing agent. The server SDK attaches to the existing chat agent and proxies each new session through to it, and a client SDK adds a site widget in about three lines. Telephony and UI components come with it, and a bundled skill lets a coding agent convert a chat agent to voice in roughly one prompt. The talk is a product preview with a short local demo and little measured data, so the claims are mostly unverified.

## Key ideas
- **Voice is the next interface for agents** — The speaker says chat is now the default AI interface but feels limited. Voice is faster, more accessible (for people with dyslexia or who struggle with keyboards) and omnichannel, so it can reach phone lines and meeting calls. ([1:02](https://youtu.be/DCZZ3AJKzuc?t=62))
- **Most voice stacks share the same two layers** — A voice engine handles speech-to-text, text-to-speech and turn-taking. An agent layer handles LLMs, RAG, tool calling and integrations. Teams that already built the agent layer did not want to rebuild it. ([2:03](https://youtu.be/DCZZ3AJKzuc?t=123))
- **Wrap the existing agent instead of replacing it** — VoiceEngine is pitched as a first-class primitive that attaches to any existing chat agent. For each new session it starts a loop that proxies traffic to the agent, so the agent's evals and transcription work are kept. ([3:24](https://youtu.be/DCZZ3AJKzuc?t=204))
- **Client SDK adds a site widget with very little code** — The speaker says the client SDK takes about three lines to add a widget to a website. Telephony and prebuilt UI components (shadcn/Vercel style) are offered out of the box once the agent is wrapped. ([4:21](https://youtu.be/DCZZ3AJKzuc?t=261))
- **A coding agent plus a bundled skill does the conversion** — The planned release ships with a skill. The speaker says one prompt is enough for a coding agent to read the codebase, find the chat agent, work out how to deploy it and write the wrapper. The demo was run locally. ([4:21](https://youtu.be/DCZZ3AJKzuc?t=261))
- **Reuse existing tool calls and split client and server tools** — Most tool calling already lives in the chat agent's backend, so the wrapper needs no new tool work. ElevenLabs also has client-side tools (which can change the DOM in the browser) and server-side tools, and plans to let some client tool calls be proxied to the wrapped agent. ([6:41](https://youtu.be/DCZZ3AJKzuc?t=401))

## Techniques
- **Voice wrapper around an existing agent** — Keep the chat agent as-is. Attach a voice engine to each new session and proxy messages through to the agent so that the agent's logic, RAG and tools stay in place. Add a client widget on the front end. *When:* You already have a tested chat agent and want a voice channel without rewriting the agent logic or its evals.
- **Client-side vs server-side tools for voice** — Run tools that manipulate the page (DOM) as client-side tools in the browser. Run data and integration tools on the server, and proxy calls from the voice layer to the agent's backend. *When:* A voice agent needs to act on what the user sees in the browser as well as call backend systems.
- **Prompt a coding agent with a conversion skill** — Ship or install a skill that holds the best-practice wiring. Then give a coding agent one prompt that tells it to analyse the codebase, locate the agent, and write the wrapper and deploy steps. *When:* You want a fast, mostly automated migration of an existing agent to a new modality, with a skill holding the integration details.

## Numbers
- The client SDK adds a website widget in about three lines of code. ([3:24](https://youtu.be/DCZZ3AJKzuc?t=204))
- Converting an existing chat agent to voice is said to take about one prompt to a coding agent (demo was local; release was about two weeks away at the time). ([4:21](https://youtu.be/DCZZ3AJKzuc?t=261))
- Speaker says voice product release was 'a couple of weeks' away, and the product is in early preview with design partners sought. No latency, accuracy or adoption figures were given. ([2:03](https://youtu.be/DCZZ3AJKzuc?t=123))

## Hot takes
- Chat agents will either die or add voice.
- Voice is the natural medium for agents and is more accessible than text.

## Tools mentioned
ElevenLabs VoiceEngine, ElevenLabs Scribe (speech-to-text), ElevenLabs V3 (text-to-speech), ShadCN / Vercel-style UI components

## Relevance to our work
- **agentos** (1/3): AgentOS already puts a proxy in front of agents, and a voice front end could sit on that proxy. The talk gives no architecture detail beyond a session-proxy loop, and voice is not in the profile. → *Low priority: note the wrap-existing-agent proxy pattern and consider it only if AgentOS ever gets a voice channel; do not build it now.*
- **general** (1/3): Shows a common pattern for adding a new modality by wrapping an existing agent and having a coding agent do the wiring from a skill. This matches the context-engineering and skills interest. → *Read the skill-based conversion approach if the ElevenLabs skill is published, and compare it with how skills are written in our own repos.*
