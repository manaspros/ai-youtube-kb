# TEN Framework: Voice AI That Can Actually Be Interrupted

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ES3HhoYCtIc` · [watch](https://youtu.be/ES3HhoYCtIc) · **date:** 2026-07-02 · **length:** 7:51 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, Agora, Deepgram, OpenAI, ElevenLabs, xAI, LiveKit, Pipecat
- **topics:** voice-multimodal, agent-architecture · **tags:** TEN Framework, voice agents, barge-in, interruptions, turn detection, VAD, graph of extensions, Docker Compose, Agora RTC, Deepgram, ElevenLabs, TEN Manager, LiveKit Agents, Pipecat, open source

> Better Stack hands-on test of TEN Framework, an open-source runtime for real-time voice agents built as graphs of extensions, focused on whether interruptions (barge-in) work.

## Summary
The presenter tests TEN Framework, an open-source runtime for real-time multimodal voice agents, with interruption (barge-in) as the main check. TEN models an agent as a graph of extensions (STT, LLM, TTS, VAD, memory, tools) instead of a linear STT to LLM to TTS chain, so audio can keep streaming while the model thinks and the agent can stop speaking, cancel generation, or run tools in parallel. Setup needs API keys for Agora (real-time audio), Deepgram (speech recognition), an LLM (OpenAI in the demo), and ElevenLabs (voice), then a single docker compose up; the first run takes a few minutes. In the demo the agent stopped when interrupted, but its answers were off-topic (it confused "TEN" with TensorFlow), and the presenter says the Deepgram preset was best while the XAI presets were weaker. The TEN Manager graph designer lets you click into each node to see how data flows, which the presenter values for debugging real-time pipelines. The verdict is that TEN suits production or serious prototypes that need natural turn-taking, low latency, multimodal input or flexible deployment, but is too heavy for a simple text agent, and LiveKit Agents or Pipecat will get a basic voice prototype running faster.

## Key ideas
- **Interruption handling is the real test of a voice agent. The presenter starts speaking mid-answer to see whether the agent stops and listens or keeps talking.** — The demo judges TEN mainly on barge-in. The agent did cut off when interrupted, but its content was poor in the first run. ([0:00](https://youtu.be/ES3HhoYCtIc?t=0))
- **TEN models an agent as a graph of extensions rather than a linear pipeline. Each extension does one job: STT, LLM, TTS, VAD, memory, tools.** — Extensions can be written in Python, C++, Go, Rust or TypeScript. The graph lets pieces run concurrently, which matters when audio keeps streaming while the model is thinking. ([1:09](https://youtu.be/ES3HhoYCtIc?t=69))
- **A linear STT to LLM to TTS chain breaks on real conversation. Users interrupt, so the agent may need to stop speaking, cancel generation, detect silence, or call tools in parallel.** — The presenter argues this is why TEN treats agents as graphs. The claim is architectural reasoning, not a benchmark. ([1:09](https://youtu.be/ES3HhoYCtIc?t=69))
- **Bring-up needs four external services and one Docker command. Keys are needed for Agora, Deepgram, an LLM and ElevenLabs.** — TEN ships with several preset configurations. The presenter picks the Deepgram TTS preset and connects from the browser. The first Docker run takes a few minutes. ([2:32](https://youtu.be/ES3HhoYCtIc?t=152))
- **Output quality is the weak spot in the demo. The agent answered a question about TEN with TensorFlow, then apologized and stopped after being cut off.** — The presenter says the voice stack works but conversation quality is uneven. He blames the preset and the model choice, and ranks the XAI presets below Deepgram. ([2:32](https://youtu.be/ES3HhoYCtIc?t=152))
- **The TEN Manager graph designer shows the extension graph and lets you open each node, such as the Agora audio-frame node, to inspect data flow.** — The presenter values this for debugging real-time systems, where it helps locate where data flows and where latency builds. He says it is not needed for drag-and-drop building. ([4:01](https://youtu.be/ES3HhoYCtIc?t=241))
- **VAD and turn detection make the biggest difference to perceived conversation quality. Users judge the agent by whether it listens and answers at the right time, not by the architecture.** — The presenter's own experience with the demo supports this, but it is one anecdotal run. ([5:07](https://youtu.be/ES3HhoYCtIc?t=307))
- **TEN fits production or serious prototypes that need interruptions, low latency, multimodal input or flexible deployment. It is too much setup for a simple text agent or a quick voice prototype.** — The presenter's alternatives for a fast prototype are LiveKit Agents and Pipecat. ([7:22](https://youtu.be/ES3HhoYCtIc?t=442))

## Techniques
- **Graph-of-extensions voice agent** — Split the agent into separate extensions (speech recognition, VAD, LLM, TTS, memory, tools) and wire them as a graph, rather than a single STT to LLM to TTS chain. Let audio stream in while the LLM runs, so the agent can cancel generation or stop speaking when the user talks. *When:* Real-time voice agents where users interrupt, tools run in parallel, or the stack has several swappable models.
- **Barge-in test for voice agents** — Start a conversation, let the agent begin a long answer, then interrupt mid-sentence. Check whether it stops and listens, whether the next turn works, and whether the reply stays relevant. Repeat with several presets. *When:* Before trusting any voice stack. Interruption behavior is the first thing to test, before features or setup.
- **Local TEN bring-up with Docker Compose** — Add API keys for Agora (real-time audio), Deepgram (speech recognition), an LLM provider (OpenAI in the demo) and ElevenLabs (voice). Start everything with a single docker compose up from the TEN repo, wait a few minutes on the first run, then open the web UI and pick a preset. The video does not show the repo URL, key file names or compose flags. *When:* Quick evaluation of TEN on a dev machine. Check the repo README for the exact key and config file names.
- **Graph-based debugging in TEN Manager** — Open the TEN Manager designer during a live session. Click each node (for example the Agora audio-frame node) to see what flows through it and where it slows down. *When:* Diagnosing latency, dropped audio or wrong turn-taking in a real-time pipeline.

## Numbers
- First docker compose up run takes a few minutes; no latency, interruption timing or accuracy numbers are shown. ([2:32](https://youtu.be/ES3HhoYCtIc?t=152))

## Hot takes
- Turn detection and VAD matter more to conversation quality than the architecture (anecdotal, one demo run).
- A graph-based runtime is worth its setup cost only once an agent gets complex. For a simple voice or text agent it is overkill.
- For a fast voice prototype, LiveKit Agents or Pipecat will get there faster than TEN.
- The Deepgram preset is the best of the bundled configs; the XAI presets are weaker for this use case (single-run impression).

## Tools mentioned
TEN Framework (open-source real-time voice agent runtime, version not stated), TEN Manager (visual graph designer), Agora (real-time audio / RTC), Deepgram (speech recognition and TTS preset), OpenAI (LLM in the demo), ElevenLabs (TTS), XAI (alternative preset), Docker Compose, LiveKit Agents (alternative, named by presenter), Pipecat (alternative, named by presenter), Python, C++, Go, Rust, TypeScript (extension languages), SIP telephony, ESP32 hardware, speaker diarization (example configs named)

## Relevance to our work
- **agentos** (1/3): TEN's extension-graph design resembles AgentOS's manifest-toggled pillars, but voice and realtime audio are outside the current AgentOS scope. → *Only if realtime voice traffic enters AgentOS scope, compare TEN's graph-of-extensions with the pillar manifest to see whether the pattern transfers.*
- **prosharness** (1/3): ProsHarness plans phone-driven approvals, and TEN's cancel-on-interrupt model is a relevant pattern if approvals ever become voice-based. → *If ProsHarness adds voice or phone approvals, study how TEN cancels in-flight generation when the user speaks.*
- **general** (1/3): Useful reference for how production voice agents handle barge-in, VAD and turn detection, a pattern that comes up across agent designs. → *Skim the TEN repo's VAD and turn-detection docs before designing any voice-agent feature.*
