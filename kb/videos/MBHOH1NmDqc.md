# Realtime Voice Agents with Frontier Intelligence — Bohan Li, EliseAI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `MBHOH1NmDqc` · [watch](https://youtu.be/MBHOH1NmDqc) · **date:** 2026-09-18 · **length:** 13:14 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Bo (Bohan Li) · **orgs:** EliseAI, Cartesia
- **topics:** voice-multimodal, agent-architecture, inference-serving · **tags:** voice-agents, cascaded-pipeline, streaming-transcription, speculative-generation, background-tool-calls, tts-prefix-cache, latency, eliseai, cartesia

> EliseAI's Bo Li explains a cascaded voice-agent harness (streaming transcription, background tool calls, prefix-cached TTS) that keeps frontier-model intelligence at real-time speed.

## Summary
Bo Li of EliseAI presents how the company built a cascaded voice agent (transcriber, LLM, text-to-speech) that stays fast while using a frontier model. He maps the pipeline onto a self-driving stack: perception is transcription, planning is the LLM, and controls is TTS. The transcriber layers a fast streaming model (Flux) under a slower, more accurate batch model (Scribe V2), and newer text cancels stale corrections. To cut LLM round trips, background agents run tool calls on partial transcripts, the main agent generates early, and speculative output is only emitted once end-of-turn is confirmed. For TTS, a prefix cache replays audio for word sequences already synthesized, and the duplicate Cartesia audio is suppressed so playback stays seamless. A recorded booking call demonstrates the flow, but the talk gives no latency or accuracy benchmarks.

## Key ideas
- **Cascaded voice agents map onto a self-driving-style stack: perception (transcription), planning (LLM), controls (TTS).** — The speaker justifies the cascade, rather than speech-to-speech, by treating each stage like a perception, planning or control module in an autonomous car. This is what lets each stage be tuned on its own. ([0:08](https://youtu.be/MBHOH1NmDqc?t=8))
- **Layer a fast streaming transcriber under an accurate batch transcriber, and let newer text cancel stale corrections.** — A fast model (Flux) gives instant partial text, and the slower, context-aware model (Scribe V2) corrects it. If new text arrives before the accurate pass finishes, the pending correction is cancelled, because more audio beats the older result. ([1:06](https://youtu.be/MBHOH1NmDqc?t=66))
- **Use background tool calls on partial transcripts to avoid extra LLM round trips.** — Each partial transcript can trigger an early LLM generation, but nothing is emitted until end-of-user-turn is confirmed. A background agent does the lookups, and when it finds the data (for example name and date of birth), the speculative generation is cancelled and re-run with the result in context. ([3:55](https://youtu.be/MBHOH1NmDqc?t=235))
- **Tool results are pushed back into the main agent's context so it believes it made the call itself.** — The background agent's output is injected as if the main agent had made the tool call. The speaker also notes that the tool can correct mis-transcriptions by phonetic matching, so the lookup adds intelligence rather than only speed. ([3:55](https://youtu.be/MBHOH1NmDqc?t=235))
- **A prefix cache of already-synthesized audio hides LLM generation time in TTS.** — The cache is keyed on word sequences from the streaming output. It waits for about three words before the first hit, plays cached audio on a miss, and sends the rest to the TTS WebSocket. The user hears a fast response even though the sentence is still being generated. ([6:49](https://youtu.be/MBHOH1NmDqc?t=409))
- **Suppress duplicate TTS audio so the cached prefix and the synthesized sentence join without a seam.** — Cartesia renders the full sentence with natural prosody and has no knowledge of the cache. Because the prefix was already played, the duplicate audio is dropped and the remainder is played after the cached audio finishes. The speaker admits there can be a small hiccup. ([8:12](https://youtu.be/MBHOH1NmDqc?t=492))
- **The talk gives no benchmark numbers, so the latency gains are demonstrated qualitatively through one recorded call.** — The only evidence is the screen-recorded booking call, plus a claim that it feels fast. Treat the speed benefits as the speaker's assertion rather than measured results. ([9:12](https://youtu.be/MBHOH1NmDqc?t=552))

## Techniques
- **Streaming speculative transcription (two-tier ASR)** — Run a fast streaming ASR for instant partial text and a slower, more accurate batch ASR on the same audio. Emit the fast text immediately, and replace it when the accurate pass returns. Cancel the pending correction if new text arrives first. *When:* Voice agents where the LLM needs accurate entities (names, dates) but the user should not wait for batch ASR latency.
- **Early generation with background tool calls and cancellation** — On each partial transcript, start an LLM generation and a background tool lookup. Hold all output until end-of-turn is confirmed. If the background tool returns new data, cancel the speculative generation and re-trigger it with the result. Inject tool results so the main agent sees them as its own calls. *When:* Latency-bound agents whose LLM is slow and whose tool calls are the main cause of round trips, such as slot-filling flows.
- **Word-sequence prefix cache for TTS** — Cache synthesized audio keyed by word sequences from earlier generations. Require a minimum match (here about three words) before using the cache. Play cached audio as the stream starts, and send the uncached remainder to the TTS WebSocket. *When:* Templated or repetitive agent utterances (greetings, confirmations, stock phrases) where the first audio should start before the full LLM output exists.
- **Playback deduplication after speculative TTS** — When the TTS engine re-synthesizes the full sentence, drop the audio for the prefix that was already played from cache, and play only the rest. Schedule the remainder after the cached audio finishes. *When:* Combined with a prefix cache, when the TTS engine has no awareness of that cache and produces full-sentence prosody.

## Numbers
- The prefix cache waits for about three words before its first hit. ([6:49](https://youtu.be/MBHOH1NmDqc?t=409))
- No latency, accuracy, or cost benchmarks are given; the speed claims rest on one recorded booking call. ([9:12](https://youtu.be/MBHOH1NmDqc?t=552))

## Hot takes
- Cascaded STT, LLM, and TTS is still the right design when you need frontier-model intelligence in a voice agent, despite the added pipeline complexity.
- Tool-call round trips, not token generation, are the main latency cost for slow LLM agents, so move them into the background.
- Voice latency is a harness problem more than a model problem: cancellation, prefix caching, and playback stitching do most of the work.

## Tools mentioned
Flux (fast streaming transcriber), Scribe V2 (accurate batch transcriber), Cartesia (TTS with WebSocket support)

## Relevance to our work
- **agentos** (1/3): The speculative-generation and cancel-on-new-context pattern is relevant to latency work in the L1 proxy, but only if AgentOS adds a voice or streaming path. → *Read the talk's cancel-and-retrigger logic before designing any AgentOS streaming path where a speculative generation could commit side effects.*
- **general** (1/3): A clear example of the 'do the slow tool work speculatively and cancel on change' pattern, which applies to any agent harness that waits on tools. → *Keep the background-tool-call-with-cancellation pattern in mind as a latency technique for multi-step agents.*
