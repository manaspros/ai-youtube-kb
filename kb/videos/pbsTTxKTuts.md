# Developers Might Finally Have a Local TTS Model That Doesn’t Suck

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pbsTTxKTuts` · [watch](https://youtu.be/pbsTTxKTuts) · **date:** 2026-06-02 · **length:** 7:58 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Better Stack, Supertone, ElevenLabs, OpenAI
- **topics:** voice-multimodal, local-ai · **tags:** text-to-speech, local-inference, onnx-runtime, voice-agents, openai-compatible-api, supertonic, python, cpu-inference

> Hands-on test of Supertonic 3, a 99M-parameter local TTS model: fast and easy to deploy, but it mangles prices, dates and expression tags, so test your own app text first.

## Summary
The Better Stack presenter argues that cloud TTS has three hidden costs (per-call money, network latency, and privacy because text leaves the device) and that earlier local TTS models are often too big, need a GPU, start slowly, or break on real app text. He runs Supertonic 3, a local on-device TTS model from Supertone, through a small Python harness. Normal English and sample Arabic, French and Korean sound clean, and local generation is very fast, though no timings are shown. Numbers are the failure case: a sentence with an invoice total, decimal prices and a June 2026 date reads badly, and expression tags (laugh, breath, sigh) are only available through a paid API key. Deployment is the strength: pip install, a Python SDK, a CLI, and a local HTTP server with an OpenAI-compatible speech endpoint, so an app that already speaks the OpenAI speech API can be pointed at it. His verdict is to try it for local voice agents and private desktop apps, but skip it for expressive narration or easy voice cloning, and run your own tests on invoices, tickets, markdown and long paragraphs.

## Key ideas
- **Cloud TTS has three hidden costs: money per call, latency, and privacy** — Every request sends text off the device, every user action becomes an API call, and the speech bill grows with the app. The presenter says this matters most for voice agents that send text to a third-party server. ([0:00](https://youtu.be/pbsTTxKTuts?t=0))
- **Earlier local TTS models tend to fail on real app text** — He lists the problems: huge files, a need for a GPU, slow starts, and models that sound fine on clean demo sentences but break on money, dates, phone numbers, times and odd formatting. ([1:11](https://youtu.be/pbsTTxKTuts?t=71))
- **Supertonic 3 fails the messy-text test on numbers** — A test sentence with an invoice total, decimal prices and a June 2026 date was read badly. He calls the local version's handling of prices and numbers bad, and says it was the failure that mattered most to him. ([2:25](https://youtu.be/pbsTTxKTuts?t=145))
- **Supertonic 3 is small and CPU-only, with broad language coverage** — The model has about 99M parameters, runs on CPU through ONNX Runtime with no GPU, cloud server or API key, and supports 31 languages. The Arabic, French and Korean samples sounded clean to a presenter who does not speak them. ([3:29](https://youtu.be/pbsTTxKTuts?t=209))
- **Expression tags are paywalled** — Version 3 supports style tags such as laugh, breath and sigh, but they require a paid API key, so the free local version does not give expressive speech. ([4:37](https://youtu.be/pbsTTxKTuts?t=277))
- **Deployment is the real strength: an OpenAI-compatible local server** — The package offers a Python SDK, a CLI and a local HTTP server with an OpenAI-compatible v1 audio speech alias. An app that already expects the OpenAI speech API can be pointed at the local server without redesigning its client code. Example clients are included for browser, Java, C++ and C#. ([5:35](https://youtu.be/pbsTTxKTuts?t=335))
- **Verdict: good for local voice agents, not for expressive narration** — He suggests it for local voice agents, desktop apps and cached local setups. He would skip it for narration that needs emotion or for easy voice cloning, and says to test your own invoices, tickets, markdown and long paragraphs before committing. ([6:34](https://youtu.be/pbsTTxKTuts?t=394))

## Techniques
- **Stress-test TTS with production-shaped strings** — Build a fixed set of strings like the app would produce: currency with cents, a due date, a phone number, a clock time, and a short invoice sentence. Synthesize each one and listen for mispronounced numbers and dates. Run the same set against every candidate model before choosing one. The video shows a simple balance-due sentence and a multi-number invoice sentence as the test cases. *When:* Before picking any TTS model for an app that speaks data (billing, notifications, support replies) rather than prose.
- **Side-by-side demo harness for a TTS model** — Install with pip install supertonic. Create a TTS object, put the voice and voice-style settings and the demo texts into plain Python data structures, and pass each demo's keyword arguments to the TTS object's synthesize method. Run the demos in a loop. The video does not show the exact API names or arguments on screen. *When:* Quick local evaluation of a TTS model across languages, voices and tricky input before wiring it into an app.
- **Point an OpenAI-style speech client at a local server** — Run the local HTTP server that ships with the package. It exposes an OpenAI-compatible v1 audio speech alias, so an existing client using the OpenAI speech API only needs its base URL changed. The video does not show the exact command, port or model name. *When:* Moving an app that already calls a cloud speech API onto a local model for testing or privacy, without rewriting the client.

## Numbers
- Supertonic 3 model size is about 99 million parameters ([3:29](https://youtu.be/pbsTTxKTuts?t=209))
- Supertonic 3 supports 31 languages and runs on CPU through ONNX Runtime, with no GPU or API key needed for basic speech ([3:29](https://youtu.be/pbsTTxKTuts?t=209))
- Test sentence for a balance due: $12,575 due June 15th, call by 5:30 PM ([1:11](https://youtu.be/pbsTTxKTuts?t=71))
- Invoice test sentence: $12,000 for $58.75 due June 15, 2026, which the presenter says read badly ([2:25](https://youtu.be/pbsTTxKTuts?t=145))
- Local generation is described as very fast, but no latency or real-time-factor figures are given ([3:29](https://youtu.be/pbsTTxKTuts?t=209))
- Video runtime is 7:58; the presenter gives no benchmark, cost or accuracy numbers ([0:00](https://youtu.be/pbsTTxKTuts?t=0))

## Hot takes
- The presenter calls the paywalled expression tags a dealbreaker, saying the API key is what turns him off.
- A fast, CPU-only model that handles normal text well still fails the numbers test, which is the case that matters most for app-generated speech.
- Local TTS is practical for voice agents and privacy-first desktop apps, but its quality cannot be judged from demo sentences. The author's own verdict is to test your own ugly text first.
- Claims about speed are qualitative only ("insanely fast"), with no timings, so the speed claim cannot be checked from the video.
- Not sponsored; the subscribe prompts are light. The value is one hands-on test with honest negatives, but there is no methodology or repeated trials.

## Tools mentioned
Supertonic / Supertonic 3 (Supertone, on-device TTS, 99M parameters, 31 languages), supertonic (pip package: Python SDK, CLI, local HTTP server), ONNX Runtime (CPU inference), Python, OpenAI audio speech API (compatible local endpoint; cloud comparison), ElevenLabs ("11 Labs" in the transcript; cloud comparison), Java, C++, C# and browser example clients

## Relevance to our work
- **agentos** (1/3): AgentOS is an OpenAI-compatible proxy for self-hosted agents, so a local OpenAI-style speech endpoint would fit the same pattern. Voice is not on the current roadmap, and the video shows that the number-reading failures are unresolved. → *Only if voice agents come into scope: test a local OpenAI-style speech server against production-shaped strings (currency, dates, phone numbers) before routing audio through the proxy.*
