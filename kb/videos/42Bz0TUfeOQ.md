# The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `42Bz0TUfeOQ` · [watch](https://youtu.be/42Bz0TUfeOQ) · **date:** 2026-10-06 · **length:** 18:00 · **format:** talk · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Fuad Ali · **orgs:** Arize
- **topics:** observability, voice-multimodal, evals · **tags:** voice agents, tracing, OpenInference, OpenTelemetry, audio evals, LLM-as-judge, session view, time to first audio, interruptions, agent experiments, SRE agent, WebSocket events, Arize

> Arize PM Fuad Ali on why voice agent failures are invisible in transcripts, and how to trace audio sessions, run audio-native evals, and close an observe-evaluate-improve loop. Partly a product pitch, with real open-source instrumentation content.

## Summary
Fuad Ali, a product manager at Arize, argues that voice agents are fragile and hard to debug because transcripts hide what happened on the call. He walks through a refund example where the transcript looks correct but the audio shows a 2.4-second dead-air delay, the agent talking over the caller, and a misheard order number that led to the wrong refund. He proposes a session view that puts audio, transcript, per-turn latency and tool calls in one trace, linked by a session ID. He describes Arize's mapping of realtime WebSocket events onto the open-source OpenInference semantic conventions, so traces from different providers share one queryable schema. He then recommends audio-native evals (tone, interruptions, time to first audio, task success) that run on the audio rather than the transcript, attached to spans and wired to investigation agents. He closes with an observe, evaluate, improve loop, including an SRE-style agent that replays failing traces against a patched endpoint and opens a PR with a latency report. The talk is a vendor pitch, but the failure modes and instrumentation approach are concrete.

## Key ideas
- **Transcripts hide voice-agent failures** — A transcript can look correct while the call went wrong. The example shows a corrected order number in the text, but the audio shows the agent interrupted, misheard the order, and confirmed the wrong refund. Audio-specific problems such as latency, overlap and tone are invisible in text logs. ([1:40](https://youtu.be/42Bz0TUfeOQ?t=100))
- **Debug the whole session, not single turns** — Put audio, transcript, per-turn metrics and tool calls in one trace, grouped by session ID across all turns. Playing audio inline next to the tool call lets you see who spoke when, where the agent paused, and what it called. ([4:05](https://youtu.be/42Bz0TUfeOQ?t=245))
- **Map realtime provider events to one open semantic schema** — Arize mapped WebSocket events for audio input, transcripts, conversation items, responses and token counts onto OpenInference, an open-source OTel-compatible convention. The aim is one queryable schema across OpenAI Realtime, Gemini Live and others, so a new provider does not need bespoke parsing. ([6:06](https://youtu.be/42Bz0TUfeOQ?t=366))
- **Evaluate the audio, not the transcript** — Tone and sentiment, interruptions, transcription drift, time to first audio and task success should be scored from the audio with audio-capable judge models. Speaker says LLM-as-judge on transcripts is only so good. He also points toward agent-as-judge that checks tool and system state, such as whether the agent accessed the right system. ([10:21](https://youtu.be/42Bz0TUfeOQ?t=621))
- **Attach eval scores to spans and trigger investigations** — Live evals on spans let you filter failures by score and see the score next to the exact audio. Monitors on those evals can start investigation agents that look for misrepresented tool calls, uncoded product surfaces or edge cases, and suggest a code or tool change. ([12:38](https://youtu.be/42Bz0TUfeOQ?t=758))
- **Close the loop: observe, evaluate, improve, verify** — The loop is observe (traces), evaluate (scores in line), fix (by a human or an agent), then verify by replaying the failed traces against the fixed endpoint. The example is an agent that finds unbounded tool results overloading context, adds truncation, and checks that latency drops before opening a PR. A human approves or denies. ([13:37](https://youtu.be/42Bz0TUfeOQ?t=817))

## Techniques
- **Session-stitched voice trace view** — Tag every span and WebSocket event with a session ID, then render the full call as one timeline. Add speaker tags (user or assistant) and link inline audio playback, transcript, latency and tool-call spans in the same view. *When:* Debugging a live voice agent where the order of events, interruptions and tool calls matters more than any single transcript line.
- **Provider-agnostic semantic conventions for LLM traffic** — Map each provider's native event stream (here WebSocket realtime events) onto a shared OpenTelemetry-compatible schema covering session lifecycle, audio input, transcript, conversation items, response lifecycle and token counts. Use one auto-instrumenter, so new models only need a new mapping. *When:* Running several model providers, or expecting to swap models, and you need one query surface across all of them.
- **Audio-native evals for tone, latency and interruptions** — Run judge models on the raw audio of each span to score tone or frustration (positive, neutral, negative), time to first audio against an SLA, interruptions and task success. Do not rely on a transcript-only judge. *When:* Voice customer-service agents with latency SLAs or emotional-tone requirements where the transcript loses signal.
- **Online evals on spans with monitors that trigger investigation** — Deploy evals that score live traffic as it arrives, store scores on the relevant spans, and set monitors that launch an investigation agent when scores drop. The agent inspects tool calls and failing spans to propose a fix. *When:* Production agents at a volume where manual review of traces does not scale.
- **Replay failed traces against a patched endpoint to verify a fix** — Capture the traces that failed, apply a candidate fix in dev, replay those same inputs against the fixed endpoint, then trace the replay and compare latency or success before opening a PR with a before/after report. *When:* Validating a fix to an agent that depends on specific failing production conversations, instead of trusting a general test suite.

## Numbers
- 2.4 seconds of dead air before the agent responded to the first user turn (time to first audio problem); the same figure is repeated in the turn-by-turn review. ([3:06](https://youtu.be/42Bz0TUfeOQ?t=186))
- Speaker says Arize can query billions of spans with sub-second latency. This is a vendor claim and was not measured. ([11:41](https://youtu.be/42Bz0TUfeOQ?t=701))
- Speaker's example of an agent introducing a truncation step for tool results. The stated result is a before/after latency report card. No actual figures are given. ([14:57](https://youtu.be/42Bz0TUfeOQ?t=897))

## Hot takes
- The log lies: reading a transcript alone misses most voice-agent failures.
- Voice needs the same observe-evaluate-improve rigor as coding agents; the stakes are lower for a drive-through order but the discipline should be the same.
- Judging a transcript with an LLM is only so good; scoring the underlying audio, or the agent's tool and system state, is the next step.

## Tools mentioned
Arize, OpenInference, OpenTelemetry, Grafana, WebSocket realtime API, GPT Realtime, Gemini Live, LiveKit

## Relevance to our work
- **agentos** (2/3): L4 observability is Prometheus/Grafana/OTel. This talk shows a concrete way to name GenAI and realtime-audio span attributes so one schema covers many providers, and to attach eval scores to spans. → *Compare AgentOS OTel span attributes with OpenInference conventions and consider reusing its names for LLM and audio spans instead of inventing new ones, so exported traces stay compatible with other backends.*
- **prosharness** (1/3): Its replay-failed-traces-against-a-fix pattern is close to ProsHarness checkpoint and resume. The talk applies the same idea to validating fixes on production failures. → *Consider a replay mode that re-runs a failed checkpointed Claude Code run against a candidate harness change and records before/after metrics before any PR is opened.*
